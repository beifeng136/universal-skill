---
name: server-execution-thread-handoff
description: Prepare checked server, remote, CI, or worker execution-thread handoffs with prerequisite cards, transfer checks, runtime proof, isolated output roots, status sources, and finalization expectations. Use before giving a separate execution thread approved probes, runners, audits, or long jobs while keeping route, metric, evidence, release, and claim decisions on the main thread.
---

# Server Execution Thread Handoff

Use this skill to prepare execution packets for a separate server or worker
thread. It scopes the worker to execution, not judgment.

## Handoff Packet

Provide:

```text
task:
approved route/gate:
forbidden decisions:
input artifacts:
remote-visible paths and bytes/hash proof:
runtime probes:
model/asset proof if relevant:
output root:
expected artifacts:
status source:
fallback condition:
large data policy:
finalization expectation:
main-thread contact condition:
```

## Worker Boundary

The execution thread may:

```text
run approved probes
run approved wrappers/runners
collect status/logs
verify expected artifacts
report engineering failures
```

The execution thread may not decide:

```text
route pass/hold/stop
metric interpretation
evidence-object changes
ground-truth or prediction policy
release readiness
paper or product claims
```

## Failure Handling

On transfer, runtime, wrapper, queue, status, permission, or evaluator failure:

```text
stop
classify failure_layer
record expected/observed/root_cause/evidence
run only bounded diagnostics until retry permission exists
retry in a new isolated root unless resume is proven
```

## Forbidden

- Do not hand off incomplete prerequisite cards.
- Do not use local-only proof for remote execution.
- Do not ask a worker thread to fetch huge artifacts when a status summary is
  sufficient.
- Do not bypass checked/finalizer rules for completed long work.
