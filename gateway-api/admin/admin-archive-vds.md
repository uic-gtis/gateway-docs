# Admin archive VDS

> [!IMPORTANT]
> **Administrative API — not part of the public GTIS API surface.**
> These endpoints require a privileged operator or administrator role. They are
> documented for internal and partner-integrator use and are not available to general
> API consumers.

## About

This document provides details on the VDS (Vehicle Detection System) Archive admin API endpoints for integration with the React front-end application.

## Authentication Requirements

⚠️ **IMPORTANT**: All API endpoints require admin authentication. The application uses cookies for authentication after login. Ensure your requests include credentials to send cookies with cross-origin requests.

## Base URL

```console
/admin/archive/vds
```

## Overview

The VDS Archive API serves as a proxy to internal VDS archive services, providing access to historical Vehicle Detection System location and traffic data. The API handles timeouts and error responses from the archive services and returns standardized API responses.

## Available Endpoints

### Get VDS Locations

Retrieves all VDS (Vehicle Detection System) sensor locations from the archive service for the current date.

```console
GET /locations.json
```

**Query Parameters:**

- None

**Response:** (Status Code: 200 OK)

```json
{
  "success": true,
  "data": {
    "date": "2025-03-25",
    "fileTimestamp": "2025-03-25T14:30:00.000Z",
    "locations": [
      {
        "fieldDeviceId": "IL-IDOT-001",
        "location": "EB I-90 at Wolf Rd"
      },
      {
        "fieldDeviceId": "IL-IDOT-002",
        "location": "WB I-94 at Harlem Ave"
      },
      {
        "fieldDeviceId": "IL-IDOT-003",
        "location": "NB I-294 at 95th St"
      }
    ]
  }
}
```

**Error Responses:**

- 500 Internal Server Error: If unable to connect to archive service

**Notes:**

- Returns the most recent VDS locations for today's date
- Each location includes a fieldDeviceId in the format: [state]-[sourcename]-[sourceid]
- Location is a human-readable string describing the sensor position
- This endpoint proxies requests to the VDS archive service
- Connection timeout is set to 10 seconds

### Get VDS Data

Retrieves detailed VDS traffic data from the archive service for a specific device and date.

```console
GET /data.json?fieldDeviceId=[id]&date=[yyyy-MM-dd]&page=[number]&size=[count]&sort=[ASC|DESC]
```

**Query Parameters:**

- fieldDeviceId (string, required): VDS sensor identifier (e.g., "IL-IDOT-001")
- date (string, required): Date in yyyy-MM-dd format (e.g., "2025-03-25")
- page (number, optional): Page number for pagination, defaults to 0
- size (number, optional): Number of records per page, defaults to 288 (one day at 5-minute intervals)
- sort (string, optional): Sort order - "ASC" or "DESC"

**Response:** (Status Code: 200 OK)

```json
{
  "success": true,
  "data": {
    "content": [
      {
        "fieldDeviceId": "IL-IDOT-001",
        "lastUpdateTime": 1711377000000,
        "filename": "vds_20250325_143000.xml",
        "fileTimestamp": 1711377000000,
        "working": true,
        "onRoad": {
          "prefix": "",
          "roadName": "I-90",
          "suffix": "",
          "streetType": "Expy"
        },
        "crossRoad": {
          "prefix": "",
          "roadName": "Wolf",
          "suffix": "",
          "streetType": "Rd"
        },
        "crossOffset": 150.5,
        "latitude": 41.85003,
        "longitude": -87.65005,
        "speed": 24.58,
        "occupancy": 0.125,
        "volume": 1850,
        "direction": "EB",
        "mileMarker": 45.2,
        "fips": {
          "stateCode": "17",
          "countyCode": "031",
          "cityCode": "14000"
        }
      }
    ],
    "pageable": {
      "pageNumber": 0,
      "pageSize": 288,
      "sort": {
        "sorted": false,
        "unsorted": true
      }
    },
    "totalPages": 1,
    "totalElements": 288,
    "last": true,
    "first": true,
    "numberOfElements": 288,
    "size": 288,
    "number": 0
  }
}
```

**Field Descriptions:**

- fieldDeviceId: Device identifier in format [state]-[sourcename]-[sourceid]
- lastUpdateTime: Timestamp in milliseconds since epoch
- filename: Source filename of the VDS data
- fileTimestamp: File timestamp in milliseconds since epoch
- working: Boolean indicating if the sensor is operational
- onRoad: Road name components where sensor is located
- crossRoad: Cross street name components
- crossOffset: Distance from cross street in meters
- latitude: Sensor latitude in decimal degrees
- longitude: Sensor longitude in decimal degrees
- speed: Average speed in meters per second (m/s)
- occupancy: Lane occupancy as a decimal from 0.00 to 1.00
- volume: Vehicle count in vehicles per lane per hour
- direction: Cardinal direction (EB, WB, SB, NB, etc.)
- mileMarker: Mile marker in miles
- fips: Federal Information Processing Standard codes for location

**Error Responses:**

- 500 Internal Server Error: If unable to connect to archive service

**Notes:**

- This endpoint proxies requests to the VDS archive service
- Query parameters are passed through to the archive service
- Connection timeout is set to 10 seconds
- Returns paginated data in Spring Data Page format
- Default page size of 288 provides roughly one day of data at 5-minute intervals
- Speed values are in m/s (multiply by 2.237 to convert to mph)
- Occupancy values range from 0.0 (empty) to 1.0 (fully occupied)
- Volume represents hourly rate per lane

### Get VDS Report

Retrieves VDS report data from the report archive service based on query parameters.

```console
GET /report.json?[queryParameters]
```

**Query Parameters:**

- All query parameters are forwarded to the report archive service
- Typical parameters may include:
- vdsId (string): VDS sensor identifier or list of identifiers
- startDate (string): Start date for report (format: yyyyMMdd)
- endDate (string): End date for report (format: yyyyMMdd)
- reportType (string): Type of report (e.g., "daily", "weekly", "monthly")
- aggregation (string): Aggregation method (e.g., "average", "sum", "percentile")

**Response:** (Status Code: 200 OK)

```json
{
  "success": true,
  "data": {
    "reportType": "daily",
    "startDate": "2025-03-01",
    "endDate": "2025-03-31",
    "vdsLocations": [
      {
        "vdsId": "IL-IDOT-001",
        "name": "I-90 EB at Mile 45.2",
        "route": "I-90",
        "direction": "Eastbound"
      }
    ],
    "summary": {
      "totalVolume": 1250000,
      "averageSpeed": 25.4,
      "averageOccupancy": 0.123,
      "peakHourVolume": 2150,
      "peakHour": "17:00"
    },
    "dailyData": [
      {
        "date": "2025-03-01",
        "totalVolume": 42000,
        "averageSpeed": 25.6,
        "averageOccupancy": 0.119,
        "peakHourVolume": 2100
      },
      {
        "date": "2025-03-02",
        "totalVolume": 39500,
        "averageSpeed": 25.3,
        "averageOccupancy": 0.125,
        "peakHourVolume": 1980
      }
    ]
  }
}
```

**Error Responses:**

- 500 Internal Server Error: If unable to connect to report archive service

**Notes:**

- This endpoint proxies requests to the report archive service (separate from the VDS data service)
- Query parameters are passed through to the report service
- Connection timeout is set to 10 seconds
- Returns aggregated and summarized data suitable for reporting
- Report format may vary based on reportType parameter

## Data Types

### Field Device ID Format

VDS sensors use a standardized identifier format:

```console
[state]-[sourcename]-[sourceid]
```

Examples:

- IL-IDOT-001
- WI-DOT-255
- IN-INDOT-042

### VDS Metrics

VDS sensors measure three primary metrics:

- **Speed**: Average speed in meters per second (m/s)
- To convert to mph: multiply by 2.237
- To convert to km/h: multiply by 3.6
- **Occupancy**: Percentage of time the detection zone is occupied
- Decimal value from 0.00 (empty) to 1.00 (fully occupied)
- Example: 0.125 = 12.5% occupancy
- **Volume**: Number of vehicles detected per lane per hour
- Hourly rate regardless of measurement interval
- Example: 1850 vehicles/lane/hour

### Date Formats

**ISO 8601 Format** (for timestamps):

- Example: "2025-03-25T14:30:00.000Z"

**LocalDate Format** (for date parameter):

- Example: "2025-03-25"

**Compact Format** (for report endpoints):

- Example: "20250325"

### Road Name Structure

Road names are broken into components:

```json
{
  "prefix": "",
  "roadName": "I-90",
  "suffix": "",
  "streetType": "Expy"
}
```

### FIPS Codes

Federal Information Processing Standard codes identify geographic locations:

```json
{
  "stateCode": "17",
  "countyCode": "031",
  "cityCode": "14000"
}
```

## Example Usage with React

```javascript
// Example: Fetching VDS locations
const fetchVdsLocations = async () => {
  try {
    const response = await fetch('https://travelmidwest.com/admin/archive/vds/locations.json', {
      credentials: 'include', // Important: includes cookies with the request
    });
    
    if (!response.ok) {
      throw new Error('Failed to fetch VDS locations');
    }
    
    const result = await response.json();
    if (result.success) {
      const { date, fileTimestamp, locations } = result.data;
      console.log(`Found ${locations.length} VDS locations for ${date}`);
      setLocations(locations);
    }
  } catch (error) {
    console.error('Error fetching VDS locations:', error);
  }
};

// Example: Fetching VDS data for a specific device and date
const fetchVdsData = async (fieldDeviceId, date, pageSize = 288) => {
  try {
    const params = new URLSearchParams({
      fieldDeviceId: fieldDeviceId,
      date: date,  // format: "2025-03-25"
      page: '0',
      size: pageSize.toString(),
      sort: 'ASC'
    });
    
    const response = await fetch(
      `https://travelmidwest.com/admin/archive/vds/data.json?${params}`,
      {
        credentials: 'include', // Important: includes cookies with the request
      }
    );
    
    if (!response.ok) {
      throw new Error('Failed to fetch VDS data');
    }
    
    const result = await response.json();
    if (result.success) {
      const pageData = result.data;
      console.log(`Retrieved ${pageData.numberOfElements} records`);
      setVdsData(pageData.content);
    }
  } catch (error) {
    console.error('Error fetching VDS data:', error);
  }
};

// Example: Fetching VDS report
const fetchVdsReport = async (vdsId, startDate, endDate, reportType = 'daily') => {
  try {
    const params = new URLSearchParams({
      vdsId: vdsId,
      startDate: startDate,  // format: "20250301"
      endDate: endDate,      // format: "20250331"
      reportType: reportType,
      aggregation: 'average'
    });
    
    const response = await fetch(
      `https://travelmidwest.com/admin/archive/vds/report.json?${params}`,
      {
        credentials: 'include', // Important: includes cookies with the request
      }
    );
    
    if (!response.ok) {
      throw new Error('Failed to fetch VDS report');
    }
    
    const result = await response.json();
    if (result.success) {
      setReportData(result.data);
    }
  } catch (error) {
    console.error('Error fetching VDS report:', error);
  }
};

// Example: Converting speed from m/s to mph
const convertSpeed = (speedMps) => {
  return {
    mph: (speedMps * 2.237).toFixed(1),
    kmh: (speedMps * 3.6).toFixed(1)
  };
};

// Example: Processing VDS data for visualization
const processVdsDataForChart = (vdsData) => {
  return vdsData.map(record => ({
    timestamp: new Date(record.fileTimestamp),
    speedMph: record.speed * 2.237,
    occupancyPercent: record.occupancy * 100,
    volume: record.volume,
    working: record.working
  }));
};

// Example: Filtering out non-working sensors
const getWorkingSensors = (vdsData) => {
  return vdsData.filter(record => record.working);
};

// Example: Calculating average metrics from VDS data
const calculateAverageMetrics = (vdsData) => {
  const workingData = vdsData.filter(record => record.working);
  
  if (workingData.length === 0) {
    return null;
  }
  
  const totalSpeed = workingData.reduce((sum, record) => sum + record.speed, 0);
  const totalOccupancy = workingData.reduce((sum, record) => sum + record.occupancy, 0);
  const totalVolume = workingData.reduce((sum, record) => sum + record.volume, 0);
  
  return {
    averageSpeedMph: ((totalSpeed / workingData.length) * 2.237).toFixed(1),
    averageOccupancyPercent: ((totalOccupancy / workingData.length) * 100).toFixed(1),
    averageVolume: Math.round(totalVolume / workingData.length),
    recordCount: workingData.length
  };
};

// Example: Formatting location string
const formatLocation = (vdsRecord) => {
  const { direction, onRoad, crossRoad } = vdsRecord;
  return `${direction} ${onRoad.roadName} ${onRoad.streetType} at ${crossRoad.roadName} ${crossRoad.streetType}`;
};
```

## Technical Details

### Archive Services

- VDS data archive service URL: `http://archive.tsc.travelmidwest.com:8090/`
- Report archive service URL: `http://archive.tsc.travelmidwest.com:8120/`
- Connection timeout: 10 seconds
- Socket timeout: 10 seconds

### Data Collection

- VDS sensors collect traffic data at regular intervals (typically 20-30 seconds)
- Data includes per-lane measurements of speed, occupancy, and volume
- Historical data is aggregated and archived for analysis and reporting
- The archive service stores data in Cassandra for efficient time-series queries

### Pagination

- The `/data.json` endpoint returns paginated results using Spring Data Page format
- Default page size is 288, which provides approximately 24 hours of data at 5-minute intervals
- Page numbers start at 0
- Total pages and elements are included in the response

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

For any questions or issues related to this API, please contact [dev@travelmidwest.com](mailto:dev@travelmidwest.com?subject=VDS%20Archive%20Admin%20API%20Documentation).
