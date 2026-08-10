# Admin archive heatmap

> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.

## About

This document provides details on the Real-Time Archive admin API endpoints for retrieving historical traffic flow data, heat maps, and percentile statistics.

The Real-Time Archive API provides access to historical real-time traffic data, including:

- Flow location identifiers for specific road sections
- Speed heat maps throughout a given day
- Aggregated percentile statistics over date ranges

All endpoints use the LocationResolver to parse location query strings and match them to real-time traffic flow identifiers.

## Authentication Requirements

⚠️ **IMPORTANT**: All API endpoints require admin authentication. The application uses cookies for authentication after login. Ensure your requests include credentials to send cookies with cross-origin requests.

## Base URL

All API endpoints are relative to:

```console
/admin/archive/realtime
```

## Available Endpoints

### Get Flow Locations

Retrieves a list of real-time flow identifiers for a given section location in GeoJSON format.

```console
GET /flowLocations.json?query=<location query>
```

**Query Parameters:**

- query (string, required): Location query string that resolves to a section location (e.g., "EB I-290 from Austin to Cicero")

**Response:** (Status Code: 200 OK)

```json
{
  "success": true,
  "data": {
    "type": "FeatureCollection",
    "timestamp": "2025-03-25T15:31:30.000Z",
    "features": [
      {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [-87.9025495, 41.8736984]
        },
        "properties": {
          "flowIdentifier": "107N04207",
          "start": 1308.0238926629218,
          "end": 1477.9053425842214,
          "onRoad": "EB I-290 (Eisenhower Expy)",
          "crossStreet": "Wolf Rd",
          "crossOffset": 0.25,
          "mileMarker": 140.88187128861045
        }
      },
      {
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [-87.9025495, 41.8736984]
        },
        "properties": {
          "flowIdentifier": "107N04283",
          "start": 452.9605135385802,
          "end": 989.0428508867576,
          "onRoad": "EB I-290 (Eisenhower Expy)",
          "crossStreet": "Wolf Rd",
          "crossOffset": 0.25,
          "mileMarker": 140.88187128861045
        }
      }
    ]
  },
  "error": null
}
```

**Error Responses:**

- 400 Bad Request (INVALID_QUERY): Query parameter is required or invalid
- 400 Bad Request (LOCATION_AMBIGUOUS): Location ambiguous, one or both cross streets may appear more than once on the road
- 400 Bad Request (LOCATION_ERROR): Other location resolution error
- 404 Not Found: Location not found
- 500 Internal Server Error: Error resolving location

**Notes:**

- The GeoJSON format includes point geometries for each flow location
- Properties include flow identifier (TMC code), start/end distances, road names, and geographic coordinates
- Multiple flows may be returned for a single location query if the section spans multiple flow segments

### Get Heat Map

Retrieves a heat map of speeds throughout a given day for a specific section location.

```console
GET /heatmap.json?date=<yyyyMMdd>&query=<location query>
```

**Query Parameters:**

- date (string, required): Date in yyyyMMdd format (e.g., "20250325")
- query (string, required): Location query string that resolves to a section location

**Response:** (Status Code: 200 OK)

```json
{
  "success": true,
  "data": {
    "rows": [
      {
        "timestamp": "2025-03-25T00:00:00.000Z",
        "speeds": [55.3, 58.7, 52.1],
        "travelTime": 8.5
      },
      {
        "timestamp": "2025-03-25T00:05:00.000Z",
        "speeds": [54.8, 57.2, 51.9],
        "travelTime": 8.7
      }
    ],
    "locations": [
      {
        "tmc": "107N04207",
        "onRoad": "EB I-290 (Eisenhower Expy)",
        "crossStreet": "Wolf Rd",
        "crossOffset": 0.25,
        "latitude": 41.8736984,
        "longitude": -87.9025495,
        "startMileMarker": 140.88,
        "endMileMarker": 141.15
      },
      {
        "tmc": "107N04283",
        "onRoad": "EB I-290 (Eisenhower Expy)",
        "crossStreet": "Cicero Ave",
        "crossOffset": 0.0,
        "latitude": 41.8745123,
        "longitude": -87.8925432,
        "startMileMarker": 141.15,
        "endMileMarker": 141.42
      }
    ]
  },
  "error": null
}
```

**Error Responses:**

- 400 Bad Request (LOCATION_AMBIGUOUS): Location ambiguous
- 400 Bad Request (LOCATION_ERROR): Location resolution error
- 404 Not Found: Location not found
- 500 Internal Server Error: Error generating heatmap or heat map is initializing

**Notes:**

- Each row represents a time period (typically 5-minute intervals) throughout the day
- The `speeds` array contains speeds for each location in the order they appear in the `locations` array
- `travelTime` is the total travel time across all locations for that time period (in minutes)
- Speeds are in miles per hour (mph)
- Mile markers and cross offsets are in miles

### Get Percentile Data

Retrieves aggregated percentile statistics over a date range for a specific section location.

```console
GET /percentile.json?startDate=<yyyyMMdd>&endDate=<yyyyMMdd>&query=<location query>
```

**Query Parameters:**

- startDate (string, required): Start date in yyyyMMdd format (e.g., "20250301")
- endDate (string, required): End date in yyyyMMdd format (e.g., "20250331")
- query (string, required): Location query string that resolves to a section location

**Response:** (Status Code: 200 OK)

```json
{
  "success": true,
  "data": {
    "startDate": "2025-03-01",
    "endDate": "2025-03-31",
    "timesOfDay": [
      "00:00:00",
      "00:05:00",
      "00:10:00"
    ],
    "rows": [
      {
        "timeOfDay": "00:00:00",
        "locationStatistics": [
          {
            "count": 31,
            "average": 55.3,
            "stddev": 3.2,
            "tenthPercentile": 50.1,
            "twentiethPercentile": 51.8,
            "eightiethPercentile": 58.9,
            "ninetiethPercentile": 60.2,
            "minimum": 47.5,
            "maximum": 62.3,
            "median": 55.0
          },
          {
            "count": 31,
            "average": 57.8,
            "stddev": 2.9,
            "tenthPercentile": 53.2,
            "twentiethPercentile": 54.7,
            "eightiethPercentile": 60.5,
            "ninetiethPercentile": 61.8,
            "minimum": 50.1,
            "maximum": 64.2,
            "median": 57.5
          }
        ],
        "travelTimeStats": {
          "count": 31,
          "average": 8.5,
          "stddev": 0.8,
          "tenthPercentile": 7.2,
          "twentiethPercentile": 7.6,
          "eightiethPercentile": 9.3,
          "ninetiethPercentile": 9.8,
          "minimum": 6.8,
          "maximum": 10.5,
          "median": 8.4
        }
      }
    ],
    "locations": [
      {
        "tmc": "107N04207",
        "onRoad": "EB I-290 (Eisenhower Expy)",
        "crossStreet": "Wolf Rd",
        "crossOffset": 0.25,
        "latitude": 41.8736984,
        "longitude": -87.9025495,
        "startMileMarker": 140.88,
        "endMileMarker": 141.15
      },
      {
        "tmc": "107N04283",
        "onRoad": "EB I-290 (Eisenhower Expy)",
        "crossStreet": "Cicero Ave",
        "crossOffset": 0.0,
        "latitude": 41.8745123,
        "longitude": -87.8925432,
        "startMileMarker": 141.15,
        "endMileMarker": 141.42
      }
    ]
  },
  "error": null
}
```

**Error Responses:**

- 400 Bad Request (LOCATION_AMBIGUOUS): Location ambiguous
- 400 Bad Request (LOCATION_ERROR): Location resolution error
- 404 Not Found: Location not found
- 500 Internal Server Error: Error generating percentile data

**Notes:**

- Statistics are calculated across all days in the date range for each time-of-day period
- Each row corresponds to a specific time of day (e.g., midnight, 12:05 AM, 12:10 AM)
- `locationStatistics` array contains statistics for each location, in the order they appear in the `locations` array
- `travelTimeStats` contains aggregated travel time statistics across all locations
- All speed statistics are in miles per hour (mph)
- Travel time statistics are in minutes
- `count` indicates the number of data points used to calculate the statistics

## Data Types

### Location Query Format

Location queries use the LocationResolver syntax to specify road sections. Examples:

- "EB I-290 from Austin to Cicero"
- "WB I-90 at Wolf Rd"
- "NB US-41 from Grand Ave to Division St"

### Date Format

Date parameters use the yyyyMMdd format:

- Example: "20250325" for March 25, 2025

### GeoJSON Format

Flow locations are returned as GeoJSON FeatureCollection with Point geometries.

### Statistics Fields

Both LocationStatistics and TravelTimeStatistics include:

- count: Number of data points
- average: Mean value
- stddev: Standard deviation
- tenthPercentile: 10th percentile
- twentiethPercentile: 20th percentile
- eightiethPercentile: 80th percentile
- ninetiethPercentile: 90th percentile
- minimum: Minimum value
- maximum: Maximum value
- median: 50th percentile (median)

## Example Usage with React

```javascript
// Example: Fetching flow locations for a road section
const fetchFlowLocations = async (locationQuery) => {
  try {
    const params = new URLSearchParams({ query: locationQuery });
    const response = await fetch(
      `https://travelmidwest.com/admin/archive/realtime/flowLocations.json?${params}`,
      {
        credentials: 'include', // Important: includes cookies with the request
      }
    );
    
    if (!response.ok) {
      throw new Error('Failed to fetch flow locations');
    }
    
    const result = await response.json();
    if (result.success) {
      const features = result.data.features;
      console.log(`Found ${features.length} flow locations`);
      setFlowLocations(features);
    }
  } catch (error) {
    console.error('Error fetching flow locations:', error);
  }
};

// Example: Fetching heat map for a specific date and location
const fetchHeatMap = async (date, locationQuery) => {
  try {
    const params = new URLSearchParams({
      date: date, // format: "20250325"
      query: locationQuery
    });
    
    const response = await fetch(
      `https://travelmidwest.com/admin/archive/realtime/heatmap.json?${params}`,
      {
        credentials: 'include',
      }
    );
    
    if (!response.ok) {
      throw new Error('Failed to fetch heat map');
    }
    
    const result = await response.json();
    if (result.success) {
      const { rows, locations } = result.data;
      console.log(`Heat map has ${rows.length} time periods and ${locations.length} locations`);
      setHeatMapData(result.data);
    }
  } catch (error) {
    console.error('Error fetching heat map:', error);
  }
};

// Example: Fetching percentile data over a date range
const fetchPercentileData = async (startDate, endDate, locationQuery) => {
  try {
    const params = new URLSearchParams({
      startDate: startDate, // format: "20250301"
      endDate: endDate,     // format: "20250331"
      query: locationQuery
    });
    
    const response = await fetch(
      `https://travelmidwest.com/admin/archive/realtime/percentile.json?${params}`,
      {
        credentials: 'include',
      }
    );
    
    if (!response.ok) {
      throw new Error('Failed to fetch percentile data');
    }
    
    const result = await response.json();
    if (result.success) {
      const { startDate, endDate, rows, locations } = result.data;
      console.log(`Percentile data from ${startDate} to ${endDate}`);
      console.log(`${rows.length} time periods, ${locations.length} locations`);
      setPercentileData(result.data);
    }
  } catch (error) {
    console.error('Error fetching percentile data:', error);
  }
};

// Example: Processing percentile statistics
const analyzePercentileData = (percentileData) => {
  percentileData.rows.forEach((row, index) => {
    const timeOfDay = percentileData.timesOfDay[index];
    
    // Analyze each location
    row.locationStatistics.forEach((stats, locationIndex) => {
      const location = percentileData.locations[locationIndex];
      console.log(`${timeOfDay} at ${location.onRoad} near ${location.crossStreet}:`);
      console.log(`  Average speed: ${stats.average?.toFixed(1)} mph`);
      console.log(`  Median speed: ${stats.median?.toFixed(1)} mph`);
      console.log(`  20th percentile: ${stats.twentiethPercentile?.toFixed(1)} mph`);
      console.log(`  80th percentile: ${stats.eightiethPercentile?.toFixed(1)} mph`);
    });
    
    // Analyze travel time
    const ttStats = row.travelTimeStats;
    console.log(`${timeOfDay} travel time:`);
    console.log(`  Average: ${ttStats.average?.toFixed(1)} minutes`);
    console.log(`  Median: ${ttStats.median?.toFixed(1)} minutes`);
  });
};
```

## Common Location Query Examples

```console
// Chicago area highways
"EB I-290 from Austin to Cicero"
"WB I-90 from O'Hare to Downtown"
"NB I-94 at 95th St"

// With specific cross streets
"SB US-41 from Grand Ave to Division St"
"EB I-88 at Route 83"

// Milwaukee area
"WB I-94 from 27th St to 16th St"
"NB US-45 at Capitol Dr"
```

## Technical Details

### Location Resolution

- The API uses LocationResolver to parse natural language location queries
- Queries must resolve to section locations (road segments between two points)
- The system matches query sections with real-time traffic flow identifiers (TMC codes)
- Flows are filtered by lane type (ramp vs. mainline) to match the query section type

### Heat Map Data

- Heat maps show speed data in 5-minute intervals throughout a 24-hour period
- Each row represents one time interval
- Speeds array corresponds to locations in the same order as the locations array
- Travel time is calculated across all locations for the entire section

### Percentile Calculations

- Statistics are calculated by aggregating data across all days in the date range
- For each time-of-day (e.g., 3:00 PM), values from all days are collected
- Percentiles are calculated using Apache Commons Math DescriptiveStatistics
- Null, NaN, and infinite values are excluded from calculations

### Response Format

All responses follow the standardized API response format:

```json
{
  "success": true/false,
  "data": { /* response data */ },
  "error": { /* error details if success is false */ }
}
```

## Contact

For any questions or issues related to this API, please contact [dev@travelmidwest.com](mailto:dev@travelmidwest.com?subject=Real-Time%20Archive%20Admin%20API%20Documentation).
