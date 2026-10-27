# Admin incident entry

> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.

## About

The /lmiga/admin/incidentEntry endpoints provide REST APIs for creating, managing, and closing traffic incidents in the GTIS. This controller allows operators to enter incident data, resolve locations, manage lane impacts, and update incident status through RESTful endpoints.

## Authentication

Authentication is required for all endpoints in the /admin path. The loggedIn cookie must be present in all requests, and the user must be an Operator with a role named "admin" or "incidentEntry". See [Authentication](../user-api/authentication.md) for more information.

## Base URL

```console
/lmiga/admin/incidentEntry
```

### Get Dropdown Data

Retrieve all dropdown options needed for the incident entry form.

```console
GET /dropdowns.json
```

**Authentication:** Required (Operator with incidentEntry or admin role)

**Response:**

```json
{
  "success": true,
  "data": {
    "sources": [
      {
        "id": 1,
        "name": "IDOT",
        "idPrefix": "IDOT"
      }
    ],
    "confidenceLevels": [
      {
        "value": "HIGH_EVENT_CONFIDENCE_LEVEL",
        "label": "High"
      },
      {
        "value": "MEDIUM_EVENT_CONFIDENCE_LEVEL",
        "label": "Medium"
      }
    ],
    "roadwayConditions": [
      {
        "value": "DRY_ROADWAY_CONDITION",
        "label": "Dry"
      },
      {
        "value": "WET_ROADWAY_CONDITION",
        "label": "Wet"
      }
    ],
    "weatherConditions": [
      {
        "value": "CLEAR_WEATHER_CONDITION",
        "label": "Clear"
      },
      {
        "value": "RAIN_WEATHER_CONDITION",
        "label": "Rain"
      }
    ],
    "detectionTypes": [
      {
        "value": "MANUAL_DETECTION_TYPE",
        "label": "Manual"
      }
    ],
    "verificationTypes": [
      {
        "value": "VERIFIED_VERIFICATION_TYPE",
        "label": "Verified"
      }
    ],
    "laneTypes": [
      {
        "value": "Lane",
        "label": "Lane"
      },
      {
        "value": "Express",
        "label": "Express"
      },
      {
        "value": "HOV",
        "label": "HOV"
      }
    ],
    "shoulderImpacts": [
      {
        "value": "Open",
        "label": "Open"
      },
      {
        "value": "Closed",
        "label": "Closed"
      },
      {
        "value": "None",
        "label": "None"
      }
    ],
    "laneImpacts": [
      {
        "value": "Open",
        "label": "Open"
      },
      {
        "value": "Closed",
        "label": "Closed"
      },
      {
        "value": "Shifted",
        "label": "Shifted"
      }
    ],
    "durationOptions": [
      {
        "label": "15 minutes",
        "minutes": 15
      },
      {
        "label": "30 minutes",
        "minutes": 30
      },
      {
        "label": "1 hour",
        "minutes": 60
      }
    ],
    "counts": [0, 1, 2, 3, 4, 5, 6, 7, 8],
    "capabilities": ["multiLocation"]
  }
}
```

**Notes:**

- Gateway users see all event sources; a future update for agency users will provide them only their agency's sources
- Duration options range from 15 minutes to 6 hours
- `capabilities` lists what this Gateway supports beyond the single-location form. `multiLocation` means
  create and update accept a `locations` array and [Resolve Opposite Direction](#resolve-opposite-direction)
  exists. **Check for it before sending `locations`:** a Gateway without it rejects the unknown field with a
  400, so a client that checks can be deployed before or after the Gateway.

### Get New Incident Form

Retrieve an empty incident form with default values for creating a new incident.

```console
GET /new.json
```

**Authentication:** Required (Operator with incidentEntry or admin role)

**Response:**

```json
{
  "success": true,
  "data": {
    "sourceName": "IDOT",
    "confidenceLevel": "HIGH_EVENT_CONFIDENCE_LEVEL",
    "state": "EVENT_NEW_MANUAL",
    "roadwayCondition": "UNKNOWN_ROADWAY_CONDITION",
    "weather": "UNKNOWN_WEATHER_CONDITION",
    "detectionType": "UNKNOWN_DETECTION_TYPE",
    "verificationType": "UNKNOWN_VERIFICATION_TYPE",
    "automobileCount": 1,
    "accident": true,
    "occurrenceTime": "2025-10-14T10:00:00Z",
    "detectionTime": "2025-10-14T10:00:00Z",
    "verificationTime": "2025-10-14T10:00:00Z",
    "estimatedClosureTime": "2025-10-14T10:30:00Z",
    "locationResolutionStatus": "LOCATION_NO_LOCATION",
    "laneImpacts": [],
    "leftShoulder": "Open",
    "rightShoulder": "Open",
    "unspecifiedShoulder": null,
    "laneType": "Lane",
    "fullClosure": false,
    "variousLanes": false,
    "userLaneCount": 0
  }
}
```

**Notes:**

- Default times are set to current time
- Default estimated closure time is 30 minutes from current time
- Default source is the first source in the user's agency

### Get Incident by ID

Retrieve a specific incident for editing.

```console
GET /{id}.json
```

**Authentication:** Required (Operator with incidentEntry or admin role)

**URL Parameters:**

- id - The database ID of the incident

**Response:**

```json
{
  "success": true,
  "data": {
    "id": "123",
    "externalId": "IDOT-12345",
    "sourceId": "IDOT-12345",
    "locationDescription": "I-90 WB at Elgin",
    "description": "Vehicle accident",
    "comments": "Two vehicles involved",
    "sourceName": "IDOT",
    "lastUpdateTime": "2025-10-14T10:15:00Z",
    "locationResolutionStatus": "LOCATION_RESOLVED_AUTO",
    "state": "EVENT_NEW_MANUAL",
    "confidenceLevel": "HIGH_EVENT_CONFIDENCE_LEVEL",
    "severity": "MAJOR_EVENT_SEVERITY",
    "roadwayCondition": "DRY_ROADWAY_CONDITION",
    "weather": "CLEAR_WEATHER_CONDITION",
    "detectionType": "MANUAL_DETECTION_TYPE",
    "verificationType": "VERIFIED_VERIFICATION_TYPE",
    "automobileCount": 2,
    "busCount": 0,
    "motorcycleCount": 0,
    "pickupTruckCount": 0,
    "semiTrailerCount": 0,
    "tankerTruckCount": 0,
    "fatalityCount": 0,
    "injuryCount": 1,
    "accident": true,
    "fire": false,
    "hazmat": false,
    "policeAction": false,
    "medicalEmergency": true,
    "occurrenceTime": "2025-10-14T09:45:00Z",
    "detectionTime": "2025-10-14T09:46:00Z",
    "verificationTime": "2025-10-14T09:47:00Z",
    "estimatedClosureTime": "2025-10-14T10:45:00Z",
    "locations": [
      {
        "description": "I-90 WB at Elgin",
        "textProfile": "I-90 Westbound at Elgin",
        "laneCount": 3,
        "lanes": [
          {
            "laneNumber": 1,
            "impact": "Open"
          },
          {
            "laneNumber": 2,
            "impact": "Closed"
          },
          {
            "laneNumber": 3,
            "impact": "Open"
          }
        ],
        "leftShoulder": "Open",
        "rightShoulder": "Closed",
        "unspecifiedShoulder": null,
        "laneImpacts": [
          {
            "laneNumber": 1,
            "impact": "Open"
          },
          {
            "laneNumber": 2,
            "impact": "Closed"
          },
          {
            "laneNumber": 3,
            "impact": "Open"
          }
        ],
        "laneType": "Lane",
        "fullClosure": false,
        "variousLanes": false,
        "resolvedLocation": { "...": "the LinearLocation, to send back on update" }
      }
    ],
    "maxLaneCount": 3,
    "laneImpacts": [
      {
        "laneNumber": 1,
        "impact": "Open"
      },
      {
        "laneNumber": 2,
        "impact": "Closed"
      },
      {
        "laneNumber": 3,
        "impact": "Open"
      }
    ],
    "leftShoulder": "Open",
    "rightShoulder": "Closed",
    "unspecifiedShoulder": null,
    "laneType": "Lane",
    "fullClosure": false,
    "variousLanes": false
  }
}
```

**Notes:**

- `locations` holds every location of the incident: both directions of a closure entered as two locations,
  for example. Each entry carries its own lanes, in two forms: `lanes`, every lane description including the
  shoulders (at lane number 0 or -1), and the edit form's fields `laneImpacts` (numbered lanes only),
  `leftShoulder`, `rightShoulder`, `unspecifiedShoulder`, `laneType`, `fullClosure` and `variousLanes`.
- The top-level lane fields (`maxLaneCount`, `laneImpacts`, the shoulders, `laneType`, `fullClosure`,
  `variousLanes`) describe the **first** location only. They are kept for clients that edit one location.

**Error Response:**

```json
{
  "success": false,
  "error": {
    "code": "NOT_FOUND",
    "message": "Incident not found with ID: 123"
  }
}
```

### Get Incidents List

Retrieve a list of all live incidents for the current user's agency.

```console
GET /incidents.json
```

**Authentication:** Required (Operator with incidentEntry or admin role)

**Response:**

```json
{
  "success": true,
  "data": [
    {
      "id": "123",
      "externalId": "IL-COMCENTER-2020.09.30.12.8823145",
      "location": "I-90 WB at Elgin",
      "description": "Vehicle accident blocking 1 lane"
    },
    {
      "id": "124",
      "externalId": "IL-COMCENTER-2020.09.30.12.8823146",
      "location": "I-94 NB near Lake Forest",
      "description": "Stalled vehicle on shoulder"
    }
  ]
}
```

**Notes:**

- Gateway users see all live incidents across all agencies
- Agency users see only their agency's incidents (filtered by source ID prefix)
- Results are sorted alphabetically by location
- Only incidents with live state are returned

### Resolve Location

Resolve a location description to determine lane count and valid location information.

```console
POST /resolve.json
```

**Method:** POST
**Content-Type:** application/json
**Authentication:** Required (Operator with incidentEntry or admin role)

**Request Body:**

```json
{
  "locationDescription": "I-90 WB at Elgin",
  "userLaneCount": 0
}
```

**Response (Successful Resolution):**

```json
{
  "success": true,
  "data": {
    "resolved": true,
    "ambiguous": false,
    "laneCount": 3,
    "locations": [
      {
        "description": "I-90 Westbound at Elgin",
        "textProfile": "I-90 WB at Elgin Rd",
        "laneCount": 3
      }
    ]
  }
}
```

**Response (Location Not Found):**

```json
{
  "success": true,
  "data": {
    "resolved": false,
    "ambiguous": false,
    "errorMessage": "Nothing was found that matches \"I-999 at Nowhere\""
  }
}
```

**Response (Ambiguous Location):**

```json
{
  "success": true,
  "data": {
    "resolved": false,
    "ambiguous": true,
    "errorMessage": "\"Main St\" is ambiguous. Multiple locations found.",
    "locations": [
      {
        "description": "Main St at Oak Ave, Chicago",
        "textProfile": "Main St (Chicago)",
        "laneCount": 2
      },
      {
        "description": "Main St at Elm St, Naperville",
        "textProfile": "Main St (Naperville)",
        "laneCount": 4
      }
    ]
  }
}
```

**Notes:**

- This endpoint must be called before creating an incident to resolve the location
- If location cannot be resolved, user can specify `userLaneCount` to proceed with unresolved location
- Ambiguous locations return multiple options for user to choose from

### Resolve Opposite Direction

Find the opposite direction of a location already resolved, for a closure in both directions. This is the
Map Editor's **Select Opposite**: each end of the section is turned to the other carriageway.

```console
POST /resolve/opposite.json
```

**Method:** POST
**Content-Type:** application/json
**Authentication:** Required (Operator with incidentEntry or admin role)
**Requires:** `multiLocation` in the [dropdown data](#get-dropdown-data) `capabilities`

**Request Body:**

The `resolvedLocation` from a [Resolve Location](#resolve-location) response, or from a location of a fetched
incident, sent back unchanged:

```json
{
  "resolvedLocation": { "...": "the LinearLocation as received" }
}
```

**Response (Found):**

The same shape as Resolve Location. `laneCount` is the opposite direction's own, which can differ from the
direction asked about.

```json
{
  "success": true,
  "data": {
    "resolved": true,
    "ambiguous": false,
    "laneCount": 2,
    "locations": [
      {
        "description": "WB IL-116 from IL-115 to IL-47",
        "textProfile": "IL-116 from IL-47 to IL-115",
        "laneCount": 2,
        "resolvedLocation": { "...": "send this as the second location's resolvedLocation" }
      }
    ]
  }
}
```

**Response (Ramp):**

```json
{
  "success": true,
  "data": {
    "resolved": false,
    "ambiguous": false,
    "errorMessage": "The opposite direction cannot be found for a ramp."
  }
}
```

**Notes:**

- A ramp has no opposite direction, so it is refused, as in the Map Editor
- When the opposite cannot be found for another reason, `resolved` is false and `errorMessage` says why
- `textProfile` is the operator's original text, carried over unchanged

### Create Incident

Create a new incident.

```console
POST create.json
```

**Method:** POST
**Content-Type:** application/json
**Authentication:** Required (Operator with incidentEntry or admin role)

**Request Body:**

```json
{
  "locationDescription": "I-90 WB at Elgin",
  "description": "Vehicle accident",
  "comments": "Two vehicles involved, emergency services on scene",
  "sourceName": "IDOT",
  "confidenceLevel": "HIGH_EVENT_CONFIDENCE_LEVEL",
  "severity": "MAJOR_EVENT_SEVERITY",
  "roadwayCondition": "DRY_ROADWAY_CONDITION",
  "weather": "CLEAR_WEATHER_CONDITION",
  "detectionType": "MANUAL_DETECTION_TYPE",
  "verificationType": "VERIFIED_VERIFICATION_TYPE",
  "automobileCount": 2,
  "busCount": 0,
  "motorcycleCount": 0,
  "pickupTruckCount": 0,
  "semiTrailerCount": 0,
  "tankerTruckCount": 0,
  "fatalityCount": 0,
  "injuryCount": 1,
  "accident": true,
  "fire": false,
  "hazmat": false,
  "policeAction": false,
  "medicalEmergency": true,
  "occurrenceTime": "2025-10-14T09:45:00Z",
  "detectionTime": "2025-10-14T09:46:00Z",
  "verificationTime": "2025-10-14T09:47:00Z",
  "isDurationOption": true,
  "durationMinutes": 60,
  "laneImpacts": [
    {
      "laneNumber": 1,
      "impact": "Open"
    },
    {
      "laneNumber": 2,
      "impact": "Closed"
    },
    {
      "laneNumber": 3,
      "impact": "Open"
    }
  ],
  "leftShoulder": "Open",
  "rightShoulder": "Open",
  "laneType": "Lane",
  "fullClosure": false,
  "variousLanes": false,
  "userLaneCount": 0
}
```

**Response:**

- Status: 200 OK
- Body: The created incident JSON (same structure as GET /{id}.json response)

**Validation Error Response:**

```json
{
  "success": false,
  "errors": {
    "locationDescription": "You must resolve the incident location before creating the incident.",
    "estimatedClosureTime": "\"13:00\" does not match either \"hh:mm AM/PM\", \"mm/dd/yyyy hh:mm AM/PM\" or ISO 8601 format."
  }
}
```

**Notes:**

- Location must be resolved (laneImpacts present) OR userLaneCount must be specified
- Either `isDurationOption: true` with `durationMinutes` OR `estimatedClosureTime` string must be provided
- External ID is automatically generated with format: {sourceIdPrefix}-{VMID}
- Incident is automatically published to the Gateway upon creation
- occurrenceTime, detectionTime, and verificationTime can ***null*** if unknown

#### More than one location (both directions)

**Requires:** `multiLocation` in the [dropdown data](#get-dropdown-data) `capabilities`.

An incident can have several locations, as the Map Editor enters a closure in both directions: one location
per direction. Send them as `locations`, each with its own `resolvedLocation` and lanes. Get the second
direction from [Resolve Opposite Direction](#resolve-opposite-direction).

```json
{
  "locationDescription": "IL-116 from IL-47 to IL-115",
  "description": "Road closed",
  "sourceName": "IDOT",
  "severity": "MAJOR_EVENT_SEVERITY",
  "detectionType": "MANUAL_DETECTION_TYPE",
  "isDurationOption": true,
  "durationMinutes": 120,
  "shareLaneInformation": false,
  "locations": [
    {
      "resolvedLocation": { "...": "from resolve.json" },
      "locationDescription": "EB IL-116 from IL-47 to IL-115",
      "fullClosure": true
    },
    {
      "resolvedLocation": { "...": "from resolve/opposite.json" },
      "locationDescription": "WB IL-116 from IL-115 to IL-47",
      "laneImpacts": [
        {"laneNumber": 1, "impact": "Closed"},
        {"laneNumber": 2, "impact": "Open"}
      ],
      "leftShoulder": "Open",
      "rightShoulder": "Open",
      "laneType": "Lane"
    }
  ]
}
```

- When `locations` is present it is the **complete** list of the incident's locations. The single-location
  fields (`resolvedLocation`, `laneImpacts`, the shoulders, `laneType`, `fullClosure`, `variousLanes`,
  `createUnresolved`, `userLaneCount`) are then ignored.
- Every entry must have a `resolvedLocation`. An incident whose location cannot be resolved uses the
  single-location fields with `createUnresolved`.
- `shareLaneInformation: true` is the Map Editor's "Duplicate lane information across all locations": every
  location gets the first entry's lanes and shoulders, and the lane fields of the other entries are ignored.
  Each location still stores its own copy. A shared lane numbered higher than another location's lane count
  is a validation error, because the two directions of a road can have different numbers of lanes.
- An entry's `locationDescription` defaults to the top-level `locationDescription`, and the top-level one
  defaults to the first entry's.

### Update Incident

Update an existing incident.

```console
PUT /{id}/update.json
```

**Method:** PUT
**Content-Type:** application/json
**Authentication:** Required (Operator with incidentEntry or admin role)

**URL Parameters:**

- id - The database ID of the incident to update

**Request Body:**

Same structure as Create Incident request body

**Response:**

- Status: 200 OK
- Body: The updated incident JSON (same structure as GET /{id}.json response)

**Error Response (Not Found):**

```json
{
  "success": false,
  "error": {
    "code": "NOT_FOUND",
    "message": "Incident not found with ID: 123"
  }
}
```

**Notes:**

- Incident state is automatically set to EVENT_UPDATED_MANUAL
- Updated incident is automatically published to the Gateway
- All validation rules from Create Incident apply
- **With `locations`**, the incident's locations are replaced by exactly that list.
- **Without `locations`** (the single-location shape), the request edits the incident's **first** location and
  keeps any others. An incident entered in the Map Editor with both directions therefore keeps its second
  direction when it is saved from a client that edits only one location.

### Close Incident

Close an existing incident.

```console
PUT /{id}/close.json
```

**Method:** PUT
**Authentication:** Required (Operator with incidentEntry or admin role)

**URL Parameters:**

- id - The database ID of the incident to close

**Response:**

- Status: 200 OK
- Body: The closed incident JSON (same structure as GET /{id}.json response)

**Error Response (Not Found):**

```json
{
  "success": false,
  "error": {
    "code": "NOT_FOUND",
    "message": "Incident not found with ID: 123"
  }
}
```

**Notes:**

- Closing an incident sets the closed time and estimated closure time to current time
- Incident state is set to EVENT_CLOSED_MANUAL
- Closed incident is automatically published to the Gateway

## Request Field Descriptions

### Location Fields

- **locationDescription** - String - Human-readable location description (e.g., "I-90 WB at Elgin")
- **laneImpacts** - Array of LaneImpactDto - Lane impact information for each lane
  - laneNumber - Integer - Lane number (1-based)
  - impact - String - "Open", "Closed", or "Shifted"
- **leftShoulder** - String - "Open", "Closed", or "None". An omitted value, and an empty string,
  both mean "not set": they publish an open shoulder, unless `unspecifiedShoulder` is set, in which
  case they publish no shoulder description at all. See
  [Shoulders without a side](#shoulders-without-a-side).
- **rightShoulder** - String - the same values and the same rules as `leftShoulder`.
- **unspecifiedShoulder** - String - "Open", "Closed", or "None". A shoulder closure whose side the
  reporting source never named. Optional, and **omitting it is not the same as sending "Open"**: an
  absent value publishes no shoulder description at all, so a client that does not know about this
  field cannot accidentally add one to every incident it saves. **Mutually exclusive with
  `leftShoulder` and `rightShoulder`** — sending it together with either of them is a validation
  error. See [Shoulders without a side](#shoulders-without-a-side).
- **laneType** - String - "Lane", "Express", "HOV", "Reversible", "Local", "Cash", "IPO", or "ORT"
- **fullClosure** - Boolean - True if all lanes are closed
- **variousLanes** - Boolean - True for various lane impacts
- **userLaneCount** - Integer - Manual lane count for unresolved locations

### Multiple Location Fields

Available when `capabilities` includes `multiLocation`; see
[More than one location](#more-than-one-location-both-directions).

- **locations** - Array - Every location of the incident. Omit it to use the single-location fields above.
  Each entry has:
  - resolvedLocation - Object - Required. The `resolvedLocation` from resolve.json or resolve/opposite.json
  - locationDescription - String - The text for this location
  - laneImpacts, leftShoulder, rightShoulder, unspecifiedShoulder, laneType, fullClosure, variousLanes - this
    location's lanes, with the same meanings and rules as the single-location fields
- **shareLaneInformation** - Boolean - Give every location the first entry's lanes and shoulders

### Shoulders without a side

Several upstream feeds report a shoulder closure without saying which side — "shoulder closed"
rather than "left shoulder closed". That impact cannot be attributed to a side without inventing
information, so it is carried in its own field rather than guessed at.

**A shoulder is described either by side or without one, never both.** `unspecifiedShoulder` means
the source did not say which side, so it cannot stand beside a side that was named. The Map Editor
enforces the same rule: choosing a side clears its unspecified impact, and choosing an unspecified
impact clears both sides.

Five consequences that are easy to miss:

- **A request may not name both.** Sending a real value ("Open" or "Closed") for
  `unspecifiedShoulder` together with a real value for `leftShoulder` or `rightShoulder` returns
  **400 Bad Request** with a field error on `unspecifiedShoulder`:

  ```json
  {
    "success": false,
    "errors": {
      "unspecifiedShoulder": "An unspecified shoulder means the side is unknown, so it cannot be combined with a left or right shoulder. Set the unspecified shoulder to None, or set the left and right shoulders to None."
    }
  }
  ```

  `"None"` is the absence of a shoulder description, so it never conflicts: `unspecifiedShoulder`
  with both sided fields `"None"` is the normal way to record a side-less closure.
- **The empty string means "not set", for all three fields.** It is not a value, and it is not
  `"Open"`. Sending `"unspecifiedShoulder": ""` records no side-less shoulder, and sending
  `"leftShoulder": ""` is the same as omitting it.
- **Beside a set `unspecifiedShoulder`, an omitted or empty side records nothing.** On its own an
  absent `leftShoulder` publishes an open shoulder, because an ordinary incident's shoulders are open
  unless something says otherwise. That default does not apply next to a shoulder whose side is
  unknown, since it would invent the very contradiction the rule above rejects.
- **In a response, when `unspecifiedShoulder` is set, `leftShoulder` and `rightShoulder` both read
  `"None"`.** The source described "the shoulder" without a side, so neither sided value applies. A
  client that renders only the two sided fields will show nothing at all for such an incident, which
  is exactly the failure this field exists to prevent.
- **In a request, omitting `unspecifiedShoulder` is not the same as sending `"Open"`.** For the two
  sided fields an omitted value publishes an open shoulder; for this one it publishes no shoulder
  description at all.

An incident whose shoulder has no side comes back like this:

```json
"leftShoulder": "None",
"rightShoulder": "None",
"unspecifiedShoulder": "Closed"
```

All three fields appear on the incident and on each entry in `locations[]`.

### Incident Details

- **description** - String - Brief incident description
- **comments** - String - Additional comments or notes
- **sourceName** - String - Name of the reporting source
- **confidenceLevel** - String - Event confidence level enum value
- **severity** - String - Event severity enum value
- **roadwayCondition** - String - Roadway condition enum value
- **weather** - String - Weather condition enum value
- **detectionType** - String - Detection type enum value
- **verificationType** - String - Verification type enum value

### Vehicle Counts

- **automobileCount** - Integer - Number of automobiles (0-8)
- **busCount** - Integer - Number of buses (0-8)
- **motorcycleCount** - Integer - Number of motorcycles (0-8)
- **pickupTruckCount** - Integer - Number of pickup trucks (0-8)
- **semiTrailerCount** - Integer - Number of semi-trailers (0-8)
- **tankerTruckCount** - Integer - Number of tanker trucks (0-8)
- **fatalityCount** - Integer - Number of fatalities (0-8)
- **injuryCount** - Integer - Number of injuries (0-8)

### Incident Features

- **accident** - Boolean - True if incident is an accident
- **fire** - Boolean - True if vehicle fire is present
- **hazmat** - Boolean - True if hazmat is involved
- **policeAction** - Boolean - True if police action is required
- **medicalEmergency** - Boolean - True if medical assistance is needed

### Time Fields

- **occurrenceTime** - ISO 8601 DateTime - When incident occurred
- **detectionTime** - ISO 8601 DateTime - When incident was detected
- **verificationTime** - ISO 8601 DateTime - When incident was verified
- **estimatedClosureTime** - String or Date - Either "hh:mm a", "MM/dd/yyyy hh:mm a" or ISO 8601 format
- **isDurationOption** - Boolean - True if using preset duration instead of specific time
- **durationMinutes** - Integer - Duration in minutes (15, 30, 60, 90, 120, 180, 240, 300, 360)

## Data Validation

- Location must be resolved with lane impacts OR userLaneCount must be specified
- Estimated closure time must be in valid format if not using duration option
- Vehicle counts must be between 0-8
- `unspecifiedShoulder` cannot be combined with `leftShoulder` or `rightShoulder` (see
  [Shoulders without a side](#shoulders-without-a-side))
- Required fields: sourceName, confidenceLevel, occurrenceTime, detectionTime, verificationTime
- With `locations`: every entry needs a `resolvedLocation` and lane impacts, a full closure or various lanes
  (only the first entry when `shareLaneInformation` is true). With `shareLaneInformation`, no shared lane may be
  numbered higher than another location's lane count. Errors name the entry, e.g. `locations[1].laneImpacts`.

## Error Handling

The API returns appropriate HTTP status codes:

- 200 OK - Request succeeded
- 400 Bad Request - Validation errors (returns errors object with field-specific messages)
- 404 Not Found - Incident not found
- 500 Internal Server Error - Server-side error (e.g., publication failure)

All error responses follow the standard format:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Error description"
  }
}
```

OR for validation errors:

```json
{
  "success": false,
  "errors": {
    "fieldName": "Field-specific error message"
  }
}
```

## Example Usage

### Creating an Incident

```console
# Step 1: Get dropdown data
curl -X GET \
  -H "Cookie: loggedIn=true" \
  https://travelmidwest.com/lmiga/admin/incidentEntry/dropdowns.json

# Step 2: Resolve location
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Cookie: loggedIn=true" \
  -d '{
    "locationDescription": "I-90 WB at Elgin"
  }' \
  https://travelmidwest.com/lmiga/admin/incidentEntry/resolve.json

# Step 3: Create incident
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Cookie: loggedIn=true" \
  -d '{
    "locationDescription": "I-90 WB at Elgin",
    "description": "Vehicle accident",
    "sourceName": "IDOT",
    "confidenceLevel": "HIGH_EVENT_CONFIDENCE_LEVEL",
    "automobileCount": 2,
    "accident": true,
    "occurrenceTime": "2025-10-14T09:45:00Z",
    "detectionTime": "2025-10-14T09:46:00Z",
    "verificationTime": "2025-10-14T09:47:00Z",
    "isDurationOption": true,
    "durationMinutes": 60,
    "laneImpacts": [
      {"laneNumber": 1, "impact": "Open"},
      {"laneNumber": 2, "impact": "Closed"},
      {"laneNumber": 3, "impact": "Open"}
    ],
    "leftShoulder": "Open",
    "rightShoulder": "Open",
    "laneType": "Lane"
  }' \
  https://travelmidwest.com/lmiga/admin/incidentEntry/create.json
```

### Creating a Closure in Both Directions

```console
# Step 1: Check that the Gateway supports more than one location
curl -X GET \
  -H "Cookie: loggedIn=true" \
  https://travelmidwest.com/lmiga/admin/incidentEntry/dropdowns.json
# ... "capabilities": ["multiLocation"]

# Step 2: Resolve the first direction, and keep data.locations[0].resolvedLocation
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Cookie: loggedIn=true" \
  -d '{"locationDescription": "EB IL-116 from IL-47 to IL-115"}' \
  https://travelmidwest.com/lmiga/admin/incidentEntry/resolve.json

# Step 3: Ask for the opposite direction, and keep its resolvedLocation too
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Cookie: loggedIn=true" \
  -d '{"resolvedLocation": <resolvedLocation from step 2>}' \
  https://travelmidwest.com/lmiga/admin/incidentEntry/resolve/opposite.json

# Step 4: Create the incident with both locations, sharing one full closure
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Cookie: loggedIn=true" \
  -d '{
    "locationDescription": "IL-116 from IL-47 to IL-115",
    "description": "Road closed",
    "sourceName": "IDOT",
    "severity": "MAJOR_EVENT_SEVERITY",
    "detectionType": "MANUAL_DETECTION_TYPE",
    "isDurationOption": true,
    "durationMinutes": 120,
    "shareLaneInformation": true,
    "locations": [
      {"resolvedLocation": <from step 2>, "fullClosure": true},
      {"resolvedLocation": <from step 3>}
    ]
  }' \
  https://travelmidwest.com/lmiga/admin/incidentEntry/create.json
```

### Updating an Incident

```console
curl -X PUT \
  -H "Content-Type: application/json" \
  -H "Cookie: loggedIn=true" \
  -d '{
    "locationDescription": "I-90 WB at Elgin",
    "description": "Vehicle accident - CLEARED",
    "sourceName": "IDOT",
    "laneImpacts": [
      {"laneNumber": 1, "impact": "Open"},
      {"laneNumber": 2, "impact": "Open"},
      {"laneNumber": 3, "impact": "Open"}
    ]
  }' \
  https://travelmidwest.com/lmiga/admin/incidentEntry/123/update.json
```

### Closing an Incident

```console
curl -X PUT \
  -H "Cookie: loggedIn=true" \
  https://travelmidwest.com/lmiga/admin/incidentEntry/123/close.json
```

## Notes

- All timestamp fields use ISO 8601 format (e.g., "2025-10-14T09:45:00Z")
- The loggedIn cookie is required for authentication
- User must have Operator role with "admin" or "incidentEntry" access
- All create, update, and close operations are automatically published to the Gateway
- Publication failures will return a 500 error with appropriate message
- Incidents are assigned unique external IDs based on source prefix and VMID
- Location resolution uses the LocationResolver service for validation
- Gateway users can see and manage incidents from all agencies
- Agency users can only see and manage incidents from their assigned agency
