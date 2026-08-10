# Show Camera

## About

> [!NOTE]
> The showCamera.json endpoint is used to obtain information for the cameras present in the [cameraInfo.csv](../camera-info-csv.md) file.

The Show Camera JSON endpoint provides metadata for a single camera, including its location description, source agency, and available directions with image URLs and ages. It is used by the ShowCamera page which replaces the old showCamera.jsp popup.

![1773264511401-584.png](../images/1773264511401-584.png)

## Request

```console
https://travelmidwest.com/lmiga/showCamera.json?id=cameraExternalId
```

Parameters:

- id (required)
  - The external ID of the camera (e.g., `IL-IDOTD4-4219`, `IL-ISTHA-OYVF2%2FCdGpuYwBNqc%3D`)
  - Note: the ID must be URL-encoded if it contains special characters

## Response

```json
{
    "id": "IL-IDOTD4-4219",
    "locationDescription": "I-74 at Maher Rd. (Exit 75)",
    "sourceName": "IDOT D4",
    "remote": true,
    "directions": [
        {
            "code": "E",
            "displayName": "East",
            "remoteUrl": "https://cctv.travelmidwest.com/IL-IDOTD4-4219_E.jpg",
            "ageMs": 181042
        },
        {
            "code": "N",
            "displayName": "North",
            "remoteUrl": "https://cctv.travelmidwest.com/IL-IDOTD4-4219_N.jpg",
            "ageMs": 183519
        },
        {
            "code": "S",
            "displayName": "South",
            "remoteUrl": "https://cctv.travelmidwest.com/IL-IDOTD4-4219_S.jpg",
            "ageMs": 179204
        },
        {
            "code": "W",
            "displayName": "West",
            "remoteUrl": "https://cctv.travelmidwest.com/IL-IDOTD4-4219_W.jpg",
            "ageMs": 185101
        }
    ]
}
```

Data fields:

- id — the external ID of the camera, matching the `id` parameter in the request
- locationDescription — a text description of where the camera is located (e.g., "I-74 at Maher Rd. (Exit 75)")
- sourceName — the name of the source agency that operates the camera (e.g., "IDOT D4", "Illinois Tollway", "IDOT D1")
- remote — `true` if the camera images are served from an external URL (e.g., cctv.travelmidwest.com), `false` if served via the `/snapshot` endpoint
- directions — an array of available camera directions, sorted alphabetically by direction code. Single-direction cameras (BasicCamera, IdotCamera) will have one entry with code `NONE`.
  - code — the direction code: `N`, `S`, `E`, `W`, `NE`, `NW`, `SE`, `SW`, or `NONE`
  - displayName — the human-readable direction name: "North", "South", "East", "West", "Northeast", "Northwest", "Southeast", "Southwest", or "None"
  - remoteUrl — the direct URL to the camera image if the camera is remote; `null` if the camera is not remote (use the `/snapshot` endpoint instead)
  - ageMs — the age of the most recent image in milliseconds; `-1` if the age is unknown

## Image URLs

To display the camera image, use one of the following approaches depending on the `remote` flag:

- **Remote cameras** (`remote` = `true`): Use the `remoteUrl` field from the direction entry directly as an `<img src>`.
- **Non-remote cameras** (`remote` = `false`): Use the `/snapshot` endpoint:

```console
https://travelmidwest.com/lmiga/snapshot?id=cameraExternalId&direction=directionCode
```

The `direction` parameter is required for multi-direction cameras and should be omitted for single-direction cameras (code = `NONE`).

## Error Responses

- **404 Not Found** — returned if no camera exists with the given `id`
- **400 Bad Request** — returned if the `id` parameter is missing

## ShowCamera Page

The ShowCamera page is a standalone React page that uses this endpoint. It can be opened directly or embedded as a popup:

```console
https://travelmidwest.com/showCamera?id=IL-IDOTD4-4219&direction=E
```

Parameters:

- id (required) — the camera external ID
- direction (optional) — the initial direction to display; defaults to the first available direction

The page has no header or navigation menu, making it suitable for use as a popup window or iframe embed. The image and age refresh automatically every 30 seconds.
