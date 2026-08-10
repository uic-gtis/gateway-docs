# Admin my routes users

> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.

## About

This page documents the API endpoints for managing My Routes (Trip Alerts) users in the Travel Midwest system.

## Base URL

```console
https://travelmidwest.com/lmiga/admin/users/trip
```

## Authentication

All API endpoints require administrative privileges. You must have:

- Admin login credentials
- A valid `loggedIn` authentication cookie

## API Endpoints

### List All Trip Users

#### Request

Retrieves a list of all trip alerts users in a simplified format:

URL: `/all.json`
Method: `GET`
Full Path: `https://travelmidwest.com/lmiga/admin/users/trip/all.json`

#### Response

Returns a JSON array of Trip User summaries with the following structure:

```json
[
  {
    "id": 123,
    "email": "user@example.com",
    "format": "HTML",
    "suspendPeriod": {
      "start": "2025-12-20T00:00:00.000Z",
      "end": "2026-01-02T00:00:00.000Z"
    },
    "trips": ["I-90 EB: O'Hare to Downtown", "I-290 WB: UIC to Hillside"],
    "created": "2025-03-15T14:30:00.000Z",
    "updated": "2025-06-01T09:00:00.000Z",
    "verified": true,
    "bouncing": false
  }
]
```

#### Field Descriptions

| Field | Type | Description |
| --- | --- | --- |
| id | Long | The database ID of the trip user |
| email | String | The user's email address (also used as login) |
| format | String | Email alert format preference: `HTML` or `TEXT` |
| suspendPeriod | Object or null | Date range during which alerts are suspended (e.g., vacation). Null if no suspension is active |
| suspendPeriod.start | Date | Start of the suspension period |
| suspendPeriod.end | Date | End of the suspension period |
| trips | String[] | List of trip route descriptions the user has configured alerts for |
| created | Date | When the user account was created |
| updated | Date | When the user account was last updated |
| verified | Boolean | Whether the user has verified their email address |
| bouncing | Boolean | Whether the user's email address is bouncing (undeliverable) |

### Become User (Masquerade)

#### Request

Allows an admin to log in as a specific trip user to view and troubleshoot their account. This clears the admin session and creates a new session as the specified trip user.

URL: `/{id}/becomeUser.json`
Method: `GET`
Full Path: `https://travelmidwest.com/lmiga/admin/users/trip/{id}/becomeUser.json`

Path Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| id | Long | The database ID of the trip user to masquerade as |

**Important:** This endpoint clears your admin session. After calling this endpoint, you will be logged in as the specified trip user and will no longer have admin access. You will need to log in again with admin credentials to regain admin access.

#### Response (Success)

Returns a JSON object confirming the session switch:

```json
{
  "status": "success",
  "message": "Logged in as user 123"
}
```

#### Response (Error)

Common error responses:

| HTTP Status | Error | Description |
| --- | --- | --- |
| 404 | Not Found | No trip user exists with the specified ID |

## Examples

### Fetching All Alerts Users

Request:

```console
GET https://travelmidwest.com/lmiga/admin/users/trip/all.json
```

### Masquerading as an Alerts User

Request:

```console
GET https://travelmidwest.com/lmiga/admin/users/trip/123/becomeUser.json
```

After a successful response, navigate to the Trip Map page to view the user's saved routes and alert settings as if you were that user.
