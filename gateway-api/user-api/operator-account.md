# Operator Account

## About

This document provides comprehensive documentation for the Travel Midwest Operator Account Management API endpoints. These APIs allow operators to manage their account information and view available agencies.

> [!WARNING]
> Authentication Required: All API endpoints require the user to be logged in as an Operator. Users must authenticate through the `/lmiga/user/login.json` endpoint before accessing these APIs.

## Base URL

```
https://travelmidwest.com/lmiga/admin/
```

## Authentication

Before using any of the endpoints documented here, users must be [authenticated](authentication.md) via:

```
POST https://travelmidwest.com/lmiga/user/login.json
```

See [Authentication](authentication.md) for more information about logging in. All requests to the endpoints in this documentation will return a **401 Unauthorized** error if the user is not properly authenticated.

## Common Response Format

All API responses follow a standard format:

### Success Response Structure

```json
{
  "success": true,
  "data": object,
  "error": null
}
```

### Error Response Structure

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "ERROR_CODE",
    "message": "Error message description",
    "fieldErrors": {
      "fieldName": "Error message for specific field"
    }
  }
}
```

## API Endpoints

### Get Operator Account Information

Retrieves the current operator's account information.

```
GET https://travelmidwest.com/lmiga/admin/account.json
```

#### Request

No parameters required.

#### Response

**Success (200 OK)**

```json
{
  "success": true,
  "data": {
    "login": "operator123",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phoneNumber": "555-123-4567",
    "agencyId": 42,
    "agencyName": "Travel Agency XYZ"
  },
  "error": null
}
```

**Error (401 Unauthorized)**

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "UNAUTHORIZED",
    "message": "You must be logged in to access this resource"
  }
}
```

**Error (403 Forbidden)**

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "FORBIDDEN",
    "message": "You do not have the required permissions to access this resource"
  }
}
```

### Update Operator Account Information

Updates the current operator's account information.

```
POST https://travelmidwest.com/lmiga/admin/account.json
```

#### Post Request

```json
Content-Type: `application/json`

{
  "login": "new_login",
  "password": "new_password",   Optional, only include if changing password
  "name": "Updated Name",
  "email": "updated.email@example.com",
  "phoneNumber": "555-987-6543",
  "agencyId": 42   Optional, only include if changing agency
}
```

| **Field** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| login | String | Yes | The operator's login name (username) |
| password | String | No | New password (if changing) |
| name | String | Yes | The operator's full name |
| email | String | Yes | The operator's email address |
| phoneNumber | String | Yes | The operator's phone number |
| agencyId | Long | No | ID of the operator's agency |

#### Response

**Success (200 OK)**

```json
{
  "success": true,
  "data": {
    "login": "new_login",
    "name": "Updated Name",
    "email": "updated.email@example.com",
    "phoneNumber": "555-987-6543",
    "agencyId": 42,
    "agencyName": "Travel Agency XYZ"
  },
  "error": null
}
```

**Error (400 Bad Request) - Login Already Exists**

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "LOGIN_EXISTS",
    "message": "There already is a user with the login \"new_login\". Please choose another."
  }
}
```

**Error (400 Bad Request) - Invalid Password**

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "INVALID_PASSWORD",
    "message": "The password does not meet security requirements"
  }
}
```

**Error (400 Bad Request) - Invalid Agency**

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "INVALID_AGENCY",
    "message": "The specified agency does not exist"
  }
}
```

### Delete Operator Account

Deletes the current operator's account and logs them out.

```
DELETE https://travelmidwest.com/lmiga/admin/account.json
```

#### Request

No parameters required.

#### Response

**Success (200 OK)**

```json
{
  "success": true,
  "data": {
    "success": true,
    "message": "Your account has been successfully deleted"
  },
  "error": null
}
```

**Error responses**: Same as Get Account Information.

### Check Login Availability

Checks if a login name is available for use.

```
GET https://travelmidwest.com/lmiga/admin/check-login.json?login=desired_login&excludeCurrentUser=true
```

#### Request Parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| login | String | Yes | - | The login name to check |
| excludeCurrentUser | Boolean | No | True | Whether to exclude the current user's login from the check |

#### Response

**Success (200 OK)**

```json
{
  "success": true,
  "data": {
    "available": true,
    "login": "desired_login"
  },
  "error": null
}
```

### Check Password Security

Checks if a password meets security requirements.

```
POST https://travelmidwest.com/lmiga/admin/check-password.json
```

#### Post Body

```json
Content-Type: `application/json`

{
  "password": "check-this--password"
}
```

#### Response

**Success (200 OK)**

```json
{
  "success": true,
  "data": {
    "valid": true,
    "password": "••••••••",
    "strength": "strong"
  },
  "error": null
}
```

The strength field will be "weak", "moderate", "strong" or "very-strong". Only "strong" or "very-strong" passwords are allowed.

### Get Available Agencies

Retrieves a list of all available agencies for selection during account updates.

```
GET https://travelmidwest.com/lmiga/admin/agencies.json
```

#### Request

No parameters required.

#### Response

**Success (200 OK)**

```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "name": "Travel Agency XYZ"
    },
    {
      "id": 2,
      "name": "Global Journeys Inc."
    },
    {
      "id": 3,
      "name": "Midwest Travels"
    }
  ],
  "error": null
}
```

**Error (500 Internal Server Error)**

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "SERVER_ERROR",
    "message": "An error occurred while retrieving the list of agencies"
  }
}
```

## Implementation Notes

1. The login validation (`check-login.json`) should be used to validate username availability before submitting account updates.
1. The password validation (`check-password.json`) should be used to ensure passwords meet security requirements before submission.
1. When updating an account, only changed fields need to be included in the request payload.
1. Password field should only be included when the user wishes to change their password.
1. After successful account deletion, the UI should redirect the user to the login page as they will be automatically logged out.
1. The agencies list should be loaded when the account form is initialized to populate the agency selection dropdown.

## Error Handling

The React application should handle the following error scenarios:

- Authentication errors (401 Unauthorized).
- Permission errors (403 Forbidden).
- Validation errors for login, password, and agency selection.
- Server errors (500 Internal Server Error).

## Example React Implementation

Here's a simplified example of how to implement the account form in React:

```javascript
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const AccountForm = () => {
  const [accountData, setAccountData] = useState({});
  const [agencies, setAgencies] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
 Fetch account data and agencies when component mounts
    Promise.all([
      axios.get('https://travelmidwest.com/lmiga/admin/account.json'),
      axios.get('https://travelmidwest.com/lmiga/admin/agencies.json')
    ]).then(([accountRes, agenciesRes]) => {
      setAccountData(accountRes.data.data);
      setAgencies(agenciesRes.data.data);
      setLoading(false);
    }).catch(err => {
      setError(err.response?.data?.error || { message: 'An error occurred' });
      setLoading(false);
    });
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('https://travelmidwest.com/lmiga/admin/account.json', accountData);
      setAccountData(response.data.data);
      alert('Account updated successfully!');
    } catch (err) {
      setError(err.response?.data?.error || { message: 'An error occurred' });
    }
  };

 Implement the rest of the form...
};
```
