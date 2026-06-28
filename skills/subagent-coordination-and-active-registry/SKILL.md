---
name: subagent-coordination-and-active-registry
description: Coordinate bounded support subagents and active-subagent registry hygiene. Use when delegating engineering, docs, audits, transfer prep, environment checks, registry sync, report drafting, or process hardening while keeping route decisions, metric interpretation, evidence selection, release claims, and paper claims on the main agent.
---

# Subagent Coordination And Active Registry

Use this skill to keep delegated work scoped, observable, and closed.

## Startup

State:

```text
parallel side-task scan:
subagent decision: launch_now | already_active | none_with_reason
reason:
main-agent-owned decisions:
support tasks allowed:
registry path or status mechanism:
```

If no subagent is used, provide a concrete `none_with_reason`.

## Assignment Rules

Good subagent tasks:

```text
environment audit
file inventory
transfer preparation
docs/readout draft
registry synchronization
small script implementation
test/log triage
process hardening
```

Main agent keeps:

```text
route decisions
metric interpretation
fixed evidence object selection
ground-truth or label policy
prediction/result claims
release or paper claims
state progression
```

## Registry Hygiene

Track:

```text
subagent id:
task:
scope:
forbidden decisions:
start time:
status:
final artifacts:
closure summary:
remaining risk:
```

Mark support output draft-only until checked or finalized by the main workflow.

## Forbidden

- Do not use subagent status as performance or release evidence.
- Do not mark a support task complete without final artifacts when the project
  requires them.
- Do not delegate claims, evidence-object selection, or route pass/hold/stop.
