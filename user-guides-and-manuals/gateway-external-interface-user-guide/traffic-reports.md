# Traffic Reports

Traffic reports available on the Gateway are the Link Congestion report, the Travel Time Report, and the Link Traffic report. Congestion and other traffic parameters are reported on a "link" basis. A link is a sequence of spatially contiguous sections which can be sections from different roadways.

Traffic Reports report the congestion levels of links only. The Traffic Report contains a more complete set of traffic parameters than Congestion Reports, including travel times, speeds and occupancy. Congestion reports are generated when the link reported about is not defined for traffic reporting. Both reports have the report ID and time stamp.

The Travel Time Report is specialized to contain data for users interested particularly in the travel time view of traffic conditions. It contains a link location, and linkID made up of well-known sub-parts for easy reference. Included is a string for human consumption with a meaningful translation of the location information, e.g. Highway X from Cross Road Y to Cross Road Z.

The data for the Traffic Reports contain a time when the location was entered as a check on the identification of the data in the system. The structs are updated without the location being changed when the same traffic condition changes. Two structs with the same locations are about the same traffic condition even if the ids aren't the same. When the location changes the traffic data is about another traffic condition.

## Link Congestion Reports

Link congestion reports contain low, medium, high congestion level information on detectorized road ways. Typical link lengths are from one half to one mile.

### Link Congestion Input Format

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

### Link Congestion Output Format

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

### Congestion Level

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

### Link Congestion

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

## Link travel time reports

The specialized Link Travel Time Report contains a link travel time list.

### Link Traffic Input Format

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

### Link Traffic Output Format

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

### Link Traffic

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
