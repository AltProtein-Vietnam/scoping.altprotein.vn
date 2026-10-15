"""Raw-material cost of protein recovered from broken rice (our calculation).

Inputs:
- Broken rice price: VFA export quote for fragrant 100% broken rice, USD 368 to 372 per t (FS-26, 19 Sep 2026);
  domestic An Giang fragrant broken rice 8,500 to 8,600 VND/kg (FS-26), converted at 26,000 VND per USD.
- Protein in milled rice: 7.9 g per 100 g, ordinary polished rice, Vietnamese food composition table code 1004 (DIE-12).
  The NTU thesis (SLP source) reports broken kernels slightly higher in protein than whole kernels, so 7.9% is a
  conservative-to-central figure; we also show 9%.
- Recovery and purity: Viscozyme-assisted extraction of VD20 broken rice, about 55% protein recovery at
  76 to 77% protein, 36 h at about 53 degC (Can Tho University and Nguyen Tat Thanh University, 2026; SLP source).
- Benchmark: Chinese pea protein USD 2 to 3 per kg (TPP-05).
No processing, energy, enzyme, labour or capital cost is included: this is the raw-material floor only.
"""
prices_usd_per_t = {"export quote low": 368, "export quote high": 372,
                    "domestic low": 8500 * 1000 / 26000, "domestic high": 8600 * 1000 / 26000}
protein_shares = [0.079, 0.09]
recovery = 0.55
purity = 0.765
for name, p in prices_usd_per_t.items():
    for ps in protein_shares:
        kg_protein = 1000 * ps * recovery
        kg_product = kg_protein / purity
        print(f"{name:18s} price USD {p:6.1f}/t, protein {ps*100:.1f}%: "
              f"{kg_protein:5.1f} kg protein/t, {kg_product:5.1f} kg product/t, "
              f"raw material USD {p/kg_protein:5.2f} per kg protein, USD {p/kg_product:5.2f} per kg of 76.5% product, "
              f"carbohydrate-rich residue {1000-kg_product:6.1f} kg/t")
print("Benchmark: Chinese pea protein USD 2 to 3 per kg (TPP-05)")
