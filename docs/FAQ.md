# FAQ

Short answers to the questions this repository actually receives. If yours is missing,
open a discussion.

---

### Is this open source?

No. It is **source-available** under BUSL-1.1.

You can read every persona, the orchestration schema, and the full client. You can run
them. What you may not do without a commercial licence is operate it as a commercial
product.

The licence converts to Apache-2.0 four years after release. Details in
[LICENSE](../LICENSE) and [NOTICE.md](../NOTICE.md).

### What exactly is closed?

| Layer | In this repo |
|:--|:--:|
| Persona definitions, priors, refusal rules | full |
| Orchestration schema, stages, disagreement protocol | full |
| Client (CLI + SDK) | full |
| Training prompts and their evolved wording | not included |
| Evaluation weighting and calibration internals | not included |
| Live data adapters and history store | not included |

The closed rows are *absent files*, not scrambled ones. See
[VERIFY.md](VERIFY.md) §5 for the check that demonstrates this.

### Why BUSL and not MIT?

Because the protocol is the part we want read, and the training layer is the part we
sell. MIT would license away the second part along with the first. BUSL is the narrowest
licence we found that keeps those two separate — see
[LICENSE-RATIONALE.md](LICENSE-RATIONALE.md) for the alternatives we rejected and why.

### Can I use it at work?

Internal evaluation, academic use, and personal non-commercial use are granted for
30 days without asking. After that, or for anything customer-facing, you need a
commercial licence.

When in doubt, ask first — the answer is usually yes and it takes one email.

### Why is averaging banned instead of just discouraged?

Because a weighted mean of two disagreeing analysts produces a number that **neither of
them proposed and neither would defend**. It looks like a conclusion, so it gets
downstream treatment as one.

The schema rejects `disagreement: average` at validation time, not at review time. You
can watch it happen in [VERIFY.md](VERIFY.md) §2 — one word changed, exit code 2.

The longer argument is in [docs/architecture.md](architecture.md) and in the write-up
[Why a multi-agent system must not average](https://dev.to/soccerdreamai/why-a-multi-agent-system-must-not-average-3p5d).

### What happens when the team genuinely cannot agree?

It returns `unresolved`, and the CLI exits `1`.

That is a shipped answer, not an error path. A midpoint would have been a conclusion
nobody proposed and nobody would defend — so there isn't one.

### Is this a betting product?

No. This repository contains no odds feed, no stake sizing, no selection output, and
gives no advice. It is a research framework. See [NOTICE.md](../NOTICE.md) §8.

### Why does `team run` exit with code 4?

Because inference is hosted. `team run` requires the service and a key; the repository
does not contain a model and will not pretend it does. Exit `4` says exactly that.

`demo` and `validate` run fully offline — that is the whole client contract.

### How do I add my own persona?

Write one markdown file with four sections — `Prior`, `Method`, `Evidence standard`,
`Refusal` — then reference it from a team file and validate:

```bash
python3 cli/sd.py validate teams/my-team.yaml
```

The full contract is in [agents/_schema.md](../agents/_schema.md). Personas that cannot
state what they would refuse are rejected, because a persona with no refusal rule is a
persona that will agree with anything.

### Can I fork it and publish my own version?

Yes, under BUSL terms, with three conditions from [TRADEMARK.md](../TRADEMARK.md):

1. rename it, 2. state that your fork is not official, 3. do not imply endorsement.

The name and marks are not part of the licence grant.

### Found a security issue?

Do not open a public issue. Use GitHub's private vulnerability reporting on this
repository, or see [SECURITY.md](../SECURITY.md).
