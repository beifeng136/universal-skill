#!/usr/bin/env python3
"""Build a portable bytes/sha256 manifest for exact required files."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", required=True)
    p.add_argument("--input-list", required=True, help="Text file, one relative file per line")
    p.add_argument("--server-root", required=True)
    p.add_argument("--out-json", required=True)
    p.add_argument("--out-csv", default="")
    args = p.parse_args()

    root = Path(args.root).resolve()
    input_list = Path(args.input_list).resolve()
    rows = []
    for raw in input_list.read_text(encoding="utf-8").splitlines():
        rel = raw.strip().replace("\\", "/")
        if not rel or rel.startswith("#"):
            continue
        local = (root / rel).resolve()
        if not local.exists() or not local.is_file():
            raise SystemExit(f"required file missing or not a file: {rel}")
        rows.append(
            {
                "relpath": rel,
                "local_path": str(local),
                "server_path": str(Path(args.server_root) / rel),
                "bytes": local.stat().st_size,
                "sha256": sha256_file(local),
                "required": True,
            }
        )

    out_json = Path(args.out_json)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps({"root": str(root), "files": rows}, indent=2), encoding="utf-8")

    if args.out_csv:
        out_csv = Path(args.out_csv)
        out_csv.parent.mkdir(parents=True, exist_ok=True)
        with out_csv.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["relpath", "local_path", "server_path", "bytes", "sha256", "required"])
            w.writeheader()
            w.writerows(rows)

    print(json.dumps({"file_count": len(rows), "out_json": str(out_json)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
