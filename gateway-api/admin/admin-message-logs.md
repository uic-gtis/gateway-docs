# Admin message logs

> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.

## About

This document provides documentation for the Message Logs Admin API endpoints, which allow administrators to retrieve and filter message logs.

## Base URL

All endpoints are accessible under:

```console
/lmiga/admin/messagelogs
```

## Authentication

Authentication is required for all admin endpoints. The API uses cookie-based authentication:

- A valid loggedIn cookie must be included with all requests
- If the cookie is missing or invalid, the server will respond with a 401 Unauthorized status

## Available Endpoints

### Get All Operators

```console
/operators.json
```

Retrieves a list of all distinct operators who have created or modified messages.

- **URL**: `/lmiga/admin/messagelogs/operators.json`
- **Method**: GET
- **Response**: JSON array of operator usernames

#### Example Request

```javascript
// Using Fetch API 
fetch('/lmiga/admin/messagelogs/operators.json', { 
  method: 'GET', 
  credentials: 'include' // Important: required to send cookies 
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

#### Example Response

```json
["admin", "john.doe", "jane.smith", "operator1"]
```

### Get All Priorities

```console
/priorities.json
```

Retrieves all available message priority levels.

- **URL**: /lmiga/admin/messagelogs/priorties.json
- **Method**: GET
- **Response**: JSON array of priority level names

#### Example Request

```javascript
fetch('/lmiga/admin/messagelogs/priorties.json', { 
  method: 'GET', 
  credentials: 'include' })
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

#### Example Response

```json
["OUTAGE", "ALERT", "HIGH", "MEDIUM", "LOW"]
```

### Search Message Logs

Searches and retrieves message logs based on multiple filter criteria.

- **URL**: /lmiga/admin/messagelogs/logs.json
- **Method**: POST
- **Content-Type**: application/json
- **Request Body**: JSON object containing filter parameters
- **Query Parameters**:
  - page: Zero-based page index (default: 0)
  - size: Number of items per page (default: 20)
  - sort: Sort field and direction, e.g., updateDate,desc
- **Response**: Paginated JSON response of matching message logs

#### Filter Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| text | string | Filter logs containing this text (case-insensitive) |
| operator | string | Filter logs by operator username (case-insensitive) |
| priority | string | Filter logs by priority level (e.g., "HIGH", "MEDIUM") |
| startDate | date | Filter logs on or after this date |
| endDate | date | Filter logs on or before this date |
| id | number | Filter logs by specific message ID |

#### Example Request

```javascript
const filter = {
  text: "important message",
  operator: "admin",
  priority: "HIGH",
  startDate: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString(), // 30 days ago
  endDate: new Date().toISOString(),
  id: null
};

fetch('/lmiga/admin/messagelogs/logs.json?page=0&size=10&sort=updateDate,desc', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  credentials: 'include',
  body: JSON.stringify(filter)
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

#### Example Response

```json
{
  "content": [
    {
      "messageId": 123,
      "text": "Important system maintenance scheduled",
      "startDate": "2025-03-20T08:00:00",
      "expirationDate": "2025-03-25T20:00:00",
      "amberAlert": false,
      "priority": "HIGH",
      "userName": "admin",
      "updateDate": "2025-03-15T14:22:15",
      "updateType": "UPDATE"
    },
    {
      "messageId": 121,
      "text": "Important network update completed",
      "startDate": "2025-03-10T12:00:00",
      "expirationDate": "2025-03-15T23:59:59",
      "amberAlert": false,
      "priority": "HIGH",
      "userName": "admin",
      "updateDate": "2025-03-10T17:30:45",
      "updateType": "CREATE"
    }
  ],
  "pageable": {
    "sort": {
      "sorted": true,
      "unsorted": false,
      "empty": false
    },
    "pageNumber": 0,
    "pageSize": 10,
    "offset": 0,
    "paged": true,
    "unpaged": false
  },
  "totalPages": 1,
  "totalElements": 2,
  "last": true,
  "first": true,
  "size": 10,
  "number": 0,
  "sort": {
    "sorted": true,
    "unsorted": false,
    "empty": false
  },
  "numberOfElements": 2,
  "empty": false
}
```
