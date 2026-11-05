# Verify this repository in two minutes

Every expected output below was produced by running the command against this exact commit,
before the commit was made. Nothing here is aspirational.

No account, no network, no install. Python 3.8+ and nothing else.

If a check fails on a fresh clone, that is a bug — open an issue.

---

## 0. Fresh clone

```bash
git clone https://github.com/SoccerDreamAI/soccerdream-experts
cd soccerdream-experts
python3 --version   # 3.8 or newer
```

---

## 1. The client has zero dependencies

```bash
grep -E "^(import|from) " cli/sd.py
```

Expected: exactly three lines, all standard library.

```
import os
import re
import sys
```

It never opens a socket:

```bash
grep -niE "requests|urllib|socket|httpx|openai|anthropic" cli/sd.py
```

Expected: **no output**. The file is 267 lines and contains no network code.

---

## 2. Disagreement is escalated, not averaged

```bash
python3 cli/sd.py demo; echo "exit=$?"
```

Expected `exit=0`. The stage worth reading is 3:

```
stage 3/4  challenge    B challenges A: "your window is too narrow"
                        A cites 3 independent figures -> stands
                        B cites 1, short of 2 -> withdraws, in writing
                        (the withdrawal is the output of this round)
```

B is not blended into A. B loses the exchange and says so in writing.

Now confirm the tooling **refuses** the alternative. Change one word:

```bash
cp teams/example-team.yaml my-team.yaml
python3 -c "import pathlib;p=pathlib.Path('my-team.yaml');p.write_text(p.read_text().replace('disagreement: escalate','disagreement: average'))"
python3 cli/sd.py validate my-team.yaml; echo "exit=$?"
```

Expected `exit=2`:

```
  FAIL  match-research-team: rules.disagreement: average - averaging erases
        the only informative fact in a disagreement. Use `escalate`.

  1 error(s). A team that fails here will fail at runtime, later and louder.
```

This is the whole argument of the repository, expressed as a failing check rather
than a paragraph. If your own team file says `average`, the tool will not run it.

---

## 3. "No conclusion" is a valid outcome

```bash
python3 cli/sd.py demo --unresolved; echo "exit=$?"
```

Expected `exit=1`, and the last block reads:

```
conclusion              unresolved
                        shipped as `unresolved`, not as a midpoint
                        a midpoint would have been a conclusion
                        nobody proposed and nobody would defend

exit 1                  not an error. See `sd --help`.
```

`exit=1` means "ran to completion and declined to answer". It is deliberately
distinct from `2`, which means "your file is broken".

---

## 4. Exit codes are a contract, not incidental

| Code | Meaning | Reproduce with |
|:--:|:--|:--|
| `0` | completed, conclusion reached | `cli/sd.py demo` |
| `1` | completed, **no conclusion** — valid, not a failure | `cli/sd.py demo --unresolved` |
| `2` | team file invalid; details on stderr | `cli/sd.py validate tests/fixtures/bad-team.yaml` |
| `4` | needs the hosted service | `cli/sd.py team run teams/example-team.yaml` |

Verify all four in one pass:

```bash
for c in "demo" "demo --unresolved" "validate teams/example-team.yaml" "team run teams/example-team.yaml"; do
  python3 cli/sd.py $c >/dev/null 2>&1; echo "$c -> $?"
done
```

Expected, in order: `0`, `1`, `0`, `4`.

---

## 5. The closed layers are absent, not obfuscated

```bash
grep -rniE "hit_rate|training_prompt|calibration_weight" --include="*.py" --include="*.md" --exclude=VERIFY.md .
```

Expected: **no output**. (`--exclude=VERIFY.md` only stops this file from matching
its own example — it does not exclude any real source file.) There is no training layer in this repository to reverse
engineer, because none was shipped. The closed layers are missing files, not
scrambled ones.

---

## What you cannot verify here

Three things, stated plainly rather than buried:

- **Whether the team is right.** Inference runs on the hosted service. This repo
  ships the protocol, not the model.
- **Whether the training prompts work.** They are not in this repository, by
  design — see [NOTICE.md](../NOTICE.md) §3.
- **Whether it beats a single model.** This repository publishes no accuracy
  claim, so there is nothing to verify — and nothing here that could mislead you.

A repository that lets you check its small claims is worth more than one that asks
you to trust its large ones.

---

## If something above does not reproduce

Open an issue with your OS and Python version. A false claim in this file is treated
as a defect, not as marketing drift.
