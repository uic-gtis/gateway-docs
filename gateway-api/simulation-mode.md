# Simulation Mode

## About

Testing hosts can be switched from live data feeds to a recorded or fabricated set, so that a scenario
can be replayed on demand. A host serving fabricated data looks exactly like one serving real data, which
is a correctness problem rather than a cosmetic one: a host mistaken for real-time is one an operator may
begin hand-editing.

The `simulationMode.json` file reports whether the host answering the request is serving real or simulated
data, so that a page can say so and an automated test can decline to run against the wrong kind of host.

Production hosts answer `real-time` or `unknown`.

## simulationMode.json

### Request

```console
https://travelmidwest.com/lmiga/simulationMode.json
```

No parameters. The answer describes the host that serves the request, so it must be requested from the
host being asked about.

> [!IMPORTANT]
> Request the path under `/lmiga/`, and decide what a host is serving by reading the `mode` field — never
> by the status code alone. A request to `/simulationMode.json` at the root is answered by the website
> itself with `200` and an HTML body, so a check that tests only for `200` will appear to succeed against a
> host that has no such endpoint.

### Response

A single object with the following attributes:

- mode — a string: `real-time`, `simulated`, or `unknown`
- generation — a string identifying the environment as of its last verified mode change, or `null` if the
  host has never been switched
- state — a string describing the switching mechanism itself: `ready`, `switching`, `error`, or `null`
  where no such mechanism is installed
- asOf — an ISO 8601 UTC timestamp of when the host read its own mode

`mode` is never guessed. A host that has never been switched, a host part-way through a switch, and a host
whose switch failed all report `unknown`, and `unknown` is a normal answer rather than a fault. Use `state`
to tell those cases apart: a fresh host reports `ready`, a failed switch reports `error`.

`generation` changes on every verified mode change, so a long-running test can record it at the start,
compare at the end, and discard a result that spans a change rather than reporting a mixture.

### Example

A host serving simulated data:

```json
{
  "mode": "simulated",
  "generation": "20260910T130230Z-a1b2c3d4",
  "state": "ready",
  "asOf": "2026-09-10T18:14:43Z"
}
```

A host with no switching mechanism installed, which is the ordinary production answer:

```json
{
  "mode": "unknown",
  "generation": null,
  "state": null,
  "asOf": "2026-09-10T18:14:43Z"
}
```
