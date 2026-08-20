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

`check_fields.py` is the level below it — same idea, one step further in:

```
python tools/check_fields.py --gateway /path/to/gateway     # add --endpoint to narrow
```

`check_coverage.py` asks "is this endpoint documented at all?"; this asks "are the
*fields* we describe the fields it really returns?". It works because the GeoJSON map
endpoints all build their `properties` object from a small POJO (`IncidentProperties`,
`CameraProperties`, …) under Lombok `@Getter`/`@Value` and serialized by Jackson, so the
wire names are statically extractable from the class — and the docs list them as
`- name — description` bullets. The doc-section-to-class mapping is written out by hand
in `MAPPING`, not inferred, and anything it cannot parse is reported as UNMAPPED rather
than skipped.

It proposes; it does not conclude. It compares **names only** — value sets, types, units
and null behaviour are invisible to it, and several of the worst errors found in the
first pass were value-set errors on correctly-named fields (`stat` on `incidentMap.json`
was documented with a severity vocabulary the code never produces). Read the code before
editing a document on its say-so.

Three traps it has to handle, all of which produced false findings first:

- **`@JsonProperty` renames.** `SpecialEventPropertiesDto` declares `lastUpdated` and
  ships it as `lstUpd`. Reading the declaration alone reports correct documentation as
  wrong — the most dangerous output this tool can produce.
- **Package-private fields.** Classes under Lombok `@Value` declare `String id;` with no
  visibility keyword. A regex demanding `private` matches nothing, and an empty field
  list makes every documented field look undocumented — a page of false findings that
  reads exactly like a real one.
- **Constructor locals.** Only declarations at class-body brace depth are fields;
  otherwise `formatter` and `imageAge` get reported as undocumented wire fields.

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

- Three images the source pages reference are gone from the wiki (they 404, and their
  pages report zero attachments). All three were recovered from elsewhere and are
  committed under `images/`, so the pages are whole. The conversion scripts still record
  the loss as it stood — `MISSING_IMAGES` in `xwiki2md.py` names all three, and
  `fetch_assets.py` cannot download them — which is history, not a live gap. It is also
  one more reason not to re-run the conversion over these documents: it would bury the
  restored figures under "figure unavailable" markers again.
- The Smart Work Zone Specifications page named individual third-party vendor staff with
  direct e-mail and phone; those are replaced with the GTIS team address (see
  `REDACTIONS` in `xwiki2md.py`). The rules fail the build if they stop matching.
- `gateway-traffic-data-archive.md` used to carry a copy of the data definitions from
  the External Interface User Guide, in CORBA IDL where the guide gives XSD. That copy
  is gone; the section is now a table of links into the guide, and the five diagrams it
  duplicated (`lat-long-diagram.svg` and friends, cosmetic variants of figures the guide
  already shows) went with it.
- Two passages in `locations.md` no longer match the wiki, on purpose. The wiki calls
  the ramp figure a ramp from I-355 North where the recovered map plainly shows I-290
  North, so the caption was written against the figure; and the geometry point figure,
  which arrives with no caption of its own, was given one along with the XML the drawing
  depicts. Both edits live in the markdown only, as edits to this repository should.
- `locations.md` also documents the LatLongRamp profile, which the wiki never covered:
  it is a version 2.0 addition, written from `LatLongRampPoint` and `GenericSection` in
  the gateway source rather than from any wiki page.
