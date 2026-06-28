# Reusable Project Kit

This folder stores project-agnostic assets extracted from the `new_paper`
operating system so future projects can reuse the workflow without inheriting
old scientific claims or large data.

## Included

- `skills/project-os-bootstrap`: create a minimal project operating system.
- `skills/cross-project-server-fastlane`: prepare safe server transfer/runtime
  execution.
- `skills/living-engineering-error-loop`: turn repeated engineering failures
  into guardrails.
- `skills/project-guidance-transfer`: extract reusable workflow guidance from
  an old project and adapt it into a new project without copying old claims.

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
