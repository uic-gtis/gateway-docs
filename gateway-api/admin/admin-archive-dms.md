# Admin archive DMS

> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.

## About

This document provides details on the DMS (Dynamic Message Sign) Archive admin API endpoints for integration with the React front-end application.

The DMS Archive API serves as a proxy to the internal DMS archive service, providing access to historical Dynamic Message Sign location and message data. The API handles timeouts and error responses from the archive service and returns standardized API responses.

## Authentication Requirements

⚠️ **IMPORTANT**: All API endpoints require admin authentication. The application uses cookies for authentication after login. Ensure your requests include credentials to send cookies with cross-origin requests.

## Base URL

```console
/admin/archive/dms
```

## Available Endpoints

### Get DMS Locations

Retrieves all DMS locations from the archive service.

```console
GET /locations.json
```

**Query Parameters:**

- None

**Response:** (Status Code: 200 OK)

```json
{
  "success": true,
  "data": [
    {
      "id": "DMS-001",
      "name": "I-90 at Mile 45",
      "latitude": 41.85003,
      "longitude": -87.65005,
      "route": "I-90",
      "direction": "Eastbound"
    },
    {
      "id": "DMS-002",
      "name": "I-94 at Junction 12",
      "latitude": 41.87894,
      "longitude": -87.63589,
      "route": "I-94",
      "direction": "Westbound"
    }
  ]
}
```

**Error Responses:**

- 500 Internal Server Error: If unable to connect to archive service
- Other status codes: Forwarded from archive service

**Notes:**

- This endpoint proxies requests to the internal archive service
- Connection timeout is set to 10 seconds
- Returns data in standardized API response format

### Get DMS Text Data

Retrieves DMS text message data from the archive service based on query parameters.

```console
GET /text.json?[queryParameters]
```

**Query Parameters:**

- All query parameters are forwarded to the archive service
- Typical parameters may include:
- dmsId (string): DMS location identifier
- startDate (ISO 8601): Start date for message retrieval
- endDate (ISO 8601): End date for message retrieval

**Response:** (Status Code: 200 OK)

```json
{
  "success": true,
  "data": [
    {
      "dmsId": "DMS-001",
      "timestamp": "2025-03-25T14:30:00.000Z",
      "messageText": "ACCIDENT AHEAD - USE CAUTION",
      "operator": "IDOT"
    },
    {
      "dmsId": "DMS-001",
      "timestamp": "2025-03-25T15:45:00.000Z",
      "messageText": "ACCIDENT CLEARED - NORMAL TRAFFIC",
      "operator": "IDOT"
    }
  ]
}
```

**Error Responses:**

- 500 Internal Server Error: If unable to connect to archive service
- Other status codes: Forwarded from archive service

**Notes:**

- This endpoint proxies requests to the internal archive service
- Query parameters are passed through to the archive service
- Connection timeout is set to 10 seconds
- Returns data in standardized API response format

## Data Types

### Date Format

All date fields follow the ISO 8601 standard (UTC):

- Example: "2025-03-25T14:30:00.000Z"

## Example Usage with React

```javascript
// Example: Fetching DMS locations
const fetchDmsLocations = async () => {
  try {
    const response = await fetch('https://travelmidwest.com/admin/archive/dms/locations.json', {
      credentials: 'include', // Important: includes cookies with the request
    });
    if (!response.ok) {
      throw new Error('Failed to fetch DMS locations');
    }
    const result = await response.json();
    if (result.success) {
      setLocations(result.data);
    }
  } catch (error) {
    console.error('Error fetching DMS locations:', error);
  }
};

// Example: Fetching DMS text data with query parameters
const fetchDmsText = async (dmsId, startDate, endDate) => {
  try {
    const params = new URLSearchParams({
      dmsId: dmsId,
      startDate: startDate,
      endDate: endDate
    });
    
    const response = await fetch(`https://travelmidwest.com/admin/archive/dms/text.json?${params}`, {
      credentials: 'include', // Important: includes cookies with the request
    });
    
    if (!response.ok) {
      throw new Error('Failed to fetch DMS text data');
    }
    
    const result = await response.json();
    if (result.success) {
      setDmsMessages(result.data);
    }
  } catch (error) {
    console.error('Error fetching DMS text:', error);
  }
};
```

## Technical Details

### Archive Service

- Internal archive service URL: `http://archive.tsc.travelmidwest.com:8080/`
- Connection timeout: 10 seconds
- Socket timeout: 10 seconds

### Response Format

All responses follow the standardized API response format:

```json
{
  "success": true/false,
  "data": { /* response data */ },
  "error": { /* error details if success is false */ }
}
```

## Contact

For any questions or issues related to this API, please contact [dev@travelmidwest.com](mailto:dev@travelmidwest.com?subject=DMS%20Archive%20Admin%20API%20Documentation).
