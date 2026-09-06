#!/usr/bin/env python3
"""Prepare a deterministic pt-BR string patch plan for a Now Brief build.

This script deliberately does not modify the original APK. It consumes a
CSV translation map and a text/string dump produced during decompilation and
writes a patch manifest that can be applied by the selected APK/DEX toolchain.

The separation keeps the repository free of the original/proprietary APK and
makes the localization changes reviewable and reproducible.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def load_map(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    required = {"english", "pt-BR"}
    if not required.issubset(rows[0] if rows else {}):
        raise SystemExit("CSV must contain english and pt-BR columns")
    return [r for r in rows if r.get("english") and r.get("pt-BR")]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--map", default="localization/pt-BR.csv")
    p.add_argument("--strings", required=True, help="UTF-8 text dump containing strings found in the APK")
    p.add_argument("--out", default="build/pt-BR-patch.json")
    args = p.parse_args()

    rows = load_map(Path(args.map))
    text = Path(args.strings).read_text(encoding="utf-8", errors="replace")
    present = []
    missing = []
    for row in rows:
        source = row["english"]
        item = {"from": source, "to": row["pt-BR"], "status": row.get("status", "review")}
        if source in text:
            present.append(item)
        else:
            missing.append(item)

    result = {
        "format": 1,
        "locale": "pt-BR",
        "source": str(args.strings),
        "matched": present,
        "unmatched": missing,
        "matched_count": len(present),
        "unmatched_count": len(missing),
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"matched={len(present)} unmatched={len(missing)} output={out}")


if __name__ == "__main__":
    main()
