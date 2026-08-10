# Message Alerts

## About

Message alerts provide short yet important traffic information. Message alerts are displayed in a rotating banner across the top of the [TravelMidwest.com](http://TravelMidwest.com) website. There are two types of message alert files available:

1. messages.json — alerts are an array of HTML strings with embedded hyperlinks. This API is deprecated and will be removed in the near future.
1. alerts.json — alert data is broken out into separate fields such as the incident, metro area, and lat/long.

## messages.json

> [!WARNING]
> The `messages.json` API is deprecated and will be removed, use `alerts.json` instead.

### Request

```console
https://travelmidwest.com/lmiga/messages.json
```

### Response

A Message Alerts request returns a JSON object containing an array of strings, one for each message.

### Example

```console
[
   "Chicago Skyway and Indiana Toll Road information is currently unavailable.",
   "Madison County, Illinois - I-270 will be closed in both the eastbound and westbound directions on Wednesday, February 4, 2015, weather permitting. The lane closures will begin at 9:45 a.m. and will reopen within two hours. <a href=\\\"https://travelmidwest.com/lmiga/announcements.jsp?type=highPriority\\\" class=\\\"motdLink\\\" title=\\\"popup text\\\"> More information.</a>"
]
```

## alerts.json

The `alerts.json` file breaks out the various data fields separately.

### Request

```console
https://travelmidwest.com/lmiga/alerts.json
```

### Response

The alerts.json file will be a list of objects, each with the following fields:

- text — text of the alert
- incidentId — incident identifier, if any, for major accident alerts
- mapName — name of the map for heavy congestion alerts
- latitude — in decimal degrees, if known, otherwise null
- longitude — in decimal degrees, if known, otherwise null

### Example

```json
[
    {
        "text": "Heavy congestion in Chicago area on EB I-80 and NB Lake Shore Dr",
        "incidentId": null,
        "mapName": "chicagoArea",
        "latitude": null,
        "longitude": null
    },
    {
        "text": "Partial closure incident on WB I-90 (Jane Addams Memorial Tollway) at Roselle Rd (+1.3 miles), Hoffman Estates, Cook, IL",
        "incidentId": "IL-TESTTIMS-INCIDENT.2023.10.18.12.5972095",
        "mapName": null,
        "latitude": 42.06672,
        "longitude": -88.1058
    }
]
```
