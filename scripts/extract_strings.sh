#!/usr/bin/env bash
set -euo pipefail

APK="${1:-Now.Brief.apk}"
OUT="${2:-analysis/strings}"

if [[ ! -f "$APK" ]]; then
  echo "APK not found: $APK" >&2
  exit 1
fi

mkdir -p "$OUT"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

unzip -q -o "$APK" 'classes*.dex' -d "$TMP"
: > "$OUT/all.txt"

for dex in "$TMP"/classes*.dex; do
  [[ -f "$dex" ]] || continue
  strings -el "$dex" >> "$OUT/all.txt" || true
  strings "$dex" >> "$OUT/all.txt" || true
done

LC_ALL=C sort -u "$OUT/all.txt" -o "$OUT/all.txt"

grep -E '^[[:print:]][[:print:] ]{3,180}$' "$OUT/all.txt" \
  | grep -Ei 'brief|weather|fitness|sleep|calendar|contact|news|settings|schedule|energy|location|audio|voice|feed|photo|morning|afternoon|evening|night|today|tomorrow|welcome|ready|score|goal' \
  | grep -vE '^(androidx|android\.|kotlin\.|java\.|javax\.|org\.|com\.google|Landroid|Lcom|Icons\.|Filled\.|Outlined\.|Rounded\.|Sharp\.|TwoTone\.|Use the AutoMirrored|Expected |Failed |Cannot |Could not |Key already|Already |Fragment already|Executor already|EOF |Arrays already|Deflater already)' \
  | sort -u > "$OUT/candidates.txt" || true

echo "Wrote: $OUT/all.txt"
echo "Wrote: $OUT/candidates.txt"
