---
name: checked-result-finalizer
description: Finalize or audit completed long tasks, subagent handoffs, status syncs, docs/process artifacts, route cards, readout cards, engineering outputs, and results that may support project state, route progression, artifact reuse, metric claims, release notes, or paper/reporting claims.
---

# Checked Result Finalizer

Use this skill when work is complete enough that it might affect state,
artifact reuse, route progression, metric reporting, paper/report claims,
release claims, or subagent closure.

## Finalization Workflow

1. Identify result class:
   - `long_job`
   - `subagent`
   - `route_card`
   - `readout_card`
   - `status_sync`
   - `docs`
   - `engineering`
   - `experiment_result`
   - `release_artifact`
2. Check the target project's finalized-results ledger for an existing matching
   result id.
3. Verify result path, expected artifacts, and status sources exist before
   finalization. Missing expected artifacts are a hold, not a warning.
4. Decide whether the output is checked or draft.
5. If no finalizer record exists yet, report `HOLD_UNFINALIZED`; do not claim
   checked completion, metric results, route progression, artifact reuse, or
   paper/release readiness.
6. Update subagent status if applicable.
7. Run the target project's finalizer tool when one exists.
8. Keep draft outputs from advancing state.

## Completion Checklist

```text
result id:
result kind:
artifact paths:
status source:
fixed evidence object if metric/claim relevant:
prediction/GT/data edit flag:
metric claim flag:
paper/release/product claim flag:
artifact registry action:
decision ledger action:
finalizer action:
state sync needed:
subagent closure needed:
```

## Generic Finalizer Record

If the project has no finalizer tool, create an append-only record with:

```text
timestamp:
result_id:
result_kind:
result_path:
expected_artifacts:
verified_artifacts:
status:
claim_boundary:
notes:
```

## Forbidden

- Do not claim checked completion from stdout, chat memory, or folder existence.
- Do not treat a readout with summary numbers as checked evidence until a
  finalizer record exists.
- Do not register drafts as current checked results.
- Do not finalize before verifying expected artifacts and status sources.
- Do not parallelize finalization with verification.
