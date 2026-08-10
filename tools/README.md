# Migration tooling

These scripts produced this repository from the GTIS internal wiki
(`wiki.travelmidwest.com`, XWiki 2.1 syntax). They are kept so the conversion is
reproducible and auditable, not because they need to run again — **this repository is
now the source of truth**, and the documents should be edited directly from here.

## Pipeline

```
python tools/fetch_wiki_meta.py   # network: page map, heading anchors, diagram SVGs
python tools/xwiki2md.py          # offline: .xwiki -> .md, rewrites every link
python tools/fetch_assets.py      # network: images and file attachments
python tools/verify.py            # offline: links, anchors, fences, leftovers, secrets
```

`fetch_wiki_meta.py` writes `wiki-meta.json`, which is committed so `xwiki2md.py` and
`verify.py` run without network access.

## Keeping the docs honest

`check_coverage.py` is the ongoing one — it diffs this repository against the endpoints
the gateway actually serves, in both directions:

```
python tools/check_coverage.py --gateway /path/to/gateway     # add -v to list coverage
```

Endpoints deliberately not documented go in its `INTERNAL` map with a reason, so
"nobody has documented this yet" and "this is intentionally not public API" stay
distinct states and a green run means something.

Two matching subtleties, both learned the hard way:

- **Match on endpoint filename, not full path.** The docs write endpoints
  inconsistently — `https://travelmidwest.com/lmiga/foo.json`, `### POST /lmiga/foo.json`,
  `#### GET {id}/routeTraffic.json` beneath a stated base path. Matching full paths
  reported ~70 endpoints as undocumented that were documented all along.
- **Endpoints with no filename** (`/camera`, `/snapshot`, `/messageSign`) cannot be
  matched that way, and searching the prose for the literal path is far too noisy —
  `/camera` matches every `</camera>` XML closing tag, `/messageSign` matches the
  `img_url` column of the dmsInfo.csv sample rows. Those are listed in `DOCUMENTED_IN`
  instead, hand-verified once, naming the file that documents each.

## Why a custom converter

Pandoc has no XWiki *reader* (XWiki is output-only). Converting via the wiki's rendered
HTML also fails: XWiki renders code blocks as `<div class="code">` with per-token
`<span style="color:…">` and `<br/>`, so all 286 code blocks would lose their fences and
language tags.

## Things that bit us, recorded so they don't again

- **Dots in space names are literal in REST URLs.** Escaping them as `%5C.` (the form
  used in a page *reference*) makes the endpoint answer 200 with nothing. That silently
  dropped the `cameraInfo.csv` diagrams and images on the first pass.
- **`WebPreferences` children report their parent's path**, so a naive tree walk
  recurses forever. Only descend into `.WebHome` pages.
- **Attachment URLs need `/WebHome/`**: `/bin/download/<space path>/WebHome/<file>`.
- **A `{{diagram}}` macro stores only draw.io XML**, and a diagram page rendered on its
  own emits no SVG — the SVG appears only on the page that *embeds* the macro. The
  diagram index is therefore built wiki-wide and keyed by diagram name.
- **The REST attachments endpoint under-reports.** `fetch_assets.py` also scrapes
  `<img src>` from rendered pages.
- **Tilde escapes are stored double-escaped**: `~~/` means `/`.
- **XWiki heading anchors (`HFooBar`) are not GitHub slugs.** They are resolved via the
  rendered heading ids, then re-slugified, in a second pass so duplicate headings get
  the right `-1` suffix.

## Known content gaps

- Three images are referenced by the source pages but no longer exist on the wiki (they
  404, and their pages report zero attachments). Each is now a visible "figure
  unavailable" note in the page — a hidden HTML comment left the surrounding prose
  referring to something the reader could not see was missing. If the originals turn up,
  drop them in `images/` and replace the notes.
- `xwiki2md.py` re-runs will reintroduce the `<!-- TODO(docs) -->` form of those markers;
  see `MISSING_IMAGES` in that script.
- The Smart Work Zone Specifications page named individual third-party vendor staff with
  direct e-mail and phone; those are replaced with the GTIS team address (see
  `REDACTIONS` in `xwiki2md.py`). The rules fail the build if they stop matching.
