#!/usr/bin/env python3
"""Extract heuristic const-string references from selected methods in a DEX file.

This is intentionally a lightweight analyzer: it does not decompile DEX. It resolves
method code_item offsets from class_data and scans for const-string / jumbo references.
"""
from __future__ import annotations
import argparse, struct
from pathlib import Path

def u16(b,o): return struct.unpack_from("<H",b,o)[0]
def u32(b,o): return struct.unpack_from("<I",b,o)[0]

def uleb(b,o):
    v=0; shift=0
    while True:
        x=b[o]; o+=1; v |= (x & 0x7f) << shift
        if x < 0x80: return v,o
        shift += 7

def dex_strings(b):
    n=u32(b,56); off=u32(b,60); out=[]
    for i in range(n):
        p=u32(b,off+4*i); _,p=uleb(b,p)
        start=p
        while b[p] != 0: p+=1
        out.append(b[start:p].decode("utf-8","replace"))
    return out

def dex_types(b,strings):
    n=u32(b,64); off=u32(b,68)
    return [strings[u32(b,off+4*i)] for i in range(n)]

def dex_methods(b,types,strings):
    n=u32(b,88); off=u32(b,92); out=[]
    for i in range(n):
        c=u16(b,off+8*i); name=u32(b,off+8*i+4)
        out.append((types[c],strings[name]))
    return out

def class_methods(b,class_off):
    p=u32(b,class_off+24)
    static,p=uleb(b,p); inst,p=uleb(b,p); direct,p=uleb(b,p); virtual,p=uleb(b,p)
    for count in (static,inst):
        idx=0
        for _ in range(count):
            d,p=uleb(b,p); _,p=uleb(b,p); idx+=d
    result=[]
    for kind,count in (("direct",direct),("virtual",virtual)):
        idx=0
        for _ in range(count):
            d,p=uleb(b,p); flags,p=uleb(b,p); code,p=uleb(b,p); idx+=d
            result.append((kind,idx,flags,code))
    return result

def refs(b,code_off,strings):
    if not code_off: return []
    size=u32(b,code_off+12); start=code_off+16
    if start+2*size > len(b): return []
    units=[u16(b,start+2*i) for i in range(size)]
    found=[]
    for i,w in enumerate(units):
        op=w & 0xff
        if op == 0x1a and i+1 < size:
            idx=units[i+1]
        elif op == 0x1b and i+2 < size:
            idx=units[i+1] | (units[i+2] << 16)
        else:
            continue
        if idx < len(strings): found.append((idx,strings[idx]))
    return found

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("dex", type=Path)
    ap.add_argument("--class", dest="klass", required=True)
    ap.add_argument("--method", action="append", required=True)
    args=ap.parse_args()
    b=args.dex.read_bytes(); strings=dex_strings(b); types=dex_types(b,strings)
    methods=dex_methods(b,types,strings)
    defs_off=u32(b,100); defs_size=u32(b,96); class_off=None
    for i in range(defs_size):
        off=defs_off+32*i
        if types[u32(b,off)] == args.klass: class_off=off; break
    if class_off is None: raise SystemExit(f"class not found: {args.klass}")
    wanted=set(args.method)
    for _,mi,_,code in class_methods(b,class_off):
        name=methods[mi][1]
        if name not in wanted: continue
        seen=[]
        for item in refs(b,code,strings):
            if item not in seen: seen.append(item)
        print(f"[{name}] {len(seen)} string refs")
        for idx,s in seen: print(f"  {idx}: {s}")

if __name__ == "__main__": main()
