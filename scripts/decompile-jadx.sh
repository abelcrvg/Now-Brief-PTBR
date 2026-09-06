#!/usr/bin/env bash
set -euo pipefail

APK="${1:-Now.Brief.apk}"
OUT="${2:-build/jadx}"
JADX_BIN="${JADX_BIN:-jadx}"

if [[ ! -f "$APK" ]]; then
  echo "APK não encontrado: $APK" >&2
  exit 1
fi

if ! command -v "$JADX_BIN" >/dev/null 2>&1; then
  echo "JADX não encontrado. Instale o JADX 1.5.6+ ou defina JADX_BIN=/caminho/para/jadx." >&2
  exit 1
fi

mkdir -p "$OUT"
"$JADX_BIN" --version
"$JADX_BIN" -d "$OUT" --show-bad-code --deobf "$APK"

echo
printf 'Decompilação concluída em: %s\n' "$OUT"
printf 'Código-fonte: %s/sources\n' "$OUT"
printf 'Recursos: %s/resources\n' "$OUT"
