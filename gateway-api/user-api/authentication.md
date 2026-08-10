# Authentication

## About

This document provides information for React developers about integrating with the Travel Midwest Authentication API. The API allows applications to authenticate users and retrieve their profile information and appropriate context path.

## Base URL

The base URL for all endpoints:

```console
https://travelmidwest.com/lmiga/user/login.json
```

## Login

- **Method**: POST
- **Content-Type**: application/json

### Request

The authentication request should include the following JSON payload:

```json
{
  "username": "user@example.com",
  "password": "userPassword123"
}
```

#### Fields

| Field | Type | Description |
| --- | --- | --- |
| username | String | The user's login ID or email address |
| password | String | The user's password |

### Response

#### Successful Authentication

For successful authentication, the server returns HTTP 200 OK with a JSON response that includes:

- User profile information
- Appropriate context path for the authenticated user

Example response:

```json
{
  "id": 123,
  "login": "jsmith",
  "name": "John Smith",
  "email": "jsmith@example.com",
  "company": "Example Transportation Co.",
  "phoneNumber": "555-123-4567",
  "jobTitle": "Traffic Engineer",
  "address": {
    "street": "123 Main St",
    "city": "Chicago",
    "state": "IL",
    "zip": "60601"
  },
  "roles": ["download", "viewer"],
  "contextPath": "download"
}
```

For alerts users, the response will contain different fields:

```json
{
  "id": 456,
  "email": "user@example.com",
  "format": "HTML",
  "emailVerified": true,
  "bouncing": false,
  "created": "2023-06-15T14:30:45.000Z",
  "lastLoggedIn": "2023-08-10T09:15:22.000Z",
  "suspendAlertsPeriod": {
    "start": "2023-12-24T00:00:00.000Z",
    "end": "2024-01-02T23:59:59.000Z"
  },
  "contextPath": "trip"
}
```

#### Failed Authentication

For failed authentication, the server returns HTTP 401 Unauthorized with a JSON response:

```json
{
  "success": false,
  "message": "Invalid username or password"
}
```

## User Types and Context Paths

The API supports different types of users, each with their own context path:

| User Type | Context Path | Description |
| --- | --- | --- |
| AlertsUser | trip | Users who receive travel alerts |
| DownloadUser | download | Users with permission to download data |
| IncidentEntryUser | entry | Users who can enter incidents |
| IncidentNotificationUser | notification | Users who receive incident notifications |
| Operator | admin | System operators |

The React application should redirect users to the appropriate path based on the `contextPath` field in the response.

## Integration Example

Here's an example of integrating with the authentication API using React and fetch:

```javascript
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await fetch('https://travelmidwest.com/lmiga/user/login.json', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
        credentials: 'include'  Important: to send and receive cookies
      });
 
      const data = await response.json();
 
      if (!response.ok) {
        throw new Error(data.message || 'Authentication failed');
      }
 
       Store user data in state management (Redux, Context API, etc.)
      localStorage.setItem('user', JSON.stringify(data));
 
  Redirect to appropriate context path
      navigate(`/${data.contextPath}`);
 
    } catch (err) {
      setError(err.message || 'An error occurred during login');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-container">
      <h2>Login to Travel Midwest</h2>
      {error && <div className="error-message">{error}</div>}
      <form onSubmit={handleLogin}>
        <div className="form-group">
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Logging in...' : 'Login'}
        </button>
      </form>
    </div>
  );
};

export default Login;
```

## Logout

Log out the currently logged in user.

- /user/logout.json

**Response**

```json
{
  "success": true/false
  "message": "Logged out" / "User not logged in"
}
```

## Session Management

The Travel Midwest API provides endpoints for managing user sessions, including checking session status and renewing active sessions.

### Session Status

Check if a user has an active session and when it expires. This endpoint does not require authentication and does not extend the session.

URL: /session/status.json
Method: GET
Authentication: Not required
Full URL: https://travelmidwest.com/lmiga/session/status.json

#### Request

No request body required. Session information is read from cookies.

```javascript
// Example using fetch
const response = await fetch('https://travelmidwest.com/lmiga/session/status.json', {
method: 'GET',
credentials: 'include'  // Important: to send cookies
});
```

#### Response

##### Authenticated User

```json
{
  "success": true,
  "data": {
    "authenticated": true,
    "expiresAt": "2025-01-20T15:30:00.000Z"
  },
  "error": null
}
```

##### Unauthenticated User

```json
{
  "success": true,  
  "data": {
    "authenticated": false,  
    "expiresAt": null
  },
  "error": null
}
```

##### Alerts User (No Session Timeout)

For alerts users who don't have session timeout:

```json
{
  "success": true,
  "data": {
    "authenticated": true,
    "expiresAt": null
  },
  "error": null
}
```

#### Response Fields

| Field | Type | Description |  |
| --- | --- | --- | --- |
| authenticated | Boolean | Whether the user has an active session |  |
| expiresAt | String/null | ISO 8601 formatted date/time when the session expires. Null for unauthenticated users or users without session timeout |  |

### Session Renewal

Renew an active session to extend its expiration time. This endpoint requires authentication and will update the session's last access time.

URL: /session/auth/renew.json
Method: POST
Authentication: Required
Full URL: https://travelmidwest.com/lmiga/session/auth/renew.json

#### Request

No request body required. The session to renew is identified by cookies.

```javascript
// Example using fetch
const response = await fetch('https://travelmidwest.com/lmiga/session/auth/renew.json', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  credentials: 'include'  // Important: to send and receive cookies
});
```

#### Response

##### Successful Renewal

```json
{
  "success": true,
  "data": {
    "expiresAt": "2025-01-20T16:00:00.000Z"
  },
  "error": null
}
```

##### Alerts User Renewal

For alerts users (who don't have session timeout):

```json
{
  "success": true,
  "data": {
    "expiresAt": null
  },
  "error": null
}
```

##### No Active Session

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "UNAUTHORIZED_ERROR",
    "message": "No active session to renew",
    "fieldErrors": {}
  }
}
```

#### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| expiresAt | String/null | ISO 8601 formatted date/time when the renewed session expires. Null for users without session timeout |

### React Integration Example

Here's an example of implementing session management in a React application:

```javascript
import React, { useState, useEffect, useCallback } from 'react';
const SessionManager = ({ children }) => {
const [sessionStatus, setSessionStatus] = useState(null);
const [isChecking, setIsChecking] = useState(false);
// Check session status
const checkSession = useCallback(async () => {
setIsChecking(true);
try {
const response = await fetch('https://travelmidwest.com/lmiga/session/status.json', {
method: 'GET',
credentials: 'include'
});
  const data = await response.json();
  
  if (data.success) {
    setSessionStatus(data.data);
    
    // If authenticated and session expires soon, show warning
    if (data.data.authenticated && data.data.expiresAt) {
      const expiryTime = new Date(data.data.expiresAt).getTime();
      const now = new Date().getTime();
      const minutesRemaining = (expiryTime - now) / (1000 * 60);
      
      if (minutesRemaining < 5) {
        console.warn('Session expires in less than 5 minutes');
        // Show warning to user or auto-renew
      }
    }
  }
} catch (error) {
  console.error('Failed to check session status:', error);
} finally {
  setIsChecking(false);
}
}, []);
// Renew session
const renewSession = useCallback(async () => {
try {
const response = await fetch('https://travelmidwest.com/lmiga/session/auth/renew.json', {
method: 'POST',
headers: {
'Content-Type': 'application/json',
},
credentials: 'include'
});
  const data = await response.json();
  
  if (data.success) {
    console.log('Session renewed. New expiry:', data.data.expiresAt);
    // Update session status
    setSessionStatus({
      authenticated: true,
      expiresAt: data.data.expiresAt
    });
    return true;
  } else {
    console.error('Failed to renew session:', data.error.message);
    return false;
  }
} catch (error) {
  console.error('Failed to renew session:', error);
  return false;
}
}, []);
// Check session status on mount and periodically
useEffect(() => {
checkSession();
// Check session status every 5 minutes
const interval = setInterval(checkSession, 5 * 60 * 1000);

return () => clearInterval(interval);
}, [checkSession]);
// Set up activity-based renewal
useEffect(() => {
if (!sessionStatus?.authenticated) return;
const handleUserActivity = () => {
  // Debounce renewal requests
  if (window.renewalTimeout) {
    clearTimeout(window.renewalTimeout);
  }
  
  window.renewalTimeout = setTimeout(() => {
    renewSession();
  }, 60000); // Renew after 1 minute of activity
};

// Listen for user activity
window.addEventListener('mousemove', handleUserActivity);
window.addEventListener('keypress', handleUserActivity);

return () => {
  window.removeEventListener('mousemove', handleUserActivity);
  window.removeEventListener('keypress', handleUserActivity);
  if (window.renewalTimeout) {
    clearTimeout(window.renewalTimeout);
  }
};
}, [sessionStatus, renewSession]);
return (
<div>
{sessionStatus && !sessionStatus.authenticated && (
<div className="session-expired">
Your session has expired. Please log in again.
</div>
)}
{children}
</div>
);
};
export default SessionManager;
```

### Session Timeout Warning Component

```javascript
import React, { useState, useEffect } from 'react';
const SessionTimeoutWarning = ({ expiresAt, onRenew }) => {
const [showWarning, setShowWarning] = useState(false);
const [minutesRemaining, setMinutesRemaining] = useState(null);
useEffect(() => {
if (!expiresAt) return;
const checkTimeRemaining = () => {
  const now = new Date().getTime();
  const expiry = new Date(expiresAt).getTime();
  const minutes = Math.floor((expiry - now) / (1000 * 60));
  
  setMinutesRemaining(minutes);
  
  // Show warning when 5 minutes or less remaining
  if (minutes <= 5 && minutes > 0) {
    setShowWarning(true);
  } else if (minutes <= 0) {
    // Session expired
    window.location.href = '/login';
  } else {
    setShowWarning(false);
  }
};

checkTimeRemaining();
const interval = setInterval(checkTimeRemaining, 30000); // Check every 30 seconds

return () => clearInterval(interval);
}, [expiresAt]);
if (!showWarning) return null;
return (
<div className="session-warning">
<p>Your session will expire in {minutesRemaining} minute{minutesRemaining !== 1 ? 's' : ''}.</p>
<button onClick={onRenew}>Extend Session</button>
</div>
);
};
```

### Session Implementation Notes

- **Session Status Checking**: The status endpoint is designed for periodic polling without affecting session timeout. It's safe to call frequently without extending the user's session.
- **Session Renewal**: The renewal endpoint should be called sparingly, typically in response to user activity or when the session is about to expire.
- **Cookie Management**: Both endpoints rely on session cookies. Ensure credentials: 'include' is set in all fetch requests.
- **User Types**: Different user types have different session behaviors:
  - Admin users (Operators, DownloadUsers, etc.) have session timeout (default 30 minutes)
  - Alerts users don't have session timeout and remain logged in until explicit logout
- **Error Handling**: Always implement proper error handling for network failures and unexpected responses.
- **Security**: The renewal endpoint requires authentication to prevent unauthorized session extension.

### Session Management Best Practices

1. Polling Frequency: Check session status no more than once per minute to avoid unnecessary server load.
1. User Experience: Warn users before their session expires and provide an easy way to extend it.
1. Auto-Renewal: Consider implementing activity-based auto-renewal for better user experience.
1. Logout Handling: When a session expires, redirect users to the login page with a clear message.
1. State Management: Store session status in your React state management solution (Redux, Context API, etc.) for easy access across components.

## Security Considerations

- HTTPS required for all requests.

## Rate Limiting and Brute Force Protection

The API implements brute force protection:

- After 3 failed login attempts, delays are progressively added.
- Clients should handle 429 Too Many Requests responses appropriately.

## Troubleshooting

### Common Issues

- **Cookies Not Being Saved**: Ensure you include `credentials: 'include'` in fetch requests.
- **CORS Issues**: Contact the API administrator if you experience CORS-related problems.
- **Session Expiration**: Implement proper handling for expired sessions.

### Support

For additional support or to report issues with the API, please contact [support@travelmidwest.com](mailto:support@travelmidwest.com?subject=User%20Authentication%20API)
