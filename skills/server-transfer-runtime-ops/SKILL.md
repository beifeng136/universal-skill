---
name: server-transfer-runtime-ops
description: Run a pre-launch gate for server or remote transfer and runtime execution. Use for material manifests, queue health, runtime profiles, runner wrappers, large artifact bundles, checked server launches, server-side bytes/hash verification, missing/mismatch transfer plans, and BLOCK/HOLD/ALLOW decisions before durable remote jobs.
---

# Server Transfer Runtime Ops

Use this skill to compose transfer, runtime, queue, wrapper, and launch checks
into one remote-execution gate. It does not authorize route, metric, product,
ground-truth, prediction, release, or paper decisions.

## Gate Workflow

1. Read project entry rules and current state.
2. Confirm a real task declaration and subagent decision.
3. Query reusable materials if this recreates material.
4. Build an exact required-files manifest.
5. Verify remote-side bytes/hash, not local existence.
6. Probe runtime imports and model/asset load if relevant.
7. Check runner wrapper/status contract.
8. Check output root is absent for a new launch.
9. Decide `BLOCK_LAUNCH`, `HOLD_FOR_REVIEW`, or `ALLOW_CHECKED_SERVER_LAUNCH`.

## Fastlane Defaults

```text
large_data_policy:
  keep checked large artifacts server-resident
  sync changed scripts/configs first
  transfer only missing or mismatched manifest rows
  pull back summary/status/manifests before huge payloads

launch_ladder:
  wrapper contract
  read-only remote path/hash probe
  runtime import/model-load probe
  materialize/table-only run
  evaluation or heavy execution only after materialization is checked
```

Do not parse huge JSON/CSV files in interactive shells; use hashes, streaming
counters, or checked summaries.

## Decision Rules

`BLOCK_LAUNCH` when:

```text
preflight/status gate is blocked
manifest is missing or ambiguous
remote verification has missing/mismatched rows
runtime or model-load probe fails
wrapper/status contract fails
new output root already exists
status source or expected artifacts are undefined
same-class engineering failure lacks guardrail and self-test
```

`HOLD_FOR_REVIEW` when a noncritical warning needs main-thread judgment.

`ALLOW_CHECKED_SERVER_LAUNCH` only when transfer, runtime, wrapper,
output-root, status, fallback, and finalizer expectations are green.

## Failure Intake

Before retrying failed remote work, record:

```text
error id:
task:
command or runner:
expected:
observed:
first bad artifact/log:
failure_layer:
root_cause:
guardrail:
self-test:
retry_allowed:
next_output_root:
```

## Forbidden

- Do not launch from local-only proof.
- Do not overwrite existing roots or failed roots.
- Do not use ambiguous foreground transport for durable long jobs.
- Do not duplicate jobs after status timeout without queue/status diagnostics.
- Do not convert missing imports, path drift, wrapper failure, or missing files
  into scientific/domain failure evidence.
