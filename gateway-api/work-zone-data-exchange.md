# Work Zone Data Exchange (WZDx)

## About

The [Work Zone Data Exchange (WZDx)](https://github.com/usdot-jpo-ode/wzdx) is a US DOT
specification for publishing work zone activity as GeoJSON. The specification, its schemas
and its enumerated types are maintained in the official repository:

- Specification and schemas — [github.com/usdot-jpo-ode/wzdx](https://github.com/usdot-jpo-ode/wzdx)
- Released versions — [github.com/usdot-jpo-ode/wzdx/releases](https://github.com/usdot-jpo-ode/wzdx/releases)
- v4.2 work zone feed schema — [schemas/4.2/WorkZoneFeed.json](https://github.com/usdot-jpo-ode/wzdx/blob/main/schemas/4.2/WorkZoneFeed.json)
- Guide to building a feed — [Creating_a_WZDx_Feed.md](https://github.com/usdot-jpo-ode/wzdx/blob/main/Creating_a_WZDx_Feed.md)

GTIS both **consumes** and **publishes** WZDx:

- It ingests WZDx feeds from the Illinois Tollway and WisDOT.
- It converts work zones from the GTIS roadwork database into WZDx format, so that agencies
  that do not publish WZDx themselves are still represented.
- It republishes the combined result through the endpoints below. The GTIS feed declares
  `"version": "4.2"` in its `feed_info`.

Three endpoints serve this data. They differ in *format* (map-oriented GeoJSON vs. the WZDx
document format) and in *scope* (everything vs. the Illinois-only subset published to the
Trihydro SDX):

| Endpoint | Format | Methods | Scope |
| --- | --- | --- | --- |
| [constructionWzdxMap.json](#constructionwzdxmapjson) | GTIS construction map GeoJSON | POST | GTIS roadwork + ingested WZDx, for drawing maps |
| [wzdxData.json](#wzdxdatajson) | WZDx work zone feed | GET, POST | Ingested WZDx, optionally plus converted GTIS roadwork |
| [illinoisWzdx.json](#illinoiswzdxjson) | WZDx work zone feed | GET, POST | Illinois sources only, Tollway excluded, cleaned |

None of the three requires authentication. Signing in adds nothing to `wzdxData.json` or
`illinoisWzdx.json`. For `constructionWzdxMap.json` it sets the `auth` property and relaxes
the confidence-level filter on the GTIS roadwork half of the response, so an authenticated
caller also sees roadwork that has not been confirmed to high confidence.

### Caching

All three endpoints send `ETag`, `Last-Modified` and `Cache-Control: max-age=300,
must-revalidate`. The underlying data does not change faster than that, so send the `ETag`
back as `If-None-Match` (or the `Last-Modified` value as `If-Modified-Since`) and expect a
304 rather than re-downloading. This matters most for `wzdxData.json`, whose response is
roughly 17–20 MB.

`constructionWzdxMap.json` additionally caches each distinct combination of bounding box,
parameters and authentication state server-side for five minutes.

## constructionWzdxMap.json

*Also summarized in [Map Data → Construction (WZDx)](map-data.md#construction-wzdx).*

Returns construction in the same GeoJSON shape as
[constructionMap.json](map-data.md#construction), drawn from two sources at once: the GTIS
roadwork database and the WZDx feeds GTIS ingests from the Illinois Tollway and WisDOT. Use
this endpoint when you want work zones to draw on a map alongside other GTIS layers; use
[wzdxData.json](#wzdxdatajson) when you want the WZDx document format itself.

### Request

```console
https://travelmidwest.com/lmiga/constructionWzdxMap.json
```

POST only — a GET returns 405 Method Not Allowed.

#### Query Parameters

- **type** (optional) — restrict the response to one of the two sources. Matched
  case-insensitively as a substring, so `Roadwork`, `roadwork` and `RoadWork` are equivalent:
  - `Roadwork` — GTIS roadwork database only.
  - `WZDx` — ingested WZDx events only.
  - omitted — both.
- **agency** (optional) — accepted, but it does **not** currently filter the response. It
  only varies the server-side cache key, so `?agency=WISDOT` and `?agency=TIMS` return the
  same features as an unfiltered request.

#### POST Body

- `bbox` — see [Bounding Box](map-data.md#bounding-box) (optional; if omitted or empty, all
  features are returned).

```console
curl -X POST -H 'Content-Type: application/json' \
     -d '{"bbox":[-88.5,41.5,-87.5,42.1]}' \
     'https://travelmidwest.com/lmiga/constructionWzdxMap.json?type=WZDx'
```

### Response

A GeoJSON FeatureCollection:

- type — "FeatureCollection"
- timestamp — the last-modified time of the data, ISO 8601 (see the caveat below)
- features — an array of GeoJSON features each with the following fields:
  - type — "Feature"
  - geometry — a GeoJSON GeometryCollection. Linear events contribute a MultiLineString
    giving the extent of the work zone; point events contribute one Point per location. A
    single feature may hold several geometries.
  - properties — a JSON object with the following fields:
    - id — the event ID. GTIS roadwork IDs look like `IL-IDOT-ROADWORK.2026.8.11.14.17232575`;
      ingested WZDx IDs look like `WI-WisDOT-WZDX-4c9cd5cb-…` or `IL-TIMS-WZDX-3889631`.
    - locDesc — the location description
    - desc — the description
    - sev — the severity: "Major", "Medium", "Minor", "None", or "Unknown"
    - closure — the lane closure. For GTIS roadwork this is prose ("Various lanes closed");
      for ingested WZDx events it is the WZDx `vehicle_impact` value ("some-lanes-closed",
      "all-lanes-closed", "all-lanes-open", …), or an empty string when the source omits it.
    - time — the time period, formatted `M/d/yy h:mm a to M/d/yy h:mm a`
    - dur — the duration
    - src — the name of the source agency ("IDOT", "Illinois Tollway", "WisDOT", "InDOT",
      "Lake County", …). Currently `null` on ingested WZDx events.
    - mo — true or false, whether the event is a moving operation
    - lstUpd — the formatted last update time, `M/d/yy h:mm a`
    - a — true or false, whether the event is on an arterial rather than an expressway or
      connector ramp
    - restrictions — the WZDx restrictions for the event, e.g. `"Reduced Width:132.0 inches"`;
      `null` when there are none, which is always the case for GTIS roadwork
    - auth — true if the response was generated for an authenticated caller, false otherwise

Every property above is always present; ones that do not apply are `null` or empty rather
than omitted.

> [!NOTE]
> `timestamp` reflects the newest GTIS roadwork event in the response. Ingested WZDx events
> do not contribute to it, so a `?type=WZDx` request reports `1970-01-01T00:00:00Z`. Use
> the `Last-Modified` response header, or the per-event `lstUpd` property, instead of
> `timestamp` for those requests.

### Example

One ingested WZDx feature, trimmed:

```json
{
  "type": "Feature",
  "geometry": {
    "type": "GeometryCollection",
    "geometries": [
      {"type": "MultiLineString", "coordinates": [[[-90.46530636, 42.53632965], [-90.46532681, 42.53632974]]]}
    ]
  },
  "properties": {
    "id": "WI-WisDOT-WZDX-4c9cd5cb-c6f7-fb5f-b2b7-18365f26b765",
    "locDesc": "WIS 11 WB from PARK LN to WIS 35 NB (END CC)",
    "desc": "Mainline Right Shoulder Closed. Daily from 08/20/2026 to 09/30/2026, 06:00 AM - 08:30 PM, M, T, W, Th, F (excluding Sun, Sat)",
    "sev": "Medium",
    "closure": "some-lanes-closed",
    "time": "9/1/26 11:00 AM to 9/2/26 1:30 AM",
    "dur": "0 day",
    "src": null,
    "mo": false,
    "lstUpd": "8/13/26 6:28 PM",
    "a": false,
    "restrictions": "Reduced Width:132.0 inches",
    "auth": false
  }
}
```

And one GTIS roadwork feature, trimmed:

```json
{
  "type": "Feature",
  "geometry": {
    "type": "GeometryCollection",
    "geometries": [
      {"type": "MultiLineString", "coordinates": [[[-87.84, 41.42], [-87.84, 41.44]]]},
      {"type": "MultiLineString", "coordinates": [[[-87.84, 41.44], [-87.84, 41.42]]]}
    ]
  },
  "properties": {
    "id": "IL-IDOT-ROADWORK.2026.8.11.14.17232575",
    "locDesc": "NB US-45 from Manhattan Monee Rd to Stuenkel Rd, SB US-45 from Stuenkel Rd to Manhattan Monee Rd",
    "desc": "",
    "sev": "Medium",
    "closure": "Various lanes closed",
    "time": "8/14/26 9:00 AM to 11/18/26 5:00 PM",
    "dur": "96 days",
    "src": "IDOT",
    "mo": false,
    "lstUpd": "8/14/26 9:04 AM",
    "a": true,
    "restrictions": null,
    "auth": false
  }
}
```

## wzdxData.json

*Also summarized in [Map Data → WZDx Data Feed](map-data.md#wzdx-data-feed).*

Serves the GTIS work zone feed in WZDx document format: the events ingested from the
Illinois Tollway and WisDOT, optionally merged with GTIS roadwork converted to WZDx.

### Request

```console
https://travelmidwest.com/lmiga/wzdxData.json
https://travelmidwest.com/lmiga/wzdxData.json?includeRoadWork=true
```

Both GET and POST are supported and return the same thing.

#### Query Parameters

- **includeRoadWork** (optional, boolean, default `false`) — when `true`, GTIS roadwork is
  converted to WZDx and merged into the feed. Roadwork from agencies that already publish a
  WZDx feed is skipped, so events are not duplicated.
- **agency** (optional) — accepted but **not currently implemented**; it has no effect on
  the response.

#### POST Body

- `bbox` — accepted but **not currently implemented**; the full feed is returned regardless.
  Filter client-side, or use [constructionWzdxMap.json](#constructionwzdxmapjson), which does
  honour a bounding box.

> [!WARNING]
> The response is large — roughly 17 MB, or 20 MB with `includeRoadWork=true`. Use
> conditional requests (see [Caching](#caching)) rather than polling for the whole document.

### Response

A WZDx work zone feed:

- type — "FeatureCollection"
- feed_info — feed metadata:
  - publisher — "GTIS"
  - contact_name — "GTIS TravelMidwest.com"
  - contact_email — "support@travelmidwest.com"
  - update_frequency — the nominal update interval in seconds (600)
  - update_date — the feed's update time, ISO 8601
  - version — the WZDx specification version the feed targets ("4.2")
  - data_sources — an array of objects with a `data_source_id`, listing the sources present
    in the feed. Without `includeRoadWork` this is the ingested WZDx sources; with it, the
    GTIS roadwork sources are added.
- features — an array of WZDx road event features:
  - type — "Feature"
  - id — the event ID
  - bbox — a GeoJSON bounding box, present on some sources only
  - geometry — a GeoJSON LineString, MultiLineString or MultiPoint
  - properties — a WZDx road event object:
    - core_details — `data_source_id`, `event_type` ("work-zone" or "detour"), `name`,
      `description`, `road_names`, `direction`, `update_date`, `creation_date` and
      `related_road_events`
    - start_date / end_date — ISO 8601
    - is_start_date_verified / is_end_date_verified
    - is_start_position_verified / is_end_position_verified
    - beginning_cross_street / ending_cross_street
    - beginning_milepost / ending_milepost
    - vehicle_impact — e.g. "some-lanes-closed", "all-lanes-closed", "flagging",
      "temporary-traffic-signal", "alternating-one-way", "all-lanes-open"
    - lanes — an array of lane objects (`type`, `order`, `status`)
    - restrictions — an array of WZDx restriction objects
    - work_zone_type, worker_presence, reduced_speed_limit_kph, location_method,
      types_of_work, impacted_cds_curb_zones

Field names and permitted values follow the WZDx specification; see
[the specification repository](https://github.com/usdot-jpo-ode/wzdx) for the authoritative
definitions.

> [!NOTE]
> Features converted from GTIS roadwork (`includeRoadWork=true`) are less complete than the
> natively-published ones. Consumers should expect, and tolerate:
>
> - **Missing `geometry`.** Roadwork whose location could not be resolved yields a feature
>   with no `geometry` member at all, which is not valid GeoJSON. Skip those features.
> - **A different `update_date` type.** Native events carry an ISO 8601 string; converted
>   events carry epoch milliseconds as a number.
> - **Empty strings in place of absent values**, e.g. `"vehicle_impact": ""`.
>
> The [Illinois feed](#illinoiswzdxjson) exists partly to correct problems of this kind
> before the data is forwarded to the SDX.

### Example

The feed header, and one ingested Tollway feature with its coordinates trimmed:

```json
{
  "type": "FeatureCollection",
  "feed_info": {
    "publisher": "GTIS",
    "contact_name": "GTIS TravelMidwest.com",
    "contact_email": "support@travelmidwest.com",
    "update_frequency": 600,
    "update_date": "2026-08-19T20:44:14.937000000Z",
    "version": "4.2",
    "data_sources": [{"data_source_id": "TIMS"}, {"data_source_id": "WisDOT"}]
  },
  "features": [
    {
      "id": "IL-TIMS-WZDX-3889631",
      "type": "Feature",
      "bbox": [-87.87420654, 42.15692138, -87.87393951, 42.16706085],
      "geometry": {"type": "LineString", "coordinates": [[-87.8742, 42.1569], [-87.8739, 42.1670]]},
      "properties": {
        "core_details": {
          "data_source_id": "Illinois Tollway",
          "event_type": "work-zone",
          "name": "work-zone event",
          "description": "Roadwork event of type Brdg Repairs",
          "road_names": ["I-94"],
          "direction": "westbound",
          "update_date": "2026-08-18T14:04:15Z",
          "creation_date": "2026-08-18T14:02:20Z",
          "related_road_events": [{"id": "[3889629]", "type": "related-work-zone"}]
        },
        "start_date": "2026-08-20T01:00:00Z",
        "end_date": "2026-08-20T04:00:00Z",
        "vehicle_impact": "some-lanes-closed",
        "work_zone_type": "static",
        "location_method": "unknown",
        "ending_milepost": 24.3,
        "lanes": [
          {"type": "shoulder", "order": 1, "status": "closed"},
          {"type": "general", "order": 2, "status": "closed"},
          {"type": "general", "order": 3, "status": "open"}
        ]
      }
    }
  ]
}
```

## illinoisWzdx.json

*Also summarized in [Map Data → Illinois WZDx Feed](map-data.md#illinois-wzdx-feed).*

> [!IMPORTANT]
> This endpoint is not yet available on travelmidwest.com — it returns 404 as of
> 19 August 2026. The description below reflects the implementation in the GTIS source
> tree, which has not been deployed. Until it ships, use `wzdxData.json?includeRoadWork=true`
> and filter for Illinois sources yourself.

Serves the Illinois-filtered WZDx feed: the same data GTIS uploads to the Trihydro Situation
Data Exchange (SDX). It starts from the same events as
[wzdxData.json](#wzdxdatajson) with GTIS roadwork always merged in, then:

- keeps Illinois sources only (`IL-*`),
- excludes the Illinois Tollway, which publishes to the SDX itself, and
- applies geometry and property corrections so that the result validates against the WZDx
  schema.

### Request

```console
https://travelmidwest.com/lmiga/illinoisWzdx.json
```

Both GET and POST are supported.

#### Query Parameters

- **agency** (optional) — accepted; not currently implemented as a filter.

#### POST Body

- `bbox` — see [Bounding Box](map-data.md#bounding-box) (optional). Unlike
  `wzdxData.json`, this endpoint does apply the bounding box: a feature is kept when any of
  its coordinates falls inside it. Point, LineString, MultiPoint and MultiLineString
  geometries are tested; features with any other geometry type are kept.

### Response

The same WZDx feed structure as [wzdxData.json](#wzdxdatajson) — `type`, `feed_info` and
`features` — with `feed_info` built for the Illinois feed and only the filtered, corrected
features included.

## See also

- [Map Data](map-data.md) — the other GeoJSON map layers, including the non-WZDx
  [Construction](map-data.md#construction) endpoint.
- [Report Data → Construction](report-data.md#construction) — the same construction data
  organized by report location rather than bounding box.
- [GTIS Smart Work Zone Specifications](../user-guides-and-manuals/gtis-smart-work-zone-specifications.md)
  — requirements for contractors and vendors publishing smart work zone data to GTIS.
- [WZDx specification](https://github.com/usdot-jpo-ode/wzdx) — the authoritative field
  definitions, schemas and enumerated types.
