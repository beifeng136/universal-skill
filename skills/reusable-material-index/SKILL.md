---
name: reusable-material-index
description: Query, verify, and refresh a project's reusable material index before rerunning experiments, rebuilding artifacts, selecting datasets, reusing outputs, or creating duplicated material. Use for manifests, prediction files, feature tables, benchmark outputs, scripts, model artifacts, reports, source materials, known risk notes, and any task where existing artifacts may save work or prevent stale/wrong evidence.
---

# Reusable Material Index

Use this skill before creating or reusing project material. The goal is to
prevent duplicate work, stale evidence objects, wrong artifact identity,
leakage, and accidental comparison across incompatible inputs.

## Workflow

1. Identify the target project root and its authority files:
   - entry rules
   - artifact registry
   - reusable-material index, if present
   - finalized or checked results
   - current state or route card
2. Query the smallest useful index first. Prefer a project query script if one
   exists; otherwise use targeted search over registry, status cards, readouts,
   manifests, and filenames.
3. If the first query returns no hits, broaden terms once before rebuilding.
4. Before reuse, verify identity and risk fields.
5. After producing a reusable checked artifact, refresh or update the index.

## Reuse Check

Verify before depending on an artifact:

```text
artifact id:
path:
evidence object / split / benchmark / issue id:
input ids:
source data policy:
prediction or output identity:
producer script or run id:
checked/finalized status:
registry entry:
known risk notes:
leakage / oracle / private-data risk:
compatible with current task? yes/no:
```

For non-research projects, replace evidence object with the stable target of
work: release version, deployment target, customer case, test suite, dataset,
or benchmark.

## Refresh Rule

When a completed artifact may be reused later:

```text
register artifact
record checked/finalized state
refresh material index or add an index entry
state whether downstream use is allowed, draft-only, or blocked
```

If no reusable index exists, create a small durable note or registry entry
instead of leaving reuse knowledge only in chat.

## Forbidden

- Do not compare results from different evidence objects unless the comparison
  is explicitly designed for that mismatch.
- Do not reuse diagnostic-only, oracle, private, or leakage-prone fields as
  deployable features.
- Do not treat unfinalized outputs as checked evidence.
- Do not overwrite historical output roots to make reuse look cleaner.
