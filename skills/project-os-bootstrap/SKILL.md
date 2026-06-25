---
name: project-os-bootstrap
description: Create, install, audit, or repair a reusable project operating system for research or engineering projects. Use when starting a new project, migrating an existing project into a disciplined workflow, creating AGENTS.md/current_state/artifact registry/decision ledger/preflight/finalizer structure, preserving a project for restart, or adapting the new_paper-style guidance system to another project without copying project-specific science claims.
---

# Project OS Bootstrap

Use this skill to give any serious project a small operating system: entry
rules, current state, artifacts, decisions, failure logs, preflight gates, and
restart/preservation discipline.

This skill is project-agnostic. Do not copy old project claims, AP metrics,
denominators, dataset names, or route conclusions into a new project unless the
user explicitly asks to migrate that exact project.

## Default Workflow

1. Identify the project root and user goal.
2. Decide whether this is a new install, audit, repair, or preservation.
3. If the project already has rules, read them before changing anything:
   `AGENTS.md`, `.codex/`, `docs/`, `status/`, `README`, or local scripts.
4. Create or repair this minimal structure:

```text
AGENTS.md
project_os/
  status/current_state.json
  status/artifact_registry.jsonl
  status/decision_ledger.jsonl
  status/active_subagents.json
  status/finalized_results.jsonl
  templates/result_card_template.md
  templates/preservation_card_template.md
  tools/project_preflight.py
  tools/finalize_result.py
  tools/register_artifact.py
```

5. Keep domain-specific work outside the project OS. The OS tracks evidence and
   decisions; it does not decide the scientific truth by itself.
6. Run the generated preflight before nontrivial work.
7. Preserve and restart from state files, not chat memory.

## Project Entry Rules

Every nontrivial work block should start by answering:

```text
task:
why now:
task type: research | engineering | docs | status | route | report | process
current state:
active branch or route:
fixed denominator or evidence object:
subagent decision:
new experiment:
allowed actions:
forbidden actions:
claim allowed:
failure attribution needed:
strategy bypass check:
expected artifact:
finalize needed:
```

For small general software projects, replace `fixed denominator` with the
stable object being tested, such as `test suite`, `benchmark`, `dataset`,
`deployment target`, or `issue id`.

## State Files

Use `current_state.json` as the single machine-readable entry point:

```json
{
  "schema_version": 1,
  "updated_at": "",
  "project_name": "",
  "mainline": "",
  "station": "",
  "active_branch": "",
  "active_question": "",
  "current_evidence_object": "",
  "next_required_deliverable": "",
  "hard_rules": [],
  "forbidden_next_actions": []
}
```

Use append-only JSONL for evidence chains:

```text
artifact_registry.jsonl   -> files that matter
decision_ledger.jsonl     -> decisions and why
finalized_results.jsonl   -> checked results
engineering_errors.jsonl  -> repeated failures and guardrails
```

## Preflight Rules

Before experiments, server jobs, destructive edits, route changes, status
claims, or paper/report claims:

1. Verify required OS files exist.
2. Read `current_state.json`.
3. Check whether state is stale relative to newer reports.
4. Check active subagents.
5. Check whether the branch/route is known.
6. State whether a claim is allowed.
7. Block if required evidence identity is missing.

Use `scripts/bootstrap_project_os.py` from this skill to install a starter kit.

## Preservation

When a project pauses or might stop:

1. Create a lightweight Git-tracked restart branch with code, docs, state, and
   manifests only.
2. Keep large data, model weights, caches, and raw outputs outside Git.
3. Write a preservation card with:

```text
where the full snapshot lives
what is tracked in Git
what is intentionally excluded
current state
last checked result
known blockers
exact restart steps
```

4. Test that another agent can restart from `AGENTS.md` and `current_state.json`.

## Subagents

Use subagents for bounded support work:

```text
engineering/tooling
transfer/server setup
status/artifact sync
docs/report drafts
audits and inventory
```

Keep main-thread decisions on:

```text
research route
metric interpretation
pass/hold/stop
claims
state progression
```

If no subagent is used, write `none_with_reason` with a real reason.

## Forbidden

- Do not copy a previous project's scientific claims into a new project OS.
- Do not let the OS become a pile of stale documents; keep `current_state.json`
  authoritative.
- Do not claim results from unfinalized artifacts.
- Do not put large data, model weights, caches, or raw run directories into Git.
- Do not retry repeated engineering failures without a root cause and guardrail.
- Do not use chat memory as the only restart mechanism.
