#!/usr/bin/env python3
"""Install a small, project-agnostic operating-system skeleton."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def write_new(path: Path, text: str, overwrite: bool) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return "exists"
    path.write_text(text, encoding="utf-8")
    return "written"


def json_line(obj: dict) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Project root to initialize")
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--mainline", default="mainline")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    ts = now_iso()
    actions: dict[str, str] = {}

    agents = f"""# Project Entry Rules

This project uses a reusable project operating system.

Before nontrivial work, read this file and run:

```powershell
python project_os/tools/project_preflight.py --root . --task-type <type> --action-summary "<what you will do>"
```

Then report:

```text
project:
mainline:
station:
active_branch:
current_evidence_object:
next_required_deliverable:
allowed_to_continue:
```

Hard rules:

```text
read current_state.json before route/status claims
record important artifacts in artifact_registry.jsonl
record decisions in decision_ledger.jsonl
finalize completed long tasks before claiming checked completion
do not put large data, model weights, caches, or raw run outputs in Git
repeated engineering failures need root cause, guardrail, and self-test
```
"""

    current_state = {
        "schema_version": 1,
        "updated_at": ts,
        "project_name": args.project_name,
        "mainline": args.mainline,
        "station": "initialized",
        "active_branch": "",
        "active_question": "Define the first checked deliverable.",
        "current_evidence_object": "",
        "next_required_deliverable": "initial_project_plan_or_status_card",
        "hard_rules": [
            "run project preflight before nontrivial work",
            "finalize checked results before claims",
            "record artifacts and decisions",
            "preserve large data outside Git",
        ],
        "forbidden_next_actions": [
            "claim unchecked results",
            "commit large data or model weights",
        ],
    }

    preflight = """#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=".")
    p.add_argument("--task-type", required=True)
    p.add_argument("--action-summary", required=True)
    args = p.parse_args()
    root = Path(args.root).resolve()
    required = [
        "AGENTS.md",
        "project_os/status/current_state.json",
        "project_os/status/artifact_registry.jsonl",
        "project_os/status/decision_ledger.jsonl",
        "project_os/status/finalized_results.jsonl",
    ]
    missing = [x for x in required if not (root / x).exists()]
    state = {}
    state_path = root / "project_os/status/current_state.json"
    if state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
    allowed = not missing
    print(json.dumps({
        "project_root": str(root),
        "task_type": args.task_type,
        "action_summary": args.action_summary,
        "missing_required_files": missing,
        "state": {
            "project_name": state.get("project_name"),
            "mainline": state.get("mainline"),
            "station": state.get("station"),
            "active_branch": state.get("active_branch"),
            "current_evidence_object": state.get("current_evidence_object"),
            "next_required_deliverable": state.get("next_required_deliverable"),
        },
        "allowed_to_continue": "YES" if allowed else "NO",
    }, ensure_ascii=False, indent=2))
    return 0 if allowed else 1

if __name__ == "__main__":
    raise SystemExit(main())
"""

    finalize = """#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from datetime import datetime, timezone
from pathlib import Path

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", default=".")
    p.add_argument("--result-id", required=True)
    p.add_argument("--result-kind", required=True)
    p.add_argument("--result-path", required=True)
    p.add_argument("--notes", default="")
    args = p.parse_args()
    root = Path(args.root).resolve()
    result_path = (root / args.result_path).resolve()
    if not result_path.exists():
        raise SystemExit(f"result path missing: {result_path}")
    out = root / "project_os/status/finalized_results.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    rec = {
        "result_id": args.result_id,
        "result_kind": args.result_kind,
        "result_path": str(result_path),
        "notes": args.notes,
        "timestamp": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
    }
    with out.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\\n")
    print(json.dumps(rec, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
"""

    actions["AGENTS.md"] = write_new(root / "AGENTS.md", agents, args.overwrite)
    actions["current_state.json"] = write_new(
        root / "project_os/status/current_state.json",
        json.dumps(current_state, ensure_ascii=False, indent=2) + "\n",
        args.overwrite,
    )
    for rel in [
        "project_os/status/artifact_registry.jsonl",
        "project_os/status/decision_ledger.jsonl",
        "project_os/status/finalized_results.jsonl",
        "project_os/status/engineering_errors.jsonl",
    ]:
        seed = json_line({"timestamp": ts, "event": "initialized", "project": args.project_name})
        actions[rel] = write_new(root / rel, seed, args.overwrite)

    actions["active_subagents.json"] = write_new(
        root / "project_os/status/active_subagents.json",
        json.dumps({"schema_version": 1, "active": [], "completed": []}, indent=2) + "\n",
        args.overwrite,
    )
    actions["project_preflight.py"] = write_new(
        root / "project_os/tools/project_preflight.py", preflight, args.overwrite
    )
    actions["finalize_result.py"] = write_new(
        root / "project_os/tools/finalize_result.py", finalize, args.overwrite
    )
    actions["result_card_template.md"] = write_new(
        root / "project_os/templates/result_card_template.md",
        "# Result Card\n\nresult id:\nresult kind:\ninput/evidence object:\noutput artifacts:\nclaim boundary:\nfinalizer status:\n",
        args.overwrite,
    )
    actions["preservation_card_template.md"] = write_new(
        root / "project_os/templates/preservation_card_template.md",
        "# Preservation Card\n\nsnapshot location:\ngit branch:\ntracked contents:\nexcluded contents:\ncurrent state:\nknown blockers:\nrestart steps:\n",
        args.overwrite,
    )

    print(json.dumps({"root": str(root), "actions": actions}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
