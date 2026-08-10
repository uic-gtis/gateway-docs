# Locate City

## About

The locateCity.json endpoint returns a list of cities and their lat/long coordinates for use with map zooming and centering. The endpoint is meant to be used in an incremental search functionality and can return back a list based on incomplete input. For instance, "Mill " will return "Mill Creek, Illinois", "Mill Creek, Indiana" and "Mill Shoals, Illinois". The list is truncated to the first 10 matches. Matches will either be against the first few letters of the city name matching the "name" parameter, if possible, or, if there are no matches based on the first few characters, then matches will be based on the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) between the "name" parameter and all city names. In the later case, then 10 lowest Levenshtein distance cities will be returned. The use of the Levenstein distance allows for misspellings such as "Nspervill " for "Naperville, Illinois".

## Request

```console
https://travelmidwest.com/lmiga/locateCity.json?name=[name]
```

The request is a simple request parameter "name" which can be the full or partial name of a city in the coverage area.

## Response

The response will be a JSON array with the following fields:

- name — human readable city name
- center — array of longitude in degrees and latitude in degrees
- size — in square meters
- population — not used
- fips — city, county, state, cityCode, stateCode

## Example

```console
https://travelmidwest.com/lmiga/locateCity.json?name=Chicago
```

```json
[
    {
        "name": "Chicago Heights",
        "center": [
            -87.5999462,
            41.5124184
        ],
        "size": 2.11302832E8,
        "population": 30408,
        "fips": {
            "city": "Chicago Heights",
            "county": "Cook",
            "state": "Illinois",
            "cityCode": 14026,
            "stateCode": 17
        }
    },
    {
        "name": "Chicago Ridge",
        "center": [
            -87.778848,
            41.7054691
        ],
        "size": 1.9527424E7,
        "population": 14366,
        "fips": {
            "city": "Chicago Ridge",
            "county": "Cook",
            "state": "Illinois",
            "cityCode": 14065,
            "stateCode": 17
        }
    },
    {
        "name": "Chicago",
        "center": [
            -87.7316876,
            41.8340495
        ],
        "size": -1.692346799E9,
        "population": 0,
        "fips": {
            "city": "Chicago",
            "county": "Cook",
            "state": "Illinois",
            "cityCode": 14000,
            "stateCode": 17
        }
    }
]
```
