# Trucker Reports

## About

The trucker reports are broken down into incidents, travel times and construction that are relevant to the truckers (i.e., major events and unusually high travel times).

## Trucker Construction

The construction events for the truckerConstruction.json file consist of events that are:

- Active or about to be active in the next 24 hours
- Are marked as severity "Major"

### Request URL

```console
https://travelmidwest.com/lmiga/truckerConstruction.json
```

### Response

The data returned in `truckerConstruction.json` is an array of objects, each with the following fields:

- id — unique id for the construction event
- briefLocation — on road, from road and to road without jurisdictions
- fullLocation — same as brief location but includes city, county and state
- fromCity — name of city event starts in
- fromCounty — county the event starts in
- fromState — state the event starts in
- toCity — city the event ends in
- toCounty = county event ends in
- toState  — state the event ends in
- mileMarker — mile marker or range of mile markers on the "onRoad"
- severity — Should be "Major" for the truckers
- closureDetails — lanes closed
- timePeriods — describes times the road work is or will be active
- source — agency that provided data
- description — description of road work
- announcementId — if there is an announce,ment linked to this road work, the id will be provided in this field
- latitude — in decimal degrees
- longitude — in decimal degrees

> [!NOTE]
> A given construction event may appear in more than one object entry if it has multiple locations associated with it. In this case, there will be one object int he returned array for each location.

### Example

```json
[
   {
      "announcementId" : "",
      "briefLocation" : "NB US-151 at Mendota St",
      "closureDetails" : "All lanes closed and both shoulders open",
      "description" : "Maintenance",
      "fromCity" : "Madison",
      "fromCounty" : "Dane",
      "fromState" : "WI",
      "fullLocation" : "NB US-151 at Mendota St, Madison, Dane, WI",
      "id" : "WI-WisDOT-ROADWORK.2023.7.21.0.6179016",
      "latitude" : 43.1188523,
      "longitude" : -89.3214072,
      "mileMarker" : "",
      "severity" : "Major",
      "source" : "WisDOT",
      "timePeriods" : "6/19/23 6:00 AM to 9/22/23 6:00 PM",
      "toCity" : "Madison",
      "toCounty" : "Dane",
      "toState" : "WI"
   }
]
```

## Trucker Incidents

Trucker incidents are incidents that meet the following criteria:

- Are active (i.e., haven't ended yet) or are clearing with traffic present
- Have high confidence level
- Have passed validation checks
- Have one of the following:
  - "Major" severity
  - Expected to last an hour or more
  - Have already lasted at least an hour

### Request

```console
https://travelmidwest.com/lmiga/truckerIncidents.json
```

### Response

The data returned in `truckerIncidents.json` is an array of major incidents, each object with the following fields:

- id — unique identifier for incident
- description — description of incident
- briefLocation — on road, from road and to road without jurisdictions
- fullLocation — same as brief location but includes city, county and state
- fromCity — name of city event starts in
- fromCounty — county the event starts in
- fromState — state the event starts in
- toCity — city the event ends in
- toCounty = county event ends in
- toState  — state the event ends in
- mileMarker — single or range or mile marker numbers on the highway where incident occurred
- closureDetails — description of lanes closed
- status — New, Updated, Canceled, Closed, Deleted, or Clearing
- startTime — M/d/yy h:mm a
- estimatedEndTime — M/d/yy h:mm a
- source — name of agency that sent incident information
- latitude — in degrees, useful for map centering
- longitude — in degrees, useful for map centering
A given incdent event may appear in more than one object entry if it has multiple locations associated with it. In this case, there will be one object int he returned array for each location.

### Example

```json
[
   {
      "briefLocation" : "Crash on US 51 South at Ramp from I-39 North. The right shoulder is blocked.",
      "closureDetails" : "Right shoulder closed, all lanes open",
      "description" : "Crash on US 51 South at Ramp from I-39 North. The right shoulder is blocked.",
      "estimatedEndTime" : "Unknown",
      "fromCity" : "Burke",
      "fromCounty" : "Dane",
      "fromState" : "WI",
      "fullLocation" : "Crash on US 51 South at Ramp from I-39 North. The right shoulder is blocked., Burke, Dane, WI",
      "id" : "WI-WisDOT-INCIDENT.2023.7.21.6.6179450",
      "latitude" : 43.1828881,
      "longitude" : -89.3242941,
      "mileMarker" : "",
      "source" : "WisDOT",
      "startTime" : "7/21/23 6:40 AM",
      "status" : "Updated",
      "toCity" : "Burke",
      "toCounty" : "Dane",
      "toState" : "WI"
   }
]
```

## Trucker Travel Times

The `truckerTravelTimes..json` file returns travel time "watch zones". Watch zones are travel time reports that meet the following criteria:

- Has travel time statistics
- Travel time is not disabled by system operator
- Travel time passed validation testing
- Travel time congestion level is not "Unknown"
- Has a valid location
- Is more than 8 miles long
- Travel time is more than 33% higher than average travel time OR is marked as congestion level "Heavy"

### Request

```console
https://travelmidwest.com/lmiga/truckerTravelTimes.json
```

### Response

The data returned in truckerTravelTimes.json is as follows:

- id — unique identifier for the travel time, may also be used to link to statistics web site
- onRoad — name of road the travel time is for
- congestionLevel — "Uncongested", "Light", "Medium", or "Heavy"
- fromRoad — start of travel time location on the "onRoad"
- toRoad — ending cross street of travel time lionk
- travelTime — in minutes
- averageTravelTime — in minutes
- length — in miles
- speed — in MPH
- overAverage — true or false depending on whether travel time is more than 50% above average travel time

### Example

```json
[{
        "id": "IL-TIMS-I_294-N-17",
        "onRoad": "NB I-294",
        "congestionLevel": "Light",
        "fromRoad": "83rd St Plaza",
        "toRoad": "Cermak Rd (22nd St) Plaza",
        "travelTime": "16",
        "averageTravelTime": "12",
        "length": "10.5",
        "speed": "39",
        "overAverage": "false"
    }, {
        "id": "IL-TESTTSC-165",
        "onRoad": "SB Edens Expy",
        "congestionLevel": "Light",
        "fromRoad": "Deerfield Rd",
        "toRoad": "Wilson Ave",
        "travelTime": "27",
        "averageTravelTime": "19",
        "length": "16.4",
        "speed": "36",
        "overAverage": "false"
    },
{
```

## Trucker Announcements

Trucker announcements are any announcements that have been flagged as important to the trucker community.

### Request

```console
https://travelmidwest.com/lmiga/truckerAnnouncements.json?state=[state]
```

`[state]` is the name of a state in the coverage area — "", "Illinois", "Indiana", "Michigan", "Wisconsin", "Iowa", "Missouri", or "Kentucky"

Note that the empty string ("") or no *state* parameter will return all trucking related announcements in all states.

### Response

A trucker announcements request returns an array of JSON objects with the following fields:

- id — identifier for announcement
- title — Title of announcement
- html — HTML markup with content of announcement
- icon — URL of icon for announcement (relative to `https:~/~/travelmidwest.com/lmiga/`)
- link — URL of related web page for announcement
- creationDate — milliseconds since epoch to date of announcement's creation
- lastUpdate — milliseconds since epoch (1/1/1970 Midnight) to time this announcement was last updated
- events — array of event identifiers that are associated with this announcement (may be empty)

### Example

The following is an example from `state=Illinois` on 8/2/2023:

```json
[{
        "id": 614681953,
        "title": "Inspections on I-55 bridges over Des Plaines River ",
        "html": "\r\n        \r\n        \r\n      <p class=\"MsoNormal\"><span><b><span>CHICAGO</span></b></span><span><span>\r\n – The Illinois Department of Transportation announced today that a \r\nroutine inspection of the Interstate 55 bridges over the Des Plaines \r\nRiver, near Channahon, will begin, weather permitting, Monday, Aug. 7.</span></span></p>\r\n\r\n<p class=\"MsoNormal\"><span><span>To complete the inspections, daily lane\r\n closures will be required, starting with the southbound bridges until \r\napproximately Aug.\r\n 14, when inspections begin on the northbound bridges. The inspections \r\non both bridges are expected to be completed by Saturday, Aug. 19, \r\nweather permitting. <br></span></span></p>\r\n<p class=\"MsoNormal\"><span><span>To minimize the impact to traffic, the \r\nsouthbound closures will take place between 7 a.m. and 2 p.m., Monday \r\nthrough Thursday and\r\n Saturdays, if necessary. The northbound closures will take place from 9\r\n a.m. to 3 p.m. A minimum of one lane in both directions will remain \r\nopen during inspections. <br></span></span></p>\r\n<span></span>\r\n<p class=\"MsoNormal\"><span>Motorists can expect delays and should allow \r\nextra time for trips through this area. Alternative routes are \r\nencouraged. Drivers are urged to pay close attention to flaggers\r\n and signs in the work zones, obey the posted speed limits and be on the\r\n alert for workers and equipment. <br></span></p>\r\n<p class=\"MsoNormal\"><span>Over the\r\n</span><span><a href=\"https://idot.illinois.gov/transportation-system/transportation-management/transportation-improvement-programs/myp.html\"><span>next six years</span></a></span><span>,\r\n IDOT is planning to improve more than 3,000 miles of highway and nearly\r\n 10 million square feet of bridge deck as part of the Rebuild Illinois \r\ncapital program, which is investing $33.2 billion into all modes of \r\ntransportation.\r\n</span><span><a href=\"https://idot.maps.arcgis.com/apps/dashboards/90fafc6f3acc49cfa4577104115c43a0\"><span>Accomplishments</span></a></span><span>\r\n through Year Four of Rebuild Illinois included approximately $12.1 \r\nbillion of improvements statewide on 5,339 miles of highway, 533 bridges\r\n and 762 additional safety improvements.</span></p>\r\n      ",
        "icon": "webfile/images/IDOTLogo.gif",
        "link": "",
        "creationDate": "2023-07-25T22:07:29.979+00:00",
        "lastUpdate": "2023-07-25T22:10:55.446+00:00",
        "events": []
    },
. . .
```
