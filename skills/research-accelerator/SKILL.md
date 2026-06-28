---
name: research-accelerator
description: Coordinate long-running research or evidence-driven project acceleration without route drift. Use when Codex is asked to continue, accelerate, plan, execute, or report a governed research project; open or scale experiment gates; coordinate subagents; prepare server/nightly jobs; handle fixed-evidence metrics; attribute failures; update status/readouts; or finalize checked results.
---

# Research Accelerator

Use this skill as a top-level orchestrator for a governed research project. It
does not replace the project's own entry rules; it forces state lock, route
gate, subagent split, execution packaging, failure attribution, and checked
closure.

## Core Rule

Keep the main agent on research judgment. Move bounded engineering, transfer,
runtime, status, registry, docs, and finalization tasks into support lanes when
that speeds execution without weakening evidence discipline.

Do not trade speed for:

```text
fixed evidence object discipline
artifact identity
output isolation
route consistency
failure attribution
checked finalization
claim boundaries
```

## Startup

1. Read project entry rules.
2. Run the real preflight/status gate with task type, risky-action flag,
   subagent decision, and action summary when available.
3. Stop if the gate blocks work.
4. State:

```text
project:
mainline / objective:
station / phase:
active route:
fixed evidence object / benchmark:
parallel side-task scan:
subagent decision:
allowed_to_continue:
```

## Companion Skill Routing

Load the smallest relevant set:

```text
project-entry-state-lock:
  all status-aware continuation

research-route-gate:
  route design, pass/hold/stop, scale, switch

experiment-launch-denominator-gate:
  experiment, rerun, training, evaluation, benchmark launch

reusable-material-index:
  lookup before rebuilding or reusing artifacts

failure-attribution-strategy-bypass:
  failed, suspicious, old-route-like, or blocked work

runtime-capability-inventory:
  local/server/model/dependency/runtime choice

long-job-nightly-planning:
  heavy, background, server, training, materialization, audit jobs

engineering-transfer-guardrail or server-transfer-runtime-ops:
  transfer, remote execution, runner wrapper, queue, status issues

subagent-coordination-and-active-registry:
  bounded support work

route-readout-card-authoring:
  route cards, diagnostics, readouts

checked-result-finalizer and status-artifact-registry-sync:
  closure, registry, decision ledger, reusable artifact sync

paper-claim-writing:
  manuscript/report language from checked evidence only
```

## Four-Lane Execution

```text
Lane 1 - main research judgment:
  objective, evidence object, interpretation, pass/hold/stop, route switch,
  claim boundary.

Lane 2 - support work:
  scripts, audits, runtime probes, transfer prep, registry sync, report drafts.

Lane 3 - evidence ladder:
  smoke -> fixed small subset -> larger frozen subset -> official/full set.

Lane 4 - long/server jobs:
  isolated output root, expected artifacts, status source, fallback,
  finalization command.
```

Use larger coherent work blocks when local, bounded, and allowed: plan,
implement/run, readout, register/finalize, then report.

## Experiment Gate

Before launch:

```text
route objective:
old-route resemblance:
mechanism difference:
fixed evidence object:
reusable material query:
output root:
expected artifacts:
metric or evaluation:
pass:
hold:
stop:
scale-up condition:
forbidden next retry:
finalize needed:
```

## Failure And Bypass

When a result is weak, suspicious, or blocked:

```text
failure_layer:
root_cause:
evidence:
engineering_or_domain:
mechanism difference now:
allowed next diagnostic:
strategy bypass:
stop condition:
```

If infrastructure friction blocks progress for more than one work block,
consider a smaller local diagnostic or schema self-test while keeping the main
route decision separate.

## Closure

For completed work:

```text
verify artifacts exist
mark draft/checked/finalized
refresh reusable-material index when useful
sync status/registry/decision ledger when state changes
separate raw observations from claims
```

## Forbidden

- Do not use chat memory as the restart mechanism.
- Do not launch experiments without fixed evidence and output-root policy.
- Do not make metric, release, or paper claims without checked artifacts.
- Do not let support lanes make main research decisions.
