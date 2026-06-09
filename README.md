# 🛩️ HadesFCS — SKiDL Netlist Reconstruction

> Reproducing the schematics of the open-source [**HadesFCS**](https://github.com/pms67/HadesFCS) flight-control hardware by pms67 as Python programs using [SKiDL](https://github.com/devbisme/skidl) — with an automated netlist comparison against the originals.

---

## 🚀 Project Overview

**[HadesFCS](https://github.com/pms67/HadesFCS)** is an open-source flight-control-system hardware project by [pms67](https://github.com/pms67), distributed as KiCad designs across several boards.

This project takes those boards and **reconstructs each schematic programmatically** with **[SKiDL](https://github.com/devbisme/skidl)** — a Python module that describes electronic circuits in code and emits a standard KiCad netlist. Each generated netlist is then **compared, net-for-net, against the original** to prove the reconstruction is electrically identical.

**The goal:** rebuild every HadesFCS board from code — components, values, footprints and connections — and verify each one matches the original netlist exactly.

Each of the 5 components lives in its own self-contained folder; every script derives its paths from its own location, so any folder runs unchanged on macOS, Windows, or a freshly cloned checkout.

### Components

`Hades` · `HadesGPSDongle` · `HadesMicro` · `HadesMicroJLCPCB` · `HadesNT`

---

## 📁 Repository Structure

Every component folder is self-contained and follows the same naming convention:

```
HadesFCS/
│
├── Hades/                       ← example component folder
│   ├── Hades.py                 ← SKiDL script: defines parts + nets, runs ERC, emits the netlist
│   ├── Hades_sklib.py           ← SKiDL parts library used by the script
│   ├── Hades.net                ← generated KiCad netlist (output)
│   ├── Hades.log                ← generation / ERC run log (summary)
│   ├── Hades.erc                ← electrical-rule-check report
│   ├── original_Hades.net       ← reference (original) netlist
│   ├── validation.py            ← compares the generated netlist vs the reference
│   └── Hades_validation.txt     ← validation report (auto-generated)
│
├── HadesGPSDongle/
├── HadesMicro/
├── HadesMicroJLCPCB/
├── HadesNT/
│
└── README.md                    ← this file
```

### 📌 Naming convention (per folder `<C>/`)

| File | Purpose |
|------|---------|
| `<C>.py` | SKiDL script — `generate_netlist()` writes `<C>.net`; `ERC()` writes `<C>.erc`. |
| `<C>_sklib.py` | SKiDL parts library the script resolves its components from. |
| `<C>.net` | Generated KiCad netlist. |
| `<C>.log` / `<C>.erc` | Generation log + electrical-rule-check report. |
| `original_<C>.net` | The reference netlist (the original board's export). |
| `validation.py` | Compares `<C>.net` against `original_<C>.net`. |
| `<C>_validation.txt` | Auto-generated comparison report. |

---

## 🛠️ Tools & Environment

| Tool | Purpose |
|------|---------|
| **SKiDL** | Describe each circuit in Python and emit a KiCad netlist |
| **Python 3** | Runtime for the generators and the comparison script |

> `validation.py` is **pure Python** (standard library only) — no extra dependencies needed to compare netlists.

---

## 📐 Methodology

### Step 1 — Describe the circuit in SKiDL
`<C>.py` instantiates every component (`Part(...)`) with its reference designator, value and footprint — drawing the part definitions from `<C>_sklib.py` — then wires them together into named nets.

### Step 2 — Generate the netlist
The script ends with `ERC()` (electrical-rule check → `<C>.erc` + `.log`) and `generate_netlist()`, which writes the KiCad netlist `<C>.net` (named after the script).

### Step 3 — Validate against the original
`validation.py` parses both netlists and compares them, writing the full report to `<C>_validation.txt`.

---

## 🔍 Validation Script (`validation.py`)

A self-contained, dependency-free netlist comparator that parses the KiCad netlist format and checks:

1. **Component count** — number of components in each netlist.
2. **Reference designators** — every `ref` matches between original and reconstruction.
3. **Component values** — value string per reference.
4. **Footprints** — footprint per reference.
5. **Net names** — the set of named nets.
6. **Pin-to-net connectivity** — every `(ref, pin)` node on every net.
7. **Total nets** — overall net count, then a PASS/FAIL verdict.

---

## 📊 Results

Every component validated to **🎉 PERFECT MATCH — 100% identical** to its reference netlist: matching component count, reference designators, values, footprints, named nets, and pin-to-net connectivity.

| Component | Components | Named Nets | Total Nets | Pin Connections | Verdict |
|-----------|:----------:|:----------:|:----------:|:---------------:|---------|
| `HadesGPSDongle`   | 27  | 16  | 27  | 84  | 🎉 PERFECT MATCH |
| `HadesMicro`       | 87  | 132 | 161 | 369 | 🎉 PERFECT MATCH |
| `HadesMicroJLCPCB` | 84  | 144 | 175 | 363 | 🎉 PERFECT MATCH |
| `HadesNT`          | 102 | 118 | 144 | 406 | 🎉 PERFECT MATCH |
| `Hades`            | 195 | 270 | 316 | 767 | 🎉 PERFECT MATCH |

---

## 🏃 How to Run

```bash
pip install skidl
cd <C>                # e.g. Hades, HadesGPSDongle, HadesMicro, HadesMicroJLCPCB, HadesNT
python <C>.py         # defines the circuit, runs ERC, writes <C>.net (+ .erc, .log)
python validation.py  # compares <C>.net vs original_<C>.net -> writes the report
```

---

## 🔗 References

- **Original hardware project:** [pms67/HadesFCS](https://github.com/pms67/HadesFCS) — open-source flight control system (the source of every board reconstructed here)
- **SKiDL:** [devbisme/skidl](https://github.com/devbisme/skidl) — Python module for describing circuits and generating netlists

---

## 🙏 Credits

- **[pms67](https://github.com/pms67)** — original HadesFCS design. The original design files belong to their author under their respective license.
- **[SKiDL](https://github.com/devbisme/skidl)** — the Python library used for the netlist reconstruction.
