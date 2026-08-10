# Incident notification response

> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.

## About

The incidentResponse.json API reports which users were notified about an incident, and how they responded. You must be logged in with "admin" or "eventNotificationViewer" privileges for this API.

## Request

```console
https://travelmidwest.com/lmiga/incidentResponse.json?id=externalIncidentId
```

This is a GET request with one required query parameter:

- **id** (required) - the external ID of the incident to report on

An id that matches no incident returns an empty response body.

## Response

The response is a JSON object with the following fields:

- **incident **- object with the following fields:
  - externalId - will be same as passed in "id" parameter
  - status - "New", "Updated", "Canceled", "Closed", "Deleted" or "Clearing"
  - location - textual description of impact and location of incident
  - description - information from data source describing incident
  - lanes - human readable version of lanes closed, e.g, "Right two lanes closed"
  - start - date and time incident started, formatted as "m/d/yyyy HH:MM:SS z"
  - end - estimated end date/time, if known, insane format as start
  - source - agency that reported the incident
  - sourceId - identifier for source (not really needed but may be used in a future API)
  - features - list of things that happened in text form, e.g. "Accident with collision, road block"
  - notificationDistance - estimate of how many miles of road this incident will block
  - latitude, longitude - in degrees for incident location
- **notifications **- array of objects representing users that were notified, each with the following fields:
  - name - person's name that was contacted
  - phone - phone number
  - email - email address
  - agency - person's agency name, e.g. "IDOT"
  - sendTime - time notification was sent
  - **dms **- array of objects representing DMS that should publish information about the incident (will be empty if notificationDistance doesn't span a DMS)
    - location - textual description of location of DMS
    - status - status of DMS - Unknown, Not available, Operational, etc.
    - currentMessage - current message being displayed on the DMS
    - suggestedMessage - message that should be display, e.g. "Incident 5 miles ahead"
    - lastUpdate - last time DMS was updated as m/d/yyyy HH:MM a z
    - lastReceived - last time the DMS sent data to the GTIS
    - distanceToEventInMiles - double number, self explanatory
