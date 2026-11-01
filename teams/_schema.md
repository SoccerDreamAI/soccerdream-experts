# Team Schema

A team is a single YAML file in `teams/`. It names the stages, the members, and the rules
that govern how disagreement is resolved. Everything here is public and everything here
is enforced by the loader.

## Full example

```yaml
name: match-research-team
version: 1
description: Four-member research team with an enforced challenge stage.

stages:
  - context
  - specialists
  - challenge
  - review

members:
  - ref: agents/quantitative-analyst.md
  - ref: agents/market-odds-reader.md
  - ref: agents/contrarian-hunter.md
  - ref: agents/red-team-reviewer.md

rules:
  independence: strict
  disagreement: escalate
  confidence: calibrated
  max_rounds: 2

output:
  format: report
  language: auto
  include_evidence: true
```

## Fields

### Top level

| Field | Required | Type | Notes |
|:--|:--:|:--|:--|
| `name` | ✅ | string | kebab-case, unique within the repo |
| `version` | ✅ | int | bump on any behavioural change |
| `description` | — | string | ≤ 200 chars |
| `stages` | ✅ | list | see below; order matters |
| `members` | ✅ | list | 2–12 entries |
| `rules` | ✅ | map | see below |
| `output` | — | map | defaults shown below |

### `stages`

Four stage types exist. A team may repeat `challenge` but must contain `review` last.

| Stage | Purpose | Required |
|:--|:--|:--:|
| `context` | Normalize inputs into one unit and one time frame | ✅ |
| `specialists` | Each member reasons independently, in parallel | ✅ |
| `challenge` | Conflicting reads face each other; one must yield | ✅ |
| `review` | Red-team audit; may overturn the conclusion | ✅ |

```yaml
stages:
  - context
  - specialists
  - challenge
  - challenge      # allowed: second round if the first produced no yield
  - review
```

### `members`

```yaml
members:
  - ref: agents/quantitative-analyst.md
    role: specialist            # specialist | challenger | reviewer
    weight: 1.0                 # only honoured when rules.disagreement=weighted
```

| Field | Required | Default | Notes |
|:--|:--:|:--|:--|
| `ref` | ✅ | — | relative path; must resolve inside the repo |
| `role` | — | `specialist` | exactly one `reviewer` per team |
| `weight` | — | `1.0` | ignored unless disagreement mode is `weighted` |

### `rules`

#### `independence`

| Value | Behaviour |
|:--|:--|
| `strict` *(default)* | No member sees another's draft. This is the whole point. |
| `relaxed` | Members may see prior drafts. Measurably worse; offered for cheap runs only. |

#### `disagreement`

| Value | Behaviour |
|:--|:--|
| `escalate` *(default)* | Conflicts go to the challenge stage. Nothing is averaged. |
| `weighted` | Conflicts resolved by member weight. **Discouraged** — see architecture doc. |
| `majority` | Conflicts resolved by count. **Discouraged** for the same reason. |

`escalate` is the only mode that preserves the information content of a disagreement.
The other two destroy it by construction, and are supported only so that the difference
can be measured rather than asserted.

#### `confidence`

| Value | Behaviour |
|:--|:--|
| `calibrated` *(default)* | Confidence downgrades automatically when load-bearing citations are weak |
| `reported` | Members state confidence; nothing is enforced |

#### `max_rounds`

Integer, 1–4, default `2`. Total challenge rounds allowed before the team must conclude.

### `output`

| Field | Default | Notes |
|:--|:--|:--|
| `format` | `report` | `report` \| `json` |
| `language` | `auto` | `auto` \| `en` \| `zh` |
| `include_evidence` | `true` | if `false`, citations are stripped — **not recommended** |

## Validation

The loader rejects a team file when:

- a `ref` does not exist, or resolves outside the repository root
- `review` is not the last stage
- there is not exactly one member with `role: reviewer`
- any member lacks all four required persona sections
- `rules.disagreement` is `weighted`/`majority` **and** no `weight` is set on any member

Run `make lint` to validate every team file at once.

## Design notes

Two members is the minimum that can produce a disagreement. Three is where the challenge
stage starts doing real work. Beyond six, the marginal member mostly adds cost — the
first four positions cover the space; the fifth and sixth tend to restate.

If your team never produces a disagreement, that is a signal about your personas, not
about the events. Two personas with genuinely different priors should conflict on a
meaningful fraction of inputs. If they never do, one of them is not doing its job.
