"""Calculations quoted in L1-meat-imports.md (our calculations). Inputs and their sources are noted inline."""
FX = 26000  # VND per USD, package convention

# Import shares of supply, 2025
pork_imp = 183.4            # kt, customs (MIM-06)
pork_live = 5389.2          # kt live weight (MAC-14)
dress_pork = 0.723          # BLA-030
poultry_imp = 978.3 * 0.3677  # kt, 36.77% of 978.3 kt (MIM-05)
poultry_live = 2602.0       # kt live weight (MAC-14)
dress_poultry = 0.70        # BLA-031
bovine_dom = 321.5          # kt, OECD-FAO 2025 production (QNT-01, BLA-035)
buffalo_imp = 978.3 * 0.1768  # kt (MIM-05)
print('pork import share', round(pork_imp / (pork_live * dress_pork + pork_imp), 3))
print('poultry import share', round(poultry_imp / (poultry_live * dress_poultry + poultry_imp), 3))
print('bovine import share, buffalo only', round(buffalo_imp / (bovine_dom + buffalo_imp), 3))
dom_meat = pork_live * dress_pork + poultry_live * dress_poultry + bovine_dom
print('all meat imports share by weight', round(978.3 / (dom_meat + 978.3), 3))
print('USDA shares', round(151 / 4073, 3), round(175 / 1595, 3), round(135 / 420, 3))  # MIM-03

# Prices
for usd_t in (2273, 1638):  # MIM-06, MIM-09
    vnd = usd_t * FX / 1000
    lo, hi = 62000 / dress_pork, 69000 / dress_pork  # live pig, MIM-07
    print('pork import VND/kg', round(vnd), 'gap', round(1 - vnd / lo, 2), 'to', round(1 - vnd / hi, 2))
print('India H1 2026 USD/kg', round(462.8 / 108.2, 2))  # MIM-26
vn, bra, rus, usa, eu = 3714.13, 1306.20, 1909.53, 2137.14, 2256.22  # OECD PP pigmeat 2024, MIM-15
print('VN pig price ratios', [round(vn / x, 2) for x in (bra, rus, usa, eu)])
print('VN / India bovine', round(6861.88 / 1352.53, 1))
print('Brazil pig BT check, USD million', round(520.7558 * (5364.3 - 3976.5071) / 1000, 1))  # equals OECD BT USD 722.7 million

# Protein scale
meat_prot = 978.3 * 0.15  # DMA-001
print('imported meat protein kt', round(meat_prot, 1))
print('benchmark displaced share', round(2.35 / meat_prot, 3))  # DMO-0273
mp = 108786 * 0.362 + 34132 * 0.263  # MIM-01 tonnes; MIM-27 protein
print('milk powder protein t 2023', round(mp), 'R6 share', round(1290 / mp, 3))  # DMO-0267
print('Russia pork kt', round(0.4844 * 183.4, 1), 'share of meat imports', round(0.4844 * 183.4 / 978.3, 3))
