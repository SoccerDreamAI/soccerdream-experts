#!/usr/bin/env python3
"""sd — the SoccerDream expert-team client.

Deliberately small and dependency-free: `python3 cli/sd.py <command>` works on a fresh
clone with nothing installed. Inference runs on the hosted service (NOTICE.md §3); nothing
in this file calls a model, and nothing in this file is missing because of that.

Commands
    validate <team.yaml>   check a team file and every persona it references
    demo                   print a recorded run of the protocol
    demo --unresolved      the same run, ending with no conclusion

Exit codes
    0  valid / completed with a conclusion
    1  completed, no conclusion reached  (a valid outcome, not an error)
    2  invalid team or persona file
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

CONTRACT = ("## Prior", "## Method", "## Evidence standard", "## Refusal")
STAGES = ("context", "specialists", "challenge", "review")
ROLES = ("specialist", "challenger", "reviewer")

# Values that quietly undo the whole design. Named so the error can explain itself.
BANNED = {
    "average": "averaging erases the only informative fact in a disagreement",
    "mean": "averaging erases the only informative fact in a disagreement",
    "vote": "a vote asks who has more support; a challenge asks who can point at evidence",
    "highest-confidence": "self-reported confidence is not evidence and is never calibrated",
}


def read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def parse_team(text):
    """Extract the four things this validator needs.

    A subset parser, not a YAML implementation. The repository ships no yaml dependency on
    purpose: a validator that needs `pip install` is a validator most visitors never run.
    If your team file uses anchors, aliases or flow mappings, validate it with PyYAML.
    """
    team = {"name": None, "stages": [], "members": [], "rules": {}, "refs": []}
    section = None
    current = None

    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        if re.match(r"^[A-Za-z_]+:", line):
            section = line.split(":", 1)[0].strip()
            if section == "name":
                team["name"] = line.split(":", 1)[1].strip() or None
            current = None
            continue

        stripped = line.strip()

        if section == "stages" and stripped.startswith("- "):
            team["stages"].append(stripped[2:].strip())
        elif section == "members":
            if stripped.startswith("- "):
                current = {}
                team["members"].append(current)
                stripped = stripped[2:].strip()
            if current is not None and ":" in stripped:
                key, _, value = stripped.partition(":")
                current[key.strip()] = value.strip()
        elif section == "rules" and ":" in stripped:
            key, _, value = stripped.partition(":")
            team["rules"][key.strip()] = value.strip()

    team["refs"] = [m.get("ref") for m in team["members"] if m.get("ref")]
    return team


def validate(path):
    errors, warnings = [], []

    if not os.path.isfile(path):
        return ["file not found: %s" % path], []

    team = parse_team(read(path))
    label = team["name"] or os.path.basename(path)

    if not team["name"]:
        errors.append("missing `name:`")
    if not team["members"]:
        errors.append("missing `members:` — a team of nobody has no disagreement to escalate")

    # stages
    if not team["stages"]:
        errors.append("missing `stages:`")
    else:
        for required in STAGES:
            if required not in team["stages"]:
                if required == "review":
                    errors.append("missing `review` stage — nothing can overturn the conclusion")
                else:
                    warnings.append("missing `%s` stage" % required)

    # rules
    rules = team["rules"]
    if "disagreement" not in rules:
        errors.append("missing `rules.disagreement` — defaults are for people who do not care")
    else:
        value = rules["disagreement"].strip().strip('"\'')
        if value in BANNED:
            errors.append(
                "rules.disagreement: %s — %s. Use `escalate`." % (value, BANNED[value]))
        elif value != "escalate":
            warnings.append("rules.disagreement: %r is not a documented value" % value)

    if rules.get("independence") != "strict":
        warnings.append(
            "rules.independence is %r — without `strict`, members read each other's drafts "
            "and you get one estimate four times" % rules.get("independence", "unset"))

    rounds = rules.get("max_rounds")
    if rounds is not None and not re.fullmatch(r"\d+", rounds.strip()):
        errors.append("rules.max_rounds: %r is not an integer" % rounds)

    # members
    roles = {}
    for i, member in enumerate(team["members"], 1):
        role = member.get("role")
        if role not in ROLES:
            errors.append("member %d: role %r is not one of %s" % (i, role, ", ".join(ROLES)))
        else:
            roles[role] = roles.get(role, 0) + 1

        ref = member.get("ref")
        if not ref:
            errors.append("member %d: missing `ref:`" % i)
            continue
        target = os.path.join(ROOT, ref)
        if not os.path.isfile(target):
            errors.append("member %d: ref not found: %s" % (i, ref))
            continue
        body = read(target)
        missing = [s for s in CONTRACT if s not in body]
        if missing:
            errors.append("%s is missing %s" % (ref, ", ".join(missing)))

    if len(team["members"]) < 2:
        errors.append("a team needs at least two members; one member cannot disagree")
    if roles.get("reviewer", 0) == 0:
        errors.append("no member has role `reviewer` — nothing can overturn the conclusion")
    if roles.get("challenger", 0) == 0:
        warnings.append("no member has role `challenger` — disagreement will have no advocate")

    return ["%s: %s" % (label, e) for e in errors], warnings


def check(path):
    errors, warnings = validate(path)
    for w in warnings:
        print("  warn  %s" % w)
    for e in errors:
        print("  FAIL  %s" % e)
    if errors:
        print("\n  %d error(s). A team that fails here will fail at runtime, later and louder."
              % len(errors))
        return 2
    print("  ok    %s" % path)
    if warnings:
        print("        %d warning(s), no errors" % len(warnings))
    return 0


def demo(unresolved=False):
    out = []
    add = out.append

    add("NOTE  Simulated run. Fixed inputs, no model calls. The reasoning engine is not")
    add("      in this repository — see NOTICE.md section 3. What this shows is the")
    add("      protocol: who is allowed to say what, and what happens when they disagree.")
    add("")

    if not unresolved:
        add("stage 1/4  context      2 sources normalized -> 1 canonical record (demo-001)")
        add("stage 2/4  specialists  A: range 1.2 - 1.8, 3 citations")
        add("                        B: range 2.1 - 2.6, 1 citation")
        add("                        -> disagree, zero overlap")
        add("stage 3/4  challenge    B challenges A: \"your window is too narrow\"")
        add("                        A cites 3 independent figures -> stands")
        add("                        B cites 1, short of 2 -> withdraws, in writing")
        add("                        (the withdrawal is the output of this round)")
        add("stage 4/4  review       load-bearing claim rests on 1 source")
        add("                        -> confidence high downgraded to medium")
        add("")
        add("conclusion              range 1.2 - 1.8, confidence medium")
        add("                        no single outcome named, by design")
        add("")
        add("exit 0")
        code = 0
    else:
        add("stage 1/4  context      2 sources normalized -> 1 canonical record (demo-001)")
        add("stage 2/4  specialists  A: range 1.2 - 1.8, 3 citations")
        add("                        B: range 2.1 - 2.6, 2 citations")
        add("                        -> disagree, zero overlap")
        add("stage 3/4  challenge    B challenges A; A cites 3 and stands")
        add("                        B cites 2 and stands")
        add("                        neither withdraws")
        add("stage 4/4  review       no side is wrong on the evidence available")
        add("                        reviewer declines to break the tie")
        add("")
        add("conclusion              unresolved")
        add("                        shipped as `unresolved`, not as a midpoint")
        add("                        a midpoint would have been a conclusion")
        add("                        nobody proposed and nobody would defend")
        add("")
        add("exit 1                  not an error. See `sd --help`.")
        code = 1

    print("\n".join(out))
    return code


def usage():
    print(__doc__.strip())
    return 0


def main(argv):
    if not argv or argv[0] in ("-h", "--help", "help"):
        return usage()

    cmd = argv[0]

    if cmd == "validate":
        if len(argv) < 2:
            print("usage: sd validate <team.yaml>", file=sys.stderr)
            return 2
        return check(argv[1])

    if cmd == "demo":
        return demo(unresolved="--unresolved" in argv[1:])

    # The hosted commands need the service, and the service needs a token. Say so plainly
    # rather than failing somewhere confusing later.
    if cmd in ("auth", "team", "run"):
        print("`sd %s` talks to the hosted service.\n\n"
              "This repository is source-available, not open source: the client contract is\n"
              "here, the inference is not. What runs offline on a fresh clone is:\n\n"
              "    python3 cli/sd.py validate teams/example-team.yaml\n"
              "    python3 cli/sd.py demo\n\n"
              "Access to the hosted run is separate — see https://soccerdreamai.com"
              % cmd, file=sys.stderr)
        return 4

    print("unknown command: %s\n" % cmd, file=sys.stderr)
    return usage()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
