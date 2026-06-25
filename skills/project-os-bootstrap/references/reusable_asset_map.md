# Reusable Asset Map

Use this map when extracting a project operating system from an existing
project.

## Usually Reusable

- Entry rules: `AGENTS.md` shape, startup gate, current-state acknowledgement.
- State skeleton: current state, artifact registry, decision ledger, finalized
  results, active subagents, engineering errors.
- Finalizer pattern: verify result path and expected artifacts before claiming
  checked completion.
- Artifact registry schema: stable id, path, status, provenance, claim boundary.
- Decision ledger schema: decision id, timestamp, evidence, consequence,
  forbidden next actions.
- Failure attribution: failure layer, root cause, strategy bypass, retry rules.
- Preservation card: snapshot location, Git branch, exclusions, restart steps.
- Reusable material index concept: query existing materials before rebuilding.

## Project-Specific, Do Not Reuse Blindly

- Dataset names, model names, metric identities, paper claims, route outcomes.
- Existing registry JSONL records.
- Branch maps and decision history.
- Large data, model weights, prediction JSON, raw run outputs, logs, caches.
- Private machine paths, credentials, bucket names, remote queue identities.

## Good Cross-Project Skill Candidates

- project OS bootstrap
- checked result finalizer
- reusable asset/material index
- remote execution transfer fastlane
- engineering recurrence registry
- long job planner
- runtime capability inventory
- evidence card authoring
