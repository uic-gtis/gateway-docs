# IDOT Incidents

## About

The `stationOne.json` endpoint is a GeoJSON file containing incidents from official Illinois Department of Transportation (IDOT) sources.

## Request

```console
https://travelmidwest.com/lmiga/stationOne.json?encodeLines=true/false
```

## Response

The returned file is in GeoJSON format with both polyline and point features depending on the closure type. The feature properties for each incident are as follows:

- id - unique identifier for the incident
- desc - textual description, usually from Station One email
- location - detailed location description along with lanes closed if known
- status - New, Updated, or Clearing
- start - incident reported time, or null if unknown (ISO 8601 format)
- end - estimated end time, or null if unknown (ISO 8601 format)
- src - IDOT Dx where "x" is the District number, may also be IDOT ComCenter for D1 if we get it from them first
- emergencyVehiclePresent - will almost always be false unless we get a Waze event beforehand that indicates this
- duration - "short" or "long" if incident is expected to last more than an hour, we use this to draw a larger icon
- fullClosure - "true" if all lanes in at least one direction are closed, "false" otherwise

## Examples

### encodeLines~=false

```json
{
  "type": "FeatureCollection",
  "timestamp": "2025-03-24 14:24:32",
  "features": [
    {
      "geometry": {
        "type": "GeometryCollection",
        "geometries": [
          {
            "type": "MultiLineString",
            "coordinates": [
              [
                [-88.1780113, 41.5759381],
                [-88.1777235, 41.5762408],
                [-88.1773368, 41.5766175],
                [-88.1769321, 41.5769875],
                [-88.1765994, 41.5772566],
                [-88.1761317, 41.5776468],
                [-88.175754, 41.577963],
                [-88.1749986, 41.5785618],
                [-88.1733618, 41.579887],
                [-88.1723456, 41.5807077],
                [-88.171878, 41.5810912],
                [-88.1704301, 41.5822684],
                [-88.1694588, 41.5830622],
                [-88.1686404, 41.5837282]
              ]
            ]
          }
        ]
      },
      "properties": {
        "id": "IL-IDOT-INCIDENT.2025.3.24.14.6398037",
        "desc": "Partial closure from I-80 to US-30, move over for safety.",
        "location": "Partial closure NB I-55 (Barack Obama Presidential Expy) from I-80 to US-30, Unincorporated Will County (Channahon), IL",
        "status": "Updated",
        "start": "2025-03-24T19:23:09.520Z",
        "end": "2025-03-27T16:02:30.603Z",
        "src": "IDOT D1",
        "emergencyVehiclePresent": false,
        "duration": "long",
        "fullClosure": false
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "GeometryCollection",
        "geometries": [
          {
            "type": "Point",
            "coordinates": [-89.4783027, 41.4162228]
          }
        ]
      },
      "properties": {
        "id": "IL-IDOTD3-INCIDENT.2023.11.16.9.5988295",
        "desc": "Roof on the Red Covered Bridge on CR 1950 E., 1/2 mile north of IL Rt. 26 has collapsed for unknown reasons and the roadway is blocked.  The bridge will remain closed until further notice. \u003Ca href=\"https://idot.illinois.gov/news/red-covered-bridge--fixing-an-antique.html\"\u003E More information about the bridge\u003C/a\u003E",
        "location": "Full closure SB and NB 1950 St at 1835 Ave (Red Covered Bridge), Princeton, Bureau, IL",
        "status": "Updated",
        "start": "2023-11-16T15:05:31.500Z",
        "end": "2027-01-01T04:00:22.203Z",
        "src": "IDOT D3",
        "emergencyVehiclePresent": false,
        "duration": "long",
        "fullClosure": true
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "GeometryCollection",
        "geometries": [
          {
            "type": "Point",
            "coordinates": [-91.2985271, 39.7558802]
          }
        ]
      },
      "properties": {
        "id": "IL-IDOTD6-INCIDENT.2025.3.20.2.6392174",
        "desc": "Accident",
        "location": "Partial closure WB I-72 at I-172, Hull, Pike, IL",
        "status": "Updated",
        "start": "2025-03-20T07:53:52.899Z",
        "end": "2025-03-27T16:02:23.678Z",
        "src": "IDOT D6",
        "emergencyVehiclePresent": false,
        "duration": "long",
        "fullClosure": false
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "GeometryCollection",
        "geometries": [
          {
            "type": "Point",
            "coordinates": [-89.4464757, 40.0680927]
          },
          {
            "type": "Point",
            "coordinates": [-89.4472132, 40.0673631]
          }
        ]
      },
      "properties": {
        "id": "IL-IDOTD6-INCIDENT.2025.3.17.12.6388712",
        "desc": "Bridge Painting",
        "location": "Partial closures I-55 NB at 800th Ave and SB at near 800th Ave, Broadwell, Logan, IL",
        "status": "Updated",
        "start": "2025-03-17T17:41:06.023Z",
        "end": "2025-03-31T17:56:06.023Z",
        "src": "IDOT D6",
        "emergencyVehiclePresent": false,
        "duration": "long",
        "fullClosure": false
      },
      "type": "Feature"
    }
  ]
}
```

### encodeLines~=true

```json
{
  "type": "FeatureCollection",
  "timestamp": "2025-03-24 14:24:32",
  "features": [
    {
      "geometry": {
        "type": "GeometryCollection",
        "geometries": [
          {
            "type": "MultiLineString",
            "coordinates": [
              "oye|Fp`iyOeABgA?kEFwW^qABaBBmCDgHHkIHiCD{HLwEFsORkABgDDyA@uACo@A{AGgAIu@Eq@Ky@KuAQsAUqBc@{Aa@}Bq@sAg@cA[m@YiB}@uC_BqAw@sCgBiAq@_EcCcHkEiOkJiAs@uAy@q@a@sBoAuFiDmBkAsAy@aBcAqCeBuBqAk@]qBoAu@c@{@i@i@[{A_A{CiBiGwDuJcGkIgFy@e@kAk@oAm@sAm@kAe@iAa@qAa@iBg@eBa@qEu@eAOkAKgAGwAGgAC}AAyA?}ABqEHcJNiINcRXaOXsQXwLRcCDsNTcKP{@@eFHs@@uFJ_HJcEHsCDwEFiCDuDF_BA}BIiBOoBUmB[kCo@{@WoAa@wB{@kB}@uAu@iAu@oA}@{AkAs@o@{@y@kAkAiAqAu@aAmA}A}@kAwBuCiGgIcDiEkA}AkFaH}CaEeCcD"
            ]
          }
        ]
      },
      "properties": {
        "id": "IL-IDOT-INCIDENT.2025.3.24.14.6398037",
        "desc": "Partial closure from I-80 to US-30, move over for safety.",
        "location": "Partial closure NB I-55 (Barack Obama Presidential Expy) from I-80 to US-30, Unincorporated Will County (Channahon), IL",
        "status": "Updated",
        "start": "2025-03-24T19:23:09.520Z",
        "end": "2025-03-24T22:30:09.520Z",
        "src": "IDOT D1",
        "emergencyVehiclePresent": false,
        "duration": "long",
        "fullClosure": false
      },
      "type": "Feature"
    },
    {
      "geometry": {
        "type": "GeometryCollection",
        "geometries": [
          {
            "type": "Point",
            "coordinates": [-89.4783027, 41.4162228]
          }
        ]
      },
      "properties": {
        "id": "IL-IDOTD3-INCIDENT.2023.11.16.9.5988295",
        "desc": "Roof on the Red Covered Bridge on CR 1950 E., 1/2 mile north of IL Rt. 26 has collapsed for unknown reasons and the roadway is blocked.  The bridge will remain closed until further notice. \u003Ca href=\"https://idot.illinois.gov/news/red-covered-bridge--fixing-an-antique.html\"\u003E More information about the bridge\u003C/a\u003E",
        "location": "Full closure SB and NB 1950 St at 1835 Ave (Red Covered Bridge), Princeton, Bureau, IL",
        "status": "Updated",
        "start": "2023-11-16T15:05:31.500Z",
        "end": "2027-01-01T04:00:22.203Z",
        "src": "IDOT D3",
        "emergencyVehiclePresent": false,
        "duration": "long",
        "fullClosure": true
      },
      "type": "Feature"
    }
  ]
}
```
