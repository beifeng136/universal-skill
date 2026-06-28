---
name: status-artifact-registry-sync
description: Synchronize project status cards, artifact registry entries, decision ledger notes, finalized-result references, and reusable material indexes after process, docs, engineering, route, report, or finalized-result work. Use when state/registry hygiene is needed without making scientific, product, metric, data, prediction, denominator, or route decisions.
---

# Status Artifact Registry Sync

Use this skill for status and artifact hygiene. It does not replace the project
entry rules, preflight script, route gate, or finalizer.

## Required Startup

1. Read the project entry rules.
2. Run the project preflight/status gate with a status, docs, report, process,
   or registry-sync task type when available.
3. Stop if the gate blocks work.

## Canonical Targets

Map these concepts to the target project's actual files:

```text
current state
artifact registry
decision ledger
finalized results
active subagents
reusable material index
status cards
route/readout cards
engineering error log
```

## Sync Rules

- Distinguish `draft`, `checked`, `current`, `hold`, `superseded`, and
  `archived` artifact states explicitly.
- Register route/readout cards as artifacts or mark them draft-only.
- Reference finalizer output before treating long work as checked complete.
- Refresh reusable material indexes after finalized reusable artifacts are
  created.
- Record decisions with reasons and evidence paths.
- Keep large data, model weights, caches, raw outputs, and private credentials
  out of Git unless the project explicitly permits them.

## Claim Boundary

Registry sync may say:

```text
artifact exists
artifact is draft/checked/current/hold
decision was recorded
finalizer record exists
```

Registry sync may not say:

```text
metric improved
route passed
paper claim is proven
release is safe
commercial readiness is established
```

Those require the relevant route, metric, product, security, or claim gate.

## Forbidden

- Do not use registry sync to advance a scientific or product route without
  main-agent route judgment.
- Do not report metrics, paper-level claims, generality, or deployable claims.
- Do not edit GT, predictions, denominators, benchmark definitions, or metric
  logic.
- Do not create checked-result status without a finalizer record.
