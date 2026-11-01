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

There is nothing to install. `cli/sd.py` uses the standard library only — no `requirements.txt`,
no build step, no virtualenv:

```bash
git clone https://github.com/SoccerDreamAI/soccerdream-experts
cd soccerdream-experts
python3 cli/sd.py --help
```

There is no published `pip` or `npm` package. This file used to tell you to run
`pip install soccerdream-experts`, which resolved to nothing; a quickstart that 404s costs more
trust than a quickstart that does not exist. If a package is published later, this paragraph is
where it will be announced.

Optional, if you would rather type `sd` than `python3 cli/sd.py`:

```bash
alias sd='python3 /path/to/soccerdream-experts/cli/sd.py'
```

## Commands

```bash
python3 cli/sd.py demo                        # recorded run of the protocol
python3 cli/sd.py demo --unresolved           # ... ending with no conclusion
python3 cli/sd.py validate teams/example-team.yaml
```

`validate` runs the same contract checks as `make lint-schema`, with better error messages, and
it also verifies that every `ref:` in the team file exists and carries all four sections. Run it
before opening a PR that touches `agents/` or `teams/`.

Anything that needs the hosted service is a stub here and says so:

```bash
python3 cli/sd.py team run ...     # exits 4 with an explanation, never a silent failure
```

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
