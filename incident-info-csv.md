# incidentInfo.csv

The `incidentInfo.csv` web service provides real-time incident information in comma-separated values (CSV) format:

```
https://travelmidwest.com/lmiga/incidentInfo.csv
```

The web service accepts up to three optional filter parameters.

1, Include only incidents in the states and counties provided:

```
incidentInfo.csv?stateAndCounty=state1,county1&stateAndCounty=state2,county2&...stateAndCounty=state_n,county_n
```

2. Include only incidents in the given IDOT District (integer from 1 to 9):

```
incidentInfo.csv?idotDistrict=district1&idotDistrict=district2...&idotDistrict=district_n
```

3. Include IDOT District incidents from Station One:

```
incidentInfo.csv?stationOne=true
```

If no parameters are provided for `stateAndCounty,` `idotDistrict, or stationOne`, then all known incidents in District 8 will be returned.

Note that some incident id's will appear more than once in the listing if the incident has multiple locations. For example, an incident that blocks both sides of the road will have two entries, one for each direction blocked.

| Column | Value |
| --- | --- |
| y | Latitude in decimal degrees. |
| x | Longitude in decimal degrees. |
| Description | Text description of incident as entered by operator. |
| Location | Direction onRoad at crossStreet, city, county, state. |
| ClosureDetails | Lanes closed. |
| Status | New, Updated, or Clearing. |
| StartTime | MM/dd/YY HH:mm z |
| EstimatedEndTime | MM/dd/YY HH:mm z |
| Source | Agency name such as MnDOT, Lake County, Illinois Tollway, MoDOT, IDOT, etc. |
| Features | Incident, Accident, Incident with road block, Incident with disabled vehicle, etc. |
| LastUpdated | MM/dd/YY HH:mm z |
| id | GTIS identifier |
| district | IDOT District number (1 through 9) or 0 if not in Illinois |
