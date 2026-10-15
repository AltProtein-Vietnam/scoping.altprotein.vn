"""Wave 13 L4 (alternative seafood) calculations. Standard library only.

Inputs come from:
- raw/comtrade_mirror_2025.json and raw/comtrade_mirror_2024.json (UN Comtrade public preview API,
  partner imports from Viet Nam, HS 030499 and 160420; SLS-05)
- raw/comtrade_vn_2023.json (Viet Nam reported trade 2023; SLS-05)
- Huda et al. 2000 (SLS-20): threadfin bream surimi powder at about 5% moisture held 72% protein
- BUY-07: Chinese soy protein isolate landed at USD 1.96 to 2.44 per kg of protein (90% protein)
- Ye et al. 2024 (SLS-07): sensory rejection at 30 to 40% plant/surimi protein substitution
- ASSUMPTION (not sourced, flagged Low): frozen surimi dry matter 20 to 25%
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
NAMES = {156: "China", 392: "Japan", 410: "Korea", 764: "Thailand", 842: "United States"}


def load(name):
    with open(os.path.join(RAW, name)) as f:
        return json.load(f)["data"]


print("1. Mirror imports from Viet Nam (partner-reported), HS 030499 and 160420")
rows = []
for y in (2024, 2025):
    for r in load(f"comtrade_mirror_{y}.json"):
        rows.append((y, NAMES[r["reporterCode"]], r["cmdCode"], r["primaryValue"], r["netWgt"]))
for y, c, hs, v, w in sorted(rows):
    print(f"  {y} {c:14s} {hs} USD {v/1e6:6.2f} m  {w/1e3:9.1f} t  USD {v/w:5.2f}/kg")

for y in (2024, 2025):
    sel = [r for r in rows if r[0] == y and r[2] == "030499" and r[1] in ("Korea", "Thailand", "China")]
    v = sum(r[3] for r in sel)
    w = sum(r[4] for r in sel)
    print(f"  {y} Korea+Thailand+China HS 030499: USD {v/1e6:.1f} m, {w/1e3:.1f} t, USD {v/w:.2f}/kg")

print("\n2. Viet Nam reported 2023 exports")
for r in load("comtrade_vn_2023.json"):
    if r["flowCode"] == "X":
        print(f"  {r['cmdCode']} USD {r['primaryValue']/1e6:.1f} m {r['netWgt']/1e3:.1f} t USD {r['primaryValue']/r['netWgt']:.2f}/kg")

print("\n3. Cost per kg of protein: tropical surimi against soy protein isolate (our calculation)")
powder_protein, powder_moisture = 0.72, 0.05
protein_in_dm = powder_protein / (1 - powder_moisture)
print(f"  protein share of surimi dry matter (Huda 2000): {protein_in_dm:.3f}")
dm_low, dm_high = 0.20, 0.25  # assumption
p_low, p_high = protein_in_dm * dm_low, protein_in_dm * dm_high
print(f"  frozen surimi protein at 20 to 25% dry matter (assumption): {p_low:.3f} to {p_high:.3f}")
uv_low, uv_high = 1.67, 2.24  # Korea and Thailand 2025 unit values, HS 030499
cpp_low, cpp_high = uv_low / p_high, uv_high / p_low
print(f"  surimi USD per kg protein: {cpp_low:.1f} to {cpp_high:.1f}")
spi_low, spi_high = 1.96, 2.44  # BUY-07, per kg protein landed
print(f"  soy isolate USD per kg protein: {spi_low} to {spi_high}")
print(f"  ratio surimi/isolate: {cpp_low/spi_high:.1f} to {cpp_high/spi_low:.1f}")
for s in (0.10, 0.20, 0.30):
    save_low = s * (1 - spi_high / cpp_low)
    save_high = s * (1 - spi_low / cpp_high)
    print(f"  substitution {s:.0%}: protein-cost saving {save_low:.1%} to {save_high:.1%}")

print("\n4. Pangasius price gap to cultivated cost (our calculation)")
fx = 26000
fg_low, fg_high = 26500 / fx, 30000 / fx
print(f"  pangasius farm gate USD {fg_low:.2f} to {fg_high:.2f}/kg (FM-11, Dec 2024)")
rt_low, rt_high = 100000 / fx, 116800 / fx
print(f"  pangasius retail fillet USD {rt_low:.2f} to {rt_high:.2f}/kg (DPP-008, DPP-009)")
print(f"  Humbird USD 37 to 51/kg wet cells = {37/fg_high:.0f} to {51/fg_low:.0f} x farm gate; {37/rt_high:.0f} to {51/rt_low:.0f} x retail fillet")
