# travelTimeService.json

## Introduction

The GTIS provides a web service that returns travel times in Illinois for arbitrary locations.

The web service is password protected and requires approval from IDOT for a [TravelMidwest.com account](https://go.travelmidwest.com/register) with the "illinoistmc" access role.

Please note that regular user account registration and approval does not automatically grant the "illinoistmc" access role.

## Request

The travelTimeService.json web service accepts two request forms: request parameters (GET or form-encoded POST) and a JSON request body (POST with Content-Type "application/json"). Both forms return the same response (see below).

### Request Parameters

The travelTimeService.json web service can be accessed via the following URL syntax:

```
https://travelmidwest.com/lmiga/travelTimeService.json?locations=location1&locations=location2&...locations=location_n]
```

Note that one or more "locations" parameters may be passed to the travelTimeService.json page.

### Locations

The "locations" request parameter can have several different formats.

#### Mile Post Format

The format of a mile post locations parameter is as follows:

- `//dir road// FROM //milepost1//[,//city//][,//state//][,//county//] TO //milepost2// [,//city//][,//state//][,//county//]`

where

- *dir* is a compass direction and must be one of NB, SB, EB, WB, NEB, NWB, SEB, SWB
- *road* is the name of a road, county route, state route, or interstate
  - county routes typically are formatted as "CR-xx"
  - state routes are formatted as "IL-xx"
  - U.S. routes are formatted as "US-xx"
  - interstates are formatted as "I-xx"
- *milepost1* is the first mile post value as a decimal number (e.g., "10.0")
- //milepost2 //is the second milepost value and must be downstream of the first milepost
- *city, state, and county* are optional city, state and county names used to disambiguate mile posts. Typically only the state needs to be specified for interstate routes.

#### Cross Street Format

The format of a cross street locations parameter is as follows:

- *dir onroad* FROM *road1*[,*city*][,*state*][,*county*] TO *road2*[,*city*][,*state*][,*county*]

See Mile Post Format for the meaning and format of *dir, onroad, road1, city, state, county //and //road2.*

#### Lat/Long Format

The format of a lat/long locations parameter is as follows:

- *road* FROM *lat1*[N],*long1*[E] TO *lat2*[N],*long2*[E]

where

- *road* is formatted the same as with the mile post format (see above)
- //lat1,long1 //is the latitude and longitude in decimal degrees of the first point on the road
- //lat2,long2 //is the latitude and longitude in decimal degrees of the second point on the road

### JSON Request Body

> [!NOTE]
> The JSON Request Body parameter is not available for use on TravelMidwest.com at present.  It is currently being tested and will be deployed soon.

Alternatively, the request may be sent as an HTTP POST with a Content-Type of "application/json" and a JSON body with the following fields:

- locations: optional array of free-form location strings, resolved the same way as the "locations" request parameters (see Locations above)
- sections: optional array of already-resolved road section objects (see Section Format below)

Resolved locations and posted sections are concatenated (locations first) into a single route, and the travel time is computed for the combined route.

#### Section Format

Each entry in the "sections" array is a JSON object with the following fields:

- start: point location object for the start of the section (required, see Point Location Format below)
- end: point location object for the end of the section (required)
- startOffset: distance in meters along the first road segment where the section starts (optional, defaults to 0)
- endOffset: distance in meters along the last road segment where the section ends (optional, defaults to 0)
- disegments: optional array of directional segment id strings. Each string is a numeric segment id followed by a direction suffix, "R" or "N" (e.g., "1339880748R"). When present, these segments are used as-is; when absent, the road segments are recomputed from the start and end points.
- length: length of the section in meters (optional)
- averageSpeedLimit: average speed limit over the section in miles per hour (optional)

#### Point Location Format

A point location is a JSON object holding one or more *profiles*, each an alternate way of naming the same spot on the road network. At least one profile must be set. The most commonly used profiles are:

- milepost: a point at a mile-marker value
  - roadName: road name object (see below)
  - milepost: mile-marker value in *miles* as a decimal number
  - fips: optional city/county/state object (see below)
- crossStreet: a point on a road at an intersecting road
  - roadName: road name object for the on-road
  - crossStreet: road name object for the intersecting road
  - offsetInMeters: signed distance in meters from the intersection, positive in the on-road's direction of travel
  - fips: optional
- latLong: a coordinate on a named road
  - roadName: road name object (*required* - a coordinate alone is ambiguous)
  - coord: [longitude, latitude] in decimal degrees, longitude first
- sif: a road segment id, direction, and offset
  - id: numeric segment id
  - dir: segment traversal direction, "REF_TO_NONREF" or "NONREF_TO_REF" (corresponding to the "R"/"N" suffix used in disegments strings)
  - offset: distance in meters from the segment's start node
- ramp: a point along a ramp from one road to another
  - from: road name object for the road the ramp leaves
  - to: road name object for the road the ramp joins
  - offsetInMeters: distance in meters from the start of the ramp
  - fips: optional

Note that all offset fields are in meters; the lone exception is the milepost value, which is in miles.

A *road name object* has the following fields (only "name" is required):

- name: the bare road name (e.g., "I-90", "Clark")
- direction: bound abbreviation, one of NB, SB, EB, WB, NEB, NWB, SEB, SWB; omit when unknown
- streetType: "St", "Blvd", "Rd", "Ave", ...; omit when blank (expressways have none)
- prefix / suffix: directional affixes "N"/"S"/"E"/"W"; optional

A *fips object* disambiguates by place; all fields are optional strings or numbers:

- city, county, state: place names (e.g., "Chicago", "Cook", "Illinois")
- zip: ZIP code
- cityCode, countyCode, stateCode: numeric FIPS codes

An example request body:

```json
{
    "locations": ["NB US-41 from IL-22 to Golf Rd"],
    "sections": [
        {
            "start": { "sif": { "dir": "REF_TO_NONREF", "offset": 64.28, "id": 1339880748 } },
            "startOffset": 64.28,
            "end": { "sif": { "dir": "REF_TO_NONREF", "offset": 197.23, "id": 736019060 } },
            "endOffset": 197.23,
            "disegments": ["1339880748R", "1311164246R", "736019060R"],
            "length": 4822.96,
            "averageSpeedLimit": 61.5
        }
    ]
}
```

Note that requests that POST "locations" as request parameters together with a Content-Type of "application/json" are not supported; use one request form or the other.

### Credentials

TravelMidwest.com will respond with a 401 status code indicating that authentication is required to access travelTimeService.json. The "Authorization" request header should be included to avoid this response. See [RFC 7235](https://tools.ietf.org/html/rfc7235) for more information on Basic authentication.

## Response

The service will respond with GeoJSON as follows:

- type: "Feature"
- geometry:
  - type: "MultiLineString"
  - coordinates: [ [lng1,lat1], [lng2,lat2], [lng3,lat3], ... ]
- properties:
  - travelTimeInSeconds: decimal number representing travel time in seconds
  - speedInMetersPerSecond: decimal number representing speed in m/s
  - congestionLevel: "UNKNOWN_CONGESTION_LEVEL", "NON_CONGESTION", "LIGHT_CONGESTION", "MEDIUM_CONGESTION", "HEAVY_CONGESTION"
  - sources: array of data source objects, each with "sourceName", "agencyName", and "idPrefix" string fields
  - oldestTimestamp: millis - milliseconds since midnight on 1/1/1970
  - lengthInMeters: decimal number representing length of route for input locations
  - realTimePercentage: amount of real time data 0.0 to 1.0 with 0.7 being historical data cutoff
  - locationError: null or a string representing location parsing/resolving error

## Example

An example request:

```
https://travelmidwest.com/lmiga/travelTimeService.json?locations=NB+US-41+from+IL-22+to+Golf+Rd
```

The resulting JSON output (reformatted for easier readability):

```json
{
    "type": "Feature",
    "geometry": {
        "type": "MultiLineString",
        "coordinates": [[[-87.7468502, 42.0553032], [-87.7468322, 42.0561979], [-87.7468142, 42.056859], [-87.7467872, 42.0575467], [-87.7467872, 42.0578606], [-87.7467782, 42.0583013], [-87.7467692, 42.0589423], [-87.7467602, 42.0591893], [-87.7467512, 42.0596968], [-87.7467332, 42.0602777], [-87.7467243, 42.0605981], [-87.7466883, 42.0613727], [-87.7466793, 42.0617399], [-87.7466703, 42.062481], [-87.7466613, 42.0628015], [-87.7466613, 42.0632622], [-87.7466523, 42.0636628], [-87.7466523, 42.0639432], [-87.7466343, 42.0647777], [-87.7466073, 42.0653786], [-87.7465984, 42.0655989], [-87.7465894, 42.0660396], [-87.7465804, 42.0664268], [-87.7465624, 42.0668207], [-87.7465984, 42.0672613], [-87.7466523, 42.0675417], [-87.7467962, 42.0680892], [-87.7469221, 42.0683829], [-87.747084, 42.0687968], [-87.7472728, 42.0692107], [-87.7475426, 42.069658], [-87.7480283, 42.0704191], [-87.7481542, 42.0706127], [-87.7488017, 42.0716408], [-87.7491434, 42.0721681], [-87.7493413, 42.0724819], [-87.7499708, 42.0734632], [-87.7502586, 42.0739105], [-87.7508521, 42.0748784], [-87.7515176, 42.075833], [-87.7518504, 42.0762402], [-87.752291, 42.0768676], [-87.7525608, 42.077168], [-87.7529925, 42.0776219], [-87.7533522, 42.0780291], [-87.753694, 42.0784429], [-87.7539638, 42.0788301], [-87.7543595, 42.0794976], [-87.7547282, 42.0802318], [-87.754989, 42.0808793], [-87.7551689, 42.0812798], [-87.7553218, 42.0815801], [-87.7556095, 42.0821408], [-87.7558614, 42.082568], [-87.7560772, 42.0829417], [-87.756356, 42.083429], [-87.7564909, 42.0836225], [-87.7573362, 42.0849507], [-87.7580287, 42.086052], [-87.7582086, 42.0863523], [-87.7584064, 42.0866727], [-87.7585323, 42.0869597], [-87.7586582, 42.0873201], [-87.7588561, 42.0876805], [-87.759, 42.0879274], [-87.7593867, 42.0887416], [-87.7595755, 42.0890687], [-87.7598094, 42.0894491], [-87.7600792, 42.0898629], [-87.7604119, 42.0903701], [-87.7613562, 42.0918516], [-87.7618958, 42.0926791], [-87.7623904, 42.0934399], [-87.7626332, 42.093807], [-87.7628041, 42.0940806], [-87.7640272, 42.0959824], [-87.7644589, 42.0966431], [-87.7660417, 42.0990787], [-87.7666172, 42.0999795], [-87.7670759, 42.1007069], [-87.7674086, 42.1012073], [-87.7675525, 42.1014208], [-87.7676784, 42.1016277], [-87.768209, 42.1024684], [-87.7701066, 42.1054109], [-87.7707001, 42.1062383], [-87.7711408, 42.1068121], [-87.7719142, 42.1077128], [-87.7726876, 42.1086468], [-87.7731643, 42.1093007], [-87.7738837, 42.1104015], [-87.7753406, 42.1127432], [-87.7755745, 42.1131101], [-87.7773641, 42.1159921], [-87.777544, 42.116279], [-87.7780476, 42.1171128], [-87.7783713, 42.1176332], [-87.7790009, 42.1186271], [-87.7793786, 42.1192408], [-87.780206, 42.1205683], [-87.7808265, 42.1215622], [-87.7818967, 42.1232831], [-87.7830298, 42.1250774], [-87.7836863, 42.126158], [-87.784109, 42.1268517], [-87.7843158, 42.1272385], [-87.7844777, 42.1275386], [-87.7846486, 42.1279388], [-87.7847925, 42.1282723], [-87.7849274, 42.1287525], [-87.7850263, 42.1290994], [-87.7851072, 42.1295329], [-87.7851882, 42.1302932], [-87.7852691, 42.1315804], [-87.7853411, 42.1321807], [-87.785494, 42.1330077], [-87.7856468, 42.1336213], [-87.7858987, 42.1343482], [-87.7861864, 42.1350284], [-87.7865012, 42.135622], [-87.7868969, 42.1362889], [-87.7873466, 42.1369091], [-87.7875624, 42.1372092], [-87.7878232, 42.1375493], [-87.7879941, 42.1377627], [-87.7882279, 42.1380494], [-87.7890283, 42.1390497], [-87.7897028, 42.1398833], [-87.7903233, 42.1406569], [-87.790773, 42.1411703], [-87.7913305, 42.1418572], [-87.7922299, 42.1429708], [-87.7924727, 42.1432708], [-87.7926256, 42.1434776], [-87.7930303, 42.144011], [-87.7934709, 42.1446111], [-87.7941994, 42.1456714], [-87.7945321, 42.1461714], [-87.7966455, 42.1494586], [-87.7968794, 42.1498187], [-87.7970862, 42.1501387], [-87.7975898, 42.1509188], [-87.7980665, 42.1516522], [-87.7984622, 42.1523323], [-87.798642, 42.152639], [-87.7990197, 42.153179], [-87.7991816, 42.153399], [-87.7995503, 42.153859], [-87.8, 42.1543991], [-87.8002968, 42.1547524], [-87.8004766, 42.1549391], [-87.8006745, 42.1551391], [-87.8008543, 42.1553391], [-87.801367, 42.1558391], [-87.8018436, 42.1562791], [-87.8023922, 42.1567391], [-87.8027339, 42.1570192], [-87.803903, 42.1580192], [-87.8042178, 42.1582925], [-87.8047664, 42.1587525], [-87.8051981, 42.1591125], [-87.8054409, 42.1593325], [-87.8056567, 42.1595591], [-87.8059265, 42.1598325], [-87.8061424, 42.1600724], [-87.806592, 42.1605191], [-87.8069967, 42.1609524], [-87.8076982, 42.161699], [-87.8081928, 42.1622123], [-87.8089572, 42.1630123], [-87.809191, 42.1632389], [-87.8093619, 42.1634189], [-87.8099195, 42.1640122], [-87.8104141, 42.1645388], [-87.8109987, 42.1651987], [-87.8113764, 42.1656587], [-87.8115922, 42.1659386], [-87.811871, 42.1663386], [-87.8120239, 42.1665585], [-87.8121588, 42.1667718], [-87.8123926, 42.1671518], [-87.8126265, 42.1675717], [-87.8127524, 42.1677717], [-87.8130042, 42.1682716], [-87.8141103, 42.1704712], [-87.8144791, 42.1712577], [-87.8148927, 42.1722175], [-87.8152435, 42.1731973], [-87.8157831, 42.1747369], [-87.8161698, 42.1759099], [-87.8163227, 42.1763431], [-87.8166284, 42.1772895], [-87.8168533, 42.1779226], [-87.8169432, 42.1781425], [-87.8170511, 42.1784491], [-87.817186, 42.178769], [-87.8173209, 42.1790489], [-87.8175008, 42.1794088], [-87.8177886, 42.1799419], [-87.8179145, 42.1801618], [-87.8181123, 42.1804617], [-87.8183281, 42.1808083], [-87.818508, 42.1810482], [-87.8187778, 42.1814813], [-87.8189667, 42.1817213], [-87.8196591, 42.1825209], [-87.819821, 42.1827009], [-87.8201088, 42.1830008], [-87.8205495, 42.1834406], [-87.8209542, 42.1838271], [-87.8212329, 42.184107], [-87.8215207, 42.1844002], [-87.8218265, 42.1847001], [-87.822429, 42.1852931], [-87.8228068, 42.185673], [-87.8231665, 42.1860328], [-87.8234273, 42.1862993], [-87.8238769, 42.1867925], [-87.8240928, 42.1870523], [-87.8244705, 42.1875121], [-87.8247673, 42.1879186], [-87.8249112, 42.1881118], [-87.825154, 42.1884583], [-87.8254508, 42.1889181], [-87.8257925, 42.1894379], [-87.8260173, 42.189791], [-87.8262871, 42.1902108], [-87.826476, 42.1904906], [-87.8269526, 42.1912303], [-87.8272674, 42.19171], [-87.827834, 42.1925629], [-87.8282117, 42.1931492], [-87.8293268, 42.1948815], [-87.830433, 42.1965672], [-87.8305859, 42.1968204], [-87.8314133, 42.1980796], [-87.8320518, 42.199059], [-87.8325284, 42.1997985]]]
    },
    "properties": {
        "travelTimeInSeconds": 908.5113646840339,
        "speedInMetersPerSecond": 19.59219754730294,
        "congestionLevel": "LIGHT_CONGESTION",
        "sources": [],
        "oldestTimestamp": 1568651615000,
        "lengthInMeters": 17799.734130859375,
        "realTimePercentage": 0.9365556208333028,
        "locationError": null
    }
}
```
