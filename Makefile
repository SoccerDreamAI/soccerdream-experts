# Local commands — identical to what CI runs.
# If these pass locally, CI should pass. If they do not, fix that first.

SHELL := /bin/bash
PERSONA_DIR := agents
TEAM_DIR := teams

.DEFAULT_GOAL := help

.PHONY: help lint lint-schema lint-secrets lint-length test clean

help:
	@echo "make lint          run all checks (schema + secrets + length)"
	@echo "make test          run unit tests"
	@echo "make lint-schema   validate persona and team files"
	@echo "make lint-secrets  scan for credentials"
	@echo "make lint-length   check persona word counts"

## Full lint gate
lint: lint-schema lint-secrets lint-length
	@echo "✓ lint passed"

## Every persona must have the four required sections, in order.
## Every team file must have the four required stages with review last.
lint-schema:
	@echo "→ validating personas"
	@fail=0; \
	for f in $(PERSONA_DIR)/*.md; do \
	  case "$$f" in */_schema.md) continue ;; esac; \
	  for s in "## Prior" "## Method" "## Evidence standard" "## Refusal"; do \
	    grep -qF "$$s" "$$f" || { echo "  ✗ $$f missing: $$s"; fail=1; }; \
	  done; \
	done; \
	for f in $(TEAM_DIR)/*.yaml; do \
	  grep -qE '^name:' "$$f" || { echo "  ✗ $$f missing: name"; fail=1; }; \
	  grep -qE '^\s*- review' "$$f" || { echo "  ✗ $$f missing: review stage"; fail=1; }; \
	done; \
	if [ $$fail -eq 0 ]; then echo "  ✓ schema ok"; else echo "  ✗ schema failed"; exit 1; fi

## No credentials, ever. This is the check that closes a PR fastest.
## Only real key *shapes* are matched — bare prefixes like "sk-live-" appear in our own
## docs as counter-examples, and matching those would make CI permanently red.
lint-secrets:
	@echo "→ scanning for credentials"
	@excl="--exclude-dir=.git --exclude=Makefile --exclude=personalize.sh"; \
	hits=0; \
	for pat in 'sk-live-[A-Za-z0-9]{10,}' 'sk-[A-Za-z0-9]{24,}' \
	           'ghp_[A-Za-z0-9]{20,}' 'AKIA[0-9A-Z]{16}' \
	           '-----BEGIN [A-Z ]*PRIVATE KEY-----' ; do \
	  found=$$(grep -rIlE $$excl "$$pat" . 2>/dev/null); \
	  if [ -n "$$found" ]; then \
	    echo "  ✗ possible secret matched: $$pat"; echo "$$found" | sed 's/^/      /'; hits=1; \
	  fi; \
	done; \
	if find . -path ./.git -prune -o \( -name '.env' -o -name '.env.*' -o -name '*.pem' -o -name '*.key' \) -print 2>/dev/null | grep -q .; then \
	  echo "  ✗ credential-shaped file present"; hits=1; \
	fi; \
	if [ $$hits -eq 0 ]; then echo "  ✓ no credentials found"; else exit 1; fi

## Personas over 400 words are usually restating themselves.
##
## Counts the body only, i.e. everything after the closing `---` of the front
## matter. The earlier version used `sed '1,/^---$$/d;1,/^---$$/d'`, which looks
## right and is not: after the first deletion the remaining text contains no
## `---`, so the second range runs to EOF and deletes the file. It reported 0
## words for every persona and therefore never failed — a check that cannot fail
## is worse than no check. Hence the explicit "no body" guard below.
lint-length:
	@echo "→ checking persona length"
	@fail=0; \
	for f in $(PERSONA_DIR)/*.md; do \
	  case "$$f" in */_schema.md) continue ;; esac; \
	  body=$$(awk 'BEGIN{d=0} /^---[[:space:]]*$$/{d++; next} d>=2' "$$f" | wc -w); \
	  if [ "$$body" -eq 0 ]; then \
	    echo "  ✗ $$f: no body found after front matter (parser broken?)"; fail=1; \
	  elif [ "$$body" -gt 800 ]; then \
	    echo "  ✗ $$f is $$body words (hard limit 800)"; fail=1; \
	  elif [ "$$body" -gt 400 ]; then \
	    echo "  ! $$f is $$body words (soft limit 400)"; \
	  fi; \
	done; \
	if [ $$fail -eq 0 ]; then echo "  ✓ length ok"; else exit 1; fi

test:
	@echo "→ running tests"
	@python3 cli/sd.py validate teams/example-team.yaml
	@python3 cli/sd.py demo > /dev/null && echo "  ✓ demo exits 0"
	@python3 cli/sd.py demo --unresolved > /dev/null; \
	  test $$? -eq 1 && echo "  ✓ demo --unresolved exits 1, as documented"
	@python3 cli/sd.py team run teams/example-team.yaml > /dev/null 2>&1; \
	  test $$? -eq 4 && echo "  ✓ hosted-only command exits 4 instead of failing obscurely"
	@python3 cli/sd.py validate tests/fixtures/bad-team.yaml > /dev/null 2>&1; \
	  test $$? -eq 2 && echo "  ✓ a team that averages disagreement is rejected with exit 2"
	@if ls tests/test_*.py >/dev/null 2>&1; then python -m pytest -q tests || exit 1; fi
	@echo "✓ tests passed"

clean:
	@find . -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
	@find . -name '*.pyc' -delete 2>/dev/null || true
	@echo "✓ cleaned"
