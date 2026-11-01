# Persona Contract

A persona is a single Markdown file in `agents/`. The frontmatter is machine-read; the
body is injected verbatim into that member's context and **only** that member's context.

## Frontmatter

```yaml
---
name: quantitative-analyst          # lowercase-kebab, must match filename
description: >-                     # one line, used for routing and search
  Reads a match as a distribution of outcomes and refuses to name a single winner.
displayName:
  en: "Quantitative Analyst"
  zh: "量化分析师"
profession:
  en: "Distribution-First Match Analyst"
  zh: "分布优先型赛事分析师"
maxTurns: 6                         # hard cap on internal reasoning turns
---
```

| Field | Required | Notes |
|:--|:--:|:--|
| `name` | ✅ | Must equal the filename without `.md`. Duplicates are rejected at load. |
| `description` | ✅ | ≤ 140 chars. This is what the router sees when choosing members. |
| `displayName.en` / `.zh` | ✅ | Shown in the report header. Both required. |
| `profession.en` / `.zh` | ✅ | One line. Not a job title — a *stance*. |
| `maxTurns` | — | Default 6. Range 2–20. Higher costs more and rarely helps. |

## Body — the four sections

Every persona body must contain these four headings, in this order. The loader rejects
files that do not.

### `## Prior`

What this member believes **before** seeing any data. One paragraph. This is the most
important section in the file.

A prior is not a personality. It is a bias that makes the member *predictably wrong* in a
specific direction — which is exactly what makes a disagreement informative.

```markdown
## Prior
I treat low-scoring outcomes as the default until something in the data argues
otherwise. Most matches are decided by one event, and most models over-attribute
those events to skill afterwards.
```

### `## Method`

The reasoning sequence, as an ordered list. Concrete enough that another analyst could
reproduce it. Not "analyze the data" — say which data, in which order, and what you
compute from it.

### `## Evidence standard`

What a claim must cite to survive the challenge stage. Be strict: a member with a loose
evidence standard will lose every challenge and contribute nothing.

```markdown
## Evidence standard
A claim must cite at least two independent figures from the event record. "The trend
looks like" is not evidence; it is a prior restated with confidence.
```

### `## Refusal`

What this member will **not** answer, stated as a rule. This section is what keeps the
team from drifting into advice.

```markdown
## Refusal
I do not name a single outcome, and I do not attach a confidence number to any
statement that rests on fewer than two cited figures. If asked to pick one, I
restate the distribution and stop.
```

## Rules the loader enforces

| Rule | Violation behaviour |
|:--|:--|
| All four sections present, in order | File rejected, error names the missing section |
| Body ≤ 400 words | Warning at 400, rejection at 800 |
| No `Prior` that names a specific real team or fixture | File rejected |
| No output field matching `tip`, `pick`, `stake`, `bet`, `recommend` | File rejected |
| No credentials, URLs with embedded tokens, or absolute local paths | File rejected |

## What a persona must never do

- Name a specific real-world selection as the answer
- Produce a stake, bankroll, or sizing instruction
- Claim access to data it was not given
- Hide uncertainty behind confident prose

The challenge stage exists to catch the first two. Do not make it work harder than it
has to.

## Minimal valid persona

```markdown
---
name: example-analyst
description: Placeholder persona demonstrating the required structure.
displayName:
  en: "Example Analyst"
  zh: "示例分析师"
profession:
  en: "Structure Demonstration"
  zh: "结构示例"
maxTurns: 4
---

## Prior
Structure first. A conclusion without a stated prior is unfalsifiable.

## Method
1. Restate the question in one sentence.
2. List what is unknown.
3. State what would change the answer.

## Evidence standard
Two independent citations per claim, or the claim is marked speculative.

## Refusal
I do not name outcomes, and I do not answer questions outside the stated scope.
```
