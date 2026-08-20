# Gateway Traffic Data Archive

## Preamble

The Gateway traffic data archive is a project that was put together for archiving traffic data from the Gary-Chicago-Milwaukee Gateway system. The Gateway system allows one to access traffic data in gzip'd XML format. There are several XML files available: congestion, travel times, vehicle detector station (VDS) data, construction, special events, and incidents.

## Availability

### Real-Time Data

Data provided by our real-time feeds are packaged as gzip'd XML files. Please refer to [XML and Camera Image Download Manual](xml-and-camera-image-download-manual.md) for details.

To register for a download account:

1. Go to [https://go.travelmidwest.com/register](https://go.travelmidwest.com/register).
1. Select the checkbox labeled `**XML Data Feed and Camera Images**`.
1. Complete the remainder of the registration form.

### Archived Data

> [!NOTE]
> Due to the growing size of our traffic data archive, only the past 24 hours of data are available for immediate download. As of December 31, 2023 the compressed archive contains over 29.5 million files totaling approximately 8.4 TiB (roughly more than 50 TiB uncompressed).
>
> Please contact us at [traffic-data-archive@travelmidwest.com](mailto:traffic-data-archive@travelmidwest.com?subject=Traffic%20data%20archive%20bulk%20transfer%20request) to arrange for bulk transfer onto portable storage, e.g. USB drives.
>
> When requesting more than a year's worth of data, we recommend:
>
> - Formatting drives as [FAT](https://en.wikipedia.org/wiki/File_Allocation_Table) or [BTRFS](https://en.wikipedia.org/wiki/Btrfs) instead of [NTFS](https://en.wikipedia.org/wiki/NTFS) if at all possible because NTFS does not perform as well with large numbers of small files.
> - [CMR](https://en.wikipedia.org/wiki/Perpendicular_recording) instead of [SMR](https://en.wikipedia.org/wiki/Shingled_magnetic_recording) hard drives, or even better, [solid-state drives (SSD)](https://en.wikipedia.org/wiki/Solid-state_drive).
> - Consider using internal SATA HDD/SSD drives instead of USB connected drives if transfer speed is important.
> - Allow for a turnaround time of at least a few days, perhaps more, depending on the volume of data requested, transfer method and/or storage medium.

Navigating the data archive:

- Data prior to March 10, 2007 is stored slightly differently from files after that date. Prior to March 10, 2007, there are 24 “hour” directories in each “day” directory. There are no sub-directories for each type of data, they are all located in the “hour” directory.
- After March 10, 2007, there is a per-year subdirectory (as of this document's writing, the archive spans the years 2007 thru 2023).
- Each year's subdirectory contains a per-month subdirectory. The monthly subdirectories are 2008/01, 2008/02, ... 2008/12, etc.
- Each monthly subdirectory in turn contains a per-day subdirectory.
- Within each daily subdirectory, there are subdirectories for each data type.
- We do not provide documentation for the raw data subdirectories `d4`, `d8`, `gai`, `indot`, `mdot`, `mndot`, and `wisdot`. Please contact the corresponding agencies for details regarding the information in their data feeds.

Archived files use the following naming scheme: `yyyy.MM.dd-hh.mm.ss-TYPE.gz`

| Field | Description |
| --- | --- |
| yyyy | 4-digit year |
| MM | 2-digit month |
| dd | 2-digit day of the month |
| hh | 00 to 23 |
| mm | 0 to 59 |
| ss | 0 to 59 |
| TYPE | travel / dms / har / vds / incidents / special / congestion |

| **Directory** | **Description** |
| --- | --- |
| announcements | Press releases related to road closures |
| congestion | High, medium, low congestion data for each link on the map. Includes link's start/end lat/long, link status, congestion value, speed and a timestamp |
| construction | Road work information (some of the data in these files is for future road work) |
| d4 | Raw data files from IDOT District 4, before they get converted into standard formats in congestion, construction, dms, incidents, traffic and vds sub-directories |
| d8 | Raw data files from IDOT District 8, before they get converted into standard formats in congestion, construction, dms, incidents, traffic and vds sub-directories |
| detailed_congestion | Similar to congestion sub-directory, except XML files also contain speed data |
| dms | Dynamic message sign text status and location |
| gai | Raw data files from IDOT's GettingAroundIllinois.com, before they get converted into standard formats in congestion, construction, dms, incidents, traffic and vds sub-directories |
| incidents | Active incident location, type, and lanes affected |
| indot | Raw data files from InDOT, before they get converted into standard formats in congestion, construction, dms, incidents, traffic and vds sub-directories |
| map | Gateway traffic map. |
| mdot | Raw data files from MDOT, before they get converted into standard formats in congestion, construction, dms, incidents, traffic and vds sub-directories |
| mndot | Raw data files from MnDOT, before they get converted into standard formats in congestion, construction, dms, incidents, traffic and vds sub-directories |
| motd | Message of the day archive - text messages that appear at the top of travelmidwest.com - mostly contains incident information from incidents sub-directory |
| traffic | Travel time for selected expressway routes. The start lat/long, end lat/long, travel time (in seconds), link length (in meters), and average speed (in m/s) are included |
| vds | Vehicle detector station (VDS) data. Includes sensor's lat/long location, satus, occupancy percentage and volume of vehicles over last 60 minutes per lane. |
| wisdot | Raw data files from WisDOT, before they get converted into standard formats in congestion, construction, dms, incidents, traffic and vds sub-directories |

## Data Definitions

The archive holds the same XML the live feeds serve, so the definitions of its fields are the ones in the [Gateway External Interface User Guide](gateway-external-interface-user-guide/README.md). This section used to repeat them in CORBA IDL; the guide is the single copy now, and gives them as the XSD the feeds are validated against. With few exceptions the field names are an exact 1-to-1 match with the tags in the archived files.

| For | See |
| --- | --- |
| Location profiles — lat/long, landmark, address, mile marker, cross street, ramp, geometry and text — and the lane descriptions that go with them | [Locations](gateway-external-interface-user-guide/locations.md) |
| `RoadwayEvent`, the fields incidents, road work and special events share, and the incident, roadwork and special event reports built on them | [Roadway Events](gateway-external-interface-user-guide/roadway-events.md) |
| Vehicle detector station, weather sensor station, dynamic message sign and highway advisory radio reports | [Device Station Reports](gateway-external-interface-user-guide/device-station-reports.md) |
| Link congestion and link travel time reports | [Traffic Reports](gateway-external-interface-user-guide/traffic-reports.md) |
| The XML schema for each report in one place | [Gateway XML Reference](gateway-external-interface-user-guide/gateway-xml-reference.md) |
| Which of these are version 2.0 only | [Versions](gateway-external-interface-user-guide/versions.md) |
