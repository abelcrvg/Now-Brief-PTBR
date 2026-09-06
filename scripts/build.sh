#!/usr/bin/env bash
set -euo pipefail

PROJECT="${1:-decompiled}"

command -v apktool >/dev/null 2>&1 || {
  echo "apktool não encontrado." >&2
  exit 1
}

if [[ ! -d "$PROJECT" ]]; then
  echo "Projeto descompilado não encontrado: $PROJECT" >&2
  exit 1
fi

apktool b "$PROJECT" -o Now-Brief-unsigned.apk

echo "APK reconstruído: Now-Brief-unsigned.apk"
