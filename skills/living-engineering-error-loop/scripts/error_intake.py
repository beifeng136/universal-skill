#!/usr/bin/env python3
"""Draft or append portable engineering failure intake records."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out-jsonl", required=True)
    p.add_argument("--error-id", required=True)
    p.add_argument("--project", default="")
    p.add_argument("--task", required=True)
    p.add_argument("--command-or-runner", default="")
    p.add_argument("--failure-layer", required=True)
    p.add_argument("--expected", default="")
    p.add_argument("--observed", required=True)
    p.add_argument("--root-cause", default="unknown")
    p.add_argument("--guardrail", default="")
    p.add_argument("--self-test", default="")
    p.add_argument("--retry-allowed", choices=["yes", "no", "diagnostic_only"], default="no")
    args = p.parse_args()

    rec = {
        "error_id": args.error_id,
        "timestamp": now_iso(),
        "project": args.project,
        "task": args.task,
        "command_or_runner": args.command_or_runner,
        "expected": args.expected,
        "observed": args.observed,
        "failure_layer": args.failure_layer,
        "root_cause": args.root_cause,
        "guardrail": args.guardrail,
        "self_test": args.self_test,
        "retry_allowed": args.retry_allowed,
    }

    out = Path(args.out_jsonl)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\n")
    print(json.dumps(rec, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
