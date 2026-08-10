# Camera Upload Manual

## About

This manual describes several simple methods for providing camera images to the Gateway over the internet.

See also:

- [GTIS Smart Work Zone Specifications for Construction Contractors and Vendors](gtis-smart-work-zone-specifications.md)
- [XML and Camera Image Download Manual](xml-and-camera-image-download-manual.md)

## cctvSnapshots.xml

In addition to camera images, the Gateway also requires a `cctvSnapshots.xml` file that contains [metadata](https://en.wikipedia.org/wiki/Metadata) used to position camera icons and thumbnail images on the TravelMidwest.com website.

Sample [XML](https://en.wikipedia.org/wiki/XML) for two cameras:

```xml
<cctvCameras>
  <camera>
    <id>TWR_Lisle_West_EB</id>
    <description>TWR Lisle West EB</description>
    <approaches>
      <approach>
        <direction>west</direction>
        <description>West Leg</description>
        <filename>TWR_Lisle_West_EB_cctv_West_Leg.jpg</filename>
        <lastUpdated>1401885681248</lastUpdated>
        <isUnavailableImage>false</isUnavailableImage>
      </approach>
    </approaches>
    <location>
      <road>I-88</road>
      <milepost>131.2</milepost>
      <latitude>41.80942153930664</latitude>
      <longitude>-88.05293273925781</longitude>
    </location>
    <snapshotsBlocked>false</snapshotsBlocked>
  </camera>
  <camera>
    <id>TWR_Golf_NB</id>
    <description>TWR Golf NB</description>
    <approaches>
      <approach>
        <direction>north</direction>
        <description>North Leg</description>
        <filename>TWR_Golf_NB_cctv_North_Leg.jpg</filename>
        <lastUpdated>1401885072680</lastUpdated>
        <isUnavailableImage>false</isUnavailableImage>
      </approach>
      <approach>
        <direction>south</direction>
        <description>South Leg</description>
        <filename>TWR_Golf_NB_cctv_South_Leg.jpg</filename>
        <lastUpdated>1401885072755</lastUpdated>
        <isUnavailableImage>false</isUnavailableImage>
      </approach>
    </approaches>
    <location>
      <road>I-294</road>
      <milepost>45.4</milepost>
      <latitude>42.05561065673828</latitude>
      <longitude>-87.86768341064453</longitude>
    </location>
    <snapshotsBlocked>false</snapshotsBlocked>
  </camera>
</cctvCameras>
```

The <`cctvCameras>` element contains one or more `<camera>` sub-elements:

- **camera** — Contains the `<id>`, `<description>`, `<approaches>`, `<location>` and `<snapshotsBlocked>` sub-elements.
  - **id** — Unique identifier for the camera. Used by the Gateway to store a camera in its database and to reference a camera in website URLs.
  - **description** — Short description of where a camera is and what it is looking at.
  - **approaches** — Contains one or more sub-elements describing a view a camera has of its surroundings. For instance, a camera may be programmed to look in two directions down a road, each direction would be an approach:
    - direction — Direction a camera is pointing: north, south, east, west
    - description — Not presently used.
    - filename — Name of the file uploaded to the same directory as the `cctvSnapshots.xml` file where this approach of this camera is stored.
    - lastUpdated — Time in milliseconds since midnight on 1/1/1970 until a camera image was last updated.
    - isUnavailableImage — Not presently used.
  - **location** — Describes where a camera is located plus the latitude and longitude control where a camera icon is placed on the Gateway map:
    - road — Name of the road a camera is on or near. Interstates should be formatted as "I-xx" where xx is the Interstate number as in "I-80" or "I-294".
    - milepost — Milepost number where a camera is located. Should be a decimal number such as "80.4".
    - latitude — Latitude in decimal degrees.
    - longitude — Longitude in decimal degrees.
  - **snapshotsBlocked** — Not presently used.

## Transfer Methods

### Uploads via Syncthing

[Syncthing](https://en.wikipedia.org/wiki/Syncthing) is a secure cross-platform open-source peer-to-peer file synchronization application. Currently the most efficient and robust method we support, generally requiring the least amount of network bandwidth and system resources.

After contacting us ([cameras@travelmidwest.com](mailto:cameras@travelmidwest.com?subject=Syncthing)) regarding interest in transferring camera images via Syncthing:

1. Download and install Syncthing: [https://syncthing.net/downloads/](https://syncthing.net/downloads/)
1. Access your Syncthing's web-based interface (default private URL: [http://127.0.0.1:8384/](http://127.0.0.1:8384/)).
1. Under the **Remote Devices** section, click the [Add Remote Device] button.
1. Under the **General** tab, enter the **Device ID** for our Syncthing server.
1. Assign a preferred **Device Name** (e.g. Travel Midwest).
1. Click the [Save] button.
1. Under the **Folders** section, click the [Add Folder] button.
1. Under the **General** tab, assign a preferred **Folder Label**.
1. Update **Folder Path** to point to your source folder.
1. Copy the **Folder ID** (e.g., ABCDE-12345) for use in the final step below.
1. Under the **Sharing** tab, tick the checkbox for the new remote device that was added in steps 3 thru 6.
1. Under the **Advanced** tab, change the **Folder Type** to "Send Only" (we will set our end to "Receive Only").
1. Tick the checkbox for **Ignore Permissions**.
1. Click the [Save] button.
1. Please email the **Folder ID** copied during step 10 to [syncthing@travelmidwest.com](mailto:syncthing@travelmidwest.com?subject=Syncthing%20Folder%20ID) so that we know you are ready to begin file transfers.

As soon as we accept your connection, your Syncthing instance will monitor your specified folder and mirror any changes to our server in near real-time. Syncthing also offers options for configuring a custom sync delay and/or interval, plus a robust [REST API](https://docs.syncthing.net/dev/rest.html) for additional flexibility.

See also:

- *Syncthing Downloads* — [https://syncthing.net/downloads/](https://go.travelmidwest.com/syncthing-downloads)
- *Getting Started* — [https://docs.syncthing.net/intro/getting-started.html](https://go.travelmidwest.com/syncthing-getting-started)
- *An Intro to the GUI* — [https://docs.syncthing.net/intro/gui.html](https://go.travelmidwest.com/syncthing-intro-gui)
- *Starting Syncthing Automatically* — [https://docs.syncthing.net/users/autostart.html](https://go.travelmidwest.com/syncthing-autostart)

### Uploads via FTPS

1. Install a suitable FTP client that supports the [FTPS](https://en.wikipedia.org/wiki/FTPS) protocol. Compatible clients we have tested include, but are not limited to:
1*. cURL ([https://curl.se/](https://curl.se/))
1*. FileZilla ([https://filezilla-project.org/](https://filezilla-project.org/))
1*. lftp ([https://github.com/lavv17/lftp/](https://github.com/lavv17/lftp/))
1*. rclone ([https://rclone.org/](https://rclone.org/))
1*. SyncBackPro ([https://2brightsparks.com/syncback/sbpro.html](https://2brightsparks.com/syncback/sbpro.html))
1*. WinSCP ([https://winscp.net/](https://winscp.net/))
1. Use the following connection settings:
1*. **Server:** `files.travelmidwest.com`
1*. **Network port:** `21/tcp`
1*. **Security:** `FTPS (FTP over SSL) with SSL/TLS Explicit encryption` (aka. "FTPES" mode).
1*. **Data transfer mode:** `passive`
1. Please email a request for FTP user credentials to [cameras@travelmidwest.com](mailto:cameras@travelmidwest.com?subject=Requesting%20FTP%20user%20account).

See also:

- [https://en.wikipedia.org/wiki/Comparison_of_FTP_client_software](https://en.wikipedia.org/wiki/Comparison_of_FTP_client_software)

### Downloads via FTP/HTTP

Camera images in JPEG format along with a companion `cctvSnapshots.xml` file are downloaded by the Gateway from an internet accessible FTP(S) or HTTP(S) server.

Please forward connection details to [cameras@travelmidwest.com](mailto:cameras@travelmidwest.com.?subject=Camera%20image%20downloads%20via%20FTP%2FHTTP) (if preferred, any required user credentials may also be provided via other methods).
