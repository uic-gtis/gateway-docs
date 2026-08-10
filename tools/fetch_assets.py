"""Download the images and file attachments the converted docs reference.

Run after xwiki2md.py (which writes tools/assets-used.json).

An image referenced by a page is not necessarily *attached* to that page -- the
flattened "all in one" user guide references images that live on the child pages it was
assembled from. So this sweeps every page under both wiki spaces and builds one
name -> URL index, rather than looking only at the referencing page.

Attachment download URLs need "/WebHome/" in the path; without it every request 404s.
"""

import json
import re
import sys
import urllib.request
from pathlib import Path

WIKI = "https://wiki.travelmidwest.com"
REST = WIKI + "/rest/wikis/xwiki"
ROOT = Path(__file__).resolve().parent.parent
USED = Path(__file__).resolve().parent / "assets-used.json"


def get_json(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def space_url(segs):
    # Dots pass through literally; escaping them as %5C. breaks the endpoint silently.
    return "".join("/spaces/" + s for s in segs)


IMG_SRC = re.compile(r'<img[^>]*\ssrc="(/bin/download/[^"]+)"')


def get_text(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def sweep(root_seg, index):
    """name -> download URL for every attachment under a top-level space.

    Two sources, because neither alone is complete: the REST attachments endpoint
    under-reports on some pages, while the rendered HTML only shows images that are
    actually displayed. The rendered <img src> is ground truth where it exists.
    """
    stack = [[root_seg]]
    while stack:
        segs = stack.pop()
        try:
            att = get_json(REST + space_url(segs)
                           + "/pages/WebHome/attachments?media=json&number=500")
        except Exception:
            att = {}
        for a in att.get("attachments", []) if isinstance(att, dict) else []:
            index.setdefault(
                a["name"],
                WIKI + "/bin/download/" + "/".join(segs) + "/WebHome/" + a["name"])

        try:
            page_html = get_text(WIKI + "/bin/view/" + "/".join(segs) + "/?xpage=plain")
        except Exception:
            page_html = ""
        for src in IMG_SRC.findall(page_html):
            src = src.split("?")[0].replace("&amp;", "&")
            index.setdefault(src.rsplit("/", 1)[-1], WIKI + src)
        try:
            kids = get_json(REST + space_url(segs)
                            + "/pages/WebHome/children?media=json&number=500")
        except Exception:
            continue
        for k in kids.get("pageSummaries", []):
            ref = k["id"].split(":", 1)[1]
            # A WebPreferences child reports its *parent's* path, so recursing on it
            # walks in a circle forever. Only real (WebHome) pages are descendable.
            if not ref.endswith(".WebHome"):
                continue
            parts = [p.replace("\\.", ".") for p in re.split(r"(?<!\\)\.", ref)[:-1]]
            if len(parts) <= len(segs):
                continue
            stack.append(parts)


def main():
    if not USED.exists():
        print("missing %s -- run tools/xwiki2md.py first" % USED.name)
        return 1
    used = [tuple(x) for x in json.loads(USED.read_text(encoding="utf-8"))]

    print("indexing wiki attachments...")
    index = {}
    sweep("Web-Services", index)
    sweep("User-Guides-Manuals", index)
    sweep("Media-Content", index)
    print("  %d attachments found across the wiki" % len(index))

    missing, ok = [], 0
    for kind, name in used:
        dest = ROOT / ("images" if kind == "image" else "files") / name
        url = index.get(name)
        if url is None:
            missing.append(name)
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                data = r.read()
        except Exception as e:
            print("  FAILED %s: %s" % (name, e))
            missing.append(name)
            continue
        dest.write_bytes(data)
        ok += 1
        print("  %8d B  %s/%s" % (len(data), dest.parent.name, name))

    print("\ndownloaded %d/%d" % (ok, len(used)))
    if missing:
        print("MISSING (no attachment with this name anywhere on the wiki):")
        for m in missing:
            print("   ", m)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
