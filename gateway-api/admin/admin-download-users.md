# Admin download users

> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.

## About

This page documents the API endpoints exposed by the `AdminDownloadUsersJsonController` for managing Download Users in the Travel Midwest system.

## Base URL

All API endpoints are accessible at:

```console
https://travelmidwest.com/lmiga/admin/users/download
```

## Authentication

All API endpoints require administrative privileges. You must have:

- Admin login credentials
- A valid `loggedIn` authentication cookie

## API Endpoints

### List All Download Users

#### Request

Retrieves a list of all download users in a simplified format:

URL: `/all.json`
Method: `GET`
Full Path: `https://travelmidwest.com/lmiga/admin/users/download/all.json`

#### Response

Returns a JSON array of Download User summaries with the following structure:

```json
[
  {
    "id": 123,
    "login": "username",
    "name": "Full Name",
    "organization": "Company Name",
    "email": "user@example.com",
    "roles": ["role1", "role2"],
    "agreementSent": "2025-03-15T14:30:00.000Z",
    "agreementReceived": "2025-03-16T10:15:00.000Z",
    "approved": "2025-03-17T09:45:00.000Z",
    "rejected": null,
    "updated": "2025-03-17T09:45:00.000Z" 
  }
]
```

### Get Download User Details

#### Request

Retrieves detailed information about a specific download user:

URL: `/{id}/user.json`
Method: `GET`
Full Path: `https://travelmidwest.com/lmiga/admin/users/download/{id}/user.json`

Path Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| id | Long | The database ID of the download user |

#### Response (Success)

Returns a JSON object with the following structure:

```json
{
  "id": 123,
  "login": "username",
  "name": "Full Name",
  "email": "user@example.com",
  "company": "Company Name",
  "phoneNumber": "555-123-4567",
  "jobTitle": "Traffic Analyst",
  "address": {
    "street": "123 Main St",
    "city": "Chicago",
    "state": "IL",
    "zip": "60601"
  },
  "faxNumber": "555-123-4568",
  "approved": "2025-03-17T09:45:00.000Z", 
  "updated": "2025-03-17T09:45:00.000Z",
  "neverExpires": false,
  "roles": ["downloaduser", "xmluser"],
  "rejected": null, 
  "agreementSent": "2025-03-15T14:30:00.000Z",
  "agreementReceived": "2025-03-16T10:15:00.000Z",
  "warningSent": null,
  "needsAgreement": false,
  "requestLink": true,
  "requestXml": true,
  "ipAddress": "192.168.1.1",
  "intendedUsage": "Traffic monitoring for research",
  "intendedLocation": "Chicago metropolitan area",
  "revenue": false,
  "businessPartners": [
    {
      "id": 456,
      "name": "Partner Name",
      "company": "Partner Company",
      "phone": "555-987-6543",
      "email": "partner@example.com",
      "purpose": "Data sharing for regional traffic analysis"
    }
  ]
}
```

#### Response (Error)

In case of errors, the response will have the following structure:

```json
{
  "error": "Error type",
  "message": "Detailed error message"
}
```

Common error responses:

| HTTP Status | Error | Description |
| --- | --- | --- |
| 404 | User not found | No user exists with the specified ID |
| 400 | Invalid user type | The user with the specified ID is not a Download User |
| 500 | Retrieval failed | An internal server error occurred |

### Update Download User

#### Request

Updates a download user's information and settings:

URL: `/{id}/user.json`
Method: `POST`
Full Path: `https://travelmidwest.com/lmiga/admin/users/download/{id}/user.json`

Path Parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| id | Long | The database ID of the download user |

#### Request Body

The request body should be a JSON object with the following structure:

```json
{
  "login": "username",
  "password": "newPassword",
  "name": "Full Name",
  "email": "user@example.com",
  "company": "Company Name",
  "phoneNumber": "555-123-4567",
  "jobTitle": "Traffic Analyst",
  "address": {  
    "street": "123 Main St",
    "city": "Chicago",
    "state": "IL",
    "zip": "60601"
  },
  "faxNumber": "555-123-4568",
  "approved": "2025-03-17T09:45:00.000Z",
  "neverExpires": false,
  "roles": ["xmluser"],
  "rejected": null,
  "agreementSent": "2025-03-15T14:30:00.000Z",
  "agreementReceived": "2025-03-16T10:15:00.000Z",
  "warningSent": null,
  "requestLink": true,
  "requestXml": true,
  "ipAddress": "192.168.1.1",
  "intendedUsage": "Traffic monitoring for research",
  "intendedLocation": "Chicago metropolitan area",
  "revenue": false,
  "businessPartners": [
    {
      "id": 456,
      "name": "Partner Name",
      "company": "Partner Company",
      "phone": "555-987-6543",
      "email": "partner@example.com",
      "purpose": "Data sharing for regional traffic analysis"
    }
  ]
}
```

Note: The `password` field is optional and should only be included when changing the user's password.

#### Response (Success)

Returns the updated download user object with the same structure as the Get Download User endpoint.

#### Response (Error)

In case of errors, the response will have the following structure:

```json
{
  "error": "Error type",
  "message": "Detailed error message"
}
```

For password validation errors, the response includes details about the validation failure:

```json
{
  "error": "Invalid password",
  "message": "The password does not meet security requirements",
  "details": [
    "Password must be at least 8 characters long",
    "Password must contain at least one uppercase letter",
    "Password must contain at least one digit"
  ]
}
```

Common error responses:

| HTTP Status | Error | Description |
| --- | --- | --- |
| 404 | User not found | No user exists with the specified ID |
| 400 | Invalid user type | The user with the specified ID is not a Download User |
| 400 | Invalid password | The provided password does not meet security requirements |
| 500 | Update failed | An internal server error occurred |

### Get Access Roles

#### Request

Retrieves a list of all access roles:

URL: `/roles.json`
Method: `GET`
Full Path: `https://travelmidwest.com/lmiga/admin/users/download/roles.json`

#### Response

Returns a JSON array of Download User summaries with the following structure:

```json
[
  {
    "name": "xmluser",
    "description": "Allowed to access *.xml.gz reports." 
  }
]
```

### Delete user

#### Request

URL: `/{id}/user.json`
Method: `DELETE`

#### Response

```json
{
  "success": "true",
  "message": "Account {id} has been successfully deleted"
}
```

## Special Behaviors

### Password Handling

When updating a user, the password field is optional:

- If provided, it will be validated against security requirements
- If not provided, the user's password remains unchanged

### XML Access

When XML access is removed (`requestXml` changed from `true` to `false`):

- The "xmluser" role is automatically removed from the user
- The IP address field is cleared

### Approval Workflow

When a user is approved (changing from unapproved to approved):

- The system triggers the full user approval process
- The `updated` timestamp is automatically set to the current date and time

## Examples

### Fetching All Download Users

Request:

```console
GET https://travelmidwest.com/lmiga/admin/users/download/all.json
```

### Getting a Specific Download User

Request:

```console
GET https://travelmidwest.com/lmiga/admin/users/download/123/user.json
```

### Updating a Download User

Request:

```console
POST https://travelmidwest.com/lmiga/admin/users/download/123/user.json
```

Request Body:

```json
{
  "login": "jsmith",
  "name": "John Smith",
  "email": "john.smith@example.com",
  "company": "Traffic Solutions Inc.",
  "phoneNumber": "312-555-1234",
  "jobTitle": "Senior Traffic Analyst",
  "address": {
    "street": "233 S Wacker Dr",
    "city": "Chicago",
    "state": "IL",
    "zip": "60606"
  },
  "approved": "2025-03-30T14:00:00.000Z",  
  "neverExpires": true,
  "roles": ["xmluser"],
  "requestLink": true,
  "requestXml": true,
  "ipAddress": "203.0.113.45",
  "intendedUsage": "Traffic pattern analysis for city planning",
  "intendedLocation": "Greater Chicago Area",
  "revenue": false
}
```
