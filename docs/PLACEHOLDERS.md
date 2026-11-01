# Placeholders — replace before publishing

Every value below must be replaced before this repo goes public. Nothing here is optional.

---

## 1. Repository identity

| Placeholder | Appears in | Replace with |
|:--|:--|:--|
| `ORG` | `README.md`, `README.zh-CN.md`, `.github/ISSUE_TEMPLATE/config.yml` | Your GitHub org or username |
| `main` | `CONTRIBUTING*.md`, `.github/workflows/ci.yml` | Your default branch (only if not `main`) |

Quick check:

```bash
grep -rn "ORG" . --exclude-dir=.git
```

## 2. Links

| Placeholder | Replace with | Notes |
|:--|:--|:--|
| `https://soccerdreamai.com` | Your live site root | Already filled in — verify it resolves |
| `https://github.com/ORG/soccerdream-experts/discussions` | Real Discussions URL | Must enable Discussions in repo settings first |
| `https://github.com/ORG/soccerdream-experts/security/advisories/new` | Real advisory URL | Must enable private vulnerability reporting |

> **Discussions must be enabled before publishing** — `config.yml` points two contact
> links at it, and a dead link in the issue chooser looks careless.

## 3. Media

| Placeholder | Path | Status |
|:--|:--|:--|
| `team-run.gif` | `docs/assets/team-run.gif` | ❌ **missing** — README renders a broken image until this exists |

The GIF is the single highest-value asset in this repo. Requirements:

- **3 seconds to comprehension.** No title card, no logo intro.
- Shows a disagreement being resolved — that is the product.
- Width 820px, under 3 MB, loops cleanly.
- No betting terminology, no currencies, no real fixture names.

If you cannot produce it, replace the `<img>` block with a static PNG. A broken image is
worse than no image.

## 4. Package names

| Placeholder | Appears in | Notes |
|:--|:--|:--|
| `pip install soccerdream-experts` | `README*.md` | Must actually exist on PyPI, or the quick start is a lie |
| `npx soccerdream-experts` | `README*.md` | Same for npm |
| `sd` | `README*.md`, `CONTRIBUTING*.md`, `Makefile` | CLI binary name |

**If the packages are not published yet**, change the quick start to a source install:

```bash
git clone https://github.com/ORG/soccerdream-experts.git
cd soccerdream-experts && pip install -e .
```

Shipping a quick start that 404s is the fastest way to lose the audience you just earned.

## 5. License

| Task | Detail |
|:--|:--|
| Replace `LICENSE` | Swap the operative summary for the canonical BUSL-1.1 text from <https://spdx.org/licenses/BUSL-1.1.html> |
| Fill in the blanks | Licensor, Licensed Work, Change Date, Change License |
| Update `NOTICE.md` §2 | Delete the "must be replaced" caveat once done |

## 6. Missing directories referenced by the README

These paths are referenced but do not exist yet. Either create them or remove the
references — do not ship dangling paths.

| Path | Referenced by | Action |
|:--|:--|:--|
| `cli/` | `README*.md` license table, `NOTICE.md` | Add source, or reword to "published on PyPI" |
| `sdk/` | same | same |
| `scripts/` | `NOTICE.md` license table | Add, or drop from the table |
| `tests/`, `examples/` | `Makefile`, `cli/example-team.yaml` refs | Add or drop |

## 7. Contact

| Where | Currently | Replace with |
|:--|:--|:--|
| `SECURITY.md` | "contact the maintainers" | A real address, or keep the advisory-only flow and remove the email mention |
| `CODE_OF_CONDUCT.md` | "the email in the repository profile" | Set that field, or point elsewhere |
| `NOTICE.md` §7 | "contact the maintainers" | Same |

---

## Final verification

Run these before flipping the repo to public. Each one catches a different class of
embarrassment.

```bash
# 1. no dangling internal links
grep -oE '\]\([^)]+\)' README.md README.zh-CN.md | grep -v 'http' | sort -u

# 2. no placeholder left
grep -rn "ORG\|TODO\|FIXME\|<short-slug>" . --exclude-dir=.git --exclude=PLACEHOLDERS.md

# 3. no credentials
make lint-secrets

# 4. bilingual sync
make lint

# 5. every referenced path exists
for p in cli sdk docs/assets/team-run.gif; do [ -e "$p" ] || echo "MISSING: $p"; done
```
