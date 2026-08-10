# Admin announcements

> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.

## About

The /lmiga//admin/announcements end points provide REST APIs for managing announcements in the GCM Travel system. This controller allows administrators to view, create, update, and delete announcements as well as access announcement logs.

## Authentication

Authentication is required for all endpoints in the /admin path. The loggedIn cookie must be present in all requests. See [Authentication](../user-api/authentication.md) for more information.

## Base URL

All endpoints are accessible under the base URL:

```console
/lmiga/admin/announcements
```

### List Announcements

```console
GET /all.json
```

Retrieve a list of all announcements with optional filtering.

**Query Parameters:**

- type (optional) - Filter by announcement type (highPriority, construction, newsItem, siteNews, transit, or weather)
- state (optional) - Filter by state name (Regional, Illinois, Indiana, Michigan, Wisconsin, Iowa, Missouri, or Kentucky)
- agency (optional) - Filter by agency name
- roadway (optional) - Filter by roadway name

Example Response

```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "Road Work on I-94",
      "agency": "IDOT",
      "author": "Operator",
      "lastUpdate": "2025-03-15T10:00:00Z",
      "expirationDate": "2025-04-15T10:00:00Z",
      "roadway": "I-94",
      "state": "Illinois",
      "priority": "HIGH"
    },
    ...
  ]
}
```

### Get Announcement by ID

Retrieve a specific announcement by its ID.

```console
GET /{id}/announcement.json
```

**URL Parameters:**

- id - The ID of the announcement

### Get Announcement Logs

Retrieve the logs for a specific announcement.

```console
GET /{id}/logs.json
```

**URL Parameters:**

- id - The ID of the announcement

### Create Announcement

Create a new announcement.

```console
POST /announcement.json
```

**Content-Type:** application/json

**Request Body:**

```json
{
  "title": "Road Work on I-94",
  "html": "<p>Road work ongoing on I-94 northbound.</p>",
  "icon": "construction",
  "link": "https://example.com/more-info",
  "creationDate": "2025-03-15T10:00:00Z",
  "expirationDate": "2025-04-15T10:00:00Z",
  "lastUpdate": "2025-03-15T10:00:00Z",
  "author": "Joe User", 
  "agency": "IDOT",
  "roadway": "I-94",
  "state": "Illinois",
  "state2": null,
  "priority": "HIGH",
  "eventIds": ["1", "2"],
  "weatherDotGovId": null,
  "highPriorityPageOrder": 1,
  "highPriorityPage": "false",
  "newsItem": "true",
  "construction": "false",
  "transit": "false",
  "weather": "false",
  "trucker": "true"
}
```

**Response:**

- Status: 201 Created
- Body: The created announcement JSON wrapped in an object with "success" and "data"

**Example Creation**

```console
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Cookie: loggedIn=true" \
  -d '{
    "title": "Closure on I-90",
    "html": "<p>Full closure of I-90 westbound for bridge repair.</p>",
    "icon": "road-closure",
    "link": "https://example.com/i90-closure",
    "expirationDate": "2025-04-30T10:00:00Z",
    "agency": "IDOT",
    "roadway": "I-90",
    "state": "Illinois",
    "priority": "HIGH"
  }' \
  https://travelmidwest.com/lmiga/admin/announcements/announcement.json
```

### Update Announcement

Update an existing announcement.

```console
PUT /{id}/announcement.json
```

**Method:** PUT
**Content-Type:** application/json

**URL Parameters:**

- id - The ID of the announcement to update

**Request Body:**

```json
{
  "title": "Road Work on I-94",
  "html": "<p>Road work ongoing on I-94 northbound.</p>",
  "icon": "construction",
  "link": "https://example.com/more-info",
  "creationDate": "2025-03-15T10:00:00Z",
  "expirationDate": "2025-04-15T10:00:00Z",
  "lastUpdate": "2025-03-15T10:00:00Z",
  "author": "Joe User", 
  "agency": "IDOT",
  "roadway": "I-94",
  "state": "Illinois",
  "state2": null,
  "priority": "HIGH",
  "eventIds": ["1", "2"],
  "weatherDotGovId": null,
  "highPriorityPageOrder": 1,
  "highPriorityPage": "false",
  "newsItem": "true",
  "construction": "false",
  "transit": "false",
  "weather": "false",
  "trucker": "true"
}
```

**Response:**

- Status: 200 OK
- Body: The updated announcement JSON wrapped in an object with "success" and "data".

### Delete Announcement

Delete an announcement.

```console
DELETE /{id}/announcement.json
```

**Method:** DELETE
**Authentication:** Required

**URL Parameters:**

- id - The ID of the announcement to delete

**Response:**

```
{
  "success": true,
  "data": {
    "success": true,
    "message": "Announcement has been successfully deleted"
  }
}
```

### Get Operators

Retrieve a list of all operators who have made changes to announcements.

```console
GET /operators.json
```

### Get Roadways

Retrieve a list of all roadways that have announcements.

```console
GET /roadways.json
```

### Get States

Retrieve a list of all states.

```console
GET /states.json
```

### Get Agencies

Retrieve a list of all agencies.

```console
GET /agencies.json
```

### Get Priorities

Retrieve a list of all announcement priorities.

```console
GET /priorities.json
```

### Get Events

Retrieve a list of scheduled events that can be associates with an announcement.

```console
GET /events.json
```

Returns:

- id - Long - database id
- type - String - "RoadWork" or "SpecialEvent"
- externalId - String - id used on website and in operators' Map Editors
- location - String - impact and description of location of the event
- description - String - description of event as entered by operator or data source
- operator - String - comma separated list of names of humans or data sources that provided data
- active - boolean - "true" or "false" if event is currently active

```
{
  "success": true,
  "data": [
    {
      "id": 1,
      "type": "SpecialEvent",
      "externalId": "SE-2025-001",
      "location": "Downtown Chicago - Michigan Ave, Columbus Dr",
      "description": "Chicago Marathon",
      "operator": "CDOT",
      "active": true
    },
    {
      "id": 2,
      "type": "RoadWork",
      "externalId": "RW-2025-042",
      "location": "I-90 Westbound between exits 51-53",
      "description": "Lane closures for resurfacing work",
      "operator": "IDOT",
      "active": true
    }
  ]
}
```

### Get Links

Retrieve a list of existing distinct links in the database.

```json
GET /links.json
```

Returns:

- array of strings

```json
{
  "success": true,
  "data": [
    "https://www.ctatransit.org",
    "https://rtachicago.org",
    "https://illinois.gov/construction/allRoadWork.html",
    "https://www.wisdot.gov/allroads/transitProviders/all.html"
  ]
}
```

### Reorder High Priority Announcements

Reorder high priority page announcements by updating their display order.

```console
POST /reorder.json
```

**Method:** POST
**Content-Type:** application/json
**Authentication:** Required

**Request Body:**

```json
{
  "ids": [123, 456, 789]
}
```

The `ids` array contains announcement IDs in the desired display order. The first ID in the array will be assigned order position 0, the second will be position 1, and so on.

**Response:**

> [!WARNING]
> An older version of the API returned two "success" fields.  The data.success field was redundant and was removed.

Success response when all announcements are reordered:

```json
{
  "success": true,
  "data": {
    "updatedCount": 3,
    "updatedIds": [123, 456, 789],
    "message": "Successfully reordered 3 announcements"
  }
}
```

Partial success response when some announcements could not be reordered:

```json
{
  "success": true,
  "data": {
    "updatedCount": 2,
    "updatedIds": [123, 789],
    "errors": [
      "Announcement with ID 456 is not a high priority page announcement"
    ],
    "message": "Partially reordered announcements with some errors"
  }
}
```

Error response when no announcements could be reordered:

```json
{
  "success": false,
  "error": {
    "code": "REORDER_FAILED",
    "message": "Failed to reorder announcements"
  }
}
```

**Validation Rules:**

- The `ids` array must not be null or empty
- Only announcements marked as high priority page announcements (`highPriorityPage: true`) can be reordered
- Non-existent announcement IDs will be skipped with an error message
- The authenticated user must have operator privileges

**Example:**

```console
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Cookie: loggedIn=true" \
  -d '{
    "ids": [45, 23, 67, 12]
  }' \
  https://travelmidwest.com/lmiga/admin/announcements/reorder.json
```

This endpoint replaces the functionality of the legacy `/orderAnnouncements.jsp` page, providing a REST API suitable for React-based admin interfaces. Each successfully reordered announcement will have its `highPriorityPageOrder` field updated and a corresponding audit log entry created.

## Data Validation

- Announcement state field must be specified (state2 can be null or empty)
- Announcement titles cannot be empty
- Announcement html cannot be empty
- Announcement icon required when a link is provided
- Expiration dates must be after creation dates
- Invalid parameters will result in appropriate error responses
- Minimum one category required - At least one of the following must be checked: newsItem, siteNews, construction, transit, weather, or trucker
- Category exclusivity - Only one of the following can be checked: siteNews, construction, transit, or weather

## Error Handling

The API returns appropriate HTTP status codes:

- 200 OK - Request succeeded
- 201 Created - Resource successfully created
- 204 No Content - Resource successfully deleted
- 400 Bad Request - Invalid request (e.g., validation errors)
- 404 Not Found - Resource not found
- 500 Internal Server Error - Server-side error

## Notes

- All timestamp fields are returned in ISO 8601 format
- The loggedIn cookie is required for authentication
- The controller logs all actions (create, update, delete) for audit purposes
