# Report Data

## About

All reports are organized into hierarchical geographic locations starting with the top level "GATEWAY" location:

- GATEWAY
  - GATEWAY.IL
    - GATEWAY.IL.I-55
      - GATEWAY.IL.I-55.I-55 NB
      - GATEWAY.IL.I-55.I-55 SB
    - GATEWAY.IL.I-90
      - GATEWAY.IL.I-90.I-90 EB
      - GATEWAY.IL.I-90.I-90 WB
    - ...
  - GATEWAY.IL.ARTERIALS
    - GATEWAY.IL.ARTERIALS.ADAMS
    - GATEWAY.IL.ARTERIALS.ALEXANDER
    - ...
  - GATEWAY.WI
    - GATEWAY.WI.I-94
      - GATEWAY.WI.I-94.I-94 EB
      - GATEWAY.WI.I-94.I-94 WB
    - ...
  - GATEWAY.REGIONAL
    - GATEWAY.REGIONAL.I-24

This document covers the hierarchical, report-location form of the data; the same underlying data organized spatially by bounding box is described in [Map Data](map-data.md).

## "path" Parameter and Report Locations

The Travel Times and Incidents JSON download require a path parameter, which indicates a Travel Midwest report location. Reports are organized hierarchically with the "GATEWAY" report including all possible reports, "GATEWAY.IL" containing all Illinois reports, etc.

### Request

```console
https://travelmidwest.com/lmiga/reportLocations.json
```

### Response

The `reportLocations.json` endpoint will respond to GET or POST requests with hierarchical JSON data formatted as follows:

- displayName — Human readable name for report location.
- path — See "The path Parameter" in the section above.
- children — An array of child locations, each with displayName, path, and children of their own.

### Example

A partial response example:

```json
{
    "displayName": "Entire Region",
    "path": "GATEWAY",
    "children": [{
            "displayName": "Regional",
            "path": "GATEWAY.REGIONAL",
            "children": [{
                    "displayName": "I-24",
                    "path": "GATEWAY.REGIONAL.I-24",
                    "children": [{
                            "displayName": "I-24 WB",
                            "path": "GATEWAY.REGIONAL.I-24.I-24 WB",
                            "children": []
                        }, {
                            "displayName": "I-24 EB",
                            "path": "GATEWAY.REGIONAL.I-24.I-24 EB",
                            "children": []
                        }
                    ]
                }, {
                    "displayName": "I-39",
                    "path": "GATEWAY.REGIONAL.I-39",
                    "children": [{
                            "displayName": "I-39 NB",
                            "path": "GATEWAY.REGIONAL.I-39.I-39 NB",
                            "children": []
                        }, {
                            "displayName": "I-39 SB",
                            "path": "GATEWAY.REGIONAL.I-39.I-39 SB",
                            "children": []
                        }
                    ]
                },
.
.
.
[truncated]
```

## Nearest Report Location

The `nearestReportLocation.json` API endpoint takes the GPS currentPosition() object as input and returns an array of matching report location paths and their distances. An arterial county report location is also returned. This endpoint is used on the [https://travelmidwest.com/lmiga/mytravel.jsp](https://travelmidwest.com/lmiga/mytravel.jsp) page.

### Request

```console
https://ravelmidwest.com/lmiga/nearestReportLocation.json
```

A POST parameter named "currentPosition" is required as input. See section 5.3 of https://www.w3.org/TR/geolocation-API.

- (((
coords — Coordinates from HTML GeoLocation API's getCurrentPosition() method. See also [w3schools](https://www.w3schools.com/html/html5_geolocation.asp) and [w3.org](https://www.w3.org/TR/geolocation-API/).
- (((
| Property | Returns |
| --- | --- |
| coords.latitude | The latitude as a decimal number (always returned) |
| coords.longitude | The longitude as a decimal number (always returned) |
| coords.accuracy | The accuracy of position (always returned) |
| coords.altitude | The altitude in meters above the mean sea level (returned if available) |
| coords.altitudeAccuracy | The altitude accuracy of position (returned if available) |
| coords.heading | The heading as degrees clockwise from North (returned if available) |
| coords.speed | The speed in meters per second (returned if available) |

- timestamp — The date/time of the response (returned if available)

### Response

A JSON array containing the following fields for each element of the array:

- path — the report location path, see "The path Parameter" section located above.
- distance — distance in meters from the input GPS coordinates to the report location.
The returned array will be sorted by distance, lowest distance first. A GATEWAY.[state].ARTERIALS.[county] path is always appended, if possible, for the arterial county report that the coordinates are contained within. State will be "IL", "IN", "WI", MI", "KY", "MO", "IA", or "REGIONAL". County will be the county name, capitalized, like "COOK", "WILL", etc.

## Travel Times

*For the bounding-box/GeoJSON form of this data, see [Map Data → Travel Times](map-data.md#travel-times).*

The GTIS provides a fixed number of travel times that can be downloaded in JSON format.

### Request

```console
https://travelmidwest.com/lmiga/travelTime.json?path=[path]
```

The "path"// //parameter must match one of the parameter values from `reportLocations.json`. If the path is not a leaf in the report location hierarchy, then all leaf reports will be returned in an array.

### Response

Returns travel time report in JSON format. The URL for this page is "travelTime.json?path=[path]" where path defines the report (e.g., GATEWAY.IL.I-55) for I-55 in Illinois. The returned JSON is an array of javascript objects. Each object has the following fields:

- tablePath — path from reportLocations.json
- tableName — header description of report location, e.g., "I-55 NB"
- reportRows — array of travel time data objects, each with the following fields:
  - level — congestion level, one of Unknown, Uncongested, Light, Medium, Heavy
  - on — roadway the travel time is "on", should not be needed for the report since the "path" defines the "on" road
  - from — "from" cross street name
  - to — "to" cross street name
  - tt — travel time in minutes, -1 if not available
  - avg — average time in minutes, -1 if not available
  - id — external indetifier for travel time, can be used to access travel time statistics website at https://travelmidweststats.com/GCMLink.aspx?GCMLinkID=[id]
  - len — length of road between "from" and "to" in miles
  - spd — average speed in mile per hour (MPH)
  - ovrAvg — "true" if travel time is more than 50% over average, used on web site to flag travel time in red color

### Example

```console
https://travelmidwest.com/lmiga/travelTime.json?path=GATEWAY.IL.I-55
```

```json
[{
        "tablePath": "GATEWAY.IL.I-55.I-55 NB",
        "reportRows": [{
                "level": "Uncongested",
                "on": "NB I-55/64 (Poplar St Brg)",
                "from": "Mississippi River",
                "to": "I-64",
                "tt": 2.8666666666666667,
                "avg": -1.0,
                "id": "IL-IDOTD8-I55_NB01",
                "len": 2.748946154457965,
                "spd": "51",
                "ovrAvg": false
            },
.
.
.
        ],
        "tableName": "I-55 NB"
    }, {
        "tablePath": "GATEWAY.IL.I-55.I-55 SB",
        "reportRows": [{
                "level": "Medium",
                "on": null,
                "from": "KING",
                "to": "HARLEM",
                "tt": 34.93333333333333,
                "avg": 37.43,
                "id": "IL-TSCDMS-SB_I_55_KING_TO_HARLEM_72",
                "len": 10.319732760677642,
                "spd": "18",
                "ovrAvg": false
            },
.
.
.
        ],
        "tableName": "I-55 SB"
    }
]
```

## Incidents

*For the bounding-box/GeoJSON form of this data, see [Map Data → Incidents](map-data.md#incidents).*

### Request

```console
https://travelmidwest.com/lmiga/incidents.json?path=[path]
```

The "path" parameter must match one of the parametURL syntax:er values from reportLocations.json. The path can be any value from reportLocations.json and not just leaf reports. If an upper level report is requested, then multiple incident reports will be returned in a JSON array, one for each leaf report contained within the upper level parent report.

### Response

Returns incidents associated with a given report in JSON format with the following fields:

- reportRows — an array of incident reports
  - id — unique identifier
  - description — description of the incident
  - location — "at" or "from to" location description
  - fullLocation — "on", "from" "to" and municipalities
  - fromCity — city at start of incident
  - fromCounty — county at start of incident
  - fromState — state at start of incident's location
  - toCity — city where incident location ends
  - toCounty — county at incident's end location
  - toState — state where incident ends
  - mileMarker — mile marker on the report location's expressway where the incident is located
  - closureDetails — lanes that are closed
  - status — New or Updated
  - startTime — when the incident started
  - estimatedEndTIme — guess as to when the incident will end, mnay be "Unknown" for some sources
  - source — agency that sent the incident to the GTIS
  - latitude — decimal lattude
  - longitude — decimal longitude
- tableName — expressway and direction
- tablePath — see Path section above

### Example

```console
https://travelmidwest.com/lmiga/incidents.json?path=GATEWAY
```

```json
[
   {
      "reportRows" : [
         {
            "closureDetails" : "All lanes and shoulders closed",
            "description" : "Incident with structure damage",
            "estimatedEndTime" : "11/16/24 9:20 AM",
            "fromCity" : "Princeton",
            "fromCounty" : "Bureau",
            "fromState" : "IL",
            "fullLocation" : "NB 1950 St from 1835 Ave to 1900 Ave, Princeton, Bureau, IL",
            "id" : "IL-IDOTD3-INCIDENT.2023.11.16.9.5988295",
            "latitude" : 41.4170591,
            "location" : "NB 1950 St from 1835 Ave to 1900 Ave",
            "longitude" : -89.4787074,
            "mileMarker" : "",
            "source" : "IDOT",
            "startTime" : "11/16/23 9:05 AM",
            "status" : "Updated",
            "toCity" : "Princeton",
            "toCounty" : "Bureau",
            "toState" : "IL"
         },
         {
            "closureDetails" : "All lanes and shoulders closed",
            "description" : "Incident with structure damage",
            "estimatedEndTime" : "11/16/24 9:20 AM",
            "fromCity" : "Princeton",
            "fromCounty" : "Bureau",
            "fromState" : "IL",
            "fullLocation" : "SB 1950 St from 1900 Ave to 1835 Ave, Princeton, Bureau, IL",
            "id" : "IL-IDOTD3-INCIDENT.2023.11.16.9.5988295",
            "latitude" : 41.4170591,
            "location" : "SB 1950 St from 1900 Ave to 1835 Ave",
            "longitude" : -89.4787074,
            "mileMarker" : "",
            "source" : "IDOT",
            "startTime" : "11/16/23 9:05 AM",
            "status" : "Updated",
            "toCity" : "Princeton",
            "toCounty" : "Bureau",
            "toState" : "IL"
         }
      ],
      "tableName" : "Bureau County",
      "tablePath" : "GATEWAY.IL.ARTERIALS.BUREAU"
   },
   {
      "reportRows" : [
         {
            "closureDetails" : "All lanes and shoulders closed",
            "description" : "Detoured using IL-23 to US-52 to IL-47",
            "estimatedEndTime" : "12/31/23 11:59 PM",
            "fromCity" : "Unincorporated La Salle County (Leland)",
            "fromCounty" : "LaSalle",
            "fromState" : "IL",
            "fullLocation" : "NEB US-34 from 22nd Rd to 22nd Rd, Unincorporated La Salle County (Leland), IL",
            "id" : "IL-IDOTD3-INCIDENT.2023.8.18.16.5912080",
            "latitude" : 41.6157801,
            "location" : "NEB US-34 from 22nd Rd to 22nd Rd",
            "longitude" : -88.7515619,
            "mileMarker" : "",
            "source" : "IDOT",
            "startTime" : "8/18/23 4:46 PM",
            "status" : "Updated",
            "toCity" : "Unincorporated La Salle County (Leland)",
            "toCounty" : "LaSalle",
            "toState" : "IL"
         },
         {
            "closureDetails" : "All lanes and shoulders closed",
            "description" : "Detoured using IL-23 to US-52 to IL-47",
            "estimatedEndTime" : "12/31/23 11:59 PM",
            "fromCity" : "Unincorporated La Salle County (Leland)",
            "fromCounty" : "LaSalle",
            "fromState" : "IL",
            "fullLocation" : "SWB US-34 from 22nd Rd to near 22nd Rd, Unincorporated La Salle County (Leland), IL",
            "id" : "IL-IDOTD3-INCIDENT.2023.8.18.16.5912080",
            "latitude" : 41.6157801,
            "location" : "SWB US-34 from 22nd Rd to near 22nd Rd",
            "longitude" : -88.7515619,
            "mileMarker" : "",
            "source" : "IDOT",
            "startTime" : "8/18/23 4:46 PM",
            "status" : "Updated",
            "toCity" : "Unincorporated La Salle County (Leland)",
            "toCounty" : "LaSalle",
            "toState" : "IL"
         }
      ],
      "tableName" : "LaSalle County",
      "tablePath" : "GATEWAY.IL.ARTERIALS.LASALLE"
   },
   {
      "reportRows" : [
         {
            "closureDetails" : "Various lanes closed",
            "description" : "Possible delays due to VEHICLE CRASH on I-70 Eastbound.",
            "estimatedEndTime" : "Unknown",
            "fromCity" : "St Louis",
            "fromCounty" : "St Louis (City)",
            "fromState" : "MO",
            "fullLocation" : "EB I-70 at Adelaide Ave, St Louis, St Louis (City), MO",
            "id" : "MO-MODOT-INCIDENT.2023.12.21.23.6014525",
            "latitude" : 38.6815053,
            "location" : "at Adelaide Ave",
            "longitude" : -90.2145942,
            "mileMarker" : "",
            "source" : "MoDOT",
            "startTime" : "12/21/23 11:14 PM",
            "status" : "Updated",
            "toCity" : "St Louis",
            "toCounty" : "St Louis (City)",
            "toState" : "MO"
         }
      ],
      "tableName" : "I-70 EB",
      "tablePath" : "GATEWAY.MO.I-70.I-70 EB"
   },
   {
      "reportRows" : [
         {
            "closureDetails" : "Various lanes closed",
            "description" : "Possible delays due to VEHICLE CRASH on I-70 Westbound.",
            "estimatedEndTime" : "Unknown",
            "fromCity" : "St Louis",
            "fromCounty" : "St Louis (City)",
            "fromState" : "MO",
            "fullLocation" : "WB I-70 at Taylor Ave, St Louis, St Louis (City), MO",
            "id" : "MO-MODOT-INCIDENT.2023.12.21.23.6014528",
            "latitude" : 38.6836606,
            "location" : "at Taylor Ave",
            "longitude" : -90.2242799,
            "mileMarker" : "",
            "source" : "MoDOT",
            "startTime" : "12/21/23 11:35 PM",
            "status" : "Updated",
            "toCity" : "St Louis",
            "toCounty" : "St Louis (City)",
            "toState" : "MO"
         }
      ],
      "tableName" : "I-70 WB",
      "tablePath" : "GATEWAY.MO.I-70.I-70 WB"
   },
   {
      "reportRows" : [
         {
            "closureDetails" : "All lanes and shoulders closed",
            "description" : "MO-77 is CLOSED Northbound due to OTHER.",
            "estimatedEndTime" : "Unknown",
            "fromCity" : "East Prairie",
            "fromCounty" : "Mississippi",
            "fromState" : "MO",
            "fullLocation" : "NWB MO-77 at Levee Rd, East Prairie, Mississippi, MO",
            "id" : "MO-MODOT-INCIDENT.2023.8.23.14.5916331",
            "latitude" : 36.58819,
            "location" : "NWB MO-77 at Levee Rd",
            "longitude" : -89.2162047,
            "mileMarker" : "",
            "source" : "MoDOT",
            "startTime" : "8/23/23 2:01 PM",
            "status" : "Updated",
            "toCity" : "East Prairie",
            "toCounty" : "Mississippi",
            "toState" : "MO"
         },
         {
            "closureDetails" : "All lanes and shoulders closed",
            "description" : "MO-77 is CLOSED Southbound due to OTHER.",
            "estimatedEndTime" : "Unknown",
            "fromCity" : "East Prairie",
            "fromCounty" : "Mississippi",
            "fromState" : "MO",
            "fullLocation" : "SEB MO-77 near Levee Rd, East Prairie, Mississippi, MO",
            "id" : "MO-MODOT-INCIDENT.2023.8.23.14.5916330",
            "latitude" : 36.58819,
            "location" : "SEB MO-77 near Levee Rd",
            "longitude" : -89.2162047,
            "mileMarker" : "",
            "source" : "MoDOT",
            "startTime" : "8/23/23 2:01 PM",
            "status" : "Updated",
            "toCity" : "East Prairie",
            "toCounty" : "Mississippi",
            "toState" : "MO"
         }
      ],
      "tableName" : "Mississippi County",
      "tablePath" : "GATEWAY.MO.ARTERIALS.MISSISSIPPI"
   },
   {
      "reportRows" : [
         {
            "closureDetails" : "Various lanes closed",
            "description" : "Possible delays due to VEHICLE CRASH on I-70 Eastbound.",
            "estimatedEndTime" : "Unknown",
            "fromCity" : "St Louis",
            "fromCounty" : "St Louis (City)",
            "fromState" : "MO",
            "fullLocation" : "EB I-70 at Adelaide Ave, St Louis, St Louis (City), MO",
            "id" : "MO-MODOT-INCIDENT.2023.12.21.23.6014525",
            "latitude" : 38.6815053,
            "location" : "at Adelaide Ave",
            "longitude" : -90.2145942,
            "mileMarker" : "",
            "source" : "MoDOT",
            "startTime" : "12/21/23 11:14 PM",
            "status" : "Updated",
            "toCity" : "St Louis",
            "toCounty" : "St Louis (City)",
            "toState" : "MO"
         }
      ],
      "tableName" : "I-70 EB",
      "tablePath" : "GATEWAY.REGIONAL.I-70.I-70 EB"
   },
   {
      "reportRows" : [
         {
            "closureDetails" : "Various lanes closed",
            "description" : "Possible delays due to VEHICLE CRASH on I-70 Westbound.",
            "estimatedEndTime" : "Unknown",
            "fromCity" : "St Louis",
            "fromCounty" : "St Louis (City)",
            "fromState" : "MO",
            "fullLocation" : "WB I-70 at Taylor Ave, St Louis, St Louis (City), MO",
            "id" : "MO-MODOT-INCIDENT.2023.12.21.23.6014528",
            "latitude" : 38.6836606,
            "location" : "at Taylor Ave",
            "longitude" : -90.2242799,
            "mileMarker" : "",
            "source" : "MoDOT",
            "startTime" : "12/21/23 11:35 PM",
            "status" : "Updated",
            "toCity" : "St Louis",
            "toCounty" : "St Louis (City)",
            "toState" : "MO"
         }
      ],
      "tableName" : "I-70 WB",
      "tablePath" : "GATEWAY.REGIONAL.I-70.I-70 WB"
   }
]
```

## Construction

*For the bounding-box/GeoJSON form of this data, see [Map Data → Construction](map-data.md#construction).*

The GTIS allows active construction events to be downloaded in JSON format.

### Request

```console
https://travelmidwest.com/lmiga/construction.json?path=[path]
```

The "path" parameter must match one of the parameter values from reportLocations.json. The path can be any value from reportLocations.json and not just leaf reports. If an upper level report is requested, then multiple construction reports will be returned in a JSON array, one for each leaf report contained within the upper level parent report.

### Response

Returns construction events associated with a given report in JSON format with the following fields:

- reportRows — an array of incident reports
  - id — unique identifier
  - location — "at" or "from-to" location description
  - fullLocation — same as above but includes "on" road and mnicipalities
  - fromCity, fromCounty, fromState — municipalities where event's location begins
  - toCity, toCounty, toState — municipalities where event's location ends
  - mileMarker — mile marker on the report location's expressway where the incident is located, may be a range of low to high mile markers
  - severity — severity of construction event Unknown, None, Minor, Medium, or Major
  - closureDetails — lanes that are closed
  - timePeriods — start date/time to end date/time of event. There are multiple formats for this field in order to minimize the amount of text used to describe the time periods.
  - source — agency that sent the construction event to the GTIS
  - description — textual description of the construction event as sent by source agency
  - announcementId — announcement that goes with this event
  - latitude — in decimal degrees to centroid of event
  - longitude — in decimal degrees to centroid of event
- tableName — expressway and direction
- tablePath — see Path section above

### Example

```console
https://travelmidwest.com/lmiga/construction.json?path=GATEWAY.IL.I-55.I-55+NB
```

```json
[
   {
      "reportRows" : [
         {
            "announcementId" : "",
            "closureDetails" : "Various lanes closed",
            "description" : "Expect lane restrictions for roadway improvement. Vehicle width restricted to 22'.",
            "fromCity" : "Staunton",
            "fromCounty" : "Macoupin",
            "fromState" : "IL",
            "fullLocation" : "NB I-55 from Staunton Rd, Staunton, Macoupin, IL to near IL-138, White City, Macoupin, IL",
            "id" : "IL-GAI-ROADWORK.2023.5.5.15.5822063",
            "latitude" : 39.0460105,
            "location" : "Staunton Rd to near IL-138",
            "longitude" : -89.7554282,
            "mileMarker" : "40.4 to 44.3",
            "severity" : "Medium",
            "source" : "IDOT",
            "timePeriods" : "7/6/23 6:00 AM to 6/11/24 5:59 AM",
            "toCity" : "White City",
            "toCounty" : "Macoupin",
            "toState" : "IL"
         },
         {
            "announcementId" : "",
            "closureDetails" : "Various lanes closed",
            "description" : "Expect lane restrictions for roadway improvement.",
            "fromCity" : "Waggoner",
            "fromCounty" : "Montgomery",
            "fromState" : "IL",
            "fullLocation" : "NB I-55 from IL-127, Waggoner, Montgomery, IL to 33rd Ave, Unincorporated Montgomery County (Farmersville), IL",
            "id" : "IL-GAI-ROADWORK.2023.3.2.12.5776053",
            "latitude" : 39.3933839,
            "location" : "IL-127 to 33rd Ave",
            "longitude" : -89.6429592,
            "mileMarker" : "63.1 to 73.0",
            "severity" : "Medium",
            "source" : "IDOT",
            "timePeriods" : "3/13/23 6:00 AM to 7/13/24 5:59 AM",
            "toCity" : "Unincorporated Montgomery County (Farmersville)",
            "toCounty" : "Montgomery",
            "toState" : "IL"
         },
         {
            "announcementId" : "",
            "closureDetails" : "Both shoulders closed, all lanes open",
            "description" : "traffic shifts left WZ 55mph;  Long Term Closure",
            "fromCity" : "Joliet",
            "fromCounty" : "Will",
            "fromState" : "IL",
            "fullLocation" : "NB Stevenson / I-55 from 0.5 miles south of IL-59, Joliet, Will, IL to Jefferson St (US-52), Shorewood, Will, IL",
            "id" : "IL-IDOT-ROADWORK.2023.5.23.16.5839594",
            "latitude" : 41.5104049,
            "location" : "0.5 miles south of IL-59 to Jefferson St (US-52)",
            "longitude" : -88.1965193,
            "mileMarker" : "251.1 to 252.8",
            "severity" : "Minor",
            "source" : "IDOT",
            "timePeriods" : "5/23/23 12:00 AM to 6/3/24 11:59 PM",
            "toCity" : "Shorewood",
            "toCounty" : "Will",
            "toState" : "IL"
         },
         {
            "announcementId" : "",
            "closureDetails" : "Both shoulders closed, all lanes open",
            "description" : "Long Term Closure",
            "fromCity" : "Bolingbrook",
            "fromCounty" : "Will",
            "fromState" : "IL",
            "fullLocation" : "NB Stevenson / I-55 from 0.5 miles south of Bolingbrook Dr (IL-53) to 0.5 miles north of Bolingbrook Dr (IL-53), Bolingbrook, Will, IL",
            "id" : "IL-IDOT-ROADWORK.2023.12.18.12.6011173",
            "latitude" : 41.6850348,
            "location" : "0.5 miles south of Bolingbrook Dr (IL-53) to 0.5 miles north of Bolingbrook Dr (IL-53)",
            "longitude" : -88.0679345,
            "mileMarker" : "266.6 to 267.6",
            "severity" : "Minor",
            "source" : "IDOT",
            "timePeriods" : "8/8/23 12:00 AM to 12/27/23 11:59 PM",
            "toCity" : "Bolingbrook",
            "toCounty" : "Will",
            "toState" : "IL"
         },
         {
            "announcementId" : "",
            "closureDetails" : "Left lane and left shoulder closed, two lanes open",
            "description" : "",
            "fromCity" : "Bolingbrook",
            "fromCounty" : "Will",
            "fromState" : "IL",
            "fullLocation" : "NB Stevenson / I-55 from 0.5 miles south of Bolingbrook Dr (IL-53) to 0.5 miles north of Bolingbrook Dr (IL-53), Bolingbrook, Will, IL",
            "id" : "IL-IDOT-ROADWORK.2023.12.21.11.6013895",
            "latitude" : 41.6850348,
            "location" : "0.5 miles south of Bolingbrook Dr (IL-53) to 0.5 miles north of Bolingbrook Dr (IL-53)",
            "longitude" : -88.0679345,
            "mileMarker" : "266.6 to 267.6",
            "severity" : "Minor",
            "source" : "IDOT",
            "timePeriods" : "12/21/23 9:00 PM to 12/22/23 5:00 AM",
            "toCity" : "Bolingbrook",
            "toCounty" : "Will",
            "toState" : "IL"
         },
         {
            "announcementId" : "",
            "closureDetails" : "Both shoulders closed, all lanes open with partial ramp closures",
            "description" : "Moving Operation",
            "fromCity" : "Bolingbrook",
            "fromCounty" : "Will",
            "fromState" : "IL",
            "fullLocation" : "NB Stevenson / I-55 from I-355, Bolingbrook, Will, IL to Lake Shore Dr (US-41), Chicago, Cook, IL",
            "id" : "IL-IDOT-ROADWORK.2023.12.21.11.6013798",
            "latitude" : 41.7841973,
            "location" : "I-355 to Lake Shore Dr (US-41)",
            "longitude" : -87.8300103,
            "mileMarker" : "269.4 to 293.7",
            "severity" : "Minor",
            "source" : "IDOT",
            "timePeriods" : "12/22/23 9:00 AM to 3:00 PM",
            "toCity" : "Chicago",
            "toCounty" : "Cook",
            "toState" : "IL"
         },
         {
            "announcementId" : "",
            "closureDetails" : "Both shoulders closed, all lanes open",
            "description" : "Long Term Closure",
            "fromCity" : "Woodridge",
            "fromCounty" : "DuPage",
            "fromState" : "IL",
            "fullLocation" : "NB Stevenson / I-55 from 0.5 miles south of Lemont Rd, Woodridge, DuPage, IL to 0.5 miles north of Lemont Rd, Darien, DuPage, IL",
            "id" : "IL-IDOT-ROADWORK.2023.12.18.12.6011175",
            "latitude" : 41.7166538,
            "location" : "0.5 miles south of Lemont Rd to 0.5 miles north of Lemont Rd",
            "longitude" : -88.0068167,
            "mileMarker" : "270.4 to 271.4",
            "severity" : "Minor",
            "source" : "IDOT",
            "timePeriods" : "8/12/22 12:00 AM to 12/27/23 11:59 PM",
            "toCity" : "Darien",
            "toCounty" : "DuPage",
            "toState" : "IL"
         },
         {
            "announcementId" : "",
            "closureDetails" : "All lanes and shoulders closed",
            "description" : "Long Term Closure",
            "fromCity" : "Darien",
            "fromCounty" : "DuPage",
            "fromState" : "IL",
            "fullLocation" : "Ramp from NB Stevenson / I-55 to NB Lemont Rd, Darien, DuPage, IL",
            "id" : "IL-IDOT-ROADWORK.2023.12.18.12.6011177",
            "latitude" : 41.7171908,
            "location" : "Exit ramp to NB Lemont Rd",
            "longitude" : -88.0055577,
            "mileMarker" : "270.9",
            "severity" : "Medium",
            "source" : "IDOT",
            "timePeriods" : "8/12/22 12:00 AM to 12/27/23 11:59 PM",
            "toCity" : "Darien",
            "toCounty" : "DuPage",
            "toState" : "IL"
         }
      ],
      "tableName" : "I-55 NB",
      "tablePath" : "GATEWAY.IL.I-55.I-55 NB"
   }
]
```

## Special Events

*For the bounding-box/GeoJSON form of this data, see [Map Data → Special Events](map-data.md#special-events).*

The GTIS allows active special events like stadium events, festivals, and parades to be downloaded in JSON format.

### Request

```console
https://travelmidwest.com/lmiga/specialEvents.json?path=[path]
```

The "path" parameter must match one of the parameter values from reportLocations.json. The path can be any value from reportLocations.json and not just leaf reports. If an upper level report is requested, then multiple special event reports will be returned in a JSON array, one for each leaf report contained within the upper-level parent report.

### Response

Returns special events associated with a given report in JSON format with the following fields:

- reportRows — an array of special event reports
  - location — an HTML <a> tag linking to the [TravelMidwest.com/lmiga/map.jsp](http://TravelMidwest.com/lmiga/map.jsp) page where the incident is located
  - mileMarker — mile marker on the report location's expressway where the incident is located
  - severity — severity of construction event Unknown, None, Minor, Medium, or Major
  - closureDetails — lanes that are closed
  - timePeriods — start date/time to end date/time of event. There are multiple formats for this field in order to minimize the amount of text used to describe the time periods.
  - source — agency that sent the construction event to the GTIS
  - description — textual description of the construction event as sent by source agency
- tableName — expressway and direction
- tablePath — see Path section above

## Congestion

*For the bounding-box/GeoJSON form of this data, see [Map Data → Congestion](map-data.md#congestion).*

The GTIS provides a fixed number of congestion links that can be downloaded in JSON format.

### Request

```console
https://travelmidwest.com/lmiga/congestion.json?path=[path]
```

The "path"// //parameter must match one of the parameter values from reportLocations.json. If the path is not a leaf in the report location hierarchy, then all leaf reports will be returned in an array.

### Response

Returns congestion report in JSON format. The URL for this page is "congestion.json?path=[path]" where path defines the report (e.g., GATEWAY.IL.I-55) for I-55 in Illinois. The returned JSON is an array of javascript objects. Each object has the following fields:

- tablePath — path from reportLocations.json
- tableName — header description of report location, e.g., "I-55 NB"
- reportRows — array of travel time data objects, each with the following fields:
  - img — congestion img link like images/congestion_light.gif
  - on — always blank
  - from — "from" cross street name
  - to — "to" cross street name
  - len — length of road between "from" and "to" in miles
  - level — "Unknown", "Uncongested", "Light", "Medium", or "Heavy"

### Example

```console
https://travelmidwest.com/lmiga/congestion.json?path=GATEWAY.IL.I-55
```

```json
[{
        "tableName": "I-55 NB",
        "reportRows": [{
                "img": "<img src='images/congestion_unknown.gif' alt='Unknown Congestion'/>",
                "on": "",
                "from": "Reed Rd (+0.5 miles)",
                "to": "Lorenzo Rd (+0.2 miles)",
                "len": "6.6"
            }, {
                "img": "<img src='images/congestion_unknown.gif' alt='Unknown Congestion'/>",
                "on": "",
                "from": "Bluff Rd (+0.5 miles)",
                "to": "Black Rd (+1.0 miles)",
                "len": "7.7"
            },
.
.
.
        ],
        "tablePath": "GATEWAY.IL.I-55.I-55 NB"
    }, {
        "tableName": "I-55 SB",
        "reportRows": [{
                "img": "<img src='images/congestion_unknown.gif' alt='Unknown Congestion'/>",
                "on": "",
                "from": "",
                "to": "Bluff Rd (-0.5 miles)",
                "len": "46.6"
            }, {
                "img": "<img src='images/congestion_unknown.gif' alt='Unknown Congestion'/>",
                "on": "",
                "from": "Lorenzo Rd (-0.2 miles)",
                "to": "Reed Rd (-0.4 miles)",
                "len": "6.7"
            }
        ],
.
.
.
        "tablePath": "GATEWAY.IL.I-55.I-55 SB"
    }
]
```

## Camera Locations and Report

*For the bounding-box/GeoJSON form of this data, see [Map Data → Cameras](map-data.md#cameras).*

There are two end points for the camera report:

1. **cameraReportLocations.json** — provides a list of all report locations that contain cameras
1. **cameraReport.json?path=[path]** — provides a list of cameras for the given report location

### Camera Report Locations

#### Request

```
https://travelmidwest.com/lmiga/cameraReportLocations.json
```

#### Response

`The data returned will be similar to `reportLocations.json, but arranged differently with state and arterial report locations interleaved. Also, report locations that have no cameras will be filtered from the normal report location hierarchy.

1. GATEWAY
1. GATEWAY.REGIONAL
  1. GATEWAY.REGIONAL.I-39
  1. GATEWAY.REGIONAL.I-55
  1. . . .
1. GATEWAY.IL
  1. GATEWAY.IL.I-39
  1. GATEWAY.IL.I-55
  1. . . .
1. GATEWAY.IL.ARTERIALS
  1. GATEWAY.IL.ARTERIALS.ADAMS
  1. GATEWAY.IL.ARTERIALS.CHAMPAIGN
  1. . . .
1. ~-~- repeats for other states ~-~-
The following fields will be present for each camera report location in the returned JSON array:

- path — see "path" description above, this is a unique identifier for the report table
- label — a human readable label for the report table
- children — descendant children reports, if any, may be an empty array
Example response:

```json
[{
        "path": "GATEWAY",
        "label": "Entire Region",
        "children": []
    }, {
        "path": "GATEWAY.REGIONAL",
        "label": "Regional Expressways",
        "children": [{
                "path": "GATEWAY.REGIONAL.I-39",
                "label": "I-39 Expressways",
                "children": []
            }, {
                "path": "GATEWAY.REGIONAL.I-55",
                "label": "I-55 Expressways",
                "children": []
            }, {
                "path": "GATEWAY.REGIONAL.I-80",
                "label": "I-80 Expressways",
                "children": []
            }, {
                "path": "GATEWAY.REGIONAL.I-90",
                "label": "I-90 Expressways",
                "children": []
            }, {
                "path": "GATEWAY.REGIONAL.I-94",
                "label": "I-94 Expressways",
                "children": []
            }
        ]
    }, {
        "path": "GATEWAY.IL",
        "label": "Illinois Expressways",
        "children": [{
                "path": "GATEWAY.IL.I-39",
                "label": "I-39 Expressways",
                "children": []
            }, {
                "path": "GATEWAY.IL.I-55",
                "label": "I-55 Expressways",
                "children": []
            }, {
                "path": "GATEWAY.IL.I-57",
                "label": "I-57 Expressways",
                "children": []
            },
.
.
.
        ]
    }, {
        "path": "GATEWAY.IL.ARTERIALS",
        "label": "Illinois Arterials",
        "children": [{
                "path": "GATEWAY.IL.ARTERIALS.ADAMS",
                "label": "Adams County",
                "children": []
            }, {
                "path": "GATEWAY.IL.ARTERIALS.CHAMPAIGN",
                "label": "Champaign County",
                "children": []
            }, {
.
.
.
```

### Camera Report

#### Request

The following URL is used to access the congestion report data in JSON format: [https://travelmidwest.com/lmiga/cameraReport.json?path=~\[path~\]](https://travelmidwest.com/lmiga/cameraReport.json?path=[path)]. If a path parameter is not provided, then the "FavoriteLocations" cookie is used if possible. FavoriteLocations should be a comma separated list of report location paths.
The "path"// //parameter must match one of the parameter values from cameraReportLocations.json. If the path is not a leaf in the report location hierarchy, then all leaf reports will be returned in an array.

#### Response

The response will be a JSON object with the following fields:

- updatedMessage — "Updated: m/d/yyyy h:MM AM/PM"
- noDataMessage — a message to explain the lack of cameras, or empty if there are cameras
- reportTables — an array of objects, each with the following fields:
  - path — report location path, e.g. "GATEWAY.IL.ARTERIALS.LAKE"
  - displayName — human readable name for table, e.g. "Lake County"
  - cells — an array of objects, each with the following:
    - externalId — unique id for camera
    - name — agency's name for camera
    - agency — name of the agency, e.g. "Lake County"
    - location — location of camera
    - idotDistrict — district number from 1 to 9 if known
    - imageAge  — "M minutes, S seconds old" for camera
    - imageDirections — an array of objects for each direction the camera can point:
      - age — "M minutes, S seconds old" for this direction
      - url — image URL
      - encodedUrl — same as URL but encoded
    - direction — default direction for camera
    - url — url if camera does not have any imageDirections
    - singleView — "true" to use url, "false" to use imageDirections
    - latitude — latitude of the camera in decimal degrees
    - longitude — longitude of the camera in decimal degrees

## DMS Report

The dynamic message sign (DMS) report provides overhead message sign images for a given report location.

### Request

```console
https://travelmidwest.com/lmiga/dmsReport.json?path=[path]
```

The "path" parameter must match one of the parameter values from reportLocations.json. The path can be any value from reportLocations.json and not just leaf reports. If an upper-level report is requested, then multiple DMS reports will be returned in a JSON array, one for each leaf report contained within the upper-level parent report.

### Response

Returns DMS associated with a given report in JSON format with the following fields:

- reportRows — an array of incident reports
  - statusImage — HTML for status image e.g., "<img src='images/GREY.gif' alt='Unknown'>"
  - status — Unknown, Not available, Operational, Operational but degraded, Non-operational, Communications failure, or Down for maintenance
  - location — location of DMS
  - mileMarker — mile marker on the report location's expressway where the incident is located
  - message — HTML representing DMS's text, may contain <br/> tags seprating lines and "~-~-~-~-~-~-~-~-~-~-" to separate phases
  - messageImageUrl — <img src> URL for image representing DMS sign, "messageSign?id=[id]"
  - source — agency that sent the DMS image
  - id — unique identifier for DMS
  - lastReportReceived — m/d/yyyy HH:MM AM/PM of last time GTIS received data for this DMS
  - lastUpdateTime — m/d/yyyy HH:MM AM/PM timestamp sent by agency
- tableName — expressway and direction
- tablePath — see Path section above

## VDS Report

Vehicle Detector Station (VDS)

> [!WARNING]
> 7/20/2023 — The vdsReport.json API endpoint is only available on the testing system.

### Request

```
https://travelmidwest.com/lmiga/vdsReport.json?path=[path]
```

The "path" parameter must match one of the parameter values from reportLocations.json. The path can be any value from reportLocations.json and not just leaf reports. If an upper-level report is requested, then multiple VDS reports will be returned in a JSON array, one for each leaf report contained within the upper-level parent report.

### Response

Returns VDS associated with a given report in JSON format with the following fields:

- reportRows — an array of incident reports
  - statusImage — HTML for status image e.g., "<img src='images/GREY.gif' alt='Unknown'>"
  - status — Unknown, Not available, Operational, Operational but degraded, Non-operational, Communications failure, or Down for maintenance
  - location — location of VDS
  - mileMarker — mile marker on the report location's expressway where the incident is located
  - speed — in mile per hour (MPH)
  - occupancy — percent occupancy
  - volume — in vehicles per hour per lane
  - source — agency that sent the VDS image
  - id — unique identifier for VDS
  - lastReportReceived — m/d/yyyy HH:MM AM/PM of last time GTIS received data for this VDS
  - lastUpdateTime — m/d/yyyy HH:MM AM/PM timestamp sent by agency
- tableName — expressway and direction
- tablePath — see Path section above

## Weather Station Report

*For the bounding-box/GeoJSON form of this data, see [Map Data → Weather Stations](map-data.md#weather-stations).*

Weather Sensor Station (WSS)

> [!WARNING]
> 7/20/2023 — The weatherStationReport.json API endpoint is only available on the testing system.

### Request

```console
https://travelmidwest.com/lmiga/weatherStationReport.json?path=[path]
```

The "path" parameter must match one of the parameter values from `reportLocations.json`. The path can be any value from `reportLocations.json` and not just leaf reports. If an upper-level report is requested, then multiple WSS reports will be returned in a JSON array, one for each leaf report contained within the upper-level parent report.

### Response

Returns weather station reports associated with a given location in JSON format with the following fields:

- reportRows — an array of incident reports
  - statusImage — HTML for status image e.g., "<img src='images/GREY.gif' alt='Unknown'>"
  - status — Unknown, Not available, Operational, Operational but degraded, Non-operational, Communications failure, or Down for maintenance
  - location — location of VDS
  - mileMarker — mile marker on the report location's expressway where the incident is located
  - atmosReadings — summary text of atmospheric readings
  - precipitation — textual description of precipitation seen
  - pavementCondition — textual description of pavement conditions
  - readingsTime — m/d/yyyy HH:MM AM/PM of when data was collected
  - source — agency that sent the VDS image
  - id — unique identifier for VDS
  - lastReportReceived — m/d/yyyy HH:MM AM/PM of last time GTIS received data for this VDS
  - lastUpdateTime — m/d/yyyy HH:MM AM/PM timestamp sent by agency
- tableName — expressway and direction
- tablePath — see Path section above
