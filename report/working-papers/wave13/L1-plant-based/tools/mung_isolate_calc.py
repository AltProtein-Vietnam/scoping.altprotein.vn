"""Raw-material cost of a mung bean protein isolate made from imported beans (our calculation).

Inputs:
- Mung bean price, HS 0713.31 (mung and black gram beans) into Vietnam:
  * partner-reported exports to Vietnam (mirror, FOB): USD 0.666/kg (2023, 129,380 t), 0.696/kg (2024, 185,470 t),
    0.811/kg (2025, 167,108 t). UN Comtrade public preview API, queried 2026-10-15 (raw/comtrade_mirror_071331_*.json).
  * Vietnam-reported imports (CIF), 2023: USD 138.3 million, 103,835 t with weight estimated by Comtrade, USD 1.33/kg
    (FORM-08; raw/comtrade_vn_071331_2023.json). Vietnam has not reported 2024 or 2025.
- Protein in mung bean seed: 23.4 g per 100 g (Vietnamese food composition table, code 3010, DIE-12).
- Isolate purity: 85% protein (FDA GRN 000684 specification is more than 80% on a dry basis; SLP source).
- Protein recovery into the isolate: 60 to 80% (our assumption; not sourced; wet extraction and acid precipitation).
- Benchmarks: Chinese pea protein USD 2 to 3/kg; Western pea protein USD 6.75 to 8.50/kg (TPP-05);
  egg white powder from India USD 5.90/kg (ch16, BUY-02).
Excludes processing, energy, water, labour, capital and any credit for the starch and fibre co-products.
"""
prices = {"mirror FOB 2023": 0.666, "mirror FOB 2024": 0.696, "mirror FOB 2025": 0.811, "VN-reported CIF 2023": 1.331}
protein = 0.234
purity = 0.85
for name, p in prices.items():
    for rec in (0.6, 0.8):
        kg_protein_per_kg_bean = protein * rec
        cost_per_kg_protein = p / kg_protein_per_kg_bean
        cost_per_kg_isolate = cost_per_kg_protein * purity
        beans_per_kg_isolate = purity / kg_protein_per_kg_bean
        print(f"{name:22s} USD {p:.3f}/kg, recovery {rec:.0%}: {beans_per_kg_isolate:4.1f} kg beans per kg isolate; "
              f"raw material USD {cost_per_kg_protein:4.2f}/kg protein, USD {cost_per_kg_isolate:4.2f}/kg isolate")
print("Benchmarks: Chinese pea USD 2 to 3/kg; Western pea USD 6.75 to 8.50/kg (TPP-05); Indian egg white powder USD 5.90/kg (ch16)")
