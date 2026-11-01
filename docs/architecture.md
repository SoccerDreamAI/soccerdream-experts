# Architecture

[English](#) · [简体中文](zh-CN/architecture.md)

## The shape

```
                 ┌──────────────┐
   event  ──────▶│   context    │  normalize units, time frame, source priority
                 └──────┬───────┘
                        │  one canonical record
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
  ┌──────────┐   ┌──────────┐   ┌──────────┐
  │ member A │   │ member B │   │ member C │   ← independent, no shared context
  └────┬─────┘   └────┬─────┘   └────┬─────┘
       └──────────────┼──────────────┘
                      ▼
              ┌───────────────┐
              │  agreement?   │
              └───┬───────┬───┘
             yes  │       │  no
                  │       ▼
                  │  ┌──────────────┐
                  │  │  challenge   │  conflicting claims face each other
                  │  │  (1..n)      │  one must yield, or both are marked unresolved
                  │  └──────┬───────┘
                  ▼         ▼
              ┌───────────────┐
              │    review     │  adversarial audit, may overturn
              └───────┬───────┘
                      ▼
              conclusion + confidence + cited evidence
```

## Why independence is strict

Every member receives the same canonical record and nothing else. No shared draft, no
running summary, no "here is what the others think".

This is not a stylistic preference. The moment member B sees member A's draft, B's output
stops being an independent estimate and becomes a *revision* of A's. Two correlated
estimates look like agreement and carry the information of one. You have paid for four
members and received one.

The cost is real: independent members produce messier, more contradictory output. That
mess **is** the signal.

## Why averaging is banned

The obvious way to resolve four conflicting reads is to average them. It is also the way
that guarantees you learn nothing.

Consider two members: one says the distribution is narrow and low, the other says it is
wide and high. The average is a medium-width distribution centred in the middle — a shape
**neither member proposed, and neither member would defend**. You have manufactured a
conclusion that no participant believes, and you have destroyed the one genuinely
informative fact in the run: that two informed readers disagreed sharply.

Averaging also fails asymmetrically. When members agree, averaging is a no-op and costs
nothing. When they disagree, averaging is at its most destructive. So the operation only
activates in exactly the case where you most need the disagreement preserved.

Escalation instead asks a question averaging cannot: **which claim can point at its
evidence?** The challenge stage is a citation contest, not a vote. A claim survives
because it cites two independent figures; it fails because it cites a vibe. The losing
member must yield explicitly, and the yield is recorded.

If neither side yields, both claims are marked `unresolved` and the conclusion carries
that marking into publication. An honest "we could not settle this" is more useful than a
fabricated midpoint.

## Why the reviewer can overturn

The review stage is the only member that reads the assembled draft, and it has authority
to overturn the conclusion rather than merely comment on it.

Reviewers without authority produce advisory notes that get ignored under deadline.
Reviewers with authority produce a different failure mode — they can kill good conclusions
— which is why the reviewer's checks are **mechanical and ordered**, not judgement-based.
Five fixed audits, run in sequence, each producing a diff against a named sentence.

A run is allowed to end with **no conclusion**. That outcome is published as-is. The
alternative — shipping a conclusion the reviewer could not defend — is worse than an
admission of uncertainty, and it is the failure mode that most analysis products have.

## What is not in this repository

The training layer, the evaluation weights, and the live data adapters run on the hosted
service. This repository contains everything needed to understand the *shape* of a run and
to build your own team against it. It does not contain the calibration that makes the
hosted version's confidence numbers meaningful.

We state this plainly because the alternative — publishing a repo that looks complete and
is not — damages the project more than the missing code ever would.

## Failure modes we have hit

Recorded here because they are the useful part of any architecture document.

| Failure | Symptom | Fix |
|:--|:--|:--|
| Leaky independence | Members converge suspiciously often | Shared context was threaded through the runtime, not the prompts |
| Reviewer rubber-stamp | Zero overturns across many runs | Reviewer was reading the draft after the conclusion was formatted for output |
| Persona collapse | Two "different" members produce near-identical text | Priors were both restatements of "be careful and consider multiple factors" |
| Confidence inflation | High confidence on single-source claims | Confidence was member-reported, not calibrated against the citation audit |
| Challenge theatre | Disagreements resolved in one turn, always | The challenger had no evidence standard, so it always yielded first |

Four of those five were prompt problems, not code problems. Only the first was structural.
That ratio is worth remembering when you debug your own team.
