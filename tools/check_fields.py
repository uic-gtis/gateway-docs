#!/usr/bin/env python3
"""Compare the response fields this documentation describes against the fields the
gateway actually serializes.

    python tools/check_fields.py --gateway /path/to/gateway
    python tools/check_fields.py --gateway /path/to/gateway --endpoint incidentMap.json

``check_coverage.py`` answers "is this endpoint documented at all?". This answers the
next question down: "are the *fields* we describe for it the fields it really returns?"

HOW IT WORKS, AND WHAT THAT MEANS FOR TRUSTING IT

The GeoJSON map endpoints all build their ``properties`` object from a small POJO --
``IncidentProperties``, ``CameraProperties``, ``DmsProperties`` and friends -- annotated
with Lombok ``@Getter`` and serialized by Jackson. So the wire field names are exactly
the POJO's instance field names, and both sides are statically extractable: the Java
fields by parsing the class, the documented names from the ``- name — description``
bullet lists the docs use.

That equivalence is the whole basis of this tool, and it is why the mapping below is
written out by hand rather than guessed. A class this cannot parse, or an endpoint whose
JSON is assembled some other way, must NOT be silently skipped -- it is reported as
UNMAPPED so the gap stays visible.

THIS TOOL PROPOSES, IT DOES NOT CONCLUDE

Every difference it prints is a *candidate*, to be confirmed by reading the code before
any document is edited. It cannot see:

  * value sets -- a field documented as "Major/Medium/Minor" that actually carries
    "New/Updated/Canceled" has the right *name*, so this tool says nothing. Several real
    errors found in the first pass were of exactly this kind.
  * types, formats, units, and null behaviour.
  * fields set only under a condition (``respDet`` is populated only for authenticated
    callers), which are still always serialized -- as null -- because these POJOs carry
    no @JsonInclude.
  * anything about request parameters.

So a clean run means "the field names line up", not "the documentation is correct".
Name-level agreement is the floor, not the ceiling.
"""

import argparse
import os
import re
import sys

# doc file -> heading under which the endpoint's fields are described -> Java properties
# class. Written out by hand and verified once, endpoint by endpoint; see the module
# docstring for why this is not inferred.
#
# "class" is the simple name of the properties POJO. Where a controller nests several
# (congestion has lines, popup and update forms), each documented section names its own.
MAPPING = {
    "incidentMap.json": {
        "doc": "gateway-api/map-data.md",
        "heading": "Incidents",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/IncidentMapJsonController.java",
        "class": "IncidentProperties",
    },
    "constructionMap.json": {
        "doc": "gateway-api/map-data.md",
        "heading": "Construction",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/ConstructionMapJsonController.java",
        "class": "ConstructionProperties",
    },
    "cameraMap.json": {
        "doc": "gateway-api/map-data.md",
        "heading": "cameraMap.json",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/CameraMapJsonController.java",
        "class": "CameraProperties",
    },
    "dmsMap.json": {
        "doc": "gateway-api/map-data.md",
        "heading": "Message Signs",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/DmsMapJsonController.java",
        "class": "DmsProperties",
    },
    "specialEventMap.json": {
        "doc": "gateway-api/map-data.md",
        "heading": "Special Events",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/SpecialEventMapJsonController.java",
        "class": "SpecialEventPropertiesDto",
    },
    "restAreaMap.json": {
        "doc": "gateway-api/map-data.md",
        "heading": "Rest Areas",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/RestAreaMapJsonController.java",
        "class": "RestAreaProperties",
    },
    "roadLabels.json": {
        "doc": "gateway-api/map-data.md",
        "heading": "Road Labels",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/RoadLabelsJsonController.java",
        "class": "LabelPropertiesDto",
    },
    "truckParkingMap.json": {
        "doc": "gateway-api/map-data.md",
        "heading": "Truck Parking",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/TpimsProperties.java",
        "class": "TpimsProperties",
    },
    "ferryMap.json": {
        "doc": "gateway-api/map-data.md",
        "heading": "Ferry",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/FerryMapJsonController.java",
        "class": "FerryProperties",
    },
    "congestionMap.json (lines)": {
        "doc": "gateway-api/map-data.md",
        "heading": "Congestion Lines",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/CongestionMapJsonController.java",
        "class": "CongestionLinesProperties",
    },
    "congestionMap.json (popup)": {
        "doc": "gateway-api/map-data.md",
        "heading": "Congestion Popup Data",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/CongestionMapJsonController.java",
        "class": "CongestionPopupProperties",
    },
    "realTimeTrafficMap.json (lines)": {
        "doc": "gateway-api/map-data.md",
        "heading": "Encoded Lines",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/RealTimeTrafficMapJsonController.java",
        "class": "RealTimeTrafficLinePropertiesDto",
    },
    "realTimeTrafficMap.json (popup)": {
        "doc": "gateway-api/map-data.md",
        "heading": "Popup",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/RealTimeTrafficMapJsonController.java",
        "class": "RealTimeTrafficPopupPropertiesDto",
    },
    "alertsMap.json": {
        "doc": "gateway-api/map-data.md",
        "heading": "Alerts",
        "java": "webapp/src/main/java/com/gcmtravel/web/json/AlertsMapJsonController.java",
        "class": "AlertProperties",
    },
}

# GeoJSON envelope keys. The documents describe the whole response, so they legitimately
# list the FeatureCollection and Feature structure around the properties object; those
# names never appear in a properties POJO and are not findings.
ENVELOPE = {
    "type", "timestamp", "features", "geometry", "geometries", "coordinates",
    "properties", "bbox",
}

# Bullets that name a JSON field: "- id — the incident ID". The docs use an em dash
# throughout; a hyphen separator is accepted too because a handful of lines use one.
FIELD_BULLET = re.compile(r"^\s*[-*]\s+`?([A-Za-z_][A-Za-z0-9_]*)`?\s*[—–-]\s+")

# Field declarations, in both styles these classes use:
#   private final String id;            -- plain POJO with @Getter
#   String id;                          -- package-private, under Lombok @Value, which
#                                          rewrites them to private final and generates
#                                          the getters Jackson serializes
# The visibility keyword is therefore optional, and its absence is meaningful rather
# than a reason to skip the line. Getting this wrong is not a harmless miss: an
# unmatched class yields an empty field list, and every documented field then looks
# like it is "documented but not serialized" -- a page of false findings that reads
# exactly like a real one.
JAVA_FIELD = re.compile(
    r"^\s*(?:(?:private|protected|public)\s+)?(?:final\s+)?"
    r"(?!static\b|return\b|new\b|this\b)"
    r"[A-Za-z_][\w.<>\[\], ]*\s+"
    r"([A-Za-z_][A-Za-z0-9_]*)\s*(?:=[^;]*)?;\s*$"
)
# Constants and statics are not wire fields.
JAVA_SKIP = re.compile(r"\bstatic\b|serialVersionUID")
# Jackson overrides on the declaration above the field.
JSON_PROPERTY = re.compile(r'@JsonProperty\(\s*"([^"]+)"')
JSON_IGNORE = re.compile(r"@JsonIgnore\b")


def doc_fields(path, heading):
    """Field names in the bullet list under the given heading, until the next heading of
    the same or higher level. Nested bullets are included -- properties are nested under
    a "properties" bullet in most sections."""
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()

    start = None
    level = 0
    for i, line in enumerate(lines):
        match = re.match(r"^(#{2,4})\s+(.*?)\s*$", line)
        if match and match.group(2) == heading:
            start = i + 1
            level = len(match.group(1))
            break
    if start is None:
        return None

    names, seen = [], set()
    in_fence = False
    in_request = False
    for line in lines[start:]:
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        stop = re.match(r"^(#{2,4})\s+(.*?)\s*$", line)
        if stop:
            if len(stop.group(1)) <= level:
                break
            # A "Request" subsection describes query and POST parameters, not response
            # fields. Reading its bullets as fields reports `bbox`, `zoom` and
            # `includeGeneralAlerts` as documented-but-not-serialized on every endpoint.
            in_request = stop.group(2).strip().lower().startswith("request")
        if in_request:
            continue
        match = FIELD_BULLET.match(line)
        if match and match.group(1) not in seen:
            seen.add(match.group(1))
            names.append(match.group(1))
    return names


def java_fields(path, class_name):
    """Instance field names declared in the named class body, found by brace matching
    from the class declaration so a nested class does not bleed into its sibling."""
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as handle:
        source = handle.read()

    decl = re.search(r"\bclass\s+" + re.escape(class_name) + r"\b", source)
    if not decl:
        return None
    open_brace = source.find("{", decl.end())
    if open_brace < 0:
        return None

    depth, end = 0, len(source)
    for i in range(open_brace, len(source)):
        if source[i] == "{":
            depth += 1
        elif source[i] == "}":
            depth -= 1
            if depth == 0:
                end = i
                break

    # Only declarations sitting directly in the class body are fields. Without this the
    # constructor's local variables (`formatter`, `imageAge`, `longTerm`) are picked up
    # and reported as undocumented wire fields, which is nonsense -- they never leave
    # the constructor. Track depth and accept a line only at depth 1.
    names, depth, rename, ignore = [], 0, None, False
    for line in source[open_brace:end].splitlines():
        at_body_level = depth == 1 or (depth == 0 and line.lstrip().startswith("{"))
        if at_body_level:
            # The Java field name is not always the wire name. SpecialEventPropertiesDto
            # declares `lastUpdated` and ships it as `lstUpd` via @JsonProperty; reading
            # the declaration alone reports the correct documentation as wrong, which is
            # the most dangerous kind of false positive this tool can produce.
            renamed = JSON_PROPERTY.search(line)
            if renamed:
                rename = renamed.group(1)
            if JSON_IGNORE.search(line):
                ignore = True
            if not JAVA_SKIP.search(line):
                match = JAVA_FIELD.match(line)
                if match:
                    if not ignore:
                        names.append(rename or match.group(1))
                    rename, ignore = None, False
        depth += line.count("{") - line.count("}")
    return names


def main():
    parser = argparse.ArgumentParser(
        description="Compare documented response fields against the serialized POJOs.")
    parser.add_argument("--gateway", required=True, help="path to a gateway checkout")
    parser.add_argument("--endpoint", help="check only this endpoint key")
    args = parser.parse_args()

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.isdir(os.path.join(args.gateway, "webapp")):
        sys.exit("%s does not look like a gateway checkout (no webapp/)" % args.gateway)

    items = sorted(MAPPING.items())
    if args.endpoint:
        items = [(k, v) for k, v in items if k == args.endpoint]
        if not items:
            sys.exit("unknown endpoint %r; known: %s"
                     % (args.endpoint, ", ".join(sorted(MAPPING))))

    unmapped, differing, agreeing = [], [], []
    for name, spec in items:
        documented = doc_fields(os.path.join(root, spec["doc"]), spec["heading"])
        actual = java_fields(os.path.join(args.gateway, spec["java"]), spec["class"])

        if documented is None:
            unmapped.append((name, "heading %r not found in %s"
                             % (spec["heading"], spec["doc"])))
            continue
        if actual is None:
            unmapped.append((name, "class %s not found in %s"
                             % (spec["class"], spec["java"])))
            continue

        missing = [f for f in actual if f not in documented]
        extra = [f for f in documented if f not in actual and f not in ENVELOPE]
        if missing or extra:
            differing.append((name, missing, extra, spec))
        else:
            agreeing.append((name, actual))

    for name, fields in agreeing:
        print("OK       %-32s %d fields" % (name, len(fields)))
    for name, missing, extra, spec in differing:
        print("\nDIFFERS  %s" % name)
        print("         %s -> %s" % (spec["doc"], spec["class"]))
        if missing:
            print("         serialized but not documented: %s" % ", ".join(missing))
        if extra:
            print("         documented but not serialized: %s" % ", ".join(extra))
    for name, why in unmapped:
        print("\nUNMAPPED %s\n         %s" % (name, why))

    print("\n%d endpoints checked: %d agree, %d differ, %d unmapped"
          % (len(items), len(agreeing), len(differing), len(unmapped)))
    print("Name-level only. Value sets, types, units and null behaviour are not checked "
          "-- see the module docstring.")

    # Differences are findings to triage, not build failures: this is a maintenance
    # tool like check_coverage.py, and several "extra" fields are legitimately
    # documented structure (geometry, type) rather than errors.
    return 1 if unmapped else 0


if __name__ == "__main__":
    sys.exit(main())
