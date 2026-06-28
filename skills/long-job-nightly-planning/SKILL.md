---
name: long-job-nightly-planning
description: Plan checked long-running, background, nightly, server, training, inference, materialization, audit, transfer, or evaluation jobs with isolated output roots, fixed inputs, expected artifacts, status sources, fallback conditions, and finalization expectations. Use before staging heavy work so operational execution does not consume the main decision thread.
---

# Long Job Nightly Planning

Use this skill to package heavy work as isolated, observable execution. It does
not authorize the underlying research, release, or product route; it packages
an already-approved gate for safe running.

## Job Card

Before launch, write:

```text
job name:
owner / project tags:
approved route or gate:
fixed evidence object / benchmark / release target:
input artifacts:
input visibility proof:
runtime/env proof:
model or asset path + exact bytes/hash if relevant:
output root exists? must be false for new launch:
expected artifacts:
status source:
probe or smoke command:
fallback / stop condition:
resource use:
finalizer or closure command:
large artifact pullback policy:
```

## Execution Rules

- Use a new isolated output root for each new launch.
- Preserve failed roots; retry in a new root unless checkpoint resume is proven.
- Prefer small status/summary artifacts before pulling large outputs.
- For remote jobs, prove file visibility and runtime readiness in remote
  context.
- Run materialization or table-only stages before expensive evaluation when the
  output format itself is risky.
- Keep final pass/hold/stop or claim interpretation on the main project thread.

## Completion

A long job is not complete until:

```text
status source exists
expected artifacts exist or missing artifacts are explained
logs are available
result is checked/finalized or marked draft/failed
registry or decision ledger is updated when the output affects future work
```

## Forbidden

- Do not launch without expected artifacts, status source, fallback condition,
  and output-root policy.
- Do not overwrite existing output roots.
- Do not use stdout alone as checked completion.
- Do not let long-job debugging become the main route decision loop.
