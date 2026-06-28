# Reusable Project Kit

This folder stores project-agnostic assets extracted from the `new_paper`
operating system so future projects can reuse the workflow without inheriting
old scientific claims or large data.

Many old project skills are already generally useful even when their bodies
mention old project names or paths. Treat those mentions as placeholders to
translate into the target project's authority files.

## Included

- `skills/project-os-bootstrap`: create a minimal project operating system.
- `skills/living-engineering-error-loop`: turn repeated engineering failures
  into guardrails.
- `skills/project-guidance-transfer`: extract reusable workflow guidance from
  an old project and adapt it into a new project without copying old claims.
- `skills/project-entry-state-lock`: start governed work from the real project
  state instead of chat memory.
- `skills/research-accelerator`: coordinate long-running research work without
  route drift.
- `skills/research-route-gate`: plan, hold, stop, switch, scale, and report
  evidence-driven routes safely.
- `skills/experiment-launch-denominator-gate`: gate experiment launches by
  fixed evidence object, output root, expected artifacts, and finalization.
- `skills/reusable-material-index`: query and verify existing artifacts before
  rebuilding or rerunning work.
- `skills/failure-attribution-strategy-bypass`: diagnose failed or weak routes
  before retry and require a real mechanism difference.
- `skills/route-readout-card-authoring`: write route/readout cards with
  evidence scope, artifact state, diagnosis, and claim boundaries.
- `skills/checked-result-finalizer`: finalize auditable results before state,
  route, metric, paper, or release claims.
- `skills/status-artifact-registry-sync`: synchronize status, artifacts,
  decisions, finalized results, and reusable material indexes.
- `skills/runtime-capability-inventory`: choose local/server/model/runtime
  environments from evidence rather than names.
- `skills/long-job-nightly-planning`: package heavy/background jobs with fixed
  inputs, isolated output roots, status sources, and finalizers.
- `skills/subagent-coordination-and-active-registry`: delegate bounded support
  work while preserving main-agent decision ownership.
- `skills/paper-claim-writing`: draft report/manuscript language from checked
  evidence only.
- `skills/cross-project-server-fastlane`: prepare safe server transfer/runtime
  execution.
- `skills/engineering-transfer-guardrail`: harden transfer, remote execution,
  queue, wrapper, and retry work.
- `skills/server-transfer-runtime-ops`: run end-to-end server transfer/runtime
  pre-launch gates with BLOCK/HOLD/ALLOW decisions.
- `skills/server-execution-thread-handoff`: prepare bounded server/worker
  execution packets.
- `skills/engineering-issue-registry-recurrence`: register recurring
  engineering failures, add guardrails, self-test, and decide retry permission.

The full old-project workflow skill trigger catalog lives at:

```text
skills/project-guidance-transfer/references/old-project-skill-trigger-catalog.md
```

## Not Included

- data, model weights, raw outputs, prediction JSON, caches, logs
- `new_paper` route history, AP claims, paper drafts, dataset-specific records
- private machine/server credentials or queue identities

## Install To Codex Skills

Copy a skill folder into:

```text
C:/Users/32105/.codex/skills/<skill-name>
```

Then restart or refresh Codex so the skill metadata is loaded.

## Bootstrap A New Project

```powershell
python C:/Users/32105/.codex/skills/project-os-bootstrap/scripts/bootstrap_project_os.py `
  --root C:/path/to/new_project `
  --project-name my_project `
  --mainline "initial mainline"
```

Then start future work from the generated `AGENTS.md`.
