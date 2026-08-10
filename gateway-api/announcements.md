# Announcements

## About

The **Gateway Traveler Information System (GTIS)** provides some traffic information in [JSON](https://wikipedia.org/wiki/JSON) format in addition to our standard [XML formats](../user-guides-and-manuals/xml-and-camera-image-download-manual.md) (our XML format supports more types of data and the content of the data is richer while the JSON format is suitable for mobile devices because the data is more compact and easier to parse).

## Announcements

Announcements are important traveler related news stories and come in one of six types "construction", "newsItem", "highPriority", "siteNews", "transit", and "weather".

### Request

```console
https://travelmidwest.com/lmiga/announcements.json?type=[type]&state=[state]
```

A request takes two required parameters "type" and "state":

- "type" — must be one of "construction", "newsItem", "highPriority", "siteNews", "transit", or "weather".
- "state" — must be one of "Regional", "Illinois", "Indiana", "Michigan", "Wisconsin", "Iowa", "Missouri" or "Kentucky".
Note that the blank string ("") can be passed for state in which case all announcements of the given "type" will be returned.

### Response

An Announcements request returns an array of JSON objects with the following fields:

- id — identifier for announcement
- title — Title of announcement
- html — HTML markup with content of announcement
- icon — URL of icon for announcement (relative to [https://travelmidwest.com/limga](http://www.travelmidwest.com/limga))
- link — URL of related web page for announcement
- creationDate — milliseconds since epoch to date of announcement's creation
- lastUpdate — milliseconds since epoch (1/1/1970 Midnight) to time this announcement was last updated
- events — array of event identifiers that are associated with this announcement (may be empty)

### Example

```console
https://travelmidwest.com/lmiga/announcements.json?type=construction&state=Michigan
```

```
[
    {
        "creationDate": 1421773462670,
        "html": "<p><strong>Fast Facts:</strong></p>\r\n<ul>\r\n    <li><strong>The original span of the Blue Water Bridge will be closed for resurfacing beginning in April.</strong></li>\r\n    <li><strong>The eastbound span of the Blue Water Bridge will accommodate both directions of traffic throughout the project.</strong></li>\r\n    <li><strong>This work will preserve the safety and reliability of the Blue Water Bridge.</strong></li>\r\n</ul>\r\n<p>The Blue Water Bridge international crossing in Port Huron will be partially closed beginning in April for resurfacing and waterproof undercoating on its original span. Work on the bridge is expected to be finished by July 1. The Michigan Department of Transportation (MDOT) and Blue Water Bridge Canada (BWBC), co-owners of the Blue Water Bridge, are coordinating the work on this project.<br />\r\n<br />\r\nThe original bridge, built in 1937, currently serves westbound traffic entering the United States. The eastbound portion of the bridge, built in 1997, will be used to accommodate both directions of international traffic throughout the project. Only one lane of traffic will be open in each direction across the bridge, with two lanes available in each direction as vehicles approach the toll plazas at each end of the bridge.<br />\r\n<br />\r\n&quot;This important project continues the long-term commitment of MDOT and BWBC to maintain and preserve the safety and reliability of the Blue Water Bridge,&quot; said MDOT Blue Water Bridge Manager Mike Szuch. &quot;We will do our best to minimize and manage any short-term traffic delays for cross-border travelers.&quot;<br />\r\n<br />\r\nLimited lane availability during this project will prevent the use of a dedicated lane for NEXUS and F.A.S.T. motorists, as well as buses. Wide loads will be restricted to less than 11 feet, and bicyclists cannot be accommodated during the construction. Due to the longer wait times expected at the border, motorists are encouraged to travel at off-peak hours if possible, or travel south to use the international bridge or tunnel crossings in the Detroit/Windsor area.<br />\r\n<br />\r\nMDOT and BWBC have been seeking input and assistance from local border security and public safety agencies to ensure that the most efficient traffic plans are incorporated into this project. Traffic flow and sign placement are being developed to help reduce delays and keep vehicles moving safely. Staffs from both agencies also are refining their daily traffic management procedures to promote the efficient flow of vehicles during work, while also maintaining emergency vehicle access.</p>\r\n<p>For Blue Water Bridge traffic updates and other bridge information on Twitter, follow <a href=\"http://www.twitter.com/MDOT_BWB\">www.twitter.com/MDOT_BWB</a> and <a href=\"http://www.twitter.com/bluewaterbridge\">www.twitter.com/bluewaterbridge</a>.</p>",
        "icon": "webfile/images/MDOT_new.png",
        "lastUpdate": 1422306592182,
        "link": "http://www.michigan.gov/drive",
        "title": "Blue Water Bridge Resurfacing Spring 2015"
    }
]
```
