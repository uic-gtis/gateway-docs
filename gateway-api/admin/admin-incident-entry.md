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
    "counts": [0, 1, 2, 3, 4, 5, 6, 7, 8]
  }
}
```

**Notes:**

- Gateway users see all event sources; a future update for agency users will provide them only their agency's sources
- Duration options range from 15 minutes to 6 hours

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
        ]
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
    "rightShoulder": "Open",
    "laneType": "Lane",
    "fullClosure": false,
    "variousLanes": false
  }
}
```

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
- occurrenceTime, detectionTime, and verificationTime can ***null*** if unknown

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
- **leftShoulder** - String - "Open", "Closed", or "None"
- **rightShoulder** - String - "Open", "Closed", or "None"
- **laneType** - String - "Lane", "Express", "HOV", "Reversible", "Local", "Cash", "IPO", or "ORT"
- **fullClosure** - Boolean - True if all lanes are closed
- **variousLanes** - Boolean - True for various lane impacts
- **userLaneCount** - Integer - Manual lane count for unresolved locations

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
- Required fields: sourceName, confidenceLevel, occurrenceTime, detectionTime, verificationTime

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
  https://travelmidwest.com/lmiga/admin/incidentEntry.json
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
  https://travelmidwest.com/lmiga/admin/incidentEntry/123.json
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
