---
name: route-readout-card-authoring
description: Draft route cards, diagnostic readouts, experiment summaries, decision notes, and status cards with explicit artifact state, evidence scope, observation, diagnosis, route decision, next action, and claim boundaries. Use when writing reports that must not imply unsupported metrics, results, dataset scope, release readiness, or paper claims.
---

# Route Readout Card Authoring

Use this skill for durable project readouts. It writes what is known, what is
not known, and what decision is or is not authorized.

## Startup

1. Read the target project's entry rules and current state.
2. Run the project's preflight/status gate if one exists.
3. Identify whether the card is draft-only or checked.
4. Do not turn a draft readout into a route decision unless the project rules
   authorize that decision.

## Card Shape

```text
card id:
artifact_state: draft | checked | finalized | hold_unfinalized
task / route:
evidence object / benchmark / target:
input artifacts:
output artifacts:
observation:
diagnosis:
failure attribution needed:
route decision: none | pass | hold | stop | switch | scale
next action:
claim boundary:
finalizer / registry status:
```

Use bounded language when the evidence is small, diagnostic, draft-only, or
not representative.

## HOLD_UNFINALIZED

Mark a card `hold_unfinalized` when:

```text
artifacts exist but have not been checked
metrics are reported without traceable evaluator identity
the fixed evidence object is missing
registry/finalizer entries are missing
the card depends on support output that lacks final artifacts
```

## Forbidden

- Do not imply performance, release, or paper claims from unfinalized artifacts.
- Do not edit ground truth, predictions, denominator definitions, metric logic,
  production configuration, or route state from a readout-only task.
- Do not hide uncertainty by moving it into vague wording.
