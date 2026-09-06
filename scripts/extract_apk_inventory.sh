#!/usr/bin/env bash
set -euo pipefail
APK="${1:-Now.Brief.apk}"
OUT="${2:-apk-inventory}"
rm -rf "$OUT"
mkdir -p "$OUT/dex"
unzip -q "$APK" -d "$OUT/unpacked"
find "$OUT/unpacked" -type f | sort > "$OUT/files.txt"
find "$OUT/unpacked" -type f -name '*.dex' -print0 | while IFS= read -r -d '' f; do
  b=$(basename "$f")
  strings -el "$f" > "$OUT/dex/${b}.utf16.txt" || true
  strings "$f" > "$OUT/dex/${b}.ascii.txt" || true
done
find "$OUT/unpacked/assets" -type f -printf '%P\n' 2>/dev/null | sort > "$OUT/assets.txt" || true
python - "$OUT" <<'PY'
import sys
from pathlib import Path
out=Path(sys.argv[1])
files=(out/'files.txt').read_text(errors='ignore').splitlines()
lines=['# APK inventory','','| Item | Value |','|---|---|',f'| ZIP entries | {len(files)} |']
for p in files:
    if p.endswith('.dex'):
        fp=out.parent / p
        if fp.exists(): lines.append(f'| {p} | {fp.stat().st_size} bytes |')
(out/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
PY
