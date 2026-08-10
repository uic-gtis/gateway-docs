"""Post-conversion checks. Exits non-zero on any failure.

    python tools/verify.py

Checks: no XWiki markup survived, code fences balance, every relative link and #anchor
resolves, every asset is present and referenced, and nothing credential-shaped is about
to be published.
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"tools", ".git", "images", "files"}

XWIKI_LEFTOVERS = [
    (r"\{\{[a-zA-Z/]", "xwiki macro"),
    (r">>doc:|>>url:|>>attach:", "xwiki link target"),
    (r"\(%\s|\(%%\)", "xwiki parameter block"),
    (r"\x00", "unresolved converter placeholder"),
    (r"^=+ .* =+\s*$", "xwiki heading"),
]

SECRET_PATTERNS = [
    (r"(?i)\b(api[_-]?key|secret|token|passwd)\s*[:=]\s*[\"']?[A-Za-z0-9/+_-]{16,}", "credential-shaped"),
    (r"(?i)\bpassword\"?\s*[:=]\s*[\"'](?![^\"']*(?:string|password|characters|\.\.\.|xxx|\*))"
     r"[^\"']{8,}[\"']", "password literal"),
    # Private IPs, but not the dotted runs inside identifiers like
    # "IL-TESTTIMS-INCIDENT.2023.10.18.12.5972095".
    (r"(?<![\d.])(?:10|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}(?![\d.])", "private IP"),
]

# Documentation placeholders that look credential-shaped but are not.
SECRET_ALLOW = re.compile(
    r"(?i)newPassword|SecureP@ssword123|userPassword123|your[-_ ]?password|<password>|"
    r"\[password\]|examplePassword|plaintext_password|plain text|new_password|"
    r"check-this|192\.168\.1\.(?:1|20)\b|•")   # • = a masked "••••••••"

# Real e-mail addresses are legitimate in contact sections, but this repo is public, so
# every non-placeholder address is reported for a human to confirm.
EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
EMAIL_PLACEHOLDER = re.compile(
    r"(?i)@(?:travelmidwest\.com|example\.com|doe\.com|this\.com|reset\.com|"
    r"email\.com|newemail\.com|domain\.com|test\.com)$")


def md_files():
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP_DIRS and not d.startswith(".")]
        for f in sorted(fn):
            if f.endswith(".md"):
                yield Path(dp) / f


def gh_slug(text):
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    return re.sub(r"\s+", "-", s)


def strip_code(text):
    """Blank out fenced code so checks do not fire on JSON/XML samples."""
    out, fence = [], None
    for line in text.split("\n"):
        m = re.match(r"^(`{3,})", line)
        if fence is None and m:
            fence = m.group(1)
            out.append("")
            continue
        if fence is not None:
            if m and m.group(1).startswith(fence):
                fence = None
            out.append("")
            continue
        out.append(line)
    return "\n".join(out)


def slugs_of(text):
    seen, table = {}, set()
    for line in strip_code(text).split("\n"):
        m = re.match(r"^#{1,6}\s+(.*?)\s*$", line)
        if not m:
            continue
        h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", m.group(1))     # links -> text
        h = re.sub(r"[`*_]", "", h)
        base = gh_slug(h)
        k = seen.get(base, 0)
        seen[base] = k + 1
        table.add(base if k == 0 else "%s-%d" % (base, k))
    return table


def main():
    files = list(md_files())
    text = {p: p.read_text(encoding="utf-8") for p in files}
    fails = []

    # 1. no XWiki markup survived
    for p, t in text.items():
        body = strip_code(t)
        for pat, what in XWIKI_LEFTOVERS:
            for m in re.finditer(pat, body, re.M):
                fails.append("%s: %s left over: %r"
                             % (p.relative_to(ROOT), what, m.group(0)[:60]))

    # 2. code fences balance
    for p, t in text.items():
        if t.count("\n```") % 2:
            fails.append("%s: odd number of code fences" % p.relative_to(ROOT))

    # 3. links resolve
    slug_cache = {p: slugs_of(t) for p, t in text.items()}
    n_links = 0
    for p, t in text.items():
        for m in re.finditer(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)\)", strip_code(t)):
            tgt = m.group(1)
            if re.match(r"^(https?|mailto|ftp):", tgt):
                continue
            n_links += 1
            path, _, anchor = tgt.partition("#")
            dest = p if not path else (p.parent / path).resolve()
            if not dest.exists():
                fails.append("%s: dead link -> %s" % (p.relative_to(ROOT), tgt))
                continue
            if anchor and dest.suffix == ".md":
                if anchor not in slug_cache.get(dest, slugs_of(dest.read_text(encoding="utf-8"))):
                    fails.append("%s: anchor not found -> %s" % (p.relative_to(ROOT), tgt))

    # 4. images / attachments present and referenced
    referenced, n_img = set(), 0
    for p, t in text.items():
        for m in re.finditer(r"!\[[^\]]*\]\(([^)\s]+)\)", t):
            n_img += 1
            dest = (p.parent / m.group(1)).resolve()
            referenced.add(dest)
            if not dest.exists():
                fails.append("%s: missing image -> %s" % (p.relative_to(ROOT), m.group(1)))
        for m in re.finditer(r"\[[^\]]*\]\(([^)\s]*files/[^)\s]+)\)", t):
            referenced.add((p.parent / m.group(1)).resolve())
    for d in ("images", "files"):
        for f in (ROOT / d).glob("*"):
            if f.resolve() not in referenced:
                fails.append("%s/%s is not referenced by any document" % (d, f.name))
            elif f.stat().st_size == 0:
                fails.append("%s/%s is empty" % (d, f.name))

    # 5. nothing credential-shaped
    review = []
    for p, t in text.items():
        for line in t.split("\n"):
            if not SECRET_ALLOW.search(line):
                for pat, what in SECRET_PATTERNS:
                    m = re.search(pat, line)
                    if m:
                        fails.append("%s: possible %s: %r"
                                     % (p.relative_to(ROOT), what, m.group(0)[:70]))
            for m in EMAIL_RE.finditer(line):
                if not EMAIL_PLACEHOLDER.search(m.group(0)):
                    review.append("%s: %s" % (p.relative_to(ROOT), m.group(0)))

    print("%d markdown files, %d internal links, %d images checked"
          % (len(files), n_links, n_img))
    if review:
        print("\nFOR HUMAN REVIEW - real e-mail addresses in a public repo:")
        for r in sorted(set(review)):
            print("   ", r)
    if fails:
        print("\n%d PROBLEM(S):" % len(fails))
        for f in fails:
            print("   ", f)
        return 1
    print("all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
