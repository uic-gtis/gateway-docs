# Projects

## About

A list of major construction projects that appear on the website menu is provided via the `projectsMenuItems.json` file.

## projectsMenuItems.json

### Request

```console
https://travelmidwest.com/lmiga/projectsMenuItems.json
```

### Response

The response for a projectsMenuItems.json request will be an array of project menu items, each with the following attributes:

- label — a string for the menu item label
- url — the URL that the menu should link to

### Example

```json
[
  {
    "label":"IL  I-57: Rebuilding from Chicago to Carbondale",
    "link":"https://idot.illinois.gov/about-idot/stay-connected/blog/i-57-rebuild.html"},
  {
    "label":"IL I-57/74 Interchange Reconstruction (Champaign)",
    "link":"https://idot.illinois.gov/projects/I57-I74-Reconstruction-Project/overview#top"
  },
  {
    "label":"IL I-80 Corridor: Ridge Rd to US-30 (Will County)",
    "link":"https://www.i80will.org/"
  },
  {
    "label":"IL Jane Byrne Interchange",
    "link":"https://www.janebyrneinterchange.org/"
  },
  {
    "label":"Jane Byrne Camera",
    "link":"janeByrneInterchangeCameras.jsp"
  },
  {
    "label":"Zoo Interchange  (WI)",
    "link":"https://projects.511wi.gov/zoo-interchange-project/"
  }
]
```
