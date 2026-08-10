# Truck Parking Reports

## About

[Truck Parking Information System (TPIMS)](https://truckparking.travelmidwest.com/) provides parking lot locations and stall availability information.

## Truck Parking GPS Report

The truck parking GPS report accepts a latitude and longitude, returning a list of truck parking lots sorted by distance from the provided coordinates.

### Request

```console
https://travelmidwest.com/lmiga/tpimsGpsReport.json
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

The response will consist of a list of truck parking lot objects and distInMiles:

- lot
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
- distanceInMiles - float number distance from currentPosition to the lot

### Example

Request with GPS coordinates in Peoria, Illinois:

```console
curl 'https://testing81.travelmidwest.com/lmiga/tpimsGpsReport.json' -H 'Accept: application/json' --data-raw '{"coords": {"accuracy":228,"altitude":null,"altitudeAccuracy":null,"heading":null,"latitude":40.69365,"longitude":-89.58899,"speed":null},"timestamp":1710253937081}'
```

Response:

```json
[{
        "distanceInMiles": 18.881216217486024,
        "lot": {
            "siteId": "IL00074IE011400005",
            "availableSpots": "21",
            "capacity": "25",
            "timestamp": "2024-03-12T14:33:21.331Z",
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
        "distanceInMiles": 19.549926716708704,
        "lot": {
            "siteId": "IL00074IW011400006",
            "availableSpots": "12",
            "capacity": "18",
            "timestamp": "2024-03-12T14:32:50.351Z",
            "exit": "",
            "highway": "WB I-74",
            "milePost": "114.0",
            "amenities": [],
            "images": [],
            "trustData": true,
            "open": true,
            "trend": "Filling"
        }
    }, {
        "distanceInMiles": 29.183996303699008,
        "lot": {
            "siteId": "IL00074IW006200004",
            "availableSpots": "4",
            "capacity": "12",
            "timestamp": "2024-03-12T14:33:21.516Z",
            "exit": "",
            "highway": "WB I-74",
            "milePost": "62.0",
            "amenities": [],
            "images": [],
            "trustData": true,
            "open": true,
            "trend": "Steady"
        }
    }, {
        "distanceInMiles": 29.335122706946592,
        "lot": {
            "siteId": "IL00074IE006200001",
            "availableSpots": "9",
            "capacity": "13",
            "timestamp": "2024-03-12T14:32:48.756Z",
            "exit": "",
            "highway": "EB I-74",
            "milePost": "62.0",
            "amenities": [],
            "images": [],
            "trustData": true,
            "open": true,
            "trend": "Steady"
        }
    }
]
```

## Truck Parking Report

The truck parking report returns a list of all known truck parking lots in the coverage area.

### Request

```console
https://travelmidwest.com/lmiga/tpimsReport.json
```

### Response

The response will consist of a list of truck parking lot objects, each with the following fields:

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
