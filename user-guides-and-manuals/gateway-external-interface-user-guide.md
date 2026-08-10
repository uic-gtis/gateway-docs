# Gateway External Interface User Guide

## Preamble

### Intended Audience

This document is intended for:

- Registered traffic information access users.
- ITS agencies that wish to communicate with the Gateway.
- Members of various design groups that have development responsibility for the Gateway ITS and for other ITS projects within the Corridor.
- Members of the Gateway design and development team.
- Other parties who may be contemplating the design of a similar ITS infrastructure.

### Document Organization

This document is divided into ten sections:

1. *(this page)*
1. Provides an introduction to the Gateway project and the nature of this document.
1. Discusses Gateway connectivity requirements: The use of XML and JSON technologies, Gateway data standards and publish and subscribe protocols are explained for Gateway users. The present use of Data Source Interfaces (DSI) to connect to the Gateway is discussed in this context, and the ultimate use of agency servers, along with the security considerations involved, is discussed. A basic primer of IDL statements in included.
1. Explains the Gateway specifications for roadway locations. Location specifications are a basis of device reports, incident reports, scheduled event reports, and traffic reports set out in the remainder of the document.
1. Sets out the Gateway specifications for field device reports, including Vehicle Detector Station Reports, Weather Sensor Station Reports, Dynamic Message Sign Reports, and Highway Advisory Radio Reports.
1. Provides a discussion of the roadway event reports offered by the Gateway including Incident Reports, Roadwork Reports, and Special Event Reports.
1. Sets out the nature of the Gateway traffic reports, including Congestion Reports and general Traffic Reports.
1. Explains how to publish data to the Gateway.
1. Sets out a list of the reports offered as services of the Gateway.
1. Documents the XML schema for the various Gateway traffic reports.

### Related Documents

The following documents provide more details on uploading and downloading traffic information to/from the GTIS in XML and JSON formats:

- [Online Traffic Information Access Registration Form](https://go.travelmidwest.com/register)
- [XML Upload Manual](../xml-upload-manual.md)
- [XML and Camera Image Download Manual](xml-and-camera-image-download-manual.md)
- [JSON Traffic Information Download Manual](../gateway-api/README.md)
- [Camera Meta-Data (cameraInfo.csv)](../camera-info-csv.md)
- [travelTimeService.json](../travel-time-service-json.md)

## Introduction

The **Gateway Traveler Information System (GTIS)** is an integrated information system that serves the information needs of operating agencies and travelers within its operating area. The Gateway collects dynamic and static transportation data from the distributed transportation management systems throughout the Corridor through their respective regional hubs. The Gateway compiles and coordinates this data to create a single source of transportation information. The Gateway presents this information directly to the various operating agencies through their respective regional systems, and to travelers through Information Service Providers and the Internet via TravelMidwest.com.

The successful provision of these services requires that operating agencies and information service providers adhere to standards of form and content to prevent ambiguities and facilitate the fusion of data from various sources into usable data from which messages for various kinds of subscribers can be constructed. The reception of information from the Gateway by subscribing information service providers likewise requires recognition of Gateway standards.

The standards are made as broad as possible and encompass all or most of the natural ways of conveying the information for which the Gateway was designed. As such, as little burden as possible is imposed on users adhering to the standard. In addition, the standards are consistent with national standards, insuring data interoperability with existing and future standard systems.

This User Guide provides an explanation and guide to the requirements that may be met in different ways by operating agencies and information providers with varying capabilities to provide data to and accept distributions of information from the Gateway Traveler Information System.

### Project History

*(Readers already familiar with the nature of the Gateway and its services may skip this section.)*

The GTIS has a long history of serving as a central travel information repository. The GTIS continues to collect and process data from embedded in-roadway sensors, above-roadway sensors, as well as many types of vehicle sensors, and sends this data to [TravelMidwest.com](https://travelmidwest.com/) for distribution to the motorist.

#### Gary-Chicago-Milwaukee Intelligent Transportation System Priority Corridor

The GCM Intelligent Transportation System (ITS) Priority Corridor undertook many important projects that have improved traffic operations within the region. With the re-designation of the former Gary-Chicago-Milwaukee (GCM) Corridor as the Lake Michigan Interstate Gateway Alliance (LMIGA), there are new projects, and there is a new focus on improving all interstate operations throughout an expanded area. Maintaining existing partnerships and fostering new ones is one way to achieve safe and efficient interstate operations.

#### Lake Michigan Interstate Gateway Alliance

LMIGA was the successor to the former GCM Priority Corridor. LMIGA was a multi-state, multi-disciplinary voluntary organization which used [TravelMidwest.com](https://travelmidwest.com/), email and/or text messaging to distribute information to travelers in the four-state (southern Wisconsin, northern Illinois, northern Indiana, and southwestern Michigan) area.

#### Great Lakes Regional Transportation Operations Coalition

The Great Lakes Regional Transportation Operations Coalition (GLRTOC) included transportation agencies responsible for operations on major transportation routes stretching from Minneapolis, Minnesota to Toronto, Ontario (Canada). The GLRTOC was formed in May 2010 with a core mission to collaborate on improving cross-regional transportation operations in support of regional economic competitiveness and improved quality of life. The major GLRTOC goals include incident management, improved freight operations, work zone coordination and regional coordinated traveler information. The GLRTOC three strategic focus areas included freight operations, reliability and mobility strategies, and traffic incident management/emergency transportation operations. The GLRTOC had also established relationships with adjacent multistate coalitions to enhance the use of technology and reliable operations and to provide the most efficient transportation network for mega-regions and the nation as a whole.

One of the GLRTOC projects included expansion of the Gateway Traveler Information System (GTIS)/Travel Midwest website to cover the entire Interstate 94 corridor from Minneapolis, Minnesota to Detroit, and Port Huron, Michigan. This expansion included all interstates in the Minneapolis/St. Paul and Detroit metropolitan areas in addition to providing coverage along Interstate 69 and Interstate 96 in Michigan. The goal of this project was to have automated GTIS connections with other major traffic management and operations centers in the GLRTOC area to display traveler information (travel times, speed, congestion, construction, incident, special event, and camera views, etc.).

#### Downstate Illinois Expansion

In 2015, the GTIS was expanded to cover the remainder of the State of Illinois. Additional maps that cover Bloomington/Normal, Champaign/Urbana, Kankakee, Metro East St. Louis, Peoria and Springfield were added. The following interstates were added to the reports: I-24, I-64, I-70, I-72, I-155, I-172, I-255, I-270, and I-474. The traveler information data that was made available includes construction, travel times and congestion (where available), incidents, special events, and hazardous weather (that impacts traffic). Dynamic message signs and closed circuit television cameras are displayed on the maps and reports.

The goal of the Downstate Illinois Expansion was to make GTIS/Travel Midwest website serve as the foundation traveler information resource for the Illinois Department of Transportation website Getting Around Illinois.

#### Interstate 80 Expansion

In 2016, the GTIS was expanded to cover interstate 80 from Des Moines, Iowa to Cleveland, Ohio.

## Gateway Interface Specifications

As a central hub of information, the Gateway will be exchanging data with a number of data sources and data users. The data to be collected and redistributed includes primarily traffic status information, traffic related incidents and scheduled events such as roadwork, and weather information. In order for the Gateway and relevant agencies to exchange data across a multitude of heterogeneous platforms and operating environments efficiently without ambiguity, the structures of data to be exchanged have been specified using Interface Definition Language (IDL) but then later converted to XML Schema Definition Language (XSD). There is a one-to-one mapping between the IDL and XSD formats thus maintaining backwards compatibility of data.

The specifications were based on various relevant national standardization efforts, such as Traffic Management Data Dictionary (TMDD), Message Sets for External Traffic Management Center Communications (MS/ETMC2), Location Reference Message Specification (LRMS), Message Exchange for Travel Situations (METS), and the Showcase Project.

The Gateway external data standards provide data specifications for:

- Location referencing
- Device data reports from vehicle detectors, weather sensors, dynamic message signs, and highway advisory radios
- Event reporting for incidents and scheduled events that affect the traveler
- Traffic status reporting, such as congestion levels and travel times

Detailed discussions of these specifications are provided in the following sections. These explanations include relevant parts of the XSD and XML. The full and up-to-date XML definitions for any section is given in the [XML and Camera Image Download Manual](xml-and-camera-image-download-manual.md), which should be used as the final reference. It should be stated that the work of specifying standards is on-going, and that the specifications will evolve further as time progresses.

### Uploading and Downloading Traffic Information

See the [XML Upload Manual](../xml-upload-manual.md) for publishing XML to the GTIS and the [XML and Camera Image Download Manual](xml-and-camera-image-download-manual.md) for how to download data from the GTIS. Data may also be downloaded in Javascript Object Notation (JSON) format as specified in [JSON Traffic Information Download Manual](../gateway-api/README.md) or CSV format for [Camera Meta-Data (cameraInfo.csv)](../camera-info-csv.md).

### Basics for Understanding Definitions

The scientific underpinnings of previous standards are relevant and used in the Gateway specifications. Thus, for example, in the specification for latitude and longitude the following specifications are made:

```xml
<xs:simpleType name="com.gcmtravel.HDatumType">
  <xs:restriction base="xs:string">
    <xs:enumeration value="NAD27"/>
    <xs:enumeration value="NAD83"/>
    <xs:enumeration value="WGS84"/>
    <xs:enumeration value="WGS84_PLUS_EGM96"/>
    <xs:enumeration value="OTHER_HDATUM_TYPE"/>
  </xs:restriction>
</xs:simpleType>

<xs:complexType name="com.gcmtravel.LatLong">
  <xs:sequence>
    <xs:element name="latitude" type="xs:int"/>
    <xs:element name="longitude" type="xs:int"/>
    <xs:element name="hDatum" type="com.gcmtravel.HDatumType"/>
  </xs:sequence>
</xs:complexType>
```

The above specification, com.gcmtravel.LatLong, means that the content of the latitude and longitude are to be interpreted according to the provided HDatumType, whose alternatives each represent one of the accepted methods of encoding horizontal geographic data. When a new geographic datum comes along, the addition of a new alternative and the recompilation of the involved module will update the application on whichever platform and in whatever language is being used.

The necessity of data validation does not go away with the present manner of doing things. The data obtained from a source, probably over a network, must be validated and a function used to store it in the appropriate fields in the object used for Gateway communication purposes.

Use of XSD makes precise to information providers what is needed in reports to facilitate the interpretation and fusion of information by the Gateway. For example, Time is the number of milliseconds since midnight January 1, 1970. The importance of this specification and other features of description profiles are easy to see in these specifications. The same clarity and precision is present in the information agencies receives back from the Gateway.

The highest level of data structure specification in the Gateway XSD is for reports. Reports have an ID, a time stamp, and include a list of (indefinite number of) the data structure appropriate to the specification of which it is part. It is reports that are listed as the top-level data in the Gateway XML files.

## Locations

The Gateway specification for roadway locations provides accurate, unambiguous, yet concise and flexible ways to specify locations in a roadway network. While based on the Location Reference Message Specification (LRMS), the Gateway location specification has been specifically developed for applications that adopt Center-to-Center (C2C) communication protocols. The Gateway specification significantly enhances the LRMS specification by inclusion of a comprehensive method for referencing cross-sectional components of the roadway.

A full roadway location specification includes a specification of a position along a roadway and a cross-sectional position in the road or off to the right or left of the roadway. The position along the roadway is called the linear location and may be a point location or a length of roadway called a section or link. The cross-sectional position is used for specifying an effect or intensity of effect of an event that is localized to a particular lane or part of the roadway.
Roadway locations are linear when the "point location" on a road is all that needs to be specified, or a "section" of road involving two points is required to say where a measurement or event took place. (A section is always a continuous, connected piece of road.) When in addition, a location within or off the side of a road is needed, the location is specified with a "lane" description. A roadway location can be linear, or can be a linear location together with a lane location. Below we have a diagram of these relationships:

**Figure 3-1 Roadway Location Classes**

![Roadway Location Classes Diagram](../images/roadway-location-classes-diagram.svg)

In the following sections we show how each of these profiles are is used to give a precise linear, point and section locations. In a particular situation they may be considered alternatives, or a particular location may be specified redundantly with two or more profiles. A reporting data source may choose to use one or the other because it is simpler or more natural in the situation where he is. The text profile may be a last resort for an observer when none of the other profiles apply when data is being reported. When a textual report has been supplied, a redundant specification of the location by another observer may make the location precise for the Gateway. If no other profile is provided, a manual intervention by operator may be required to make the location precise. The text profile is often the preferred way to distribute information from the Gateway in a humanly understandable form.

### Common Elements of Linear Roadway Locations

Roadway Locations have certain common elements that we explain now before going on to explain the variations for each profile. Location reports typically include the roadway name, the roadway direction, and the roadway type. The roadway name is a contains two strings and two uses of the StreetNameAffixenumeration. The strings are the name by which the roadway roadway is known, and a type, called the streetType, such as "Road", "Drive" or "Lane". The prefix StreetNameAffix is for specifications like "N.", "S.", "SE". In some areas this information is after the StreetName, while in others it is before. The XSD is as follows:

```xml
<xs:simpleType name="com.gcmtravel.StreetNameAffix">
  <xs:restriction base="xs:string">
    <xs:enumeration value="NONE"/>
    <xs:enumeration value="N"/>
    <xs:enumeration value="NE"/>
    <xs:enumeration value="E"/>
    <xs:enumeration value="SE"/>
    <xs:enumeration value="S"/>
    <xs:enumeration value="SW"/>
    <xs:enumeration value="W"/>
    <xs:enumeration value="NW"/>
  </xs:restriction>
</xs:simpleType>
<xs:complexType name="com.gcmtravel.RoadwayName">
  <xs:sequence>
    <xs:element name="name" type="xs:string"/>
    <xs:element name="prefix" type="com.gcmtravel.StreetNameAffix"/>
    <xs:element name="suffix" type="com.gcmtravel.StreetNameAffix"/>
    <xs:element name="streetType" type="xs:string"/>
  </xs:sequence>
</xs:complexType>
```

The possibilities for roadway type are given in the following enumeration:

```xml
<xs:simpleType name="com.gcmtravel.RoadwayType">
  <xs:restriction base="xs:string">
    <xs:enumeration value="UNKNOWN_ROADWAY_TYPE"/>
    <xs:enumeration value="FREEWAY"/>
    <xs:enumeration value="FREEWAY_EXPRESS"/>
    <xs:enumeration value="FREEWAY_HOV"/>
    <xs:enumeration value="FREEWAY_REVERSIBLE"/>
    <xs:enumeration value="ARTERIAL"/>
    <xs:enumeration value="LOCAL_ROAD"/>
    <xs:enumeration value="RAMP"/>
    <xs:enumeration value="OTHER_ROADWAY_TYPE"/>
  </xs:restriction>
</xs:simpleType>
```

Information provider personnel should be trained in the recognition and proper encoding for these possibilities.

The roadway direction is required in profiles specifying a location with an offset, or when specifying lanes in a bi-directional roadway. The RoadwayDirectionType, defined in the XSD below, allows the user to specify the eight general direction types. A local direction is determined by the actual direction of the roadway in a localized area in which the event being described is located. In most situations, local and global directions will agree with each other. When they differ, a global direction should be used. The global direction may vary with the type of a roadway: For an Interstate highway, the direction to be selected is the national designation; and, for a state highway, the direction is the corridor- wide direction.

```xml
<xs:simpleType name="com.gcmtravel.RoadwayDirectionType">
  <xs:restriction base="xs:string">
    <xs:enumeration value="UNKNOWN_DIRECTION_TYPE"/>
    <xs:enumeration value="EAST_BOUND"/>
    <xs:enumeration value="WEST_BOUND"/>
    <xs:enumeration value="SOUTH_BOUND"/>
    <xs:enumeration value="NORTH_BOUND"/>
    <xs:enumeration value="SOUTH_EAST_BOUND"/>
    <xs:enumeration value="SOUTH_WEST_BOUND"/>
    <xs:enumeration value="NORTH_EAST_BOUND"/>
    <xs:enumeration value="NORTH_WEST_BOUND"/>
  </xs:restriction>
</xs:simpleType>
```

Designation of a direction gives a referential basis for other encoding done by the observer. In profiles that use an offset to show the distance from a landmark, or cross street, or along a ramp, the offset is positive in the direction given and negative in the opposite direction.

An additional piece of information that is typically required is the Federal Information Processing Standard (FIPS) code of the roadway. The FIPS refers to the area or jurisdiction the location is in. The XSD for the FIPS is the following:

```xml
<xs:complexType name="com.gcmtravel.FIPSCode">
  <xs:sequence>
    <xs:element name="stateCode" type="xs:int"/>
    <xs:element name="countyCode" type="xs:int"/>
    <xs:element name="cityCode" type="xs:int"/>
  </xs:sequence>
</xs:complexType>
```

With this as background we discuss the use of each profile for locating a roadway point or section.

### LatLong Profile

In the specification of a linear point location by LatLong (latitude and longitude) you record the values of latitude and longitude in microdegrees along with the format of the measurement. The linear section location by LatLong requires the specification of two points with one designated the start and the other the end according to the direction of the roadway:

```xml
<xs:simpleType name="com.gcmtravel.HDatumType">
  <xs:restriction base="xs:string">
    <xs:enumeration value="NAD27"/>
    <xs:enumeration value="NAD83"/>
    <xs:enumeration value="WGS84"/>
    <xs:enumeration value="WGS84_PLUS_EGM96"/>
    <xs:enumeration value="OTHER_HDATUM_TYPE"/>
  </xs:restriction>
</xs:simpleType>
<xs:complexType name="com.gcmtravel.LatLong">
  <xs:sequence>
    <xs:element name="latitude" type="xs:int"/>  <!-- in microdegrees -->
    <xs:element name="longitude" type="xs:int"/> <!-- in microdegrees -->
    <xs:element name="hDatum" type="com.gcmtravel.HDatumType"/>
  </xs:sequence>
</xs:complexType>
<xs:complexType name="com.gcmtravel.LatLongPoint">
  <xs:sequence>
    <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="coord" type="com.gcmtravel.LatLong"/>
  </xs:sequence>
</xs:complexType>
<xs:complexType name="com.gcmtravel.LatLongSection">
  <xs:sequence>
    <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="startLatLong" type="com.gcmtravel.LatLong"/>
    <xs:element name="endLatLong" type="com.gcmtravel.LatLong"/>
  </xs:sequence>
</xs:complexType>
```

The LatLong profile is illustrated by the following diagram:

**Figure 3-2 LatLong Profile**

![Lat Long Section Profile Diagram](../images/lat-long-section-profile-diagram.svg)

### Landmark Profile

A linear point location can be specified by reference to a landmark. A landmark has a name represented by a string. The location by landmark uses an offset measured in the direction of the roadway. An example of location by landmark would be "300 feet North from the water tower on Interstate 88". A linear section location based on landmarks has a pair of landmark names and offsets for points designated start and end. It allows for the possibility of two FIPS codes designated start and end.

```xml
<xs:complexType name="com.gcmtravel.LandmarkPoint">
  <xs:sequence>
    <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="landmarkName" type="xs:string"/>
    <xs:element name="offset" type="xs:double"/>  <!-- in meters, positive in direction stated above -->
  </xs:sequence>
</xs:complexType>
<xs:complexType name="com.gcmtravel.LandmarkSection">
  <xs:sequence>
    <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="startLandmarkName" type="xs:string"/>
    <xs:element name="startOffset" type="xs:double"/> <!-- in meters, positive in direction stated above -->
    <xs:element name="endLandmarkName" type="xs:string"/>
    <xs:element name="endOffset" type="xs:double"/>  <!-- in meters -->
  </xs:sequence>
</xs:complexType>
```

The following is a diagram of the Landmark profile:

**Figure 3-3 Landmark Profile**

![Land Mark Section Profile Diagram](../images/land-mark-section-profile-diagram.svg)

The landmark profile is not applicable unless both sender and receiver know the landmark.

### Address Profile

The Address profile uses house numbers or addresses for locating points on the roadway. The address numbering system is a well-known part of our locating system. The Gateway specification for an address is a string representing an unsigned integer. No offset is used with this method of location. The specification for a section based on house numbers has a start house number and FIPS code and an end house number and FIPS code. The XSD specifications are:

```xml
<xs:complexType name="com.gcmtravel.AddressPoint">
  <xs:sequence>
    <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="addressNumber" type="xs:string"/>
  </xs:sequence>
</xs:complexType>
<xs:complexType name="com.gcmtravel.AddressSection">
  <xs:sequence>
    <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="startAddressNumber" type="xs:string"/>
    <xs:element name="endAddressNumber" type="xs:string"/>
  </xs:sequence>
</xs:complexType>
```

The diagram for the address profile is as follows:

**Figure 3-4 Address Profile**

![Address Profile Diagram](../images/address-profile-diagram.svg)

### Mile Marker Profile

A mile marker may be used to locate a point on a road. Mile markers often have decimal parts making for more precise locations. The XSD for this profile requires a FIPSCode to be specified. (See the discussion above of common elements in locations.)  To specify a section based on mile markers we use start and end mile markers and FIPS's.

```xml
<xs:complexType name="com.gcmtravel.MilePointPoint">
  <xs:sequence>
    <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="milePoint" type="xs:double"/>  <!-- in meters, positive in direction of increasing MM values -->
  </xs:sequence>
</xs:complexType>
<xs:complexType name="com.gcmtravel.MilePointSection">
  <xs:sequence>
    <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="startMilePoint" type="xs:double"/>  <!-- in meters, positive in direction of increasing MM values -->
    <xs:element name="endMilePoint" type="xs:double"/>    <!-- in meters -->
  </xs:sequence>
</xs:complexType>
```

The diagram for mile marker profile is:

**Figure 3-5 Mile Marker Profile**

![Mile Point Section Profile Diagram](../images/mile-point-section-profile-diagram.svg)

### Cross Street Profile

A roadway location may be specified by reference to a cross street. The RoadwayName struct, RoadwayDirectionType, and RoadwayType of the cross street is used in this profile. An offset is measured from the cross street in the direction of the roadway to the point location. A FIPSCode is also required. The specification for a section based on the cross street profiles has a "from" cross street name, direction, and type and a "to" cross street name, direction, and type. Each has an offset and a FIPSCode. The XSD is:

```xml
<xs:complexType name="com.gcmtravel.CrossStreetPoint">
  <xs:sequence>
    <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="crossStreetName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="crossStreetType" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="crossStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="offset" type="xs:double"/> <!-- in meters, positive in direction stated above -->
  </xs:sequence>
</xs:complexType>
<xs:complexType name="com.gcmtravel.CrossStreetSection">
  <xs:sequence>
    <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="startOffset" type="xs:double"/>   <!-- in meters, positive in direction stated above -->
    <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="endOffset" type="xs:double"/>     <!-- in meters, positive in direction stated above -->
  </xs:sequence>
</xs:complexType>
```

The diagram for this profile is:

**Figure 3-6 Cross Street Profile**

![Cross Street Section Profile Diagram](../images/cross-street-section-profile-diagram.svg)

### Ramp Profile

The XSD specification for a linear ramp point location provides for a "from" roadway name, type, direction, and FIPS and for a "to" roadway name, type, direction and FIPS. An offset is provided for the distance along the ramp from the "from" roadway. The specification for a section by ramp points has a start offset and an end offset to define two ramp points. Start and end are defined by the direction of traffic along the ramp.

```xml
<xs:complexType name="com.gcmtravel.RampPoint">
  <xs:sequence>
    <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="offset" type="xs:double"/>  <!-- in meters along ramp's direction -->
  </xs:sequence>
</xs:complexType>
<xs:complexType name="com.gcmtravel.RampSection">
  <xs:sequence>
    <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
    <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
    <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
    <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
    <xs:element name="startOffset" type="xs:double"/>  <!-- in meters along ramp's direction -->
    <xs:element name="endOffset" type="xs:double"/>    <!-- in meters along ramp's direction -->
  </xs:sequence>
</xs:complexType>
```

The diagram of this profile shows a ramp from "fromRoadwayName" to "toRoadwayName". The start point is A and the end point is B.

**Figure 3-7 Ramp Profile**

![Ramp Section Profile Diagram](../images/ramp-section-profile-diagram.svg)

### Between Cross Streets Profile

The XSD specification for the cross streets profile provides for locating a point on a roadway as being a percentage (float) of the way between two cross streets specified by name, direction, and type. The direction of the roadway causes one cross street to be designated the "from' street and the other the "to" street. A start percent and an end percent are used to define a start point and an end point for the section.

The GTIS does not proesently support the between cross streets profile.

### Geometry Profile

A geometry point is defined by reference to a "segment ID". This allows us to find the segment in a map database. The problem is that map databases are not standard and are often proprietary. Segment IDs are subject to change in different database versions and use of them imposes the a burden of synchronizing versions and updates. If everyone is on the same page, after obtaining a segment ID, locating a point using this method is done with an offset from the Ref node of the segment measured in the direction of the roadway specified in the SegmentDirectionType enumeration direction value. Segments have two nodes, the Ref Node and the Non-Ref Node The linear section location by geometry point uses two segment ID's and two offsets. There must be a continuous sequence of segments between the start segment whose ID is given and the end segment. The XSD for this profile is:

```xml
<xs:simpleType name="com.gcmtravel.SegmentDirectionType">
  <xs:restriction base="xs:string">
    <xs:enumeration value="REF_TO_NONREF"/>
    <xs:enumeration value="NONREF_TO_REF"/>
  </xs:restriction>
</xs:simpleType>
<xs:complexType name="com.gcmtravel.GeometryPoint">
  <xs:sequence>
    <xs:element name="direction" type="com.gcmtravel.SegmentDirectionType"/>
    <xs:element name="segmentID" type="xs:long"/>
    <xs:element name="offset" type="xs:double"/> <!-- meters from directional start -->
  </xs:sequence>
</xs:complexType>
<xs:complexType name="com.gcmtravel.LatLong">
  <xs:sequence>
    <xs:element name="latitude" type="xs:int"/>
    <xs:element name="longitude" type="xs:int"/>
    <xs:element name="hDatum" type="com.gcmtravel.HDatumType"/>
  </xs:sequence>
</xs:complexType>
<xs:complexType name="com.gcmtravel.GeometrySection">
  <xs:sequence>
    <xs:element name="startSegmentDirection" type="com.gcmtravel.SegmentDirectionType"/>
    <xs:element name="segmentIDs">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="segmentIDsElement" type="xs:long"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
    <xs:element name="startOffset" type="xs:double"/>  <!-- meters from directional start -->
    <xs:element name="endOffset" type="xs:double"/>  <!-- meters from directional start -->
  </xs:sequence>
</xs:complexType>
```

**Figure 3-9 Geometry Profile**

![Geometry Section Profile Diagram](../images/geometry-section-profile-diagram.svg)

The offsets for the geometry profiles are specified in meters from the start of the segment. For segments that represent two directions of a road, the start may be either the "Ref" or "Non-Ref" depending on the SegmentDirectionType. Most interstates are digitized as uni-directional (one segment per direction) so their offset will always be from the "Ref" node of the segment.

### Text Profile

Sometimes all you have is a description of the point or section, and the Gateway includes this possibility in its profile for designation by text. If none of the other profiles are possible, reports are submitted using a text description. The text profile may also be used to return a humanly accessible message to Gateway users. The XSD is as follows:

```xml
<xs:element name="textProfile" type="xs:string"/>
```

> [!WARNING]
> The GTIS will not be able to place data with only a text profile in its maps and reports.

### Generic Section

In addition to the profiles that specify linear section locations by two points of the same profile, the Gateway XSD provides for specifying a section by using two points of arbitrary profile. In order to specify that a point specification may be of any of the above profiles, the following is specified:

```xml
<xs:complexType name="com.gcmtravel.GenericSection">
  <xs:sequence>
    <xs:element name="startPoint" type="com.gcmtravel.PointLocationProfile"/>
    <xs:element name="endPoint" type="com.gcmtravel.PointLocationProfile"/>
  </xs:sequence>
</xs:complexType>
```

### Point Location Profile

The PointLocationProfile type groups all point location types together as follows:

```xml
<xs:complexType name="com.gcmtravel.PointLocationProfile">
  <xs:choice>
    <xs:element name="latLongPointLoc" type="com.gcmtravel.LatLongPoint"/>
    <xs:element name="landmarkPointLoc" type="com.gcmtravel.LandmarkPoint"/>
    <xs:element name="addressPointLoc" type="com.gcmtravel.AddressPoint"/>
    <xs:element name="milePointPointLoc" type="com.gcmtravel.MilePointPoint"/>
    <xs:element name="crossStreetPointLoc" type="com.gcmtravel.CrossStreetPoint"/>
    <xs:element name="rampPointLoc" type="com.gcmtravel.RampPoint"/>
    <xs:element name="betweenStreetPointLoc" type="com.gcmtravel.BetweenStreetPoint"/>
    <xs:element name="geometryPointLoc" type="com.gcmtravel.GeometryPoint"/>
  </xs:choice>
</xs:complexType>
```

### Section Location Profile

The SectionLocationProfile type groups all section location types together as follows:

```xml
<xs:complexType name="com.gcmtravel.SectionLocationProfile">
  <xs:choice>
    <xs:element name="latLongSectionLoc" type="com.gcmtravel.LatLongSection"/>
    <xs:element name="landmarkSectionLoc" type="com.gcmtravel.LandmarkSection"/>
    <xs:element name="addressSectionLoc" type="com.gcmtravel.AddressSection"/>
    <xs:element name="milePointSectionLoc" type="com.gcmtravel.MilePointSection"/>
    <xs:element name="crossStreetSectionLoc" type="com.gcmtravel.CrossStreetSection"/>
    <xs:element name="rampSectionLoc" type="com.gcmtravel.RampSection"/>
    <xs:element name="betweenStreetSectionLoc" type="com.gcmtravel.BetweenStreetSection"/>
    <xs:element name="geometrySectionLoc" type="com.gcmtravel.GeometrySection"/>
    <xs:element name="genericSectionLoc" type="com.gcmtravel.GenericSection"/>
  </xs:choice>
</xs:complexType>
```

### Linear Location

A data structure that is one of the above point specifications together with a tag for saying which, i.e. the choice of the point specifications, is called a Point Location Profile (see above). In a similar manner the choice of section specifications with a tag is the Section Location Profile. The choice of point and section specifications is the Linear Location Profile:

```xml
<xs:complexType name="com.gcmtravel.PointSectionUnion">
  <xs:choice>
    <xs:element name="point">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="pointElement" type="com.gcmtravel.PointLocationProfile"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
    <xs:element name="section">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="sectionElement" type="com.gcmtravel.SectionLocationProfile"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
  </xs:choice>
</xs:complexType>
<xs:complexType name="com.gcmtravel.LinearLocation">
  <xs:sequence>
    <xs:element name="profiles" type="com.gcmtravel.PointSectionUnion"/>
    <xs:element name="textProfile" type="xs:string"/>
  </xs:sequence>
</xs:complexType>
```

The XSD defines a list of Linear Locations and a sequence of the sequences.

### Lane Descriptions or Cross-Sectional Roadway Positions

A cross-sectional position in the road or off to the right or left of the roadway can be represented with a "lane desc" XSD specification. The cross-sectional LaneDesc location is used for specifying the effect or intensity of effect (LaneImpactType) of an event that is localized to a particular lane or part of the roadway. An example would be the closing of a particular lane because of blockage by a chemical spillage. To specify a location including the lane(s) affected, a location that includes a linear location and one or more LaneDesc(s) is used.

The basic part of the LaneDesc struct is the lane number designation. Lane numbers are an index to lanes based on the perspective of a driver going in particular direction on the roadway. The number 1 designates the leftmost lane serving traffic going in the same direction as our driver. The highest lane number is the index of the rightmost lane going in the same direction. A shoulder (right or left) is considered non-indexable and had a lane number of 0. If the lane number is unknown, it is given a negative index.

A location with lane specifications will have as many lane structs as there are lanes needing to be specified. Thus, the location of a chemical spillage closing three lanes of I-240 would include three lane descs. In this regard shoulders are counted as lanes and require specification with a separate struct. An unspecified number of lanes is represented by one lane struct with an index of 99. Negative lane numbers can be used to represent counting from the right side of the road instead of the left side so that lane -1 is the rightmost followed by -2, -3, etc. The GTIS will automatically convert negative lane numbers into their positive counterpart.

Each lane includes the lane type and lane impact type. The lane type enumeration shown below includes generic lanes, express lanes, HOV lanes, reversible lanes, off-road locations and all of these at once. With each type are sub-designations for left and right shoulders, entrance and exit lanes, and right and left designations for off-road locations. The lane impact types include closed, impassable, reduced speed and lane shifted conditions, along with unknown and none. These specifications overlap with lane numbers in some respects, but together the provide fine, grandular specifics of cross-sectional conditions.

The XSD for lanes follows this comentary. The lane types are extensive and it is appropriate that training be given personnel in the accurate reporting of lane types. For example if you have multiple lanes in each direction and a median strip, you can have shoulders on both sides of the lanes going in a single direction.

Using the roadway direction on Figure 3-10, the left shoulder position is in the center of the road as indicated. Likewise, an off the road left position is in the median left of the left shoulder. In the same way the position of the right shoulder is off the edge of the road as indicated. The location off the road to the right is beyond the right shoulder. Taking the roadway direction into account again, the left-most or innermost lane is lane 1, the second left most is lane 2, etc. By use of the lane direction types, the same distinctions can be made going the opposite direction, reversing the orientations of right and left. Left is, once again, to the center or inner part of the road, and right is toward the edge of the road. The IDL reflecting these explanations is the following:

```xml
<xs:simpleType name="com.gcmtravel.LaneType">
  <xs:restriction base="xs:string">
    <xs:enumeration value="UNKNOWN_LANE_TYPE"/>
    <xs:enumeration value="LANE"/>
    <xs:enumeration value="LEFT_SHOULDER"/>
    <xs:enumeration value="RIGHT_SHOULDER"/>
    <xs:enumeration value="SHOULDER"/>
    <xs:enumeration value="MEDIAN"/>
    <xs:enumeration value="EXPRESS_LANE"/>
    <xs:enumeration value="EXPRESS_ENTRANCE_LANE"/>
    <xs:enumeration value="EXPRESS_EXIT_LANE"/>
    <xs:enumeration value="EXPRESS_CONNECTOR_LANE"/>
    <xs:enumeration value="LEFT_EXPRESS_SHOULDER"/>
    <xs:enumeration value="RIGHT_EXPRESS_SHOULDER"/>
    <xs:enumeration value="EXPRESS_SHOULDER"/>
    <xs:enumeration value="HOV_LANE"/>
    <xs:enumeration value="HOV_ENTRANCE_LANE"/>
    <xs:enumeration value="HOV_EXIT_LANE"/>
    <xs:enumeration value="HOV_CONNECTOR_LANE"/>
    <xs:enumeration value="LEFT_HOV_SHOULDER"/>
    <xs:enumeration value="RIGHT_HOV_SHOULDER"/>
    <xs:enumeration value="HOV_SHOULDER"/>
    <xs:enumeration value="REVERSIBLE_LANE"/>
    <xs:enumeration value="REVERSIBLE_ENTRANCE_LANE"/>
    <xs:enumeration value="REVERSIBLE_EXIT_LANE"/>
    <xs:enumeration value="REVERSIBLE_CONNECTOR_LANE"/>
    <xs:enumeration value="LEFT_REVERSIBLE_SHOULDER"/>
    <xs:enumeration value="RIGHT_REVERSIBLE_SHOULDER"/>
    <xs:enumeration value="REVERSIBLE_SHOULDER"/>
    <xs:enumeration value="OFF_ROAD_LEFT"/>
    <xs:enumeration value="OFF_ROAD_RIGHT"/>
    <xs:enumeration value="OFF_ROAD"/>
    <xs:enumeration value="UNKNOWN_NUMBER_OF_LANES"/>
    <xs:enumeration value="UNKNOWN_NUMBER_OF_LANES_AND_SHOULDERS"/>
    <xs:enumeration value="CENTER_LANE"/>
    <xs:enumeration value="UNSPECIFIED_LANE"/>
    <xs:enumeration value="ALL_LANES"/>
    <xs:enumeration value="ALL_LANES_AND_SHOULDERS"/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="com.gcmtravel.LaneImpactType">
  <xs:restriction base="xs:string">
    <xs:enumeration value="UNKNOWN_LANE_IMPACT"/>
    <xs:enumeration value="NONE_LANE_IMPACT"/>
    <xs:enumeration value="CLOSED"/>
    <xs:enumeration value="IMPASSABLE"/>
    <xs:enumeration value="SPEED_REDUCED"/>
    <xs:enumeration value="LANE_SHIFTED"/>
    <xs:enumeration value="OTHER_LANE_IMPACT"/>
  </xs:restriction>
</xs:simpleType>
<xs:complexType name="com.gcmtravel.LaneDesc">
  <xs:sequence>
    <xs:element name="type" type="com.gcmtravel.LaneType"/>
    <xs:element name="laneImpact" type="com.gcmtravel.LaneImpactType"/>
    <xs:element name="laneNumber" type="xs:short"/>
  </xs:sequence>
</xs:complexType>
```

The XSD for lane specifies a sequence of LaneDesc in the usual manner:

```xml
<xs:element name="lane">
  <xs:complexType>
    <xs:sequence minOccurs="0" maxOccurs="unbounded">
      <xs:element name="laneElement" type="com.gcmtravel.LaneDesc"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

**Figure 3-10 Lane Positions**

|  |
| --- |
| ← Right shoulder |
| ←Lane 3 |
| ←Lane 2 |
| ←Lane 1 |
| ←Left Shoulder |
| <Median> |
| Left Shoulder → |
| Lane 1 → |
| Lane 2 → |
| Lane 3 → |
| Right Shoulder → |

#### Fully Specified Lane Descriptions

The system will attempt to fully specify the lanes whenever possible. The location of the event must be known and resolvable to a location with a known number of lanes. Typically lane count information is available for all interstates in the coverage area. A fully specified lane description will include a left should, one or more lanes, and a right shoulder.

**Example of Fully Specified Lanes**

```xml
<lane>
  <laneElement>
    <type>LEFT_SHOULDER</type>
    <laneImpact>CLOSED</laneImpact>
    <laneNumber>0</laneNumber>
  </laneElement>
  <laneElement>
    <type>LANE</type>
    <laneImpact>NONE_LANE_IMPACT</laneImpact>
    <laneNumber>1</laneNumber>
  </laneElement>
  <laneElement>
    <type>LANE</type>
    <laneImpact>NONE_LANE_IMPACT</laneImpact>
    <laneNumber>2</laneNumber>
  </laneElement>
  <laneElement>
    <type>LANE</type>
    <laneImpact>NONE_LANE_IMPACT</laneImpact>
    <laneNumber>3</laneNumber>
  </laneElement>
  <laneElement>
    <type>RIGHT_SHOULDER</type>
    <laneImpact>CLOSED</laneImpact>
    <laneNumber>0</laneNumber>
  </laneElement>
</lane>
```

The maximum lane number present in fully specified lane descriptions will correspond to the number of lanes at the location of the event. If the event spans a section of roadway, then the maximum number of lanes thoroughout the roadway section will be used.

#### Various Lanes

Some events do not contain information about the number of lanes or how many are closed. In these cases, the lane type will be set to UNKNOWN_NUMBER_OF_LANES, the laneImpact will be CLOSED, and the laneNumber will be zero.

**Various lanes closed**

```xml
<lane>
  <laneElement>
    <type>UNKNOWN_NUMBER_OF_LANES</type>
    <laneImpact>CLOSED</laneImpact>
    <laneNumber>0</laneNumber>
  </laneElement>
</lane>
```

#### Full Closures

Full closures can be represented two ways. The first is to provide all the lanes as in "Fully Specified Lane Descriptions" above and mark all the lanes as CLOSED. The second way of representing a full closure is to use type ALL_LANES_AND_SHOULDERS or ALL_LANES with a laneImpact of CLOSED.

**Full Closure using ALL_LANES_AND_SHOULDERS**

```xml
<lane>
  <laneElement>
    <type>UNKNOWN_NUMBER_OF_LANES</type>
    <laneImpact>CLOSED</laneImpact>
    <laneNumber>0</laneNumber>
  </laneElement>
</lane>
```

### Roadway Location

The full power of the location specifications is brought to bear when a linear location is combined with a lane specification. The Linear Roadway Location specification sets out the position along a roadway, and the lane gives the cross-sectional position in the road or off to the right or left of the roadway. The XSD is as follows:

```xml
<xs:complexType name="com.gcmtravel.RoadwayLocation">
  <xs:sequence>
    <xs:element name="linear" type="com.gcmtravel.LinearLocation"/>
    <xs:element name="lane">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="laneElement" type="com.gcmtravel.LaneDesc"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
    <xs:element name="originalInput" type="xs:string"/>
  </xs:sequence>
</xs:complexType>
```

The original input string component of the RoadwayLocation struct is for preserving the information the data provider entered that was converted to a location specification.  A sequence of Roadway Locations is specified as well in the usual manner.

```xml
<xs:sequence minOccurs="0" maxOccurs="unbounded">
  <xs:element name="locationsElement" type="com.gcmtravel.RoadwayLocation"/>
</xs:sequence>
```

### Application of the Specifications for Locations

The location specifications are used in the definitions of reports explained in other sections of this document, and do not themselves define any reports. In our discussions of the XSD for available reports in the remaining sections of this document, we will not make any new explanations of locations.

## Device Station Reports

The XSD specifications for Device Station Reports define Vehicle Detector Station (VDS) reports, Weather Sensor Station (WSS) reports, Dynamic Message Sign DMS) reports, and Highway Advisory Radio (HAR) reports. By calling them reports, we are indicating that they are services that can be obtained from the XML input and output.

### Field Device Type and Status

Device Station Reports share a common structure FieldDevice. A FieldDevice contains its status as an operational or non-operational device, a unique string device ID, its type among the devices, and a unique ID for the agency that owns the device. (See the full IDL in the Appendix for an explanation of how names are constructed.) Its location is a point location, as set out in the previous section.

```xml
<xs:simpleType name="com.gcmtravel.DeviceType">
  <xs:restriction base="xs:string">
    <xs:enumeration value="VDS_DEVICETYPE"/>
    <xs:enumeration value="DMS_DEVICETYPE"/>
    <xs:enumeration value="HAR_DEVICETYPE"/>
    <xs:enumeration value="WSS_DEVICETYPE"/>
    <xs:enumeration value="OTHER_DEVICETYPE"/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="com.gcmtravel.FieldDeviceStatus">
  <xs:restriction base="xs:string">
    <xs:enumeration value="UNKNOWN_FIELD_DEVICE_STATUS"/>
    <xs:enumeration value="NONE_FIELD_DEVICE_STATUS"/>
    <xs:enumeration value="OPERATIONAL"/>
    <xs:enumeration value="OPERATIONAL_BUT_DEGRADED"/>
    <xs:enumeration value="NON_OPERATIONAL"/>
    <xs:enumeration value="COMMUNICATOINS_FAILURE"/>
    <xs:enumeration value="DOWN_FOR_MAINTENANCE"/>
  </xs:restriction>
</xs:simpleType>
```

```xml
<xs:element name="fieldDeviceID" type="xs:string"/>
<xs:element name="owningAgencyID" type="xs:string"/>
```

Two additional enumeration fields indicate the status of data validation and fusion efforts. Data can often be corrected if it was meant to be a parsable valid entry, but was mis-entered or mis-transmitted. This recovery can be by manual or automatic procedures. It can be validated when found to be within the expected bounds and infeasible if not. It can also be pre-validation, before any validation procedure has been applied.

In a similar fashion, the Gateway attempts to resolve locations by finding their precise meaning and translating them into a common basic type, namely the geometry point profile. Correction of transmission mal-formation is done, if possible. Resolution proceeds by manual or automatic procedure. Success is indicated by a location resolved status, while lack of success is indicated by a unresolvable status. The "Location not validated" status is a pre-resolution status.

```xml
<xs:simpleType name="com.gcmtravel.LocationResolutionStatus">
  <xs:restriction base="xs:string">
    <xs:enumeration value="LOCATION_NO_LOCATION"/>
    <xs:enumeration value="LOCATION_NON_SRA"/>
    <xs:enumeration value="LOCATION_PARTIALLY_NON_SRA"/>
    <xs:enumeration value="LOCATION_NOT_VALIDATED"/>
    <xs:enumeration value="LOCATION_UNRESOLVABLE_AUTO"/>
    <xs:enumeration value="LOCATION_UNRESOLVABLE_MANUAL"/>
    <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_MANUAL"/>
    <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_AUTO"/>
    <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_AUTO"/>
    <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_MANUAL"/>
    <xs:enumeration value="LOCATION_RESOLVED_MANUAL"/>
    <xs:enumeration value="LOCATION_RESOLVED_AUTO"/>
  </xs:restriction>
</xs:simpleType>
```

The FieldDataValidationStatus and the Location Resolution Status fields are required because data validation and location resolution are in some cases carried out by data source DSI machines and the Gateway needs an indication of status to know what remains to be done. The time of the entering or updating of a Field Device is kept in the struc. The last time that the location of the device was referenced is also kept in the structure. This is useful because devices are relatively stationary and locations can be used a check on whether the same device has been given more than one FieldDevice identifier. Contrariwise, when the same device id shows up at a different location, the old device is removed from the system because it has been moved.

The XSD for a FieldDevice is as follows:

```xml
<xs:complexType name="com.gcmtravel.FieldDevice">
  <xs:sequence>
    <xs:element name="deviceStatus" type="com.gcmtravel.FieldDeviceStatus"/>
    <xs:element name="fieldDeviceID" type="xs:string"/>
    <xs:element name="type" type="com.gcmtravel.DeviceType"/>
    <xs:element name="location">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="locationElement" type="com.gcmtravel.PointLocationProfile"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
    <xs:element name="owningAgencyID" type="xs:string"/>
    <xs:element name="locStatus" type="com.gcmtravel.LocationResolutionStatus"/>
    <xs:element name="dataStatus" type="com.gcmtravel.FieldDataValidationStatus"/>
    <xs:element name="lastUpdateTime" type="xs:long"/>
    <xs:element name="locationTimeStamp" type="xs:long"/>
  </xs:sequence>
</xs:complexType>
```

### Inheritance

Figure 4-1 shows that the device reports inherit a common abstract structure from the field device specification. The links represent the super-class relationship. All of the device reports add specificity to the general structure represented by the field device. The field device needs only a point roadway location. Devices are stationary and their location need not be determined dynamically. The Gateway checks for new locations for the same device and takes the later location as the true one, adding that location to the database. Locations for portable field devices are dealt with accurately in this way.

Because XSD does not support the notion of inheritance, a "parent" reference is used to represent the fields of the super-type. The "parent" contains all the fields on the super-class.

**Figure 4-1 Device Class Inheritance**

![Field Device Class Diagram](../images/field-device-class-diagram.svg)

### Vehicle Detector Station (VDS)

#### Vehicle Detector Station Report Output Format

Like all reports in the Gateway IDL, the device reports have a list of the data structure which is the subject of the report, a report ID, and a time stamp. (See the full GatewayDevice IDL in the Appendix for the way the reportID is constructed.) The Vehicle Detector Station (VDS) report given below illustrates this common structure of reports:

```xml
<xs:element name="com.gcmtravel.VDSReport">
  <xs:complexType>
    <xs:sequence minOccurs="0" maxOccurs="unbounded">
      <xs:element name="com.gcmtravel.VDSReportElement" type="com.gcmtravel.VDS"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Vehicle Detector Station Report Input Format

A slightly different format is needed for publishing VDS reports to the GTIS as follows:

```xml
<xs:element name="com.gcmtravel.VDSReport">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="reportID" type="xs:string"/>
      <xs:element name="timeStamp" type="xs:long"/>
      <xs:element name="listOfVDS">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="listOfVDSElement" type="com.gcmtravel.VDS"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Vehicle Detector Station Types

A vehicle detector station can be any of the devices for sensing the presence and characteristics of vehicles at a specific roadway location. We begin to build up the VDS data structure by defining the various types for VDS devices:

```xml
<xs:simpleType name="com.gcmtravel.VDSType">
  <xs:restriction base="xs:string">
    <xs:enumeration value="UNKNOWN_VDS_TYPE"/>
    <xs:enumeration value="LOOP"/>
    <xs:enumeration value="VISION"/>
    <xs:enumeration value="ACOUSTIC"/>
    <xs:enumeration value="INFRARED"/>
    <xs:enumeration value="RADAR"/>
    <xs:enumeration value="MICROWAVE"/>
    <xs:enumeration value="OTHER_VDS_TYPE"/>
  </xs:restriction>
</xs:simpleType>
```

#### VDS

The VDS data structure is made up of a field device data structure, a VDS type and a number of quantities that come from vehicle detector station reports:

```xml
<xs:complexType name="com.gcmtravel.VDS">
  <xs:sequence>
    <xs:element name="parent" type="com.gcmtravel.FieldDevice"/>
    <xs:element name="type" type="com.gcmtravel.VDSType"/>
    <xs:element name="volume" type="xs:short"/>     <!-- veh/ln/hr -->
    <xs:element name="occupancy" type="xs:double"/> <!-- percentage 0 to 100 -->
    <xs:element name="speed" type="xs:double"/>     <!-- meters per second -->
    <xs:element name="isSpeedTrap" type="xs:boolean"/>
    <xs:element name="detectorizationRatio" type="xs:double"/>
  </xs:sequence>
</xs:complexType>
```

While most data elements are obvious, the following needs to be noted:

- Occupancy is the percent of time that a given point on the roadway is occupied. It is less if the speeds are high.
- The detectorizationRatio is the ratio of the number of lanes monitored to the total number of lanes.

### Weather Sensor Stations (WSS)

#### Weather Sensor Station Report Output Format

A Weather Sensor Station (WSS) report is a comprehensive report of the various roadway relevant weather measurements, including the precipitation, atmosphere and surface conditions. As usual, the report consists of a list of weather sensor station data structures, an ID string, and a time stamp.

```xml
<xs:element name="com.gcmtravel.WSSReport">
  <xs:complexType>
    <xs:sequence minOccurs="0" maxOccurs="unbounded">
      <xs:element name="com.gcmtravel.WSSReportElement" type="com.gcmtravel.WSS"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Weather Sensor Station Report Input Format

The input format for WSS is similar to its output format but with the addition of a time stamp and report identifier:

```xml
<xs:element name="com.gcmtravel.WSSReport">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="reportID" type="xs:string"/>
      <xs:element name="timeStamp" type="xs:long"/>
      <xs:element name="listOfWSS">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="listOfWSSElement" type="com.gcmtravel.WSS"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Precipitation Type and Intensity

```xml
<xs:simpleType name="com.gcmtravel.PrecipType>
  <xs:restriction base="xs:string">
    <xs:enumeration value="PRECIP_UNKNOWN"/>
    <xs:enumeration value="PRECIP_NONE"/>
    <xs:enumeration value="PRECIP_RAIN"/>
    <xs:enumeration value="PRECIP_SNOW"/>
    <xs:enumeration value="PRECIP_MIXED_RAIN_AND_SNOW"/>
    <xs:enumeration value="PRECIP_OTHER"/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="com.gcmtravel.PrecipIntensity>
  <xs:restriction base="xs:string">
    <xs:enumeration value="UNKNOWN_PRECIP_INTENSITY"/>
    <xs:enumeration value="LIGHT_PRECIP"/>
    <xs:enumeration value="MODERATE_PRECIP"/>
    <xs:enumeration value="HEAVY_PRECIP"/>
  </xs:restriction>
</xs:simpleType>
```

#### Surface Conditions

```xml
<xs:simpleType name="com.gcmtravel.SurfaceCondition>
  <xs:restriction base="xs:string">
    <xs:enumeration value="SURFACE_CONDITION_UNKNOWN"/>
    <xs:enumeration value="SURFACE_DRY"/>
    <xs:enumeration value="SURFACE_WET"/>
    <xs:enumeration value="SURFACE_CHEMICAL_WET"/>
    <xs:enumeration value="SURFACE_SNOW_ICE"/>
    <xs:enumeration value="SURFACE_ABSORPTION"/>
    <xs:enumeration value="SURFACE_ABSORPTION2"/>
    <xs:enumeration value="SURFACE_DEW"/>
    <xs:enumeration value="SURFACE_FROST"/>
    <xs:enumeration value="SURFACE_ABSORPTION_AT_DEW_POINT"/>
    <xs:enumeration value="SURFACE_FROST2"/>
    <xs:enumeration value="SURFACE_ICE_ALERT"/>
  </xs:restriction>
</xs:simpleType>
```

#### Precipitation Sensor Readings

```xml
<xs:complexType name="com.gcmtravel.PrecipReadings">
  <xs:sequence>
    <xs:element name="precipSensorStatus" type="com.gcmtravel.FieldDeviceStatus"/>
    <xs:element name="type" type="com.gcmtravel.PrecipType"/>
    <xs:element name="intensity" type="com.gcmtravel.PrecipIntensity"/>
    <xs:element name="precipRate" type="xs:double"/>  <!-- mm/hr -->
    <xs:element name="precipAccumulation" type="xs:double"/> <!-- since midnight in mm -->
  </xs:sequence>
</xs:complexType>
```

#### Atmospheric Sensor Readings

```xml
<xs:complexType name="com.gcmtravel.PrecipReadings">
  <xs:sequence>
    <xs:element name="precipSensorStatus" type="com.gcmtravel.FieldDeviceStatus"/>
    <xs:element name="type" type="com.gcmtravel.PrecipType"/>
    <xs:element name="intensity" type="com.gcmtravel.PrecipIntensity"/>
    <xs:element name="precipRate" type="xs:double"/>  <!-- mm/hr -->
    <xs:element name="precipAccumulation" type="xs:double"/> <!-- since midnight in mm -->
  </xs:sequence>
</xs:complexType>
```

#### Surface Sensor Readings

```xml
<xs:complexType name="com.gcmtravel.SurfaceReadings">
  <xs:sequence>
    <xs:element name="surfaceSensorStatus" type="com.gcmtravel.FieldDeviceStatus"/>
    <xs:element name="pavementSurfaceTemp" type="xs:double"/>  <!-- Celsius -->
    <xs:element name="pavementSubsurfaceTemp" type="xs:double"/>  <!-- Celsius -->
    <xs:element name="pavementSurfaceChemicalFactor" type="xs:short"/>
    <xs:element name="pavementCondition" type="com.gcmtravel.SurfaceCondition"/>
    <xs:element name="pavementSurfaceIceIndex" type="xs:short"/>
    <xs:element name="pavementSurfacePrecipInitialFreezingTemp" type="xs:double"/>
    <xs:element name="pavementSurfacePrecipDepth" type="xs:double"/>
  </xs:sequence>
</xs:complexType>
```

#### WSS

We show the XSD of the weather sensor station data structure as follows:

```xml
<xs:complexType name="com.gcmtravel.SurfaceReadings">
  <xs:sequence>
    <xs:element name="surfaceSensorStatus" type="com.gcmtravel.FieldDeviceStatus"/>
    <xs:element name="pavementSurfaceTemp" type="xs:double"/>  <!-- Celsius -->
    <xs:element name="pavementSubsurfaceTemp" type="xs:double"/>  <!-- Celsius -->
    <xs:element name="pavementSurfaceChemicalFactor" type="xs:short"/>
    <xs:element name="pavementCondition" type="com.gcmtravel.SurfaceCondition"/>
    <xs:element name="pavementSurfaceIceIndex" type="xs:short"/>
    <xs:element name="pavementSurfacePrecipInitialFreezingTemp" type="xs:double"/>
    <xs:element name="pavementSurfacePrecipDepth" type="xs:double"/>
  </xs:sequence>
</xs:complexType>
```

### Dynamic Message Signs (DMS)

A dynamic message sign (DMS) is a sign that can change the messages presented to the viewer, such as Variable Message Sign (VMS), Changeable Message Signs (CMS), or Blank Out Sign (BOS).

#### Dynamic Message Sign Report Output Format

Here is the format for the DMS XML output:

```xml
<xs:element name="com.gcmtravel.DMSReport">
  <xs:complexType>
    <xs:sequence minOccurs="0" maxOccurs="unbounded">
      <xs:element name="com.gcmtravel.DMSReportElement" type="com.gcmtravel.DMS"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Dynamic Message Sign Report Input Format

The Dynamic Message Sign Report consists of a dynamic message sign list, a report ID, and a time stamp:

```xml
<xs:element name="com.gcmtravel.DMSReport">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="reportID" type="xs:string"/>
      <xs:element name="timeStamp" type="xs:long"/>
      <xs:element name="listOfDMS">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="listOfDMSElement" type="com.gcmtravel.DMS"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### DMS Message Set

A message set is a logical unit of information, which may consist of multiple lines. In practice, no more than three lines may be presented to the viewer since a driver can take in a limited amount of content while passing by. A maximum of twelve lines is allowed for in the XSD. More than one message can be showing at a time on the same DMS on a rotational basis. For example, a sign may have the following message sets:

<!-- TODO(docs): image 'DMS.2019-2-25_12-18-5.382x200.png' is referenced here but the attachment no longer exists on the source wiki (404) -->

Depending on the DMS device and the length of the message, one message set can be displayed in a single frame, or more than one message set can be displayed in a single frame. For example, the above two message sets can be displayed in a single frame on a three-line DMS device, or displayed in rotation in two frames on a 2-line DMS device.

```xml
<xs:complexType name="com.gcmtravel.DMSMessageSet">
  <xs:sequence>
    <xs:element name="dmsLines">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="dmsLinesElement" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
    <xs:element name="messageExpiration" type="xs:long"/>
    <xs:element name="lastUpdateTime" type="xs:long"/>
  </xs:sequence>
</xs:complexType>
```

#### DMS

The dynamic message sign definition consists of the "parent" FieldDevice and the DMSMessageSet.

```xml
<xs:complexType name="com.gcmtravel.DMS">
  <xs:sequence>
    <xs:element name="parent" type="com.gcmtravel.FieldDevice"/>
    <xs:element name="messageSets">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="messageSetsElement" type="com.gcmtravel.DMSMessageSet"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
  </xs:sequence>
</xs:complexType>
```

### Highway Advisory Radio (HAR)

#### Highway Advisory Radio Reports Output Format

```xml
<xs:element name="com.gcmtravel.HARReport">
  <xs:complexType>
    <xs:sequence minOccurs="0" maxOccurs="unbounded">
      <xs:element name="com.gcmtravel.HARReportElement" type="com.gcmtravel.HAR"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Highway Advisory Radio Reports Input Format

Similarly to the Dynamic Message Sign Report data structure above, a Highway Advisory Radio (HAR) report consists of a list of highway advisory radio data structures, a report ID, and a time stamp.

```xml
<xs:element name="com.gcmtravel.HARReport">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="reportID" type="xs:string"/>
      <xs:element name="timeStamp" type="xs:long"/>
      <xs:element name="listOfHAR">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="listOfHARElement" type="com.gcmtravel.HAR"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### HAR Message Set

```xml
<xs:complexType name="com.gcmtravel.HARMessageSet">
  <xs:sequence>
    <xs:element name="harLines">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="harLinesElement" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
    <xs:element name="messageExpiration" type="xs:long"/>
    <xs:element name="lastUpdateTime" type="xs:long"/>
  </xs:sequence>
</xs:complexType>
```

#### HAR

The highway advisory radio data structure is as follows:

```xml
<xs:complexType name="com.gcmtravel.HAR">
  <xs:sequence>
    <xs:element name="parent" type="com.gcmtravel.FieldDevice"/>
    <xs:element name="messageSets">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="messageSetsElement" type="com.gcmtravel.HARMessageSet"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
  </xs:sequence>
</xs:complexType>
```

## Device Station Reports

The XSD specifications for Device Station Reports define Vehicle Detector Station (VDS) reports, Weather Sensor Station (WSS) reports, Dynamic Message Sign DMS) reports, and Highway Advisory Radio (HAR) reports. By calling them reports, we are indicating that they are services that can be obtained from the XML input and output.

### Field Device Type and Status

Device Station Reports share a common structure FieldDevice. A FieldDevice contains its status as an operational or non-operational device, a unique string device ID, its type among the devices, and a unique ID for the agency that owns the device. (See the full IDL in the Appendix for an explanation of how names are constructed.) Its location is a point location, as set out in the previous section.

```xml
<xs:simpleType name="com.gcmtravel.DeviceType">
  <xs:restriction base="xs:string">
    <xs:enumeration value="VDS_DEVICETYPE"/>
    <xs:enumeration value="DMS_DEVICETYPE"/>
    <xs:enumeration value="HAR_DEVICETYPE"/>
    <xs:enumeration value="WSS_DEVICETYPE"/>
    <xs:enumeration value="OTHER_DEVICETYPE"/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="com.gcmtravel.FieldDeviceStatus">
  <xs:restriction base="xs:string">
    <xs:enumeration value="UNKNOWN_FIELD_DEVICE_STATUS"/>
    <xs:enumeration value="NONE_FIELD_DEVICE_STATUS"/>
    <xs:enumeration value="OPERATIONAL"/>
    <xs:enumeration value="OPERATIONAL_BUT_DEGRADED"/>
    <xs:enumeration value="NON_OPERATIONAL"/>
    <xs:enumeration value="COMMUNICATOINS_FAILURE"/>
    <xs:enumeration value="DOWN_FOR_MAINTENANCE"/>
  </xs:restriction>
</xs:simpleType>
```

```xml
<xs:element name="fieldDeviceID" type="xs:string"/>
<xs:element name="owningAgencyID" type="xs:string"/>
```

Two additional enumeration fields indicate the status of data validation and fusion efforts. Data can often be corrected if it was meant to be a parsable valid entry, but was mis-entered or mis-transmitted. This recovery can be by manual or automatic procedures. It can be validated when found to be within the expected bounds and infeasible if not. It can also be pre-validation, before any validation procedure has been applied.

In a similar fashion, the Gateway attempts to resolve locations by finding their precise meaning and translating them into a common basic type, namely the geometry point profile. Correction of transmission mal-formation is done, if possible. Resolution proceeds by manual or automatic procedure. Success is indicated by a location resolved status, while lack of success is indicated by a unresolvable status. The "Location not validated" status is a pre-resolution status.

```xml
<xs:simpleType name="com.gcmtravel.LocationResolutionStatus">
  <xs:restriction base="xs:string">
    <xs:enumeration value="LOCATION_NO_LOCATION"/>
    <xs:enumeration value="LOCATION_NON_SRA"/>
    <xs:enumeration value="LOCATION_PARTIALLY_NON_SRA"/>
    <xs:enumeration value="LOCATION_NOT_VALIDATED"/>
    <xs:enumeration value="LOCATION_UNRESOLVABLE_AUTO"/>
    <xs:enumeration value="LOCATION_UNRESOLVABLE_MANUAL"/>
    <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_MANUAL"/>
    <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_AUTO"/>
    <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_AUTO"/>
    <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_MANUAL"/>
    <xs:enumeration value="LOCATION_RESOLVED_MANUAL"/>
    <xs:enumeration value="LOCATION_RESOLVED_AUTO"/>
  </xs:restriction>
</xs:simpleType>
```

The FieldDataValidationStatus and the Location Resolution Status fields are required because data validation and location resolution are in some cases carried out by data source DSI machines and the Gateway needs an indication of status to know what remains to be done. The time of the entering or updating of a Field Device is kept in the struc. The last time that the location of the device was referenced is also kept in the structure. This is useful because devices are relatively stationary and locations can be used a check on whether the same device has been given more than one FieldDevice identifier. Contrariwise, when the same device id shows up at a different location, the old device is removed from the system because it has been moved.

The XSD for a FieldDevice is as follows:

```xml
<xs:complexType name="com.gcmtravel.FieldDevice">
  <xs:sequence>
    <xs:element name="deviceStatus" type="com.gcmtravel.FieldDeviceStatus"/>
    <xs:element name="fieldDeviceID" type="xs:string"/>
    <xs:element name="type" type="com.gcmtravel.DeviceType"/>
    <xs:element name="location">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="locationElement" type="com.gcmtravel.PointLocationProfile"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
    <xs:element name="owningAgencyID" type="xs:string"/>
    <xs:element name="locStatus" type="com.gcmtravel.LocationResolutionStatus"/>
    <xs:element name="dataStatus" type="com.gcmtravel.FieldDataValidationStatus"/>
    <xs:element name="lastUpdateTime" type="xs:long"/>
    <xs:element name="locationTimeStamp" type="xs:long"/>
  </xs:sequence>
</xs:complexType>
```

### Inheritance

Figure 4-1 shows that the device reports inherit a common abstract structure from the field device specification. The links represent the super-class relationship. All of the device reports add specificity to the general structure represented by the field device. The field device needs only a point roadway location. Devices are stationary and their location need not be determined dynamically. The Gateway checks for new locations for the same device and takes the later location as the true one, adding that location to the database. Locations for portable field devices are dealt with accurately in this way.

Because XSD does not support the notion of inheritance, a "parent" reference is used to represent the fields of the super-type. The "parent" contains all the fields on the super-class.

**Figure 4-1 Device Class Inheritance**

![Field Device Class Diagram](../images/field-device-class-diagram.svg)

### Vehicle Detector Station (VDS)

#### Vehicle Detector Station Report Output Format

Like all reports in the Gateway IDL, the device reports have a list of the data structure which is the subject of the report, a report ID, and a time stamp. (See the full GatewayDevice IDL in the Appendix for the way the reportID is constructed.) The Vehicle Detector Station (VDS) report given below illustrates this common structure of reports:

```xml
<xs:element name="com.gcmtravel.VDSReport">
  <xs:complexType>
    <xs:sequence minOccurs="0" maxOccurs="unbounded">
      <xs:element name="com.gcmtravel.VDSReportElement" type="com.gcmtravel.VDS"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Vehicle Detector Station Report Input Format

A slightly different format is needed for publishing VDS reports to the GTIS as follows:

```xml
<xs:element name="com.gcmtravel.VDSReport">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="reportID" type="xs:string"/>
      <xs:element name="timeStamp" type="xs:long"/>
      <xs:element name="listOfVDS">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="listOfVDSElement" type="com.gcmtravel.VDS"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Vehicle Detector Station Types

A vehicle detector station can be any of the devices for sensing the presence and characteristics of vehicles at a specific roadway location. We begin to build up the VDS data structure by defining the various types for VDS devices:

```xml
<xs:simpleType name="com.gcmtravel.VDSType">
  <xs:restriction base="xs:string">
    <xs:enumeration value="UNKNOWN_VDS_TYPE"/>
    <xs:enumeration value="LOOP"/>
    <xs:enumeration value="VISION"/>
    <xs:enumeration value="ACOUSTIC"/>
    <xs:enumeration value="INFRARED"/>
    <xs:enumeration value="RADAR"/>
    <xs:enumeration value="MICROWAVE"/>
    <xs:enumeration value="OTHER_VDS_TYPE"/>
  </xs:restriction>
</xs:simpleType>
```

#### VDS

The VDS data structure is made up of a field device data structure, a VDS type and a number of quantities that come from vehicle detector station reports:

```xml
<xs:complexType name="com.gcmtravel.VDS">
  <xs:sequence>
    <xs:element name="parent" type="com.gcmtravel.FieldDevice"/>
    <xs:element name="type" type="com.gcmtravel.VDSType"/>
    <xs:element name="volume" type="xs:short"/>     <!-- veh/ln/hr -->
    <xs:element name="occupancy" type="xs:double"/> <!-- percentage 0 to 100 -->
    <xs:element name="speed" type="xs:double"/>     <!-- meters per second -->
    <xs:element name="isSpeedTrap" type="xs:boolean"/>
    <xs:element name="detectorizationRatio" type="xs:double"/>
  </xs:sequence>
</xs:complexType>
```

While most data elements are obvious, the following needs to be noted:

- Occupancy is the percent of time that a given point on the roadway is occupied. It is less if the speeds are high.
- The detectorizationRatio is the ratio of the number of lanes monitored to the total number of lanes.

### Weather Sensor Stations (WSS)

#### Weather Sensor Station Report Output Format

A Weather Sensor Station (WSS) report is a comprehensive report of the various roadway relevant weather measurements, including the precipitation, atmosphere and surface conditions. As usual, the report consists of a list of weather sensor station data structures, an ID string, and a time stamp.

```xml
<xs:element name="com.gcmtravel.WSSReport">
  <xs:complexType>
    <xs:sequence minOccurs="0" maxOccurs="unbounded">
      <xs:element name="com.gcmtravel.WSSReportElement" type="com.gcmtravel.WSS"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Weather Sensor Station Report Input Format

The input format for WSS is similar to its output format but with the addition of a time stamp and report identifier:

```xml
<xs:element name="com.gcmtravel.WSSReport">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="reportID" type="xs:string"/>
      <xs:element name="timeStamp" type="xs:long"/>
      <xs:element name="listOfWSS">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="listOfWSSElement" type="com.gcmtravel.WSS"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Precipitation Type and Intensity

```xml
<xs:simpleType name="com.gcmtravel.PrecipType>
  <xs:restriction base="xs:string">
    <xs:enumeration value="PRECIP_UNKNOWN"/>
    <xs:enumeration value="PRECIP_NONE"/>
    <xs:enumeration value="PRECIP_RAIN"/>
    <xs:enumeration value="PRECIP_SNOW"/>
    <xs:enumeration value="PRECIP_MIXED_RAIN_AND_SNOW"/>
    <xs:enumeration value="PRECIP_OTHER"/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="com.gcmtravel.PrecipIntensity>
  <xs:restriction base="xs:string">
    <xs:enumeration value="UNKNOWN_PRECIP_INTENSITY"/>
    <xs:enumeration value="LIGHT_PRECIP"/>
    <xs:enumeration value="MODERATE_PRECIP"/>
    <xs:enumeration value="HEAVY_PRECIP"/>
  </xs:restriction>
</xs:simpleType>
```

#### Surface Conditions

```xml
<xs:simpleType name="com.gcmtravel.SurfaceCondition>
  <xs:restriction base="xs:string">
    <xs:enumeration value="SURFACE_CONDITION_UNKNOWN"/>
    <xs:enumeration value="SURFACE_DRY"/>
    <xs:enumeration value="SURFACE_WET"/>
    <xs:enumeration value="SURFACE_CHEMICAL_WET"/>
    <xs:enumeration value="SURFACE_SNOW_ICE"/>
    <xs:enumeration value="SURFACE_ABSORPTION"/>
    <xs:enumeration value="SURFACE_ABSORPTION2"/>
    <xs:enumeration value="SURFACE_DEW"/>
    <xs:enumeration value="SURFACE_FROST"/>
    <xs:enumeration value="SURFACE_ABSORPTION_AT_DEW_POINT"/>
    <xs:enumeration value="SURFACE_FROST2"/>
    <xs:enumeration value="SURFACE_ICE_ALERT"/>
  </xs:restriction>
</xs:simpleType>
```

#### Precipitation Sensor Readings

```xml
<xs:complexType name="com.gcmtravel.PrecipReadings">
  <xs:sequence>
    <xs:element name="precipSensorStatus" type="com.gcmtravel.FieldDeviceStatus"/>
    <xs:element name="type" type="com.gcmtravel.PrecipType"/>
    <xs:element name="intensity" type="com.gcmtravel.PrecipIntensity"/>
    <xs:element name="precipRate" type="xs:double"/>  <!-- mm/hr -->
    <xs:element name="precipAccumulation" type="xs:double"/> <!-- since midnight in mm -->
  </xs:sequence>
</xs:complexType>
```

#### Atmospheric Sensor Readings

```xml
<xs:complexType name="com.gcmtravel.PrecipReadings">
  <xs:sequence>
    <xs:element name="precipSensorStatus" type="com.gcmtravel.FieldDeviceStatus"/>
    <xs:element name="type" type="com.gcmtravel.PrecipType"/>
    <xs:element name="intensity" type="com.gcmtravel.PrecipIntensity"/>
    <xs:element name="precipRate" type="xs:double"/>  <!-- mm/hr -->
    <xs:element name="precipAccumulation" type="xs:double"/> <!-- since midnight in mm -->
  </xs:sequence>
</xs:complexType>
```

#### Surface Sensor Readings

```xml
<xs:complexType name="com.gcmtravel.SurfaceReadings">
  <xs:sequence>
    <xs:element name="surfaceSensorStatus" type="com.gcmtravel.FieldDeviceStatus"/>
    <xs:element name="pavementSurfaceTemp" type="xs:double"/>  <!-- Celsius -->
    <xs:element name="pavementSubsurfaceTemp" type="xs:double"/>  <!-- Celsius -->
    <xs:element name="pavementSurfaceChemicalFactor" type="xs:short"/>
    <xs:element name="pavementCondition" type="com.gcmtravel.SurfaceCondition"/>
    <xs:element name="pavementSurfaceIceIndex" type="xs:short"/>
    <xs:element name="pavementSurfacePrecipInitialFreezingTemp" type="xs:double"/>
    <xs:element name="pavementSurfacePrecipDepth" type="xs:double"/>
  </xs:sequence>
</xs:complexType>
```

#### WSS

We show the XSD of the weather sensor station data structure as follows:

```xml
<xs:complexType name="com.gcmtravel.SurfaceReadings">
  <xs:sequence>
    <xs:element name="surfaceSensorStatus" type="com.gcmtravel.FieldDeviceStatus"/>
    <xs:element name="pavementSurfaceTemp" type="xs:double"/>  <!-- Celsius -->
    <xs:element name="pavementSubsurfaceTemp" type="xs:double"/>  <!-- Celsius -->
    <xs:element name="pavementSurfaceChemicalFactor" type="xs:short"/>
    <xs:element name="pavementCondition" type="com.gcmtravel.SurfaceCondition"/>
    <xs:element name="pavementSurfaceIceIndex" type="xs:short"/>
    <xs:element name="pavementSurfacePrecipInitialFreezingTemp" type="xs:double"/>
    <xs:element name="pavementSurfacePrecipDepth" type="xs:double"/>
  </xs:sequence>
</xs:complexType>
```

### Dynamic Message Signs (DMS)

A dynamic message sign (DMS) is a sign that can change the messages presented to the viewer, such as Variable Message Sign (VMS), Changeable Message Signs (CMS), or Blank Out Sign (BOS).

#### Dynamic Message Sign Report Output Format

Here is the format for the DMS XML output:

```xml
<xs:element name="com.gcmtravel.DMSReport">
  <xs:complexType>
    <xs:sequence minOccurs="0" maxOccurs="unbounded">
      <xs:element name="com.gcmtravel.DMSReportElement" type="com.gcmtravel.DMS"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Dynamic Message Sign Report Input Format

The Dynamic Message Sign Report consists of a dynamic message sign list, a report ID, and a time stamp:

```xml
<xs:element name="com.gcmtravel.DMSReport">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="reportID" type="xs:string"/>
      <xs:element name="timeStamp" type="xs:long"/>
      <xs:element name="listOfDMS">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="listOfDMSElement" type="com.gcmtravel.DMS"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### DMS Message Set

A message set is a logical unit of information, which may consist of multiple lines. In practice, no more than three lines may be presented to the viewer since a driver can take in a limited amount of content while passing by. A maximum of twelve lines is allowed for in the XSD. More than one message can be showing at a time on the same DMS on a rotational basis. For example, a sign may have the following message sets:

<!-- TODO(docs): image 'DMS.2019-2-25_12-18-5.382x200.png' is referenced here but the attachment no longer exists on the source wiki (404) -->

Depending on the DMS device and the length of the message, one message set can be displayed in a single frame, or more than one message set can be displayed in a single frame. For example, the above two message sets can be displayed in a single frame on a three-line DMS device, or displayed in rotation in two frames on a 2-line DMS device.

```xml
<xs:complexType name="com.gcmtravel.DMSMessageSet">
  <xs:sequence>
    <xs:element name="dmsLines">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="dmsLinesElement" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
    <xs:element name="messageExpiration" type="xs:long"/>
    <xs:element name="lastUpdateTime" type="xs:long"/>
  </xs:sequence>
</xs:complexType>
```

#### DMS

The dynamic message sign definition consists of the "parent" FieldDevice and the DMSMessageSet.

```xml
<xs:complexType name="com.gcmtravel.DMS">
  <xs:sequence>
    <xs:element name="parent" type="com.gcmtravel.FieldDevice"/>
    <xs:element name="messageSets">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="messageSetsElement" type="com.gcmtravel.DMSMessageSet"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
  </xs:sequence>
</xs:complexType>
```

### Highway Advisory Radio (HAR)

#### Highway Advisory Radio Reports Output Format

```xml
<xs:element name="com.gcmtravel.HARReport">
  <xs:complexType>
    <xs:sequence minOccurs="0" maxOccurs="unbounded">
      <xs:element name="com.gcmtravel.HARReportElement" type="com.gcmtravel.HAR"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Highway Advisory Radio Reports Input Format

Similarly to the Dynamic Message Sign Report data structure above, a Highway Advisory Radio (HAR) report consists of a list of highway advisory radio data structures, a report ID, and a time stamp.

```xml
<xs:element name="com.gcmtravel.HARReport">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="reportID" type="xs:string"/>
      <xs:element name="timeStamp" type="xs:long"/>
      <xs:element name="listOfHAR">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="listOfHARElement" type="com.gcmtravel.HAR"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### HAR Message Set

```xml
<xs:complexType name="com.gcmtravel.HARMessageSet">
  <xs:sequence>
    <xs:element name="harLines">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="harLinesElement" type="xs:string"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
    <xs:element name="messageExpiration" type="xs:long"/>
    <xs:element name="lastUpdateTime" type="xs:long"/>
  </xs:sequence>
</xs:complexType>
```

#### HAR

The highway advisory radio data structure is as follows:

```xml
<xs:complexType name="com.gcmtravel.HAR">
  <xs:sequence>
    <xs:element name="parent" type="com.gcmtravel.FieldDevice"/>
    <xs:element name="messageSets">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="messageSetsElement" type="com.gcmtravel.HARMessageSet"/>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
  </xs:sequence>
</xs:complexType>
```

## Traffic Reports

Traffic reports available on the Gateway are the Link Congestion report, the Travel Time Report, and the Link Traffic report. Congestion and other traffic parameters are reported on a "link" basis. A link is a sequence of spatially contiguous sections which can be sections from different roadways.

Traffic Reports report the congestion levels of links only. The Traffic Report contains a more complete set of traffic parameters than Congestion Reports, including travel times, speeds and occupancy. Congestion reports are generated when the link reported about is not defined for traffic reporting. Both reports have the report ID and time stamp.

The Travel Time Report is specialized to contain data for users interested particularly in the travel time view of traffic conditions. It contains a link location, and linkID made up of well-known sub-parts for easy reference. Included is a string for human consumption with a meaningful translation of the location information, e.g. Highway X from Cross Road Y to Cross Road Z.

The data for the Traffic Reports contain a time when the location was entered as a check on the identification of the data in the system. The structs are updated without the location being changed when the same traffic condition changes. Two structs with the same locations are about the same traffic condition even if the ids aren't the same. When the location changes the traffic data is about another traffic condition.

### Link Congestion Reports

Link congestion reports contain low, medium, high congestion level information on detectorized road ways. Typical link lengths are from one half to one mile.

#### Link Congestion Input Format

The following format is used to send link congestion data to the Gateway:

```xml
<xs:element name="com.gcmtravel.LinkCongestionReport">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="reportID" type="xs:string"/>
      <xs:element name="timeStamp" type="xs:long"/>
      <xs:element name="data">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="dataElement" type="com.gcmtravel.LinkCongestion"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Link Congestion Output Format

The following format is used in link congestion data files downloaded from the Gateway TravelMidwest.com:

```xml
<xs:element name="com.gcmtravel.LinkCongestionReport">
  <xs:complexType>
    <xs:sequence minOccurs="0" maxOccurs="unbounded">
      <xs:element name="com.gcmtravel.LinkCongestionReportElement" type="com.gcmtravel.LinkCongestion"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Congestion Level

Link congestion data structures are defined as follows:

```xml
<xs:simpleType name="com.gcmtravel.CongestionLevelType">
  <xs:restriction base="xs:string">
    <xs:enumeration value="UNKNOWN_CONGESTION_LEVEL"/
    <xs:enumeration value="NON_CONGESTION"/>
    <xs:enumeration value="LIGHT_CONGESTION"/>
    <xs:enumeration value="MEDIUM_CONGESTION"/>
    <xs:enumeration value="HEAVY_CONGESTION"/>
  </xs:restriction>
</xs:simpleType>
```

#### Link Congestion

A individual congestion link is defined as follows:

```xml
<xs:complexType name="com.gcmtravel.LinkCongestion">
  <xs:sequence>
    <xs:element name="link">
      <xs:complexType>
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
          <xs:element name="linkElement">
            <xs:complexType>
              <xs:sequence minOccurs="0" maxOccurs="unbounded">
                <xs:element name="linkElementElement" type="com.gcmtravel.SectionLocationProfile"/>
              </xs:sequence>
            </xs:complexType>
          </xs:element>
        </xs:sequence>
      </xs:complexType>
    </xs:element>
    <xs:element name="linkID" type="xs:string"/>
    <xs:element name="linkDesc" type="xs:string"/>
    <xs:element name="length" type="xs:int"/> <!-- meters -->
    <xs:element name="locationTimeStamp" type="xs:long"/>
    <xs:element name="congestionLevel" type="com.gcmtravel.CongestionLevelType"/>
    <xs:element name="locStatus" type="com.gcmtravel.LocationResolutionStatus"/>
    <xs:element name="dataStatus" type="com.gcmtravel.FieldDataValidationStatus"/>
    <xs:element name="timeStamp" type="xs:long"/>
  </xs:sequence>
</xs:complexType>
```

### Link travel time reports

The specialized Link Travel Time Report contains a link travel time list.

#### Link Traffic Input Format

The following format is used to send link traffic (travel time) data to the Gateway:

```xml
<xs:element name="com.gcmtravel.LinkTrafficReport">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="reportID" type="xs:string"/>
      <xs:element name="timeStamp" type="xs:long"/>
      <xs:element name="data">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="dataElement" type="com.gcmtravel.LinkTraffic"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Link Traffic Output Format

The following format is used in link traffic (travel time) data files downloaded from the Gateway [TravelMidwest.com](http://TravelMidwest.com):

```xml
<xs:element name="com.gcmtravel.LinkTrafficReport">
  <xs:complexType>
    <xs:sequence minOccurs="0" maxOccurs="unbounded">
      <xs:element name="com.gcmtravel.LinkTrafficReportElement" type="com.gcmtravel.LinkTraffic"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

#### Link Traffic

A individual traffic link is defined as follows:

```xml
<xs:complexType name="com.gcmtravel.LinkTraffic">
   <xs:sequence>
     <xs:element name="link">
       <xs:complexType>
         <xs:sequence minOccurs="0" maxOccurs="unbounded">
           <xs:element name="linkElement">
             <xs:complexType>
               <xs:sequence minOccurs="0" maxOccurs="unbounded">
                 <xs:element name="linkElementElement" type="com.gcmtravel.SectionLocationProfile"/>
               </xs:sequence>
             </xs:complexType>
           </xs:element>
         </xs:sequence>
       </xs:complexType>
     </xs:element>
     <xs:element name="linkID" type="xs:string"/>
     <xs:element name="linkDesc" type="xs:string"/>
     <xs:element name="length" type="xs:int"/>       <!-- meters -->
     <xs:element name="locationTimeStamp" type="xs:long"/>
     <xs:element name="isBasic" type="xs:boolean"/>
     <xs:element name="travelTime" type="xs:int"/>   <!-- seconds -->
     <xs:element name="volume" type="xs:short"/>     <!-- vehicles/lane/hour -->
     <xs:element name="speed" type="xs:double"/>     <!-- meters/second -->
     <xs:element name="occupancy" type="xs:double"/> <!-- percent 0 to 100 -->
     <xs:element name="congestionLevel" type="com.gcmtravel.CongestionLevelType"/>
     <xs:element name="locStatus" type="com.gcmtravel.LocationResolutionStatus"/>
     <xs:element name="dataStatus" type="com.gcmtravel.FieldDataValidationStatus"/>
     <xs:element name="timeStamp" type="xs:long"/>   <!-  milliseconds since epoch -->
   </xs:sequence>
</xs:complexType>
```

Of particular interest to Gateway subscribers is the travel time quantity, the most reported piece of information in the public media.

As explained above, two fields indicate the status of data validation and fusion efforts. Data can be corrected when recovery is made of data that was meant to be a ascertainable valid entry, but was mis-entered or mis-transmitted. The data recovery can be by manual or automatic procedures. Data can be validated by being found to be within expected bounds, and infeasible if not. It can also be pre-validation, before any validation procedure has been applied.

In a similar fashion, the Gateway attempts to resolve locations by finding their precise meaning and translating them into a common basic type, namely the geometry point profile. Correction of transmission mal-formation is done, if possible. Resolution proceeds by manual or automatic procedure. Success is indicated by a location resolved status, while lack of success is indicated by a unresolvable status.

The "Location not validated" is a pre-resolution status. The IDL for these enums is as follows:

```xml
<xs:simpleType name="com.gcmtravel.LocationResolutionStatus">
  <xs:restriction base="xs:string">
    <xs:enumeration value="LOCATION_NO_LOCATION"/>
    <xs:enumeration value="LOCATION_NON_SRA"/>
    <xs:enumeration value="LOCATION_PARTIALLY_NON_SRA"/>
    <xs:enumeration value="LOCATION_NOT_VALIDATED"/>
    <xs:enumeration value="LOCATION_UNRESOLVABLE_AUTO"/>
    <xs:enumeration value="LOCATION_UNRESOLVABLE_MANUAL"/>
    <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_MANUAL"/>
    <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_AUTO"/>
    <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_AUTO"/>
    <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_MANUAL"/>
    <xs:enumeration value="LOCATION_RESOLVED_MANUAL"/>
    <xs:enumeration value="LOCATION_RESOLVED_AUTO"/>
  </xs:restriction>
</xs:simpleType>
```

The FieldDataValidationStatus and the Location Resolution Status fields are required because data validation and location resolution are in some cases carried out by data source interfaces (DSI) and the Gateway needs an indication of status to know what remains to be done.

## Publishing Data to the Gateway

Historically, the **Gateway Traveler Information System (GTIS)** has been providing CORBA publish/subscribe and HTTP/XML download based external interfaces for exchanging information with data source systems and data user systems. This document describes an external interface that supports XML uploads.

> [!NOTE]
> The "datapublisher" role must be granted to your account to upload XML data via the publisher.  Contact [webmaster@travelmidwest.com](mailto:webmaster@travelmidwest.com) for more information.

## Web Service

The web service is a simple HTTP POST operation with one parameter — “report” — to the following URL:

```
https://travelmidwest.com/lmiga/publisher
```

Note:

- The report parameter is an XML document containing a LinkTrafficReport, LinkCongestionReport, IncidentReport, RoadWorkReport, HARReport, SpecialEventReport, DMSReport or HARReport.
- The report objects may, in turn, contain one or more element objects. The report objects will be processed by the Gateway, published to its subscribers and displayed on the Gateway website at [travelmidwest.com](https://travelmidwest.com/) (or [testing.travelmidwest.com](https://testing.travelmidwest.com/) when testing).
- Authentication headers with a username + password with XML upload privileges are required. The Gateway will respond with a HTML page containing the word "OK" if the data was accepted.
- During development, we encourage you to use our testing website: [https://testing.travelmidwest.com/lmiga/publisher](https://testing.travelmidwest.com/lmiga/publisher)

## Schemas

XML schemas for the various types of reports that can be sent to the Gateway via its XML upload service are available in the attachments section at the bottom of this page.

The fields contained in these schemas are described in the [Gateway External Interface User Guide]() document.

## Examples

Clients of the Gateway web service may use different programming languages and platforms to develop applications. The demonstration clients provided below serve mostly as tools to test and verify web services the Gateway provides.

### Upload a LinkTrafficReport to the Gateway

**Perl demo client**

```perl
#!/usr/bin/perl -w

use strict;

use LWP::UserAgent;
use HTTP::Request::Common qw(POST);
use MIME::Base64;

# TO DO: place production server name here
my $uri = "https://192.168.1.20/gcm/publisher";
my $userAgent = LWP::UserAgent->new(agent => 'Perl');

#READ TEST DATA XML
open(MYINPUTFILE, "<LinkTrafficReport.xml");
my(@datalines) = <MYINPUTFILE>;
my($dataline);
my $DATA_XML = "";
foreach $dataline (@datalines) {
 $DATA_XML .= $dataline;
}
close(MYINPUTFILE);

my $request = POST $uri, [ report => $DATA_XML ];
my $authorization = 'Basic ' . encode_base64('skyway:bsskyway');
$request->header("Authorization" => $authorization);

my $response = $userAgent->request($request);

#print $response->error_as_HTML unless $response->is_success;
print $response->as_string;
```

**Java demo client:**

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import com.meterware.httpunit.Base64;
import com.meterware.httpunit.PostMethodWebRequest;
import com.meterware.httpunit.WebConversation;
import com.meterware.httpunit.WebResponse;

import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;

/**
* Tests the publisher gcmtravel.com servlet by uploading a LinkTrafficReport to
* it.
*
* @author dillenbu
*
*/
public class UploadClientTest extends TestCase {
  public void testPublisher() throws Exception {
    String ltr = getLinkTrafficReport();
    WebConversation wc = new WebConversation();
    PostMethodWebRequest request = new PostMethodWebRequest(
      "https://www.travelmidwest.com/lmiga/publisher");
    request.setHeaderField("Authorization", "Basic " + Base64.encode("username:password"));
    request.setParameter("report", ltr);
    WebResponse response = wc.sendRequest(request);
    assertNotNull("No response received", response);
    assertTrue("response should say \"OK\"", response.getText().contains("OK"));
  }

  public String getLinkTrafficReport() throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(
      this.getClass().getClassLoader().getResourceAsStream(resources/LinkTrafficReport.xml")));
    StringBuffer b = new StringBuffer();
    String line;
    while ((line = in.readLine()) != null) {
      b.append(line);
    }
    return b.toString();
  }

  public static void main(String args[]) {
    XTrustProvider.install();
    com.sun.net.ssl.HostnameVerifier hv = new com.sun.net.ssl.HostnameVerifier() {
      public boolean verify(String urlHostname, String certHostname) {
        System.out.println("WARNING: Hostname is not matched for cert.");
        return true;
      }
    };
    com.sun.net.ssl.HttpsURLConnection.setDefaultHostnameVerifier(hv);
      TestRunner.run(new TestSuite(UploadClientTest.class)
    );
  }
}
```

### Example LinkTrafficReport XML

```xml
<com.gcmtravel.LinkTrafficReport>
  <reportID>IL-SKYWAY-1</reportID>
  <timeStamp>0</timeStamp>
  <data>
    <dataElement>
      <link>
        <linkElement>
          <linkElementElement>
            <crossStreetSectionLoc>
              <roadName>
                <name>CHICAGO SKYWAY</name>
                <prefix>NONE</prefix>
                <suffix>NONE</suffix>
                <streetType/>
              </roadName>
              <direction>EAST_BOUND</direction>
              <type>FREEWAY</type>
              <startFipsCode>
                <stateCode>0</stateCode>
                <countyCode>0</countyCode>
                <cityCode>0</cityCode>
              </startFipsCode>
              <endFipsCode>
                <stateCode>0</stateCode>
                <countyCode>0</countyCode>
                <cityCode>0</cityCode>
              </endFipsCode>
              <fromCrossStreetName>
                <name>DAN RYAN</name>
                <prefix>NONE</prefix>
                <suffix>NONE</suffix>
                <streetType/>
              </fromCrossStreetName>
              <fromCrossStreetType>FREEWAY</fromCrossStreetType>
              <fromStreetDirection>SOUTH_BOUND</fromStreetDirection>
              <startOffset>0.0</startOffset>
              <toCrossStreetName>
                <name>STATE LINE</name>
                <prefix>NONE</prefix>
                <suffix>NONE</suffix>
                <streetType/>
              </toCrossStreetName>
              <toCrossStreetType>UNKNOWN_ROADWAY_TYPE</toCrossStreetType>
              <toStreetDirection>UNKNOWN_DIRECTION_TYPE</toStreetDirection>
              <endOffset>0.0</endOffset>
            </crossStreetSectionLoc>
          </linkElementElement>
          <linkElementElement>
            <latLongSectionLoc>
              <roadName>
                <name>CHICAGO SKYWAY</name>
                <prefix>NONE</prefix>
                <suffix>NONE</suffix>
                <streetType/>
              </roadName>
              <direction>EAST_BOUND</direction>
              <type>FREEWAY</type>
              <startLatLong>
                <latitude>4177700</latitude>
                <longitude>-8763010</longitude>
                <hDatum>NAD83</hDatum>
              </startLatLong>
              <endLatLong>
                <latitude>4170290</latitude>
                <longitude>-8752450</longitude>
                <hDatum>NAD83</hDatum>
              </endLatLong>
            </latLongSectionLoc>
          </linkElementElement>
          <linkElementElement>
            <geometrySectionLoc>
              <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
              <segmentIDs>
                <segmentIDsElement>19844483</segmentIDsElement>
                <segmentIDsElement>19844482</segmentIDsElement>
                <segmentIDsElement>19857354</segmentIDsElement>
                <segmentIDsElement>16897708</segmentIDsElement>
                <segmentIDsElement>16897707</segmentIDsElement>
                <segmentIDsElement>19857413</segmentIDsElement>
                <segmentIDsElement>16897722</segmentIDsElement>
                <segmentIDsElement>16897721</segmentIDsElement>
                <segmentIDsElement>19856645</segmentIDsElement>
                <segmentIDsElement>16881544</segmentIDsElement>
                <segmentIDsElement>16881545</segmentIDsElement>
                <segmentIDsElement>19857880</segmentIDsElement>
                <segmentIDsElement>16881548</segmentIDsElement>
                <segmentIDsElement>16881547</segmentIDsElement>
                <segmentIDsElement>19858736</segmentIDsElement>
                <segmentIDsElement>19858768</segmentIDsElement>
                <segmentIDsElement>19859491</segmentIDsElement>
                <segmentIDsElement>19859827</segmentIDsElement>
                <segmentIDsElement>19859895</segmentIDsElement>
                <segmentIDsElement>19925397</segmentIDsElement>
                <segmentIDsElement>19860384</segmentIDsElement>
                <segmentIDsElement>19860587</segmentIDsElement>
              </segmentIDs>
              <startOffset>0.0</startOffset>
              <endOffset>344.67117</endOffset>
            </geometrySectionLoc>
          </linkElementElement>
        </linkElement>
      </link>
      <linkID>IL-SKYWAY-001</linkID>
      <linkDesc>EB:CHICAGO SKYWAY:DAN RYAN:STATE LINE:IL</linkDesc>
      <!-- TODO: set the length in meters -->
      <length>0</length>
      <locationTimeStamp>0</locationTimeStamp>
      <isBasic>false</isBasic>
      <!-- TODO: set the travel times in seconds -->
      <travelTime>0</travelTime>
      <!-- TODO: set the volume in vehicles/hour-->
      <volume>1222</volume>
      <!-- TODO: set the speed in meter/second-->
      <speed>15.99</speed>
      <!-- TODO: set the occupancy in percentage ponits, value needs to be between 0 and 100-->
      <occupancy>22.22</occupancy>
      <!-- TODO: set the congetionLevel acoording to the following:
UNKNOWN_CONGESTION_LEVEL - if unknown
NON_CONGESTION - if speed >= 55 MPH
LIGHT_CONGESTION - if speed >= 35 MPH
MEDIUM_CONGESTION - if speed >= 15 MPH
HEAVY_CONGESTION - if speed < 10 MPH
-->
      <congestionLevel>MEDIUM_CONGESTION</congestionLevel>
      <locStatus>LOCATION_PARTIALLY_RESOLVED_MANUAL</locStatus>
      <dataStatus>FIELD_DATA_NOT_VALIDATED</dataStatus>
      <!-- TODO: set the timestamp to milliseconds after Unix epoch time -->
      <timeStamp>2147483647</timeStamp>
    </dataElement>
    <dataElement>
      <link>
        <linkElement>
          <linkElementElement>
            <crossStreetSectionLoc>
              <roadName>
                <name>CHICAGO SKYWAY</name>
                <prefix>NONE</prefix>
                <suffix>NONE</suffix>
                <streetType/>
              </roadName>
              <direction>WEST_BOUND</direction>
              <type>FREEWAY</type>
              <startFipsCode>
                <stateCode>0</stateCode>
                <countyCode>0</countyCode>
                <cityCode>0</cityCode>
              </startFipsCode>
              <endFipsCode>
                <stateCode>0</stateCode>
                <countyCode>0</countyCode>
                <cityCode>0</cityCode>
              </endFipsCode>
              <fromCrossStreetName>
                <name>STATE LINE</name>
                <prefix>NONE</prefix>
                <suffix>NONE</suffix>
                <streetType/>
              </fromCrossStreetName>
              <fromCrossStreetType>UNKNOWN_ROADWAY_TYPE</fromCrossStreetType>
              <fromStreetDirection>UNKNOWN_DIRECTION_TYPE</fromStreetDirection>
              <startOffset>0.0</startOffset>
              <toCrossStreetName>
                <name>DAN RYAN</name>
                <prefix>NONE</prefix>
                <suffix>NONE</suffix>
                <streetType/>
              </toCrossStreetName>
              <toCrossStreetType>FREEWAY</toCrossStreetType>
              <toStreetDirection>NORTH_BOUND</toStreetDirection>
              <endOffset>0.0</endOffset>
            </crossStreetSectionLoc>
          </linkElementElement>
          <linkElementElement>
            <latLongSectionLoc>
              <roadName>
                <name>CHICAGO SKYWAY</name>
                <prefix>NONE</prefix>
                <suffix>NONE</suffix>
                <streetType/>
              </roadName>
              <direction>WEST_BOUND</direction>
              <type>FREEWAY</type>
              <startLatLong>
                <latitude>4170310</latitude>
                <longitude>-8752450</longitude>
                <hDatum>NAD83</hDatum>
              </startLatLong>
              <endLatLong>
                <latitude>4177860</latitude>
                <longitude>-8763030</longitude>
                <hDatum>NAD83</hDatum>
              </endLatLong>
            </latLongSectionLoc>
          </linkElementElement>
          <linkElementElement>
            <geometrySectionLoc>
              <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
              <segmentIDs>
                <segmentIDsElement>19860567</segmentIDsElement>
                <segmentIDsElement>19860381</segmentIDsElement>
                <segmentIDsElement>19925398</segmentIDsElement>
                <segmentIDsElement>19859894</segmentIDsElement>
                <segmentIDsElement>19859802</segmentIDsElement>
                <segmentIDsElement>19859481</segmentIDsElement>
                <segmentIDsElement>19858797</segmentIDsElement>
                <segmentIDsElement>19858782</segmentIDsElement>
                <segmentIDsElement>16881549</segmentIDsElement>
                <segmentIDsElement>16881550</segmentIDsElement>
                <segmentIDsElement>19857879</segmentIDsElement>
                <segmentIDsElement>19857668</segmentIDsElement>
                <segmentIDsElement>19857213</segmentIDsElement>
                <segmentIDsElement>19856630</segmentIDsElement>
                <segmentIDsElement>16897723</segmentIDsElement>
                <segmentIDsElement>16897724</segmentIDsElement>
                <segmentIDsElement>19857421</segmentIDsElement>
                <segmentIDsElement>16897706</segmentIDsElement>
                <segmentIDsElement>16897705</segmentIDsElement>
                <segmentIDsElement>19855974</segmentIDsElement>
                <segmentIDsElement>19857351</segmentIDsElement>
                <segmentIDsElement>19844457</segmentIDsElement>
                <segmentIDsElement>19844456</segmentIDsElement>
                <segmentIDsElement>19844089</segmentIDsElement>
              </segmentIDs>
              <startOffset>0.0</startOffset>
              <endOffset>12.529964</endOffset>
            </geometrySectionLoc>
          </linkElementElement>
        </linkElement>
      </link>
      <linkID>IL-SKYWAY-002</linkID>
      <linkDesc>WB:CHICAGO SKYWAY:STATE LINE:DAN RYAN:IL</linkDesc>
      <!-- TODO: set the length in meters-->
      <length>0</length>
      <locationTimeStamp>0</locationTimeStamp>
      <isBasic>false</isBasic>
      <!-- TODO: set the travel times in seconds-->
      <travelTime>0</travelTime>
      <!-- TODO: set the volume in vehicles/hour-->
      <volume>1222</volume>
      <!-- TODO: set the speed in meter/second-->
      <speed>45.99</speed>
      <!-- TODO: set the occupancy in percentage ponits, value needs to be between 0 and 100-->
      <occupancy>22.22</occupancy>
      <!-- TODO: set the congetionLevel acoording to the following:
UNKNOWN_CONGESTION_LEVEL - if unknown
NON_CONGESTION - if speed >= 55 MPH
LIGHT_CONGESTION - if speed >= 35 MPH
MEDIUM_CONGESTION - if speed >= 15 MPH
HEAVY_CONGESTION - if speed < 10 MPH
-->
      <congestionLevel>MEDIUM_CONGESTION</congestionLevel>
      <locStatus>LOCATION_PARTIALLY_RESOLVED_MANUAL</locStatus>
      <dataStatus>FIELD_DATA_NOT_VALIDATED</dataStatus>
      <!-- TODO: set the timestamp to milliseconds after Unix epoch time -->
      <timeStamp>2147483647</timeStamp>
    </dataElement>
  </data>
</com.gcmtravel.LinkTrafficReport>
```

### Example DMSReport

```xml
<com.gcmtravel.DMSReport>
  <reportID>IL-TESTTSC-DMS_2018_04_30_23_59_07</reportID>
  <timeStamp>1525150747656</timeStamp>
  <listOfDMS>
    <listOfDMSElement>
      <parent>
        <deviceStatus>OPERATIONAL</deviceStatus>
        <fieldDeviceID>IL-TESTTSC-STEVENSON-N-22</fieldDeviceID>
        <type>DMS_DEVICETYPE</type>
        <location>
          <locationElement>
            <latLongPointLoc>
              <roadName>
                <name>STEVENSON</name>
                <prefix>NONE</prefix>
                <suffix>NONE</suffix>
                <streetType/>
              </roadName>
              <direction>NORTH_BOUND</direction>
              <type>UNKNOWN_ROADWAY_TYPE</type>
              <coord>
                <latitude>4175220</latitude>
                <longitude>-8792576</longitude>
                <hDatum>NAD27</hDatum>
              </coord>
            </latLongPointLoc>
          </locationElement>
        </location>
        <owningAgencyID>IDOT D1</owningAgencyID>
        <locStatus>LOCATION_NOT_VALIDATED</locStatus>
        <dataStatus>FIELD_DATA_NOT_VALIDATED</dataStatus>
        <lastUpdateTime>1525150689639</lastUpdateTime>
        <locationTimeStamp>0</locationTimeStamp>
      </parent>
      <messageSets>
        <messageSetsElement>
          <dmsLines>
            <dmsLinesElement>[jp3][pt30o0][jl3]ROADWORK AHEAD[nl]JOLIET RD - I-294[nl]LEFT LANE CLOSED[np][jp3][pt30o0][jl3]NB JOLIET RD[nl]EXIT[nl]CLOSED</dmsLinesElement>
          </dmsLines>
          <messageExpiration>1525151649639</messageExpiration>
          <lastUpdateTime>1525150689639</lastUpdateTime>
        </messageSetsElement>
      </messageSets>
    </listOfDMSElement>
  </listOfDMS>
</com.gcmtravel.DMSReport>
```

## Validations

The GTIS will validate uploads to make sure the uploaded data is consistent with itself and the current clock time. The following sections describe the validations done for each uploaded data type.

### LinkTrafficReport

The following must be true or the uploaded travel times will not be displayed by TravelMidwest.com. This applies to each *dataElement* tag separately of the LinkTrafficReport:

- There must be at least one *linkElement* tag in the *link* tag
- The *linkID* must be formatted as state-sourcename-id (there must be at least two dash characters)
- The *speed* and the *length/travelTime* must not differ by more than +/- 20%
- The *speed* must be less than 35.76 meters per second (80 MPH)
- The *lastUpdateTime* must be less than than 2 minutes ahead of the current clock time
- The *lastUpdateTime* must be less than 7.5 minutes old
- The *occupancy* must be less than 90 (percent)
- The *volume* must be less than 8,800 (vehicles/lane/hr)
- The //length / travelTime //must be greater than 2.2352 meters per second (5 MPH)
- None of the following:
  - The *congestionLevel //is not UNKNOWN_CONGESTION_LEVEL and the //speed* is greater than 0
  - The *congestionLevel* is NON_CONGESTION and the *speed* is less than 24.14 meters per second (54 MPH)
  - The *congestionLevel* is LIGHT_CONGESTION and the *speed* is less than 15.2 meters per second (34 MPH) or the *speed* is greater than 25.03 meters per second (56 MPH)
  - The *congestionLevel* is MEDIUM_CONGESTION and the *speed* is less than 6.3 meters per second (14 MPH) or the *speed* is greater than 16.1 meters per second (36 MPH)
  - The *congestionLevel* is HEAVY_CONGESTION and the *speed* is greater than 7.1 meters per second (16 MPH)

Only *dataElement* tags that fail these validations will be rejected.

### VDSReport

The following must be true or the uploaded VDSReport will not be accepted by the GTIS. This applies to each *listOfVDSElement* tag in the VDSReport:

- There must be at least one *locationElement* tag in the *location* tag
- The //fieldDeviceID //must be formatted as state-sourcename-id (there must be at least two dash characters)
- The *lastUpdateTime* must be less than 2 minutes ahead of the current clock time
- The *lastUpdateTime* must be less than 7.5 minutes old
- The *locationTimeStamp* must be less than 2 minutes ahead of the current clock time
- The *detectorizationRatio* must be less than 0, greater than 0, or less than or equal to 1 (note that -1 means unknown)
- The *occupancy* must be less than 90 (percent)
- The *volume* must be less than 8,800 (vehicles/lane/hr)
- The *speed* must be less than 40.23 meters per second (90 MPH)

## Troubleshooting

### HTTP over TLS

Note that connections over HTTPS are required for authentication and upload. Network connections to port 80 (HTTP) are automatically redirected to port 443 (HTTPS), but if your client application does not support redirection (HTTP status code 301) your application must explicitly specify `https` in the upload URL.

### HTTP Status Code: *413 Payload Too Large*

For security and reliability reasons, all modern web servers and related systems typically cap the maximum upload size. We currently support up to **10 MB per upload**. If you experience a HTTP status code 413 — aka. "Content Too Large" / "Payload Too Large" / "Request Entity Too Large" — please confirm the upload size.

In some cases a local firewall/proxy system may also enforce an upload/download limit. If so, please contact your local IT staff for assistance.

## Receiving Data from the Gateway

The Gateway can provide traffic data in a number of formats depending on the format of data:

- XML - See the XML and Camera Image Download Manual.
- JSON - See the Gateway API
- CSV - See Camera Meta-Data (cameraInfo.csv)

## Versions

There are two versions of the Incident XML content supported and provided by the GTIS.  The XML document version is contained in the root tag:

```xml
<com.gcmtravel.IncidentReport version="2.0">
 <com.gcmtravel.IncidentReportElement>
  <parent>
   <type>INCIDENT_EVENT_TYPE</type>
   <roadwayEventID>IL-WAZE1-INCIDENT.2025.1.9.14.6327046</roadwayEventID>
   <description/>
.
.
</com.gcmtravel.IncidentReport>
```

If the version attribute is missing, then the XML is assumed to be version 1.0.

### Receiving XML Version 2 Files

At the time of writing, the only XML file that supports version 2.0 is the Incident file.

- [https://travelmidwest.com/lmiga/IncidentReport.xml.gz](https://travelmidwest.com/lmiga/IncidentReport.xml.gz) is version 1.0
- [https://travelmidwest.com/lmiga/IncidentReportV2.xml.gz](https://travelmidwest.com/lmiga/IncidentReportV2.xml.gz) is version 2.0

### Sending XML Version 2 Files

When sending XML data to the GTIS, both 1.0 and 2.0 are supported by detecting the version attribute in the uploaded content.

## Gateway XML Reference

### Detector Report XSchema for VDSReport.xml.gz

The following XSchema defines the format of VDSReport.xml:

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:simpleType name="com.gcmtravel.DeviceType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="VDS_DEVICETYPE"/>
      <xs:enumeration value="DMS_DEVICETYPE"/>
      <xs:enumeration value="HAR_DEVICETYPE"/>
      <xs:enumeration value="WSS_DEVICETYPE"/>
      <xs:enumeration value="OTHER_DEVICETYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.FIPSCode">
    <xs:sequence>
      <xs:element name="stateCode" type="xs:int"/>
      <xs:element name="countyCode" type="xs:int"/>
      <xs:element name="cityCode" type="xs:int"/>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="com.gcmtravel.FieldDataValidationStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="FIELD_DATA_NOT_VALIDATED"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_AUTO"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_MANUAL"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.FieldDeviceStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_FIELD_DEVICE_STATUS"/>
      <xs:enumeration value="NONE_FIELD_DEVICE_STATUS"/>
      <xs:enumeration value="OPERATIONAL"/>
      <xs:enumeration value="OPERATIONAL_BUT_DEGRADED"/>
      <xs:enumeration value="NON_OPERATIONAL"/>
      <xs:enumeration value="COMMUNICATOINS_FAILURE"/>
      <xs:enumeration value="DOWN_FOR_MAINTENANCE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.HDatumType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NAD27"/>
      <xs:enumeration value="NAD83"/>
      <xs:enumeration value="WGS84"/>
      <xs:enumeration value="WGS84_PLUS_EGM96"/>
      <xs:enumeration value="OTHER_HDATUM_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.LocationResolutionStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="LOCATION_NO_LOCATION"/>
      <xs:enumeration value="LOCATION_NON_SRA"/>
      <xs:enumeration value="LOCATION_PARTIALLY_NON_SRA"/>
      <xs:enumeration value="LOCATION_NOT_VALIDATED"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_AUTO"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_AUTO"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_DIRECTION_TYPE"/>
      <xs:enumeration value="EAST_BOUND"/>
      <xs:enumeration value="WEST_BOUND"/>
      <xs:enumeration value="SOUTH_BOUND"/>
      <xs:enumeration value="NORTH_BOUND"/>
      <xs:enumeration value="SOUTH_EAST_BOUND"/>
      <xs:enumeration value="SOUTH_WEST_BOUND"/>
      <xs:enumeration value="NORTH_EAST_BOUND"/>
      <xs:enumeration value="NORTH_WEST_BOUND"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_ROADWAY_TYPE"/>
      <xs:enumeration value="FREEWAY"/>
      <xs:enumeration value="FREEWAY_EXPRESS"/>
      <xs:enumeration value="FREEWAY_HOV"/>
      <xs:enumeration value="FREEWAY_REVERSIBLE"/>
      <xs:enumeration value="ARTERIAL"/>
      <xs:enumeration value="LOCAL_ROAD"/>
      <xs:enumeration value="RAMP"/>
      <xs:enumeration value="OTHER_ROADWAY_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.SegmentDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="REF_TO_NONREF"/>
      <xs:enumeration value="NONREF_TO_REF"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.StreetNameAffix">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NONE"/>
      <xs:enumeration value="N"/>
      <xs:enumeration value="NE"/>
      <xs:enumeration value="E"/>
      <xs:enumeration value="SE"/>
      <xs:enumeration value="S"/>
      <xs:enumeration value="SW"/>
      <xs:enumeration value="W"/>
      <xs:enumeration value="NW"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.VDSType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_VDS_TYPE"/>
      <xs:enumeration value="LOOP"/>
      <xs:enumeration value="VISION"/>
      <xs:enumeration value="ACOUSTIC"/>
      <xs:enumeration value="INFRARED"/>
      <xs:enumeration value="RADAR"/>
      <xs:enumeration value="MICROWAVE"/>
      <xs:enumeration value="OTHER_VDS_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.GeometryPoint">
    <xs:sequence>
      <xs:element name="direction" type="com.gcmtravel.SegmentDirectionType"/>
      <xs:element name="segmentID" type="xs:long"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLong">
    <xs:sequence>
      <xs:element name="latitude" type="xs:int"/>
      <xs:element name="longitude" type="xs:int"/>
      <xs:element name="hDatum" type="com.gcmtravel.HDatumType"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayName">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="prefix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="suffix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="streetType" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.AddressPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="addressNumber" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LandmarkPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="landmarkName" type="xs:string"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLongPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="coord" type="com.gcmtravel.LatLong"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.MilePointPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="milePoint" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.CrossStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="crossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="crossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="crossStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RampPoint">
    <xs:sequence>
      <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.BetweenStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offsetPercentage" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.PointLocationProfile">
    <xs:choice>
      <xs:element name="latLongPointLoc" type="com.gcmtravel.LatLongPoint"/>
      <xs:element name="landmarkPointLoc" type="com.gcmtravel.LandmarkPoint"/>
      <xs:element name="addressPointLoc" type="com.gcmtravel.AddressPoint"/>
      <xs:element name="milePointPointLoc" type="com.gcmtravel.MilePointPoint"/>
      <xs:element name="crossStreetPointLoc" type="com.gcmtravel.CrossStreetPoint"/>
      <xs:element name="rampPointLoc" type="com.gcmtravel.RampPoint"/
      <xs:element name="betweenStreetPointLoc" type="com.gcmtravel.BetweenStreetPoint"/>
      <xs:element name="geometryPointLoc" type="com.gcmtravel.GeometryPoint"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.FieldDevice">
    <xs:sequence>
      <xs:element name="deviceStatus" type="com.gcmtravel.FieldDeviceStatus"/>
      <xs:element name="fieldDeviceID" type="xs:string"/>
      <xs:element name="type" type="com.gcmtravel.DeviceType"/>
      <xs:element name="location">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="locationElement" type="com.gcmtravel.PointLocationProfile"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="owningAgencyID" type="xs:string"/>
      <xs:element name="locStatus" type="com.gcmtravel.LocationResolutionStatus"/>
      <xs:element name="dataStatus" type="com.gcmtravel.FieldDataValidationStatus"/>
      <xs:element name="lastUpdateTime" type="xs:long"/>
      <xs:element name="locationTimeStamp" type="xs:long"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.VDS">
    <xs:sequence>
      <xs:element name="parent" type="com.gcmtravel.FieldDevice"/>
      <xs:element name="type" type="com.gcmtravel.VDSType"/>
      <xs:element name="volume" type="xs:short"/>
      <xs:element name="occupancy" type="xs:double"/>
      <xs:element name="speed" type="xs:double"/>
      <xs:element name="isSpeedTrap" type="xs:boolean"/>
      <xs:element name="detectorizationRatio" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="com.gcmtravel.VDSReport">
    <xs:complexType>
      <xs:sequence minOccurs="0" maxOccurs="unbounded">
        <xs:element name="com.gcmtravel.VDSReportElement" type="com.gcmtravel.VDS"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

### Sample Detector Report

The following is a sample VDSReport.xml:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<com.gcmtravel.VDSReport>
  <com.gcmtravel.VDSReportElement>
    <parent>
      <deviceStatus>OPERATIONAL</deviceStatus>
      <fieldDeviceID>IL-TSC-I_80-W-717</fieldDeviceID>
      <type>VDS_DEVICETYPE</type>
      <location>
        <locationElement>
          <latLongPointLoc>
            <roadName>
              <name>I-80</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>WEST_BOUND</direction>
            <type>FREEWAY</type>
            <coord>
              <latitude>4155080</latitude>
              <longitude>-8781200</longitude>
              <hDatum>NAD83</hDatum>
            </coord>
          </latLongPointLoc>
        </locationElement>
        <locationElement>
          <crossStreetPointLoc>
            <roadName>
              <name>I-80</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>WEST_BOUND</direction>
            <type>FREEWAY</type>
            <fips>
              <stateCode>17</stateCode>
              <countyCode>197</countyCode>
              <cityCode>99197</cityCode>
            </fips>
            <crossStreetName>
              <name>80TH</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType>AVE</streetType>
            </crossStreetName>
            <crossStreetType>ARTERIAL</crossStreetType>
            <crossStreetDirection>NORTH_BOUND</crossStreetDirection>
            <offset>-0.0</offset>
          </crossStreetPointLoc>
        </locationElement>
        <locationElement>
          <geometryPointLoc>
            <direction>REF_TO_NONREF</direction>
            <segmentID>19931150</segmentID>
            <offset>1110.2383</offset>
          </geometryPointLoc>
        </locationElement>
        <locationElement>
          <milePointPointLoc>
            <roadName>
              <name>I-80</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>WEST_BOUND</direction>
            <type>FREEWAY</type>
            <fips>
              <stateCode>17</stateCode>
              <countyCode>197</countyCode>
              <cityCode>99197</cityCode>
            </fips>
            <milePoint>237836.81</milePoint>
          </milePointPointLoc>
        </locationElement>
      </location>
      <owningAgencyID>TSC</owningAgencyID>
      <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
      <dataStatus>FIELD_DATA_NOT_VALIDATED</dataStatus>
      <lastUpdateTime>1057735080432</lastUpdateTime>
      <locationTimeStamp>0</locationTimeStamp>
    </parent>
    <type>LOOP</type>
    <volume>120</volume>
    <occupancy>2.0</occupancy>
    <speed>11.938045</speed>
    <isSpeedTrap>false</isSpeedTrap>
    <detectorizationRatio>50.0</detectorizationRatio>
  </com.gcmtravel.VDSReportElement>
  <com.gcmtravel.VDSReportElement>
    <parent>
      <deviceStatus>OPERATIONAL</deviceStatus>
      <fieldDeviceID>IL-TSC-IL_53-S-795</fieldDeviceID>
      <type>VDS_DEVICETYPE</type>
      <location>
        <locationElement>
          <latLongPointLoc>
            <roadName>
              <name>IL-53</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>SOUTH_BOUND</direction>
            <type>FREEWAY</type>
            <coord>
              <latitude>4211170</latitude>
              <longitude>-8800300</longitude>
              <hDatum>NAD83</hDatum>
            </coord>
          </latLongPointLoc>
        </locationElement>
        <locationElement>
          <crossStreetPointLoc>
            <roadName>
              <name>IL-53</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>SOUTH_BOUND</direction>
            <type>FREEWAY</type>
            <fips>
              <stateCode>17</stateCode>
              <countyCode>31</countyCode>
              <cityCode>2154</cityCode>
            </fips>
            <crossStreetName>
              <name>PALATINE</name>
              <prefix>W</prefix>
              <suffix>NONE</suffix>
              <streetType>RD</streetType>
            </crossStreetName>
            <crossStreetType>ARTERIAL</crossStreetType>
            <crossStreetDirection>EAST_BOUND</crossStreetDirection>
            <offset>-362.4306</offset>
          </crossStreetPointLoc>
        </locationElement>
        <locationElement>
          <geometryPointLoc>
            <direction>REF_TO_NONREF</direction>
            <segmentID>16880531</segmentID>
            <offset>35.510563</offset>
          </geometryPointLoc>
        </locationElement>
      </location>
      <owningAgencyID>TSC</owningAgencyID>
      <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
      <dataStatus>FIELD_DATA_NOT_VALIDATED</dataStatus>
      <lastUpdateTime>1057735080432</lastUpdateTime>
      <locationTimeStamp>0</locationTimeStamp>
    </parent>
    <type>LOOP</type>
    <volume>0</volume>
    <occupancy>0.0</occupancy>
    <speed>24.587292</speed>
    <isSpeedTrap>false</isSpeedTrap>
    <detectorizationRatio>50.0</detectorizationRatio>
  </com.gcmtravel.VDSReportElement>
</com.gcmtravel.VDSReport>
```

### Incident Report XSchema Version 1 for IncidentReport.xml.gz

The following XSchema defines the format of IncidentReport.xml for version 1:

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:simpleType name="com.gcmtravel.DetectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_DETECTION_TYPE"/>
      <xs:enumeration value="DETECTED_BY_POLICE"/>
      <xs:enumeration value="DETECTED_BY_TRANSIT"/>
      <xs:enumeration value="DETECTED_BY_HIGHWAY_PATROL"/>
      <xs:enumeration value="DETECTED_BY_CCTV"/>
      <xs:enumeration value="DETECTED_BY_AERIAL_SURVEILLANCE"/>
      <xs:enumeration value="DETECTED_BY_AUTOMATED_DETECTION"/>
      <xs:enumeration value="DETECTED_BY_TRAFFIC_INFO_SERVICES"/>
      <xs:enumeration value="DETECTED_BY_COMMERCIAL_FLEET_OPERATOR"/>
      <xs:enumeration value="DETECTED_BY_OTHER_PUBLIC_AGENCY"/>
      <xs:enumeration value="DETECTED_BY_CITIZEN"/>
      <xs:enumeration value="OTHER_DETECTION_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.EventConfidenceLevel">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_EVENT_CONFIDENCE_LEVEL"/>
      <xs:enumeration value="LOW_EVENT_CONFIDENCE_LEVEL"/>
      <xs:enumeration value="MEDIUM_EVENT_CONFIDENCE_LEVEL"/>
      <xs:enumeration value="HIGH_EVENT_CONFIDENCE_LEVEL"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.EventSeverity">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_EVENT_SEVERITY"/>
      <xs:enumeration value="NONE_EVENT_SEVERITY"/>
      <xs:enumeration value="MINOR_EVENT_SEVERITY"/>
      <xs:enumeration value="MEDIUM_EVENT_SEVERITY"/>
      <xs:enumeration value="MAJOR_EVENT_SEVERITY"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.EventState">
    <xs:restriction base="xs:string">
      <xs:enumeration value="EVENT_NEW_AUTO"/>
      <xs:enumeration value="EVENT_NEW_MANUAL"/>
      <xs:enumeration value="EVENT_NEW_FROM_UNRESOLVABLE_MANUAL"/>
      <xs:enumeration value="EVENT_RESURRECTED_AUTO"/>
      <xs:enumeration value="EVENT_RESURRECTED_MANUAL"/>
      <xs:enumeration value="EVENT_UPDATED_WITH_NEW_SOURCE_DATA_AUTO"/>
      <xs:enumeration value="EVENT_UPDATED_AS_RESULT_OF_MERGE_AUTO"/>
      <xs:enumeration value="EVENT_UPDATED_AS_RESULT_OF_MERGE_MANUAL"/>
      <xs:enumeration value="EVENT_UPDATED_MANUAL"/>
      <xs:enumeration value="EVENT_CANCELED_AS_RESULT_OF_MERGE_AUTO"/>
      <xs:enumeration value="EVENT_CANCELED_AS_RESULT_OF_MERGE_MANUAL"/>
      <xs:enumeration value="EVENT_CANCELED_BY_SOURCE_AUTO"/>
      <xs:enumeration value="EVENT_CANCELED_BY_SOURCE_MANUAL"/>
      <xs:enumeration value="EVENT_TIME_EXPIRED_AUTO"/>
      <xs:enumeration value="EVENT_CLOSED_MANUAL"/>
      <xs:enumeration value="EVENT_CLOSED_BY_SOURCE_AUTO"/>
      <xs:enumeration value="EVENT_DELETION_IMMINENT"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.EventType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="INCIDENT_EVENT_TYPE"/>
      <xs:enumeration value="ROADWORK_EVENT_TYPE"/>
      <xs:enumeration value="SPECIAL_EVENT_TYPE"/>
      <xs:enumeration value="OTHER_EVENT_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.FIPSCode">
    <xs:sequence>
      <xs:element name="stateCode" type="xs:int"/>
      <xs:element name="countyCode" type="xs:int"/>
      <xs:element name="cityCode" type="xs:int"/>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="com.gcmtravel.FieldDataValidationStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="FIELD_DATA_NOT_VALIDATED"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_AUTO"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_MANUAL"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.HDatumType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NAD27"/>
      <xs:enumeration value="NAD83"/>
      <xs:enumeration value="WGS84"/>
      <xs:enumeration value="WGS84_PLUS_EGM96"/>
      <xs:enumeration value="OTHER_HDATUM_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.IncidentCounts">
    <xs:sequence>
      <xs:element name="automobileCount" type="xs:short"/>
      <xs:element name="bicycleCount" type="xs:short"/>
      <xs:element name="busCount" type="xs:short"/>
      <xs:element name="constructionVehicleCount" type="xs:short"/>
      <xs:element name="dotVehicleCount" type="xs:short"/>
      <xs:element name="heavyTruckCount" type="xs:short"/>
      <xs:element name="lightTruckCount" type="xs:short"/>
      <xs:element name="motorcycleCount" type="xs:short"/>
      <xs:element name="motorhomeCount" type="xs:short"/>
      <xs:element name="otherVehicleCount" type="xs:short"/>
      <xs:element name="pedestrianCount" type="xs:short"/>
      <xs:element name="tractorCount" type="xs:short"/>
      <xs:element name="trainCount" type="xs:short"/>
      <xs:element name="unknownTypeVehicleCount" type="xs:short"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.IncidentFeatures">
    <xs:sequence>
      <xs:element name="hasAnimalCarcass" type="xs:boolean"/>
      <xs:element name="hasAnimalHit" type="xs:boolean"/>
      <xs:element name="hasCargoSpill" type="xs:boolean"/>
      <xs:element name="hasDebris" type="xs:boolean"/>
      <xs:element name="hasDisabledVehicle" type="xs:boolean"/>
      <xs:element name="hasEarthquake" type="xs:boolean"/>
      <xs:element name="hasEntrapment" type="xs:boolean"/>
      <xs:element name="hasFallenTree" type="xs:boolean"/>
      <xs:element name="hasFallenUtilityStructure" type="xs:boolean"/>
      <xs:element name="hasFlood" type="xs:boolean"/>
      <xs:element name="hasHazmat" type="xs:boolean"/>
      <xs:element name="hasIce" type="xs:boolean"/>
      <xs:element name="hasLiveAnimal" type="xs:boolean"/>
      <xs:element name="hasMedicalAssistanceNeeded" type="xs:boolean"/>
      <xs:element name="hasMudslide" type="xs:boolean"/>
      <xs:element name="hasPedestrianHit" type="xs:boolean"/>
      <xs:element name="hasPedestrianInRoadway" type="xs:boolean"/>
      <xs:element name="hasOtherBlockage" type="xs:boolean"/>
      <xs:element name="hasOtherPropertyDamage" type="xs:boolean"/>
      <xs:element name="hasRoadsideDistraction" type="xs:boolean"/>
      <xs:element name="hasRoadsideObjectFire" type="xs:boolean"/>
      <xs:element name="hasRoadwayStructureDamage" type="xs:boolean"/>
      <xs:element name="hasSnow" type="xs:boolean"/>
      <xs:element name="hasStoppedVehicle" type="xs:boolean"/>
      <xs:element name="hasVehicleFire" type="xs:boolean"/>
      <xs:element name="hasVehicleOverturned" type="xs:boolean"/>
      <xs:element name="hasVehicleRoadsideObjectCollision" type="xs:boolean"/>
      <xs:element name="hasVehicleVehicleCollision" type="xs:boolean"/>
      <xs:element name="hasTruckJackKnifed" type="xs:boolean"/>
      <xs:element name="isAccident" type="xs:boolean"/>
      <xs:element name="isHitAndRun" type="xs:boolean"/>
      <xs:element name="isInWorkZone" type="xs:boolean"/>
      <xs:element name="isPoliceAction" type="xs:boolean"/>
      <xs:element name="isTrafficStop" type="xs:boolean"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.IncidentTimes">
    <xs:sequence>
      <xs:element name="occurrenceTime" type="xs:long"/>
      <xs:element name="detectionTime" type="xs:long"/>
      <xs:element name="verificationTime" type="xs:long"/>
      <xs:element name="movedTime" type="xs:long"/>
      <xs:element name="clearedTime" type="xs:long"/>
      <xs:element name="closedTime" type="xs:long"/>
      <xs:element name="archivedTime" type="xs:long"/>
      <xs:element name="estimatedClosureTime" type="xs:long"/>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="com.gcmtravel.LaneImpactType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_LANE_IMPACT"/>
      <xs:enumeration value="NONE_LANE_IMPACT"/>
      <xs:enumeration value="CLOSED"/>
      <xs:enumeration value="IMPASSABLE"/>
      <xs:enumeration value="SPEED_REDUCED"/>
      <xs:enumeration value="LANE_SHIFTED"/>
      <xs:enumeration value="OTHER_LANE_IMPACT"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.LaneType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_LANE_TYPE"/>
      <xs:enumeration value="LANE"/>
      <xs:enumeration value="LEFT_SHOULDER"/>
      <xs:enumeration value="RIGHT_SHOULDER"/>
      <xs:enumeration value="SHOULDER"/>
      <xs:enumeration value="MEDIAN"/>
      <xs:enumeration value="EXPRESS_LANE"/>
      <xs:enumeration value="EXPRESS_ENTRANCE_LANE"/>
      <xs:enumeration value="EXPRESS_EXIT_LANE"/>
      <xs:enumeration value="EXPRESS_CONNECTOR_LANE"/>
      <xs:enumeration value="LEFT_EXPRESS_SHOULDER"/>
      <xs:enumeration value="RIGHT_EXPRESS_SHOULDER"/>
      <xs:enumeration value="EXPRESS_SHOULDER"/>
      <xs:enumeration value="HOV_LANE"/>
      <xs:enumeration value="HOV_ENTRANCE_LANE"/>
      <xs:enumeration value="HOV_EXIT_LANE"/>
      <xs:enumeration value="HOV_CONNECTOR_LANE"/>
      <xs:enumeration value="LEFT_HOV_SHOULDER"/>
      <xs:enumeration value="RIGHT_HOV_SHOULDER"/>
      <xs:enumeration value="HOV_SHOULDER"/>
      <xs:enumeration value="REVERSIBLE_LANE"/>
      <xs:enumeration value="REVERSIBLE_ENTRANCE_LANE"/>
      <xs:enumeration value="REVERSIBLE_EXIT_LANE"/>
      <xs:enumeration value="REVERSIBLE_CONNECTOR_LANE"/>
      <xs:enumeration value="LEFT_REVERSIBLE_SHOULDER"/>
      <xs:enumeration value="RIGHT_REVERSIBLE_SHOULDER"/>
      <xs:enumeration value="REVERSIBLE_SHOULDER"/>
      <xs:enumeration value="OFF_ROAD_LEFT"/>
      <xs:enumeration value="OFF_ROAD_RIGHT"/>
      <xs:enumeration value="OFF_ROAD"/>
      <xs:enumeration value="UNKNOWN_NUMBER_OF_LANES"/>
      <xs:enumeration value="UNKNOWN_NUMBER_OF_LANES_AND_SHOULDERS"/>
      <xs:enumeration value="CENTER_LANE"/>
      <xs:enumeration value="UNSPECIFIED_LANE"/>
      <xs:enumeration value="ALL_LANES"/>
      <xs:enumeration value="ALL_LANES_AND_SHOULDERS"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.LocationResolutionStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="LOCATION_NO_LOCATION"/>
      <xs:enumeration value="LOCATION_NON_SRA"/>
      <xs:enumeration value="LOCATION_PARTIALLY_NON_SRA"/>
      <xs:enumeration value="LOCATION_NOT_VALIDATED"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_AUTO"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_AUTO"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayCondition">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_ROADWAY_CONDITION"/>
      <xs:enumeration value="NONE_ROADWAY_CONDITION"/>
      <xs:enumeration value="DRY"/>
      <xs:enumeration value="WET"/>
      <xs:enumeration value="CHEMICAL_WET"/>
      <xs:enumeration value="SNOW_ICE"/>
      <xs:enumeration value="WET_ICY"/>
      <xs:enumeration value="WET_OIL_SLICK"/>
      <xs:enumeration value="WET_HIGH_WATER"/>
      <xs:enumeration value="OTHER_ROADWAY_CONDITION"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_DIRECTION_TYPE"/>
      <xs:enumeration value="EAST_BOUND"/>
      <xs:enumeration value="WEST_BOUND"/>
      <xs:enumeration value="SOUTH_BOUND"/>
      <xs:enumeration value="NORTH_BOUND"/>
      <xs:enumeration value="SOUTH_EAST_BOUND"/>
      <xs:enumeration value="SOUTH_WEST_BOUND"/>
      <xs:enumeration value="NORTH_EAST_BOUND"/>
      <xs:enumeration value="NORTH_WEST_BOUND"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_ROADWAY_TYPE"/>
      <xs:enumeration value="FREEWAY"/>
      <xs:enumeration value="FREEWAY_EXPRESS"/>
      <xs:enumeration value="FREEWAY_HOV"/>
      <xs:enumeration value="FREEWAY_REVERSIBLE"/>
      <xs:enumeration value="ARTERIAL"/>
      <xs:enumeration value="LOCAL_ROAD"/>
      <xs:enumeration value="RAMP"/>
      <xs:enumeration value="OTHER_ROADWAY_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.SegmentDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="REF_TO_NONREF"/>
      <xs:enumeration value="NONREF_TO_REF"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.StreetNameAffix">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NONE"/>
      <xs:enumeration value="N"/>
      <xs:enumeration value="NE"/>
      <xs:enumeration value="E"/>
      <xs:enumeration value="SE"/>
      <xs:enumeration value="S"/>
      <xs:enumeration value="SW"/>
      <xs:enumeration value="W"/>
      <xs:enumeration value="NW"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.VerificationType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_VERIFICATION_TYPE"/>
      <xs:enumeration value="VERIFIED_BY_POLICE"/>
      <xs:enumeration value="VERIFIED_BY_TRANSIT"/>
      <xs:enumeration value="VERIFIED_BY_HIGHWAY_PATROL"/>
      <xs:enumeration value="VERIFIED_BY_CCTV"/>
      <xs:enumeration value="VERIFIED_BY_AERIAL_SURVEILLANCE"/>
      <xs:enumeration value="VERIFIED_BY_TRAFFIC_INFO_SERVICES"/>
      <xs:enumeration value="VERIFIED_BY_COMMERCIAL_FLEET_OPERATOR"/>
      <xs:enumeration value="VERIFIED_BY_OTHER_PUBLIC_AGENCY"/>
      <xs:enumeration value="OTHER_VERIFICATION_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.WeatherCondition">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_WEATHER_CONDITION"/>
      <xs:enumeration value="NONE_WEATHER_CONDITION"/>
      <xs:enumeration value="HEAVY_RAIN"/>
      <xs:enumeration value="LIGHT_RAIN"/>
      <xs:enumeration value="FOG"/>
      <xs:enumeration value="HAIL"/>
      <xs:enumeration value="SNOW"/>
      <xs:enumeration value="HIGHWIND"/>
      <xs:enumeration value="OTHER_WEATHER_CONDITION"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.GeometryPoint">
    <xs:sequence>
      <xs:element name="direction" type="com.gcmtravel.SegmentDirectionType"/>
      <xs:element name="segmentID" type="xs:long"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLong">
    <xs:sequence>
      <xs:element name="latitude" type="xs:int"/>
      <xs:element name="longitude" type="xs:int"/>
      <xs:element name="hDatum" type="com.gcmtravel.HDatumType"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GeometrySection">
    <xs:sequence>
      <xs:element name="startSegmentDirection" type="com.gcmtravel.SegmentDirectionType"/>
      <xs:element name="segmentIDs">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="segmentIDsElement" type="xs:long"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LaneDesc">
    <xs:sequence>
      <xs:element name="type" type="com.gcmtravel.LaneType"/>
      <xs:element name="laneImpact" type="com.gcmtravel.LaneImpactType"/>
      <xs:element name="laneNumber" type="xs:short"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayName">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="prefix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="suffix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="streetType" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.AddressPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="addressNumber" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LandmarkPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="landmarkName" type="xs:string"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLongPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="coord" type="com.gcmtravel.LatLong"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.MilePointPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="milePoint" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.AddressSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startAddressNumber" type="xs:string"/>
      <xs:element name="endAddressNumber" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LandmarkSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startLandmarkName" type="xs:string"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endLandmarkName" type="xs:string"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLongSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startLatLong" type="com.gcmtravel.LatLong"/>
      <xs:element name="endLatLong" type="com.gcmtravel.LatLong"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.MilePointSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startMilePoint" type="xs:double"/>
      <xs:element name="endMilePoint" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.CrossStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="crossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="crossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="crossStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RampPoint">
    <xs:sequence>
      <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RampSection">
    <xs:sequence>
      <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.BetweenStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offsetPercentage" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.BetweenStreetSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="startPercentage" type="xs:double"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="endPercentage" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.CrossStreetSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.PointLocationProfile">
    <xs:choice>
      <xs:element name="latLongPointLoc" type="com.gcmtravel.LatLongPoint"/>
      <xs:element name="landmarkPointLoc" type="com.gcmtravel.LandmarkPoint"/>
      <xs:element name="addressPointLoc" type="com.gcmtravel.AddressPoint"/>
      <xs:element name="milePointPointLoc" type="com.gcmtravel.MilePointPoint"/>
      <xs:element name="crossStreetPointLoc" type="com.gcmtravel.CrossStreetPoint"/>
      <xs:element name="rampPointLoc" type="com.gcmtravel.RampPoint"/>
      <xs:element name="betweenStreetPointLoc" type="com.gcmtravel.BetweenStreetPoint"/>
      <xs:element name="geometryPointLoc" type="com.gcmtravel.GeometryPoint"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GenericSection">
    <xs:sequence>
      <xs:element name="startPoint" type="com.gcmtravel.PointLocationProfile"/>
      <xs:element name="endPoint" type="com.gcmtravel.PointLocationProfile"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.SectionLocationProfile">
    <xs:choice>
      <xs:element name="latLongSectionLoc" type="com.gcmtravel.LatLongSection"/>
      <xs:element name="landmarkSectionLoc" type="com.gcmtravel.LandmarkSection"/>
      <xs:element name="addressSectionLoc" type="com.gcmtravel.AddressSection"/>
      <xs:element name="milePointSectionLoc" type="com.gcmtravel.MilePointSection"/>
      <xs:element name="crossStreetSectionLoc" type="com.gcmtravel.CrossStreetSection"/>
      <xs:element name="rampSectionLoc" type="com.gcmtravel.RampSection"/>
      <xs:element name="betweenStreetSectionLoc" type="com.gcmtravel.BetweenStreetSection"/>
      <xs:element name="geometrySectionLoc" type="com.gcmtravel.GeometrySection"/>
      <xs:element name="genericSectionLoc" type="com.gcmtravel.GenericSection"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.PointSectionUnion">
    <xs:choice>
      <xs:element name="point">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="pointElement" type="com.gcmtravel.PointLocationProfile"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="section">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="sectionElement" type="com.gcmtravel.SectionLocationProfile"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LinearLocation">
    <xs:sequence>
      <xs:element name="profiles" type="com.gcmtravel.PointSectionUnion"/>
      <xs:element name="textProfile" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayLocation">
    <xs:sequence>
      <xs:element name="linear" type="com.gcmtravel.LinearLocation"/>
      <xs:element name="lane">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="laneElement" type="com.gcmtravel.LaneDesc"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="originalInput" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayEvent">
    <xs:sequence>
      <xs:element name="type" type="com.gcmtravel.EventType"/>
      <xs:element name="comments" type="xs:string"/>
      <xs:element name="confidenceLevel" type="com.gcmtravel.EventConfidenceLevel"/>
      <xs:element name="description" type="xs:string"/>
      <xs:element name="roadwayEventID" type="xs:string"/>
      <xs:element name="rawIDs">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="rawIDsElement" type="xs:string"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="mergedWith">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="mergedWithElement" type="xs:string"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="locations">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="locationsElement" type="com.gcmtravel.RoadwayLocation"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="severity" type="com.gcmtravel.EventSeverity"/>
      <xs:element name="lastUpdateTime" type="xs:long"/>
      <xs:element name="state" type="com.gcmtravel.EventState"/>
      <xs:element name="locStatus" type="com.gcmtravel.LocationResolutionStatus"/>
      <xs:element name="dataStatus" type="com.gcmtravel.FieldDataValidationStatus"/>
      <xs:element name="operators">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="operatorsElement" type="xs:string"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.Incident">
    <xs:sequence>
      <xs:element name="counts" type="com.gcmtravel.IncidentCounts"/>
      <xs:element name="type" type="com.gcmtravel.DetectionType"/>
      <xs:element name="fatalityCount" type="xs:short"/>
      <xs:element name="features" type="com.gcmtravel.IncidentFeatures"/>
      <xs:element name="injuryCount" type="xs:short"/>
      <xs:element name="condition" type="com.gcmtravel.RoadwayCondition"/>
      <xs:element name="parent" type="com.gcmtravel.RoadwayEvent"/>
      <xs:element name="times" type="com.gcmtravel.IncidentTimes"/>
      <xs:element name="verification" type="com.gcmtravel.VerificationType"/>
      <xs:element name="weather" type="com.gcmtravel.WeatherCondition"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="com.gcmtravel.IncidentReport">
    <xs:complexType>
      <xs:sequence minOccurs="0" maxOccurs="unbounded">
        <xs:element name="com.gcmtravel.IncidentReportElement" type="com.gcmtravel.Incident"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

### Sample Incident Report

The following is a sample IncidentReport.xml:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<com.gcmtravel.IncidentReport>
  <com.gcmtravel.IncidentReportElement>
    <counts>
      <automobileCount>0</automobileCount>
      <bicycleCount>0</bicycleCount>
      <busCount>0</busCount>
      <constructionVehicleCount>0</constructionVehicleCount>
      <dotVehicleCount>0</dotVehicleCount>
      <heavyTruckCount>0</heavyTruckCount>
      <lightTruckCount>0</lightTruckCount>
      <motorcycleCount>0</motorcycleCount>
      <motorhomeCount>0</motorhomeCount>
      <otherVehicleCount>0</otherVehicleCount>
      <pedestrianCount>0</pedestrianCount>
      <tractorCount>0</tractorCount>
      <trainCount>0</trainCount>
      <unknownTypeVehicleCount>1</unknownTypeVehicleCount>
    </counts>
    <type>UNKNOWN_DETECTION_TYPE</type>
    <fatalityCount>-1</fatalityCount>
    <features>
      <hasAnimalCarcass>false</hasAnimalCarcass>
      <hasAnimalHit>false</hasAnimalHit>
      <hasCargoSpill>false</hasCargoSpill>
      <hasDebris>false</hasDebris>
      <hasDisabledVehicle>true</hasDisabledVehicle>
      <hasEarthquake>false</hasEarthquake>
      <hasEntrapment>false</hasEntrapment>
      <hasFallenTree>false</hasFallenTree>
      <hasFallenUtilityStructure>false</hasFallenUtilityStructure>
      <hasFlood>false</hasFlood>
      <hasHazmat>false</hasHazmat>
      <hasIce>false</hasIce>
      <hasLiveAnimal>false</hasLiveAnimal>
      <hasMedicalAssistanceNeeded>false</hasMedicalAssistanceNeeded>
      <hasMudslide>false</hasMudslide>
      <hasPedestrianHit>false</hasPedestrianHit>
      <hasPedestrianInRoadway>false</hasPedestrianInRoadway>
      <hasOtherBlockage>false</hasOtherBlockage>
      <hasOtherPropertyDamage>false</hasOtherPropertyDamage>
      <hasRoadsideDistraction>false</hasRoadsideDistraction>
      <hasRoadsideObjectFire>false</hasRoadsideObjectFire>
      <hasRoadwayStructureDamage>false</hasRoadwayStructureDamage>
      <hasSnow>false</hasSnow>
      <hasStoppedVehicle>false</hasStoppedVehicle>
      <hasVehicleFire>false</hasVehicleFire>
      <hasVehicleOverturned>false</hasVehicleOverturned>
      <hasVehicleRoadsideObjectCollision>false</hasVehicleRoadsideObjectCollision>
      <hasVehicleVehicleCollision>false</hasVehicleVehicleCollision>
      <hasTruckJackKnifed>false</hasTruckJackKnifed>
      <isAccident>true</isAccident>
      <isHitAndRun>false</isHitAndRun>
      <isInWorkZone>false</isInWorkZone>
      <isPoliceAction>false</isPoliceAction>
      <isTrafficStop>false</isTrafficStop>
    </features>
    <injuryCount>-1</injuryCount>
    <condition>NONE_ROADWAY_CONDITION</condition>
    <parent>
      <type>INCIDENT_EVENT_TYPE</type>
      <comments><![CDATA[125939|1@12/03/15 02:42:04->2012-03-15-0006 - disabled vehicle Severity: 1 Priority: 10 Impact: 10 I-94 EB/US 41 SB @ W LAYTON AVE EB (B-40-0238 BEGIN)->(4296005,-8793530)->On shoulder or median]]></comments>
      <confidenceLevel>HIGH_EVENT_CONFIDENCE_LEVEL</confidenceLevel>
      <description>Disabled vehicle</description>
      <roadwayEventID>WI-WisDOT-INCIDENT.2012.3.15.2.503716</roadwayEventID>
      <rawIDs>
        <rawIDsElement>WI-WisDOT-INCIDENT-125939</rawIDsElement>
      </rawIDs>
      <mergedWith></mergedWith>
      <locations>
        <locationsElement>
          <linear>
            <profiles>
              <point>
                <pointElement>
                  <crossStreetPointLoc>
                    <roadName>
                      <name>I-94</name>
                      <prefix>NONE</prefix>
                      <suffix>NONE</suffix>
                      <streetType></streetType>
                    </roadName>
                    <direction>EAST_BOUND</direction>
                    <type>UNKNOWN_ROADWAY_TYPE</type>
                    <fips>
                      <stateCode>55</stateCode>
                      <countyCode>79</countyCode>
                      <cityCode>53000</cityCode>
                    </fips>
                    <crossStreetName>
                      <name>Layton</name>
                      <prefix>W</prefix>
                      <suffix>NONE</suffix>
                      <streetType>Ave</streetType>
                    </crossStreetName>
                    <crossStreetType>UNKNOWN_ROADWAY_TYPE</crossStreetType>
                    <crossStreetDirection>WEST_BOUND</crossStreetDirection>
                    <offset>-72.05842</offset>
                  </crossStreetPointLoc
                </pointElement>
                <pointElement>
                  <latLongPointLoc>
                    <roadName>
                      <name>I-94</name>
                      <prefix>NONE</prefix>
                      <suffix>NONE</suffix>
                      <streetType></streetType>
                    </roadName>
                    <direction>EAST_BOUND</direction>
                    <type>UNKNOWN_ROADWAY_TYPE</type>
                    <coord>
                      <latitude>4296004</latitude>
                      <longitude>-8793525</longitude>
                      <hDatum>NAD83</hDatum>
                    </coord>
                  </latLongPointLoc>
                </pointElement>
                <pointElement>
                  <geometryPointLoc>
                    <direction>REF_TO_NONREF</direction>
                    <segmentID>125144450</segmentID>
                    <offset>5.0</offset>
                  </geometryPointLoc>
                </pointElement>
                <pointElement>
                  <milePointPointLoc>
                    <roadName>
                      <name>I-94</name>
                      <prefix>NONE</prefix>
                      <suffix>NONE</suffix>
                      <streetType></streetType>
                    </roadName>
                    <direction>EAST_BOUND</direction>
                    <type>UNKNOWN_ROADWAY_TYPE</type>
                    <fips>
                      <stateCode>55</stateCode>
                      <countyCode>79</countyCode>
                      <cityCode>53000</cityCode>
                    </fips>
                    <milePoint>509577.8</milePoint>
                  </milePointPointLoc>
                </pointElement
              </point>
            </profiles>
            <textProfile></textProfile>
          </linear>
          <lane>
            <laneElement>
              <type>SHOULDER</type>
              <laneImpact>CLOSED</laneImpact>
              <laneNumber>0</laneNumber>
            </laneElement>
          </lane>
          <originalInput></originalInput>
        </locationsElement>
      </locations>
      <severity>MINOR_EVENT_SEVERITY</severity>
      <lastUpdateTime>1331797887634</lastUpdateTime>
      <state>EVENT_CLOSED_BY_SOURCE_AUTO</state>
      <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
      <dataStatus>FIELD_DATA_VALIDATED_AUTO</dataStatus>
      <operators>
        <operatorsElement>WisDOT 511</operatorsElement>
      </operators>
    </parent>
    <times>
      <occurrenceTime>0</occurrenceTime>
      <detectionTime>0</detectionTime>
      <verificationTime>1331797324000</verificationTime>
      <movedTime>0</movedTime>
      <clearedTime>0</clearedTime>
      <closedTime>1331797887634</closedTime>
      <archivedTime>0</archivedTime>
      <estimatedClosureTime>1331800924000</estimatedClosureTime>
    </times>
    <verification>UNKNOWN_VERIFICATION_TYPE</verification>
    <weather>UNKNOWN_WEATHER_CONDITION</weather>
  </com.gcmtravel.IncidentReportElement>
  <com.gcmtravel.IncidentReportElement>
    <counts>
      <automobileCount>1</automobileCount>
      <bicycleCount>0</bicycleCount>
      <busCount>0</busCount>
      <constructionVehicleCount>0</constructionVehicleCount>
      <dotVehicleCount>0</dotVehicleCount>
      <heavyTruckCount>0</heavyTruckCount>
      <lightTruckCount>0</lightTruckCount>
      <motorcycleCount>0</motorcycleCount>
      <motorhomeCount>0</motorhomeCount>
      <otherVehicleCount>0</otherVehicleCount>
      <pedestrianCount>0</pedestrianCount>
      <tractorCount>0</tractorCount>
      <trainCount>0</trainCount>
      <unknownTypeVehicleCount>0</unknownTypeVehicleCount>
    </counts>
    <type>UNKNOWN_DETECTION_TYPE</type>
    <fatalityCount>0</fatalityCount>
    <features>
      <hasAnimalCarcass>false</hasAnimalCarcass>
      <hasAnimalHit>false</hasAnimalHit>
      <hasCargoSpill>false</hasCargoSpill>
      <hasDebris>false</hasDebris>
      <hasDisabledVehicle>false</hasDisabledVehicle>
      <hasEarthquake>false</hasEarthquake>
      <hasEntrapment>false</hasEntrapment>
      <hasFallenTree>false</hasFallenTree>
      <hasFallenUtilityStructure>false</hasFallenUtilityStructure>
      <hasFlood>false</hasFlood>
      <hasHazmat>false</hasHazmat>
      <hasIce>false</hasIce>
      <hasLiveAnimal>false</hasLiveAnimal>
      <hasMedicalAssistanceNeeded>false</hasMedicalAssistanceNeeded>
      <hasMudslide>false</hasMudslide>
      <hasPedestrianHit>false</hasPedestrianHit>
      <hasPedestrianInRoadway>false</hasPedestrianInRoadway>
      <hasOtherBlockage>false</hasOtherBlockage>
      <hasOtherPropertyDamage>false</hasOtherPropertyDamage>
      <hasRoadsideDistraction>false</hasRoadsideDistraction>
      <hasRoadsideObjectFire>false</hasRoadsideObjectFire>
      <hasRoadwayStructureDamage>false</hasRoadwayStructureDamage>
      <hasSnow>false</hasSnow>
      <hasStoppedVehicle>false</hasStoppedVehicle>
      <hasVehicleFire>false</hasVehicleFire>
      <hasVehicleOverturned>false</hasVehicleOverturned>
      <hasVehicleRoadsideObjectCollision>false</hasVehicleRoadsideObjectCollision>
      <hasVehicleVehicleCollision>false</hasVehicleVehicleCollision>
      <hasTruckJackKnifed>false</hasTruckJackKnifed>
      <isAccident>true</isAccident>
      <isHitAndRun>false</isHitAndRun>
      <isInWorkZone>false</isInWorkZone>
      <isPoliceAction>false</isPoliceAction>
      <isTrafficStop>false</isTrafficStop>
    </features>
    <injuryCount>0</injuryCount>
    <condition>UNKNOWN_ROADWAY_CONDITION</condition>
    <parent>
      <type>INCIDENT_EVENT_TYPE</type>
      <comments></comments>
      <confidenceLevel>HIGH_EVENT_CONFIDENCE_LEVEL</confidenceLevel>
      <description></description>
      <roadwayEventID>IL-COMMCENTER-INCIDENT.2012.3.14.7.503457</roadwayEventID>
      <rawIDs>
        <rawIDsElement>IL-COMMCENTER-31f03e059bf06b0b:6002f428:136106337d2:-7fff</rawIDsElement>
      </rawIDs>
      <mergedWith></mergedWith>
      <locations>
        <locationsElement>
          <linear>
            <profiles>
              <point>
                <pointElement>
                  <crossStreetPointLoc>
                    <roadName>
                      <name>I-94</name>
                      <prefix>NONE</prefix>
                      <suffix>NONE</suffix>
                      <streetType></streetType>
                    </roadName>
                    <direction>WEST_BOUND</direction>
                    <type>UNKNOWN_ROADWAY_TYPE</type>
                    <fips>
                      <stateCode>17</stateCode>
                      <countyCode>31</countyCode>
                      <cityCode>10487</cityCode>
                    </fips>
                    <crossStreetName>
                      <name>Dolton</name>
                      <prefix>NONE</prefix>
                      <suffix>NONE</suffix>
                      <streetType>Rd</streetType>
                    </crossStreetName>
                    <crossStreetType>UNKNOWN_ROADWAY_TYPE</crossStreetType>
                    <crossStreetDirection>NORTH_WEST_BOUND</crossStreetDirection>
                    <offset>100.005</offset>
                  </crossStreetPointLoc>
                </pointElement>
                <pointElement>
                  <latLongPointLoc>
                    <roadName>
                      <name>I-94</name>
                      <prefix>NONE</prefix>
                      <suffix>NONE</suffix>
                      <streetType></streetType>
                    </roadName>
                    <direction>WEST_BOUND</direction>
                    <type>UNKNOWN_ROADWAY_TYPE</type>
                    <coord>
                      <latitude>4163526</latitude>
                      <longitude>-8757836</longitude>
                      <hDatum>NAD83</hDatum>
                    </coord>
                  </latLongPointLoc>
                </pointElement>
                <pointElement>
                  <geometryPointLoc>
                    <direction>REF_TO_NONREF</direction>
                    <segmentID>125120807</segmentID>
                    <offset>191.015</offset>
                  </geometryPointLoc>
                </pointElement>
                <pointElement>
                  <milePointPointLoc>
                    <roadName>
                      <name>I-94</name>
                      <prefix>NONE</prefix>
                      <suffix>NONE</suffix>
                      <streetType></streetType>
                    </roadName>
                    <direction>WEST_BOUND</direction>
                    <type>UNKNOWN_ROADWAY_TYPE</type>
                    <fips>
                      <stateCode>17</stateCode>
                      <countyCode>31</countyCode>
                      <cityCode>10487</cityCode>
                    </fips>
                    <milePoint>113416.02</milePoint>
                  </milePointPointLoc>
                </pointElement>
              </point>
            </profiles>
            <textProfile>WB I-94 at 143rd St</textProfile>
          </linear>
          <lane>
            <laneElement>
              <type>ALL_LANES_AND_SHOULDERS</type>
              <laneImpact>CLOSED</laneImpact>
              <laneNumber>-1</laneNumber>
            </laneElement>
          </lane>
          <originalInput></originalInput>
        </locationsElement>
      </locations>
      <severity>MAJOR_EVENT_SEVERITY</severity>
      <lastUpdateTime>1331728030813</lastUpdateTime>
      <state>EVENT_CLOSED_MANUAL</state>
      <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
      <dataStatus>FIELD_DATA_VALIDATED_MANUAL</dataStatus>
      <operators>
        <operatorsElement>mkremer</operatorsElement>
      </operators>
    </parent>
    <times>
      <occurrenceTime>1331726766174</occurrenceTime>
      <detectionTime>0</detectionTime>
      <verificationTime>0</verificationTime>
      <movedTime>0</movedTime>
      <clearedTime>1331728029614</clearedTime>
      <closedTime>1331728029614</closedTime>
      <archivedTime>0</archivedTime>
      <estimatedClosureTime>1331729106174</estimatedClosureTime>
    </times>
    <verification>OTHER_VERIFICATION_TYPE</verification>
    <weather>UNKNOWN_WEATHER_CONDITION</weather>
  </com.gcmtravel.IncidentReportElement>
</com.gcmtravel.IncidentReport>
```

### Incident Report XSchema Version 2 for IncidentReportV2.xml.gz

The version="2.0" IncidentReportV2.xml.gz file is the same as the version 1 file but with a new RoadwayCondition schema as follows:

```xml
<!-- Version 2 -->
<xs:simpleType name="com.gcmtravel.RoadwayCondition">
   <xs:restriction base="xs:string">
     <xs:enumeration value="UNKNOWN_ROADWAY_CONDITION"/>
     <xs:enumeration value="NONE_ROADWAY_CONDITION"/>
     <xs:enumeration value="DRY"/>
     <xs:enumeration value="WET"/>
     <xs:enumeration value="CHEMICAL_WET"/>
     <xs:enumeration value="SNOW_ICE"/>
     <xs:enumeration value="WET_ICY"/>
     <xs:enumeration value="WET_OIL_SLICK"/>
     <xs:enumeration value="WET_HIGH_WATER"/>
     <xs:enumeration value="OTHER_ROADWAY_CONDITION"/>
     <xs:enumeration value="SLUSH"/>
     <xs:enumeration value="ICY_OR_SLIPPERY"/>
     <xs:enumeration value="PACKED_SNOW"/>
     <xs:enumeration value="DRIFTING_SNOW"/>
     <xs:enumeration value="SNOW_COVERED"/>
     <xs:enumeration value="SNOW_PACKED_IN_SPOTS"/>
     <xs:enumeration value="BRIDGE_DECKS_SLIPPERY"/>
   </xs:restriction>
 </xs:simpleType>
```

### Construction Report XSchema for RoadWorkReport.xml.gz

The following XSchema defines the format of RoadWorkReport.xml:

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:simpleType name="com.gcmtravel.EventConfidenceLevel">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_EVENT_CONFIDENCE_LEVEL"/>
      <xs:enumeration value="LOW_EVENT_CONFIDENCE_LEVEL"/>
      <xs:enumeration value="MEDIUM_EVENT_CONFIDENCE_LEVEL"/>
      <xs:enumeration value="HIGH_EVENT_CONFIDENCE_LEVEL"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.EventSeverity">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_EVENT_SEVERITY"/>
      <xs:enumeration value="NONE_EVENT_SEVERITY"/>
      <xs:enumeration value="MINOR_EVENT_SEVERITY"/>
      <xs:enumeration value="MEDIUM_EVENT_SEVERITY"/>
      <xs:enumeration value="MAJOR_EVENT_SEVERITY"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.EventState">
    <xs:restriction base="xs:string">
      <xs:enumeration value="EVENT_NEW_AUTO"/>
      <xs:enumeration value="EVENT_NEW_MANUAL"/>
      <xs:enumeration value="EVENT_NEW_FROM_UNRESOLVABLE_MANUAL"/>
      <xs:enumeration value="EVENT_RESURRECTED_AUTO"/>
      <xs:enumeration value="EVENT_RESURRECTED_MANUAL"/>
      <xs:enumeration value="EVENT_UPDATED_WITH_NEW_SOURCE_DATA_AUTO"/>
      <xs:enumeration value="EVENT_UPDATED_AS_RESULT_OF_MERGE_AUTO"/>
      <xs:enumeration value="EVENT_UPDATED_AS_RESULT_OF_MERGE_MANUAL"/>
      <xs:enumeration value="EVENT_UPDATED_MANUAL"/>
      <xs:enumeration value="EVENT_CANCELED_AS_RESULT_OF_MERGE_AUTO"/>
      <xs:enumeration value="EVENT_CANCELED_AS_RESULT_OF_MERGE_MANUAL"/>
      <xs:enumeration value="EVENT_CANCELED_BY_SOURCE_AUTO"/>
      <xs:enumeration value="EVENT_CANCELED_BY_SOURCE_MANUAL"/>
      <xs:enumeration value="EVENT_TIME_EXPIRED_AUTO"/>
      <xs:enumeration value="EVENT_CLOSED_MANUAL"/>
      <xs:enumeration value="EVENT_CLOSED_BY_SOURCE_AUTO"/>
      <xs:enumeration value="EVENT_DELETION_IMMINENT"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.EventType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="INCIDENT_EVENT_TYPE"/>
      <xs:enumeration value="ROADWORK_EVENT_TYPE"/>
      <xs:enumeration value="SPECIAL_EVENT_TYPE"/>
      <xs:enumeration value="OTHER_EVENT_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.FIPSCode">
    <xs:sequence>
      <xs:element name="stateCode" type="xs:int"/>
      <xs:element name="countyCode" type="xs:int"/>
      <xs:element name="cityCode" type="xs:int"/>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="com.gcmtravel.FieldDataValidationStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="FIELD_DATA_NOT_VALIDATED"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_AUTO"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_MANUAL"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.HDatumType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NAD27"/>
      <xs:enumeration value="NAD83"/>
      <xs:enumeration value="WGS84"/>
      <xs:enumeration value="WGS84_PLUS_EGM96"/>
      <xs:enumeration value="OTHER_HDATUM_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.LaneImpactType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_LANE_IMPACT"/>
      <xs:enumeration value="NONE_LANE_IMPACT"/>
      <xs:enumeration value="CLOSED"/>
      <xs:enumeration value="IMPASSABLE"/>
      <xs:enumeration value="SPEED_REDUCED"/>
      <xs:enumeration value="LANE_SHIFTED"/>
      <xs:enumeration value="OTHER_LANE_IMPACT"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.LaneType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_LANE_TYPE"/>
      <xs:enumeration value="LANE"/>
      <xs:enumeration value="LEFT_SHOULDER"/>
      <xs:enumeration value="RIGHT_SHOULDER"/>
      <xs:enumeration value="SHOULDER"/>
      <xs:enumeration value="MEDIAN"/>
      <xs:enumeration value="EXPRESS_LANE"/>
      <xs:enumeration value="EXPRESS_ENTRANCE_LANE"/>
      <xs:enumeration value="EXPRESS_EXIT_LANE"/>
      <xs:enumeration value="EXPRESS_CONNECTOR_LANE"/>
      <xs:enumeration value="LEFT_EXPRESS_SHOULDER"/>
      <xs:enumeration value="RIGHT_EXPRESS_SHOULDER"/>
      <xs:enumeration value="EXPRESS_SHOULDER"/>
      <xs:enumeration value="HOV_LANE"/>
      <xs:enumeration value="HOV_ENTRANCE_LANE"/>
      <xs:enumeration value="HOV_EXIT_LANE"/>
      <xs:enumeration value="HOV_CONNECTOR_LANE"/>
      <xs:enumeration value="LEFT_HOV_SHOULDER"/>
      <xs:enumeration value="RIGHT_HOV_SHOULDER"/>
      <xs:enumeration value="HOV_SHOULDER"/>
      <xs:enumeration value="REVERSIBLE_LANE"/>
      <xs:enumeration value="REVERSIBLE_ENTRANCE_LANE"/>
      <xs:enumeration value="REVERSIBLE_EXIT_LANE"/>
      <xs:enumeration value="REVERSIBLE_CONNECTOR_LANE"/>
      <xs:enumeration value="LEFT_REVERSIBLE_SHOULDER"/>
      <xs:enumeration value="RIGHT_REVERSIBLE_SHOULDER"/>
      <xs:enumeration value="REVERSIBLE_SHOULDER"/>
      <xs:enumeration value="OFF_ROAD_LEFT"/>
      <xs:enumeration value="OFF_ROAD_RIGHT"/>
      <xs:enumeration value="OFF_ROAD"/>
      <xs:enumeration value="UNKNOWN_NUMBER_OF_LANES"/>
      <xs:enumeration value="UNKNOWN_NUMBER_OF_LANES_AND_SHOULDERS"/>
      <xs:enumeration value="CENTER_LANE"/>
      <xs:enumeration value="UNSPECIFIED_LANE"/>
      <xs:enumeration value="ALL_LANES"/>
      <xs:enumeration value="ALL_LANES_AND_SHOULDERS"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.LocationResolutionStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="LOCATION_NO_LOCATION"/>
      <xs:enumeration value="LOCATION_NON_SRA"/>
      <xs:enumeration value="LOCATION_PARTIALLY_NON_SRA"/>
      <xs:enumeration value="LOCATION_NOT_VALIDATED"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_AUTO"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_AUTO"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadWorkType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_ROAD_WORK_TYPE"/>
      <xs:enumeration value="CONSTRUCTION"/>
      <xs:enumeration value="MAINTENANCE"/>
      <xs:enumeration value="UTILITY_WORK"/>
      <xs:enumeration value="OTHER_ROAD_WORK_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_DIRECTION_TYPE"/>
      <xs:enumeration value="EAST_BOUND"/>
      <xs:enumeration value="WEST_BOUND"/>
      <xs:enumeration value="SOUTH_BOUND"/>
      <xs:enumeration value="NORTH_BOUND"/>
      <xs:enumeration value="SOUTH_EAST_BOUND"/>
      <xs:enumeration value="SOUTH_WEST_BOUND"/>
      <xs:enumeration value="NORTH_EAST_BOUND"/>
      <xs:enumeration value="NORTH_WEST_BOUND"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_ROADWAY_TYPE"/>
      <xs:enumeration value="FREEWAY"/>
      <xs:enumeration value="FREEWAY_EXPRESS"/>
      <xs:enumeration value="FREEWAY_HOV"/>
      <xs:enumeration value="FREEWAY_REVERSIBLE"/>
      <xs:enumeration value="ARTERIAL"/>
      <xs:enumeration value="LOCAL_ROAD"/>
      <xs:enumeration value="RAMP"/>
      <xs:enumeration value="OTHER_ROADWAY_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.SegmentDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="REF_TO_NONREF"/>
      <xs:enumeration value="NONREF_TO_REF"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.StreetNameAffix">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NONE"/>
      <xs:enumeration value="N"/>
      <xs:enumeration value="NE"/>
      <xs:enumeration value="E"/>
      <xs:enumeration value="SE"/>
      <xs:enumeration value="S"/>
      <xs:enumeration value="SW"/>
      <xs:enumeration value="W"/>
      <xs:enumeration value="NW"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.TimePeriod">
    <xs:sequence>
      <xs:element name="startTime" type="xs:long"/>
      <xs:element name="endTime" type="xs:long"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GeometryPoint">
    <xs:sequence>
      <xs:element name="direction" type="com.gcmtravel.SegmentDirectionType"/>
      <xs:element name="segmentID" type="xs:long"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLong">
    <xs:sequence>
      <xs:element name="latitude" type="xs:int"/>
      <xs:element name="longitude" type="xs:int"/>
      <xs:element name="hDatum" type="com.gcmtravel.HDatumType"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GeometrySection">
    <xs:sequence>
      <xs:element name="startSegmentDirection" type="com.gcmtravel.SegmentDirectionType"/>
      <xs:element name="segmentIDs">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="segmentIDsElement" type="xs:long"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LaneDesc">
    <xs:sequence>
      <xs:element name="type" type="com.gcmtravel.LaneType"/>
      <xs:element name="laneImpact" type="com.gcmtravel.LaneImpactType"/>
      <xs:element name="laneNumber" type="xs:short"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayName">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="prefix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="suffix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="streetType" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.AddressPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="addressNumber" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LandmarkPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="landmarkName" type="xs:string"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLongPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="coord" type="com.gcmtravel.LatLong"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.MilePointPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="milePoint" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.AddressSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startAddressNumber" type="xs:string"/>
      <xs:element name="endAddressNumber" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LandmarkSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startLandmarkName" type="xs:string"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endLandmarkName" type="xs:string"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLongSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startLatLong" type="com.gcmtravel.LatLong"/>
      <xs:element name="endLatLong" type="com.gcmtravel.LatLong"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.MilePointSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startMilePoint" type="xs:double"/>
      <xs:element name="endMilePoint" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.CrossStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="crossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="crossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="crossStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RampPoint">
    <xs:sequence>
      <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RampSection">
    <xs:sequence>
      <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.BetweenStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offsetPercentage" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.BetweenStreetSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="startPercentage" type="xs:double"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="endPercentage" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.CrossStreetSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.PointLocationProfile">
    <xs:choice>
      <xs:element name="latLongPointLoc" type="com.gcmtravel.LatLongPoint"/>
      <xs:element name="landmarkPointLoc" type="com.gcmtravel.LandmarkPoint"/>
      <xs:element name="addressPointLoc" type="com.gcmtravel.AddressPoint"/>
      <xs:element name="milePointPointLoc" type="com.gcmtravel.MilePointPoint"/>
      <xs:element name="crossStreetPointLoc" type="com.gcmtravel.CrossStreetPoint"/>
      <xs:element name="rampPointLoc" type="com.gcmtravel.RampPoint"/>
      <xs:element name="betweenStreetPointLoc" type="com.gcmtravel.BetweenStreetPoint"/>
      <xs:element name="geometryPointLoc" type="com.gcmtravel.GeometryPoint"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GenericSection">
    <xs:sequence>
      <xs:element name="startPoint" type="com.gcmtravel.PointLocationProfile"/>
      <xs:element name="endPoint" type="com.gcmtravel.PointLocationProfile"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.SectionLocationProfile">
    <xs:choice>
      <xs:element name="latLongSectionLoc" type="com.gcmtravel.LatLongSection"/>
      <xs:element name="landmarkSectionLoc" type="com.gcmtravel.LandmarkSection"/>
      <xs:element name="addressSectionLoc" type="com.gcmtravel.AddressSection"/>
      <xs:element name="milePointSectionLoc" type="com.gcmtravel.MilePointSection"/>
      <xs:element name="crossStreetSectionLoc" type="com.gcmtravel.CrossStreetSection"/>
      <xs:element name="rampSectionLoc" type="com.gcmtravel.RampSection"/>
      <xs:element name="betweenStreetSectionLoc" type="com.gcmtravel.BetweenStreetSection"/>
      <xs:element name="geometrySectionLoc" type="com.gcmtravel.GeometrySection"/>
      <xs:element name="genericSectionLoc" type="com.gcmtravel.GenericSection"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.PointSectionUnion">
    <xs:choice>
      <xs:element name="point">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="pointElement" type="com.gcmtravel.PointLocationProfile"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="section">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="sectionElement" type="com.gcmtravel.SectionLocationProfile"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LinearLocation">
    <xs:sequence>
      <xs:element name="profiles" type="com.gcmtravel.PointSectionUnion"/>
      <xs:element name="textProfile" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayLocation">
    <xs:sequence>
      <xs:element name="linear" type="com.gcmtravel.LinearLocation"/>
      <xs:element name="lane">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="laneElement" type="com.gcmtravel.LaneDesc"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="originalInput" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayEvent">
    <xs:sequence>
      <xs:element name="type" type="com.gcmtravel.EventType"/>
      <xs:element name="comments" type="xs:string"/>
      <xs:element name="confidenceLevel" type="com.gcmtravel.EventConfidenceLevel"/>
      <xs:element name="description" type="xs:string"/>
      <xs:element name="roadwayEventID" type="xs:string"/>
      <xs:element name="rawIDs">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="rawIDsElement" type="xs:string"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="mergedWith">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="mergedWithElement" type="xs:string"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="locations">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="locationsElement" type="com.gcmtravel.RoadwayLocation"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="severity" type="com.gcmtravel.EventSeverity"/>
      <xs:element name="lastUpdateTime" type="xs:long"/>
      <xs:element name="state" type="com.gcmtravel.EventState"/>
      <xs:element name="locStatus" type="com.gcmtravel.LocationResolutionStatus"/>
      <xs:element name="dataStatus" type="com.gcmtravel.FieldDataValidationStatus"/>
      <xs:element name="operators">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="operatorsElement" type="xs:string"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.ScheduledEvent">
    <xs:sequence>
      <xs:element name="actualTimes">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="actualTimesElement" type="com.gcmtravel.TimePeriod"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="parent" type="com.gcmtravel.RoadwayEvent"/>
      <xs:element name="scheduledTimes">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="scheduledTimesElement" type="com.gcmtravel.TimePeriod"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="isMovingOperation" type="xs:boolean"/>
      <xs:element name="isWeatherDependent" type="xs:boolean"/>
      <xs:element name="isActive" type="xs:boolean"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadWork">
    <xs:sequence>
      <xs:element name="type" type="com.gcmtravel.RoadWorkType"/>
      <xs:element name="parent" type="com.gcmtravel.ScheduledEvent"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="com.gcmtravel.RoadWorkReport">
    <xs:complexType>
      <xs:sequence minOccurs="0" maxOccurs="unbounded">
        <xs:element name="com.gcmtravel.RoadWorkReportElement" type="com.gcmtravel.RoadWork"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

### Sample Construction Report

The following is a sample RoadWorkReport.xml:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<com.gcmtravel.RoadWorkReport>
  <com.gcmtravel.RoadWorkReportElement>
    <type>CONSTRUCTION</type>
    <parent>
      <actualTimes></actualTimes>
      <parent>
        <type>INCIDENT_EVENT_TYPE</type>
        <comments></comments>
        <confidenceLevel>MEDIUM_EVENT_CONFIDENCE_LEVEL</confidenceLevel>
        <description>Partial exit ramp closed</description>
        <roadwayEventID>IL-IDOT-ROADWORK.2003.7.8.19.196</roadwayEventID>
        <rawIDs>
          <rawIDsElement>IL-IDOT-13d0ca2558b1899e:859a68:f6445eb72b:2fed</rawIDsElement>
        </rawIDs>
        <mergedWith></mergedWith>
        <locations>
          <locationsElement>
            <linear>
              <profiles>
                <point>
                  <pointElement>
                    <geometryPointLoc>
                      <direction>REF_TO_NONREF</direction>
                      <segmentID>16891241</segmentID>
                      <offset>311.45145</offset>
                    </geometryPointLoc>
                  </pointElement>
                  <pointElement>
                    <crossStreetPointLoc>
                      <roadName>
                        <name>I-57</name>
                        <prefix>NONE</prefix>
                        <suffix>NONE</suffix>
                        <streetType></streetType>
                      </roadName>
                      <direction>NORTH_BOUND</direction>
                      <type>FREEWAY</type>
                      <fips>
                        <stateCode>17</stateCode>
                        <countyCode>197</countyCode>
                        <cityCode>99197</cityCode>
                      </fips>
                      <crossStreetName>
                        <name>WILMINGTON</name>
                        <prefix>W</prefix>
                        <suffix>NONE</suffix>
                        <streetType>RD</streetType>
                      </crossStreetName>
                      <crossStreetType>ARTERIAL</crossStreetType>
                      <crossStreetDirection>EAST_BOUND</crossStreetDirection>
                      <offset>5.6953095E-6</offset>
                    </crossStreetPointLoc>
                  </pointElement>
                  <pointElement>
                    <latLongPointLoc>
                      <roadName>
                        <name>I-57</name>
                        <prefix>NONE</prefix>
                        <suffix>NONE</suffix>
                        <streetType></streetType>
                      </roadName>
                      <direction>NORTH_BOUND</direction>
                      <type>FREEWAY</type>
                      <coord>
                        <latitude>4132444</latitude>
                        <longitude>-8781972</longitude>
                        <hDatum>NAD83</hDatum>
                      </coord>
                    </latLongPointLoc>
                  </pointElement>
                  <pointElement>
                    <milePointPointLoc>
                      <roadName>
                        <name>I-57</name>
                        <prefix>NONE</prefix>
                        <suffix>NONE</suffix>
                        <streetType></streetType>
                      </roadName>
                      <direction>NORTH_BOUND</direction>
                      <type>FREEWAY</type>
                      <fips>
                        <stateCode>17</stateCode>
                        <countyCode>197</countyCode>
                        <cityCode>99197</cityCode>
                      </fips>
                      <milePoint>526247.1</milePoint>
                    </milePointPointLoc>
                  </pointElement>
                </point>
              </profiles>
              <textProfile><![CDATA[NB I-57 @ EB W WILMINGTON RD in UNINC WILL COUNTY in ILLINOIS]]></textProfile>
            </linear>
            <lane>
              <laneElement>
                <type>RIGHT_SHOULDER</type>
                <laneImpact>CLOSED</laneImpact>
                <laneNumber>1</laneNumber>
              </laneElement>
            </lane>
            <originalInput></originalInput>
          </locationsElement>
        </locations>
        <severity>MINOR_EVENT_SEVERITY</severity>
        <lastUpdateTime>1057711524686</lastUpdateTime>
        <state>EVENT_UPDATED_MANUAL</state>
        <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
        <dataStatus>FIELD_DATA_VALIDATED_MANUAL</dataStatus>
        <operators>
          <operatorsElement>operator</operatorsElement>
        </operators>
      </parent>
      <scheduledTimes>
        <scheduledTimesElement>
          <startTime>1057759200000</startTime>
          <endTime>1057780800000</endTime>
        </scheduledTimesElement>
      </scheduledTimes>
      <isMovingOperation>false</isMovingOperation>
      <isWeatherDependent>false</isWeatherDependent>
      <isActive>false</isActive>
    </parent>
  </com.gcmtravel.RoadWorkReportElement>
  <com.gcmtravel.RoadWorkReportElement>
    <type>CONSTRUCTION</type>
    <parent>
      <actualTimes></actualTimes>
      <parent>
        <type>INCIDENT_EVENT_TYPE</type>
        <comments></comments>
        <confidenceLevel>MEDIUM_EVENT_CONFIDENCE_LEVEL</confidenceLevel>
        <description></description>
        <roadwayEventID>IL-IDOT-ROADWORK.2003.7.8.19.188</roadwayEventID>
        <rawIDs>
          <rawIDsElement>IL-IDOT-13d0ca2558b1899e:859a68:f6445eb72b:-19d2</rawIDsElement>
        </rawIDs>
        <mergedWith></mergedWith>
        <locations>
          <locationsElement>
            <linear>
              <profiles>
                <point>
                  <pointElement>
                    <geometryPointLoc>
                      <direction>REF_TO_NONREF</direction>
                      <segmentID>16891192</segmentID>
                      <offset>236.07625</offset>
                    </geometryPointLoc>
                  </pointElement>
                  <pointElement>
                    <crossStreetPointLoc>
                      <roadName>
                        <name>I-55</name>
                        <prefix>NONE</prefix>
                        <suffix>NONE</suffix>
                        <streetType></streetType>
                      </roadName>
                      <direction>SOUTH_BOUND</direction>
                      <type>FREEWAY</type>
                      <fips>
                        <stateCode>17</stateCode>
                        <countyCode>197</countyCode>
                        <cityCode>99197</cityCode>
                      </fips>
                      <crossStreetName>
                        <name>LORENZO</name>
                        <prefix>NONE</prefix>
                        <suffix>NONE</suffix>
                        <streetType>RD</streetType>
                      </crossStreetName>
                      <crossStreetType>ARTERIAL</crossStreetType>
                      <crossStreetDirection>SOUTH_BOUND</crossStreetDirection>
                      <offset>-1.0696705E-5</offset>
                    </crossStreetPointLoc>
                  </pointElement>
                  <pointElement>
                    <latLongPointLoc>
                      <roadName>
                        <name>I-55</name>
                        <prefix>NONE</prefix>
                        <suffix>NONE</suffix>
                        <streetType></streetType>
                      </roadName>
                      <direction>SOUTH_BOUND</direction>
                      <type>FREEWAY</type>
                      <coord>
                        <latitude>4134405</latitude>
                        <longitude>-8819174</longitude>
                        <hDatum>NAD83</hDatum>
                      </coord>
                    </latLongPointLoc>
                  </pointElement>
                  <pointElement>
                    <milePointPointLoc>
                      <roadName>
                        <name>I-55</name>
                        <prefix>NONE</prefix>
                        <suffix>NONE</suffix>
                        <streetType></streetType>
                      </roadName>
                      <direction>SOUTH_BOUND</direction>
                      <type>FREEWAY</type>
                      <fips>
                        <stateCode>17</stateCode>
                        <countyCode>197</countyCode>
                        <cityCode>99197</cityCode>
                      </fips>
                      <milePoint>386778.1</milePoint>
                    </milePointPointLoc>
                  </pointElement>
                </point>
              </profiles>
              <textProfile><![CDATA[SB I-55 @ SB LORENZO RD in UNINC WILL COUNTY in ILLINOIS]]></textProfile>
            </linear>
            <lane></lane>
            <originalInput></originalInput>
          </locationsElement>
          <locationsElement>
            <linear>
              <profiles>
                <point>
                  <pointElement>
                    <geometryPointLoc>
                      <direction>REF_TO_NONREF</direction>
                      <segmentID>16891190</segmentID>
                      <offset>168.07439</offset>
                    </geometryPointLoc>
                  </pointElement>
                  <pointElement>
                    <crossStreetPointLoc>
                      <roadName>
                        <name>I-55</name>
                        <prefix>NONE</prefix>
                        <suffix>NONE</suffix>
                        <streetType></streetType>
                      </roadName>
                      <direction>NORTH_BOUND</direction>
                      <type>FREEWAY</type>
                      <fips>
                        <stateCode>17</stateCode>
                        <countyCode>197</countyCode>
                        <cityCode>99197</cityCode>
                      </fips>
                      <crossStreetName>
                        <name>LORENZO</name>
                        <prefix>NONE</prefix>
                        <suffix>NONE</suffix>
                        <streetType>RD</streetType>
                      </crossStreetName>
                      <crossStreetType>ARTERIAL</crossStreetType>
                      <crossStreetDirection>SOUTH_BOUND</crossStreetDirection>
                      <offset>-1.696124E-6</offset>
                    </crossStreetPointLoc>
                  </pointElement>
                  <pointElement>
                    <latLongPointLoc>
                      <roadName>
                        <name>I-55</name>
                        <prefix>NONE</prefix>
                        <suffix>NONE</suffix>
                        <streetType></streetType>
                      </roadName>
                      <direction>NORTH_BOUND</direction>
                      <type>FREEWAY</type>
                      <coord>
                        <latitude>4134388</latitude>
                        <longitude>-8819150</longitude>
                        <hDatum>NAD83</hDatum>
                      </coord>
                    </latLongPointLoc>
                  </pointElement>
                  <pointElement>
                    <milePointPointLoc>
                      <roadName>
                        <name>I-55</name>
                        <prefix>NONE</prefix>
                        <suffix>NONE</suffix>
                        <streetType></streetType>
                      </roadName>
                      <direction>NORTH_BOUND</direction>
                      <type>FREEWAY</type>
                      <fips>
                        <stateCode>17</stateCode>
                        <countyCode>197</countyCode>
                        <cityCode>99197</cityCode>
                      </fips>
                      <milePoint>386804.72</milePoint>
                    </milePointPointLoc>
                  </pointElement>
                </point>
              </profiles>
              <textProfile><![CDATA[NB I-55 @ SB LORENZO RD in UNINC WILL COUNTY in ILLINOIS]]></textProfile>
            </linear>
            <lane></lane>
            <originalInput></originalInput>
          </locationsElement>
        </locations>
        <severity>MINOR_EVENT_SEVERITY</severity>
        <lastUpdateTime>1057709779607</lastUpdateTime>
        <state>EVENT_UPDATED_MANUAL</state>
        <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
        <dataStatus>FIELD_DATA_VALIDATED_MANUAL</dataStatus>
        <operators>
          <operatorsElement>operator</operatorsElement>
        </operators>
      </parent>
      <scheduledTimes>
        <scheduledTimesElement>
          <startTime>1057708800000</startTime>
          <endTime>1057748400000</endTime>
        </scheduledTimesElement>
      </scheduledTimes>
      <isMovingOperation>false</isMovingOperation>
      <isWeatherDependent>false</isWeatherDependent>
      <isActive>true</isActive>
    </parent>
  </com.gcmtravel.RoadWorkReportElement>
</com.gcmtravel.RoadWorkReport>
```

### Special Event Report XSchema for SpecialEventReport.xml.gz

The following XSchema defines the format of SpecialEventReport.xml:

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:simpleType name="com.gcmtravel.EventConfidenceLevel">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_EVENT_CONFIDENCE_LEVEL"/>
      <xs:enumeration value="LOW_EVENT_CONFIDENCE_LEVEL"/>
      <xs:enumeration value="MEDIUM_EVENT_CONFIDENCE_LEVEL"/>
      <xs:enumeration value="HIGH_EVENT_CONFIDENCE_LEVEL"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.EventSeverity">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_EVENT_SEVERITY"/>
      <xs:enumeration value="NONE_EVENT_SEVERITY"/>
      <xs:enumeration value="MINOR_EVENT_SEVERITY"/>
      <xs:enumeration value="MEDIUM_EVENT_SEVERITY"/>
      <xs:enumeration value="MAJOR_EVENT_SEVERITY"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.EventState">
    <xs:restriction base="xs:string">
      <xs:enumeration value="EVENT_NEW_AUTO"/>
      <xs:enumeration value="EVENT_NEW_MANUAL"/>
      <xs:enumeration value="EVENT_NEW_FROM_UNRESOLVABLE_MANUAL"/>
      <xs:enumeration value="EVENT_RESURRECTED_AUTO"/>
      <xs:enumeration value="EVENT_RESURRECTED_MANUAL"/>
      <xs:enumeration value="EVENT_UPDATED_WITH_NEW_SOURCE_DATA_AUTO"/>
      <xs:enumeration value="EVENT_UPDATED_AS_RESULT_OF_MERGE_AUTO"/>
      <xs:enumeration value="EVENT_UPDATED_AS_RESULT_OF_MERGE_MANUAL"/>
      <xs:enumeration value="EVENT_UPDATED_MANUAL"/>
      <xs:enumeration value="EVENT_CANCELED_AS_RESULT_OF_MERGE_AUTO"/>
      <xs:enumeration value="EVENT_CANCELED_AS_RESULT_OF_MERGE_MANUAL"/>
      <xs:enumeration value="EVENT_CANCELED_BY_SOURCE_AUTO"/>
      <xs:enumeration value="EVENT_CANCELED_BY_SOURCE_MANUAL"/>
      <xs:enumeration value="EVENT_TIME_EXPIRED_AUTO"/>
      <xs:enumeration value="EVENT_CLOSED_MANUAL"/>
      <xs:enumeration value="EVENT_CLOSED_BY_SOURCE_AUTO"/>
      <xs:enumeration value="EVENT_DELETION_IMMINENT"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.EventType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="INCIDENT_EVENT_TYPE"/>
      <xs:enumeration value="ROADWORK_EVENT_TYPE"/>
      <xs:enumeration value="SPECIAL_EVENT_TYPE"/>
      <xs:enumeration value="OTHER_EVENT_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.FIPSCode">
    <xs:sequence>
      <xs:element name="stateCode" type="xs:int"/>
      <xs:element name="countyCode" type="xs:int"/>
      <xs:element name="cityCode" type="xs:int"/>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="com.gcmtravel.FieldDataValidationStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="FIELD_DATA_NOT_VALIDATED"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_AUTO"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_MANUAL"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.HDatumType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NAD27"/>
      <xs:enumeration value="NAD83"/>
      <xs:enumeration value="WGS84"/>
      <xs:enumeration value="WGS84_PLUS_EGM96"/>
      <xs:enumeration value="OTHER_HDATUM_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.LaneImpactType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_LANE_IMPACT"/>
      <xs:enumeration value="NONE_LANE_IMPACT"/>
      <xs:enumeration value="CLOSED"/>
      <xs:enumeration value="IMPASSABLE"/>
      <xs:enumeration value="SPEED_REDUCED"/>
      <xs:enumeration value="LANE_SHIFTED"/>
      <xs:enumeration value="OTHER_LANE_IMPACT"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.LaneType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_LANE_TYPE"/>
      <xs:enumeration value="LANE"/>
      <xs:enumeration value="LEFT_SHOULDER"/>
      <xs:enumeration value="RIGHT_SHOULDER"/>
      <xs:enumeration value="SHOULDER"/>
      <xs:enumeration value="MEDIAN"/>
      <xs:enumeration value="EXPRESS_LANE"/>
      <xs:enumeration value="EXPRESS_ENTRANCE_LANE"/>
      <xs:enumeration value="EXPRESS_EXIT_LANE"/>
      <xs:enumeration value="EXPRESS_CONNECTOR_LANE"/>
      <xs:enumeration value="LEFT_EXPRESS_SHOULDER"/>
      <xs:enumeration value="RIGHT_EXPRESS_SHOULDER"/>
      <xs:enumeration value="EXPRESS_SHOULDER"/>
      <xs:enumeration value="HOV_LANE"/>
      <xs:enumeration value="HOV_ENTRANCE_LANE"/>
      <xs:enumeration value="HOV_EXIT_LANE"/>
      <xs:enumeration value="HOV_CONNECTOR_LANE"/>
      <xs:enumeration value="LEFT_HOV_SHOULDER"/>
      <xs:enumeration value="RIGHT_HOV_SHOULDER"/>
      <xs:enumeration value="HOV_SHOULDER"/>
      <xs:enumeration value="REVERSIBLE_LANE"/>
      <xs:enumeration value="REVERSIBLE_ENTRANCE_LANE"/>
      <xs:enumeration value="REVERSIBLE_EXIT_LANE"/>
      <xs:enumeration value="REVERSIBLE_CONNECTOR_LANE"/>
      <xs:enumeration value="LEFT_REVERSIBLE_SHOULDER"/>
      <xs:enumeration value="RIGHT_REVERSIBLE_SHOULDER"/>
      <xs:enumeration value="REVERSIBLE_SHOULDER"/>
      <xs:enumeration value="OFF_ROAD_LEFT"/>
      <xs:enumeration value="OFF_ROAD_RIGHT"/>
      <xs:enumeration value="OFF_ROAD"/>
      <xs:enumeration value="UNKNOWN_NUMBER_OF_LANES"/>
      <xs:enumeration value="UNKNOWN_NUMBER_OF_LANES_AND_SHOULDERS"/>
      <xs:enumeration value="CENTER_LANE"/>
      <xs:enumeration value="UNSPECIFIED_LANE"/>
      <xs:enumeration value="ALL_LANES"/>
      <xs:enumeration value="ALL_LANES_AND_SHOULDERS"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.LocationResolutionStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="LOCATION_NO_LOCATION"/>
      <xs:enumeration value="LOCATION_NON_SRA"/>
      <xs:enumeration value="LOCATION_PARTIALLY_NON_SRA"/>
      <xs:enumeration value="LOCATION_NOT_VALIDATED"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_AUTO"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_AUTO"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_DIRECTION_TYPE"/>
      <xs:enumeration value="EAST_BOUND"/>
      <xs:enumeration value="WEST_BOUND"/>
      <xs:enumeration value="SOUTH_BOUND"/>
      <xs:enumeration value="NORTH_BOUND"/>
      <xs:enumeration value="SOUTH_EAST_BOUND"/>
      <xs:enumeration value="SOUTH_WEST_BOUND"/>
      <xs:enumeration value="NORTH_EAST_BOUND"/>
      <xs:enumeration value="NORTH_WEST_BOUND"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayType">
     <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_ROADWAY_TYPE"/>
      <xs:enumeration value="FREEWAY"/>
      <xs:enumeration value="FREEWAY_EXPRESS"/>
      <xs:enumeration value="FREEWAY_HOV"/>
      <xs:enumeration value="FREEWAY_REVERSIBLE"/>
      <xs:enumeration value="ARTERIAL"/>
      <xs:enumeration value="LOCAL_ROAD"/>
      <xs:enumeration value="RAMP"/>
      <xs:enumeration value="OTHER_ROADWAY_TYPE"/>
     </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.SegmentDirectionType">
     <xs:restriction base="xs:string">
      <xs:enumeration value="REF_TO_NONREF"/>
      <xs:enumeration value="NONREF_TO_REF"/>
     </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.SpecialEventType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_SPECIAL_EVENT_TYPE"/>
      <xs:enumeration value="PARADE"/>
      <xs:enumeration value="STADIUM_EVENT"/>
      <xs:enumeration value="CONVENTION"/>
      <xs:enumeration value="AMUSEMENT_PARK"/>
      <xs:enumeration value="ROAD_RACE"/>
      <xs:enumeration value="MOTORCADE"/>
      <xs:enumeration value="OTHER_SPECIAL_EVENT_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.StreetNameAffix">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NONE"/>
      <xs:enumeration value="N"/>
      <xs:enumeration value="NE"/>
      <xs:enumeration value="E"/>
      <xs:enumeration value="SE"/>
      <xs:enumeration value="S"/>
      <xs:enumeration value="SW"/>
      <xs:enumeration value="W"/>
      <xs:enumeration value="NW"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.TimePeriod">
    <xs:sequence>
      <xs:element name="startTime" type="xs:long"/>
      <xs:element name="endTime" type="xs:long"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GeometryPoint">
    <xs:sequence>
      <xs:element name="direction" type="com.gcmtravel.SegmentDirectionType"/>
      <xs:element name="segmentID" type="xs:long"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLong">
    <xs:sequence>
      <xs:element name="latitude" type="xs:int"/>
      <xs:element name="longitude" type="xs:int"/>
      <xs:element name="hDatum" type="com.gcmtravel.HDatumType"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GeometrySection">
    <xs:sequence>
      <xs:element name="startSegmentDirection" type="com.gcmtravel.SegmentDirectionType"/>
      <xs:element name="segmentIDs">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="segmentIDsElement" type="xs:long"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LaneDesc">
    <xs:sequence>
      <xs:element name="type" type="com.gcmtravel.LaneType"/>
      <xs:element name="laneImpact" type="com.gcmtravel.LaneImpactType"/>
      <xs:element name="laneNumber" type="xs:short"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayName">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="prefix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="suffix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="streetType" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.AddressPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="addressNumber" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LandmarkPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="landmarkName" type="xs:string"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLongPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="coord" type="com.gcmtravel.LatLong"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.MilePointPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="milePoint" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.AddressSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startAddressNumber" type="xs:string"/>
      <xs:element name="endAddressNumber" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LandmarkSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startLandmarkName" type="xs:string"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endLandmarkName" type="xs:string"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLongSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startLatLong" type="com.gcmtravel.LatLong"/>
      <xs:element name="endLatLong" type="com.gcmtravel.LatLong"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.MilePointSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startMilePoint" type="xs:double"/>
      <xs:element name="endMilePoint" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.CrossStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="crossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="crossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="crossStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RampPoint">
    <xs:sequence>
      <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RampSection">
    <xs:sequence>
      <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.BetweenStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offsetPercentage" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.BetweenStreetSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="startPercentage" type="xs:double"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="endPercentage" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.CrossStreetSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.PointLocationProfile">
    <xs:choice>
      <xs:element name="latLongPointLoc" type="com.gcmtravel.LatLongPoint"/>
      <xs:element name="landmarkPointLoc" type="com.gcmtravel.LandmarkPoint"/>
      <xs:element name="addressPointLoc" type="com.gcmtravel.AddressPoint"/>
      <xs:element name="milePointPointLoc" type="com.gcmtravel.MilePointPoint"/>
      <xs:element name="crossStreetPointLoc" type="com.gcmtravel.CrossStreetPoint"/>
      <xs:element name="rampPointLoc" type="com.gcmtravel.RampPoint"/>
      <xs:element name="betweenStreetPointLoc" type="com.gcmtravel.BetweenStreetPoint"/>
      <xs:element name="geometryPointLoc" type="com.gcmtravel.GeometryPoint"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GenericSection">
    <xs:sequence>
      <xs:element name="startPoint" type="com.gcmtravel.PointLocationProfile"/>
      <xs:element name="endPoint" type="com.gcmtravel.PointLocationProfile"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.SectionLocationProfile">
    <xs:choice>
      <xs:element name="latLongSectionLoc" type="com.gcmtravel.LatLongSection"/>
      <xs:element name="landmarkSectionLoc" type="com.gcmtravel.LandmarkSection"/>
      <xs:element name="addressSectionLoc" type="com.gcmtravel.AddressSection"/>
      <xs:element name="milePointSectionLoc" type="com.gcmtravel.MilePointSection"/>
      <xs:element name="crossStreetSectionLoc" type="com.gcmtravel.CrossStreetSection"/>
      <xs:element name="rampSectionLoc" type="com.gcmtravel.RampSection"/>
      <xs:element name="betweenStreetSectionLoc" type="com.gcmtravel.BetweenStreetSection"/>
      <xs:element name="geometrySectionLoc" type="com.gcmtravel.GeometrySection"/>
      <xs:element name="genericSectionLoc" type="com.gcmtravel.GenericSection"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.PointSectionUnion">
    <xs:choice>
      <xs:element name="point">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="pointElement" type="com.gcmtravel.PointLocationProfile"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="section">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="sectionElement" type="com.gcmtravel.SectionLocationProfile"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LinearLocation">
    <xs:sequence>
      <xs:element name="profiles" type="com.gcmtravel.PointSectionUnion"/>
      <xs:element name="textProfile" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayLocation">
    <xs:sequence>
      <xs:element name="linear" type="com.gcmtravel.LinearLocation"/>
      <xs:element name="lane">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
           <xs:element name="laneElement" type="com.gcmtravel.LaneDesc"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="originalInput" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayEvent">
    <xs:sequence>
      <xs:element name="type" type="com.gcmtravel.EventType"/>
      <xs:element name="comments" type="xs:string"/>
      <xs:element name="confidenceLevel" type="com.gcmtravel.EventConfidenceLevel"/>
      <xs:element name="description" type="xs:string"/>
      <xs:element name="roadwayEventID" type="xs:string"/>
      <xs:element name="rawIDs">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="rawIDsElement" type="xs:string"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="mergedWith">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="mergedWithElement" type="xs:string"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="locations">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="locationsElement" type="com.gcmtravel.RoadwayLocation"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="severity" type="com.gcmtravel.EventSeverity"/>
      <xs:element name="lastUpdateTime" type="xs:long"/>
      <xs:element name="state" type="com.gcmtravel.EventState"/>
      <xs:element name="locStatus" type="com.gcmtravel.LocationResolutionStatus"/>
      <xs:element name="dataStatus" type="com.gcmtravel.FieldDataValidationStatus"/>
      <xs:element name="operators">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="operatorsElement" type="xs:string"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.ScheduledEvent">
    <xs:sequence>
      <xs:element name="actualTimes">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="actualTimesElement" type="com.gcmtravel.TimePeriod"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="parent" type="com.gcmtravel.RoadwayEvent"/>
      <xs:element name="scheduledTimes">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="scheduledTimesElement" type="com.gcmtravel.TimePeriod"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="isMovingOperation" type="xs:boolean"/>
      <xs:element name="isWeatherDependent" type="xs:boolean"/>
      <xs:element name="isActive" type="xs:boolean"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.SpecialEvent">
    <xs:sequence>
      <xs:element name="parent" type="com.gcmtravel.ScheduledEvent"/>
      <xs:element name="type" type="com.gcmtravel.SpecialEventType"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="com.gcmtravel.SpecialEventReport">
    <xs:complexType>
      <xs:sequence minOccurs="0" maxOccurs="unbounded">
        <xs:element name="com.gcmtravel.SpecialEventReportElement" type="com.gcmtravel.SpecialEvent"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

### Sample Special Event Report

The following is a sample SpecialEventReport.xml:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<com.gcmtravel.SpecialEventReport>
  <com.gcmtravel.SpecialEventReportElement>
    <parent>
      <actualTimes></actualTimes>
      <parent>
        <type>SPECIAL_EVENT_TYPE</type>
        <comments></comments>
        <confidenceLevel>HIGH_EVENT_CONFIDENCE_LEVEL</confidenceLevel>
        <description>Milwaukee Bucks vs Memphis Grizzlies at Bradley Center @ 7:30 PM</description>
        <roadwayEventID>WI-WisDOT-SPECIAL_EVENT.2012.2.29.22.500583</roadwayEventID>
        <rawIDs>
          <rawIDsElement>WI-WisDOT-583c10bfdbd326ba:-7a2c22a6:135cc452287:-7fd9</rawIDsElement>
        </rawIDs>
        <mergedWith></mergedWith>
        <locations>
          <locationsElement>
            <linear>
              <profiles>
                <point>
                  <pointElement>
                    <addressPointLoc>
                      <roadName>
                        <name>6th</name>
                        <prefix>N</prefix>
                        <suffix>NONE</suffix>
                        <streetType>St</streetType>
                      </roadName>
                      <direction>NORTH_BOUND</direction>
                      <type>UNKNOWN_ROADWAY_TYPE</type>
                      <fips>
                        <stateCode>55</stateCode>
                        <countyCode>79</countyCode>
                        <cityCode>53000</cityCode>
                      </fips>
                      <addressNumber>1030</addressNumber>
                    </addressPointLoc>
                  </pointElement>
                  <pointElement>
                    <crossStreetPointLoc>
                      <roadName>
                        <name>6th</name>
                        <prefix>N</prefix>
                        <suffix>NONE</suffix>
                        <streetType>St</streetType>
                      </roadName>
                      <direction>NORTH_BOUND</direction>
                      <type>UNKNOWN_ROADWAY_TYPE</type>
                      <fips>
                        <stateCode>55</stateCode>
                        <countyCode>79</countyCode>
                        <cityCode>53000</cityCode>
                      </fips>
                      <crossStreetName>
                        <name>US-18</name>
                        <prefix>NONE</prefix>
                        <suffix>NONE</suffix>
                        <streetType></streetType>
                      </crossStreetName>
                      <crossStreetType>UNKNOWN_ROADWAY_TYPE</crossStreetType>
                      <crossStreetDirection>WEST_BOUND</crossStreetDirection>
                      <offset>46.836994</offset>
                    </crossStreetPointLoc>
                  </pointElement>
                  <pointElement>
                    <latLongPointLoc>
                      <roadName>
                        <name>6th</name>
                        <prefix>N</prefix>
                        <suffix>NONE</suffix>
                        <streetType>St</streetType>
                      </roadName>
                      <direction>NORTH_BOUND</direction>
                      <type>UNKNOWN_ROADWAY_TYPE</type>
                      <coord>
                        <latitude>4304336</latitude>
                        <longitude>-8791887</longitude>
                        <hDatum>NAD83</hDatum>
                      </coord>
                    </latLongPointLoc>
                  </pointElement>
                  <pointElement>
                    <geometryPointLoc>
                      <direction>REF_TO_NONREF</direction>
                      <segmentID>33383215</segmentID>
                      <offset>46.836998</offset>
                    </geometryPointLoc>
                  </pointElement>
                </point>
              </profiles>
              <textProfile>Milwaukee Bucks vs Memphis Grizzlies at Bradley Center, Milwaukee, Milwaukee County, Wisconsin</textProfile>
            </linear>
            <lane>
              <laneElement>
                <type>LEFT_SHOULDER</type>
                <laneImpact>NONE_LANE_IMPACT</laneImpact>
                <laneNumber>-1</laneNumber>
              </laneElement>
              <laneElement>
                <type>LANE</type>
                <laneImpact>NONE_LANE_IMPACT</laneImpact>
                <laneNumber>1</laneNumber>
              </laneElement>
              <laneElement>
                <type>LANE</type>
                <laneImpact>NONE_LANE_IMPACT</laneImpact>
                <laneNumber>2</laneNumber>
              </laneElement>
              <laneElement>
                <type>LANE</type>
                <laneImpact>NONE_LANE_IMPACT</laneImpact>
                <laneNumber>3</laneNumber>
              </laneElement>
              <laneElement>
                <type>RIGHT_SHOULDER</type>
                <laneImpact>NONE_LANE_IMPACT</laneImpact>
                <laneNumber>-1</laneNumber>
              </laneElement>
            </lane>
            <originalInput></originalInput>
          </locationsElement>
        </locations>
        <severity>MINOR_EVENT_SEVERITY</severity>
        <lastUpdateTime>1330575336246</lastUpdateTime>
        <state>EVENT_NEW_AUTO</state>
        <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
        <dataStatus>FIELD_DATA_VALIDATED_AUTO</dataStatus>
        <operators>
          <operatorsElement>dhernandez</operatorsElement>
        </operators>
      </parent>
      <scheduledTimes>
        <scheduledTimesElement>
          <startTime>1333240200000</startTime>
          <endTime>1333251000000</endTime>
        </scheduledTimesElement>
      </scheduledTimes>
      <isMovingOperation>false</isMovingOperation>
      <isWeatherDependent>false</isWeatherDependent>
      <isActive>false</isActive>
    </parent>
    <type>STADIUM_EVENT</type>
  </com.gcmtravel.SpecialEventReportElement>
  <com.gcmtravel.SpecialEventReportElement>
    <parent>
      <actualTimes></actualTimes>
      <parent>
        <type>SPECIAL_EVENT_TYPE</type>
        <comments></comments>
        <confidenceLevel>HIGH_EVENT_CONFIDENCE_LEVEL</confidenceLevel>
        <description><![CDATA[Blackhawks vs Canucks tonight 7pm at the United Center. Expect additional traffic in the area.]]></description>
        <roadwayEventID>IL-CDOT-SPECIAL_EVENT.2012.3.21.15.505173</roadwayEventID>
        <rawIDs>
          <rawIDsElement>IL-CDOT-583c10bfdbd326ba:15162bca:13636e545c5:-7fff</rawIDsElement>
        </rawIDs>
        <mergedWith></mergedWith>
        <locations>
          <locationsElement>
            <linear>
              <profiles>
                <point>
                  <pointElement>
                    <addressPointLoc>
                      <roadName>
                        <name>Madison</name>
                        <prefix>W</prefix>
                        <suffix>NONE</suffix>
                        <streetType>St</streetType>
                      </roadName>
                      <direction>EAST_BOUND</direction>
                      <type>UNKNOWN_ROADWAY_TYPE</type>
                      <fips>
                        <stateCode>17</stateCode>
                        <countyCode>31</countyCode>
                        <cityCode>14000</cityCode>
                      </fips>
                      <addressNumber>1901</addressNumber>
                    </addressPointLoc>
                  </pointElement>
                  <pointElement>
                    <crossStreetPointLoc>
                      <roadName>
                        <name>Madison</name>
                        <prefix>W</prefix>
                        <suffix>NONE</suffix>
                        <streetType>St</streetType>
                      </roadName>
                      <direction>EAST_BOUND</direction>
                      <type>UNKNOWN_ROADWAY_TYPE</type>
                      <fips>
                        <stateCode>17</stateCode>
                        <countyCode>31</countyCode>
                        <cityCode>14000</cityCode>
                      </fips>
                      <crossStreetName>
                        <name>Wood</name>
                        <prefix>S</prefix>
                        <suffix>NONE</suffix>
                        <streetType>St</streetType>
                      </crossStreetName>
                      <crossStreetType>UNKNOWN_ROADWAY_TYPE</crossStreetType>
                      <crossStreetDirection>NORTH_BOUND</crossStreetDirection>
                      <offset>-201.17026</offset>
                    </crossStreetPointLoc>
                  </pointElement>
                  <pointElement>
                    <latLongPointLoc>
                      <roadName>
                        <name>Madison</name>
                        <prefix>W</prefix>
                        <suffix>NONE</suffix>
                        <streetType>St</streetType>
                      </roadName>
                      <direction>EAST_BOUND</direction>
                      <type>UNKNOWN_ROADWAY_TYPE</type>
                      <coord>
                        <latitude>4188133</latitude>
                        <longitude>-8767417</longitude>
                        <hDatum>NAD83</hDatum>
                      </coord>
                    </latLongPointLoc>
                  </pointElement>
                  <pointElement>
                    <geometryPointLoc>
                      <direction>REF_TO_NONREF</direction>
                      <segmentID>125145398</segmentID>
                      <offset>204.979</offset>
                    </geometryPointLoc>
                  </pointElement>
                </point>
              </profiles>
              <textProfile>Blackhawks Vs Canucks at United Center, Chicago, Cook County, Illinois</textProfile>
            </linear>
            <lane>
              <laneElement>
                <type>LEFT_SHOULDER</type>
                <laneImpact>NONE_LANE_IMPACT</laneImpact>
                <laneNumber>-1</laneNumber>
              </laneElement>
              <laneElement>
                <type>LANE</type>
                <laneImpact>NONE_LANE_IMPACT</laneImpact>
                <laneNumber>1</laneNumber>
              </laneElement>
              <laneElement>
                <type>LANE</type>
                <laneImpact>NONE_LANE_IMPACT</laneImpact>
                <laneNumber>2</laneNumber>
              </laneElement>
              <laneElement>
                <type>LANE</type>
                <laneImpact>NONE_LANE_IMPACT</laneImpact>
                <laneNumber>3</laneNumber>
              </laneElement>
              <laneElement>
                <type>RIGHT_SHOULDER</type>
                <laneImpact>NONE_LANE_IMPACT</laneImpact>
                <laneNumber>-1</laneNumber>
              </laneElement>
            </lane>
            <originalInput></originalInput>
          </locationsElement>
        </locations>
        <severity>MINOR_EVENT_SEVERITY</severity>
        <lastUpdateTime>1332370800047</lastUpdateTime>
        <state>EVENT_NEW_AUTO</state>
        <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
        <dataStatus>FIELD_DATA_VALIDATED_AUTO</dataStatus>
        <operators>
          <operatorsElement>spoodipeddi</operatorsElement>
        </operators>
      </parent>
      <scheduledTimes>
        <scheduledTimesElement>
          <startTime>1332370800000</startTime>
          <endTime>1332388800000</endTime>
        </scheduledTimesElement>
      </scheduledTimes>
      <isMovingOperation>false</isMovingOperation>
      <isWeatherDependent>false</isWeatherDependent>
      <isActive>true</isActive>
    </parent>
    <type>STADIUM_EVENT</type>
  </com.gcmtravel.SpecialEventReportElement>
</com.gcmtravel.SpecialEventReport>
```

### Congestion Report XSchema for LinkCongestionReport.xml.gz

The following XSchema defines the format of LinkCongestionReport.xml:

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:simpleType name="com.gcmtravel.CongestionLevelType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_CONGESTION_LEVEL"/>
      <xs:enumeration value="NON_CONGESTION"/>
      <xs:enumeration value="LIGHT_CONGESTION"/>
      <xs:enumeration value="MEDIUM_CONGESTION"/>
      <xs:enumeration value="HEAVY_CONGESTION"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.FIPSCode">
    <xs:sequence>
      <xs:element name="stateCode" type="xs:int"/>
      <xs:element name="countyCode" type="xs:int"/>
      <xs:element name="cityCode" type="xs:int"/>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="com.gcmtravel.FieldDataValidationStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="FIELD_DATA_NOT_VALIDATED"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_AUTO"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_MANUAL"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.HDatumType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NAD27"/>
      <xs:enumeration value="NAD83"/>
      <xs:enumeration value="WGS84"/>
      <xs:enumeration value="WGS84_PLUS_EGM96"/>
      <xs:enumeration value="OTHER_HDATUM_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.LocationResolutionStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="LOCATION_NO_LOCATION"/>
      <xs:enumeration value="LOCATION_NON_SRA"/>
      <xs:enumeration value="LOCATION_PARTIALLY_NON_SRA"/>
      <xs:enumeration value="LOCATION_NOT_VALIDATED"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_AUTO"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_AUTO"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_DIRECTION_TYPE"/>
      <xs:enumeration value="EAST_BOUND"/>
      <xs:enumeration value="WEST_BOUND"/>
      <xs:enumeration value="SOUTH_BOUND"/>
      <xs:enumeration value="NORTH_BOUND"/>
      <xs:enumeration value="SOUTH_EAST_BOUND"/>
      <xs:enumeration value="SOUTH_WEST_BOUND"/>
      <xs:enumeration value="NORTH_EAST_BOUND"/>
      <xs:enumeration value="NORTH_WEST_BOUND"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_ROADWAY_TYPE"/>
      <xs:enumeration value="FREEWAY"/>
      <xs:enumeration value="FREEWAY_EXPRESS"/>
      <xs:enumeration value="FREEWAY_HOV"/>
      <xs:enumeration value="FREEWAY_REVERSIBLE"/>
      <xs:enumeration value="ARTERIAL"/>
      <xs:enumeration value="LOCAL_ROAD"/>
      <xs:enumeration value="RAMP"/>
      <xs:enumeration value="OTHER_ROADWAY_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.SegmentDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="REF_TO_NONREF"/>
      <xs:enumeration value="NONREF_TO_REF"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.StreetNameAffix">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NONE"/>
      <xs:enumeration value="N"/>
      <xs:enumeration value="NE"/>
      <xs:enumeration value="E"/>
      <xs:enumeration value="SE"/>
      <xs:enumeration value="S"/>
      <xs:enumeration value="SW"/>
      <xs:enumeration value="W"/>
      <xs:enumeration value="NW"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.GeometryPoint">
    <xs:sequence>
      <xs:element name="direction" type="com.gcmtravel.SegmentDirectionType"/>
      <xs:element name="segmentID" type="xs:long"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLong">
    <xs:sequence>
      <xs:element name="latitude" type="xs:int"/>
      <xs:element name="longitude" type="xs:int"/>
      <xs:element name="hDatum" type="com.gcmtravel.HDatumType"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GeometrySection">
    <xs:sequence>
      <xs:element name="startSegmentDirection" type="com.gcmtravel.SegmentDirectionType"/>
      <xs:element name="segmentIDs">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="segmentIDsElement" type="xs:long"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayName">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="prefix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="suffix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="streetType" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.AddressPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="addressNumber" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LandmarkPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="landmarkName" type="xs:string"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLongPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="coord" type="com.gcmtravel.LatLong"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.MilePointPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="milePoint" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.AddressSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startAddressNumber" type="xs:string"/>
      <xs:element name="endAddressNumber" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LandmarkSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startLandmarkName" type="xs:string"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endLandmarkName" type="xs:string"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLongSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startLatLong" type="com.gcmtravel.LatLong"/>
      <xs:element name="endLatLong" type="com.gcmtravel.LatLong"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.MilePointSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startMilePoint" type="xs:double"/>
      <xs:element name="endMilePoint" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.CrossStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="crossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="crossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="crossStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RampPoint">
    <xs:sequence>
      <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RampSection">
    <xs:sequence>
      <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.BetweenStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offsetPercentage" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.BetweenStreetSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="startPercentage" type="xs:double"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="endPercentage" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.CrossStreetSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.PointLocationProfile">
    <xs:choice>
      <xs:element name="latLongPointLoc" type="com.gcmtravel.LatLongPoint"/>
      <xs:element name="landmarkPointLoc" type="com.gcmtravel.LandmarkPoint"/>
      <xs:element name="addressPointLoc" type="com.gcmtravel.AddressPoint"/>
      <xs:element name="milePointPointLoc" type="com.gcmtravel.MilePointPoint"/>
      <xs:element name="crossStreetPointLoc" type="com.gcmtravel.CrossStreetPoint"/>
      <xs:element name="rampPointLoc" type="com.gcmtravel.RampPoint"/>
      <xs:element name="betweenStreetPointLoc" type="com.gcmtravel.BetweenStreetPoint"/>
      <xs:element name="geometryPointLoc" type="com.gcmtravel.GeometryPoint"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GenericSection">
    <xs:sequence>
      <xs:element name="startPoint" type="com.gcmtravel.PointLocationProfile"/>
      <xs:element name="endPoint" type="com.gcmtravel.PointLocationProfile"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.SectionLocationProfile">
    <xs:choice>
      <xs:element name="latLongSectionLoc" type="com.gcmtravel.LatLongSection"/>
      <xs:element name="landmarkSectionLoc" type="com.gcmtravel.LandmarkSection"/>
      <xs:element name="addressSectionLoc" type="com.gcmtravel.AddressSection"/>
      <xs:element name="milePointSectionLoc" type="com.gcmtravel.MilePointSection"/>
      <xs:element name="crossStreetSectionLoc" type="com.gcmtravel.CrossStreetSection"/>
      <xs:element name="rampSectionLoc" type="com.gcmtravel.RampSection"/>
      <xs:element name="betweenStreetSectionLoc" type="com.gcmtravel.BetweenStreetSection"/>
      <xs:element name="geometrySectionLoc" type="com.gcmtravel.GeometrySection"/>
      <xs:element name="genericSectionLoc" type="com.gcmtravel.GenericSection"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LinkCongestion">
    <xs:sequence>
      <xs:element name="link">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="linkElement">
              <xs:complexType>
                <xs:sequence minOccurs="0" maxOccurs="unbounded">
                  <xs:element name="linkElementElement" type="com.gcmtravel.SectionLocationProfile"/>
                </xs:sequence>
              </xs:complexType>
            </xs:element>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="linkID" type="xs:string"/>
      <xs:element name="linkDesc" type="xs:string"/>
      <xs:element name="length" type="xs:int"/> <!-- meters -->
      <xs:element name="locationTimeStamp" type="xs:long"/>
      <xs:element name="congestionLevel" type="com.gcmtravel.CongestionLevelType"/>
      <xs:element name="locStatus" type="com.gcmtravel.LocationResolutionStatus"/>
      <xs:element name="dataStatus" type="com.gcmtravel.FieldDataValidationStatus"/>
      <xs:element name="timeStamp" type="xs:long"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="com.gcmtravel.LinkCongestionReport">
    <xs:complexType>
      <xs:sequence minOccurs="0" maxOccurs="unbounded">
        <xs:element name="com.gcmtravel.LinkCongestionReportElement" type="com.gcmtravel.LinkCongestion"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

### Sample Congestion Report

The following is a sample LinkCongestionReport.xml:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<com.gcmtravel.LinkCongestionReport>
  <com.gcmtravel.LinkCongestionReportElement>
    <link>
      <linkElement>
        <linkElementElement>
          <geometrySectionLoc>
            <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
            <segmentIDs>
              <segmentIDsElement>16888006</segmentIDsElement>
              <segmentIDsElement>16888007</segmentIDsElement>
            </segmentIDs>
            <startOffset>271.4815</startOffset>
            <endOffset>94.04786</endOffset>
          </geometrySectionLoc>
        </linkElementElement>
        <linkElementElement>
          <crossStreetSectionLoc>
            <roadName>
              <name>NORTH SOUTH</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType>FWY</streetType>
            </roadName>
            <direction>SOUTH_BOUND</direction>
            <type>FREEWAY</type>
            <startFipsCode>
              <stateCode>55</stateCode>
              <countyCode>79</countyCode>
              <cityCode>53000</cityCode>
            </startFipsCode>
            <endFipsCode>
              <stateCode>55</stateCode>
              <countyCode>79</countyCode>
              <cityCode>53000</cityCode>
            </endFipsCode>
            <fromCrossStreetName>
              <name>WISCONSIN</name>
              <prefix>W</prefix>
              <suffix>NONE</suffix>
              <streetType>AVE</streetType>
            </fromCrossStreetName>
            <fromCrossStreetType>ARTERIAL</fromCrossStreetType>
            <fromStreetDirection>WEST_BOUND</fromStreetDirection>
            <startOffset>0.0</startOffset>
            <toCrossStreetName>
              <name>WISCONSIN</name>
              <prefix>W</prefix>
              <suffix>NONE</suffix>
              <streetType>AVE</streetType>
            </toCrossStreetName>
            <toCrossStreetType>ARTERIAL</toCrossStreetType>
            <toStreetDirection>EAST_BOUND</toStreetDirection>
            <endOffset>94.04786</endOffset>
          </crossStreetSectionLoc>
        </linkElementElement>
        <linkElementElement>
          <latLongSectionLoc>
            <roadName>
              <name>NORTH SOUTH</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType>FWY</streetType>
            </roadName>
            <direction>SOUTH_BOUND</direction>
            <type>FREEWAY</type>
            <startLatLong>
              <latitude>4303635</latitude>
              <longitude>-8792560</longitude>
              <hDatum>NAD83</hDatum>
            </startLatLong>
            <endLatLong>
              <latitude>4303779</latitude>
              <longitude>-8792524</longitude>
              <hDatum>NAD83</hDatum>
            </endLatLong>
          </latLongSectionLoc>
        </linkElementElement>
      </linkElement>
    </link>
    <linkID>WI-MONITOR-WI-SB-I43-WWisconsinAve-I94</linkID>
    <linkDesc>SB:I-43:Wisconsin:Off-ramp to I-94 WB:WI:5</linkDesc>
    <length>107</length>
    <locationTimeStamp>1004650747486</locationTimeStamp>
    <congestionLevel>UNKNOWN_CONGESTION_LEVEL</congestionLevel>
    <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
    <dataStatus>FIELD_DATA_VALIDATED_AUTO</dataStatus>
    <timeStamp>1057735122919</timeStamp>
  </com.gcmtravel.LinkCongestionReportElement>
  <com.gcmtravel.LinkCongestionReportElement>
    <link>
      <linkElement>
        <linkElementElement>
          <geometrySectionLoc>
            <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
            <segmentIDs>
              <segmentIDsElement>19887277</segmentIDsElement>
              <segmentIDsElement>19887169</segmentIDsElement>
              <segmentIDsElement>19877292</segmentIDsElement>
              <segmentIDsElement>19877267</segmentIDsElement>
            </segmentIDs>
            <startOffset>414.80035</startOffset>
            <endOffset>69.35295</endOffset>
          </geometrySectionLoc>
        </linkElementElement>
        <linkElementElement>
          <crossStreetSectionLoc>
            <roadName>
              <name>I-290</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>WEST_BOUND</direction>
            <type>FREEWAY</type>
            <startFipsCode>
              <stateCode>17</stateCode>
              <countyCode>31</countyCode>
              <cityCode>35086</cityCode>
            </startFipsCode>
            <endFipsCode>
              <stateCode>17</stateCode>
              <countyCode>31</countyCode>
              <cityCode>5404</cityCode>
            </endFipsCode>
            <fromCrossStreetName>
              <name>EAST-WEST</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </fromCrossStreetName>
            <fromCrossStreetType>FREEWAY</fromCrossStreetType>
            <fromStreetDirection>WEST_BOUND</fromStreetDirection>
            <startOffset>414.80035</startOffset>
            <toCrossStreetName>
              <name>BUTTERFIELD</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType>RD</streetType>
            </toCrossStreetName>
            <toCrossStreetType>ARTERIAL</toCrossStreetType>
            <toStreetDirection>EAST_BOUND</toStreetDirection>
            <endOffset>217.23302</endOffset>
          </crossStreetSectionLoc>
        </linkElementElement>
        <linkElementElement>
          <latLongSectionLoc>
            <roadName>
              <name>I-290</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>WEST_BOUND</direction>
            <type>FREEWAY</type>
            <startLatLong>
              <latitude>4187392</latitude>
              <longitude>-8790849</longitude>
              <hDatum>NAD83</hDatum>
            </startLatLong>
            <endLatLong>
              <latitude>4187566</latitude>
              <longitude>-8791581</longitude>
              <hDatum>NAD83</hDatum>
            </endLatLong>
          </latLongSectionLoc>
        </linkElementElement>
      </linkElement>
    </link>
    <linkID>IL-TSC-I_290-W-238:28</linkID>
    <linkDesc><![CDATA[WB:I-290:I-90/I-94:Higgins:IL:28]]></linkDesc>
    <length>643</length>
    <locationTimeStamp>0</locationTimeStamp>
    <congestionLevel>LIGHT_CONGESTION</congestionLevel>
    <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
    <dataStatus>FIELD_DATA_VALIDATED_AUTO</dataStatus>
    <timeStamp>1057735058904</timeStamp>
  </com.gcmtravel.LinkCongestionReportElement>
  <com.gcmtravel.LinkCongestionReportElement>
    <link>
      <linkElement>
        <linkElementElement>
          <geometrySectionLoc>
            <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
            <segmentIDs>
              <segmentIDsElement>19797423</segmentIDsElement>
              <segmentIDsElement>19797373</segmentIDsElement>
            </segmentIDs>
            <startOffset>76.05461</startOffset>
            <endOffset>364.3053</endOffset>
          </geometrySectionLoc>
        </linkElementElement>
        <linkElementElement>
          <crossStreetSectionLoc>
            <roadName>
              <name>I-90</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>NORTH_BOUND</direction>
            <type>FREEWAY</type>
            <startFipsCode>
              <stateCode>17</stateCode>
              <countyCode>31</countyCode>
              <cityCode>14000</cityCode>
            </startFipsCode>
            <endFipsCode>
              <stateCode>17</stateCode>
              <countyCode>31</countyCode>
              <cityCode>14000</cityCode>
            </endFipsCode>
            <fromCrossStreetName>
              <name>KOSTNER</name>
              <prefix>N</prefix>
              <suffix>NONE</suffix>
              <streetType>AVE</streetType>
            </fromCrossStreetName>
            <fromCrossStreetType>ARTERIAL</fromCrossStreetType>
            <fromStreetDirection>NORTH_BOUND</fromStreetDirection>
            <startOffset>76.05461</startOffset>
            <toCrossStreetName>
              <name>MONTROSE</name>
              <prefix>W</prefix>
              <suffix>NONE</suffix>
              <streetType>AVE</streetType>
            </toCrossStreetName>
            <toCrossStreetType>ARTERIAL</toCrossStreetType>
            <toStreetDirection>WEST_BOUND</toStreetDirection>
            <endOffset>-0.35762024</endOffset>
          </crossStreetSectionLoc>
        </linkElementElement>
        <linkElementElement>
          <latLongSectionLoc>
            <roadName>
              <name>I-90</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>NORTH_BOUND</direction>
            <type>FREEWAY</type>
            <startLatLong>
              <latitude>4195860</latitude>
              <longitude>-8773903</longitude>
              <hDatum>NAD83</hDatum>
            </startLatLong>
            <endLatLong>
              <latitude>4196077</latitude>
              <longitude>-8774234</longitude>
              <hDatum>NAD83</hDatum>
            </endLatLong>
          </latLongSectionLoc>
        </linkElementElement>
        <linkElementElement>
          <milePointSectionLoc>
            <roadName>
              <name>I-90</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>NORTH_BOUND</direction>
            <type>FREEWAY</type>
            <startFipsCode>
              <stateCode>17</stateCode>
              <countyCode>31</countyCode>
              <cityCode>14000</cityCode>
            </startFipsCode>
            <endFipsCode>
              <stateCode>17</stateCode>
              <countyCode>31</countyCode>
              <cityCode>14000</cityCode>
            </endFipsCode>
            <startMilePoint>70529.06</startMilePoint>
            <endMilePoint>70163.01</endMilePoint>
          </milePointSectionLoc>
        </linkElementElement>
      </linkElement>
    </link>
    <linkID>IL-TSC-I_90-W-385:12</linkID>
    <linkDesc><![CDATA[WB:Kennedy:Eisenhower:O'Hare:IL:12]]></linkDesc>
    <length>366</length>
    <locationTimeStamp>0</locationTimeStamp>
    <congestionLevel>LIGHT_CONGESTION</congestionLevel>
    <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
    <dataStatus>FIELD_DATA_VALIDATED_AUTO</dataStatus>
    <timeStamp>1057735058907</timeStamp>
  </com.gcmtravel.LinkCongestionReportElement>
  <com.gcmtravel.LinkCongestionReportElement>
    <link>
      <linkElement>
        <linkElementElement>
          <geometrySectionLoc>
            <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
            <segmentIDs>
              <segmentIDsElement>16887741</segmentIDsElement>
              <segmentIDsElement>20102239</segmentIDsElement>
              <segmentIDsElement>16887737</segmentIDsElement>
              <segmentIDsElement>16887735</segmentIDsElement>
            </segmentIDs>
            <startOffset>2.828427</startOffset>
            <endOffset>162.00308</endOffset>
          </geometrySectionLoc>
        </linkElementElement>
        <linkElementElement>
          <crossStreetSectionLoc>
            <roadName>
              <name>I-94</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>SOUTH_WEST_BOUND</direction>
            <type>FREEWAY</type>
            <startFipsCode>
              <stateCode>55</stateCode>
              <countyCode>79</countyCode>
              <cityCode>53000</cityCode>
            </startFipsCode>
            <endFipsCode>
              <stateCode>55</stateCode>
              <countyCode>79</countyCode>
              <cityCode>53000</cityCode>
            </endFipsCode>
            <fromCrossStreetName>
              <name>WI-57</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </fromCrossStreetName>
            <fromCrossStreetType>ARTERIAL</fromCrossStreetType>
            <fromStreetDirection>NORTH_BOUND</fromStreetDirection>
            <startOffset>0.0</startOffset>
            <toCrossStreetName>
              <name>35TH</name>
              <prefix>N</prefix>
              <suffix>NONE</suffix>
              <streetType>ST</streetType>
            </toCrossStreetName>
            <toCrossStreetType>ARTERIAL</toCrossStreetType>
            <toStreetDirection>NORTH_BOUND</toStreetDirection>
            <endOffset>-2.999948</endOffset>
          </crossStreetSectionLoc>
        </linkElementElement>
        <linkElementElement>
          <latLongSectionLoc>
            <roadName>
              <name>I-94</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>SOUTH_WEST_BOUND</direction>
            <type>FREEWAY</type>
            <startLatLong>
              <latitude>4303410</latitude>
              <longitude>-8794779</longitude>
              <hDatum>NAD83</hDatum>
            </startLatLong>
            <endLatLong>
              <latitude>4303220</latitude>
              <longitude>-8795770</longitude>
              <hDatum>NAD83</hDatum>
            </endLatLong>
          </latLongSectionLoc>
        </linkElementElement>
      </linkElement>
    </link>
    <linkID>WI-MONITOR-WI-WB-I94-N27thSt-N35thSt</linkID>
    <linkDesc>WB:I-94:27th:35th:WI:2</linkDesc>
    <length>854</length>
    <locationTimeStamp>1004650775609</locationTimeStamp>
    <congestionLevel>UNKNOWN_CONGESTION_LEVEL</congestionLevel>
    <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
    <dataStatus>FIELD_DATA_VALIDATED_AUTO</dataStatus>
    <timeStamp>1057735122924</timeStamp>
  </com.gcmtravel.LinkCongestionReportElement>
</com.gcmtravel.LinkCongestionReport>
```

### Travel Time Report XSchema for LinkTrafficReport.xml.gz

The following XSchema defines the format of LinkTrafficReport.xml:

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:simpleType name="com.gcmtravel.CongestionLevelType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_CONGESTION_LEVEL"/>
      <xs:enumeration value="NON_CONGESTION"/>
      <xs:enumeration value="LIGHT_CONGESTION"/>
      <xs:enumeration value="MEDIUM_CONGESTION"/>
      <xs:enumeration value="HEAVY_CONGESTION"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.FIPSCode">
    <xs:sequence>
      <xs:element name="stateCode" type="xs:int"/>
      <xs:element name="countyCode" type="xs:int"/>
      <xs:element name="cityCode" type="xs:int"/>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="com.gcmtravel.FieldDataValidationStatus">
     <xs:restriction base="xs:string">
      <xs:enumeration value="FIELD_DATA_NOT_VALIDATED"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_AUTO"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_MANUAL"/>
     </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.HDatumType">
     <xs:restriction base="xs:string">
      <xs:enumeration value="NAD27"/>
      <xs:enumeration value="NAD83"/>
      <xs:enumeration value="WGS84"/>
      <xs:enumeration value="WGS84_PLUS_EGM96"/>
      <xs:enumeration value="OTHER_HDATUM_TYPE"/>
     </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.LocationResolutionStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="LOCATION_NO_LOCATION"/>
      <xs:enumeration value="LOCATION_NON_SRA"/>
      <xs:enumeration value="LOCATION_PARTIALLY_NON_SRA"/>
      <xs:enumeration value="LOCATION_NOT_VALIDATED"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_AUTO"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_AUTO"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_DIRECTION_TYPE"/>
      <xs:enumeration value="EAST_BOUND"/>
      <xs:enumeration value="WEST_BOUND"/>
      <xs:enumeration value="SOUTH_BOUND"/>
      <xs:enumeration value="NORTH_BOUND"/>
      <xs:enumeration value="SOUTH_EAST_BOUND"/>
      <xs:enumeration value="SOUTH_WEST_BOUND"/>
      <xs:enumeration value="NORTH_EAST_BOUND"/>
      <xs:enumeration value="NORTH_WEST_BOUND"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_ROADWAY_TYPE"/>
      <xs:enumeration value="FREEWAY"/>
      <xs:enumeration value="FREEWAY_EXPRESS"/>
      <xs:enumeration value="FREEWAY_HOV"/>
      <xs:enumeration value="FREEWAY_REVERSIBLE"/>
      <xs:enumeration value="ARTERIAL"/>
      <xs:enumeration value="LOCAL_ROAD"/>
      <xs:enumeration value="RAMP"/>
      <xs:enumeration value="OTHER_ROADWAY_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.SegmentDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="REF_TO_NONREF"/>
      <xs:enumeration value="NONREF_TO_REF"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.StreetNameAffix">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NONE"/>
      <xs:enumeration value="N"/>
      <xs:enumeration value="NE"/>
      <xs:enumeration value="E"/>
      <xs:enumeration value="SE"/>
      <xs:enumeration value="S"/>
      <xs:enumeration value="SW"/>
      <xs:enumeration value="W"/>
      <xs:enumeration value="NW"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.GeometryPoint">
    <xs:sequence>
      <xs:element name="direction" type="com.gcmtravel.SegmentDirectionType"/>
      <xs:element name="segmentID" type="xs:long"/>
     <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLong">
    <xs:sequence>
      <xs:element name="latitude" type="xs:int"/>
      <xs:element name="longitude" type="xs:int"/>
      <xs:element name="hDatum" type="com.gcmtravel.HDatumType"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GeometrySection">
    <xs:sequence>
      <xs:element name="startSegmentDirection" type="com.gcmtravel.SegmentDirectionType"/>
      <xs:element name="segmentIDs">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="segmentIDsElement" type="xs:long"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayName">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="prefix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="suffix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="streetType" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.AddressPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="addressNumber" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LandmarkPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="landmarkName" type="xs:string"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLongPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="coord" type="com.gcmtravel.LatLong"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.MilePointPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="milePoint" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.AddressSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startAddressNumber" type="xs:string"/>
      <xs:element name="endAddressNumber" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LandmarkSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startLandmarkName" type="xs:string"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endLandmarkName" type="xs:string"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLongSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startLatLong" type="com.gcmtravel.LatLong"/>
      <xs:element name="endLatLong" type="com.gcmtravel.LatLong"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.MilePointSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="startMilePoint" type="xs:double"/>
      <xs:element name="endMilePoint" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.CrossStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="crossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="crossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="crossStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RampPoint">
    <xs:sequence>
      <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RampSection">
    <xs:sequence>
      <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.BetweenStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offsetPercentage" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.BetweenStreetSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="startPercentage" type="xs:double"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="endPercentage" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.CrossStreetSection">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="startFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="endFipsCode" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="startOffset" type="xs:double"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="endOffset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.PointLocationProfile">
    <xs:choice>
      <xs:element name="latLongPointLoc" type="com.gcmtravel.LatLongPoint"/>
      <xs:element name="landmarkPointLoc" type="com.gcmtravel.LandmarkPoint"/>
      <xs:element name="addressPointLoc" type="com.gcmtravel.AddressPoint"/>
      <xs:element name="milePointPointLoc" type="com.gcmtravel.MilePointPoint"/>
      <xs:element name="crossStreetPointLoc" type="com.gcmtravel.CrossStreetPoint"/>
      <xs:element name="rampPointLoc" type="com.gcmtravel.RampPoint"/>
      <xs:element name="betweenStreetPointLoc" type="com.gcmtravel.BetweenStreetPoint"/>
      <xs:element name="geometryPointLoc" type="com.gcmtravel.GeometryPoint"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GenericSection">
    <xs:sequence>
      <xs:element name="startPoint" type="com.gcmtravel.PointLocationProfile"/>
      <xs:element name="endPoint" type="com.gcmtravel.PointLocationProfile"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.SectionLocationProfile">
    <xs:choice>
      <xs:element name="latLongSectionLoc" type="com.gcmtravel.LatLongSection"/>
      <xs:element name="landmarkSectionLoc" type="com.gcmtravel.LandmarkSection"/>
      <xs:element name="addressSectionLoc" type="com.gcmtravel.AddressSection"/>
      <xs:element name="milePointSectionLoc" type="com.gcmtravel.MilePointSection"/>
      <xs:element name="crossStreetSectionLoc" type="com.gcmtravel.CrossStreetSection"/>
      <xs:element name="rampSectionLoc" type="com.gcmtravel.RampSection"/>
      <xs:element name="betweenStreetSectionLoc" type="com.gcmtravel.BetweenStreetSection"/>
      <xs:element name="geometrySectionLoc" type="com.gcmtravel.GeometrySection"/>
      <xs:element name="genericSectionLoc" type="com.gcmtravel.GenericSection"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LinkTraffic">
    <xs:sequence>
      <xs:element name="link">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="linkElement">
              <xs:complexType>
                <xs:sequence minOccurs="0" maxOccurs="unbounded">
                  <xs:element name="linkElementElement" type="com.gcmtravel.SectionLocationProfile"/>
                </xs:sequence>
              </xs:complexType>
            </xs:element>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="linkID" type="xs:string"/>
      <xs:element name="linkDesc" type="xs:string"/>
      <xs:element name="length" type="xs:int"/> <!-- meters -->
      <xs:element name="locationTimeStamp" type="xs:long"/>
      <xs:element name="isBasic" type="xs:boolean"/>
      <xs:element name="travelTime" type="xs:int"/>
      <xs:element name="volume" type="xs:short"/>
      <xs:element name="speed" type="xs:double"/>
      <xs:element name="occupancy" type="xs:double"/>
      <xs:element name="congestionLevel" type="com.gcmtravel.CongestionLevelType"/>
      <xs:element name="locStatus" type="com.gcmtravel.LocationResolutionStatus"/>
      <xs:element name="dataStatus" type="com.gcmtravel.FieldDataValidationStatus"/>
      <xs:element name="timeStamp" type="xs:long"/>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="com.gcmtravel.LinkTrafficReport">
    <xs:complexType>
      <xs:sequence minOccurs="0" maxOccurs="unbounded">
        <xs:element name="com.gcmtravel.LinkTrafficReportElement" type="com.gcmtravel.LinkTraffic"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

### Sample Travel Time Report

The following is a sample LinkTrafficReport.xml:

**Note:** The segment IDs in the travel time report are for internal use only. It is recommended that users ignore them.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<com.gcmtravel.LinkTrafficReport>
  <com.gcmtravel.LinkTrafficReportElement>
    <link>
      <linkElement>
        <linkElementElement>
          <geometrySectionLoc>
            <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
            <segmentIDs>
              <segmentIDsElement>19796878</segmentIDsElement>
              <segmentIDsElement>19796815</segmentIDsElement>
              <segmentIDsElement>19950653</segmentIDsElement>
              <segmentIDsElement>16891224</segmentIDsElement>
              <segmentIDsElement>16891222</segmentIDsElement>
              <segmentIDsElement>16891223</segmentIDsElement>
              <segmentIDsElement>19794891</segmentIDsElement>
              <segmentIDsElement>19794541</segmentIDsElement>
              <segmentIDsElement>16891173</segmentIDsElement>
              <segmentIDsElement>16891172</segmentIDsElement>
              <segmentIDsElement>16891219</segmentIDsElement>
              <segmentIDsElement>16891220</segmentIDsElement>
              <segmentIDsElement>16891218</segmentIDsElement>
              <segmentIDsElement>16891214</segmentIDsElement>
              <segmentIDsElement>16891215</segmentIDsElement>
              <segmentIDsElement>19792497</segmentIDsElement>
              <segmentIDsElement>19791853</segmentIDsElement>
              <segmentIDsElement>16880328</segmentIDsElement>
              <segmentIDsElement>16880329</segmentIDsElement>
              <segmentIDsElement>19739105</segmentIDsElement>
              <segmentIDsElement>19772362</segmentIDsElement>
              <segmentIDsElement>16880322</segmentIDsElement>
              <segmentIDsElement>16880323</segmentIDsElement>
              <segmentIDsElement>16880321</segmentIDsElement>
              <segmentIDsElement>16880320</segmentIDsElement>
              <segmentIDsElement>16880318</segmentIDsElement>
              <segmentIDsElement>16880319</segmentIDsElement>
              <segmentIDsElement>19739100</segmentIDsElement>
              <segmentIDsElement>19772352</segmentIDsElement>
              <segmentIDsElement>19739099</segmentIDsElement>
              <segmentIDsElement>19739096</segmentIDsElement>
              <segmentIDsElement>19739094</segmentIDsElement>
              <segmentIDsElement>16880313</segmentIDsElement>
              <segmentIDsElement>16880312</segmentIDsElement>
              <segmentIDsElement>16880310</segmentIDsElement>
              <segmentIDsElement>16880311</segmentIDsElement>
              <segmentIDsElement>19739077</segmentIDsElement>
              <segmentIDsElement>16880309</segmentIDsElement>
              <segmentIDsElement>16880308</segmentIDsElement>
              <segmentIDsElement>19772344</segmentIDsElement>
              <segmentIDsElement>16880301</segmentIDsElement>
              <segmentIDsElement>16880302</segmentIDsElement>
              <segmentIDsElement>19740430</segmentIDsElement>
              <segmentIDsElement>16880293</segmentIDsElement>
              <segmentIDsElement>16880294</segmentIDsElement>
              <segmentIDsElement>16880292</segmentIDsElement>
              <segmentIDsElement>16880291</segmentIDsElement>
              <segmentIDsElement>19772343</segmentIDsElement>
              <segmentIDsElement>19772342</segmentIDsElement>
              <segmentIDsElement>19740424</segmentIDsElement>
              <segmentIDsElement>19740422</segmentIDsElement>
              <segmentIDsElement>19772340</segmentIDsElement>
              <segmentIDsElement>19772338</segmentIDsElement>
              <segmentIDsElement>19740419</segmentIDsElement>
              <segmentIDsElement>19944471</segmentIDsElement>
              <segmentIDsElement>19760435</segmentIDsElement>
              <segmentIDsElement>16880489</segmentIDsElement>
              <segmentIDsElement>16880488</segmentIDsElement>
              <segmentIDsElement>19739083</segmentIDsElement>
              <segmentIDsElement>19764668</segmentIDsElement>
              <segmentIDsElement>19771528</segmentIDsElement>
            </segmentIDs>
            <startOffset>46.624905</startOffset>
            <endOffset>98.27</endOffset>
          </geometrySectionLoc>
        </linkElementElement>
      </linkElement>
    </link>
    <linkID>GCM-GATEWAY-2203</linkID>
    <linkDesc>NB:Edens:Kennedy:Edens Spur:IL</linkDesc>
    <length>21589</length>
    <locationTimeStamp>0</locationTimeStamp>
    <isBasic>true</isBasic>
    <travelTime>1037</travelTime>
    <volume>290</volume>
    <speed>20.804554</speed>
    <occupancy>3.560721</occupancy>
    <congestionLevel>LIGHT_CONGESTION</congestionLevel>
    <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
    <dataStatus>FIELD_DATA_VALIDATED_AUTO</dataStatus>
    <timeStamp>1057735036845</timeStamp>
  </com.gcmtravel.LinkTrafficReportElement>
  <com.gcmtravel.LinkTrafficReportElement>
    <link>
      <linkElement>
        <linkElementElement>
          <geometrySectionLoc>
            <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
            <segmentIDs>
              <segmentIDsElement>19880939</segmentIDsElement>
              <segmentIDsElement>19880772</segmentIDsElement>
              <segmentIDsElement>19880709</segmentIDsElement>
              <segmentIDsElement>16898766</segmentIDsElement>
              <segmentIDsElement>16898767</segmentIDsElement>
              <segmentIDsElement>19880316</segmentIDsElement>
              <segmentIDsElement>19880057</segmentIDsElement>
              <segmentIDsElement>16898762</segmentIDsElement>
              <segmentIDsElement>16898763</segmentIDsElement>
              <segmentIDsElement>19879837</segmentIDsElement>
              <segmentIDsElement>19879816</segmentIDsElement>
              <segmentIDsElement>19879583</segmentIDsElement>
              <segmentIDsElement>19975152</segmentIDsElement>
              <segmentIDsElement>16898774</segmentIDsElement>
              <segmentIDsElement>16898773</segmentIDsElement>
              <segmentIDsElement>19878462</segmentIDsElement>
              <segmentIDsElement>19878214</segmentIDsElement>
              <segmentIDsElement>19878115</segmentIDsElement>
              <segmentIDsElement>16897726</segmentIDsElement>
              <segmentIDsElement>16897725</segmentIDsElement>
              <segmentIDsElement>19835290</segmentIDsElement>
              <segmentIDsElement>19835249</segmentIDsElement>
              <segmentIDsElement>19834437</segmentIDsElement>
              <segmentIDsElement>19834349</segmentIDsElement>
              <segmentIDsElement>19833735</segmentIDsElement>
              <segmentIDsElement>19833486</segmentIDsElement>
              <segmentIDsElement>19833065</segmentIDsElement>
              <segmentIDsElement>16897732</segmentIDsElement>
              <segmentIDsElement>16897733</segmentIDsElement>
              <segmentIDsElement>19832438</segmentIDsElement>
              <segmentIDsElement>19832233</segmentIDsElement>
              <segmentIDsElement>16897738</segmentIDsElement>
              <segmentIDsElement>16897737</segmentIDsElement>
              <segmentIDsElement>19831763</segmentIDsElement>
              <segmentIDsElement>16897743</segmentIDsElement>
              <segmentIDsElement>16897742</segmentIDsElement>
              <segmentIDsElement>16897744</segmentIDsElement>
              <segmentIDsElement>19830886</segmentIDsElement>
              <segmentIDsElement>16897750</segmentIDsElement>
              <segmentIDsElement>16897751</segmentIDsElement>
              <segmentIDsElement>19827856</segmentIDsElement>
            </segmentIDs>
            <startOffset>14.142136</startOffset>
            <endOffset>327.01376</endOffset>
          </geometrySectionLoc>
        </linkElementElement>
      </linkElement>
    </link>
    <linkID>GCM-GATEWAY-11101</linkID>
    <linkDesc>NB:I-57:I-80:Dan Ryan:IL</linkDesc>
    <length>19514</length>
    <locationTimeStamp>-100</locationTimeStamp>
    <isBasic>true</isBasic>
    <travelTime>-100</travelTime>
    <volume>-100</volume>
    <speed>-100.0</speed>
    <occupancy>-100.0</occupancy>
    <congestionLevel>UNKNOWN_CONGESTION_LEVEL</congestionLevel>
    <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
    <dataStatus>FIELD_DATA_INFEASIBLE_FOUND_AUTO</dataStatus>
    <timeStamp>1057735036844</timeStamp>
  </com.gcmtravel.LinkTrafficReportElement>
  <com.gcmtravel.LinkTrafficReportElement>
    <link>
      <linkElement>
        <linkElementElement>
          <geometrySectionLoc>
            <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
            <segmentIDs>
              <segmentIDsElement>19763414</segmentIDsElement>
              <segmentIDsElement>16896524</segmentIDsElement>
              <segmentIDsElement>16896523</segmentIDsElement>
              <segmentIDsElement>19764667</segmentIDsElement>
              <segmentIDsElement>19739088</segmentIDsElement>
              <segmentIDsElement>16896258</segmentIDsElement>
              <segmentIDsElement>16896257</segmentIDsElement>
              <segmentIDsElement>16880491</segmentIDsElement>
              <segmentIDsElement>16880490</segmentIDsElement>
              <segmentIDsElement>16880487</segmentIDsElement>
              <segmentIDsElement>16880486</segmentIDsElement>
              <segmentIDsElement>19772339</segmentIDsElement>
              <segmentIDsElement>19772341</segmentIDsElement>
              <segmentIDsElement>19740421</segmentIDsElement>
              <segmentIDsElement>19740423</segmentIDsElement>
              <segmentIDsElement>19739080</segmentIDsElement>
              <segmentIDsElement>16880298</segmentIDsElement>
              <segmentIDsElement>16880297</segmentIDsElement>
              <segmentIDsElement>16880296</segmentIDsElement>
              <segmentIDsElement>16880295</segmentIDsElement>
              <segmentIDsElement>19739082</segmentIDsElement>
              <segmentIDsElement>16880304</segmentIDsElement>
              <segmentIDsElement>16880303</segmentIDsElement>
              <segmentIDsElement>19739075</segmentIDsElement>
              <segmentIDsElement>16880306</segmentIDsElement>
              <segmentIDsElement>16880305</segmentIDsElement>
              <segmentIDsElement>19772346</segmentIDsElement>
              <segmentIDsElement>19739090</segmentIDsElement>
              <segmentIDsElement>19772347</segmentIDsElement>
              <segmentIDsElement>19739093</segmentIDsElement>
              <segmentIDsElement>16880315</segmentIDsElement>
              <segmentIDsElement>16880314</segmentIDsElement>
              <segmentIDsElement>19739097</segmentIDsElement>
              <segmentIDsElement>19739098</segmentIDsElement>
              <segmentIDsElement>19772354</segmentIDsElement>
              <segmentIDsElement>16880317</segmentIDsElement>
              <segmentIDsElement>16880316</segmentIDsElement>
              <segmentIDsElement>19740439</segmentIDsElement>
              <segmentIDsElement>19739102</segmentIDsElement>
              <segmentIDsElement>16880325</segmentIDsElement>
              <segmentIDsElement>16880324</segmentIDsElement>
              <segmentIDsElement>19740442</segmentIDsElement>
              <segmentIDsElement>19772364</segmentIDsElement>
              <segmentIDsElement>16880327</segmentIDsElement>
              <segmentIDsElement>16880326</segmentIDsElement>
              <segmentIDsElement>16880331</segmentIDsElement>
              <segmentIDsElement>16880330</segmentIDsElement>
              <segmentIDsElement>16882415</segmentIDsElement>
              <segmentIDsElement>16882416</segmentIDsElement>
              <segmentIDsElement>16891217</segmentIDsElement>
              <segmentIDsElement>16891216</segmentIDsElement>
              <segmentIDsElement>19793049</segmentIDsElement>
              <segmentIDsElement>16891171</segmentIDsElement>
              <segmentIDsElement>16891170</segmentIDsElement>
              <segmentIDsElement>19793824</segmentIDsElement>
              <segmentIDsElement>16891166</segmentIDsElement>
              <segmentIDsElement>16891165</segmentIDsElement>
              <segmentIDsElement>16891164</segmentIDsElement>
              <segmentIDsElement>19796015</segmentIDsElement>
              <segmentIDsElement>19950652</segmentIDsElement>
              <segmentIDsElement>19943538</segmentIDsElement>
              <segmentIDsElement>19797063</segmentIDsElement>
            </segmentIDs>
            <startOffset>0.0</startOffset>
            <endOffset>239.011</endOffset>
          </geometrySectionLoc>
        </linkElementElement>
      </linkElement>
      <linkElement>
        <linkElementElement>
          <geometrySectionLoc>
            <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
            <segmentIDs>
              <segmentIDsElement>19797064</segmentIDsElement>
            </segmentIDs>
            <startOffset>5.0</startOffset>
            <endOffset>101.98039</endOffset>
          </geometrySectionLoc>
        </linkElementElement>
      </linkElement>
      <linkElement>
        <linkElementElement>
          <geometrySectionLoc>
            <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
            <segmentIDs>
              <segmentIDsElement>16900473</segmentIDsElement>
              <segmentIDsElement>16900472</segmentIDsElement>
              <segmentIDsElement>19797480</segmentIDsElement>
              <segmentIDsElement>19797581</segmentIDsElement>
              <segmentIDsElement>16900480</segmentIDsElement>
              <segmentIDsElement>16900488</segmentIDsElement>
              <segmentIDsElement>16900487</segmentIDsElement>
              <segmentIDsElement>16900500</segmentIDsElement>
              <segmentIDsElement>16900499</segmentIDsElement>
              <segmentIDsElement>19798948</segmentIDsElement>
              <segmentIDsElement>19799906</segmentIDsElement>
              <segmentIDsElement>19800166</segmentIDsElement>
              <segmentIDsElement>19800526</segmentIDsElement>
              <segmentIDsElement>16900515</segmentIDsElement>
              <segmentIDsElement>16900516</segmentIDsElement>
              <segmentIDsElement>19950564</segmentIDsElement>
              <segmentIDsElement>16900525</segmentIDsElement>
              <segmentIDsElement>16900524</segmentIDsElement>
              <segmentIDsElement>19801814</segmentIDsElement>
              <segmentIDsElement>16900528</segmentIDsElement>
              <segmentIDsElement>16900537</segmentIDsElement>
              <segmentIDsElement>16900536</segmentIDsElement>
              <segmentIDsElement>19950597</segmentIDsElement>
              <segmentIDsElement>16900539</segmentIDsElement>
              <segmentIDsElement>16900563</segmentIDsElement>
              <segmentIDsElement>16900562</segmentIDsElement>
              <segmentIDsElement>16900556</segmentIDsElement>
              <segmentIDsElement>16900557</segmentIDsElement>
              <segmentIDsElement>16900555</segmentIDsElement>
              <segmentIDsElement>16900548</segmentIDsElement>
              <segmentIDsElement>16900547</segmentIDsElement>
              <segmentIDsElement>19804884</segmentIDsElement>
              <segmentIDsElement>19805006</segmentIDsElement>
              <segmentIDsElement>19805314</segmentIDsElement>
              <segmentIDsElement>19805707</segmentIDsElement>
              <segmentIDsElement>19806199</segmentIDsElement>
              <segmentIDsElement>19806956</segmentIDsElement>
              <segmentIDsElement>16900582</segmentIDsElement>
              <segmentIDsElement>16900581</segmentIDsElement>
              <segmentIDsElement>19808492</segmentIDsElement>
              <segmentIDsElement>16900587</segmentIDsElement>
              <segmentIDsElement>16900600</segmentIDsElement>
              <segmentIDsElement>16900599</segmentIDsElement>
              <segmentIDsElement>16900596</segmentIDsElement>
              <segmentIDsElement>16900595</segmentIDsElement>
              <segmentIDsElement>19950647</segmentIDsElement>
            </segmentIDs>
            <startOffset>0.0</startOffset>
            <endOffset>282.72784</endOffset>
          </geometrySectionLoc>
        </linkElementElement>
      </linkElement>
      <linkElement>
        <linkElementElement>
          <geometrySectionLoc>
            <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
            <segmentIDs>
              <segmentIDsElement>16900448</segmentIDsElement>
              <segmentIDsElement>16891509</segmentIDsElement>
              <segmentIDsElement>16891508</segmentIDsElement>
              <segmentIDsElement>19812110</segmentIDsElement>
              <segmentIDsElement>19812259</segmentIDsElement>
              <segmentIDsElement>19751485</segmentIDsElement>
              <segmentIDsElement>16891471</segmentIDsElement>
              <segmentIDsElement>16891470</segmentIDsElement>
              <segmentIDsElement>19739246</segmentIDsElement>
              <segmentIDsElement>16891465</segmentIDsElement>
              <segmentIDsElement>16891464</segmentIDsElement>
              <segmentIDsElement>19751482</segmentIDsElement>
              <segmentIDsElement>16891432</segmentIDsElement>
              <segmentIDsElement>16891431</segmentIDsElement>
              <segmentIDsElement>16891429</segmentIDsElement>
              <segmentIDsElement>19751479</segmentIDsElement>
              <segmentIDsElement>16891424</segmentIDsElement>
              <segmentIDsElement>16891423</segmentIDsElement>
              <segmentIDsElement>19751476</segmentIDsElement>
              <segmentIDsElement>16891404</segmentIDsElement>
              <segmentIDsElement>16891403</segmentIDsElement>
              <segmentIDsElement>19739250</segmentIDsElement>
              <segmentIDsElement>16891367</segmentIDsElement>
              <segmentIDsElement>16891366</segmentIDsElement>
              <segmentIDsElement>16891356</segmentIDsElement>
              <segmentIDsElement>19739251</segmentIDsElement>
            </segmentIDs>
            <startOffset>146.87466</startOffset>
            <endOffset>131.26929</endOffset>
          </geometrySectionLoc>
        </linkElementElement>
      </linkElement>
      <linkElement>
        <linkElementElement>
          <geometrySectionLoc>
            <startSegmentDirection>REF_TO_NONREF</startSegmentDirection>
            <segmentIDs>
              <segmentIDsElement>19950647</segmentIDsElement>
              <segmentIDsElement>19810066</segmentIDsElement>
              <segmentIDsElement>16900449</segmentIDsElement>
              <segmentIDsElement>16900448</segmentIDsElement>
            </segmentIDs>
            <startOffset>287.70465</startOffset>
            <endOffset>146.11018</endOffset>
          </geometrySectionLoc>
        </linkElementElement>
      </linkElement>
    </link>
    <linkID>GCM-GATEWAY-50010</linkID>
    <linkDesc>SB:I-94:Lake Cook:Eisenhower:IL</linkDesc>
    <length>36537</length>
    <locationTimeStamp>0</locationTimeStamp>
    <isBasic>false</isBasic>
    <travelTime>1488</travelTime>
    <volume>230</volume>
    <speed>24.536932</speed>
    <occupancy>2.1264489</occupancy>
    <congestionLevel>LIGHT_CONGESTION</congestionLevel>
    <locStatus>LOCATION_RESOLVED_AUTO</locStatus>
    <dataStatus>FIELD_DATA_VALIDATED_AUTO</dataStatus>
    <timeStamp>1057735036959</timeStamp>
  </com.gcmtravel.LinkTrafficReportElement>
</com.gcmtravel.LinkTrafficReport>
```

### Dynamic Message Sign Report XSchema for DMSReport.xml.gz

The following XSchema defines the format of DMSReport.xml:

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:simpleType name="com.gcmtravel.DeviceType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="VDS_DEVICETYPE"/>
      <xs:enumeration value="DMS_DEVICETYPE"/>
      <xs:enumeration value="HAR_DEVICETYPE"/>
      <xs:enumeration value="WSS_DEVICETYPE"/>
      <xs:enumeration value="OTHER_DEVICETYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="com.gcmtravel.FIPSCode">
    <xs:sequence>
      <xs:element name="stateCode" type="xs:int"/>
      <xs:element name="countyCode" type="xs:int"/>
      <xs:element name="cityCode" type="xs:int"/>
    </xs:sequence>
  </xs:complexType>
  <xs:simpleType name="com.gcmtravel.FieldDataValidationStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="FIELD_DATA_NOT_VALIDATED"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_AUTO"/>
      <xs:enumeration value="FIELD_DATA_INFEASIBLE_FOUND_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_CORRECTED_MANUAL"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_AUTO"/>
      <xs:enumeration value="FIELD_DATA_VALIDATED_MANUAL"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.FieldDeviceStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_FIELD_DEVICE_STATUS"/>
      <xs:enumeration value="NONE_FIELD_DEVICE_STATUS"/>
      <xs:enumeration value="OPERATIONAL"/>
      <xs:enumeration value="OPERATIONAL_BUT_DEGRADED"/>
      <xs:enumeration value="NON_OPERATIONAL"/>
      <xs:enumeration value="COMMUNICATOINS_FAILURE"/>
      <xs:enumeration value="DOWN_FOR_MAINTENANCE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.HDatumType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NAD27"/>
      <xs:enumeration value="NAD83"/>
      <xs:enumeration value="WGS84"/>
      <xs:enumeration value="WGS84_PLUS_EGM96"/>
      <xs:enumeration value="OTHER_HDATUM_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.LocationResolutionStatus">
    <xs:restriction base="xs:string">
      <xs:enumeration value="LOCATION_NO_LOCATION"/>
      <xs:enumeration value="LOCATION_NON_SRA"/>
      <xs:enumeration value="LOCATION_PARTIALLY_NON_SRA"/>
      <xs:enumeration value="LOCATION_NOT_VALIDATED"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_AUTO"/>
      <xs:enumeration value="LOCATION_UNRESOLVABLE_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_PARTIALLY_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_AUTO"/>
      <xs:enumeration value="LOCATION_CORRECTED_AND_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_MANUAL"/>
      <xs:enumeration value="LOCATION_RESOLVED_AUTO"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_DIRECTION_TYPE"/>
      <xs:enumeration value="EAST_BOUND"/>
      <xs:enumeration value="WEST_BOUND"/>
      <xs:enumeration value="SOUTH_BOUND"/>
      <xs:enumeration value="NORTH_BOUND"/>
      <xs:enumeration value="SOUTH_EAST_BOUND"/>
      <xs:enumeration value="SOUTH_WEST_BOUND"/>
      <xs:enumeration value="NORTH_EAST_BOUND"/>
      <xs:enumeration value="NORTH_WEST_BOUND"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.RoadwayType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="UNKNOWN_ROADWAY_TYPE"/>
      <xs:enumeration value="FREEWAY"/>
      <xs:enumeration value="FREEWAY_EXPRESS"/>
      <xs:enumeration value="FREEWAY_HOV"/>
      <xs:enumeration value="FREEWAY_REVERSIBLE"/>
      <xs:enumeration value="ARTERIAL"/>
      <xs:enumeration value="LOCAL_ROAD"/>
      <xs:enumeration value="RAMP"/>
      <xs:enumeration value="OTHER_ROADWAY_TYPE"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.SegmentDirectionType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="REF_TO_NONREF"/>
      <xs:enumeration value="NONREF_TO_REF"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="com.gcmtravel.StreetNameAffix">
    <xs:restriction base="xs:string">
      <xs:enumeration value="NONE"/>
      <xs:enumeration value="N"/>
      <xs:enumeration value="NE"/>
      <xs:enumeration value="E"/>
      <xs:enumeration value="SE"/>
      <xs:enumeration value="S"/>
      <xs:enumeration value="SW"/>
      <xs:enumeration value="W"/>
      <xs:enumeration value="NW"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:complexType name="void">
    <xs:sequence>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.DMSMessageSet">
    <xs:sequence>
      <xs:element name="dmsLines">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="dmsLinesElement" type="xs:string"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="messageExpiration" type="xs:long"/>
      <xs:element name="lastUpdateTime" type="xs:long"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.GeometryPoint">
    <xs:sequence>
      <xs:element name="direction" type="com.gcmtravel.SegmentDirectionType"/>
      <xs:element name="segmentID" type="xs:long"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLong">
    <xs:sequence>
      <xs:element name="latitude" type="xs:int"/>
      <xs:element name="longitude" type="xs:int"/>
      <xs:element name="hDatum" type="com.gcmtravel.HDatumType"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RoadwayName">
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="prefix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="suffix" type="com.gcmtravel.StreetNameAffix"/>
      <xs:element name="streetType" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.AddressPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="addressNumber" type="xs:string"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LandmarkPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="landmarkName" type="xs:string"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.LatLongPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="coord" type="com.gcmtravel.LatLong"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.MilePointPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="milePoint" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.CrossStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="crossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="crossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="crossStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.RampPoint">
    <xs:sequence>
      <xs:element name="fromRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="fromRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="toRoadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toRoadwayType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="offset" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.BetweenStreetPoint">
    <xs:sequence>
      <xs:element name="roadName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="direction" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="type" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fips" type="com.gcmtravel.FIPSCode"/>
      <xs:element name="fromCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="fromCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="fromStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="toCrossStreetName" type="com.gcmtravel.RoadwayName"/>
      <xs:element name="toCrossStreetType" type="com.gcmtravel.RoadwayType"/>
      <xs:element name="toStreetDirection" type="com.gcmtravel.RoadwayDirectionType"/>
      <xs:element name="offsetPercentage" type="xs:double"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.PointLocationProfile">
    <xs:choice>
      <xs:element name="__default" type="void"/>
      <xs:element name="rampPointLoc" type="com.gcmtravel.RampPoint"/>
      <xs:element name="latLongPointLoc" type="com.gcmtravel.LatLongPoint"/>
      <xs:element name="landmarkPointLoc" type="com.gcmtravel.LandmarkPoint"/>
      <xs:element name="addressPointLoc" type="com.gcmtravel.AddressPoint"/>
      <xs:element name="milePointPointLoc" type="com.gcmtravel.MilePointPoint"/>
      <xs:element name="crossStreetPointLoc" type="com.gcmtravel.CrossStreetPoint"/>
      <xs:element name="betweenStreetPointLoc" type="com.gcmtravel.BetweenStreetPoint"/>
      <xs:element name="geometryPointLoc" type="com.gcmtravel.GeometryPoint"/>
    </xs:choice>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.FieldDevice">
    <xs:sequence>
      <xs:element name="deviceStatus" type="com.gcmtravel.FieldDeviceStatus"/>
      <xs:element name="fieldDeviceID" type="xs:string"/>
      <xs:element name="type" type="com.gcmtravel.DeviceType"/>
      <xs:element name="location">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="locationElement" type="com.gcmtravel.PointLocationProfile"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="owningAgencyID" type="xs:string"/>
      <xs:element name="locStatus" type="com.gcmtravel.LocationResolutionStatus"/>
      <xs:element name="dataStatus" type="com.gcmtravel.FieldDataValidationStatus"/>
      <xs:element name="lastUpdateTime" type="xs:long"/>
      <xs:element name="locationTimeStamp" type="xs:long"/>
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="com.gcmtravel.DMS">
    <xs:sequence>
      <xs:element name="parent" type="com.gcmtravel.FieldDevice"/>
      <xs:element name="messageSets">
        <xs:complexType>
          <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element name="messageSetsElement" type="com.gcmtravel.DMSMessageSet"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
  <xs:element name="com.gcmtravel.DMSReport">
    <xs:complexType>
      <xs:sequence minOccurs="0" maxOccurs="unbounded">
        <xs:element name="com.gcmtravel.DMSReportElement" type="com.gcmtravel.DMS"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

### Sample Dynamic Message Sign Report

The following is a sample DMSReport.xml:

```xml
<?xml version="1.0" encoding="UTF-8"?>
  <com.gcmtravel.DMSReport>
  <com.gcmtravel.DMSReportElement>
    <parent>
      <deviceStatus>OPERATIONAL</deviceStatus>
      <fieldDeviceID>IL-TESTTIMS-I-88-E-ORCHARD</fieldDeviceID>
      <type>DMS_DEVICETYPE</type>
      <location>
        <locationElement>
          <crossStreetPointLoc>
            <roadName>
              <name>I-88</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName><direction>EAST_BOUND</direction>
            <type>UNKNOWN_ROADWAY_TYPE</type>
            <fips>
              <stateCode>17</stateCode>
              <countyCode>89</countyCode>
              <cityCode>3012</cityCode>
            </fips>
            <crossStreetName>
              <name>Orchard</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType>Rd</streetType>
            </crossStreetName>
            <crossStreetType>UNKNOWN_ROADWAY_TYPE</crossStreetType>
            <crossStreetDirection>UNKNOWN_DIRECTION_TYPE</crossStreetDirection>
            <offset>0.0</offset>
          </crossStreetPointLoc>
        </locationElement>
        <locationElement>
          <latLongPointLoc>
            <roadName><name>I-88</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>EAST_BOUND</direction>
            <type>UNKNOWN_ROADWAY_TYPE</type>
            <coord>
              <latitude>4179510</latitude>
              <longitude>-8835608</longitude>
              <hDatum>NAD83</hDatum>
            </coord>
          </latLongPointLoc>
        </locationElement>
        <locationElement>
          <geometryPointLoc>
            <direction>REF_TO_NONREF</direction>
            <segmentID>125139145</segmentID>
            <offset>549.09106</offset>
          </geometryPointLoc>
        </locationElement>
        <locationElement>
          <milePointPointLoc>
            <roadName>
              <name>I-88</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType></streetType>
            </roadName>
            <direction>EAST_BOUND</direction>
            <type>UNKNOWN_ROADWAY_TYPE</type>
            <fips>
              <stateCode>17</stateCode>
              <countyCode>89</countyCode>
              <cityCode>3012</cityCode>
            </fips>
            <milePoint>185750.12</milePoint>
          </milePointPointLoc>
        </locationElement>
      </location>
      <owningAgencyID>Illinois State Toll Highway Authority</owningAgencyID>
      <locStatus>LOCATION_RESOLVED_MANUAL</locStatus>
      <dataStatus>FIELD_DATA_VALIDATED_AUTO</dataStatus>
      <lastUpdateTime>1332375794000</lastUpdateTime>
      <locationTimeStamp>1260138818000</locationTimeStamp>
    </parent>
    <messageSets>
      <messageSetsElement>
        <dmsLines>
          <dmsLinesElement>IL-59 9 MIN</dmsLinesElement>
          <dmsLinesElement>I-355 17 MIN</dmsLinesElement>
          <dmsLinesElement>I-294 27 MIN</dmsLinesElement>
        </dmsLines>
        <messageExpiration>1332376489908</messageExpiration>
        <lastUpdateTime>1332375794000</lastUpdateTime>
      </messageSetsElement>
      <messageSetsElement>
        <dmsLines>
          <dmsLinesElement>DRIVE NOW</dmsLinesElement>
          <dmsLinesElement>TEXT LATER</dmsLinesElement>
          <dmsLinesElement><![CDATA[YOU CAN'T DO BOTH]]></dmsLinesElement>
        </dmsLines>
        <messageExpiration>1332376489908</messageExpiration>
        <lastUpdateTime>1332375794000</lastUpdateTime>
      </messageSetsElement>
    </messageSets>
  </com.gcmtravel.DMSReportElement>
  <com.gcmtravel.DMSReportElement>
    <parent>
      <deviceStatus>OPERATIONAL</deviceStatus>
      <fieldDeviceID>IL-TESTTSC-BISHOP_FORD-N-47</fieldDeviceID>
      <type>DMS_DEVICETYPE</type>
      <location>
        <locationElement>
          <crossStreetPointLoc>
            <roadName>
              <name>Bishop Ford</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType>Fwy</streetType>
            </roadName>
            <direction>NORTH_BOUND</direction>
            <type>UNKNOWN_ROADWAY_TYPE</type>
            <fips>
              <stateCode>0</stateCode>
              <countyCode>0</countyCode>
              <cityCode>0</cityCode>
            </fips>
            <crossStreetName>
              <name>145th</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType>St</streetType>
            </crossStreetName>
            <crossStreetType>UNKNOWN_ROADWAY_TYPE</crossStreetType>
            <crossStreetDirection>UNKNOWN_DIRECTION_TYPE</crossStreetDirection>
            <offset>0.0</offset>
          </crossStreetPointLoc>
        </locationElement>
        <locationElement>
          <latLongPointLoc>
            <roadName>
              <name>Bishop Ford</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType>Fwy</streetType>
            </roadName>
            <direction>NORTH_BOUND</direction>
            <type>UNKNOWN_ROADWAY_TYPE</type>
            <coord>
              <latitude>4163120</latitude>
              <longitude>-8757836</longitude>
              <hDatum>NAD83</hDatum>
            </coord>
          </latLongPointLoc>
        </locationElement>
        <locationElement>
          <geometryPointLoc>
            <direction>REF_TO_NONREF</direction>
            <segmentID>16880836</segmentID>
            <offset>556.7538</offset>
          </geometryPointLoc>
        </locationElement>
        <locationElement>
          <milePointPointLoc>
            <roadName>
              <name>Bishop Ford</name>
              <prefix>NONE</prefix>
              <suffix>NONE</suffix>
              <streetType>Fwy</streetType>
            </roadName>
            <direction>NORTH_BOUND</direction>
            <type>UNKNOWN_ROADWAY_TYPE</type>
            <fips>
              <stateCode>17</stateCode>
              <countyCode>31</countyCode>
              <cityCode>10487</cityCode>
            </fips>
            <milePoint>113867.06</milePoint>
          </milePointPointLoc>
        </locationElement>
      </location>
      <owningAgencyID>IL-TESTTSC</owningAgencyID>
      <locStatus>LOCATION_RESOLVED_MANUAL</locStatus>
      <dataStatus>FIELD_DATA_VALIDATED_AUTO</dataStatus>
      <lastUpdateTime>1332375179831</lastUpdateTime>
      <locationTimeStamp>1268773591000</locationTimeStamp>
    </parent>
    <messageSets>
      <messageSetsElement>
        <dmsLines>
          <dmsLinesElement>10 MINUTES TO</dmsLinesElement>
          <dmsLinesElement>DAN RYAN</dmsLinesElement>
        </dmsLines>
        <messageExpiration>0</messageExpiration>
        <lastUpdateTime>1332375179831</lastUpdateTime>
      </messageSetsElement>
    </messageSets>
  </com.gcmtravel.DMSReportElement>
</com.gcmtravel.DMSReport>
```

### Highway Advisory Reports

Highway Advisory Reports are not available at this time.
