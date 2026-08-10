# RSS Feeds

## Standard Fields

Standard fields for all of our [RSS](https://wikipedia.org/wiki/RSS) feeds:

| Field Name | Description |
| --- | --- |
| title | Travel Midwest Information for `[STATE_NAME]` |
| link | [https://travelmidwest.com/](https://travelmidwest.com/) |
| description | Travel Midwest Information for `[STATE_NAME]` |
| language | en/us *(U.S. English)* |
| docs | [https://blogs.law.harvard.edu/tech/rss](https://blogs.law.harvard.edu/tech/rss) *(standard RSS value)* |
| webMaster | [webmaster@travelmidwest.com](mailto:webmaster@travelmidwest.com) |

## News & Alerts

| Type | URL |
| --- | --- |
| Travel-related news and construction announcements. | [https://travelmidwest.com/lmiga/rss.jsp?type=announcement](https://travelmidwest.com/lmiga/rss.jsp?type=announcement) |
| Traffic alerts | [https://travelmidwest.com/lmiga/rss.jsp?type=message](https://travelmidwest.com/lmiga/rss.jsp?type=message) |

## Lane Closures

Incidents, construction and special events for which there are full or partial lane closures.

URL syntax:

```
https://travelmidwest.com/lmiga/news.jsp?state=STATE_NAME&type=TYPE_NAME
```

`STATE_NAME` is one of the following states in travelmidwest.com's geographical coverage:

- `**Illinois**`
- `**Indiana**`
- **`Iowa`**
- `**Michigan**`
- **`Wisconsin`**

`TYPE_NAME` is one of the following types:

- **`all`** – All incidents, construction events, and special events for which there are full or partial lane closures.
- **`incident`** – All incidents for which there are full or partial lane closures.
- **`construction`** – All construction events for which there are full or partial lane closures.
- **`specialEvent`** – All special events for which there are full or partial lane closures.

Notes:

- Case-sensitivity matters in all of the above — e.g. "Illinois" is valid, but "illinois" is not; "specialEvent" is valid, but "specialevent" is not.
- Not every `STATE_NAME` + `TYPE_NAME` combination will return results.

Examples:

| Type | URL |
| --- | --- |
| All types of events in Illinois for which there are full or partial lane closures. | [https://travelmidwest.com/lmiga/news.jsp?state=Illinois&type=all](https://travelmidwest.com/lmiga/news.jsp?state=Illinois&type=all) |
| Only construction events in Wisconsin for which there are full or partial lane closures. | [https://travelmidwest.com/lmiga/news.jsp?state=Wisconsin&type=construction](https://travelmidwest.com/lmiga/news.jsp?state=Wisconsin&type=construction) |

Fields for each item:

| Field Name | Description |
| --- | --- |
| Title | `[TYPE_NAME]` (see `TYPE_NAME` explanation above): `[LOCATION]`, where `[LOCATION]` includes details about the street name(s), traffic direction(s) (e.g., EB, which means eastbound) on those streets, city, county, and state (or other similar information), e.g., "Construction: SB I-294 (Tri-State Tollway) at 82nd St Plaza, Justice, Cook, IL". |
| Link | Link to the item in question on travelmidwest.com, on the map. |
| Date | Item creation date. |
| Description | Items within the// *description field:<br>* Closure Details – Either "full closure" or "partial closure".<br>* Location – Street name.<br>* Link – link to the item in question on travelmidwest.com, on the map.<br>* "alternative" experimental fields, (temporarily for a specialized user of this feed; these might be removed at any time):<br>** Alt Expected End Date – Expected end date of the item.<br>** Alt Location String – Longer description of the location, i.e., direction + on road name + cross street of start and end road name + city + state.<br>** Alt Description – Full description for the item.<br>** Alt Closure Details – More details about the closure, i.e., the description based on minimum and maximum lanes closed //(this is somewhat a "technical" description as there is no user-friendly way to express it)*. |
| Category | One of the following:<br>* Incidents<br>* Construction<br>* Special Events |
| Author | webmaster@travelmidwest.com |
