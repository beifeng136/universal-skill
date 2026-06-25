---
name: cross-project-server-fastlane
description: Prepare, audit, or repair reusable server transfer and runtime execution workflows across projects. Use for server jobs, GPU training, long-running experiments, file transfer, manifest/hash verification, runtime probes, output-root isolation, background execution, status sources, and preventing transfer/environment setup from consuming the main research or engineering thread.
---

# Cross-Project Server Fastlane

Use this skill when work needs a server, GPU, remote machine, large transfer,
or long background run. The goal is to make server work boring: manifest,
verify, probe, launch, monitor, summarize.

This skill is project-agnostic. Replace project-specific paths and result names
with the current project's values.

## Fastlane Principle

Do not send a heavy job to a server because "the files probably exist there".
Prove the server can see the exact files, runtime, output root, and wrapper
contract before launch.

Default ladder:

```text
1. required-file manifest
2. missing/mismatch transfer only
3. server-side bytes/hash verification
4. runtime/import/model probe
5. wrapper/status contract check
6. isolated output root proof
7. checked background launch
8. status probe
9. summary artifact pullback
10. finalization
```

## Minimal Launch Card

Before any long or GPU job, write a launch card:

```text
task:
owner/project/job tags:
local project root:
server project root:
transport mechanism:
fixed input/evidence object:
required files:
large artifacts:
server-visible proof:
runtime proof:
output root:
output root must be absent:
expected artifacts:
status source:
fallback condition:
finalizer command:
claim boundary:
```

Use `assets/server_prerequisite_card.template.md` as the template.

## Manifest Rules

Build manifests from exact files, not broad directories. Each row needs:

```text
relative path
local absolute path
server absolute path
bytes
sha256
kind: script | config | data | model | expected_output | other
required: true | false
```

Use this skill's `scripts/build_file_manifest.py` when a project does not have
its own manifest builder.

For large data, prefer:

```text
server-resident checked artifact
compressed bundle with server-side hash verification
missing-only or mismatch-only transfer
```

Avoid re-uploading or pulling back huge files unless the user explicitly needs
the payload locally.

## Runtime Proof

A runtime proof should show:

```text
python executable or command path
package imports
CUDA/GPU availability when relevant
model/cache path and exact bytes when relevant
write permission to output parent
```

Runtime import success is engineering readiness, not scientific evidence.

## Output Roots

New jobs must use a new isolated output root. Before launch:

```text
output root absent or intentionally empty
parent exists
job id recorded
status file path defined
logs path defined
expected artifacts listed
```

Do not overwrite failed roots. Preserve failed roots as evidence.

## BLOCK / HOLD / ALLOW

Use `BLOCK_LAUNCH` when:

```text
preflight is missing or blocked
required files are unverified on server
runtime proof is missing
model/data bytes mismatch
wrapper cannot produce status
output root already exists
expected artifacts/status source are undefined
same-class failure is being retried without guardrail
```

Use `HOLD_FOR_REVIEW` when evidence exists but needs main-thread or human
judgment.

Use `ALLOW_CHECKED_LAUNCH` only when file, runtime, output, wrapper, status,
fallback, and finalization proofs are all present.

## Reporting Boundary

Report only:

```text
readiness state
paths
hashes
status source
raw logs or summaries
BLOCK/HOLD/ALLOW
```

Do not make research route decisions, metric claims, paper claims, or business
claims from this skill alone.

## Failure Handling

For transfer/runtime/wrapper/queue failures:

```text
stop
classify failure layer
record expected vs observed
identify root cause
add a guardrail
self-test the guardrail
retry only in a new output root unless checkpoint resume is proven
```

Use the `living-engineering-error-loop` skill for the failure record.

## Forbidden

- Do not trust local path existence as server visibility.
- Do not launch from broad unverified directory assumptions.
- Do not use foreground interactive transport for durable long jobs.
- Do not overwrite output roots or failed roots.
- Do not clear another user's queue or remote workspace.
- Do not convert engineering failures into scientific or product evidence.
- Do not parse huge JSON/CSV interactively when a streaming summary or hash is
  enough.
