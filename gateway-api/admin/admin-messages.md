# Admin messages

> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.

## About

This document provides details on the Message of the Day (MOTD) admin API endpoints for integration with the React front-end application.

## Authentication Requirements

⚠️ **IMPORTANT**: All API endpoints require admin authentication. The application uses cookies for authentication after login. Ensure your requests include credentials to send cookies with cross-origin requests.

## Base URL

All API endpoints are relative to:

```console
/lmiga/admin/messages
```

## Available Endpoints

### Get All Messages

```console
/all.json[?activeOnly=true/false][&includeIncidentMessages=true/false]
```

**Query Parameters:**

- activeOnly (boolean, optional): When true, returns only active messages (not expired)
- includeIncidentMessages (boolean, optional): When true, includes messages generated from incidents

**Response:**

**Notes:**

- Messages are sorted by priority and then by expiration date
- Default values if parameters are not provided: activeOnly=false, includeIncidentMessages=false

### Create New Message

Creates a new message of the day and logs the creation in the message log.

```console
POST /motd.json
```

**Request Body:**

```json
{ 
  "text": "Heavy traffic expected downtown this weekend", 
  "startDate": "2025-03-25T00:00:00.000Z", 
  "expirationDate": "2025-03-27T23:59:59.000Z", 
  "amberAlert": false, 
  "priority": "HIGH", 
  "metroAreaId": 5, 
  "latitude": 41.85003, 
  "longitude": -87.65005 
}
```

**Response:** (Status Code: 201 Created)

```json
{ 
  "id": 124, 
  "text": "Heavy traffic expected downtown this weekend",
  "creationDate": "2025-03-25T10:15:30.000Z", 
  "startDate": "2025-03-25T00:00:00.000Z", 
  "expirationDate": "2025-03-27T23:59:59.000Z", 
  "amberAlert": false, 
  "priority": "HIGH", 
  "lastUpdate": "2025-03-25T10:15:30.000Z", 
  "incidentId": null, 
  "tripReportTableId": null, 
  "metroAreaId": 5, 
  "latitude": 41.85003, 
  "longitude": -87.65005 
}
```

**Notes:**

- Do not include an id field when creating a new message
- Current date/time will be used for creationDate and lastUpdate if not provided
- priority defaults to MEDIUM if not provided

### Update Existing Message

Updates an existing method given its database identifier and logs the update in the message log.

```console
PUT /lmiga/admin/messages/{id}/motd.json
```

**URL Parameters:**

- id (number, required): ID of the message to update

**Request Body:**

```json
{ 
  "text": "Updated message text", 
  "startDate": "2025-03-25T00:00:00.000Z", 
  "expirationDate": "2025-03-30T23:59:59.000Z", 
  "amberAlert": false, 
  "priority": "LOW", 
  "metroAreaId": 5, 
  "latitude": 41.85003, 
  "longitude": -87.65005 
}
```

**Response:** (Status Code: 200 OK)

```json
{  
  "id": 124, 
  "text": "Updated message text", 
  "creationDate": "2025-03-25T10:15:30.000Z", 
  "startDate": "2025-03-25T00:00:00.000Z", 
  "expirationDate": "2025-03-30T23:59:59.000Z", 
  "amberAlert": false, 
  "priority": "LOW", 
  "lastUpdate": "2025-03-25T11:45:22.000Z", 
  "incidentId": null, 
  "tripReportTableId": null, 
  "metroAreaId": 5, 
  "latitude": 41.85003, 
  "longitude": -87.65005 
}
```

**Error Responses:**

- 404 Not Found: If message with specified ID doesn't exist

### Delete Message

Deletes and logs the deletion in the message log.

```console
DELETE /lmiga/admin/messages/{id}/motd.json
```

**URL Parameters:**

- id (number, required): ID of the message to delete

**Response:** (Status Code: 204 No Content)

**Error Responses:**

- 404 Not Found: If message with specified ID doesn't exist

### Get Incidents

```console
/incidents.json
```

**Response: **(Status Code: 200 OK)

```json
[
  {
    "id": 144115188700530020,
    "location": "Partial closure EB Page Blvd at Whittier St, St Louis, St Louis (City), MO",
    "description": "Expect delays due to SIGNAL ISSUE on Route D Eastbound.",
    "operator": "MoDOT"
  },
  {
    "id": 144115188700530020,
    "location": "Partial closure WB Page Blvd at Whittier St, St Louis, St Louis (City), MO",
    "description": "Expect delays due to SIGNAL ISSUE on Route D Westbound.",
    "operator": "MoDOT"
  }
]
```

### Get Metro Areas

```console
/metroAreas.json
```

**Response: **(Status Code: 200 OK)

```json
[
  {
    "id": 1,
    "name": "Chicago",
    "mapName": "chicagoArea"
  },
  {
    "id": 2,
    "name": "Peoria",
    "mapName": "peoria"
  },
  {
    "id": 5,
    "name": "NW Indiana",
    "mapName": "gary"
  },
  {
    "id": 8,
    "name": "Madison",
    "mapName": "madison"
  },
  {
    "id": 9,
    "name": "Milwaukee",
    "mapName": "milwaukee"
  },
  {
    "id": 4,
    "name": "St. Louis",
    "mapName": "stLouis"
  },
  {
    "id": 16,
    "name": "Indianapolis",
    "mapName": "indianapolis"
  }
]
```

### Get Priority Levels

```console
/priorities.json
```

**Response: **(Status Code: 200 OK)

```json
["OUTAGE","ALERT","HIGH","MEDIUM","LOW"]
```

## Data Types

### Message Priority

The priority field can have one of the following values:

- HIGH
- MEDIUM
- LOW

### Date Format

All date fields follow the ISO 8601 standard (UTC):

- Example: "2025-03-25T14:30:00.000Z"

## Example Usage with React

```javascript
// Example: Fetching active messages 
const fetchActiveMessages = async () => { 
  try { 
    const response = await fetch('https://travelmidwest.com/lmiga/admin/messages/all.json?activeOnly=true&includeIncidentMessages=true', { 
      credentials: 'include', // Important: includes cookies with the request 
    }); 
    if (!response.ok) { 
      throw new Error('Failed to fetch messages'); 
    } 
    const messages = await response.json(); 
    setMessages(messages); 
  } catch (error) { 
    console.error('Error fetching messages:', error); 
  } 
}; 
// Example: Creating a new message 
const createMessage = async (messageData) => { 
  try { 
    const response = await fetch('https://travelmidwest.com/lmiga/admin/messages/motd.json', { 
      method: 'POST', 
      headers: { 
        'Content-Type': 'application/json', 
      }, 
      credentials: 'include', // Important: includes cookies with the request body: 
      JSON.stringify(messageData) 
    }); 
    if (!response.ok) { 
      throw new Error('Failed to create message'); 
    } 
    const createdMessage = await response.json(); // Handle successful creation 
    return createdMessage; 
  } catch (error) { 
    console.error('Error creating message:', error); 
    throw error; 
  } 
};
```

## Contact

For any questions or issues related to this API, please contact [dev@travelmidwest.com](mailto:dev@travelmidwest.com?subject=Message%20of%20the%20Day%20Admin%20API%20Documentation).
