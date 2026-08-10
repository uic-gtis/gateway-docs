# Versions

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

## Receiving XML Version 2 Files

At the time of writing, the only XML file that supports version 2.0 is the Incident file.

- [https://travelmidwest.com/lmiga/IncidentReport.xml.gz](https://travelmidwest.com/lmiga/IncidentReport.xml.gz) is version 1.0
- [https://travelmidwest.com/lmiga/IncidentReportV2.xml.gz](https://travelmidwest.com/lmiga/IncidentReportV2.xml.gz) is version 2.0

## Sending XML Version 2 Files

When sending XML data to the GTIS, both 1.0 and 2.0 are supported by detecting the version attribute in the uploaded content.
