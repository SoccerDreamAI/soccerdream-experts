# CLI

```
┌─────────────────────────────────────────────────────────────┐
│  This directory holds the client source for the `sd` CLI.   │
│  It is intentionally thin: parse args, validate the team    │
│  file, call the hosted API, render the report.              │
│                                                             │
│  There is no reasoning logic here, and none is missing.     │
│  Inference runs on the hosted service — see NOTICE.md §3.   │
└─────────────────────────────────────────────────────────────┘
```

## What belongs here

| ✅ Yes | ❌ No |
|:--|:--|
| Argument parsing, config resolution | Prompt construction |
| Team/persona schema validation | Model selection or routing |
| HTTP client for the hosted API | Any local inference |
| Report rendering (text, json) | Scoring or calibration logic |

If you find yourself wanting to add reasoning logic here, that is a signal the boundary
is in the wrong place — open an issue rather than a PR.

## Install

```bash
pip install soccerdream-experts     # published package
pip install -e .                    # from source
```

## Commands

```bash
sd auth login                       # device flow, token stored in OS keyring
sd auth status
sd team validate teams/example-team.yaml
sd team run teams/example-team.yaml --event demo-001
sd team run teams/example-team.yaml --event demo-001 --format json
```

`sd team validate` runs the same checks as `make lint-schema`, with better error messages.
Run it before opening a PR that touches `agents/` or `teams/`.

## Exit codes

| Code | Meaning |
|:--:|:--|
| `0` | Completed, conclusion published |
| `1` | Completed, **no conclusion reached** (unresolved disagreement — a valid outcome) |
| `2` | Invalid team or persona file |
| `3` | Authentication failed or token expired |
| `4` | Hosted API unreachable |
| `5` | Rate limited (retry after `--wait`) |

Exit code `1` is not an error. The red-team reviewer is allowed to overturn or withhold a
conclusion, and the CLI surfaces that honestly rather than dressing it up as success.
