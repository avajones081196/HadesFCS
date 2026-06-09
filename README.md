# HadesFCS — SKiDL Netlists

SKiDL reproductions of the **HadesFCS** boards, ported from `Ava_pms67_HadesFCS_SKiDL`.
Each of the 5 components has its own self-contained folder.

## Components
`HadesGPSDongle`, `HadesMicro`, `HadesMicroJLCPCB`, `HadesNT`, `Hades`

## Layout of every component folder `<C>/`

| File | Purpose |
|------|---------|
| `<C>.py`                  | SKiDL script — generates the netlist (`generate_netlist()` → `<C>.net`) and runs ERC |
| `<C>_sklib.py`            | SKiDL parts library used by the script |
| `<C>.net`                 | Generated KiCad netlist |
| `<C>.log` / `<C>.erc`     | Generation log + electrical-rule-check report |
| `original_<C>.net`        | Reference (original) netlist |
| `validation.py`           | Compares `<C>.net` against `original_<C>.net` |
| `<C>_validation.txt`      | Validation report |

## Run a component
```
cd <C>
python <C>.py        # generates <C>.net (+ .erc, .log)
python validation.py # writes <C>_validation.txt
```

## Result
All 5 components were generated and validated: **🎉 PERFECT MATCH — 100% identical** to
their reference netlists.
