---
name: runtime-capability-inventory
description: Choose or audit local, server, CI, GPU, model, dependency, cache, and execution environments from evidence rather than names. Use before running experiments, long jobs, model inference, training, deployment checks, server handoffs, or any task where module availability, hardware, file visibility, model weights, or runtime freshness could affect results.
---

# Runtime Capability Inventory

Use this skill before selecting an execution environment. It prevents path,
dependency, model-weight, and hardware assumptions from being mistaken for
ready-to-run evidence.

## Workflow

1. Read the target project entry rules and current state.
2. Locate the runtime inventory, if present.
3. Check inventory freshness against the intended task risk.
4. Probe only the missing facts needed for launch readiness.
5. Record the selected runtime and fallback.

## Selection Checklist

```text
inventory date:
freshness / staleness risk:
selected machine:
selected shell:
selected python or runtime:
hardware / GPU / accelerator:
required modules:
model or asset paths:
exact bytes/hash when weights or large assets matter:
input path visibility proof:
write permission proof:
runnable task class:
blocked capabilities:
fallback runtime:
status source:
```

For server or remote work, add:

```text
remote-context probe:
remote-visible input bytes/hash:
runtime import probe:
model-load probe if weights matter:
isolated output-root write proof:
queue or background-job status source:
```

## Failure Handling

If imports fail, weights are missing, GPU memory is insufficient, or remote
paths are invisible, classify the result as runtime/engineering until logs
prove a domain limitation. On repeated failure, use an engineering recurrence
loop before retry.

## Forbidden

- Do not assume readiness from environment names.
- Do not treat local path existence as server visibility.
- Do not treat import-only proof as model-load proof.
- Do not call missing files, missing imports, or path drift a model failure.
- Do not make metric, route, release, or paper claims from runtime inventory.
