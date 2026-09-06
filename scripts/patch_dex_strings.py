#!/usr/bin/env python3
"""Patch DEX string_data entries using the pt-BR CSV map.

The original APK is never stored in the repository. The tool operates on a
local APK supplied by the user and writes a separate patched APK.

Rather than replacing bytes in place, new string_data items are appended to
the DEX and the corresponding string_id offsets are redirected. This permits
translations to have different byte lengths without shifting existing DEX
structures. The DEX SHA-1 signature and Adler-32 checksum are recalculated.

The resulting APK is intentionally unsigned/invalidated with respect to the
original APK signature and must be signed with a test/release key afterwards.
"""
from __future__ import annotations
import argparse, csv, hashlib, struct, zipfile, zlib
from pathlib import Path


def uleb(data: bytes, pos: int):
    value = 0; shift = 0
    while True:
        b = data[pos]; pos += 1
        value |= (b & 0x7f) << shift
        if not b & 0x80: return value, pos
        shift += 7


def enc_uleb(value: int) -> bytes:
    out = bytearray()
    while True:
        b = value & 0x7f; value >>= 7
        if value: b |= 0x80
        out.append(b)
        if not value: return bytes(out)


def utf16_units(s: str) -> int:
    return len(s.encode('utf-16-le')) // 2


def load_map(path: Path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    if not rows or not {'english', 'pt-BR'}.issubset(rows[0]):
        raise SystemExit('translation CSV must contain english and pt-BR columns')
    return {r['english']: r['pt-BR'] for r in rows if r.get('english') and r.get('pt-BR')}


def patch_dex(data: bytes, mapping: dict[str, str]):
    if data[:4] != b'dex\n': return data, []
    size, _ = struct.unpack_from('<II', data, 32)
    if size != len(data): raise ValueError('DEX file_size mismatch')
    count, off = struct.unpack_from('<II', data, 56)
    ids = [struct.unpack_from('<I', data, off + i * 4)[0] for i in range(count)]
    matches = []
    for i, so in enumerate(ids):
        _, p = uleb(data, so); end = p
        while data[end] != 0: end += 1
        try: old = data[p:end].decode('utf-8')
        except UnicodeDecodeError: continue
        if old in mapping and mapping[old] != old:
            matches.append((i, old, mapping[old]))
    if not matches: return data, []
    out = bytearray(data)
    pad = (-len(out)) % 4
    out.extend(b'\0' * pad)
    for idx, old, new in matches:
        new_off = len(out)
        raw = new.encode('utf-8')
        out.extend(enc_uleb(utf16_units(new)))
        out.extend(raw)
        out.append(0)
        struct.pack_into('<I', out, off + idx * 4, new_off)
    struct.pack_into('<I', out, 32, len(out))
    data_off = struct.unpack_from('<I', out, 108)[0]
    struct.pack_into('<I', out, 104, len(out) - data_off)
    out[12:32] = hashlib.sha1(out[32:]).digest()
    struct.pack_into('<I', out, 8, zlib.adler32(out[12:]) & 0xffffffff)
    return bytes(out), matches


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input_apk', type=Path)
    ap.add_argument('output_apk', type=Path)
    ap.add_argument('--map', type=Path, default=Path('localization/pt-BR.csv'))
    args = ap.parse_args()
    mapping = load_map(args.map)
    total = 0
    with zipfile.ZipFile(args.input_apk, 'r') as zin, zipfile.ZipFile(args.output_apk, 'w') as zout:
        for info in zin.infolist():
            blob = zin.read(info.filename)
            if info.filename.endswith('.dex'):
                blob, matches = patch_dex(blob, mapping)
                if matches:
                    total += len(matches)
                    print(f'{info.filename}: {len(matches)} strings')
                    for _, old, new in matches:
                        print(f'  {old} -> {new}')
            zout.writestr(info, blob)
    print(f'patched strings: {total}')

if __name__ == '__main__': main()
