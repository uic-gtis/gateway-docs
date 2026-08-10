# Route Alert User API

## About

The route alert user API allows a user to register, update, and create custom routes and preferences for receiving emailed "alerts" on those routes. The registration and password check API calls starting with "/user" are public.

## Alerts User Registration - /user

The /user/trip-register.json end point provides the means to send an alert user registration request. All requests require both a valid recaptcha response and a follow up email verification.

All API endpoints are prefixed by:

- /lmiga/user/

The registration end points do not require prior authentication, they are publicly available.

### POST trip-register.json

Submit an account for registration.

Payload

```json
{
  "email": "john@doe.com",
  "password": "requested password plain text",
  "format": "HTML" | "TEXT",
  "recaptchaResponse": "response"
}
```

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "message": "Registration successful. Check your email to verify your account."
  },
  "error": null
}
```

> [!NOTE]
> The email to the user will direct them to /Trips/VerifyAlertsRegistration, see trip-verify.json below.

### POST trip-check-email.json

Check to see if an email is available for registration.

Payload

```json
{
  "email": "check@this.com"
}
```

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "available": true
  },
  "error": null
}
```

### POST trip-password-reset-request.json

Request a password reset for the given user. The response is always successful to prevent email enumeration.

Payload

```json
{
  "email": "email@reset.com",
  "recaptchaResponse": "response"
}
```

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "message": "If an account exists with that email, a reset link has been sent."
  },
  "error": null
}
```

### POST trip-password-reset.json

Reset a user's password using the token received via email. Tokens expire after 1 hour and can only be used once.

Payload

```json
{
  "token": "uuid-token-from-email",
  "newPassword": "new_plaintext_password"
}
```

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "message": "Password has been reset successfully."
  },
  "error": null
}
```

Error Response — invalid or expired token (400 status)

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "INVALID_TOKEN",
    "message": "Invalid or expired reset token."
  }
}
```

### GET trip-verify.json

Takes on request parameter:

- code=xxx

Use this end point when the user clicks on the magic link in their email. Pass the code provided by the user to trip-verify.json?code=xxx. A successful response will mark the account as "email verified" which allows alert emails to be sent to it.

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "message": "Email verified successfully."
  },
  "error": null
}
```

Already verified response (200 status)

```json
{
  "success": true,
  "data": {
    "message": "Email already verified."
  },
  "error": null
}
```

## Alerts User Account Maintenance - /user/trip

The account maintenance API requires prior authentication, see [Authentication](authentication.md). All API end points for the account maintenance start with:

- /lmiga/user/trip/

### POST resend-verification.json

Resend the email verification notification. Only applicable when the user's email has not yet been verified.

Successful Response (200 status)

```json
{
  "success": true,
  "data": "Verification email sent.",
  "error": null
}
```

Error Response — already verified (400 status)

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "ALREADY_VERIFIED",
    "message": "Email is already verified."
  }
}
```

### GET account.json

Retrieves the logged in user's account details.

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "email": "users@email.com",
    "format": "HTML" | "TEXT",
    "emailVerified": true | false,
    "created": <ISO8601 timestamp>,
    "suspendAlertsPeriod": null | {
      "start": <ISO8601 timestamp>,
      "end": <ISO8601 timestamp>
    }
  },
  "error": null
}
```

### PUT account.json

Updates the user's account information. All fields are optional; only provided fields are updated. Changing the email address will set emailVerified to false and trigger a new verification email.

Payload

```json
{
  "email": "mynew@email.com",
  "password": "new_unencrypted_plaintext_password",
  "format": "HTML" | "TEXT",
  "suspendAlertsStart": "yyyy-MM-dd" | null,
  "suspendAlertsEnd": "yyyy-MM-dd" | null,
  "clearSuspendPeriod": true | false
}
```

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "email": "users@newemail.com",
    "format": "HTML" | "TEXT",
    "emailVerified": true | false,
    "created": <ISO8601 timestamp>,
    "suspendAlertsPeriod": null | {
      "start": <ISO8601 timestamp>,
      "end": <ISO8601 timestamp>
    }
  },
  "error": null
}
```

### DELETE account.json

Deletes the logged in user's account. All alert emails will cease.

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "message": "Account deleted successfully."
  },
  "error": null
}
```

## Custom Routes

Registered trip alert users can create custom routes to receive email alerts on those routes. Route planning is a public endpoint; saving, updating, and deleting routes require authentication.

### POST /lmiga/routePlanner.json

Plans a route and provides information on it. This endpoint is public (no authentication required).

Payload

```json
{
  "start": {
    "latLng": { "lat": 44.0, "lng": -88.0 },
    "address": "descriptive text" | null
  },
  "end": {
  "latLng": { "lat": 44.0, "lng": -88.0 },
    "address": "descriptive text" | null
  },
  "waypoints": [
    { "lat": 44.0, "lng": -88.0 }, { "lat": 43.0, "lng": -87.0 }
    ],
  // the following options are not required in the request
  "useStartDirection": true | false,
  "maxDistance": <meters>,
  "maxTravelTime": <seconds>,
  "metric": "DISTANCE" | "STATIC_TRAVEL_TIME" | "DYNAMIC_TRAVEL_TIME",
  "uTurnAngleThreshold": 135.0,
  "preferredName": null,
  "preferredName2": null,
  "leftTurnPenaltySec": 8.0,
  "rightTurnPenaltySec": 3.0,
  "minorTurnThresholdDeg": 10.0,
  "minorTurnPenaltyPerDeg": 0.02,
  "preferredRoadFactor": 0.2,
  "leaveRoadPenaltyFactor": 1.8,
  "avoidTolls": true | false,
  "tollSegmentPenaltyCost": <double>,
  "avoidHighways": true | false,
  "highwaySegmentPenaltyFactor": <double>,
  "expresswaySpeedInMetersPerSecond": 26.82,
  "majorArterialSpeedInMetersPerSecond": 17.88,
  "otherSpeedInMetersPerSecond": 11.18
}
```

Successful Response (200 status)

The route will be planned and the resulting route is returned. The response includes a **routeData** field containing the server's internal serialized route. This is an opaque JSON object — store it as-is and pass it back when saving or updating the route to avoid redundant route re-computation on the server.

```json
{
  "success": true,
  "data": {
    "path": [ { "lat": 44.0, "lng": -88.0 }, ... { "lat": 42.0, "lng": -86.0 } ],
    "travelTimeSeconds": 120.0,
    "lengthMeters": 1200.0,
    "averageSpeedMph": 60.0,
    "congestionLevel": "NON_CONGESTION",
    "routeData": { ... },
    "links": [
      { "c": [ { "lat": 44.0, "lng": -88.0 }, ... ], "s": 26.82 }
    ],
    "incidents": [
      {
        "externalId": "EVT-123",
        "description": "Major accident on I-90",
        "severity": "HIGH",
        "distanceAlongRouteMeters": 5432.1,
        "locationDescription": "I-90 near Lake Shore Drive",
        "lat": 41.88,
        "lng": -87.63,
        "popup": { ... }
      }
    ],
    "roadWork": [
      {
        "externalId": "CON-456",
        "description": "Lane closure",
        "severity": "MEDIUM",
        "distanceAlongRouteMeters": 8200.0,
        "locationDescription": "I-290 westbound",
        "lat": 41.87,
        "lng": -87.75,
        "popup": { ... }
      }
    ]
  },
  "error": null
}
```

> [!NOTE]
>   **routeData** is an opaque object. Do not modify or inspect its contents. Pass it unchanged to create.json or the update route endpoint to skip re-planning. If omitted from those requests, the server will re-plan the route from waypoints using default route options.

> [!NOTE]
>   **links** contains speed segments for rendering color-coded traffic overlays. Each entry has **c** (array of lat/lng coordinates) and **s** (speed in meters per second).

> [!NOTE]
>   **popup** in incident and roadWork entries contains formatted properties matching the react-ui map popup format (IncidentProperties / ConstructionProperties).

### Saved Route Endpoints

The following endpoints require authentication. All are prefixed by:

- /lmiga/user/trip/

#### GET routes.json

List all saved routes for the authenticated user, enriched with real-time traffic info.

Successful Response (200 status)

The list response uses a slim summary DTO — it does not include full alert preferences. Use GET {id}/route.json to retrieve the full configuration for a specific route.

```json
{
  "success": true,
  "data": [
    {
      "routeId": 123,
      "displayName": "Morning Commute",
      "noAlerts": false,
      "congestionLevel": "NON_CONGESTION",
      "travelTimeSeconds": 1234.5,
      "waypointCount": 2,
      "waypoints": [
        { "lat": 41.8, "lng": -87.6, "label": "Home" },
        { "lat": 42.0, "lng": -87.8, "label": "Work" }
      ]
    }
  ],
  "error": null
}
```

> [!NOTE]
>   **congestionLevel** and **travelTimeSeconds** are populated from live traffic data. They may be absent if the server could not load traffic for the route.

#### POST create.json

Save a new custom route with alert preferences.

If ***routeData*** (from the routePlanner.json response) is included, the server uses the pre-planned route directly, avoiding expensive re-computation. If omitted, the server re-plans the route from waypoints using default route options.

**Payload**

```json
{
  "displayName": "Morning Commute",
  "waypoints": [
    { "lat": 41.8, "lng": -87.6, "label": "Home" },
    { "lat": 42.0, "lng": -87.8, "label": "Work" }
  ],
  "preferences": {
    "noAlerts": false,
    "travelTime": true,
    "congestion": false,
    "construction": false,
    "incident": false,
    "weather": true,
    "allSevereIncidents": false,
    "speedThreshold": 1000.0,
    "frequency": 86400000,
    "daysOfWeek": {
      "monday": true, "tuesday": true, "wednesday": true,
      "thursday": true, "friday": true,
      "saturday": false, "sunday": false
    },
    "period": "06:00 to 18:00",
    "noIncidentsPeriod": null
  },
  "routeData": { ... }
}
```

~|=Field|=Required|=Description
~|displayName|yes|User-facing name for the route
~|waypoints|yes|At least 2 lat/lng points (start and end); each may include an optional **label** (address text)
~|preferences|no|Alert preferences (defaults applied if omitted)
~|routeData|no|Opaque route object from routePlanner.json response. If provided, the server skips re-planning.

> [!NOTE]
>   **period** and **noIncidentsPeriod** are serialized as strings in the format "HH:MM to HH:MM" (24-hour time). When sending values to the server (in create or update), use the same string format.

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "routeId": 123,
    "displayName": "Morning Commute",
    "lengthMeters": 45678.9,
    "waypointCount": 2,
    "waypoints": [
      { "lat": 41.8, "lng": -87.6, "label": "Home" },
      { "lat": 42.0, "lng": -87.8, "label": "Work" }
    ],
    "noAlerts": false,
    "travelTime": true,
    "congestion": false,
    "construction": false,
    "incident": false,
    "weather": true,
    "allSevereIncidents": false,
    "speedThreshold": 1000.0,
    "frequency": 86400000,
    "daysOfWeek": { ... },
    "period": "06:00 to 18:00",
    "noIncidentsPeriod": null
  },
  "error": null
}
```

Error Response — invalid routeData (400 status)

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "INVALID_ROUTE_DATA",
    "message": "routeData contains no route sections"
  }
}
```

#### GET {id}/route.json

Get a specific saved route by its custom route ID.

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "routeId": 123,
    "displayName": "Morning Commute",
    "lengthMeters": 45678.9,
    "waypointCount": 2,
    "waypoints": [
      { "lat": 41.8, "lng": -87.6, "label": "Home" },
      { "lat": 42.0, "lng": -87.8, "label": "Work" }
    ],
    "noAlerts": false,
    "travelTime": true,
    "congestion": false,
    "construction": false,
    "incident": false,
    "weather": true,
    "allSevereIncidents": false,
    "speedThreshold": 1000.0,
    "frequency": 86400000,
    "daysOfWeek": { ... },
    "period": "06:00 to 18:00",
    "noIncidentsPeriod": null
  },
  "error": null
}
```

#### GET {id}/routeMap.json

Get the stored route map data (path and routeData) for a saved route without re-planning.

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "path": [ { "lat": 44.0, "lng": -88.0 }, ... ],
    "routeData": { ... },
    "lengthMeters": 45678.9
  },
  "error": null
}
```

#### GET {id}/routeTraffic.json

Get live traffic data for a stored route. Returns current travel time, speed, congestion level, speed segments, incidents, and road work along the route.

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "travelTimeSeconds": 1234.5,
    "lengthMeters": 45678.9,
    "speedMetersPerSecond": 27.5,
    "speedLimitMph": 55.0,
    "congestionLevel": "NON_CONGESTION",
    "links": [
      { "c": [ { "lat": 44.0, "lng": -88.0 }, ... ], "s": 26.82 }
    ],
    "incidents": [
      {
        "externalId": "EVT-123",
        "description": "Major accident on I-90",
        "severity": "HIGH",
        "distanceAlongRouteMeters": 5432.1,
        "locationDescription": "I-90 near Lake Shore Drive",
        "lat": 41.88,
        "lng": -87.63,
        "popup": { ... }
      }
    ],
    "roadWork": [
      {
        "externalId": "CON-456",
        "description": "Lane closure",
        "severity": "MEDIUM",
        "distanceAlongRouteMeters": 8200.0,
        "locationDescription": "I-290 westbound",
        "lat": 41.87,
        "lng": -87.75,
        "popup": { ... }
      }
    ]
  },
  "error": null
}
```

> [!NOTE]
>   **links** contains speed segments for rendering color-coded traffic overlays. Each entry has **c** (array of lat/lng coordinates) and **s** (speed in meters per second).

#### GET {id}/routeWeather.json

Get weather alerts and winter road conditions for a stored route.

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "weatherAlerts": [ ... ],
    "winterConditions": [ ... ]
  },
  "error": null
}
```

#### PUT {id}/route.json

Update a saved route. All fields are optional — only provided fields are changed.

To update **only** the display name or alert preferences, send just those fields. To update the **route geometry**, include both **routeData** and **waypoints** (at least 2). This replaces the saved route path without requiring a full re-plan.

Payload

```json
{
  "displayName": "Updated Name",
  "preferences": {
    "noAlerts": false,
    "travelTime": true,
    "congestion": true,
    "construction": false,
    "incident": true,
    "weather": true,
    "allSevereIncidents": false,
    "speedThreshold": 1000.0,
    "frequency": 86400000,
    "daysOfWeek": {
      "monday": true, "tuesday": true, "wednesday": true,
      "thursday": true, "friday": true,
      "saturday": false, "sunday": false
    },
    "period": "06:00 to 18:00",
    "noIncidentsPeriod": null
  },
  "waypoints": [
    { "lat": 41.8, "lng": -87.6, "label": "Home" },
    { "lat": 42.0, "lng": -87.8, "label": "Work" }
  ],
  "routeData": { ... }
}
```

| Field | Required | Description |
| --- | --- | --- |
| displayName | no | New display name |
| preferences | no | Updated alert preferences |
| routeData | no | Opaque route object from routePlanner.json. If provided, **waypoints** is required. |
| waypoints | no | Required when routeData is provided (at least 2 points). Ignored otherwise. |

Successful Response (200 status)

```json
{
  "success": true,
  "data": {
    "routeId": 123,
    "displayName": "Updated Name",
    "lengthMeters": 45678.9,
    "waypointCount": 2,
    "waypoints": [ ... ],
    "noAlerts": false,
    "travelTime": true,
    "congestion": true,
    "construction": false,
    "incident": true,
    "weather": true,
    "allSevereIncidents": false,
    "speedThreshold": 1000.0,
    "frequency": 86400000,
    "daysOfWeek": { ... },
    "period": "06:00 to 18:00",
    "noIncidentsPeriod": null
  },
  "error": null
}
```

Error Response — routeData provided without waypoints (400 status)

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "MISSING_WAYPOINTS",
    "message": "waypoints (at least 2) required when updating route geometry"
  }
}
```

#### DELETE {id}/route.json

Delete a saved route.

Successful Response (200 status)

```json
{
  "success": true,
  "data": "Route deleted",
  "error": null
}
```

#### POST {id}/send-now.json

Send a one-off alert email immediately for a saved route. Optionally accepts unsaved preference overrides from the UI dialog to use instead of the route's saved preferences.

Payload (optional — send empty body or omit to use saved preferences)

```json
{
  "noAlerts": false,
  "travelTime": true,
  "congestion": true,
  "construction": false,
  "incident": true,
  "weather": true,
  "allSevereIncidents": false,
  "speedThreshold": 1000.0,
  "frequency": 86400000,
  "daysOfWeek": { ... },
  "period": "06:00 to 18:00",
  "noIncidentsPeriod": null
}
```

Successful Response (200 status)

```json
{
  "success": true,
  "data": "Alert email sent successfully.",
  "error": null
}
```

Error Response — email not verified (400 status)

```
{
  "success": false,
  "data": null,
  "error": {
    "code": "EMAIL_NOT_VERIFIED",
    "message": "Please verify your email address before sending alerts."
  }
}
```
