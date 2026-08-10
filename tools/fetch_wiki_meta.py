"""Fetch everything the converter needs from the wiki, once, into wiki-meta.json.

The conversion itself (xwiki2md.py) is then fully offline and reproducible.

Per local page:
  * segs / ref  - wiki location, for resolving doc: links
  * anchors     - XWiki generated heading id -> heading text, from the rendered page.
                  XWiki emits <h1 id="HRequest">, and doc: links reference those ids,
                  so this is the only authoritative way to resolve them.
  * attachments - name -> download URL

Plus a wiki-wide ``diagrams`` index: diagram name -> rendered SVG.

Two things this has to work around:

1. ``WebPreferences`` pages report a reference whose parent-path is their own parent, so
   naively recursing on every child walks in a circle forever. Only ``.WebHome`` pages
   are real pages worth descending into.
2. A ``{{diagram}}`` macro stores only draw.io mxGraph XML, and a diagram page rendered
   on its own emits no SVG -- the SVG only appears on the page that *embeds* the macro.
   The flattened "all in one" user guide embeds diagrams whose SVGs are rendered on its
   child pages, so the index has to be built wiki-wide, keyed by diagram name, by
   zipping each page's macro list against that page's rendered SVG list.
"""

import html
import json
import re
import sys
import urllib.request
from pathlib import Path

WIKI = "https://wiki.travelmidwest.com"
REST = WIKI + "/rest/wikis/xwiki"
SRC = Path(r"D:\IntellJ-Workspace\gateway\docs\Web Services")
OUT = Path(__file__).resolve().parent / "wiki-meta.json"
SPACES = ["Web-Services", "User-Guides-Manuals"]

TITLE_ALIAS = {"XMl Upload Manual": "XML Upload Manual"}

HEADING_RE = re.compile(r"<h([1-6])\b[^>]*\bid=\"([^\"]+)\"[^>]*>(.*?)</h\1>", re.S)
TAG_RE = re.compile(r"<[^>]+>")
SVG_RE = re.compile(r"<div class=\"diagram-container\">.*?(<svg\b.*?</svg>)", re.S)
DIAGRAM_MACRO = re.compile(r"\{\{diagram\b[^}]*\}\}")
REF_ATTR = re.compile(r'reference="([^"]*)"')


def get_json(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def get_text(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def space_url(segs):
    # Dots in a space name are passed through literally. Escaping them as %5C. (which
    # is how they appear in a page *reference*) makes the REST endpoint 404, or worse,
    # answer 200 with nothing -- which is how the cameraInfo.csv diagrams and images
    # went missing on the first pass.
    return "".join("/spaces/" + s for s in segs)


def segs_of(ref):
    return [p.replace("\\.", ".") for p in re.split(r"(?<!\\)\.", ref)[:-1]]


def diagram_key(reference):
    """Normalise a {{diagram reference=...}} value to a stable short name."""
    r = reference.strip()
    if r.endswith(".WebHome"):
        r = r[: -len(".WebHome")]
    return re.split(r"(?<!\\)\.", r)[-1].replace("\\.", ".")


def crawl(root_seg):
    """Every real (WebHome) page under a top-level space: title -> segs."""
    found, stack = {}, [[root_seg]]
    while stack:
        segs = stack.pop()
        try:
            kids = get_json(REST + space_url(segs)
                            + "/pages/WebHome/children?media=json&number=500")
        except Exception:
            continue
        for k in kids.get("pageSummaries", []):
            ref = k["id"].split(":", 1)[1]
            if not ref.endswith(".WebHome"):
                continue          # WebPreferences etc. -- would recurse forever
            parts = segs_of(ref)
            if len(parts) <= len(segs):
                continue          # defensive: never walk sideways or up
            found[k["title"]] = parts
            stack.append(parts)
    return found


def heading_text(inner):
    return html.unescape(TAG_RE.sub("", inner)).strip()


def main():
    titles = {}
    for s in SPACES:
        print("crawling %s ..." % s)
        titles.update(crawl(s))
    print("  %d pages" % len(titles))

    # --- wiki-wide diagram index -------------------------------------
    print("indexing diagrams ...")
    diagrams = {}
    for title, segs in sorted(titles.items()):
        try:
            src = get_json(REST + space_url(segs) + "/pages/WebHome?media=json")["content"]
        except Exception:
            continue
        macros = DIAGRAM_MACRO.findall(src)
        if not macros:
            continue
        try:
            page_html = get_text(WIKI + "/bin/view/" + "/".join(segs) + "/?xpage=plain")
        except Exception:
            continue
        svgs = SVG_RE.findall(page_html)
        for macro, svg in zip(macros, svgs):
            ref = REF_ATTR.search(macro)
            if ref:
                diagrams.setdefault(diagram_key(ref.group(1)), svg)
        if len(macros) != len(svgs):
            print("  NOTE %s: %d macros but %d rendered SVGs"
                  % (title, len(macros), len(svgs)))
    print("  %d diagrams captured" % len(diagrams))

    # --- per-local-page metadata -------------------------------------
    meta, missing = {}, []
    for path in sorted(SRC.rglob("*.xwiki")):
        rel = path.relative_to(SRC).as_posix()
        title = TITLE_ALIAS.get(path.stem, path.stem)
        if title not in titles:
            missing.append(rel)
            continue
        segs = titles[title]
        try:
            page_html = get_text(WIKI + "/bin/view/" + "/".join(segs) + "/?xpage=plain")
        except Exception as e:
            print("  WARN render failed for %s: %s" % (rel, e))
            page_html = ""
        try:
            att = get_json(REST + space_url(segs)
                           + "/pages/WebHome/attachments?media=json&number=500"
                           ).get("attachments", [])
        except Exception:
            att = []
        meta[rel] = {
            "title": title,
            "segs": segs,
            "ref": ".".join(s.replace(".", "\\.") for s in segs) + ".WebHome",
            "view_url": WIKI + "/bin/view/" + "/".join(segs) + "/",
            "anchors": {m.group(2): heading_text(m.group(3))
                        for m in HEADING_RE.finditer(page_html)},
            "attachments": {a["name"]: WIKI + "/bin/download/" + "/".join(segs)
                            + "/WebHome/" + a["name"] for a in att},
        }

    if missing:
        print("\nERROR: no wiki page matches these local files:")
        for m in missing:
            print("   ", m)
        return 1

    OUT.write_text(json.dumps({"pages": meta, "diagrams": diagrams},
                              indent=1, ensure_ascii=False), encoding="utf-8")
    print("\nwrote %s: %d pages, %d diagrams" % (OUT.name, len(meta), len(diagrams)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
