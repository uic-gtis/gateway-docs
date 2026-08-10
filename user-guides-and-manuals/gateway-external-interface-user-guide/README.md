# Gateway External Interface User Guide

## Intended Audience

This document is intended for:

- Registered traffic information access users.
- ITS agencies that wish to communicate with the Gateway.
- Members of various design groups that have development responsibility for the Gateway ITS and for other ITS projects within the Corridor.
- Members of the Gateway design and development team.
- Other parties who may be contemplating the design of a similar ITS infrastructure.

## Contents

- [Introduction](introduction.md) — the Gateway project and the nature of this document.
- [Gateway Interface Specifications](gateway-interface-specifications.md) — Gateway connectivity requirements: the use of XML and JSON technologies, Gateway data standards, and publish and subscribe protocols. Covers the use of Data Source Interfaces (DSI) to connect to the Gateway, the ultimate use of agency servers and the security considerations involved, and includes a basic primer on IDL statements.
- [Locations](locations.md) — the Gateway specifications for roadway locations. Location specifications are the basis of the device reports, incident reports, scheduled event reports and traffic reports set out in the rest of the guide.
- [Device Station Reports](device-station-reports.md) — field device reports, including Vehicle Detector Station, Weather Sensor Station, Dynamic Message Sign and Highway Advisory Radio reports.
- [Roadway Events](roadway-events.md) — the roadway event reports: Incident Reports, and the scheduled events covered by Roadwork Reports and Special Event Reports.
- [Traffic Reports](traffic-reports.md) — Congestion Reports and general Traffic Reports.
- [Publishing Data to the Gateway](publishing-data-to-the-gateway.md) — how to publish data to the Gateway, with demo clients, schemas, validation rules and troubleshooting.
- [Receiving Data from the Gateway](receiving-data-from-the-gateway.md) — the reports offered as services of the Gateway.
- [Versions](versions.md) — interface version history.
- [Gateway XML Reference](gateway-xml-reference.md) — the XML schema for each of the Gateway traffic reports.

## Related Documents

The following documents provide more details on uploading and downloading traffic information to/from the GTIS in XML and JSON formats:

- [Online Traffic Information Access Registration Form](https://go.travelmidwest.com/register)
- [XML Upload Manual](../../xml-upload-manual.md)
- [XML and Camera Image Download Manual](../xml-and-camera-image-download-manual.md)
- [JSON Traffic Information Download Manual](../../gateway-api/README.md)
- [Camera Meta-Data (cameraInfo.csv)](../../camera-info-csv.md)
- [travelTimeService.json](../../travel-time-service-json.md)
