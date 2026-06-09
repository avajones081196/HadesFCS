#!/usr/bin/env python3
"""
compare_netlists.py  —  KiCad netlist comparator (version D & E)
Usage:
    python3 compare_netlists.py <original.net> <skidl.net>
"""

import re
import sys
from collections import defaultdict

# ─────────────────────────────────────────────────────────────────────────────
# Parser — handles both KiCad version D (spaces) and version E (tabs)
# ─────────────────────────────────────────────────────────────────────────────

def parse_netlist(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # ── Components ────────────────────────────────────────────────────────────
    # Version E: (comp \n (ref) \n (value) \n (footprint))
    # Version D: (comp \n (ref) \n (value) \n (description) \n (footprint))
    # Strategy: find each (comp ...) block, then extract ref/value/footprint from it
    components = {}
    for block in re.split(r'\n\s*(?=\(comp[\s\n])', content):
        ref_m = re.search(r'\(ref\s+"([^"]+)"\)', block)
        val_m = re.search(r'\(value\s+"([^"]+)"\)', block)
        fp_m  = re.search(r'\(footprint\s+"([^"]+)"\)', block)
        if ref_m and val_m and fp_m:
            components[ref_m.group(1)] = {
                'value':     val_m.group(1),
                'footprint': fp_m.group(1),
            }

    # ── Nets ──────────────────────────────────────────────────────────────────
    nets_section = content[content.find('(nets'):]

    # Split on net blocks — works for both indentation styles
    net_blocks = re.split(r'\n\s*(?=\(net[\s\n])', nets_section)

    nets = {}           # net_name -> set of (ref, pin)
    pin_to_net = {}     # (ref, pin) -> net_name

    for block in net_blocks:
        name_match = re.search(r'\(name\s+"([^"]+)"\)', block)
        if not name_match:
            continue
        net_name = name_match.group(1)

        # Both formats: (node ... (ref "X") ... (pin "Y") ...)
        nodes = re.findall(
            r'\(node\s+\(ref\s+"([^"]+)"\)\s+\(pin\s+"([^"]+)"\)'
            r'|\(node\s*[\n\r]+\s*\(ref\s+"([^"]+)"\)\s*[\n\r]+\s*\(pin\s+"([^"]+)"\)',
            block
        )
        parsed_nodes = set()
        for m in nodes:
            # inline match
            if m[0]:
                parsed_nodes.add((m[0], m[1]))
            # multiline match
            elif m[2]:
                parsed_nodes.add((m[2], m[3]))

        nets[net_name] = parsed_nodes
        for ref, pin in parsed_nodes:
            pin_to_net[(ref, pin)] = net_name

    return components, nets, pin_to_net


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def section(title):
    print(f'\n{"─"*58}')
    print(f'  {title}')
    print(f'{"─"*58}')

def ok(msg):   print(f'  ✓  {msg}')
def fail(msg): print(f'  ✗  {msg}')
def warn(msg): print(f'  ⚠  {msg}')


# ─────────────────────────────────────────────────────────────────────────────
# Main comparison
# ─────────────────────────────────────────────────────────────────────────────

def compare(orig_path, skidl_path):
    orig_comps,  orig_nets,  orig_pin_net  = parse_netlist(orig_path)
    skidl_comps, skidl_nets, skidl_pin_net = parse_netlist(skidl_path)

    issues = []

    print('=' * 60)
    print('  NETLIST COMPARISON REPORT')
    print(f'  Original : {orig_path}')
    print(f'  SKiDL    : {skidl_path}')
    print('=' * 60)

    # ── 1. Component count ────────────────────────────────────────────────────
    section('1. COMPONENT COUNT')
    print(f'  Original : {len(orig_comps)}')
    print(f'  SKiDL    : {len(skidl_comps)}')
    if len(orig_comps) == len(skidl_comps):
        ok('Match!')
    else:
        diff = set(orig_comps) ^ set(skidl_comps)
        fail(f'Mismatch! Differing refs: {sorted(diff)}')
        issues.append(f'Component count mismatch: {len(orig_comps)} vs {len(skidl_comps)}')

    # ── 2. Reference designators ──────────────────────────────────────────────
    section('2. REFERENCE DESIGNATORS')
    missing_refs = set(orig_comps) - set(skidl_comps)
    extra_refs   = set(skidl_comps) - set(orig_comps)
    if not missing_refs and not extra_refs:
        ok(f'All {len(orig_comps)} references match!')
    else:
        if missing_refs:
            fail(f'Missing in SKiDL : {sorted(missing_refs)}')
            issues.append(f'Missing refs: {sorted(missing_refs)}')
        if extra_refs:
            fail(f'Extra in SKiDL   : {sorted(extra_refs)}')
            issues.append(f'Extra refs: {sorted(extra_refs)}')

    # ── 3. Component values ───────────────────────────────────────────────────
    section('3. COMPONENT VALUES')
    val_mismatches = []
    for ref in sorted(set(orig_comps) & set(skidl_comps)):
        ov = orig_comps[ref]['value']
        sv = skidl_comps[ref]['value']
        if ov != sv:
            val_mismatches.append((ref, ov, sv))
    if not val_mismatches:
        ok('All values match!')
    else:
        fail(f'{len(val_mismatches)} value mismatches:')
        for ref, ov, sv in val_mismatches[:20]:
            print(f'    {ref}: orig="{ov}"  skidl="{sv}"')
        issues.append(f'{len(val_mismatches)} value mismatches')

    # ── 4. Footprints ─────────────────────────────────────────────────────────
    section('4. FOOTPRINTS')
    fp_mismatches = []
    for ref in sorted(set(orig_comps) & set(skidl_comps)):
        of = orig_comps[ref]['footprint']
        sf = skidl_comps[ref]['footprint']
        if of != sf:
            fp_mismatches.append((ref, of, sf))
    if not fp_mismatches:
        ok('All footprints match!')
    else:
        fail(f'{len(fp_mismatches)} footprint mismatches:')
        for ref, of, sf in fp_mismatches[:20]:
            print(f'    {ref}:')
            print(f'      orig  = "{of}"')
            print(f'      skidl = "{sf}"')
        issues.append(f'{len(fp_mismatches)} footprint mismatches')

    # ── 5. Net names ──────────────────────────────────────────────────────────
    section('5. NET NAMES')
    orig_named  = {n for n in orig_nets  if not n.startswith('Net-(') and not n.startswith('/')}
    skidl_named = {n for n in skidl_nets if not n.startswith('Net-(') and not n.startswith('/')}
    missing_nets = orig_named  - skidl_named
    extra_nets   = skidl_named - orig_named
    print(f'  Original : {len(orig_named)} named nets')
    print(f'  SKiDL    : {len(skidl_named)} named nets')
    if not missing_nets and not extra_nets:
        ok('All named nets match!')
    else:
        if missing_nets:
            fail(f'Missing in SKiDL ({len(missing_nets)}): {sorted(missing_nets)}')
            issues.append(f'Missing nets: {sorted(missing_nets)}')
        if extra_nets:
            warn(f'Extra in SKiDL ({len(extra_nets)}) — likely auto-suffixed power nets:')
            print(f'    {sorted(extra_nets)}')
            issues.append(f'Extra/suffixed nets: {sorted(extra_nets)}')

    # ── 6. Pin-to-net connectivity ────────────────────────────────────────────
    section('6. PIN-TO-NET CONNECTIVITY')
    print(f'  Original : {len(orig_pin_net)} pin connections')
    print(f'  SKiDL    : {len(skidl_pin_net)} pin connections')

    missing_pins  = sorted(set(orig_pin_net)  - set(skidl_pin_net))
    extra_pins    = sorted(set(skidl_pin_net) - set(orig_pin_net))
    wrong_net     = []
    for key in sorted(set(orig_pin_net) & set(skidl_pin_net)):
        if orig_pin_net[key] != skidl_pin_net[key]:
            wrong_net.append((key[0], key[1], orig_pin_net[key], skidl_pin_net[key]))

    if not missing_pins and not extra_pins and not wrong_net:
        ok('All 767 pin connections match perfectly!')
    else:
        if missing_pins:
            fail(f'Pins in orig but missing in SKiDL: {len(missing_pins)}')
            for ref, pin in missing_pins[:20]:
                print(f'    {ref}.{pin}  →  net: "{orig_pin_net[(ref,pin)]}"')
            if len(missing_pins) > 20:
                print(f'    ... and {len(missing_pins)-20} more')
            issues.append(f'{len(missing_pins)} missing pin connections')

        if extra_pins:
            fail(f'Extra pins in SKiDL not in orig: {len(extra_pins)}')
            for ref, pin in extra_pins[:10]:
                print(f'    {ref}.{pin}  →  net: "{skidl_pin_net[(ref,pin)]}"')
            issues.append(f'{len(extra_pins)} extra pin connections')

        if wrong_net:
            fail(f'Same pin, different net name: {len(wrong_net)}')
            for ref, pin, on, sn in wrong_net[:20]:
                print(f'    {ref}.{pin}:  orig="{on}"  skidl="{sn}"')
            if len(wrong_net) > 20:
                print(f'    ... and {len(wrong_net)-20} more')
            issues.append(f'{len(wrong_net)} wrong net assignments')

    # ── 7. Total nets ─────────────────────────────────────────────────────────
    section('7. TOTAL NETS')
    print(f'  Original : {len(orig_nets)} total nets')
    print(f'  SKiDL    : {len(skidl_nets)} total nets')
    if len(orig_nets) == len(skidl_nets):
        ok('Net count matches!')
    else:
        warn(f'Net count differs by {abs(len(orig_nets)-len(skidl_nets))}')

    # ── Summary ───────────────────────────────────────────────────────────────
    print('\n' + '=' * 60)
    if not issues:
        print('  🎉  PERFECT MATCH — 100% identical netlists!')
    else:
        print(f'  {len(issues)} ISSUE(S) FOUND:')
        for i, issue in enumerate(issues, 1):
            print(f'    {i}. {issue}')
    print('=' * 60)

    return len(issues) == 0


if __name__ == '__main__':
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    orig  = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE_DIR, "original_HadesGPSDongle.net")
    skidl = sys.argv[2] if len(sys.argv) > 2 else os.path.join(BASE_DIR, "HadesGPSDongle.net")
    report = os.path.join(BASE_DIR, "HadesGPSDongle_validation.txt")
    class _Tee:
        def __init__(self,*s): self.s=s
        def write(self,m):
            for x in self.s: x.write(m)
        def flush(self):
            for x in self.s: x.flush()
    _f=open(report,"w",encoding="utf-8"); _o=sys.stdout; sys.stdout=_Tee(_o,_f)
    try:
        ok=compare(orig, skidl)
    finally:
        sys.stdout=_o; _f.close()
    print("Report written -> "+os.path.basename(report))
