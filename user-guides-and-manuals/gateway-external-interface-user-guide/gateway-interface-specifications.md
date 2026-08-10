# Gateway Interface Specifications

As a central hub of information, the Gateway will be exchanging data with a number of data sources and data users. The data to be collected and redistributed includes primarily traffic status information, traffic related incidents and scheduled events such as roadwork, and weather information. In order for the Gateway and relevant agencies to exchange data across a multitude of heterogeneous platforms and operating environments efficiently without ambiguity, the structures of data to be exchanged have been specified using Interface Definition Language (IDL) but then later converted to XML Schema Definition Language (XSD). There is a one-to-one mapping between the IDL and XSD formats thus maintaining backwards compatibility of data.

The specifications were based on various relevant national standardization efforts, such as Traffic Management Data Dictionary (TMDD), Message Sets for External Traffic Management Center Communications (MS/ETMC2), Location Reference Message Specification (LRMS), Message Exchange for Travel Situations (METS), and the Showcase Project.

The Gateway external data standards provide data specifications for:

- Location referencing
- Device data reports from vehicle detectors, weather sensors, dynamic message signs, and highway advisory radios
- Event reporting for incidents and scheduled events that affect the traveler
- Traffic status reporting, such as congestion levels and travel times

Detailed discussions of these specifications are provided in the following sections. These explanations include relevant parts of the XSD and XML. The full and up-to-date XML definitions for any section is given in the [XML and Camera Image Download Manual](../xml-and-camera-image-download-manual.md), which should be used as the final reference. It should be stated that the work of specifying standards is on-going, and that the specifications will evolve further as time progresses.

## Uploading and Downloading Traffic Information

See the [XML Upload Manual](../../xml-upload-manual.md) for publishing XML to the GTIS and the [XML and Camera Image Download Manual](../xml-and-camera-image-download-manual.md) for how to download data from the GTIS. Data may also be downloaded in Javascript Object Notation (JSON) format as specified in [JSON Traffic Information Download Manual](../../gateway-api/README.md) or CSV format for [Camera Meta-Data (cameraInfo.csv)](../../camera-info-csv.md).

## Basics for Understanding Definitions

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
