"""L7 (wave 13): run the EU soy-dependency back-calculation logic on Vietnam numbers
the study already holds. Standard library only. All outputs are our calculation.

Inputs (study data files and sources):
- 2025 soybean meal fed 7.2 Mt; 2035 S-BASE 9.467, S-EFF 8.08, S-ALT 9.007 Mt (data/balance_outputs.csv)
- soybean meal crude protein 46% (balance model basis); beans 36% protein (BLA-231 assumption)
- meal extraction 0.78 t meal per t beans (BLA-047)
- food soybean use 540 kt (2025, PCV-014 from MAC-04); 98.4% of soybeans imported (ch01, MAC-04)
- domestic soybean 42.5 kt (2025, midpoint of 42 to 43 kt, MAC-04); area peak 205 kha (2010, AQF-20);
  yields 2.0 t/ha (ministry scheme, ch22 via AQF-20) and 2.5 t/ha (VINASOY 05 at Cu Jut, AIB-06)
- D-BENCH and D-STRETCH meat protein displaced in 2035: 2.35 and 9.25 kt (data/demand_outputs.csv);
  about 4.5 t soybean meal avoided per t meat protein displaced (ch22, F4 factors)
- EU reference: 15.1 Mt soy protein imports (2025) to 12.1 Mt target (2035); BAU 14.62 Mt (PPE-03)
- 2023 Vietnam-reported soybean import unit values by origin (SEC-05 raw extract in
  working-papers/wave11/L3-security-exposures/raw/ct_vn_imports_2023.json)
"""
import json, os

CP_SBM, CP_BEAN, EXTR = 0.46, 0.36, 0.78
sbm = {"2025": 7.2, "S-BASE 2035": 9.467, "S-EFF 2035": 8.08, "S-ALT 2035": 9.007}
food_beans_kt, import_share = 540.0, 0.984
dom_beans_2025_kt = 42.5

feed_prot_2025 = sbm["2025"] * CP_SBM
food_prot_2025 = food_beans_kt / 1000 * CP_BEAN * import_share
tot_2025 = feed_prot_2025 + food_prot_2025
target_2035 = 0.8 * tot_2025
feed_prot_2035 = sbm["S-BASE 2035"] * CP_SBM
tot_2035 = feed_prot_2035 + food_prot_2025  # food soy held at 2025 level (simplification)
gap = tot_2035 - target_2035
print("Imported soy protein, Mt protein")
print(f"  2025: feed {feed_prot_2025:.3f} + food {food_prot_2025:.3f} = {tot_2025:.3f}; food share {food_prot_2025/tot_2025:.1%}")
print(f"  EU-style target for 2035 (20% below 2025): {target_2035:.3f}")
print(f"  S-BASE 2035 trend: {tot_2035:.3f} ({tot_2035/tot_2025-1:+.1%} on 2025)")
print(f"  Cut needed against trend: {gap:.3f} Mt protein = {gap/CP_SBM:.2f} Mt soybean-meal equivalent")
print("EU reference: BAU change 2025 to 2035 = {:+.1%} (labelled -1% in the report figure)".format(14.62/15.1-1))

levers = {}
for label, area_kha, yld in [("domestic soy, 2010 peak area at 2.0 t/ha", 205, 2.0),
                             ("domestic soy, 2010 peak area at 2.5 t/ha", 205, 2.5),
                             ("domestic soy, 300 kha proposal at 2.5 t/ha", 300, 2.5)]:
    beans_kt = area_kha * yld
    net_prot = (beans_kt - dom_beans_2025_kt) / 1000 * CP_BEAN
    levers[label] = net_prot
    print(f"  {label}: {beans_kt:.0f} kt beans = {beans_kt/food_beans_kt:.0%} of 2025 food soy use; "
          f"net extra protein {net_prot:.3f} Mt = {net_prot/gap:.1%} of the cut; "
          f"as meal-equivalent {beans_kt*EXTR/1000:.2f} Mt = {beans_kt*EXTR/1000/sbm['S-BASE 2035']:.1%} of 2035 trend meal")
for label, kt in [("D-BENCH food routes", 2.35), ("D-STRETCH food routes", 9.25)]:
    sbm_saved = kt * 4.5 / 1000
    levers[label] = sbm_saved * CP_SBM
    print(f"  {label}: {sbm_saved*1000:.1f} kt soybean meal = {sbm_saved*CP_SBM:.4f} Mt protein = {sbm_saved*CP_SBM/gap:.1%} of the cut")
for label in ("S-EFF 2035", "S-ALT 2035"):
    d = sbm["S-BASE 2035"] - sbm[label]
    levers[label] = d * CP_SBM
    print(f"  {label} (balance model): {d:.3f} Mt soybean meal = {d*CP_SBM:.3f} Mt protein = {d*CP_SBM/gap:.1%} of the cut")

# soybean import unit values by origin, 2023 (USD per t, CIF, Vietnam-reported)
p = os.path.join(os.path.dirname(__file__), "..", "..", "..", "wave11", "L3-security-exposures", "raw", "ct_vn_imports_2023.json")
d = json.load(open(os.path.normpath(p)))
rows = d.get("data", d) if isinstance(d, dict) else d
names = {0: "World", 76: "Brazil", 124: "Canada", 842: "United States"}
print("Soybean (HS 1201) import unit values 2023, USD per t:")
for r in rows:
    if str(r.get("cmdCode")) == "1201" and r.get("partnerCode") in names:
        uv = r["primaryValue"] / r["netWgt"] * 1000
        print(f"  {names[r['partnerCode']]}: {uv:.0f} (= VND {uv*26:,.0f} per kg at 26,000 VND per USD); value USD {r['primaryValue']/1e6:.1f} M")
# domestic price 25,000 to 30,000 VND per kg (2024, AQF-20)
for v in (25000, 30000):
    print(f"  domestic {v:,} VND/kg = USD {v/26:.0f} per t; ratio to Canadian 2023 unit value {v/26/685.7:.2f}")
