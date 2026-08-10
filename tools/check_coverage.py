"""Check that this documentation covers the endpoints the gateway actually serves.

    python tools/check_coverage.py --gateway D:\\IntellJ-Workspace\\gateway

Reports both directions:

  * implemented but undocumented — an endpoint exists in the code with no mention here
  * documented but not implemented — this repo describes a path the code does not serve

A maintenance tool, not part of any build. It needs a gateway checkout to read.

Endpoints that are deliberately not documented go in INTERNAL below, each with a
reason. That keeps "nobody has documented this yet" and "this is intentionally not
public API" as distinct states, so a green run means something.

Matching is on the endpoint's **filename** (``restAreaMap.json``), not its full path.
The documentation writes endpoints inconsistently — sometimes
``https://travelmidwest.com/lmiga/foo.json``, sometimes ``### POST /lmiga/foo.json``,
sometimes ``#### GET {id}/routeTraffic.json`` under a stated base path. Matching full
paths reports dozens of endpoints as missing that are in fact documented; filenames are
unique enough across this API to be the reliable key.
"""

import argparse
import os
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
Q = '"'

# Endpoints that exist in the code and are intentionally absent from the public docs.
# Keep the reason current -- it is the only record of why each one is excluded.
INTERNAL = {
    "/geoLocate.json": "internal location-resolution helper, not a supported API",
    "/geoLocatePoint.json": "internal location-resolution helper",
    "/geoLocateSection.json": "internal location-resolution helper",
    "/geoParse.json": "internal location-parsing helper",
    "/milemarkerIcons.json": "internal map-rendering support layer",
    "/weatherPolygons.json": "internal map-rendering support layer",
    "/api/waze": "partner pull interface used by Waze, not general public API",
    "/api/waze/alerts": "partner pull interface used by Waze",
    "/api/waze/alerts/removed": "partner pull interface used by Waze",
    "/api/waze/alerts/summary": "partner pull interface used by Waze",
    "/api/waze/config": "partner pull interface used by Waze",
    "/error.html": "error page, not an API endpoint",
    "/": "site index",
    "/gwbroker": "legacy alias redirecting old gwbroker?handler=... URLs to the "
                 ".xml.gz downloads; superseded, not worth documenting",
    # ArchiveProxyController: every one of these is marked @Deprecated in the code,
    # superseded by the /admin/archive/* endpoints that the admin pages document.
    # (The React admin UI still calls /dmsArchiveLocations.json -- a frontend issue,
    # not a documentation one.)
    "/dmsArchiveLocations.json": "@Deprecated, superseded by /admin/archive/dms/locations.json",
    "/dmsArchiveText.json": "@Deprecated, superseded by /admin/archive/dms/text.json",
    "/vdsArchiveLocations.json": "@Deprecated, superseded by /admin/archive/vds/locations.json",
    "/vdsArchive.json": "@Deprecated, superseded by /admin/archive/vds/data.json",
    "/vdsArchiveReport.json": "@Deprecated, superseded by /admin/archive/vds/report.json",
}

# Endpoints whose path has no filename leaf, so the filename match cannot see them.
# Searching the prose for the literal path was tried and is too noisy to trust --
# "/camera" matches every </camera> XML closing tag, "/messageSign" matches the img_url
# column of the dmsInfo.csv sample rows. So these are hand-verified instead: the value
# is the file that documents the endpoint, checked once by reading it.
DOCUMENTED_IN = {
    "/snapshot": "gateway-api/show-camera.md",
    "/camera": "gateway-api/show-camera.md",
    "/messageSign": "dms-info-csv.md",
    "/publisher": "xml-upload-manual.md",
    "/*.xml.gz": "user-guides-and-manuals/xml-and-camera-image-download-manual.md",
    "/admin/webfiles/{*filePath}": "gateway-api/admin/admin-web-files.md",
    "/admin/webfiles/path": "gateway-api/admin/admin-web-files.md",
    "/webfile/images/**": "gateway-api/admin/admin-web-files.md",
}

MAPPING_RE = re.compile(
    r"@(?:Request|Get|Post|Put|Delete|Patch)Mapping\s*\(([^)]*)\)", re.S)
LITERAL_RE = re.compile(Q + "([^" + Q + "]*)" + Q)
# An endpoint filename, but not a JavaScript ``response.json()`` call -- the docs are
# full of fetch() examples, and without the negative lookahead every one of them reports
# as a documented endpoint named "response.json".
DOC_TOKEN_RE = re.compile(r"[A-Za-z0-9_-]+\.(?:json|csv)\b(?!\s*\()")


def implemented(gateway):
    """path -> source file, for every Spring mapping in the gateway checkout.

    A controller's full path is its class-level @RequestMapping base plus each
    method-level path. Where the class-level annotation carries the whole path and the
    methods add nothing, the base *is* the endpoint -- missing that case is what made an
    earlier version of this script report ~70 false gaps.
    """
    out = {}
    for dp, dn, fn in os.walk(gateway):
        dn[:] = [d for d in dn if d not in (".git", "target", "node_modules", "build")]
        for f in fn:
            if not f.endswith(".java"):
                continue
            fp = Path(dp) / f
            try:
                t = fp.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            if "Mapping(" not in t:
                continue
            anns = [(m.start(), [s for s in LITERAL_RE.findall(m.group(1))
                                 if s.startswith("/")])
                    for m in MAPPING_RE.finditer(t)]
            class_at = t.find("public class")
            base = ""
            for pos, lits in anns:
                if pos < class_at and lits:
                    base = lits[0]
            method_paths = [l for pos, lits in anns if pos > class_at for l in lits]
            full = [(base + l if base else l) for l in method_paths] or \
                   ([base] if base else [])
            for p in full:
                out.setdefault(p, str(fp.relative_to(gateway)).replace("\\", "/"))
    return out


def doc_text():
    """rel path -> text, for every markdown file in the repo."""
    out = {}
    for dp, dn, fn in os.walk(DOCS):
        dn[:] = [d for d in dn if d not in ("tools", ".git", "images", "files")]
        for f in fn:
            if f.endswith(".md"):
                p = Path(dp) / f
                out[str(p.relative_to(DOCS)).replace("\\", "/")] = \
                    p.read_text(encoding="utf-8")
    return out


def documented(texts):
    """Every endpoint filename mentioned anywhere in the docs -> the files naming it."""
    found = {}
    for rel, t in texts.items():
        for tok in DOC_TOKEN_RE.findall(t):
            found.setdefault(tok, set()).add(rel)
    return found


def leaf(path):
    return path.rstrip("/").split("/")[-1]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--gateway", required=True,
                    help="path to a gateway repo checkout")
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="also list what is covered")
    args = ap.parse_args()

    gw = Path(args.gateway)
    if not (gw / "webapp").is_dir():
        print("%s does not look like a gateway checkout (no webapp/)" % gw)
        return 2

    impl = implemented(gw)
    texts = doc_text()
    docs = documented(texts)

    undocumented, covered, stale_map = [], [], []
    for path, src in sorted(impl.items()):
        if path in INTERNAL or path.endswith(".jsp"):
            continue
        if path in DOCUMENTED_IN:
            where = DOCUMENTED_IN[path]
            if where not in texts:
                stale_map.append((path, where))
            covered.append((path, src))
            continue
        name = leaf(path)
        if not re.search(r"\.(json|csv)$", name):
            undocumented.append((path, src))
            continue
        if name.startswith("{"):
            # A path-parameter leaf such as /admin/incidentEntry/{id}.json. The docs
            # write these either fully qualified with a concrete id
            # ("/admin/incidentEntry/123.json") or relative to a stated base
            # ("GET /{id}.json"). So look for the relaxed leaf inside a file that also
            # names the controller's base path.
            base = path[: -len(name) - 1] or "/"
            leaf_pat = re.sub(r"\\?\{[a-zA-Z]+\\?\}", lambda _: r"(?:\{[a-zA-Z]+\}|\d+)",
                              re.escape(name))
            hit = any(re.search(leaf_pat, t) and base in t for t in texts.values())
        else:
            hit = name in docs
        (covered if hit else undocumented).append((path, src))

    # Documented endpoints with nothing serving them. Compare on filename, since the
    # docs also name files that are not endpoints at all (payload examples, downloads).
    impl_names = {leaf(p) for p in impl}
    orphans = sorted((n, sorted(f)) for n, f in docs.items()
                     # "123.json" is an example id standing in for a {id} path
                     # parameter, not an endpoint name of its own.
                     if n not in impl_names and not re.fullmatch(r"\d+\.json", n))

    print("implemented endpoints: %d   documented endpoint names: %d   internal: %d"
          % (len(impl), len(docs), len(INTERNAL)))

    if undocumented:
        print("\nIMPLEMENTED BUT UNDOCUMENTED (%d):" % len(undocumented))
        for path, src in undocumented:
            print("   %-42s %s" % (path, src))

    if orphans:
        print("\nDOCUMENTED BUT NOT SERVED (%d) - stale, or a payload/download rather "
              "than an endpoint:" % len(orphans))
        for name, files in orphans:
            print("   %-42s %s" % (name, files[0]))

    if args.verbose:
        print("\nCOVERED (%d):" % len(covered))
        for path, src in covered:
            print("   %-42s %s" % (path, src))
        print("\nINTERNAL, deliberately undocumented (%d):" % len(INTERNAL))
        for path, why in sorted(INTERNAL.items()):
            print("   %-42s %s" % (path, why))

    if stale_map:
        print("\nDOCUMENTED_IN POINTS AT A FILE THAT NO LONGER EXISTS (%d):"
              % len(stale_map))
        for path, where in stale_map:
            print("   %-42s %s" % (path, where))

    if undocumented or stale_map:
        print("\nFAIL: %d endpoint(s) need documenting or an INTERNAL entry"
              % len(undocumented))
        return 1
    print("\nOK: every implemented endpoint is documented or explicitly internal")
    return 0


if __name__ == "__main__":
    sys.exit(main())
