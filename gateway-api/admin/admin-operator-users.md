# Admin operator users

> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.

## About

The Operator Management API provides endpoints for administrators to manage operator accounts in the TravelMidwest system. These endpoints allow for creating, retrieving, updating, and deleting operator accounts, as well as retrieving related information such as roles and agencies.

## Authentication

All API endpoints require authentication with an account that has administrative privileges. Authentication is handled through a session cookie that is set after a successful login.

- **Login URL**: `https://travelmidwest.com/lmiga/user/login.json`
- **Required Role**: Admin role access is required for all endpoints

## Base URL

```
 https://travelmidwest.com/lmiga/admin/users/operator/
```

## Response Format

All responses are in JSON format and follow a consistent structure:

For successful responses:

```json
{
  "success": true,
  "data": { ... },
  "error": null
}
```

For error responses:

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "ERROR_CODE",
    "message": "Error message",
    "fieldErrors": { ... }  Optional field validation errors
  }
}
```

## Endpoints

### List All Operators

Retrieves a list of all operator accounts in the system.

- **URL**: `all.json`
- **Method**: `GET`
- **Full URL**: `[https://travelmidwest.com/lmiga/admin/users/operator/all.json](https://travelmidwest.com/lmiga/admin/users/operator/all.json)`

#### Response

**Success Response (200 OK)**

```json
{
  "success": true,
  "data": [
    {
      "id": 123,
      "login": "operator1",
      "name": "John Doe",
      "organization": "IDOT",
      "email": "john.doe@example.com",
      "agencyName": "Illinois Department of Transportation",
      "roles": ["admin", "operator"],
      "approved": "2025-04-01T10:30:00.000Z",
      "updated": "2025-04-10T15:45:00.000Z"
    },
 more operators...
  ],
  "error": null
}
```

### Get Operator Details

Retrieves detailed information about a specific operator account.

- **URL**: `/{id}/user.json`
- **Method**: `GET`
- **Full URL Example**: `[https://travelmidwest.com/lmiga/admin/users/operator/123/user.json](https://travelmidwest.com/lmiga/admin/users/operator/123/user.json)`

#### URL Parameters

| Parameter | Description |
| --- | --- |
| id | The database ID of the operator to retrieve |

#### Response

**Success Response (200 OK)**

```json
{
  "success": true,
  "data": {
    "id": 123,
    "login": "operator1",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "company": "IDOT",
    "phoneNumber": "312-555-1234",
    "jobTitle": "Traffic Systems Manager",
    "faxNumber": "312-555-5678",
    "approved": "2025-04-01T10:30:00.000Z",
    "updated": "2025-04-10T15:45:00.000Z",
    "neverExpires": true,
    "roles": ["admin", "operator"],
    "agencyId": 5,
    "agencyName": "Illinois Department of Transportation"
  },
  "error": null
}
```

**Error Response (404 Not Found)**

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "User not found",
    "message": "No user exists with ID 123"
  }
}
```

**Error Response (400 Bad Request)**

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "Invalid user type",
    "message": "User with ID 123 is not an Operator"
  }
}
```

### Create Operator

Creates a new operator account.

- **URL**: `create.json`
- **Method**: `POST`
- **Full URL**: `[https://travelmidwest.com/lmiga/admin/users/operator/create.json](https://travelmidwest.com/lmiga/admin/users/operator/create.json)`
- **Content-Type**: `application/json`

#### Request Body

```json
{
  "login": "newoperator",
  "password": "SecureP@ssword123",
  "name": "Jane Smith",
  "email": "jane.smith@example.com",
  "company": "CDOT",
  "phoneNumber": "312-555-9876",
  "jobTitle": "Systems Administrator",
  "faxNumber": "312-555-4321",
  "neverExpires": false,
  "roles": ["operator"],
  "agencyId": 6
}
```

#### Response

**Success Response (200 OK)**

```json
{
  "success": true,
  "data": {
    "id": 456,
    "login": "newoperator",
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "company": "CDOT",
    "phoneNumber": "312-555-9876",
    "jobTitle": "Systems Administrator",
    "faxNumber": "312-555-4321",
    "approved": "2025-05-13T14:30:00.000Z",
    "updated": "2025-05-13T14:30:00.000Z",
    "neverExpires": false,
    "roles": ["operator"],
    "agencyId": 6,
    "agencyName": "Chicago Department of Transportation"
  },
  "error": null
}
```

**Error Response (400 Bad Request) - Login Exists**

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "LOGIN_EXISTS",
    "message": "A user with the login 'newoperator' already exists"
  }
}
```

**Error Response (400 Bad Request) - Password Validation**

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation error",
    "fieldErrors": {
      "password": "Password does not meet security requirements: must be at least 10 characters, must contain at least one number, must contain at least one special character"
    }
  }
}
```

### Update Operator

Updates an existing operator account.

- **URL**: `/{id}/user.json`
- **Method**: `POST`
- **Full URL Example**: `[https://travelmidwest.com/lmiga/admin/users/operator/123/user.json](https://travelmidwest.com/lmiga/admin/users/operator/123/user.json)`
- **Content-Type**: `application/json`

#### URL Parameters

| Parameter | Description |
| --- | --- |
| id | The database ID of the operator to update |

#### Request Body

```json
{
  "login": "operator1",
  "password": "",  Leave empty to keep the current password
  "name": "John Doe",
  "email": "john.doe.updated@example.com",
  "company": "IDOT",
  "phoneNumber": "312-555-1234",
  "jobTitle": "Senior Traffic Systems Manager",
  "faxNumber": "312-555-5678",
  "neverExpires": true,
  "roles": ["admin", "operator", "reporter"],
  "agencyId": 5,
  "approved": "2025-04-01T10:30:00.000Z"
}
```

#### Response

**Success Response (200 OK)**

```json
{
  "success": true,
  "data": {
    "id": 123,
    "login": "operator1",
    "name": "John Doe",
    "email": "john.doe.updated@example.com",
    "company": "IDOT",
    "phoneNumber": "312-555-1234",
    "jobTitle": "Senior Traffic Systems Manager",
    "faxNumber": "312-555-5678",
    "approved": "2025-04-01T10:30:00.000Z",
    "updated": "2025-05-13T15:00:00.000Z",
    "neverExpires": true,
    "roles": ["admin", "operator", "reporter"],
    "agencyId": 5,
    "agencyName": "Illinois Department of Transportation"
  },
  "error": null
}
```

**Error Responses**: Same as "Get Operator Details" with additional password validation errors as in "Create Operator"

### Delete Operator

Deletes an operator account.

- **URL**: `/{id}/user.json`
- **Method**: `DELETE`
- **Full URL Example**: `[https://travelmidwest.com/lmiga/admin/users/operator/123/user.json](https://travelmidwest.com/lmiga/admin/users/operator/123/user.json)`

#### URL Parameters

| Parameter | Description |
| --- | --- |
| id | The database ID of the operator to delete |

#### Response

**Success Response (200 OK)**

```json
{
  "success": true,
  "data": {
    "success": true,
    "message": "Operator account 123 has been successfully deleted"
  },
  "error": null
}
```

**Error Responses**: Same as "Get Operator Details"

### Get Roles

Retrieves a list of all available roles that can be assigned to operators.

- **URL**: `roles.json`
- **Method**: `GET`
- **Full URL**: `[https://travelmidwest.com/lmiga/admin/users/operator/roles.json](https://travelmidwest.com/lmiga/admin/users/operator/roles.json)`

#### Response

**Success Response (200 OK)**

```json
{
  "success": true,
  "data": [
    {
      "name": "admin",
      "description": "Administrator with full system access"
    },
    {
      "name": "operator",
      "description": "Standard operator with access to operational functions"
    },
    {
      "name": "reporter",
      "description": "Can generate and view reports"
    }
 more roles...
  ],
  "error": null
}
```

### Get Agencies

Retrieves a list of all available agencies that can be assigned to operators.

- **URL**: `agencies.json`
- **Method**: `GET`
- **Full URL**: `[https://travelmidwest.com/lmiga/admin/users/operator/agencies.json](https://travelmidwest.com/lmiga/admin/users/operator/agencies.json)`

#### Response

**Success Response (200 OK)**

```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Gary Chicago International Airport"
    },
    {
      "id": 5,
      "name": "Illinois Department of Transportation"
    },
    {
      "id": 6,
      "name": "Chicago Department of Transportation"
    }
 more agencies...
  ],
  "error": null
}
```

## Error Codes

| Error Code | Description |
| --- | --- |
| User not found | The requested user ID does not exist |
| Invalid user type | The user exists but is not an Operator |
| LOGIN_EXISTS | The login name is already taken by another user |
| PASSWORD_REQUIRED | A password is required when creating a new operator |
| INVALID_PASSWORD | The password does not meet security requirements |
| VALIDATION_ERROR | General validation error, see fieldErrors for details |
| INVALID_AGENCY | The specified agency does not exist |
| UNAUTHORIZED | Authentication is required to access this resource |
| FORBIDDEN | The authenticated user lacks permission for this action |
| SERVER_ERROR | An unexpected error occurred on the server |

## Implementation Notes

- All date fields are returned in ISO 8601 format (UTC).
- The password field is never returned in responses.
- When updating an operator, fields not included in the request body will retain their current values.
- To change a password, include the new password in the update request. To keep the current password, omit the password field or provide an empty string.
- The `approved` field can be set to grant immediate approval to an operator account.
