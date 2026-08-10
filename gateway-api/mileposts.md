# Mileposts

## About

API endpoints for retrieving milepost data for expressways in the Travel Midwest region.

**Base URL:**

```
https://travelmidwest.com/lmiga
```

## Response Format

All endpoints return a standardized JSON response:

### Success Response

```json
{
  "success": true,
  "data": { ... },
  "error": null
}
```

### Error Response

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Description of the error",
    "fieldErrors": {
      "fieldName": "Field-specific error message"
    }
  }
}
```

## Endpoints

### GET /mileposts/expressways.json

Returns all expressways grouped by state, including full state names. Use this endpoint on application load to populate state and expressway selection controls.

**URL:**

```
https://travelmidwest.com/lmiga/mileposts/expressways.json
```

**Parameters:** None

**Response:**

```json
{
  "success": true,
  "data": {
    "IL": {
      "name": "Illinois",
      "expressways": [
        {
          "path": "GATEWAY.IL.I-55",
          "displayName": "I-55"
        },
        {
          "path": "GATEWAY.IL.I-80",
          "displayName": "I-80"
        },
        {
          "path": "GATEWAY.IL.I-90",
          "displayName": "I-90"
        }
      ]
    },
    "IN": {
      "name": "Indiana",
      "expressways": [
        {
          "path": "GATEWAY.IN.I-65",
          "displayName": "I-65"
        },
        {
          "path": "GATEWAY.IN.I-70",
          "displayName": "I-70"
        }
      ]
    },
    "WI": {
      "name": "Wisconsin",
      "expressways": [
        {
          "path": "GATEWAY.WI.I-94",
          "displayName": "I-94"
        }
      ]
    }
  },
  "error": null
}
```

**Usage Notes:**

- The response keys are state abbreviations (e.g., "IL", "IN", "WI")
- Each state object contains `name` (full state name) and `expressways` (list of expressways)
- Derive the list of available states from `Object.keys(data)`
- Get the full state name via `data[stateAbbrev].name`
- Get expressways for a selected state via `data[stateAbbrev].expressways`
- The `path` value is used as the `expressway` parameter for the mileposts endpoint

**React Example:**

```javascript
const [expresswaysByState, setExpresswaysByState] = useState({});
const [states, setStates] = useState([]);

useEffect(() => {
  const loadExpressways = async () => {
    const response = await fetch('https://travelmidwest.com/lmiga/mileposts/expressways.json');
    const result = await response.json();
    
    if (result.success) {
      setExpresswaysByState(result.data);
      // Derive states from the response keys
      setStates(Object.keys(result.data).sort());
    }
  };
  loadExpressways();
}, []);

// Get state name
const getStateName = (stateAbbrev) => {
  return expresswaysByState[stateAbbrev]?.name || stateAbbrev;
};

// Get expressways for selected state
const getExpresswaysForState = (stateAbbrev) => {
  return expresswaysByState[stateAbbrev]?.expressways || [];
};
```

### GET /mileposts/mileposts.json

Returns milepost data for a specific expressway, including cross street information, coordinates, and IDOT district.

**URL:**

```
https://travelmidwest.com/lmiga/mileposts/mileposts.json
```

**Parameters:**

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| expressway | string | Yes | - | Expressway path from `/expressways.json` endpoint (e.g., "GATEWAY.IL.I-90") |
| interval | integer | No | 5 | Milepost interval in miles (1-10) |

**Example Request:**

```
https://travelmidwest.com/lmiga/mileposts/mileposts.json?expressway=GATEWAY.IL.I-90&interval=5
```

**Response:**

```json
{
  "success": true,
  "data": {
    "expressway": "I-90",
    "state": "Illinois",
    "stateAbbrev": "IL",
    "interval": 5,
    "caption": "Mileposts for I-90 in Illinois Within the Travel Midwest Region",
    "mileposts": [
      {
        "milepost": 0.0,
        "crossStreet": "State Line Road",
        "offset": 0.15,
        "municipality": "Chicago",
        "county": "Cook",
        "latitude": 41.9876,
        "longitude": -87.8765,
        "idotDistrict": 1
      },
      {
        "milepost": 5.0,
        "crossStreet": "Cumberland Avenue",
        "offset": 0.08,
        "municipality": "Chicago",
        "county": "Cook",
        "latitude": 41.9901,
        "longitude": -87.8432,
        "idotDistrict": 1
      },
      {
        "milepost": 10.0,
        "crossStreet": "Harlem Avenue",
        "offset": 0.22,
        "municipality": "Schiller Park",
        "county": "Cook",
        "latitude": 41.9923,
        "longitude": -87.8067,
        "idotDistrict": 1
      }
    ]
  },
  "error": null
}
```

**Milepost Object Properties:**

| Property | Type | Description |
| --- | --- | --- |
| milepost | number | Mile marker value (rounded to nearest interval) |
| crossStreet | string | Name of the nearest cross street |
| offset | number | Distance offset from the cross street (in miles) |
| municipality | string | City or municipality name |
| county | string | County name |
| latitude | number or null | Decimal latitude (WGS84), null if unavailable |
| longitude | number or null | Decimal longitude (WGS84), null if unavailable |
| idotDistrict | integer or null | IDOT district number (1-9), null if outside Illinois |

**Notes:**

- The state is automatically extracted from the expressway path (e.g., "GATEWAY.IL.I-90" → "IL")
- Milepost values are rounded to the nearest interval when the error is less than 5%
- Mileposts with error exceeding 5% are excluded from the response
- The `idotDistrict` field is only populated for locations within Illinois

**Validation Error Response:**

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "fieldErrors": {
      "expressway": "Expressway is required",
      "interval": "Interval must be between 1 and 10"
    }
  }
}
```

**React Example:**

```javascript
const fetchMileposts = async (expresswayPath, interval = 5) => {
  const url = new URL('https://travelmidwest.com/lmiga/mileposts/mileposts.json');
  url.searchParams.set('expressway', expresswayPath);
  url.searchParams.set('interval', interval.toString());
  
  const response = await fetch(url);
  const result = await response.json();
  
  if (result.success) {
    const { caption, mileposts } = result.data;
    setCaption(caption);
    setMileposts(mileposts);
  } else {
    // Handle validation errors
    if (result.error.fieldErrors) {
      setFieldErrors(result.error.fieldErrors);
    } else {
      setError(result.error.message);
    }
  }
};
```

## Complete React Integration Example

Below is a complete example of a React component that uses these endpoints to display milepost data:

```javascript
import React, { useState, useEffect } from 'react';

const BASE_URL = 'https://travelmidwest.com/lmiga';

const MilepostViewer = () => {
  const [expresswaysByState, setExpresswaysByState] = useState({});
  const [states, setStates] = useState([]);
  const [mileposts, setMileposts] = useState(null);
  const [selectedState, setSelectedState] = useState('');
  const [selectedExpressway, setSelectedExpressway] = useState('');
  const [interval, setInterval] = useState(5);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Fetch expressways (grouped by state) on mount
  useEffect(() => {
    const loadExpressways = async () => {
      try {
        const response = await fetch(`${BASE_URL}/mileposts/expressways.json`);
        const result = await response.json();
        if (result.success) {
          setExpresswaysByState(result.data);
          setStates(Object.keys(result.data).sort());
        }
      } catch (err) {
        setError('Failed to load expressways');
      }
    };
    loadExpressways();
  }, []);

  // Reset expressway selection when state changes
  useEffect(() => {
    setSelectedExpressway('');
  }, [selectedState]);

  // Get state info for current state
  const currentStateInfo = selectedState ? expresswaysByState[selectedState] : null;
  const currentExpressways = currentStateInfo?.expressways || [];

  // Fetch mileposts
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedExpressway) return;

    setLoading(true);
    setError(null);

    try {
      const url = new URL(`${BASE_URL}/mileposts/mileposts.json`);
      url.searchParams.set('expressway', selectedExpressway);
      url.searchParams.set('interval', interval.toString());

      const response = await fetch(url);
      const result = await response.json();

      if (result.success) {
        setMileposts(result.data);
      } else {
        setError(result.error.message);
      }
    } catch (err) {
      setError('Failed to load mileposts');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="milepost-viewer">
      <form onSubmit={handleSubmit}>
        <select 
          value={selectedState} 
          onChange={(e) => setSelectedState(e.target.value)}
        >
          <option value="">Select State</option>
          {states.map((abbrev) => (
            <option key={abbrev} value={abbrev}>
              {expresswaysByState[abbrev]?.name || abbrev}
            </option>
          ))}
        </select>

        <select 
          value={selectedExpressway} 
          onChange={(e) => setSelectedExpressway(e.target.value)}
          disabled={!selectedState}
        >
          <option value="">Select Expressway</option>
          {currentExpressways.map((exp) => (
            <option key={exp.path} value={exp.path}>
              {exp.displayName}
            </option>
          ))}
        </select>

        <select 
          value={interval} 
          onChange={(e) => setInterval(Number(e.target.value))}
        >
          {[1, 2, 5, 10].map((val) => (
            <option key={val} value={val}>{val} mile interval</option>
          ))}
        </select>

        <button type="submit" disabled={!selectedExpressway || loading}>
          {loading ? 'Loading...' : 'Get Mileposts'}
        </button>
      </form>

      {error && <div className="error">{error}</div>}

      {mileposts && (
        <div className="results">
          <h2>{mileposts.caption}</h2>
          <table>
            <thead>
              <tr>
                <th>Milepost</th>
                <th>Cross Street</th>
                <th>Municipality</th>
                <th>County</th>
                <th>IDOT District</th>
                <th>Coordinates</th>
              </tr>
            </thead>
            <tbody>
              {mileposts.mileposts.map((mp, idx) => (
                <tr key={idx}>
                  <td>{mp.milepost.toFixed(0)}</td>
                  <td>{mp.crossStreet}</td>
                  <td>{mp.municipality}</td>
                  <td>{mp.county}</td>
                  <td>{mp.idotDistrict ?? 'N/A'}</td>
                  <td>
                    {mp.latitude && mp.longitude 
                      ? `${mp.latitude.toFixed(4)}, ${mp.longitude.toFixed(4)}`
                      : 'N/A'}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default MilepostViewer;
```

## TypeScript Interfaces

For TypeScript projects, use these interface definitions:

```typescript
interface ApiResponse<T> {
  success: boolean;
  data: T | null;
  error: ApiError | null;
}

interface ApiError {
  code: string;
  message: string;
  fieldErrors: Record<string, string>;
}

interface StateExpressways {
  name: string;
  expressways: ExpresswayInfo[];
}

interface ExpresswayInfo {
  path: string;
  displayName: string;
}

interface MilepostInfo {
  milepost: number;
  crossStreet: string;
  offset: number;
  municipality: string;
  county: string;
  latitude: number | null;
  longitude: number | null;
  idotDistrict: number | null;
}

interface MilepostResponse {
  expressway: string;
  state: string;
  stateAbbrev: string;
  interval: number;
  caption: string;
  mileposts: MilepostInfo[];
}

// API response types
type ExpresswaysResponse = ApiResponse<Record<string, StateExpressways>>;
type MilepostsResponse = ApiResponse<MilepostResponse>;
```

## Error Handling

| HTTP Status | Error Code | Description |
| --- | --- | --- |
| 400 | VALIDATION_ERROR | Invalid or missing request parameters |
| 401 | UNAUTHORIZED_ERROR | Authentication required (if applicable) |
| 404 | NOT_FOUND | Requested resource not found (invalid expressway path) |
| 500 | ERROR | Internal server error |

Always check the `success` field in the response before accessing `data`.
