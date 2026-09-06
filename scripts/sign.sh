#!/usr/bin/env bash
set -euo pipefail

APK="${1:-Now-Brief-unsigned.apk}"
OUT="${2:-Now-Brief-PTBR.apk}"
KEYSTORE="${KEYSTORE:-nowbrief-debug.keystore}"
ALIAS="${KEY_ALIAS:-nowbrief}"

if [[ ! -f "$APK" ]]; then
  echo "APK não encontrado: $APK" >&2
  exit 1
fi

command -v apksigner >/dev/null 2>&1 || {
  echo "apksigner não encontrado." >&2
  exit 1
}

if [[ ! -f "$KEYSTORE" ]]; then
  command -v keytool >/dev/null 2>&1 || {
    echo "keytool não encontrado para criar a chave local." >&2
    exit 1
  }
  keytool -genkeypair -v \
    -keystore "$KEYSTORE" \
    -alias "$ALIAS" \
    -keyalg RSA \
    -keysize 2048 \
    -validity 10000 \
    -storepass android \
    -keypass android \
    -dname "CN=Now Brief PT-BR, O=Local Development, C=BR"
fi

apksigner sign \
  --ks "$KEYSTORE" \
  --ks-pass pass:android \
  --key-pass pass:android \
  --out "$OUT" \
  "$APK"

echo "APK assinado: $OUT"
