# Chicago Quick Traffic

## About

The chicagoQuickTraffic.json and chicagoQuickTrafficDetail.json endpoints provide legacy travel time information for expressways in and around the City of Chicago.

## chicagoQuickTraffic.json

### Request

```console
https://travelmidwest.com/lmiga/chicagoQuickTraffic.json
```

Both GET and POST requests are supported. There are no parameters. The chicagoQuickTraffic.json file contains travel times for multiple expressways in the Chicago area in the following two elements of an array:

- 0th element — age and oldest object with the following two fields:
  - ageInMinutes — "XX" number of minutes
  - oldest — "dow MMM dd HH:mm:ss zzz yyyy"
- 1st element — list of expressway objects, each with the following fields:
  - caption — string detailed description of the expressway, "Kennedy Expressway (I-90, I-90/94)" for example
  - path — see section 6.1 for path description
  - webCaption — shorter version of caption, "Kennedy — I-90" for example
  - rows — array of travel time segments on the given expressway objects, each containing the following fields:
    - description — string description of travel time segment, "Inbound Kennedy from O'Hare to I-290/Jane Byrne Interchange" for example
    - shortDescription — shorter version of description meant to be used for mobile applications, "IB O'Hare to I-290" for example
    - ids — array of travel time report identifiers that were added together to make this segment's travel time
    - travelTime — XX — whole number of minutes
    - speed — YY — whole number in MPH
    - id — first element of ids array or the word "multiple"
    - over — "true" if over 50% higher than average travel time for this segment for this time of day and day of week, "false" otherwise

### Response

```json
[{
        "ageInMinutes": "11",
        "oldest": "Mon Jun 05 16:31:37 CDT 2023"
    }, [{
            "caption": "Kennedy Expressway (I-90, I-90/94)",
            "path": "GATEWAY.IL.KENNEDY",
            "wapCaption": "Kennedy - I-90",
            "rows": [{
                    "description": "Inbound Kennedy from O'Hare to I-290/Jane Byrne Interchange",
                    "shortDescription": "IB O'Hare to I-290",
                    "ids": ["IL-TESTTSC-192"],
                    "travelTime": 50,
                    "speed": 20,
                    "id": "IL-TESTTSC-192",
                    "over": false
                }, {
                    "description": "Inbound Kennedy from Montrose to I-290/Jane Byrne Interchange",
                    "shortDescription": "IB Montrose to I-290",
                    "ids": ["IL-TESTTSC-232"],
                    "travelTime": 17,
                    "speed": 29,
                    "id": "IL-TESTTSC-232",
                    "over": false
                },
                .
                .
                .
      }]
}]
```

## chicagoQuickTrafficDetail.json

### Request

```console
https://travelmidwest.com/lmiga/chicagoQuickTrafficDetail.json?id=[id]
```

The `chicagoQuickTrafficDetail.json` endpoint provides more details for one travel time segment in the `chicagoQuickTraffic.json` file where `id` is an ID from the chicagoQuickTraffic.json file. The `chicagoQuickTrafficDetail.json` endpoint returns one object with the following fields:

- location — same as description in the chicagoQuickTraffic.json file
- travelTime — same as the travelTime in chicagoQuickTraffic.json
- averageTravelTime — average travel time for segment in whole number of minutes for current day of week and time of day
- congestion — UNKNOWN_CONGESTION_LEVEL, NON_CONGESTION, LIGHT_CONGESTION, MEDIUM_CONGESTION, HEAVY_CONGESTION
- length — length of travel time segment in whole number of miles
- speed — average speed across segment in MPH
- lastUpdate — time travel time segment was updated
