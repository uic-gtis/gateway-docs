# XML Upload Manual

## Introduction

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

### JSON response variant

The endpoint above answers with an HTML page reading "OK" or "ERROR", which tells you
whether the report as a whole was accepted but nothing about the individual objects in
it. A second endpoint publishes exactly the same way — same `report` parameter, same
processing, same logging — but answers with JSON:

```
https://travelmidwest.com/lmiga/publisher/publish.json
```

The response describes each object that was published, along with any per-object errors,
so a client can tell which items in a multi-object report succeeded. A request with a
missing or empty `report` parameter returns a validation error rather than an HTML error
page.

Both endpoints are current; use whichever suits your client. The `datapublisher` role
and authentication requirements are identical.

## Schemas

XML schemas for the various types of reports that can be sent to the Gateway via its XML upload service are available in the attachments section at the bottom of this page.

The fields contained in these schemas are described in the [Gateway External Interface User Guide](user-guides-and-manuals/gateway-external-interface-user-guide/README.md) document.

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

# Use testing.travelmidwest.com while developing, travelmidwest.com in production
my $uri = "https://travelmidwest.com/lmiga/publisher";
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
