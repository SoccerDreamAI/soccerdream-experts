# Why a multi-agent system must not average

> We shipped four analysis personas, then deleted every vote and every weighted mean
> from the codebase.

## Every multi-agent framework has the same first bug

Look at how most multi-agent projects are built. Three roles read the same material, each
writes a conclusion, an orchestrator merges them into one answer.

The merge is usually a weighted mean, or a majority vote.

It seems obviously right — isn't that what ensembles do? Random forests average, voting
classifiers vote, bagging reduces variance. Same word, so the same move should apply.

The analogy is wrong, and the cost is not small.

An ensemble averages **homogeneous weak learners** with independent noise on a shared
objective. Averaging cancels the noise.

A multi-agent team is **heterogeneous judges** whose value is precisely that they disagree:
one reads the shape of a distribution, one reads whether consensus has drifted, one exists
to find the dissent nobody else produces. Average those three and you do not get a steadier
answer. You get a sentence sanded down until it has no position.

## Averaging is loudest exactly where it is most destructive

This is the part worth its own section.

**When the members agree, averaging is the identity operation. Nothing happens, nothing is
lost.**

**When the members disagree, averaging is at full strength** — because at that moment the
only informative fact in the run is *that two informed readers disagreed*.

The operation activates precisely in the case where you most need the disagreement kept.

Two members read the same record:

- A: narrow and low
- B: wide and high

The average is medium-width and centred. That shape was **proposed by nobody and would be
defended by nobody**. You manufactured a conclusion no participant believes, and destroyed
the one real signal in the run.

I call that a fabricated consensus. It is not even a compromise — a compromise at least
admits the disagreement happened.

## Independence has to be structural, not encouraged

The second trap is subtler: shared context.

As the system runs, the members' outputs start to look alike, and they converge nicely.
It reads like maturity. It is B having seen A's draft.

The moment B reads A's conclusion before reading the material, B's output stops being an
independent estimate and becomes a **revision** of A's. Two correlated estimates look like
agreement and carry the information of one.

**You paid for four members and received one.**

So each member gets the same canonical record and nothing else. No shared draft, no rolling
summary, no "here is what the others think".

The cost is real: independent members produce messier, more contradictory output. That mess
**is** the signal. It is what you paid for.

## If voting is out, escalate

Disagreement cannot be averaged, so how does a run end?

It escalates to a **challenge** stage with one rule:

> A challenge is a citation contest, not a vote.

A challenged claim has two exits:

1. cite two independent figures and stand;
2. fail to cite, and **withdraw explicitly**.

There is no third path. The withdrawal must be recorded, because the withdrawal is the
actual output of that round.

If both sides stand, neither is decided. Both are marked `unresolved`, and that marking
travels into the published result. An honest "we could not settle this" beats a fabricated
midpoint.

The distinction matters: a vote asks **who has more support**. A challenge asks **who can
point at their evidence**. The first rewards confident phrasing. The second rewards having
actually checked.

## The reviewer must be able to overturn — with mechanical checks

The final stage reads the whole transcript and **can change the conclusion**, not merely
comment on it.

Reviewers without authority produce advisory notes, and advisory notes get ignored under
deadline. That is failure mode one.

Grant authority instead and failure mode two arrives: reviewers with authority **kill good
conclusions**, especially when their check is "this feels off".

So the reviewer's checks are fixed: **five audits, fixed order, each producing a diff
against a named sentence.** No scores, no general impressions, no "consider reviewing this
further". Either show that the sentence does not support the conclusion, or pass it.

One more rule that feels wrong until you need it: **a run is allowed to end with no
conclusion**, and that outcome is published as-is. The alternative — shipping a conclusion
the reviewer could not defend — is the failure mode most analysis products actually have.

## Five failure modes we hit

The table below is the useful part of our architecture doc. The diagram is not.

| Failure | Symptom | Cause and fix |
|:--|:--|:--|
| Leaky independence | Members converge suspiciously often | Context leaked through the **runtime**, not the prompts |
| Reviewer rubber-stamp | Zero overturns over many runs | Reviewer read the draft **after** it was formatted for output |
| Persona collapse | Two "different" members write near-identical text | Both priors were restatements of "be careful, consider many factors" |
| Confidence inflation | High confidence on single-source claims | Confidence was **member-reported**, never calibrated against the citation audit |
| Challenge theatre | Disagreements resolve in one turn, always | The challenger had no evidence standard, so it always yielded first |

Four of the five were prompt problems, not code problems. Only the first was structural.

That ratio is worth remembering when you debug your own team.

## Where the line is

We run this in production. The public repository is **source-available, not open source**.

Public: the four personas, the orchestration schema, the client, and the reasoning above.

Not public: the training prompts, the evaluation weights, the live data adapters, the
settlement logic.

We say this in the first line rather than letting you install it and discover it. A
repository that looks complete and is not damages a project more than the missing code ever
would.

## If you remember one thing

It is not "use more models", and not "add a reviewer".

It is this: **when two informed judges disagree, the disagreement is the asset. Do not wash
it out with a mean.**

Any operation that smooths a disagreement deserves one question first — am I removing noise,
or destroying evidence?

---

**[github.com/SoccerDreamAI/soccerdream-experts](https://github.com/SoccerDreamAI/soccerdream-experts)**
— the four personas, the orchestration schema, and the architecture rationale behind the
table above, in English and Chinese. Source-available: read it, fork it, and keep the
attribution.

*This is an analysis framework. It does not predict outcomes, is not advice, and is not
intended for wagering.*
