# GTIS API Documentation

Public documentation for the **Gateway Traffic Information System** (GTIS), the traffic
data platform behind [travelmidwest.com](https://travelmidwest.com). GTIS aggregates
real-time traffic information — travel times, incidents, construction, dynamic message
signs, cameras, truck parking and weather — from transportation agencies across
Illinois and neighbouring states, and republishes it through the APIs documented here.

> [!NOTE]
> The APIs described here, and the data they serve, may change at any time without
> notice. We cannot guarantee their availability or their suitability for use in
> third-party applications.

## Contents

### [Gateway API](gateway-api/README.md)

JSON and GeoJSON endpoints serving live traffic data — travel times, incidents, cameras, dynamic message signs, work zones, truck parking and more.

- [Admin](gateway-api/admin/README.md) — Privileged endpoints for administering GTIS content and user accounts.
- [Announcements](gateway-api/announcements.md)
- [Chicago Quick Traffic](gateway-api/chicago-quick-traffic.md)
- [IDOT Incidents](gateway-api/idot-incidents.md)
- [Locate City](gateway-api/locate-city.md)
- [Map Data](gateway-api/map-data.md)
- [Message Alerts](gateway-api/message-alerts.md)
- [Mileposts](gateway-api/mileposts.md)
- [Projects](gateway-api/projects.md)
- [Report Data](gateway-api/report-data.md)
- [Show Camera](gateway-api/show-camera.md)
- [Travel Time Statistics Graph](gateway-api/travel-time-statistics-graph.md)
- [Truck Parking Reports](gateway-api/truck-parking-reports.md)
- [Trucker Reports](gateway-api/trucker-reports.md)
- [User API](gateway-api/user-api/README.md) — Account and authentication endpoints for the various kinds of GTIS user.
- [Work Zone Data Exchange (WZDx)](gateway-api/work-zone-data-exchange.md)

### [Work Zone Data Exchange (WZDx)](gateway-api/work-zone-data-exchange.md)

GTIS ingests [WZDx](https://github.com/usdot-jpo-ode/wzdx) feeds from the Illinois Tollway
and WisDOT, converts its own roadwork database to WZDx, and republishes the result through
three endpoints:

- **constructionWzdxMap.json** — GTIS roadwork and ingested WZDx together, as map-ready GeoJSON.
- **wzdxData.json** — the combined work zone feed in WZDx document format.
- **illinoisWzdx.json** — the Illinois-only subset published to the Trihydro SDX.

See [Work Zone Data Exchange](gateway-api/work-zone-data-exchange.md) for request
parameters, response fields and examples.

### [User Guides and Manuals](user-guides-and-manuals/README.md)

Longer-form guides for publishing data to, and receiving data from, the Gateway.

- [Camera Upload Manual](user-guides-and-manuals/camera-upload-manual.md)
- [Gateway External Interface User Guide](user-guides-and-manuals/gateway-external-interface-user-guide/README.md)
- [Gateway Traffic Data Archive](user-guides-and-manuals/gateway-traffic-data-archive.md)
- [GTIS Smart Work Zone Specifications for Construction Contractors and Vendors](user-guides-and-manuals/gtis-smart-work-zone-specifications.md)
- [XML and Camera Image Download Manual](user-guides-and-manuals/xml-and-camera-image-download-manual.md)

### Feeds and Reference

Flat-file feeds and standalone reference documents.

- [cameraInfo.csv](camera-info-csv.md)
- [dmsInfo.csv](dms-info-csv.md)
- [incidentInfo.csv](incident-info-csv.md)
- [RSS Feeds](rss-feeds.md)
- [travelTimeService.json](travel-time-service-json.md)
- [XML Upload Manual](xml-upload-manual.md)

---

These documents were migrated from the internal GTIS wiki. This repository is now the
authoritative copy — please open a pull request here rather than editing the wiki.
