# Download User Account

## About

This document describes the REST API endpoints available for Download User account management on TravelMidwest.com.

## Authentication

All endpoints require authentication with a valid Download User account. Authentication is done via cookies, specifically the `loggedIn` cookie that is set upon successful login.

## Base URL

```console
https://travelmidwest.com/lmiga/
```

## Endpoints

### Registration

Registers a new download user.

```json
POST /lmiga/user/register.json
```

#### Request Body

```json
{
 "login":           "string",               // desired login name
 "password":        "string",               // plain‐text password
 "name":            "string",               // full name
 "email":           "string",               // email address
 "company":         "string",               // company name
 "phoneNumber":     "string",               // contact phone
 "faxNumber":       "string",               // contact fax
 "address": {
   "street":        "string",
   "city":          "string",
   "state":         "string",
   "zip":           "string"
  },
 "intendedUsage":   "string",               // what user intends to use data for
 "intendedLocation":"string",               // where data will be displayed
 "requestLink":     true,                   // true to request a link
 "requestXml":      false,                  // true to request XML/camera download
 "revenue":         false,                  // true if user will earn revenue
 "recaptchaResponse":"string"               // reCAPTCHA v3 token
}
```

#### Response

On success:

```json
{
  "success": true,
  "data": {
    "message": "User created successfully",
    "userId": "long"
  }
}
```

On validation or server error, returns:

```json
{
 "success": false,
 "data": null,
 "error": {
   "code": "ERROR_CODE",
   "message": "Human‑readable message",
   "fieldErrors": {
     "password": "must be at least 8 characters",
     /* … */
    }
  }
}
```

> [!NOTE]
> This endpoint performs:
>
> - reCAPTCHA validation
> - login uniqueness check
> - password strength validation
> - user creation & persistence
> - email notification to administrators

#### Confirmation Email

As part of a successfully submitted registration form, the system will automatically inform the system access approver via email about the registration.  The access approver will be provided a link to approve or deny the request.

### Get User Account Information

Retrieves the current user's account information.

```json
GET /lmiga/user/download/account.json
```

#### Response

On success (HTTP 200):

```json
{
  "login": "string",
  "name": "string",
  "email": "string",
  "company": "string",
  "phoneNumber": "string",
  "jobTitle": "string",
  "address": {
    "street": "string",
    "city": "string",
    "state": "string",
    "zip": "string"
  },
  "faxNumber": "string",
  "requestLink": boolean,
  "requestXml": boolean,
  "ipAddress": "string",
  "intendedUsage": "string",
  "intendedLocation": "string",
  "revenue": boolean,
  "businessPartners": [
    {
      "name": "string",
      "company": "string",
      "phone": "string",
      "email": "string",
      "purpose": "string"
    }
  ],
  "warningSent": "date-time",
  "needsAgreement": boolean
}
```

On error:

- **401 Unauthorized** - User is not authenticated
- **403 Forbidden** - User does not have Download User permissions
- **500 Internal Server Error** - Server error

### Update User Account Information

Updates the current user's account information.

```console
POST /lmiga/user/download/account.json
```

#### Request

```json
{
  "login": "string",
  "password": "string", // Optional, only included when changing password
  "name": "string",
  "email": "string",
  "company": "string",
  "phoneNumber": "string",
  "jobTitle": "string",
  "address": {
    "street": "string",
    "city": "string",
    "state": "string",
    "zip": "string"
  },
  "faxNumber": "string",
  "requestLink": boolean,
  "requestXml": boolean,
  "ipAddress": "string",
  "intendedUsage": "string",
  "intendedLocation": "string",
  "revenue": boolean,
  "businessPartners": [
    {
      "name": "string",
      "company": "string",
      "phone": "string",
      "email": "string",
      "purpose": "string"
    }
  ]
}
```

#### Response

On success (HTTP 200):

```json
{
  // Updated user information (same structure as GET response)
}
```

On error:

- **400 Bad Request** - Invalid data, such as login already in use or invalid password
- **401 Unauthorized** - User is not authenticated
- **403 Forbidden** - User does not have Download User permissions
- **500 Internal Server Error** - Server error

For password validation errors, the response will include detailed messages:

```json
{
  "error": "Invalid password",
  "message": "The password does not meet security requirements",
  "details": [
    "Password must be at least 10 characters long",
    "Password should contain at least one uppercase letter",
    // Additional validation messages
  ]
}
```

### Delete User Account

Deletes the current user's account.

```console
DELETE /lmiga/user/download/account.json
```

#### Response

On success (HTTP 200):

```json
{
    "success": true,
    "message": "Your account has been successfully deleted"
}
```

On error:

- **401 Unauthorized** - User is not authenticated
- **403 Forbidden** - User does not have Download User permissions
- **500 Internal Server Error** - Server error

### Check Login Availability

Checks if a login name is available for registration or account update.

```console
GET /lmiga/user/download/check-login.json?login={loginName}&excludeCurrentUser={boolean}
```

#### Parameters

- **login** (required) - The login name to check
- **excludeCurrentUser** (optional, default: true) - Whether to exclude the current user's login from the check

#### Response

On success (HTTP 200):

```json
{
  "available": boolean,
  "message": "string"
}
```

On error:

- **401 Unauthorized** - When excludeCurrentUser=true and user is not authenticated
- **500 Internal Server Error** - Server error

### Validate Password

Checks if a password meets the security requirements. This endpoint is available for both authenticated and unauthenticated users.

```console
POST /lmiga/user/check-password.json
```

#### Post Body (application/json)

- **password** (required) - The password to validate

```
{
  "password": "check-this-password"
}
```

#### Response

On success (HTTP 200):

```json
{
  "valid": boolean,
  "message": "string",
  "strength": "strong",
  "details": [
    "string",
    // Additional validation messages if valid=false
  ]
}
```

On error:

- **500 Internal Server Error** - Server error

#### Password Requirements

Passwords must meet the following criteria:

- At least 10 characters long
- Contain characters from at least 3 of the following categories:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Digits (0-9)
  - Special characters (symbols)
- Must not contain common keyboard patterns (like "qwerty" or "asdfg")
- Must not contain sequential characters (like "abcdef" or "12345")
- Must not contain dictionary words
- Must have sufficient strength according to the zxcvbn password strength algorithm

#### Password Strength Indicator

The strength field provides feedback on password quality:

- **weak** - Password needs significant improvement
- **moderate** - Password meets some requirements but could be stronger
- **strong** - Password is reasonably secure
- **very-strong** - Password exceeds security requirements

### Request Password Reset

Requests a password reset email for a download user account. The email contains a link with a one-time token that expires after 1 hour.

This endpoint does **not** require authentication — it is used when a user has forgotten their password.

```console
POST /lmiga/user/download-password-reset-request.json
```

#### Request Body

```json
{
  "email": "string",
  "recaptchaResponse": "string"
}
```

#### Response

Always returns success to prevent email enumeration:

```json
{
  "success": true,
  "data": {
    "message": "If an account exists with that email, a reset link has been sent."
  }
}
```

> [!NOTE]
> - reCAPTCHA v3 validation is required
> - The email link points to `/User/DownloadUser/ResetPassword?token=<TOKEN>` in the React UI
> - Tokens expire after 1 hour and can only be used once
> - Token hashes are stored in the `password_reset_token` table with `userType = "DOWNLOAD"`

### Reset Password with Token

Completes the password reset using the token from the email link. This endpoint does **not** require authentication.

```console
POST /lmiga/user/download-password-reset.json
```

#### Request Body

```json
{
  "token": "string",
  "newPassword": "string"
}
```

#### Response

On success:

```json
{
  "success": true,
  "data": {
    "message": "Password has been reset successfully."
  }
}
```

On error:

- **400 Bad Request** with code `INVALID_TOKEN` — token is missing, expired, already used, or belongs to a different user type
- **400 Bad Request** with `fieldErrors.newPassword` — new password does not meet security requirements (see Password Requirements below)

> [!NOTE]
> - The new password is validated against the same password strength requirements as registration
> - The token is marked as used after a successful reset and cannot be reused
> - Use `POST /lmiga/user/check-password.json` for real-time password strength feedback while the user types

## Error Responses

All error responses follow this format:

```json
{
  "error": "string", // Error code or short description
  "message": "string" // Detailed error message
}
```

For password validation errors, an extended format is used:

```json
{
  "error": "string",
  "message": "string",
  "details": [
    "string",
    // Additional validation messages
  ]
}
```

#### Example Usage

```javascript
// Check password strength during form input
fetch('/lmiga/user/check-password.json', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ password: password })
})
  .then(response => response.json())
  .then(data => {
    if (data.data.valid) {
      // Password meets requirements
      showStrengthIndicator(data.data.strength);
    } else {
      // Show validation errors
      displayErrors(data.data.details);
    }
  });
```
