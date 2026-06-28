---
name: experiment-launch-denominator-gate
description: Gate experiment launches, reruns, scale-ups, and handoffs against project startup, reusable-material lookup, fixed evidence object or denominator discipline, smallest useful test selection, expected artifacts, and checked-result requirements. Use before opening, rerunning, scaling, or delegating science/engineering experiment work.
---

# Experiment Launch Denominator Gate

Use this skill to prepare or audit an experiment launch gate. It does not
replace the project's entry rules or preflight script.

## Required Startup

1. Read the project entry rules.
2. Run the project preflight/status gate with real task fields when available.
3. Stop if `allowed_to_continue` or the equivalent gate is not positive.
4. Query the project's reusable material index, artifact registry, prior
   readouts, or manifests for relevant dataset, mechanism, source, runner,
   denominator, or benchmark terms unless there is a concrete skip reason.

## Gate Checklist

Before launch, confirm:

```text
experiment objective:
fixed evidence object / denominator / split / benchmark:
smallest useful gate:
output root:
expected artifacts:
status source:
pass condition:
hold condition:
stop condition:
fallback condition:
reusable material checked:
large-data policy:
finalization path:
claim boundary:
```

For server-backed or long experiments, require:

```text
path visibility proof
runtime smoke
hash or manifest check
isolated output root
background status source
checked materialization before evaluation
```

## Launch Bias

Prefer:

```text
small fixed gates over full reruns
existing reusable artifacts over recreation
schema/materialize-only checks before evaluation
summaries/manifests/hashes over large artifact transfer
explicit output roots over implicit defaults
```

## Forbidden

- Do not make route decisions from this skill alone.
- Do not claim metrics, generality, paper-level, commercial, or deployable
  results from a launch gate.
- Do not edit GT, prediction material, denominator definitions, or metric logic
  unless that is explicitly the gated task.
- Do not bypass checked/finalizer requirements when results may support future
  claims.
- Do not launch a heavy rerun when a smaller fixed diagnostic can answer the
  next question.
