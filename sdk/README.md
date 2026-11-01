# SDK

The programmatic surface: load a team, validate it, run it, read the report as data.

```
┌──────────────────────────────────────────────────────────────┐
│  Same boundary as cli/: parsing, validation, transport.      │
│  No prompt construction, no scoring, no local inference.     │
│  Inference runs on the hosted service — NOTICE.md §3.        │
└──────────────────────────────────────────────────────────────┘
```

## What belongs here

| ✅ Yes | ❌ No |
|:--|:--|
| `load_team(path)`, `validate(team)` | Prompt assembly |
| Typed models for the run report | Calibration or scoring |
| Retry, backoff, pagination | Model selection |
| Error types that map to exit codes | Any local inference |

## Shape

```python
from soccerexperts import Team, run

team = Team.load("teams/example-team.yaml")
team.validate()                      # raises TeamSchemaError with a file:line pointer

result = run(team, event="demo-001")

result.conclusion                    # None when the team could not settle
result.confidence                    # "high" | "medium" | "low" | "unresolved"
result.stages[2].withdrew            # the claim that yielded, and why
result.citations                     # every cited figure, with its source id
```

`result.conclusion is None` is a **successful run**, not a failure. The review stage is
allowed to overturn or withhold a conclusion; the SDK surfaces that as `None` rather than
inventing an empty answer. Treat it as a first-class case in your integration — code that
assumes a conclusion exists will crash on exactly the runs that are most interesting.

## Why the report is structured, not prose

Prose is for humans reading a page. An SDK consumer needs to diff two runs, count how often
a member yields, and check whether a cited figure actually exists in the input. That
requires fields, ids, and stable ordering — so the report is data, and rendering to text is
the CLI's job.

## Not in scope

- Streaming token output. The team's value is the resolved disagreement, not the tokens.
- Caching. Hosted-side concern; a client cache would hide the disagreement structure.
- Local evaluation of team quality. That requires the closed layers — see NOTICE.md §4.
