# GTIS Smart Work Zone Specifications for Construction Contractors and Vendors

## Introduction

The **Gateway Traveler Information System (GTIS)**, and its associated website [TravelMidwest.com](https://TravelMidwest.com), support one standard and two proprietary smart work zone data formats. Vendors who wish to integrate smart work zone devices with the GTIS should follow the protocols and procedures in this document to ensure compatibility. Vendors can contact [support@travelmidwest.com](mailto:support@travelmidwest.com?subject=GTIS%20Smart%20Work%20Zone) for additional assistance with integration.

## Devices Supported

The GTIS supports integration with the following types of smart work zone devices:

- CCTV cameras
- Variable message signs
- Speed detectors

After integration, these devices will appear on [TravelMidwest.com](https://www.TravelMidwest.com).

## Supported Integration Methods

The GTIS can receive smart work zone data in a number of ways such as:

- Upload to TravelMidwest.com using GTIS formatted files,
- Upload to JamLogic, or
- Upload to iConeTraffic.

Each of these integration methods is discussed below.

### Upload to TravelMidwest.com

XML upload to TravelMidwest.com requires an approved account along with its username and password (see the [XML Upload Manual](../xml-upload-manual.md) for details). This is the recommended integration method because it ensures the vendor has complete control over the data being transmitted.

### Upload to JamLogic

JamLogic can be used to integrate CCTV cameras, variable message signs, and speed detectors. The GTIS supports JamLogic's XML file format. The vendor should contact Ver-Mac or JamLogic to initiate this integration method:

- Contact [support@travelmidwest.com](mailto:support@travelmidwest.com?subject=GTIS%20Smart%20Work%20Zone%20%2F%20JamLogic) and the GTIS team will put you in touch with the vendor.

The XML format specification was published at
`https://www.jamlogic.com/download/XML+Secure+Interface/`, which no longer resolves.
Request the current specification from [JamLogic](https://www.jamlogic.com/).

Once the vendor has established an XML feed through JamLogic using their XML format specification, [support@travelmidwest.com](mailto:support@travelmidwest.com?subject=GTIS%20Smart%20Work%20Zone%20%2F%20JamLogic%20XML%20file) should be contacted and provided the XML file URL. The URL takes the form `https://public.jamlogic.com/WorkZoneFeed/secure/<feed code>`, where the feed code identifies your feed.

### Upload to iConeTraffic

iConeTraffic.com has extended Waze's XML event format to support smart work zone devices. For documentation on the iConeTraffic.com file format:

- [https://developers.google.com/waze/data-feed/incident-information](https://developers.google.com/waze/data-feed/incident-information)
- [https://gstatic.com/road-incidents/incidents_feed.xsd](https://gstatic.com/road-incidents/incidents_feed.xsd)

The GTIS is integrated with IconeTraffic.com and supports automatic download of construction events and smart work zone devices from iConeTraffic.com. To initiate this integration method, the vendor should contact:

- Contact [support@travelmidwest.com](mailto:support@travelmidwest.com?subject=GTIS%20Smart%20Work%20Zone%20%2F%20iConeTraffic) and the GTIS team will put you in touch with the vendor.
