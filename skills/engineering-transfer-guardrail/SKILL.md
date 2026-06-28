---
name: engineering-transfer-guardrail
description: Prepare, audit, or harden file transfer, server execution, queue work, dependency sync, remote/local path mapping, runner wrappers, materialization, long jobs, and engineering retries. Use when infrastructure work could otherwise consume the main project thread or be mistaken for scientific, product, metric, or release evidence.
---

# Engineering Transfer Guardrail

Use this skill for transfer and infrastructure work. It keeps engineering
bounded and prevents operational problems from becoming domain claims.

## Transfer Gate

Before moving or launching anything, prove:

```text
task class:
local source path:
remote target path:
transport mechanism:
required files:
bytes/hash manifest:
remote-visible proof:
runtime proof:
output root:
output root launch rule:
expected artifacts:
status source:
fallback condition:
owner/project/job tags:
```

Prefer manifest-driven missing/mismatch transfer over broad ad hoc copying.
For large artifacts, keep them remote-resident when summaries, hashes, or
manifests are sufficient.

## Launch Decisions

Use:

```text
BLOCK_LAUNCH:
  hard prerequisite missing or failed

HOLD_FOR_REVIEW:
  evidence exists but needs main-thread or human judgment

ALLOW_CHECKED_LAUNCH:
  transfer, runtime, wrapper, output-root, status, fallback, and finalization
  expectations are green
```

## Recurrence Rule

For same-class failures:

```text
stop
classify failure_layer
record expected / observed / root cause / evidence
patch guardrail or record manual exception
self-test the guardrail
retry only in a new isolated root unless resume is proven
```

## Forbidden

- Do not treat local path existence as remote visibility.
- Do not launch from incomplete prerequisite cards.
- Do not overwrite output roots, failed roots, manifests, or status files.
- Do not clear another owner's queue or shared execution state.
- Do not let execution helpers make route, metric, ground-truth, prediction,
  release, or paper-claim decisions.
