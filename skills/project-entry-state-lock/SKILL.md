---
name: project-entry-state-lock
description: Start or continue nontrivial work blocks in any governed project by reading the project entry rules, running the real project preflight/status gate, reading current state, and reporting mainline/station/branch/fixed evidence object/subagent decision. Use for continue-project turns, status-aware coding, route work, process hardening, reports, server planning, and any task that depends on project state.
---

# Project Entry State Lock

Use this skill as the first guard for any serious project. It does not replace
the project's own entry rules; it forces the correct startup sequence before
meaningful work.

## Workflow

1. Identify the project root.
2. Read the project's entry rules, usually one of:
   - `AGENTS.md`
   - `START_HERE.md`
   - `.codex/`
   - project guidance index
3. Run the project's real preflight/status gate with real task fields. If no
   preflight tool exists, explicitly record that and use the entry rules plus
   current state as the gate.
4. Stop if the gate says work is blocked.
5. Read the authoritative current state file.
6. Report:
   - project
   - mainline or objective
   - station or current phase
   - active branch or route
   - fixed evidence object, denominator, benchmark, issue id, or deployment target
   - subagent decision
   - allowed_to_continue

If the gate allows continuation but reports stale state, newer unchecked
artifacts, or registry inconsistency, do not launch science, server, release,
claim, or destructive work. First close, classify, or explicitly mark the newer
artifact as draft-only, then rerun the gate.

## Short Gate

```text
task:
why now:
task type:
current state:
active branch or route:
fixed evidence object:
subagent decision:
new experiment or risky action:
claim allowed:
failure attribution needed:
strategy bypass check:
expected artifact:
finalize needed:
```

For non-research projects, replace `fixed evidence object` with the stable
object being tested, such as a test suite, benchmark, issue id, release target,
deployment target, or customer-reported bug.

## Forbidden

- Do not treat a preflight call without real task fields as valid startup.
- Do not continue blocked work by relying on chat memory.
- Do not make route, denominator, prediction, GT, metric, release, or paper
  decisions from this skill alone.
- Do not repair state unless the task explicitly allows status or process
  repair.
