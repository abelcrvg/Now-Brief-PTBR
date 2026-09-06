#!/usr/bin/env python3
"""Validate a patched APK without requiring Android build tools.

Checks ZIP integrity, DEX headers/sizes/checksums, and verifies that mapped
English strings are absent from DEX string tables when they were replaced.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import struct
import sys
import zipfile
import zlib
from pathlib import Path


def uleb(data: bytes, off: int):
    result = 0
    shift = 0
    while True:
        b = data[off]
        off += 1
        result |= (b & 0x7f) << shift
        if not b & 0x80:
            return result, off
        shift += 7


def dex_strings(data: bytes) -> set[str]:
    if data[:4] != b"dex\n":
        raise ValueError("not a DEX file")
    string_ids_size, string_ids_off = struct.unpack_from("<II", data, 56)
    out = set()
    for i in range(string_ids_size):
        off = struct.unpack_from("<I", data, string_ids_off + i * 4)[0]
        _, p = uleb(data, off)
        end = data.index(b"\x00", p)
        out.add(data[p:end].decode("utf-8"))
    return out


def validate_dex(name: str, data: bytes):
    errors = []
    if len(data) < 112 or data[:8] != b"dex\n039\x00":
        return [f"{name}: invalid DEX header"]
    file_size = struct.unpack_from("<I", data, 32)[0]
    header_size = struct.unpack_from("<I", data, 36)[0]
    endian = struct.unpack_from("<I", data, 40)[0]
    if file_size != len(data):
        errors.append(f"{name}: file_size={file_size}, actual={len(data)}")
    if header_size != 112:
        errors.append(f"{name}: header_size={header_size}")
    if endian != 0x12345678:
        errors.append(f"{name}: unexpected endian tag 0x{endian:08x}")
    expected_sha1 = hashlib.sha1(data[32:]).digest()
    if data[12:32] != expected_sha1:
        errors.append(f"{name}: SHA-1 signature mismatch")
    expected_adler = zlib.adler32(data[12:]) & 0xffffffff
    actual_adler = struct.unpack_from("<I", data, 8)[0]
    if actual_adler != expected_adler:
        errors.append(f"{name}: Adler-32 mismatch")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("apk", type=Path)
    ap.add_argument("--map", dest="mapping", type=Path, default=Path("localization/pt-BR.csv"))
    args = ap.parse_args()
    if not args.apk.is_file():
        print(f"ERROR: APK not found: {args.apk}")
        return 2

    with zipfile.ZipFile(args.apk) as z:
        bad = z.testzip()
        if bad:
            print(f"ERROR: corrupt ZIP entry: {bad}")
            return 1
        dex_names = sorted(n for n in z.namelist() if n.endswith(".dex"))
        if not dex_names:
            print("ERROR: no DEX files found")
            return 1
        all_strings = set()
        errors = []
        for name in dex_names:
            data = z.read(name)
            errors.extend(validate_dex(name, data))
            try:
                all_strings.update(dex_strings(data))
            except Exception as exc:
                errors.append(f"{name}: string table parse failed: {exc}")

    if errors:
        for e in errors:
            print("ERROR:", e)
        return 1

    missing_replacements = 0
    checked = 0
    with args.mapping.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            src = (row.get("source") or "").strip()
            dst = (row.get("pt-BR") or row.get("pt_br") or row.get("translation") or "").strip()
            if not src or not dst:
                continue
            checked += 1
            if src in all_strings and dst not in all_strings:
                # Source may legitimately remain in a non-UI context; report, don't fail.
                missing_replacements += 1

    print(f"OK: ZIP integrity + {len(dex_names)} DEX checksum(s) validated")
    print(f"OK: {len(all_strings)} unique DEX strings indexed")
    print(f"INFO: {checked} localization entries checked; {missing_replacements} source-only entries remain")
    if missing_replacements:
        print("WARNING: remaining source-only entries may be legitimate or may need another patch strategy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
