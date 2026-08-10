"""Convert the GTIS XWiki 2.1 documentation dumps to GitHub-Flavored Markdown.

Run tools/fetch_wiki_meta.py first; this script is then fully offline.

    python tools/xwiki2md.py

Exits non-zero if any link could not be resolved, rather than silently emitting a
dead link.

Design notes
------------
* Line-oriented state machine. Nothing inside a ``{{code}}`` block is ever touched by
  an inline rule -- that is the single most important invariant here, because the
  corpus is 286 code blocks of JSON/XML full of characters that look like markup.
* Anchors are resolved in two passes. Pass 1 turns ``anchor="HFooBar"`` into a
  placeholder carrying the *heading text* (looked up in wiki-meta.json). Pass 2, once
  every file's headings are known, turns that into a real GitHub slug with the correct
  duplicate suffix. Doing it in one pass cannot get duplicates right.
* Tables may contain multi-line cells (XWiki ``(((`` groups). GFM has no such thing, so
  those collapse to ``<br>``.
"""

import json
import re
import sys
from pathlib import Path

SRC = Path(r"D:\IntellJ-Workspace\gateway\docs\Web Services")
ROOT = Path(__file__).resolve().parent.parent
META_PATH = Path(__file__).resolve().parent / "wiki-meta.json"

# ---------------------------------------------------------------- naming

SLUG_OVERRIDE = {
    "cameraInfo.csv": "camera-info-csv",
    "dmsInfo.csv": "dms-info-csv",
    "incidentInfo.csv": "incident-info-csv",
    "travelTimeService.json": "travel-time-service-json",
    "XMl Upload Manual": "xml-upload-manual",
    "GTIS Smart Work Zone Specifications for Construction Contractors and Vendors":
        "gtis-smart-work-zone-specifications",
}

# doc: targets that have no page of their own in this repo.
REF_OVERRIDE = {
    # The XML Reference was copy/pasted into the user guide as an inline section.
    "User-Guides-Manuals.Gateway-External-Interface-User-Guide.Gateway-XML-Reference.WebHome":
        ("user-guides-and-manuals/gateway-external-interface-user-guide.md",
         "Gateway XML Reference"),
    # An old all-in-one export of what is now the Gateway API section.
    "User-Guides-Manuals.JSON-Traffic-Information-Download-Manual-all-in-one.WebHome":
        ("gateway-api/README.md", None),
}

# Custom {{id name="..."/}} anchors: name -> the heading text they sit under.
CUSTOM_ANCHOR = {"bbox": "Bounding Box"}

# Images the source pages reference but that no longer exist on the wiki: the rendered
# page links to them and gets a 404, and the owning page reports zero attachments.
# Lost upstream (these pages predate the Confluence -> XWiki migration). Emitting a
# marker keeps the loss visible instead of shipping a broken image.
MISSING_IMAGES = {
    "DMS.2019-2-25_12-18-5.382x200.png",
    "image2017-11-6_8-36-5.png",
    "image2017-11-6_8-38-10.png",
}

GTIS_CONTACT = ("- Contact [support@travelmidwest.com]"
                "(mailto:support@travelmidwest.com?subject=%s) and the GTIS team will "
                "put you in touch with the vendor.")

# This repository is public. The source wiki names individual third-party vendor staff
# and gives their direct work e-mail and phone number; those are replaced with the GTIS
# team address. Each rule must match, or the conversion fails loudly -- a redaction that
# silently stops matching after an upstream edit would leak the details it exists to
# remove.
REDACTIONS = [
    ("user-guides-and-manuals/gtis-smart-work-zone-specifications.md",
     r"- Mike Granger \(\[mgranger@[^\n]*\n",
     GTIS_CONTACT % "GTIS%20Smart%20Work%20Zone%20%2F%20JamLogic" + "\n"),
    ("user-guides-and-manuals/gtis-smart-work-zone-specifications.md",
     r"- Adam Kovar\n(?:.*\n)*?[^\n]*r\.sheckler@iconeproducts\.com[^\n]*\)\n",
     GTIS_CONTACT % "GTIS%20Smart%20Work%20Zone%20%2F%20iConeTraffic" + "\n"),
]


def redact(out_path, md):
    """Apply the redactions for one output file; returns (text, rules_that_missed)."""
    missed = []
    for path, pat, repl in REDACTIONS:
        if path != out_path:
            continue
        md, n = re.subn(pat, repl, md)
        if not n:
            missed.append(pat)
    return md, missed


ADMIN_BANNER = """> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.
"""

LANG_FIX = {"js": "javascript", "json": "json", "none": "", "console": "console",
            "http": "http", "xml": "xml", "java": "java", "html": "html",
            "typescript": "typescript", "python": "python", "perl": "perl",
            "bash": "bash", "csv": "csv", "javascript": "javascript"}


def file_slug(stem):
    if stem in SLUG_OVERRIDE:
        return SLUG_OVERRIDE[stem]
    s = re.sub(r"[^\w\s-]", "", stem).strip().lower()
    return re.sub(r"[\s_]+", "-", s)


def untilde(s):
    """Undo XWiki's escape character. Stored double-escaped, so "~~/" means "/"."""
    return s.replace("~~/", "/").replace("~/", "/").replace("~~", "~")


def gh_slug(text):
    """GitHub's heading-anchor algorithm (pre-dedup)."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    return re.sub(r"\s+", "-", s)


def out_path_for(rel):
    """docs/Web Services relative path -> repo-relative .md path."""
    p = Path(rel)
    stem = p.stem
    parts = list(p.parts[:-1])
    # A page whose stem matches a sibling directory is that section's index page.
    if (SRC.joinpath(*parts, stem)).is_dir():
        return "/".join([file_slug(x) for x in parts] + [file_slug(stem), "README.md"])
    return "/".join([file_slug(x) for x in parts] + [file_slug(stem) + ".md"])


# ---------------------------------------------------------------- inline

PH = "\x00PH%d\x00"


class Inline:
    """Inline converter for one document. Collects link problems as it goes."""

    def __init__(self, doc):
        self.doc = doc

    # -- links ---------------------------------------------------------
    def _link(self, m):
        inner = m.group(1)
        if inner.startswith("image:"):
            return self._image(inner[len("image:"):])

        if ">>" in inner:
            label, target = inner.split(">>", 1)
        else:
            label, target = None, inner
        label = (label or "").strip()

        parts = target.split("||")
        target = parts[0].strip()
        params = "||".join(parts[1:])
        am = re.search(r'anchor="([^"]*)"', params)
        anchor = am.group(1) if am else None

        href, anchor_owner = self._resolve(target, anchor)
        if href is None:
            return m.group(0)  # left as-is; recorded as a problem already

        if anchor:
            href += self._anchor_ph(anchor_owner, anchor)

        if not label:
            label = target.split(":", 1)[-1] or href
        # The label is stashed before the document-level unescape runs, so undo the
        # tilde escaping here or a URL-shaped label keeps its "https:~~/~~/".
        return "[%s](%s)" % (self.esc_label(untilde(label)), href)

    def _resolve(self, target, anchor):
        """Return (href, page-rel-path-that-owns-the-anchor)."""
        if target.startswith("url:"):
            return target[4:], None
        if re.match(r"^(https?|ftp):", target):
            return target, None
        if target.startswith("mailto:"):
            return re.sub(r"^mailto:(mailto:)?", "mailto:", target), None
        if target.startswith("attach:"):
            name = target[len("attach:"):]
            self.doc.assets_used.add(("attach", name))
            return self.doc.rel_to("files/" + name), None
        if target.startswith("doc:"):
            ref = target[4:].strip()
            if not ref:  # [[L>>doc:||anchor="x"]] - same page
                return "", self.doc.rel
            return self._resolve_doc(ref)
        if not target:
            return "", self.doc.rel
        # A bare reference with no scheme, e.g. [[Space.Page.WebHome]]
        return self._resolve_doc(target)

    def _resolve_doc(self, ref):
        if ref in REF_OVERRIDE:
            path, forced = REF_OVERRIDE[ref]
            if forced:
                return self.doc.rel_to(path) + "#" + PH % self.doc.push(
                    ("anchor_text", path, forced)), None
            return self.doc.rel_to(path), path
        tgt = self.doc.by_ref.get(ref)
        if tgt is None:
            self.doc.problems.append("unresolved doc: link -> %s" % ref)
            return None, None
        if tgt == self.doc.rel:
            return "", self.doc.rel
        return self.doc.rel_to(self.doc.out_for[tgt]), tgt

    def _anchor_ph(self, owner_rel, anchor):
        """Placeholder for '#slug'; resolved in pass 2 once headings are known."""
        if owner_rel is None:
            return "#" + anchor
        text = CUSTOM_ANCHOR.get(anchor)
        if text is None:
            text = self.doc.meta.get(owner_rel, {}).get("anchors", {}).get(anchor)
        if text is None:
            self.doc.problems.append(
                "unknown anchor %r in %s" % (anchor, owner_rel))
            return "#" + gh_slug(anchor)
        return "#" + PH % self.doc.push(
            ("anchor_text", self.doc.out_for[owner_rel], text))

    def _image(self, inner):
        name = inner.split("||")[0].strip()
        if name in MISSING_IMAGES:
            return ("<!-- TODO(docs): image %r is referenced here but the attachment no "
                    "longer exists on the source wiki (404) -->" % name)
        self.doc.assets_used.add(("image", name))
        return "![%s](%s)" % (name, self.doc.rel_to("images/" + name))

    @staticmethod
    def esc_label(s):
        return s.replace("[", "\\[").replace("]", "\\]")

    # -- main ----------------------------------------------------------
    def run(self, s, in_table=False):
        keep = []

        def stash(text):
            keep.append(text)
            return PH % self.doc.push(("literal", len(keep) - 1, keep))

        # 1. inline {{code}}x{{/code}} and ##x## become backticked literals.
        s = re.sub(r"\{\{code(?:\s[^}]*)?\}\}(.*?)\{\{/code\}\}",
                   lambda m: stash("`%s`" % m.group(1)), s)
        s = re.sub(r"(?<!#)##(?!#)(.+?)(?<!#)##(?!#)",
                   lambda m: stash("`%s`" % m.group(1)), s)
        # 2. links and images.
        s = re.sub(r"\[\[(.+?)\]\]", lambda m: stash(self._link(m)), s)
        # 3. drop styling parameter blocks.
        s = re.sub(r"\(%.*?%\)", "", s)
        # 4. tilde escapes. The wiki stores these double-escaped, so ~~/ means /.
        s = untilde(s)
        # 5. italics -- must not fire on the // of a URL.
        s = re.sub(r"(?<![:\w/])//(?=\S)(.+?)(?<=\S)//(?!/)", r"*\1*", s)
        # 6. GFM table cells cannot contain a raw pipe.
        if in_table:
            s = s.replace("|", "\\|")
        return s


# ---------------------------------------------------------------- document

CODE_ANY = re.compile(r"\{\{code(\s[^}]*)?\}\}")
ALERT_OPEN = re.compile(r"^\{\{(info|warning|error|success|note)\}\}\s*$")
HEADING = re.compile(r"^(={1,6})\s+(.*?)\s+\1\s*$")
BULLET = re.compile(r"^(\*+)\s+(.*)$")
NUMBER = re.compile(r"^(1+)[.)]\s+(.*)$")
PARAM_LINE = re.compile(r"^\(%.*?%\)\s*")
DIAGRAM = re.compile(r"\{\{diagram\b[^}]*\}\}")
NAV_MACRO = re.compile(r"\{\{(children|documentTree)\b[^}]*\}\}")
INCLUDE = re.compile(r"\{\{include\b[^}]*\}\}")

# {{include}} pulls a shared snippet page. There is exactly one in the corpus; this is
# the text the wiki actually renders for it.
INCLUDE_TEXT = {
    "HAPI": ("Please note that the API described herein — along with the data "
             "provided by it — are subject to change at any time without notice, "
             "therefore we cannot provide guarantees as to the availability and/or "
             "suitability for use in third-party applications."),
}
ALERT_KIND = {"info": "NOTE", "note": "NOTE", "warning": "WARNING",
              "error": "CAUTION", "success": "TIP"}


def diagram_key(reference):
    r = reference.strip()
    if r.endswith(".WebHome"):
        r = r[: -len(".WebHome")]
    return re.split(r"(?<!\\)\.", r)[-1].replace("\\.", ".")


class Doc:
    def __init__(self, rel, meta, by_ref, out_for, diagrams):
        self.rel = rel
        self.meta = meta
        self.by_ref = by_ref
        self.out_for = out_for
        self.diagrams = diagrams
        self.out = out_for[rel]
        self.problems = []
        self.assets_used = set()
        self.headings = []
        self.slots = []
        self.diagram_index = 0
        self.svg_out = {}
        self.inline = Inline(self)

    def push(self, payload):
        self.slots.append(payload)
        return len(self.slots) - 1

    def rel_to(self, repo_path):
        """Repo-root-relative path -> path relative to this document."""
        from os.path import relpath
        base = Path(self.out).parent.as_posix() or "."
        r = relpath(repo_path, base).replace("\\", "/")
        return r

    # -- block level ---------------------------------------------------
    def convert(self, text):
        lines = text.replace("\r\n", "\n").split("\n")
        out, i, n = [], 0, len(lines)
        while i < n:
            line = lines[i]
            stripped = line.strip()

            # floating TOC box -> dropped; GitHub renders its own outline
            if stripped.startswith('(% class="box floatinginfobox"'):
                i += 1
                if i < n and lines[i].strip() == "(((":
                    depth = 1
                    i += 1
                    while i < n and depth:
                        depth += lines[i].count("(((") - lines[i].count(")))")
                        i += 1
                continue
            if stripped in ("{{toc/}}", "{{toc}}", "{{/toc}}"):
                i += 1
                continue

            # {{box}} wraps a floating table-of-contents; GitHub renders its own
            if stripped.startswith("{{box"):
                i += 1
                while i < n and lines[i].strip() != "{{/box}}":
                    i += 1
                i += 1
                continue

            # {{{ verbatim }}}
            if stripped.startswith("{{{") and stripped.endswith("}}}"):
                inner = stripped[3:-3]
                out += ["```", inner, "```", ""]
                i += 1
                continue

            # fenced code. The macro is not always alone on its line -- one block is
            # wrapped in ** ** -- so match anywhere and keep whatever surrounds it.
            m = CODE_ANY.search(line)
            if m and "{{/code}}" not in line[m.end():]:
                attrs = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1) or ""))
                lang = LANG_FIX.get((attrs.get("language") or "").lower(),
                                    (attrs.get("language") or "").lower())
                title = (attrs.get("title") or "").strip().strip("=").strip()
                prefix, tail = line[:m.start()], ""
                head_frag = line[m.end():]
                body = [head_frag] if head_frag.strip() else []
                i += 1
                while i < n and "{{/code}}" not in lines[i]:
                    body.append(lines[i])
                    i += 1
                if i < n:
                    close = lines[i]
                    ci = close.index("{{/code}}")
                    if close[:ci].strip():
                        body.append(close[:ci])
                    tail = close[ci + len("{{/code}}"):]
                    i += 1
                while body and not body[0].strip():
                    body.pop(0)
                while body and not body[-1].strip():
                    body.pop()
                if title:
                    out += ["**%s**" % title, ""]
                if prefix.strip(" *_/"):
                    out += [self.inline.run(prefix).rstrip(), ""]
                fence = "```"
                while any(l.startswith(fence) for l in body):
                    fence += "`"
                out += [fence + lang] + body + [fence, ""]
                if tail.strip(" *_/"):
                    out += [self.inline.run(tail).lstrip(), ""]
                continue

            # alert blocks
            m = ALERT_OPEN.match(stripped)
            if m:
                kind = ALERT_KIND[m.group(1)]
                body = []
                i += 1
                while i < n and lines[i].strip() != "{{/%s}}" % m.group(1):
                    body.append(lines[i])
                    i += 1
                i += 1
                inner = self.convert("\n".join(body)).strip("\n").split("\n")
                out.append("> [!%s]" % kind)
                out += ["> " + x if x.strip() else ">" for x in inner]
                out.append("")
                continue

            # diagrams -- the macro only stores draw.io XML, so we use the SVG the
            # wiki server rendered for it (captured in wiki-meta.json, in page order).
            if DIAGRAM.search(line):
                out += [DIAGRAM.sub(lambda mm: self.render_diagram(mm.group(0)),
                                    line).strip(), ""]
                i += 1
                continue

            # navigation macros -> generated child index (filled in pass 2)
            if NAV_MACRO.search(line):
                out.append(PH % self.push(("child_index",)))
                i += 1
                continue

            m = INCLUDE.search(line)
            if m:
                sec = re.search(r'section="([^"]*)"', m.group(0))
                text = INCLUDE_TEXT.get(sec.group(1) if sec else "")
                if text is None:
                    self.problems.append("unhandled {{include}}: %s" % m.group(0))
                    text = ""
                out += [text, ""]
                i += 1
                continue

            # tables
            if stripped.startswith("|"):
                rows, i = self.read_table(lines, i)
                out += self.render_table(rows) + [""]
                continue

            # headings
            m = HEADING.match(line)
            if m:
                text = self.inline.run(re.sub(r"\{\{id\b[^}]*\}\}", "", m.group(2))).strip()
                self.headings.append(text)
                # Demoted one level: the page title becomes the document's only H1.
                # GitHub slugs depend on heading text, not level, so anchors are safe.
                out += ["", "#" * min(len(m.group(1)) + 1, 6) + " " + text, ""]
                i += 1
                continue

            if re.match(r"^-{4,}\s*$", stripped):
                out += ["", "---", ""]
                i += 1
                continue

            # strip a leading styling block, then fall through
            if PARAM_LINE.match(line):
                line = PARAM_LINE.sub("", line, count=1)
                stripped = line.strip()
                if not stripped:
                    i += 1
                    continue

            if stripped in ("(((", ")))"):
                i += 1
                continue

            m = BULLET.match(stripped)
            if m:
                out.append("  " * (len(m.group(1)) - 1) + "- " + self.inline.run(m.group(2)))
                i += 1
                continue
            m = NUMBER.match(stripped)
            if m:
                out.append("  " * (len(m.group(1)) - 1) + "1. " + self.inline.run(m.group(2)))
                i += 1
                continue

            out.append(self.inline.run(line).rstrip())
            i += 1

        return "\n".join(out)

    def render_diagram(self, macro):
        """A {{diagram}} macro -> an <img> at the SVG the wiki server rendered for it."""
        ref = re.search(r'reference="([^"]*)"', macro)
        label = diagram_key(ref.group(1)) if ref else "diagram"
        pretty = re.sub(r"(?<!^)(?=[A-Z])", " ", label).strip()
        name = file_slug(pretty)
        svg = self.diagrams.get(label)
        if svg:
            self.svg_out[name] = svg
        else:
            self.problems.append("no rendered SVG for diagram %r" % label)
        return "![%s](%s)" % (pretty, self.rel_to("images/" + name + ".svg"))

    # -- tables --------------------------------------------------------
    @staticmethod
    def read_table(lines, i):
        rows, n = [], len(lines)
        while i < n and lines[i].startswith("|"):
            row = lines[i]
            depth = row.count("(((") - row.count(")))")
            i += 1
            while depth > 0 and i < n:
                row += "\n" + lines[i]
                depth += lines[i].count("(((") - lines[i].count(")))")
                i += 1
            rows.append(row)
        return rows, i

    def split_cells(self, row):
        # Protect [[...]] so their || parameter separators survive the split.
        held = []
        row = re.sub(r"\[\[.+?\]\]", lambda m: held.append(m.group(0)) or "\x01%d\x01" % (len(held) - 1), row, flags=re.S)
        cells, header = [], row.lstrip("|").startswith("=")
        for raw in row.lstrip("|").split("|"):
            c = raw.lstrip("=")
            c = re.sub(r"\(%.*?%\)", "", c)
            c = c.replace("(((", "").replace(")))", "")
            c = re.sub(r"\x01(\d+)\x01", lambda m: held[int(m.group(1))], c)
            # A cell can hold macros too; GFM tables have no block constructs, so an
            # alert becomes a bold lead-in rather than a callout.
            c = DIAGRAM.sub(lambda mm: self.render_diagram(mm.group(0)), c)
            c = re.sub(r"\{\{(info|note)\}\}", "**Note:** ", c)
            c = re.sub(r"\{\{warning\}\}", "**Warning:** ", c)
            c = re.sub(r"\{\{error\}\}", "**Caution:** ", c)
            c = re.sub(r"\{\{success\}\}", "**Tip:** ", c)
            c = re.sub(r"\{\{/(info|note|warning|error|success)\}\}", "", c)
            c = re.sub(r"\n\s*\n", "\n", c.strip())
            c = "<br>".join(x.strip() for x in c.split("\n") if x.strip())
            cells.append(self.inline.run(c, in_table=True).strip())
        return header, cells

    def render_table(self, rows):
        parsed = [self.split_cells(r) for r in rows]
        width = max(len(c) for _, c in parsed)
        body = [c + [""] * (width - len(c)) for _, c in parsed]
        if parsed and parsed[0][0]:
            head, body = body[0], body[1:]
        else:
            head = [""] * width
        return (["| " + " | ".join(head) + " |",
                 "|" + "|".join([" --- "] * width) + "|"]
                + ["| " + " | ".join(r) + " |" for r in body])


# ---------------------------------------------------------------- indexes

SECTION_BLURB = {
    "gateway-api": "JSON and GeoJSON endpoints serving live traffic data — travel "
                   "times, incidents, cameras, dynamic message signs, work zones, "
                   "truck parking and more.",
    "gateway-api/admin": "Privileged endpoints for administering GTIS content and "
                         "user accounts.",
    "gateway-api/user-api": "Account and authentication endpoints for the various "
                            "kinds of GTIS user.",
    "user-guides-and-manuals": "Longer-form guides for publishing data to, and "
                               "receiving data from, the Gateway.",
}

ROOT_README = """# GTIS API Documentation

Public documentation for the **Gateway Traffic Information System** (GTIS), the traffic
data platform behind [travelmidwest.com](https://travelmidwest.com). GTIS aggregates
real-time traffic information — travel times, incidents, construction, dynamic message
signs, cameras, truck parking and weather — from transportation agencies across
Illinois and neighbouring states, and republishes it through the APIs documented here.

> [!NOTE]
> The APIs described here, and the data they serve, may change at any time without
> notice. We cannot guarantee their availability or their suitability for use in
> third-party applications.

## Contents

%s

---

These documents were migrated from the internal GTIS wiki. This repository is now the
authoritative copy — please open a pull request here rather than editing the wiki.
"""


DIR_TITLE = {
    "gateway-api": "Gateway API",
    "gateway-api/admin": "Admin",
    "gateway-api/user-api": "User API",
    "user-guides-and-manuals": "User Guides and Manuals",
}


def dir_title(dirpath):
    return DIR_TITLE.get(dirpath, dirpath.rsplit("/", 1)[-1].replace("-", " ").title())


def build_indexes(final, title_by_out):
    """Generate the pages that have no wiki source: the root and section indexes."""
    from os.path import relpath

    def entries(dirpath):
        """Docs in a directory, plus the index page of each subdirectory."""
        out = []
        for o in final:
            p = Path(o)
            parent = p.parent.as_posix()
            if p.name != "README.md" and parent == dirpath:
                out.append(o)
            elif p.name == "README.md" and p.parent.parent.as_posix() == dirpath:
                out.append(o)
        return sorted(out, key=lambda o: title_by_out.get(o, Path(o).parent.name).lower())

    def bullets(dirpath, base):
        return "\n".join(
            "- [%s](%s)" % (title_by_out.get(o, Path(o).parent.name.replace("-", " ").title()),
                            relpath(o, base).replace("\\", "/"))
            for o in entries(dirpath))

    made = {}

    # A section directory that had no wiki index page of its own.
    for dirpath in {Path(o).parent.as_posix() for o in final}:
        if dirpath in (".", "images", "files") or dirpath + "/README.md" in final:
            continue
        body = "# %s\n" % dir_title(dirpath)
        if SECTION_BLURB.get(dirpath):
            body += "\n%s\n" % SECTION_BLURB[dirpath]
        made[dirpath + "/README.md"] = body + "\n" + bullets(dirpath, dirpath) + "\n"

    # Root index: top-level docs, then each section with its own pages listed under it.
    all_out = dict(final)
    all_out.update(made)

    def entries_all(dirpath):
        out = []
        for o in all_out:
            p = Path(o)
            if p.name != "README.md" and p.parent.as_posix() == dirpath:
                out.append(o)
            elif p.name == "README.md" and p.parent.parent.as_posix() == dirpath:
                out.append(o)
        return sorted(out, key=lambda o: title_by_out.get(o, Path(o).parent.name).lower())

    top = entries_all(".")
    lines = []
    for o in [x for x in top if Path(x).name == "README.md"]:
        section = Path(o).parent.as_posix()
        lines += ["### [%s](%s)" % (dir_title(section), o), ""]
        if SECTION_BLURB.get(section):
            lines += [SECTION_BLURB[section], ""]
        for c in entries_all(section):
            if Path(c).name == "README.md":
                sub = Path(c).parent.as_posix()
                lines.append("- [%s](%s) — %s" % (dir_title(sub), c, SECTION_BLURB.get(sub, "")))
            else:
                lines.append("- [%s](%s)" % (title_by_out.get(c, c), c))
        lines.append("")

    loose = [x for x in top if Path(x).name != "README.md"]
    if loose:
        lines += ["### Feeds and Reference", "",
                  "Flat-file feeds and standalone reference documents.", ""]
        lines += ["- [%s](%s)" % (title_by_out.get(o, o), o) for o in loose]
    made["README.md"] = ROOT_README % "\n".join(lines).strip()
    return made


# ---------------------------------------------------------------- driver

def main():
    if not META_PATH.exists():
        print("missing %s -- run tools/fetch_wiki_meta.py first" % META_PATH.name)
        return 1
    blob = json.loads(META_PATH.read_text(encoding="utf-8"))
    meta, diagrams = blob["pages"], blob["diagrams"]
    out_for = {rel: out_path_for(rel) for rel in meta}
    by_ref = {v["ref"]: rel for rel, v in meta.items()}

    docs, problems = {}, []
    for rel, info in sorted(meta.items()):
        d = Doc(rel, meta, by_ref, out_for, diagrams)
        md = d.convert((SRC / rel).read_text(encoding="utf-8"))
        docs[rel] = (d, md)
        problems += ["%s: %s" % (rel, p) for p in d.problems]

    # pass 2 -- heading slugs per output file, then fill placeholders
    slugs = {}
    for rel, (d, _) in docs.items():
        seen, table = {}, {}
        for h in d.headings:
            base = gh_slug(h)
            k = seen.get(base, 0)
            seen[base] = k + 1
            table.setdefault(h, base if k == 0 else "%s-%d" % (base, k))
        slugs[out_for[rel]] = table

    title_by_out = {o: meta[rel]["title"] for rel, o in out_for.items()}
    children = {}
    for rel, o in out_for.items():
        parent = str(Path(o).parent).replace("\\", "/")
        if Path(o).name == "README.md":
            parent = str(Path(o).parent.parent).replace("\\", "/")
        children.setdefault(parent, []).append(o)

    final = {}
    for rel, (d, md) in docs.items():
        def fill(m):
            kind, *rest = d.slots[int(m.group(1))]
            if kind == "literal":
                idx, keep = rest
                return keep[idx]
            if kind == "anchor_text":
                path, text = rest
                s = slugs.get(path, {}).get(text)
                if s is None:
                    d.problems.append("anchor text %r not a heading in %s" % (text, path))
                    return gh_slug(text)
                return s
            if kind == "child_index":
                own = str(Path(d.out).parent).replace("\\", "/")
                kids = sorted(x for x in children.get(own, []) if x != d.out)
                return "\n".join(
                    "- [%s](%s)" % (title_by_out[x], d.rel_to(x)) for x in kids)
            return ""
        # Stashed literals can themselves contain placeholders (a link literal holds
        # an anchor placeholder), and re.sub does not rescan its own output.
        for _ in range(8):
            new = re.sub(r"\x00PH(\d+)\x00", fill, md)
            if new == md:
                break
            md = new
        if "\x00PH" in md:
            d.problems.append("placeholder left unresolved after 8 passes")
        md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
        md, missed = redact(out_for[rel], md)
        for pat in missed:
            d.problems.append("redaction rule matched nothing: %s" % pat)
        head = "# %s\n" % meta[rel]["title"]
        if out_for[rel].startswith("gateway-api/admin/"):
            head += "\n" + ADMIN_BANNER
        md = head + "\n" + md
        final[out_for[rel]] = md
        problems += ["%s: %s" % (rel, p) for p in d.problems if p not in d.problems[:0]]

    final.update(build_indexes(final, title_by_out))

    for out, md in final.items():
        p = ROOT / out
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(md, encoding="utf-8", newline="\n")

    (ROOT / "images").mkdir(parents=True, exist_ok=True)
    n_svg = 0
    for rel, (d, _) in docs.items():
        for name, svg in d.svg_out.items():
            (ROOT / "images" / (name + ".svg")).write_text(svg, encoding="utf-8", newline="\n")
            n_svg += 1

    assets = sorted({a for d, _ in docs.values() for a in d.assets_used})
    (Path(__file__).resolve().parent / "assets-used.json").write_text(
        json.dumps([list(a) for a in assets], indent=1), encoding="utf-8")

    print("wrote %d markdown files, %d diagram SVGs, %d other assets needed"
          % (len(final), n_svg, len(assets)))
    seen = set()
    uniq = [p for p in problems if not (p in seen or seen.add(p))]
    if uniq:
        print("\n%d unresolved:" % len(uniq))
        for p in uniq:
            print("   ", p)
        return 1
    print("all links resolved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
