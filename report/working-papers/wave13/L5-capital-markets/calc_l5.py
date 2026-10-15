"""Arithmetic for line L5 (wave 13). Conversions at 26,000 VND per USD (study convention)."""
FX = 26000
items = {
    "Leasing small-value threshold, VND 100 million": 100e6,
    "Leasing small-value threshold in draft, VND 400 million": 400e6,
    "Leasing balance end Q1 2025, VND 40,700 billion": 40700e9,
    "Production-line leases 30 June 2025, VND 6,900 billion": 6900e9,
    "BIDV SCFast 2026 package, VND 15,000 billion": 15000e9,
    "BIDV unsecured distributor limit, VND 10 billion": 10e9,
    "HCMC guarantee fund charter capital, VND 227,903,438,870": 227903438870,
    "HCMC fund per-customer cap (15% of charter capital)": 0.15 * 227903438870,
    "HCMC fund total guarantee cap (3 x charter capital)": 3 * 227903438870,
    "Decree 57/2018 processing cap, VND 15 billion": 15e9,
    "Decree 57/2018 machinery cap, VND 5 billion": 5e9,
}
for k, v in items.items():
    print(f"{k}: VND {v/1e9:,.1f} billion = USD {v/FX/1e6:,.2f} million")
print("T1 working capital USD 0.6 to 3.5 million = VND", 0.6e6*FX/1e9, "to", 3.5e6*FX/1e9, "billion")
print("Factoring share of credit: 16,000 / 17,000,000 =", round(16000/17000000*100, 3), "%")
# Decree 57/2018 Art. 11 condition: processed value at least 1.5 times raw value.
# T1 inputs from the package: landed Chinese textured protein USD 1.29 to 1.38 per kg;
# breakeven delivered flour USD 700 to 940 per t (1 t/h line at 70%).
for p in (1.29, 1.38):
    for f in (0.70, 0.94):
        print(f"product USD {p}/kg over flour USD {f}/kg = {p/f:.2f} times (ignores yield loss and other inputs)")
