# Map Data

## About

GTIS map data is provided in [GeoJSON](https://tools.ietf.org/html/rfc7946) format suitable for presenting on maps. Most responses are a GeoJSON FeatureCollection giving a list of geometric features of the given type. Each feature also includes non-spatial properties, e.g. for constructing a popup for that feature. The names of the fields are often highly abbreviated to reduce bandwidth use.

Most map data URLs require a POST parameter that is a JSON object specifying a bounding box. Some endpoints use GET requests instead; see the individual sections for details.

## Bounding Box

`bbox` — A four-element array of numbers `[minlong, minlat, maxlong, maxlat]` declaring the bounding box for the request (typically the visible extent of the map).

## Travel Times

### Request

```console
https://travelmidwest.com/lmiga/travelTimeMap.json
```

The request requires a POST parameter specifying the request bounds as described in the [Bounding Box](#bounding-box) section.

### Response

The response for a Travel Time request is a GeoJSON FeatureCollection with additional fields for the travel time properties. The location of the Travel Time feature is a point roughly at the midpoint of the section for which it gives a travel time. The xOff, yOff, xJust, and yJust properties can be used to offset the feature from the road so that it does not cover the road or the congestion coloring on the road. The response FeatureCollection has the following fields:

- type — "FeatureCollection"
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format
- features — an array of GeoJSON features each with the following fields:
  - type — "Feature"
  - geometry — a GeoJSON Point object with the following fields:
    - type — "Point"
    - coordinates — an array [long, lat] giving the point
  - properties — a JSON object with the following fields
    - id — the string travel time ID
    - locDesc — the location description for the travel time section
    - tt — the travel time in minutes
    - avgTt — the average travel time in minutes with a link to [travelmidweststats.com](http://travelmidweststats.com/) for the travel time
    - cng — the congestion level: "Uncongested", "Light", "Medium", "Heavy", or "Unknown"
    - len — the length in miles of the travel time section
    - spd — the average speed in mph over the travel time section
    - lstUpd — the formatted update time of the travel time
    - chgo — true or false, whether the travel time is downtown Chicago oriented
    - rot — the direction of travel for a downtown Chicago oriented travel time in degrees
    - xOff — an x offset used to place the icon to the side of the road
    - yOff — a y offset used to place the icon to the side of the road
    - xJust — an x justification used to place the icon to the side of the road
    - yJust — a y justification used to place the icon to the side of the road

### Example

```json
{
  "type": "FeatureCollection",
  "timestamp": "2018-03-09 12:42:53",
  "features": [
    {
      "type": "Feature",
      "geometry": {"type":"Point", "coordinates":[-88.0140652,41.614738]},
      "properties":
        {
          "id": "IL-TIMS-I_355-S-61",
          "xJust": 1.0,
          "yJust": 0.5,
          "xOff": -4,
          "yOff": 0,
          "rot": 90.0,
          "chgo": false,
          "locDesc": "SB I-355 from Boughton Rd Plaza to I-80",
          "tt": "12 minutes",
          "avgTt": "<a href='https://travelmidweststats.com/GCMLink.aspx?GCMLinkID=IL-TIMS-I_355-S-61' class='viewerCell' target='_blank'>13</a>",
          "cng": "Uncongested",
          "len": "14.3 miles",
          "spd": "64 mph",
          "lstUpd": "3/9/18 12:41 PM"
        }
    },
    {
      "type": "Feature",
      "geometry" :{"type":"Point", "coordinates":[-88.0305857,41.7044687]},
      "properties":
        {
          "id":"IL-TESTTSC-222",
          "xJust": 0.5,
          "yJust": 0.5,
          "xOff" :-4,
          "yOff" :-18,
          "rot": -124.99999999999997,
          "chgo": true,
          "locDesc": "SB Stevenson Expy from Dan Ryan to I-355",
          "tt": "48 minutes",
          "avgTt": "<a href='https://travelmidweststats.com/GCMLink.aspx?GCMLinkID=IL-TESTTSC-222' class='viewerCell' target='_blank'>38</a>",
          "cng": "Medium",
          "len": "24.0 miles",
          "spd": "30 mph",
          "lstUpd": "3/9/18 12:40 PM"
        }
    },
    {
      "type": "Feature",
      "geometry": {"type":"Point", "coordinates":[-88.1978323,41.4954258]},
      "properties":
        {
          "id":"IL-TESTTSC-531",
          "xJust": 0.5,
          "yJust": 0.5,
          "xOff": -16,
          "yOff": -18,
          "rot": -180.0,
          "chgo": true,
          "locDesc": "I-55 from Dan Ryan to I-80",
          "tt": "66 minutes",
          "avgTt": "<a href='https://travelmidweststats.com/GCMLink.aspx?GCMLinkID=IL-TESTTSC-531' class='viewerCell' target='_blank'>56</a>",
          "cng": "Light",
          "len": "42.1 miles",
          "spd": "38 mph",
          "lstUpd": "3/9/18 12:40 PM"
        }
    },
    ..... additional travel time features omitted for clarity .....
  ]
}
```

## Congestion

Since there can be thousands of congestion sections in a major metropolitan area such as Chicago and most users will want to update the congestion coloring on their maps periodically, three types of congestion request are supported:

1. Lines — An initial request returns the color, locations and IDs for congestion determined by the request JSON POST parameter.
1. Update — An update request returns the congestion level for a list of congestion IDs without the associated geometry and other properties to improve performance, and is intended to update the congestion for sections already on the map. A JSON POST parameter is used to send a list of congestion IDs with a JSON reply containing the congestion level for each queried ID.
1. Popup — A popup request returns more detailed information about an individual congestion segment given its ID. This information is used in the map popup for congestion. Unlike lines and update reqeusts, this is a GET and not a POST. The congestion ID is provided as a parameter to the request as part of the URL.

### Congestion Lines

The congestion lines request is used to obtain the coordinates, the congestion identifier (id), and the congestion colors (cng).

#### Request

```console
https://travelmidwest.com/lmiga/congestionMap.json?type=lines
```

For obtaining the initial Congestion GeoJSON, the POST parameter for the request is a JSON object with the following fields:

- bbox — see [Bounding Box](#bounding-box) section
- exclude — an array of congestion IDs to exclude from response (the intent of the exclude field is that if the map program caches the congestion features, it is not necessary to request feature already in the cache, e.g. upon a pan)

#### Response

The response for a type=lines Congestion request is a GeoJSON FeatureCollection with additional fields for the congestion section properties and source timestamps. Each congestion section is returned as a GeoJSON MultiLineString, i.e. an array of GeoJSON LineStrings giving a polyline. The response FeatureCollection has the following fields:

- type — "FeatureCollection"
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format
- features — an array of GeoJSON features each with the following fields:
  - type — "Feature"
  - geometry — a GeoJSON MultiLineString  object with the following fields:
    - type — "MultiLineString"
    - coordinates — an array of arrays of arrays [long, lat] giving the sections (polylines)
  - properties — a JSON object with the following fields
    - id — the string congestion ID
    - a — true or false, whether the congestion is on an arterial
    - cng — a single character: "N" for not congested, "L" for light congestion, "M" for medium congestion, "H" for heavy congestion, "U" for unknown congestion
- sourceInformationList — an array of JSON objects with the following fields:
  - name — the source name (Illinois Tollway, IDOT, etc)
  - timestamp — the milliseconds since 1/1/1970

#### Example

```json
{
  "type": "FeatureCollection",
  "timestamp": "2018-03-09 12:31:37",
  "features": [
    {
      "type": "Feature",
      "geometry":
        {
          "type": "MultiLineString",
          "coordinates": [[[-87.6344261,41.8403009],[-87.6344081,41.8412054],[-87.6343991,41.8415873],[-87.6343901,41.8417548],[-87.6343991,41.8417749],
            [-87.6344081,41.8419893],[-87.6344081,41.8420094],[-87.6343991,41.8419826],[-87.6344261,41.8420563],[-87.6344171,41.8420496],
            [-87.6344351,41.8420763],[-87.6344801,41.8421634],[-87.634633,41.8423644],[-87.634588,41.8422907],[-87.6343901,41.8420763],
            [-87.6343272,41.8420295],[-87.6344171,41.8420964],[-87.634552,41.8422036],[-87.634534,41.8421902],[-87.6346689,41.8422706],
            [-87.6346959,41.842284],[-87.6346959,41.842284],[-87.6348218,41.8423309],[-87.6346869,41.842284],[-87.634633,41.8422773],
            [-87.6350467,41.8423577],[-87.6353884,41.8424314],[-87.635892,41.8425319],[-87.6361528,41.8425989],[-87.6377086,41.8429674],
            [-87.6379784,41.843021],[-87.6382033,41.843088],[-87.6382123,41.8430947],[-87.63859,41.8431818],[-87.6386439,41.8431885],
            [-87.6392825,41.8433359],[-87.6395612,41.8434096],[-87.6393994,41.8433694],[-87.6394353,41.8433761],[-87.6403976,41.8436106]]]
        },
      "properties":
        {
          "id": "IL-TESTTSC-DAN_RYAN_EXPRESS-N-5017",
          "cng": "M",
          "a": false,
        }
    },
    {
      "type": "Feature",
      "geometry":
        {
          "type": "MultiLineString",
          "coordinates": [[[-87.6237692,41.7759351],[-87.6235264,41.7756669],[-87.6232745,41.7753114],[-87.6232296,41.7752443],[-87.6230767,41.775023],
            [-87.6228788,41.7746474],[-87.622672,41.7742383],[-87.6224742,41.7737621],[-87.6223123,41.7732189],[-87.6222403,41.7727494],
            [-87.6221594,41.7723335],[-87.6221054,41.7717433],[-87.6220695,41.7712134],[-87.6220335,41.7704354],[-87.6219885,41.7701268]]]
        },
      "properties":
        {
          "id": "IL-TESTTSC-DAN_RYAN-S-5313",
          "cng": "L",
          "a": false,
        }
     },
     {
       "type": "Feature",
       "geometry":
         {
           "type": "MultiLineString",
           "coordinates": [[[-87.6632134,41.9148016],[-87.6628806,41.9142596],[-87.6622871,41.9132825],[-87.6618194,41.912553],[-87.6614777,41.9120243],
             [-87.6612259,41.9116495],[-87.661001,41.9113082],[-87.6609291,41.9112212],[-87.6609111,41.9112011],[-87.6607582,41.9110338],
             [-87.6604435,41.910746],[-87.6599848,41.9103311],[-87.6593193,41.9097421],[-87.6588966,41.9093272],[-87.658366,41.9087382]]]
         },
       "properties":
         {
           "id": "IL-TESTTSC-KENNEDY-E-2032",
           "cng": "H",
           "a": false,
         }
     },
     ..... additional congestion features omitted for clarity .....
  ],
  "sourceInformationList": [
    {"name": "Skyway", "timestamp": 1520620298000},
    {"name": "Chicago DOT", "timestamp": 1520619847096},
    {"name": "InDOT", "timestamp": 1520620311000},
    {"name": "Illinois Tollway", "timestamp": 1520620260046},
    {"name": "IDOT D1", "timestamp": 1520620164098}
  ]
}
```

### Congestion Update

The congestion update request is used to update the map colors for congestion segments.

#### Request

```console
https://travelmidwest.com/lmiga/congestionMap.json?type=update
```

For obtaining the congestion update GeoJSON, the POST parameter for the request is a JSON object with a single field:

- ids — an array of congestion IDs

#### Response

The response for a type=update Congestion request is a JSON object with the following fields:

- updates — an array of JSON objects with the following fields:
  - id — the congestion ID
  - cng — a single character: "N" for not congested, "L" for light congestion, "M" for medium congestion, "H" for heavy congestion, "U" for unknown congestion
- sourceInformationList — an array of JSON objects with the following fields:
  - name — the source name (Illinois Tollway, IDOT, etc)
  - timestamp — the milliseconds since 1/1/1970

#### Example

```json
{
  "updates": [
    {"id": "IL-TESTTSC-I_55-S-6174", "cng": "N"},
    {"id": "IL-TIMS-I_294-S-SEG-9997", "cng": "N"},
    {"id": "IL-TESTTSC-EDENS-N-1132", "cng": "N"},
    {"id": "IL-TESTTSC-I_57-N-9017", "cng": "L"},
    {"id": "IL-CDOT-526", "cng": "L"},
    ..... additional congestion updates omitted for clarity .....
  ],
  "sourceInformationList": [
    {"name": "Skyway", "timestamp": 1520620298000},
    {"name": "Chicago DOT", "timestamp": 1520619847096},
    {"name": "InDOT", "timestamp": 1520620311000},
    {"name": "Illinois Tollway", "timestamp": 1520620260046},
    {"name": "IDOT D1", "timestamp": 1520620164098}
  ],
}
```

### Congestion Popup Data

The congesiton popup request is meant to be used to obtain detailed information on a specific congestion segment once its been clicked on.

#### Request

```console
https://travelmidwest.com/lmiga/congestionMap.json?type=popup&id=[id]
```

Where id is the identifier for the congestion object. This request is meant to be used to populate the congestion popup that appears when a congestion polyline is clicked on. Note this is a GET request so there are no POST parameters to pass. Only the id is needed.

#### Response

The response for a type=popup GET reqeust is a JSON object containing the following information:

- id — the congestion ID
- cng — the congestion level (see above)
- loc — the location description for the congestion
- len — the length in miles of the congestion
- tt — travel time in minutes (authenticated only)
- upd — the formatted update time of the congestion

#### Example

```json
{
  "id":"IL-TESTTSC-STEVENSON-S-6117",
  "cng":"L",
  "loc":"SB I-55 from Cicero Ave (+0.3 miles) to Central Ave (-0.3 miles)",
  "len":"0.6",
  "upd":"8/9/2019 6:50 AM",
  "tt":null
}
```

## Real-time Congestion Data

Real-time congestion data is provided in Illinois only and covers the entire state. As with congestion data, there are three types of data that can be obtained:

1. Encoded lines — An initial request returns the color, locations and IDs for congestion determined by the request JSON POST parameter. The lat/long coordinates are encoded to reduce the bandwidth needed for transmission, see [Google's polyline encoding algorithm](https://developers.google.com/maps/documentation/utilities/polylinealgorithm) for details.
1. Update — An update request returns the congestion level for a list of congestion IDs without the associated geometry and other properties to improve performance, and is intended to update the congestion for sections already on the map. A JSON POST parameter is used to send a list of congestion IDs with a JSON reply containing the congestion level for each queried ID.
1. Popup — A popup request returns more detailed information about an individual congestion segment given its ID. This information is used in the map popup for congestion. Unlike lines and update reqeusts, this is a GET and not a POST. The congestion ID is provided as a parameter to the request as part of the URL.
The "type" request parameter controls the type of data returned as follows.

### Encoded Lines

An initial request returns the color, locations and IDs for congestion determined by the request JSON POST parameter. The lat/long coordinates are encoded to reduce the bandwidth needed for transmission, see [Google's polyline encoding algorithm](https://developers.google.com/maps/documentation/utilities/polylinealgorithm) for details.

```console
https://travelmidwest.com/lmiga/realTimeTrafficMap.json?type=encoded_lines
```

The POST parameter for the request is a JSON object with the following fields:

- bbox — see [Bounding Box](#bounding-box) section
- exclude — an array of real time traffic IDs to exclude from response
- type — "FeatureCollection"
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format
- features — an array of GeoJSON features each with the following fields:
  - type — "MultiLineString"
  - coordinates — an array of arrays of arrays [long, lat]s giving the sections
  - type — "Feature"
  - geometry
    - coordinates[0] — an encoded polyline, see [Google's encoded polyline](https://developers.google.com/maps/documentation/utilities/polylinealgorithm) algorithm for details
    - type — "MultiLineString"
  - properties — a JSON object with the following fields
    - id — the real time traffic ID
    - a — true or false, whether the real time traffic is on an arterial
    - cng — a single character: "N" for not congested, "L" for light congestion, "M" for medium congestion, "H" for heavy congestion, "U" for unknown congestion

### Update

An update request returns the congestion level for a list of congestion IDs without the associated geometry and other properties to improve performance, and is intended to update the congestion for sections already on the map. A JSON POST parameter is used to send a list of congestion IDs with a JSON reply containing the congestion level for each queried ID.

```console
https://travelmidwest.com/lmiga/realTimeTrafficMap.json?type=update
```

The POST parameter for the request is a JSON object with one field:

- ids — an array of real time traffic IDsThe response is a JSON object with the following fields:
- updates — an array of JSON objects with the following fields:
  - id — the real time traffic ID
  - cng — the congestion level (see above)

### Popup

A popup request returns more detailed information about an individual congestion segment given its ID. This information is used in the map popup for congestion. Unlike lines and update reqeusts, this is a GET and not a POST. The congestion ID is provided as a parameter to the request as part of the URL.

```console
https://travelmidwest.com/lmiga/realTimeTrafficMap.json?type=popup&id=[id]
```

The request parameter **id** determines the congestion segment to retreive properties for. The response is a JSON object with the following fields:

- id — the real time traffic ID
- a — true or false, whether the real time traffic is on an arterial
- cng — a single character: "N" for not congested, "L" for light congestion, "M" for medium congestion, "H" for heavy congestion, "U" for unknown congestion
- loc — the location description for the real time traffic
- len — the length in miles of the real time traffic
- upd — the formatted update time of the real time traffic

## Incidents

Two types of incident request are supported: the default returns Point + GeometryCollection features, and `type=lines` returns MultiLineString features suitable for highlighting the affected road segment.

### Request

```console
https://travelmidwest.com/lmiga/incidentMap.json
https://travelmidwest.com/lmiga/incidentMap.json?type=lines
```

The request requires a POST parameter specifying the request bounds as described in the [Bounding Box](#bounding-box) section.

### Response

The response is a GeoJSON FeatureCollection with additional fields for the incident properties. The geometry for an incident event is a GeoJSON FeatureCollection which contains two elements, a Point and a MultiLineString. The location of the MultiLineString is the actual extent of the incident. If the incident is a point location, then the MultiLineString will contain a singe polyline with the same start and end point. The location of the point geometry is midway along that section and is suitable for an incident icon. (Many maps would place an icon at the point and highlight the MultiLineString when the incident is selected.)
The response FeatureCollection has the following fields:

- type — "FeatureCollection"
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format
- features — an array of GeoJSON features each with the following fields:
  - type — "Feature"
  - geometry — an array containing the following fields for its elements:
    - type — "GeometryCollection"
    - geometries — an one item array
      - type — "Point"
      - coordinates — an array [lng, lat] giving the point in decimal degrees
  - properties — a JSON object with the following fields
    - id — the incident ID
    - locDesc — the location description for the incident
    - desc — the description of the incident
    - stat — the status: "Major", "Medium", "Minor", "None", or "Unknown"
    - closure — the lane closure for the incident
    - lanes — "full", "partial", or "clearing"
    - start — the formatted start time of the incident
    - end — the formatted estimated end time of the incident
    - dur — the estimated duration of the incident
    - src — the name of the source agency
    - locDir — local direction used for placing icon on correct side of road (NB, SB, EB, WB, NEB, SEB, NWB, SWB)
    - biDir — "true" if the incident is also on the other side of the road, "false" otherwise

### Example

```json
{
  "type": "FeatureCollection",
  "timestamp": "2018-03-09 12:31:37",
  "features": [
    {
      "type": "Feature",
      "geometry":
        {
          "type": "GeometryCollection",
          "geometries": [
            {"type": "Point ", "coordinates": [-87.82228,41.73606]},
            {"type ": "MultiLineString", "coordinates":[[[-87.82228,41.73606],[-87.82228,41.73606]]]}
          ]
        },
      "properties":
        {
          "id": "IL-TESTTIMS-INCIDENT.2018.3.9.12.3165633",
          "desc": "I-294 Southbound - STALL - North of Roberts Rd - MP 19.0 - 1 right lane blocked of 5",
          "locDesc": "SB I-294 (Tri-State Tollway) at Roberts Rd (-0.3 miles), Hickory Hills, Cook, IL",
          "closure": "Right lane closed, four lanes open",
          "stat": "Updated",
          "start": "3/9/2018 12:24 PM",
          "end": "3/9/2018 1:0 PM",
          "src": "Illinois Tollway TIMS",
          "lanes": "partial",
          "dur": "short",
          "locDir": "SB",
          "biDir": "false"
        }
    }
  ]
}
```

## Construction

As with incidents, a `type=lines` variant is supported that returns MultiLineString features.

### Request

```console
https://travelmidwest.com/lmiga/constructionMap.json
https://travelmidwest.com/lmiga/constructionMap.json?type=lines
```

The request requires a POST parameter specifying the request bounds as described in the [Bounding Box](#bounding-box) section.

### Response

The response is a GeoJSON FeatureCollection with additional fields for the construction properties. Like that for incidents, the geometry for a construction event is a GeoJSON FeatureCollection whcih contains two elements, a Point and a MultiLineString. The location of the MultiLineString is the actual extent of the construction and the location of the point is midway along that section and is suitable for a construction icon.  The response FeatureCollection has the following fields:

- type — "FeatureCollection"
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format
- features — an array of GeoJSON features each with the following fields:
  - type — "GeometryCollection"
  - geometry — a two-element array containing GeoJSON Point and MultiLineString objects with the following fields:
    - type — "Point" for the first, "MultiLineString" for the second
    - coordinates — an array [long, lat] giving the point for the first, an array of arrays of arrays [long, lat]s giving the sections for the second
  - id — the construction ID
  - locDesc — the location description for the construction
  - desc — the description of the construction
  - sev — the severity: "Major", "Medium", "Minor", "None", or "Unknown"
  - closure — the lane closure for the construction
  - time — the time periods for the construction
  - dur — the duration of the construction
  - a — true or false, whether the construction is on an arterial
  - src — the name of the source agency
  - lstUpd — the formatted last update time of the construction
  - mo — true or false, whether the construction is a moving operation
  - type — "Feature"
  - geometry — a GeoJSON GeometryCollection object with the following fields:
  - properties — a JSON object with the following fields

### Example

```json
{
  "type": "FeatureCollection",
  "timestamp": "2018-03-09 12:40:51",
  "features":  [
    {
      "type": "Feature",
      "geometry":
        {
          "type": "GeometryCollection",
          "geometries": [
            {"type": "Point", "coordinates": [-87.9272988,42.3495606]},
            {
              "type": "MultiLineString",
              "coordinates":[
                [[-87.9487026,42.4913346],[-87.9485767,42.4910494],[-87.9483968,42.4905918],[-87.9481271,42.4897695],
                [-87.9479562,42.4891528],[-87.9477763,42.4884233],[-87.9477134,42.4880917],[-87.9476684,42.4878729],[-87.9475605,42.4871633],
                [-87.9474975,42.486573],[-87.9474705,42.4859828],[-87.9474436,42.4855318],[-87.9474256,42.4851273],[-87.9474166,42.4849283],
                [-87.9474436,42.4845967],[-87.9474436,42.4845171],[-87.9474705,42.48396],[-87.9474885,42.4837213],[-87.9475425,42.4829121],
                ..... additional polyline coordinates omitted for clarity ..... ]
              ]
            }
          ]
        },
      "properties":
        {
          "id": "IL-LAKECOUNTY-ROADWORK.2018.3.9.6.3165294",
          "a": false,
          "locDesc": "<span title='EB I-94 from Russell Rd (-0.3 miles), Zion, Lake, IL to IL-22 (-0.4 miles), Lake Forest, Lake, IL'>
            EB I-94 from Russell Rd (-0.3 miles) to IL-22 (-0.4 miles)</span>",
          "desc": "Pavement Repair",
          "sev": "Medium","closure":"All lanes with unknown impact","time":"3/9/18 7:00 AM to 9/30/18 3:00 PM",
          "dur": "205 days",
          "src": "Lake County",
          "mo": false,
          "lstUpd": "3/9/18 7:00 AM"
        }
    }
  ]
}
```

## Cameras

Camera data in JSON format can be accessed in two different files, cameraMap.json and cameras.json:

- cameraMap.json — this file is meant to be used as part of a mapping library such as LeaftLet
- cameras.json — this file is meant to be used for camera reports but it is in GeoJSON format and could also be used for mapping applications
Both files have similar information in them. The sections that follow document both files.

### cameraMap.json

The cameraMap.json file is suitable for placing camera icons on a map.

#### Request

```console
https://travelmidwest.com/lmiga/cameraMap.json
```

The request requires a POST parameter specifying the request bounds as described in the [Bounding Box](#bounding-box) section.

#### Response

The response for a Camera request is a GeoJSON FeatureCollection with additional fields for the camera properties. The xOff, yOff, xJust, and yJust properties can be used to offset the feature from the road so that it does not cover the road or the congestion coloring on the road. The response FeatureCollection has the following fields:

- type — "FeatureCollection"
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format
- features — an array of GeoJSON features each with the following fields:
  - type — "Point"
  - coordinates — an array [long, lat] giving the point
  - id — the string camera ID
  - locDesc — the location description for the camera
  - dis — true or false, whether the camera is disabled
  - age — the formatted image age in minutes and seconds
  - src — the name of the source agency
  - dirs — for a multi-directional camera, an array of the directions ("N", "S", "E", or "W")
  - remUrls — an array of image URLs for the camera if Travel Midwest accesses the camera remotely
  - xOff — an x offset used to place the icon to the side of the road
  - yOff — a y offset used to place the icon to the side of the road
  - xJust — an x justification used to place the icon to the side of the road
  - yJust — a y justification used to place the icon to the side of the road
  - type — "Feature"
  - geometry — a GeoJSON Point object with the following fields:
  - properties — a JSON object with the following fields

### Image URLs

Cameras have a small 176 pixel wide thumbnail for map popup and report purposes and a full-size snapshot image. The URLs for the thumbnail and snapshot depends on whether the remUrls array is empty or not. Cameras with a non-empty remUrls are considered to be "remote" in that another agency is hosting the images for it. Multi-directional cameras have dirs.length > 1.
The follow table details the camera thumbnail and snapshot URLs for each case. The "i" represents the camera direction index into the dirs and remUrls arrays.

|  | Multi-directional?<br>(dirs.length > 0) | Thumbnail | Snapshot |
| --- | --- | --- | --- |
| Not Remote<br>remUrls.length==0 | No | camera?type=thumbnail&id=[id] | snapshot?id=[id] |
| Yes | camera?type=thumbnail?id=[id]&direction=[dir] | snapshot?id=[id]&direction=[dir] |  |
| Remote | N/A | remUrls[i] (CSS width set to 176 pixels) | remUrls[i] |

#### Example

```json
{
  "type": "FeatureCollection",
  "timestamp": "2018-03-09 12:33:48",
  "features": [
    {
      "type": "Feature",
      "geometry": {"type": "Point", "coordinates": [-87.9474,42.2554]},
      "properties":
        {
          "id": "IL-LAKECOUNTY-cam172_30_8_97",
          "locDesc": "IL 21 at S. Artaius",
          "xJust": 0.0,
          "yJust": 0.0,
          "xOff": 0,
          "yOff": 0,
          "age": "6 minutes, 43 seconds ago",
          "src": "Lake County",
          "dis": false,
          "remUrls":["https://www.lakecountypassage.com/snapshots/IL_21_@_S._Artaius_cctv_North_Leg.jpg",
            "https://www.lakecountypassage.com/snapshots/IL_21_@_S._Artaius_cctv_South_Leg.jpg"],
          "dirs":["N","S"]
        }
      },
      {
        "type": "Feature",
        "geometry": {"type":"Point", "coordinates": [-87.6466,41.8748]},
        "properties":
          {
            "id": "IL-IDOT-IK0",
            "locDesc": "Jane Byrne Interchange",
            "xJust": 0.0,
            "yJust": 0.5,
            "xOff": 8,
            "yOff": 0,
            "age": "3 minutes, 51 seconds ago",
            "src": "IDOT D1",
            "dis": false,
            "remUrls": [],
            "dirs":[]
          }
      },
      {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [-87.7385,41.9581]},
        "properties":
          {
            "id": "IL-IDOT-KE7D",
            "locDesc": "Kennedy Expressway and Kostner",
            "xJust": 0.0,
            "yJust" :1.0,
            "xOff": 8,
            "yOff": -4,
            "age": "4 minutes, 11 seconds ago",
            "src": "IDOT D1",
            "dis": false,
            "remUrls": [],
            "dirs": []
          }
      },
      ..... additional camera features omitted for clarity .....
  ]
}
```

### cameras.json

The cameras.json file provides camera data suitable for reports.

#### Request

```console
https://travelmidwest.com/lmiga/cameras.json
```

The following parameters are optional:

| Parameter | Description | Default Value |
| --- | --- | --- |
| state | Name of the state to download camera data for. Supports the following values:<br>Illinois, Indiana, Wisconsin, Michigan, Missouri, Iowa, Missouri, Iowa or Kentucky | Illinois |
| idPrefix | Allows filtering the cameras — only cameras whose ID starts with this value will be returned. Can be specified multiple times to include cameras matching any of the given prefixes. | IL-IDOTD4 |
| maintenance | Whether to return only cameras that need maintenance (images are more than 15 minutes old). | false (POST parameters as specified in the [Bounding Box](#bounding-box) section are not required.) |

#### Response

The cameras.json file is automatically updated with new camera data as the data becomes available to the GTIS. The fields in the file are as follows:

- type – “FeatureCollection”
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format
- features – an array of GeoJSON features with the following fields each
  - geometry – a GeoJSON point objects with
    - type – “Point”
    - coordinates — an array [long, lat]
  - properties
    - id — the string camera ID in the format [state]-[source_name]-[agency_id]
    - description — description of camera's location
    - onRoad – interstate, route, or street name the camera is located on (e.g., “I-474”, “US-24”, “IL-8”, “University St”, etc.)
    - crossRoad — cross road, bridge name, or landmark name the camera is near
    - age — the formatted image age in minutes and seconds
    - urls – an array of
      - direction – n, s, e, w that the camera can face
      - thumbnail – url of a thumbnail sized image for the given direction
      - url – of the full-sized camera image for the given direction
    - state – state camera is in (i.e., “Illinois”)
    - district – IDOT district camera is located in (1, 2, 3, 4, 5, 6, 7, 8, or 9) or “null” if not in Illinois
    - county – name of county camera is in (e.g., “Peoria”, “St Clair”, etc.)
    - city – name of city camera is located in (e.g., “Peoria”, “Springfield”, etc.)
    - bridge – “true” if the camera is on a river bridge, “false” otherwise
    - mileMarker — a decimal amount, the approximate mile marker location of the camera along the 'onRoad'
The camera properties in cameras.json are sufficient to allow camera filtering in a report. Note that the file is in GeoJSON format.
The camera properties will be sorted based on the *onRoad* and *mileMarker* properties as follows:

1. "I-xx" interstates first
1. "US-xx" U.S. Routes next
1. "IL-xx" Illinois routes next
1. By roadName alphabetically
1. By xx route number next (smaller first)
1. By mileMarker next (smaller first)

## Message Signs

### Request

```console
https://travelmidwest.com/lmiga/dmsMap.json
```

The request requires a POST parameter specifying the request bounds as described in the [Bounding Box](#bounding-box) section.

### Response

The response for a Message Sign request is a GeoJSON FeatureCollection with additional fields for the message sign properties. The response FeatureCollection has the following fields:

- type — "FeatureCollection"
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format
- features — an array of GeoJSON features each with the following fields:
  - type — "Point"
  - coordinates — an array [long, lat] giving the point
  - id — the string message sign ID
  - locDesc — the location description for the message sign
  - mm — the mile marker for the message sign
  - stat — the status: "Operational", "Operational but degraded", "Non-operational", "Communication failure", "Down for maintenance", "Unknown", or "Not available"
  - lines — an array of the lines on the message sign
  - msg — an HTML <img> tag whose src attribute is the relative URL of the sign image
  - lstRecd — the formatted last received time of the message sign
  - locDir — the local direction for placing the icon to the side of the road ("NB", "SB", etc.)
  - extOff — the extra offset for placing the icon on the map
  - type — "Feature"
  - geometry — a GeoJSON Point object with the following fields:
  - properties — a JSON object with the following fields

### Example

```json
{
  "type": "FeatureCollection",
  "timestamp": "2018-03-09 12:40:51",
  "features": [
    {
      "type": "Feature",
      "geometry": {"type":"Point", "coordinates":[-88.26764,41.79946]},
      "properties":
        {
          "id": "IL-TESTTIMS-I-88-W-Eola_Road",
          "locDesc": "WB I-88 at Farnsworth Avenue (-0.8 miles)",
          "locDir": "WB",
          "extOff": false,
          "mm": "120.0",
          "stat": "Operational",
          "msg": "<img src='messageSign?id=IL-TESTTIMS-I-88-W-Eola_Road&small=true' width='150'
            alt='TIME TO ORCHARD RD DEKALB TOLL MIN 5 30 . SEE FLASHING LIGHTS MOVE OVER GIVE THEM DISTANCE '/>",
          "lines": ["TIME TO ORCHARD RD DEKALB TOLL MIN 5 30","SEE FLASHING LIGHTS","MOVE OVER","GIVE THEM DISTANCE"],
          "lstRecd": "3/9/18 12:40 PM"
        }
    },
    {
      "type": "Feature",
      "geometry": {"type":"Point", "coordinates":[-87.82099,41.92633]},
      "properties":
        {
          "id": "IL-TESTTSC-GRAND_AV-E-53",
          "locDesc": "EB Grand Ave at 78th Ave",
          "locDir": "EB",
          "extOff": false,
          "mm": "N/A",
          "stat": "Operational",
          "msg": "<img src='messageSign?id=IL-TESTTSC-GRAND_AV-E-53&small=true' width='150' alt='LONG RAILROAD CROSSING DO NOT STOP ON TRACKS '/>",
          "lines": ["LONG RAILROAD CROSSING","DO NOT","STOP ON","TRACKS"],
          "lstRecd": "3/9/18 12:40 PM"}
        },
    {
      "type": "Feature",
      "geometry": {"type":"Point", "coordinates":[-87.93003,41.75045]},
      "properties":
        {
          "id": "IL-TESTTSC-STEVENSON-N-22",
          "locDesc": "NB I-55 at County Line Rd",
          "locDir": "NEB",
          "extOff": false,
          "mm": "275.5",
          "stat": "Operational",
          "msg": "<img src='messageSign?id=IL-TESTTSC-STEVENSON-N-22&small=true' width='150' alt='10 MIN TO HARLEM 26 MIN TO DAN RYAN '/>",
          "lines": ["10 MIN TO HARLEM","26 MIN TO DAN RYAN"],
          "lstRecd": "3/9/18 12:40 PM"
        }
    },
    ..... additional message sign features omitted for clarity .....
  ]
}
```

## Special Events

As with incidents and construction, a `type=lines` variant is supported that returns MultiLineString features.

### Request

```console
https://travelmidwest.com/lmiga/specialEventMap.json
https://travelmidwest.com/lmiga/specialEventMap.json?type=lines
```

The request requires a POST parameter specifying the request bounds as described in the [Bounding Box](#bounding-box) section.

### Response

The response is a GeoJSON FeatureCollection with additional fields for the special event properties. Like that for incidents and construction, the geometry for a special event is a GeoJSON FeatureCollection whcih contains two elements, a Point and a MultiLineString. The location of the MultiLineString is the actual extent of the event and the location of the point is midway along that section and is suitable for a special event icon. The response FeatureCollection has the following fields:

- type — "FeatureCollection"
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format
- features — an array of GeoJSON features each with the following fields:
  - type — "GeometryCollection"
  - geometry — a two-element array containing GeoJSON Point and MultiLineString objects with the following fields:
    - type — "Point" for the first, "MultiLineString" for the second
    - coordinates — an array [long, lat] giving the point for the first, an array of arrays of arrays [long, lat]s giving the sections for the second
  - id — the event ID
  - locDesc — the location description for the event
  - desc — the description of the event
  - sev — the severity: "Major", "Medium", "Minor", "None", or "Unknown"
  - closure — the lane closure for the event
  - time — the time periods for the event
  - dur — the duration of the event
  - src — the name of the source agency
  - lstUpd — the formatted last update time of the event
  - mo — true or false, whether the event is a moving operation
  - type — "Feature"
  - geometry — a GeoJSON GeometryCollection object with the following fields:
  - properties — a JSON object with the following fields

### Example

```json
{
  "type": "FeatureCollection",
  "timestamp": "2018-03-09 15:43:50",
  "features": [
    {
      "type": "Feature",
      "geometry":
        {
          "type": "GeometryCollection",
          "geometries": [
            {"type": "Point", "coordinates": [-87.6242188,41.8894064]},
            {
              "type": "MultiLineString",
              "coordinates": [
                [[-87.6241829,41.8821622],[-87.6241919,41.8824969],[-87.6242008,41.8828317],[-87.6242098,41.8832268],[-87.6242098,41.8832602],
                [-87.6242278,41.8836218],[-87.6242278,41.8837021],[-87.6242458,41.8838695],[-87.6242908,41.8841373],[-87.6243268,41.8842913],
                [-87.6243627,41.8843784],[-87.6244167,41.8844989],[-87.6244617,41.8848471],[-87.6244706,41.8849408],[-87.6244706,41.8849609],
                ..... additional polyline coordinates omitted for clarity ..... ]
              ]
            }
          ]
        },
      "properties":
        {
          "id": "IL-CDOT-SPECIAL_EVENT.2018.3.9.15.3166322",
          "locDesc": "<span title='NB Michigan Ave from Madison St to Chicago Ave, Chicago, Cook, IL'>
            NB Michigan Ave from Madison St to Chicago Ave</span>",
          "desc": "spring parade",
          "sev": "Medium",
          "closure": "All lanes and shoulders closed",
          "time": "3/9/18 1:00 PM to 4:00 PM",
          "dur": "3 hours",
          "src": "Chicago DOT",
          "mo": true,
          "lstUpd": "3/9/18 3:31 PM"
        }
    }
  ]
}
```

## Weather Stations

### Request

```console
https://travelmidwest.com/lmiga/wssMap.json
```

The request requires a POST parameter specifying the request bounds as described in the [Bounding Box](#bounding-box) section.

### Response

The response for a Weather Station request is a GeoJSON FeatureCollection with additional fields for the weather station properties. The response FeatureCollection has the following fields:

- type — "FeatureCollection"
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format
- features — an array of GeoJSON features each with the following fields:
  - type — "Point"
  - coordinates — an array [long, lat] giving the point
  - id — the string message sign ID
  - locDesc — the location description for the message sign
  - stat — the status: "Operational", "Operational but degraded", "Non-operational", "Communication failure", "Down for maintenance", "Unknown", or "Not available"
  - atmos — the atmospheric readings at the weather station
  - precip — the precipitation at the weather station
  - pvmnt — the pavement condition at the weather station
  - tm — the readings time
  - locDir — the local direction for placing the icon to the side of the road ("NB", "SB", etc.)
  - extOff — the extra offset for placing the icon on the map
  - type — "Feature"
  - geometry — a GeoJSON Point object with the following fields:
  - properties — a JSON object with the following fields

### Example

```json
{
  "type": "FeatureCollection",
  "timestamp": "2018-04-17 17:48:58",
  "features": [
    {
      "type": "Feature",
      "geometry": {"type": "Point", "coordinates": [-88.0051,42.13914]},
      "properties":
        {
          "id": "IL-IDOTD4-558008",
          "locDesc": "WB IL-68 at Kennedy Dr (-0.2 miles)",
          "locDir": "WB",
          "extOff": false,
          "stat": "Operational",
          "atmos": "39&#176;F, 49% relative humidity,  wind 0 mph",
          "precip": "none",
          "pvmnt": "dry",
          "tm": "4/17/18 5:41 PM"
        }
      },
      {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [-88.35661,41.68498]},
        "properties":
          {
            "id": "IL-IDOTD4-593006",
            "locDesc": "NEB US-34 at IL-31",
            "locDir": "EB",
            "extOff": false,
            "stat": "Operational but degraded",
            "atmos": "44&#176;F, 41% relative humidity,  wind 4 mph from the northeast with gusts to 6 mph, visibility 1.1 miles",
            "precip": "none",
            "pvmnt": "unknown",
            "tm": "4/17/18 5:40 PM"
          }
        },
        {
          "type": "Feature",
          "geometry": {"type": "Point", "coordinates" :[-88.35661,41.68498]},
          "properties":
            {
              "id": "IL-IDOTD4-558006",
              "locDesc": "NEB US-34 at IL-31",
              "locDir": "EB",
              "extOff": false,
              "stat": "Operational but degraded",
              "atmos": "44&#176;F, 41% relative humidity,  wind 4 mph from the east with gusts to 6 mph, visibility 1.1 miles",
              "precip": "none",
              "pvmnt": "unknown",
              "tm": "4/17/18 5:41 PM"
            }
          },
          ..... additional weather station features omitted for clarity .....
  ]
}
```

## Weather Warnings

### Request

```console
https://travelmidwest.com/lmiga/weatherMap.json
```

The request requires a POST parameter specifying the request bounds as described in the [Bounding Box](#bounding-box) section.

### Response

The response for a Weather Warning request is a GeoJSON FeatureCollection with additional fields for the weather warning type. The response FeatureCollection has the following fields:

- type — "FeatureCollection"
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format
- features — an array of GeoJSON features each with the following fields:
  - properties — a JSON object with the following fields
    - id - identifier that matches weatherReport
    - type — the warning type: "TO" (tornado), "SV" (severe thunderstorm), or "FF" (flash flood)
    - headline - from weather.gov
    - description - full description of the alert
    - sections - description broken down into array of 1 or more sections for the alert
      - heading - heading of the section
      - description - text of the section
    - summary - AI generated summary of the alert
  - type — "Feature"
  - geometry — a GeoJSON Polygon object with the following fields:
    - type — "Polygon"
    - coordinates — an array of array [long, lat]s giving the vertices, the first and last are equal

Note that some sections have a blank ("") heading field.  These sections mostly occur as the first element of the array because there is some preamble text with the asterisk list following it.  Very rarely, there will be an empty heading field in the middle or end of the sections array.

### Example

```json
{
    "type": "FeatureCollection",
    "timestamp": "2023-09-17 08:43:27",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            -88.0299988,
                            41.9900017
                        ],
                        [
                            -88.0299988,
                            41.9900017
                        ]
                    ]
                ]
            },
            "properties": {
                "id": "weather-dot-gov-id-xxx",
                "type": "Flash flood warning",
                "headline": "Flood Warning issued January 29 at 7:06AM EST by NWS Chicago",
                "description": "...Forecast flooding changed from Minor to Moderate severity for the\nfollowing rivers in Ohio...Indiana...\n\nSaint Joseph River Ohio near Newville affecting Allen IN,\nDefiance and De Kalb Counties.\n\n\n\n.Snow melt followed by heavy rain has resulted in rising water on\narea rivers.\n\nFor the Saint Joseph River Ohio...including Newville...Moderate\nflooding is forecast.\n\n* WHAT...Minor flooding is occurring and moderate flooding is\nforecast.\n\n* WHERE...Saint Joseph River Ohio near Newville.\n\n* WHEN...Until further notice.\n\n* IMPACTS...At 14.0 feet, Significant flooding occurs on DeKalb\nCounty Road 42 about 3 miles northeast of Newville. Considerable\nagricultural and low land flooding occurs along the St. Joseph\nRiver to the Cedarville Reservoir.\n\n* ADDITIONAL DETAILS...\n- At 6:45 AM EST Monday the stage was 13.7 feet.\n- Recent Activity...The maximum river stage in the 24 hours\nending at 6:45 AM EST Monday was 13.7 feet.\n- Forecast...The river is expected to rise to a crest of 14.0\nfeet just after midnight tonight.\n- Flood stage is 12.0 feet.\n- http://www.weather.gov/safety/flood",
                "sections": [
                    {
                        "heading": "",
                        "description": "Forecast flooding changed from Minor to Moderate severity for the\nfollowing rivers in Ohio and Indiana. Saint Joseph River Ohio near Newville affecting Allen IN,\nDefiance and De Kalb Counties.  Snow melt followed by heavy rain has resulted in rising water on\narea rivers. For the Saint Joseph River Ohio including Newville. Moderate\nflooding is forecast."
                    },
                    {
                        "heading": "What",
                        "description": "Minor flooding is occurring and moderate flooding is forecast."
                    },
                    {
                        "heading": "Where",
                        "description": "Saint Joseph River Ohio near Newville."
                    },
                    {
                        "heading": "When",
                        "description": "Until further notice."
                    },
                    {
                        "heading": "Impacts",
                        "description": "At 14.0 feet, Significant flooding occurs on DeKalb County Road 42 about 3 miles northeast of Newville. Considerable agricultural and low land flooding occurs along the St. Joseph River to the Cedarville Reservoir."
                    },
                    {
                        "heading": "Additional Details",
                        "description": "- At 6:45 AM EST Monday the stage was 13.7 feet. - Recent Activity...The maximum river stage in the 24 hours ending at 6:45 AM EST Monday was 13.7 feet. - Forecast...The river is expected to rise to a crest of 14.0 feet just after midnight tonight. - Flood stage is 12.0 feet. - http://www.weather.gov/safety/flood"
                    }
                ],
                "summary": "Moderate flooding is forecast for the Saint Joseph River near Newville, Ohio, affecting Allen, Defiance, and De\nKalb Counties. Rising water is due to snow melt and heavy rain. Significant flooding is expected at 14.0 feet,\nimpacting DeKalb County Road 42 and surrounding agricultural areas."
            }
        }
    ]
}
```

## Mile Markers

> [!NOTE]
> The mile marker database is known to be missing many mile markers. We are working on this.

### Request

```console
https://travelmidwest.com/lmiga/milepostsMap.json
```

The request requires a POST parameter specifying the request bounds as described in the [Bounding Box](#bounding-box) section.

### Response

The response for a Mile markers POST request is a GeoJSON FeatureCollection with fields for the mile marker details. The response FeatureCollection has the following fields:

- type — "FeatureCollection"
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format (CST)
- features — an array of GeoJSON features, each with the following fields:
  - type — "Point"
  - coordinates — and array containing two elements, the longitude and latitude in decimal degrees
  - properties — a JSON object with the following fields:
    - expressway — the name of the expressway the mile marker is on
    - mieMarker — the mile post number in whole miles
    - crossStreet — the nearest cross street's name
    - offset — the offset in miles from the mile marker to the corss street, positive if east or south wards
    - municipality — the name of the city the marker is in
    - county — the name of the county the marker is in
    - locDir — the direction (EB or SB), only eastbound and southbound markers are provided

## Road Labels

The underlying base map is expected to contain road labels, but these will be covered up by other map data elements. The roadLabels.json endpoint is meant to be used for placing Interstate icons on the map above the congestion lines and other map data.

### Request

```console
https://travelmidwest.com/lmiga/roadLabels.json
```

One POST parameter named "request" is required with the following fields:

- boundingBox — see the [Bounding Box](#bounding-box) section
- zoom — zoom level in pixels per projected coordinate width (approximately meters in Mercator coordinates). The *zoom* parameter can be calculated from a LeafLet Map object as follows:

Leaflet Javascript Code to Compute Zoom Parameter:

```javascript
var bounds = map.getBounds();
var mercatorWidth = L.Projection.Mercator.project(bounds.getNorthEast()).x — L.Projection.Mercator.project(bounds.getNorthWest()).x;
var zoom = map.getSize().x / mercatorWidth;
```

### Response

The response for a roadLabels.json request is a GeoJSON FeatureCollection with fields for the road labels that match the bounding box and zoom input parameters.

- type — "FeatureCollection"
- timestamp — the timestamp in yyyy-MM-dd HH:mm:ss format (CST)
- features — an array of GeoJSON features, each with the following fields:
  - type — "Point"
  - coordinates — an array containing two elements, the longitude and latitude in decimal degrees
- properties — a JSON object
  - label — text "XXX" for Interstate number XXX

### Example

```json
{
   "boundingBox" : {
      "bbox" : [
         -88.2339477539063,
         41.6062013751795,
         -87.2444915771484,
         42.0452134550104
      ]
   },
   "zoom" : 0.0130826645466792
}
```

```json
{
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -88.1725435,
                    41.8061888
                ]
            },
            "properties": {
                "label": "88"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -88.1428479,
                    41.6468955
                ]
            },
            "properties": {
                "label": "55"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -87.9907009,
                    41.7251921
                ]
            },
            "properties": {
                "label": "55"
            }
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -87.908503,
                    41.7967025
                ]
            },
            "properties": {
                "label": "294"
            }
        },
        .
        .
        .
    ]
}
```

## Transit Events

### Request

```console
https://travelmidwest.com/lmiga/transitEventMap.json
```

Both GET and POST methods are supported.

**POST** — The request body specifies the bounding box as described in the [Bounding Box](#bounding-box) section. Returns all transit events within the bounds.

**GET** — Returns transit events without a bounding box filter. The following query parameters are supported:

- **agency** (optional, default "ALL") — filter by agency: "CTA", "METRA", "ALL", or empty. Case insensitive.
- **noBus** (optional, default "FALSE") — set to "TRUE" to exclude bus-related events
- **noTrivial** (optional, default "FALSE") — set to "TRUE" to exclude low-severity events

### Response

The response is a GeoJSON FeatureCollection with additional fields for the transit event properties. The geometry for a transit event is a GeoJSON FeatureCollection which contains one or more geometries of types Point and  MultiLineString. The response FeatureCollection has the following fields:

- id — ID of the event
- eventUrl — link to transit agency's web site where information of the event can be found
- cause — cause of the event
- effect — effect of the event
- header — short description of the event
- description — description of the event
- severity — severity of the event
- impactedRoutes — ID list of routes impacted by the event
- impactedSTops — ID list of stops or stations impacted by the event
- timePeriods: time periods when the event will be active

### Example

```json
{
  "type" : "FeatureCollection",
  "timestamp" : "2023-11-08 17:12:03",
  "features" : [ {
    "type" : "Feature",
    "geometry" : {
      "type" : "GeometryCollection",
      "geometries" : [ {
        "type" : "MultiLineString",
        "coordinates" : [ [ [ -87.63898127098, 41.87879145493 ], [ -87.63892878377, 41.88306171354 ], [ -87.63893247695, 41.88346240086 ], [ -87.63894655595, 41.88426038555 ], [ -87.63892053992, 41.88542477344 ], [ -87.63895124107, 41.88572648684 ], [ -87.63897387994, 41.88584016832 ], [ -87.63910378361, 41.88624333384 ], [ -87.63952541844, 41.88688392103 ], [ -87.6398581971, 41.88737475639 ], [ -87.63996169038, 41.88753312672 ], [ -87.6401305275, 41.88767955619 ], [ -87.64030468093, 41.88780768242 ], [ -87.64050747758, 41.88791101961 ], [ -87.6406108095, 41.88794645711 ], [ -87.64062731957, 41.88794792885 ], [ -87.64071850367, 41.88796562296 ], [ -87.64081030124, 41.88797811997 ], [ -87.64091219737, 41.88797942051 ], [ -87.64115087553, 41.8879822316 ], [ -87.64290406502, 41.88801325483 ], [ -87.64674752783, 41.88793144413 ], [ -87.6472569467, 41.88794375079 ], [ -87.64762790203, 41.88798301427 ], [ -87.65057354052, 41.88838202084 ], [ -87.6508062749, 41.88840432951 ], [ -87.65162865063, 41.88847101819 ], [ -87.65370991047, 41.88843807424 ], [ -87.65448868256, 41.88843993642 ], [ -87.65735216851, 41.88842782446 ], [ -87.66038278974, 41.88856924931 ], [ -87.66096497352, 41.88858192156 ], [ -87.66609568334, 41.88865808776 ], [ -87.6680378721, 41.88864465803 ], [ -87.66817466346, 41.88864545047 ], [ -87.66927711283, 41.88864359822 ], [ -87.67153630205, 41.88860587138 ], [ -87.67438348023, 41.88857421997 ], [ -87.68350703509, 41.88844482573 ], [ -87.68483155658, 41.88843518356 ], [ -87.68529323035, 41.88841611163 ], [ -87.6858214819, 41.88847171591 ], [ -87.68613772582, 41.88848019445 ], [ -87.68632580669, 41.88849261856 ], [ -87.68684947778, 41.88853838329 ], [ -87.68734059405, 41.88866201866 ], [ -87.68842046637, 41.88904747082 ], [ -87.68862446212, 41.88912797737 ], [ -87.68977606739, 41.88960405316 ], [ -87.690860822, 41.89001868307 ], [ -87.6914434851, 41.89026069444 ], [ -87.69205244157, 41.8905134838 ], [ -87.69233240843, 41.89062747568 ], [ -87.69267304358, 41.89075712741 ], [ -87.70124533853, 41.89411793257 ], [ -87.70166184356, 41.89432697855 ], [ -87.70221751631, 41.8945891909 ], [ -87.70372988222, 41.89535678875 ], [ -87.70582039963, 41.89643384639 ], [ -87.70683792399, 41.89696150217 ], [ -87.70733287513, 41.89721804764 ], [ -87.70866848136, 41.8980403727 ], [ -87.7112511061, 41.899882084 ], [ -87.71372226707, 41.90189325619 ], [ -87.71517372269, 41.90331438336 ], [ -87.71641248306, 41.90460914152 ], [ -87.71762125498, 41.90609102197 ], [ -87.71881964145, 41.9077305133 ], [ -87.71961735359, 41.90891962144 ], [ -87.72029086572, 41.90996604441 ], [ -87.72078220733, 41.91089638421 ], [ -87.72149120111, 41.91222290433 ], [ -87.72178812729, 41.91309525556 ], [ -87.72204773025, 41.91358649034 ], [ -87.7226878356, 41.91479874767 ], [ -87.72367442415, 41.91666769283 ], [ -87.72724274194, 41.9235263297 ], [ -87.72770491394, 41.92447896373 ], [ -87.73061393687, 41.93003220502 ], [ -87.73375203559, 41.93606543096 ], [ -87.74041296154, 41.94887121031 ], [ -87.74225328648, 41.95257608609 ], [ -87.74244332914, 41.95294582343 ], [ -87.74313220999, 41.95428444608 ], [ -87.74620185465, 41.96013143652 ], [ -87.7471167986, 41.9619851212 ], [ -87.74732022172, 41.9623806411 ], [ -87.74952426179, 41.96644705786 ], [ -87.74991799875, 41.96739616779 ], [ -87.75004606599, 41.96759097402 ], [ -87.75195383063, 41.9713479192 ], [ -87.75494718125, 41.97709046382 ], [ -87.75547571344, 41.97801916212 ], [ -87.75672165512, 41.98048391501 ], [ -87.75761963585, 41.98220254378 ], [ -87.76011910201, 41.98702568258 ], [ -87.76321756814, 41.9929659216 ], [ -87.7655658348, 41.99751450704 ], [ -87.76571586872, 41.99781488773 ], [ -87.76826327144, 42.00267290063 ], [ -87.77092208075, 42.00784030959 ], [ -87.7742562747, 42.01428501408 ], [ -87.77644094753, 42.01852002677 ], [ -87.7769514792, 42.01950321986 ], [ -87.77787973783, 42.02123279192 ], [ -87.77858350295, 42.02258841172 ], [ -87.77875793659, 42.02292267779 ], [ -87.78138222997, 42.02796548671 ], [ -87.78512994287, 42.03529327517 ], [ -87.78696831851, 42.03873231199 ], [ -87.79054211157, 42.045637845 ], [ -87.79375418067, 42.05178168334 ], [ -87.79697400009, 42.05795339063 ], [ -87.80117984877, 42.06610450186 ], [ -87.80535600352, 42.07415615955 ], [ -87.80702251935, 42.07725782063 ], [ -87.80845647171, 42.08011269007 ], [ -87.81085704658, 42.08574537962 ], [ -87.81413531796, 42.09359405948 ], [ -87.81599650254, 42.09820080647 ], [ -87.81721294711, 42.10117600089 ], [ -87.81890682038, 42.10532904243 ], [ -87.81941140018, 42.10658745376 ], [ -87.82134630391, 42.11130649337 ], [ -87.82144162648, 42.11153983108 ], [ -87.82246088029, 42.11401120929 ], [ -87.82442456268, 42.11872909398 ], [ -87.82462741169, 42.1192220707 ], [ -87.82483093554, 42.11969737276 ], [ -87.82533162898, 42.12104870985 ], [ -87.82555598516, 42.12157075357 ], [ -87.82648761576, 42.12371653077 ], [ -87.82697774266, 42.12497484155 ], [ -87.82777190484, 42.12685330166 ], [ -87.82797677536, 42.1273563774 ], [ -87.82951361745, 42.1311003692 ], [ -87.83060619277, 42.13377703761 ], [ -87.8315490878, 42.13601903662 ], [ -87.83217859776, 42.13742200088 ], [ -87.83303851439, 42.1388609546 ], [ -87.84066719952, 42.15125198925 ], [ -87.84545522865, 42.15894692996 ], [ -87.84742008823, 42.16213540728 ], [ -87.84794542722, 42.16311052355 ], [ -87.84968940602, 42.16778810229 ], [ -87.85442677764, 42.18129487747 ], [ -87.86903796118, 42.2121673711 ], [ -87.87752288334, 42.22981017348 ], [ -87.88688815866, 42.24940722319 ], [ -87.88821697871, 42.25226793965 ], [ -87.88880523986, 42.25345102249 ], [ -87.88975973621, 42.25539633648 ], [ -87.89084302239, 42.25863522497 ], [ -87.89102962819, 42.25927497674 ], [ -87.8914509766, 42.26085237187 ], [ -87.89171192199, 42.2616729932 ], [ -87.89207856315, 42.26298957421 ], [ -87.89257941742, 42.26470211179 ], [ -87.89411137474, 42.27011869108 ], [ -87.89576118484, 42.27596825893 ], [ -87.89614075092, 42.27731569113 ], [ -87.89660546944, 42.27890870063 ], [ -87.89699848418, 42.28025343648 ], [ -87.89706713065, 42.28051301559 ], [ -87.89714616884, 42.28073936197 ], [ -87.89730505914, 42.28114129175 ], [ -87.8976067969, 42.2815257897 ], [ -87.89792375423, 42.2819482142 ], [ -87.89835860781, 42.28238892205 ], [ -87.89869559018, 42.28266138099 ], [ -87.89936655481, 42.28312699052 ], [ -87.89989355084, 42.28344389464 ], [ -87.90061966762, 42.2837702829 ], [ -87.90123684278, 42.28400588425 ], [ -87.90164901008, 42.28412166058 ], [ -87.90236649472, 42.284286666 ], [ -87.90312710958, 42.2843661974 ], [ -87.9041685084, 42.28441553638 ], [ -87.93440978916, 42.28628057936 ], [ -87.9372241425, 42.28646630043 ], [ -87.93827564786, 42.2865137397 ], [ -87.93941412421, 42.28659805614 ], [ -87.94053383101, 42.28682759937 ], [ -87.94099024182, 42.28691747543 ], [ -87.94154667291, 42.28705040865 ], [ -87.94246686217, 42.28735775234 ], [ -87.94366607372, 42.28786062116 ], [ -87.94969935831, 42.29033571117 ], [ -87.95047523656, 42.29053589845 ], [ -87.95114591315, 42.29063525963 ], [ -87.95415832554, 42.29064917937 ], [ -87.95546483806, 42.29083580619 ], [ -87.9564457378, 42.2911066173 ], [ -87.976636141, 42.29948095119 ], [ -87.97836207898, 42.30018537764 ], [ -87.97920573591, 42.30051486903 ], [ -87.97980912307, 42.30071967737 ], [ -87.98065462936, 42.30095997335 ], [ -87.98378447946, 42.30149924148 ], [ -87.98547654167, 42.30173153605 ], [ -87.98687265653, 42.30209544694 ], [ -87.98767304599, 42.30238130835 ], [ -87.98848972886, 42.30271725509 ], [ -87.98929594497, 42.30311432815 ], [ -87.99642170973, 42.30720999908 ], [ -87.99797290406, 42.30809008052 ], [ -87.99902157361, 42.30874258543 ], [ -87.99964836716, 42.30915623145 ], [ -88.00010035399, 42.3094843696 ], [ -88.0010124181, 42.31024495642 ], [ -88.00249683888, 42.31191357764 ], [ -88.00442592019, 42.31415315318 ], [ -88.00532838116, 42.31498557086 ], [ -88.00632978597, 42.31571321516 ], [ -88.00735174792, 42.31635755743 ], [ -88.01127480693, 42.31862311209 ], [ -88.01555170323, 42.32116590221 ], [ -88.02381674161, 42.32600260404 ], [ -88.02510164164, 42.32673981786 ], [ -88.02553629892, 42.32694473393 ], [ -88.02827762265, 42.32798287724 ], [ -88.04294528808, 42.3334075929 ], [ -88.05531581933, 42.33802111997 ], [ -88.06796776366, 42.34269672616 ], [ -88.08982638461, 42.3527066919 ], [ -88.09486983586, 42.35503443752 ], [ -88.09621997454, 42.35563887593 ], [ -88.09727409942, 42.3561185079 ], [ -88.09837145496, 42.35664756445 ], [ -88.10104734825, 42.35839841685 ], [ -88.10344605556, 42.36007091587 ], [ -88.10434011306, 42.3605566909 ], [ -88.10545302516, 42.36104603482 ], [ -88.11121724223, 42.36350107355 ], [ -88.11226505757, 42.3639452091 ], [ -88.11267685932, 42.36409486807 ], [ -88.11384264558, 42.3644174757 ], [ -88.12482481896, 42.36705604889 ], [ -88.12666619707, 42.36753685047 ], [ -88.12680045352, 42.36757036421 ], [ -88.12791382814, 42.36782187866 ], [ -88.12885875079, 42.36813521511 ], [ -88.12951113764, 42.36835727408 ], [ -88.13495657659, 42.37111590168 ], [ -88.1379887891, 42.37261940722 ], [ -88.13985912237, 42.37386843268 ], [ -88.14079299923, 42.37464821003 ], [ -88.1411359787, 42.3749605803 ], [ -88.14579495641, 42.37888040707 ], [ -88.14945682373, 42.38194356437 ], [ -88.15111200872, 42.38294340881 ], [ -88.1532441914, 42.38370469824 ], [ -88.15561397676, 42.38418205405 ], [ -88.15662741252, 42.38438039184 ], [ -88.1607974327, 42.38508941975 ], [ -88.1633347813, 42.3856653483 ], [ -88.16725686204, 42.3876031789 ], [ -88.17055128827, 42.38932265815 ], [ -88.17358728817, 42.39071310151 ], [ -88.17775898178, 42.39239447365 ], [ -88.1790132677, 42.39323465003 ], [ -88.180543803, 42.39496980995 ], [ -88.18180906032, 42.39679696628 ], [ -88.1823738185, 42.3983062851 ] ] ]
      } ]
    },
    "properties" : {
      "id" : "IL-METRA-ALERT-2",
      "eventUrl" : "https://metrarail.com/maps-schedules/train-lines/MD-N?Twitter=1&Email=1&SMS=0&Website=1&OnBoard=0>fsrt=1",
      "cause" : "Unknown Cause",
      "effect" : "Unknown Effect",
      "header" : "MDN 2125 delayed",
      "description" : "Milwaukee North Outbound train 2125 due into Fox Lake at 5:38 p.m. may be 15 to 20 minutes behind schedule due to mechanical problems.",
      "severity" : "UNKNOWN_SEVERITY",
      "impactedRoutes" : [ "IL-METRA-ROUTE-MD-N" ],
      "impactedStops" : [ ],
      "timePeriods" : [ ]
    }
  } ]
}
```

## Truck Parking

Truck parking information management systems (TPIMS) provide truck parking availability within the GTIS coverage area.  The following states provide truck parking data:

- Illinois
- Indiana
- Iowa
- Kentucky
- Michigan
- Wisconsin

### Request

```console
https://travelmidwest.com/lmiga/tpimsMap.json
```

The request requires a POST parameter specifying the request bounds as described in the [Bounding Box](#bounding-box) section.

### Response

The response is a GeoJSON FeatureCollection with additional fields for the truck parking lot properties. The geometry for a truck parking lot is a GeoJSON Point. The response FeatureCollection has the following fields:

- siteId - unique string identifying the parking lot
- timestamp - string timestamp of when lot availability data was last updated is ISO 8601 format
- availableSpots - string representing number of stalls open for parking
- capacity - string representing number of stalls in parking lot
- exit - highway exit to reach parking lot
- highway - string name of highway or expressway lot is located on
- milePost - string milepost number where lot is located on highway
- amenities - array of strings representing amenities at the parking lot
- images - array of string URLs of images for parking lot
- trustData - boolean true or false
- open - boolean true or false
- trend - string Clearing, Steady, Filling, or Unknown

### Example

```json
{
    "type": "FeatureCollection",
    "timestamp": "2024-03-12 08:16:58",
    "features": [{
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-89.2450395, 40.6124998]
            },
            "properties": {
                "siteId": "IL00074IE011400005",
                "availableSpots": "17",
                "capacity": "25",
                "timestamp": "2024-03-12T13:16:58.784Z",
                "exit": "",
                "highway": "EB I-74",
                "milePost": "114.0",
                "amenities": [],
                "images": [],
                "trustData": true,
                "open": true,
                "trend": "Clearing"
            }
        }, {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-90.0894901, 40.8802148]
            },
            "properties": {
                "siteId": "IL00074IW006200004",
                "availableSpots": "2",
                "capacity": "12",
                "timestamp": "2024-03-12T13:16:58.909Z",
                "exit": "",
                "highway": "WB I-74",
                "milePost": "62.0",
                "amenities": [],
                "images": [],
                "trustData": true,
                "open": true,
                "trend": "Filling"
            }
        }
    }]
}
```

## Winter Road Conditions

The Winter Road Condition API provides near–real-time winter roadway condition information across multiple states within the GTIS coverage area.  The data is aggregated from state DOT winter condition feeds and normalized into a single GeoJSON response format that supports varying classification systems.

This service is designed to support multi-state feeds, including states with different winter condition taxonomies (e.g., Illinois and Iowa).

### Request

```console
[https://travelmidwest.com/lmiga/winterConditionMap.json](https://travelmidwest.com/lmiga/winterConditionMap.json)
```

Both GET and POST methods are supported. A POST body specifying the geographic bounding box is optional — if omitted (or when using GET), all winter condition features are returned. Optional query parameters can be used to filter the results.

#### Query Parameters

- **minimumConditionLevel** (optional, integer)
  Filters returned features to only those at or above the specified severity level.
  Typical values range from `1` (least severe) upward, depending on the source data.

#### POST Body

The POST body must include a bounding box as described in the [Bounding Box](#bounding-box) section.

```json
{
"bbox": [-93, 39, -86, 43]
}
```

### Response

The response is a **GeoJSON FeatureCollection** containing winter road condition features.
Each feature represents a roadway segment affected by winter conditions.

The geometry type is typically **MultiLineString**, representing one or more connected roadway segments.

```json
{
"type": "FeatureCollection",
"features": [ ... ]
}
```

### Feature Properties

Each Feature in the FeatureCollection contains a `properties` object with the following fields:

- **gid**
  Internal unique identifier.

- **objectId**
  Identifier provided by the source agency.

- **conditionType**
  String describing the reported winter road condition classification.  Examples include:
  - Clear
  - Partially Covered
  - Mostly Covered by Snow or Ice
  - Covered by Snow or Ice
  - Partially Covered with Ice
  - Completely Covered with Ice
  - Travel Not Advised
  - Impassable or Closed
  - Towing Not Recommended (Availability varies by state.)
- **state**
  Two-letter state abbreviation (e.g., `IL`, `IA`).

- **district**
  Administrative district, if provided by the source feed.

- **adminLevel1**
  Administrative level 1 area (commonly county).
  Used instead of explicit county naming to support states with differing schemas.

- **adminLevel2**
  Administrative level 2 area (commonly city or sub-county area), when available.

- **location**
  Human-readable location description as provided or derived from the source feed.
  Formatting is source-dependent and may not be normalized.

- **segmentIds**
  Array of roadway segment identifiers associated with the condition.

- **lastUpdated**
  Timestamp indicating when the condition was last updated by the source system, in ISO 8601 format.

- **conditionLevel**
  Integer representing the severity level of the condition.
  Used for filtering via the `minimumConditionLevel` request parameter.

### Geometry

- **type**: `MultiLineString`
- **coordinates**:
  An array of line strings, each consisting of `[longitude, latitude]` coordinate pairs.

The geometry represents the spatial extent of the affected roadway segment(s).

### Example

The following is a simplified example excerpt of the response structure:

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "MultiLineString",
        "coordinates": [
          [ [-87.83540, 42.15268], [-87.83519, 42.15237] ]
        ]
      },
      "properties": {
        "gid": 12345,
        "objectId": "IL-DOT-98765",
        "conditionType": "Partially Covered",
        "conditionLevel": 2,
        "state": "IL",
        "district": "1",
        "adminLevel1": "Lake",
        "adminLevel2": "Waukegan",
        "location": "I-94 between IL 132 and IL 173",
        "segmentIds": ["SEG123", "SEG124"],
        "lastUpdated": "2025-12-22T14:31:09Z"
      }
    }
  ]
}
```

### Notes

- Condition classifications vary by state; not all condition types are available in every jurisdiction.
- Administrative area text is provided as-is from source feeds and may not be normalized.
- Visualization decisions (colors, symbols, patterns) are intentionally left to the client application layer.
- The API is designed to accommodate additional states and expanded classification systems without breaking schema compatibility.

### Recommended Colors

The following colors are recommended for consistent rendering across multiple traffic information web portals.

- Seasonal (green / not displayed) - matches IDOT Clear
- Partially Covered (blue) - matches IDOT Partly covered by snow or ice
- Partially Covered with Ice (blue with white dots) - IaDOT only
- Mostly covered by snow or ice (dark blue?) - IDOT only
- Completely Covered (pink) - matches IDOT Covered by snow or ice
- Completely Covered with Ice (pink with white dots) - IaDOT only
- Travel Not Advised (purple) - IaDOT only
- Impassable or Closed (red with black dots) - IaDOT only
- Towing Not Recommended (light blue shaded county shape) - IaDOT only

## Alerts

The alertsMap.json endpoint provides high-priority alert features for display on the map. Alerts include severe weather, major incidents, and other high-priority notifications.

### Request

```console
https://travelmidwest.com/lmiga/alertsMap.json
```

The request requires a POST parameter with the following fields:

- bbox — see [Bounding Box](#bounding-box) section
- includeGeneralAlerts — (optional, boolean, default true) whether to include general (non-geo-located) alerts
- highestOnly — (optional, boolean, default false) whether to return only the highest priority alerts

### Response

The response is a GeoJSON FeatureCollection with the following feature properties:

- text — the alert text
- incidentId — associated incident ID, if any
- mapName — the map name the alert is associated with
- priority — the alert priority level
- latitude — the latitude of the alert
- longitude — the longitude of the alert
- active — true or false, whether the alert is currently active

## Events by ID

The eventMap.json endpoint retrieves features for specific events (incidents, construction, special events, or cameras) by their external IDs. This is used to display specific events on the map by ID rather than by bounding box.

### Request

```console
https://travelmidwest.com/lmiga/eventMap.json
```

The request requires a POST parameter with the following field:

- ids — a comma-delimited string of external IDs (incident, roadwork, special event, or camera IDs)

### Response

The response is a GeoJSON FeatureCollection containing features for the requested IDs. Each feature's geometry and properties match the format of its source type (incident, construction, special event, or camera).

## Ferry

The ferryMap.json endpoint provides ferry crossing locations and status.

### Request

```console
https://travelmidwest.com/lmiga/ferryMap.json
```

This is a GET request with no parameters required.

### Response

The response is a GeoJSON FeatureCollection with Point features for each ferry crossing. The feature properties include:

- id — the ferry identifier
- name — the ferry name
- description — description of the ferry service
- status — the ferry's operational status

## Construction (WZDx)

The constructionWzdxMap.json endpoint returns construction data from both the GTIS roadwork database and WZDx (Work Zone Data Exchange) feeds. It extends the standard constructionMap.json with additional WZDx-specific fields.

### Request

```console
https://travelmidwest.com/lmiga/constructionWzdxMap.json
```

The request is a POST with optional query parameters and a JSON body:

#### Query Parameters

- **agency** (optional) — filter by agency: "TIMS", "WISDOT", or omit for all
- **type** (optional) — filter by data source: "Roadwork", "WZDx", or omit for all

#### POST Body

- bbox — see [Bounding Box](#bounding-box) section (optional)

### Response

The response is a GeoJSON FeatureCollection with the same construction feature format as constructionMap.json. Feature properties include:

- id — the construction ID
- locDesc — the location description
- desc — the description
- sev — the severity
- closure — the lane closure
- time — the time periods
- dur — the duration
- src — the source agency name
- mo — true or false, whether it is a moving operation
- lstUpd — the formatted last update time
- restrictions — WZDx restrictions, if applicable
- auth — the authorizing agency, if applicable

## WZDx Data Feed

The wzdxData.json endpoint serves the raw WZDx (Work Zone Data Exchange) feed containing work zone data from Tollway and WisDOT WZDx sources, with optional inclusion of GTIS roadwork data converted to WZDx format.

### Request

```console
https://travelmidwest.com/lmiga/wzdxData.json
```

Both GET and POST methods are supported.

#### Query Parameters

- **agency** (optional) — filter by agency
- **includeRoadWork** (optional, boolean, default false) — set to true to include GTIS roadwork data converted to WZDx format

#### POST Body

- bbox — see [Bounding Box](#bounding-box) section (optional — if omitted, all WZDx features are returned)

### Response

The response is a WZDx-format GeoJSON FeatureCollection. Each feature represents a work zone in WZDx v4 format. The response has the same structure as the [Illinois WZDx Feed](#illinois-wzdx-feed) but is not filtered to Illinois-only sources.

## Illinois WZDx Feed

The illinoisWzdx.json endpoint serves the Illinois-filtered WZDx (Work Zone Data Exchange) feed. This feed contains the same data that is uploaded to the Trihydro SDX: Illinois sources only, Tollway excluded, with geometry and property corrections applied.

### Request

```console
https://travelmidwest.com/lmiga/illinoisWzdx.json
```

Both GET and POST methods are supported.

#### Query Parameters

- **agency** (optional) — filter by agency

#### POST Body

- bbox — see [Bounding Box](#bounding-box) section (optional — if omitted, all Illinois WZDx features are returned)

### Response

The response is a WZDx-format GeoJSON FeatureCollection with an additional `feed_info` object. Each feature represents a work zone in WZDx v4 format.

- type — "FeatureCollection"
- feed_info — a JSON object with WZDx feed metadata (publisher, version, update frequency, etc.)
- features — an array of WZDx work zone features each with the following fields:
  - type — "Feature"
  - geometry — a GeoJSON geometry object (typically LineString or MultiLineString)
  - properties — a WZDx work zone properties object including:
    - core_details — WZDx core details (event type, description, direction, road names, etc.)
    - start_date — ISO 8601 start date of the work zone
    - end_date — ISO 8601 end date of the work zone
    - vehicle_impact — the impact on vehicles (e.g., "some-lanes-closed")
    - restrictions — array of WZDx restriction objects, if applicable

## Vehicle Detection Stations

Vehicle Detection Stations (VDS) provide real-time traffic flow data including speed, occupancy, and volume. Two request modes are supported.

### Map Data

#### Request

```console
https://travelmidwest.com/lmiga/vdsMap.json?type=map
```

The request requires a POST parameter specifying the request bounds as described in the [Bounding Box](#bounding-box) section.

#### Response

The response is a GeoJSON FeatureCollection with Point features for each VDS within the bounding box. Feature properties include:

- id — the VDS external ID
- location — the location description
- direction — the direction of travel
- mileMarker — the mile marker
- status — the operational status
- updated — the last update time
- speed — the current speed reading
- occupancy — the current occupancy reading
- volume — the current volume reading

### Metadata

#### Request

```console
https://travelmidwest.com/lmiga/vdsMap.json?type=metaData&id=[id]
```

This is a GET request. The **id** parameter specifies the VDS external ID.

#### Response

The response is a GeoJSON FeatureCollection with a single Point feature for the requested VDS, with the same properties as the map data response.

## Transit Stops

### Request

```console
https://travelmidwest.com/lmiga/transitStopMap.json
```

The request requires a POST parameter with the following fields:

- bbox — see [Bounding Box](#bounding-box) section (optional)
- noBus — (optional, boolean, default false) set to true to exclude bus stops and show only rail/train stations

### Response

The response is a GeoJSON FeatureCollection containing Point features for transit stops within the bounding box.

## Transit Routes

### Request

```console
https://travelmidwest.com/lmiga/transitRouteMap.json
```

This is a GET request with the following query parameter:

- **routeIdCsv** (required) — comma-separated list of route IDs

### Response

The response is a GeoJSON FeatureCollection containing features for the specified transit routes.

## Rest Areas

> [!NOTE]
> This endpoint is present in the application but is not yet deployed to
> travelmidwest.com; it currently returns 404 there.

The restAreaMap.json endpoint provides rest area locations and whether each is open.

### Request

```console
https://travelmidwest.com/lmiga/restAreaMap.json
```

GET or POST. The POST body may contain:

- bbox — see [Bounding Box](#bounding-box) section (optional; all rest areas are returned when omitted)

### Response

The response is a GeoJSON FeatureCollection with a Point feature for each rest area.
Rest areas with no latitude or longitude are omitted. The collection timestamp is the
last update time of the rest area data. Feature properties:

- externalId — the rest area identifier
- name — the rest area name
- address — the street address. Illinois records populate a location field and Iowa
  records an address field; this property carries whichever is present, preferring
  address.
- description — description of the rest area and its facilities
- open — `"Yes"`, `"No"`, or `"Unknown"` when the operating agency does not report status

Responses are cached for 15 minutes and carry an ETag.

## Weigh Stations

> [!NOTE]
> This endpoint is present in the application but is not yet deployed to
> travelmidwest.com; it currently returns 404 there.

The weighStationMap.json endpoint provides commercial vehicle weigh station locations
and whether each is open.

### Request

```console
https://travelmidwest.com/lmiga/weighStationMap.json
```

GET or POST. The POST body may contain:

- bbox — see [Bounding Box](#bounding-box) section (optional; all weigh stations are returned when omitted)

### Response

The response is a GeoJSON FeatureCollection with a Point feature for each weigh station.
Stations with no latitude or longitude are omitted. Feature properties:

- externalId — the weigh station identifier
- name — the weigh station name
- address — the street address
- description — description of the weigh station
- open — `"Yes"`, `"No"`, or `"Unknown"` when the operating agency does not report status

Responses are cached for 15 minutes and carry an ETag.
