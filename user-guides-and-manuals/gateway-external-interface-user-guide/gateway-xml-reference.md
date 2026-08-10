# Gateway XML Reference

## Detector Report XSchema for VDSReport.xml.gz

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

## Sample Detector Report

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

## Incident Report XSchema Version 1 for IncidentReport.xml.gz

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

## Sample Incident Report

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

## Incident Report XSchema Version 2 for IncidentReportV2.xml.gz

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

## Construction Report XSchema for RoadWorkReport.xml.gz

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

## Sample Construction Report

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

## Special Event Report XSchema for SpecialEventReport.xml.gz

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

## Sample Special Event Report

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

## Congestion Report XSchema for LinkCongestionReport.xml.gz

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

## Sample Congestion Report

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

## Travel Time Report XSchema for LinkTrafficReport.xml.gz

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

## Sample Travel Time Report

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

## Dynamic Message Sign Report XSchema for DMSReport.xml.gz

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

## Sample Dynamic Message Sign Report

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

## Highway Advisory Reports

Highway Advisory Reports are not available at this time.
