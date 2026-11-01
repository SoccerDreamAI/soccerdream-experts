# Contributing

[English](#) · [简体中文](CONTRIBUTING.zh-CN.md)

Thanks for wanting to improve this. Two minutes here will save us a review cycle.

## The fastest way to contribute: a persona

Personas (`agents/*.md`) are the highest-leverage contribution and the easiest to review.
A good persona is **narrow** and **disagreeable** — it should have a prior that makes it
wrong sometimes, and a refusal rule that keeps it in its lane.

Read [`agents/_schema.md`](agents/_schema.md) for the contract. Then copy an existing
persona and change one thing.

### What makes a persona get merged

| ✅ Merged | ❌ Sent back |
|:--|:--|
| A specific domain and an explicit prior | "A smart analyst who is good at everything" |
| States what evidence would change its mind | Restates the obvious |
| Has a refusal rule (what it will *not* answer) | Answers everything confidently |
| Cites the reasoning pattern, not the conclusion | Bakes in a fixed conclusion |
| Under 400 words | 2,000 words of vibes |

## What we will not merge

- Any persona that produces a **betting tip, stake size, or "recommended pick"**. This
  project is an analysis framework; keep it that way.
- Any change that **averages conflicting reads**. Disagreement is escalated, never blended.
- Real match data, real odds snapshots, or anything scraped from a live feed.
- Hard-coded credentials of any kind. See [SECURITY.md](SECURITY.md).
- Dependencies added for convenience. Justify every one in the PR description.

## Workflow

```bash
# 1. fork, then clone your fork
git clone git@github.com:<you>/soccerdream-experts.git
cd soccerdream-experts

# 2. branch — never work on main
git checkout -b persona/add-injury-context-reader

# 3. make your change, then validate locally
make lint          # schema + markdown + secret scan
make test          # unit tests

# 4. commit — see format below
git commit -m "feat(agents): add injury-context reader persona"

# 5. push and open a PR against main
git push origin persona/add-injury-context-reader
```

`make lint` and `make test` are the same commands CI runs. If they pass locally, CI
should pass. If CI fails and you cannot reproduce it, say so in the PR — we will look.

## Branch naming

```
persona/<short-slug>      new or changed persona
team/<short-slug>         new or changed team config
fix/<short-slug>          bug fix
docs/<short-slug>         documentation only
chore/<short-slug>        tooling, CI, deps
```

## Commit format

We use Conventional Commits. Subject line in imperative mood, under 72 characters,
no trailing period.

```
<type>(<scope>): <subject>

[optional body — explain *why*, not *what*; the diff shows what]

[optional footer — Refs #123, BREAKING CHANGE: ...]
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`.
Scopes: `agents`, `teams`, `cli`, `sdk`, `docs`, `ci`.

Good:

```
feat(agents): add injury-context reader persona

Existing personas weight recent form but ignore confirmed absences. This one
takes the team sheet first and refuses to comment when a lineup is unconfirmed.
```

Bad:

```
updated stuff
```

## Pull request

Fill in every section of the template. A PR that says only "fix" will be closed with a
link back here. If your PR closes an issue, add `Closes #123` on its own line.

Expect one of three outcomes within a week: **merge**, **changes requested** (with
specifics), or **decline** (with a reason). We do not leave PRs silently open — if a
week passes with no response, ping the thread.

## Language

- Code, comments, commit messages, and persona bodies: **English**.
- Docs may be submitted in either language; we maintain `*.zh-CN.md` mirrors ourselves.
- PR discussions: either. We will reply in the language you used.

## Code of conduct

Be direct about the work and generous about the person. Disagreement about a design is
welcome; dismissiveness is not. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
