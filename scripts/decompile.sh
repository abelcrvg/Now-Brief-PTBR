#!/usr/bin/env bash
set -euo pipefail

APK="${1:-Now.Brief.apk}"
OUT="${2:-decompiled}"

if [[ ! -f "$APK" ]]; then
  echo "APK não encontrado: $APK" >&2
  exit 1
fi

command -v apktool >/dev/null 2>&1 || {
  echo "apktool não encontrado. Instale o apktool antes de executar este script." >&2
  exit 1
}

rm -rf "$OUT"
apktool d -f "$APK" -o "$OUT"
echo "Descompilação concluída em: $OUT"
