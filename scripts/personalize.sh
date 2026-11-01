#!/usr/bin/env bash
# One-shot personalisation: replace every placeholder, then verify.
#
#   ./scripts/personalize.sh <github-org> <repo-name> [site-domain]
#
# Example:
#   ./scripts/personalize.sh soccerdream soccerdream-experts soccerdreamai.com
#
# Safe to re-run. Idempotent. Refuses to run if a required argument is missing.
set -euo pipefail

ORG="${1:-}"
REPO="${2:-}"
DOMAIN="${3:-}"

if [[ -z "$ORG" || -z "$REPO" ]]; then
  cat >&2 <<'EOF'
usage: ./scripts/personalize.sh <github-org> <repo-name> [site-domain]

  <github-org>   your GitHub username or organisation, e.g. soccerdream
  <repo-name>    repository slug, e.g. soccerdream-experts
  [site-domain]  optional; rewrites soccerdreamai.com links if you use another domain
EOF
  exit 2
fi

cd "$(dirname "$0")/.."

echo "→ org=$ORG  repo=$REPO  domain=${DOMAIN:-<unchanged>}"

# --- 1. rewrite placeholders -------------------------------------------------
# Files are explicit rather than a blanket find, so that PLACEHOLDERS.md (which
# documents the placeholders) is never rewritten.
FILES=(
  README.md
  README.zh-CN.md
  CONTRIBUTING.md
  CONTRIBUTING.zh-CN.md
  SECURITY.md
  CODE_OF_CONDUCT.md
  NOTICE.md
  CLA.md
  CITATION.cff
  LAUNCH-CHECKLIST.md
  .github/ISSUE_TEMPLATE/config.yml
  .github/workflows/ci.yml
  .github/PULL_REQUEST_TEMPLATE.md
)

for f in "${FILES[@]}"; do
  [[ -f "$f" ]] || continue
  # ORG/soccerdream-experts  ->  <org>/<repo>
  sed -i "s|ORG/soccerdream-experts|${ORG}/${REPO}|g" "$f"
  # remaining bare ORG tokens
  sed -i "s|ORG/${REPO}|${ORG}/${REPO}|g" "$f"
  sed -i "s|\bORG\b|${ORG}|g" "$f"
done

if [[ -n "$DOMAIN" && "$DOMAIN" != "soccerdreamai.com" ]]; then
  for f in "${FILES[@]}"; do
    [[ -f "$f" ]] || continue
    sed -i "s|soccerdreamai\.com|${DOMAIN}|g" "$f"
  done
fi

echo "✓ placeholders rewritten"

# --- 2. verify nothing dangling ---------------------------------------------
echo "→ verifying"
fail=0

# Only a bare ORG token is a real leftover. The `<short-slug>` and `<short description>`
# strings are deliberate placeholders in issue templates and branch-naming docs — they are
# instructions for contributors, not something to substitute.
leftover=$(grep -rn --exclude-dir=.git --exclude=PLACEHOLDERS.md --exclude=personalize.sh \
            -E '\bORG\b' . 2>/dev/null || true)
if [[ -n "$leftover" ]]; then
  echo "  ✗ bare ORG token remains:"; echo "$leftover" | head -20; fail=1
else
  echo "  ✓ no placeholders left"
fi

if [[ ! -f docs/assets/team-run.gif ]]; then
  echo "  ✗ docs/assets/team-run.gif missing — README hero will 404"
  echo "    regenerate with: python scripts/make-hero-gif.py"
  fail=1
else
  echo "  ✓ hero gif present ($(du -h docs/assets/team-run.gif | cut -f1))"
fi

if grep -q "Operative Summary" LICENSE 2>/dev/null; then
  echo "  ! LICENSE is still the summary — replace with canonical BUSL-1.1 before publishing"
  echo "    https://spdx.org/licenses/BUSL-1.1.html"
fi

# secret scan (same shapes as make lint-secrets; excludes this script and the Makefile
# so the patterns do not match their own definitions)
for pat in 'sk-live-[A-Za-z0-9]{10,}' 'sk-[A-Za-z0-9]{24,}' 'ghp_[A-Za-z0-9]{20,}' 'AKIA[0-9A-Z]{16}'; do
  if grep -rIlE --exclude-dir=.git --exclude=Makefile --exclude=personalize.sh "$pat" . >/dev/null 2>&1; then
    echo "  ✗ possible secret: $pat"; fail=1
  fi
done
[[ $fail -eq 0 ]] && echo "  ✓ no credentials"

# bilingual link integrity — compare the exact relative form GitHub expects,
# not the full path (a full-path match passes on the file's own name and proves nothing)
check_pair() {
  local en="$1" zh="$2" want_en="$3" want_zh="$4"
  if [[ ! -f "$en" || ! -f "$zh" ]]; then
    echo "  ✗ missing bilingual pair: $en / $zh"; fail=1; return
  fi
  grep -qF "$want_en" "$en" || { echo "  ✗ $en does not link to $want_en"; fail=1; }
  grep -qF "$want_zh" "$zh" || { echo "  ✗ $zh does not link back to $want_zh"; fail=1; }
}
check_pair README.md           README.zh-CN.md           README.zh-CN.md           README.md
check_pair CONTRIBUTING.md     CONTRIBUTING.zh-CN.md     CONTRIBUTING.zh-CN.md     CONTRIBUTING.md
check_pair docs/architecture.md docs/zh-CN/architecture.md zh-CN/architecture.md   ../architecture.md
[[ $fail -eq 0 ]] && echo "  ✓ bilingual links intact"

echo
if [[ $fail -ne 0 ]]; then
  echo "✗ completed with problems — fix the items above before pushing" >&2
  exit 1
fi

# --- 3. print the exact push commands ---------------------------------------
cat <<EOF

✓ ready to publish

  git init -b main
  git add -A
  git -c user.name="$ORG" -c user.email="you@example.com" \\
      commit -m "chore: initial public release v0.1.0"

  # create the empty repo on GitHub first, then:
  git remote add origin git@github.com:${ORG}/${REPO}.git
  git push -u origin main

Then, in repository settings:
  - About + 20 topics      -> LAUNCH-CHECKLIST.md
  - Discussions ON         -> categories: Announcements / Q&A / Show your team / Ideas
  - Private advisory ON    -> SECURITY.md links here
  - Social preview 1280x600
  - Wiki OFF

Note: replace the placeholder email above with a real one, or commits will carry a
bogus author. Your email becomes public in every commit — use a noreply address if
you would rather it did not.
EOF
