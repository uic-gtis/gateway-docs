# dmsInfo.csv

The [XML and Camera Image Download Manual](https://confluence.travelmidwest.com/display/PUBLIC/XML+and+Camera+Image+Download+Manual) describes detailed dynamic message sign (DMS) data that can be accessed from the TravelMdiwest.com website for registered users while the `dmsInfo.csv` web service provides publicly available DMS data to all users:

```
https://travelmidwest.com/lmiga/dmsInfo.csv
```

Output is in comma-separated values (CSV) format compatible with spreadsheet (e.g. Microsoft Excel, LibreOffice Calc) plus other data processing applications and systems, e.g.:

```
id,y,x,timestamp,road_name,direction,location,mile_marker,message1,message2,message3,img_url,status
MO-MODOT-I64_WB_at_WO_Spoede_Ave,38.63622,-90.42281,2022-08-15T13:10Z,I-64,WB,WB I-64 at Spoede Rd (+0.4 miles),27.161048236658303,"[5 Min,  via 8 Min,  via 5 Min]","","","/messageSign?id=MO-MODOT-I64_WB_at_WO_Spoede_Ave",Operational
MO-MODOT-Rte_K_NB_at_S_Outer_Rd,38.74935,-90.69999,2022-08-15T13:10Z,MO-K,NB,NB MO-K at Pheasant Point Blvd,0.0,"","","","/messageSign?id=MO-MODOT-Rte_K_NB_at_S_Outer_Rd",Operational
MO-MODOT-I70_EB_at_At_Adelaide_Ave,38.67997,-90.21203,2022-08-15T13:10Z,I-70,EB,EB I-70 at Adelaide Ave,0.0,"","","","/messageSign?id=MO-MODOT-I70_EB_at_At_Adelaide_Ave",Operational
MO-MODOT-Rte_141_NB_at_Gravois_Bluff_Rd,38.50442,-90.44329,2022-08-15T13:10Z,MO-141,NB,NB MO-141 at Gravois Bluffs Blvd (-0.2 miles),0.0,"[Work Zone, Crashes Are Up, Take It Slow]","","","/messageSign?id=MO-MODOT-Rte_141_NB_at_Gravois_Bluff_Rd",Operational
MO-MODOT-I64_EB_at_EO_Boone's_Crossing,38.66939,-90.58619,2022-08-15T13:10Z,I-64,EB,EB I-64 at Boone's Crossing St (+0.7 miles),0.0,"[ 5 MIN,  8 MIN]","","","/messageSign?id=MO-MODOT-I64_EB_at_EO_Boone's_Crossing",Operational
MO-MODOT-I64_WB_at_WO_Daniel_Boone_Bridge,38.69819,-90.66681,2022-08-15T13:10Z,I-64,WB,WB I-64 at Missouri Research Park Cir (-0.5 miles),0.0,"[Winghaven 6 MIN, RTE N 8 MIN]","","","/messageSign?id=MO-MODOT-I64_WB_at_WO_Daniel_Boone_Bridge",Operational
IL-TESTTSC-US-45-LAWRENCE,41.96496,-87.87674,2022-08-15T13:13Z,US-12,WB,WB US-12 at Lawrence Ave,0.0,"[OBEY THE LIMIT, OR, PAY THE TICKET]","","","/messageSign?id=IL-TESTTSC-US-45-LAWRENCE",Operational
KY-KYTC-KYTC.DMS01002,37.06062,-88.65925,2022-08-15T13:12Z,I-24,WB,WB I-24 at US-62 (+0.3 miles),6.1263938391575055,"[DRIVE SOBER ,  OR GET ,  PULLED OVER ]","[ PLAN FOR A  ,  DESIGNATED ,  DRIVER]","","/messageSign?id=KY-KYTC-KYTC.DMS01002",Operational
KY-KYTC-KYTC.DMS01003,37.09995,-88.68916,2022-08-15T13:12Z,I-24,EB,EB I-24 at KY-305 (-0.2 miles),2.7852268104315496,"[DRIVE SOBER ,  OR GET ,  PULLED OVER ]","[ PLAN FOR A  ,  DESIGNATED ,  DRIVER]","","/messageSign?id=KY-KYTC-KYTC.DMS01003",Operational
```

The first line is a header row that provides field/column labels for the remaining rows:

| Column | Value |
| --- | --- |
| id | This is a unique identifier for thew DMS in the format "state-agency-id" where state is a state abbreviation like "IL", "MO", etc., agency is the name of the agency within the state that is providing the data, and id is an identifier unique to that agency. |
| y | Latitude in decimal degrees using the WGS84 datum. |
| x | Longitude in decimal degrees using the WGS84 datum. |
| timestamp | Timestamp in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| road_name | Name of the road or expressway that the DMS is located on. |
| direction | Direction of traffic on the road that the DMS is located on. It will be an abbreviation: NB, SB, EB, WB, NEB, NWB, SEB, or SWB. |
| location | Human readable description of the DMS's location. |
| mile_marker | Decimal mile marker that the DMS is located at on the road. This will be 0.0 if the mile marker is unknown. The units of this number are miles. |
| message1<br>message2<br>message3 | These are the "phases" of the DMS in text format. Each will be a list of lines separated by commas. Because these fields contains commas, they are quoted. Some DMS contain encoded images in their message fields. These will have empty message fields. The img_url field provides the image in these cases. |
| img_url | URL to an image representation of the sign as seen on the [DMS Report](https://travelmidwest.com/lmiga/dmsReport.jsp). |
| status | Status of the DMS: Unknown, Not available, Operational, Operation but degraded, Non-operational, Communication failure, or Down for maintenance. |

## Sign Images

The `img_url` values above point at the messageSign endpoint, which renders the sign's
current message as a PNG. It can be requested directly and used as an `<img src>`:

```console
https://travelmidwest.com/lmiga/messageSign?id=signExternalId
```

- **id** (required) — the DMS external ID, as in the `id` column above
- **small** (optional) — set to `true` for a reduced-size rendering

When a sign has several message phases they are stacked vertically into a single image.
A request for an unknown or missing `id`, or a sign whose image cannot be rendered,
returns a "not available" placeholder image rather than an error status. Responses are
cached for one minute and carry an ETag.

Questions and/or comments can be addressed to: [webmaster@travelmidwest.com](mailto:webmaster@travelmidwest.com?subject=dmsInfo.csv)
