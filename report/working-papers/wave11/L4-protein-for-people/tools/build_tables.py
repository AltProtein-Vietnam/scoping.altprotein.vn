"""Build the L4 tables from the FAOSTAT FBS extract for Viet Nam and the USDA feed-ingredient table.

Inputs (all saved in ../raw):
  faostat_fbs_vnm_2010_2023.csv   FAOSTAT Food Balances (2010-), bulk file FoodBalanceSheets_E_Asia.zip (DIE-07), area 237.
  usda_gain_vm2026-0012_feed_tables.txt  USDA GAIN Grain and Feed Annual VM2026-0012, Table 2 (MAC-01 / FS-23).
Outputs (in ..):
  data_protein_supply_by_source.csv, data_self_sufficiency_by_food.csv, data_animal_protein_import_reliance.csv
All ratios and shares are our calculation. Standard library only.
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..')
rows = list(csv.DictReader(open(os.path.join(OUT, 'raw', 'faostat_fbs_vnm_2010_2023.csv'))))
IDX = {}
for r in rows:
    IDX[(r['Item'], r['Element Code'])] = r

def val(item, el, yr):
    r = IDX.get((item, el))
    if not r:
        return None
    v = r.get('Y%d' % yr, '')
    return float(v) if v not in ('', None) else None

def z(x):
    return 0.0 if x is None else x

YEARS = [2010, 2015, 2020, 2023]
pop = {y: val('Population', '511', y) for y in YEARS}  # thousand people

# ---------- 1. protein supply by source ----------
GROUPS = [
    # (item_group label, [FBS items], plant/animal)
    ('Rice', ['Rice and products'], 'plant'),
    ('Wheat', ['Wheat and products'], 'plant'),
    ('Maize', ['Maize and products'], 'plant'),
    ('Other cereals', ['Barley and products', 'Rye and products', 'Oats', 'Millet and products', 'Sorghum and products', 'Cereals, other'], 'plant'),
    ('Soybeans (tofu, soy milk and other soy foods)', ['Soyabeans'], 'plant'),
    ('Pulses (beans, peas, other)', ['Beans', 'Peas', 'Pulses, Other and products'], 'plant'),
    ('Groundnuts', ['Groundnuts'], 'plant'),
    ('Tree nuts', ['Nuts and products'], 'plant'),
    ('Other oilcrops (sesame, coconut and others)', ['Sunflower seed', 'Rape and Mustardseed', 'Cottonseed', 'Coconuts - Incl Copra', 'Sesame seed', 'Palm kernels', 'Olives (including preserved)', 'Oilcrops, Other'], 'plant'),
    ('Vegetables', ['Tomatoes and products', 'Onions', 'Vegetables, other'], 'plant'),
    ('Fruits', ['Oranges, Mandarines', 'Lemons, Limes and products', 'Grapefruit and products', 'Citrus, Other', 'Bananas', 'Plantains', 'Apples and products', 'Pineapples and products', 'Dates', 'Grapes and products (excl wine)', 'Fruits, other'], 'plant'),
    ('Starchy roots', ['Potatoes and products', 'Cassava and products', 'Sweet potatoes', 'Roots, Other', 'Yams'], 'plant'),
    ('Other plant foods (sugar, spices, stimulants, drinks, aquatic plants)', None, 'plant'),
    ('Pigmeat', ['Pigmeat'], 'animal'),
    ('Poultry meat', ['Poultry Meat'], 'animal'),
    ('Bovine meat (beef and buffalo)', ['Bovine Meat'], 'animal'),
    ('Mutton, goat and other meat', ['Mutton & Goat Meat', 'Meat, Other'], 'animal'),
    ('Edible offal', ['Offals, Edible'], 'animal'),
    ('Eggs', ['Eggs'], 'animal'),
    ('Milk and dairy (excluding butter)', ['Milk - Excluding Butter'], 'animal'),
    ('Fish and seafood', ['Freshwater Fish', 'Demersal Fish', 'Pelagic Fish', 'Marine Fish, Other', 'Crustaceans', 'Cephalopods', 'Molluscs, Other', 'Aquatic Animals, Others'], 'animal'),
    ('Other animal products (animal fats, butter, honey, infant food)', None, 'animal'),
]
AGG = {'Population', 'Grand Total', 'Vegetal Products', 'Animal Products', 'Cereals - Excluding Beer', 'Starchy Roots', 'Sugar Crops', 'Sugar & Sweeteners', 'Pulses', 'Treenuts', 'Oilcrops', 'Vegetable Oils', 'Vegetables', 'Fruits - Excluding Wine', 'Stimulants', 'Spices', 'Alcoholic Beverages', 'Miscellaneous', 'Meat', 'Offals', 'Animal fats', 'Milk - Excluding Butter', 'Eggs', 'Fish, Seafood', 'Aquatic Products, Other'}
# leaf items with element 674
leaf = {}
for r in rows:
    if r['Element Code'] == '674':
        leaf.setdefault(r['Item'], r)
# Item names that appear both as aggregate and leaf: 'Eggs', 'Milk - Excluding Butter', 'Miscellaneous'. Item codes separate them.
leaf_by_code = {r['Item Code']: r for r in rows if r['Element Code'] == '674'}
AGG_CODES = {'2901', '2903', '2941', '2905', '2907', '2908', '2909', '2911', '2912', '2913', '2914', '2918', '2919', '2922', '2923', '2924', '2928', '2943', '2945', '2946', '2948', '2949', '2960', '2961'}
leaf_codes = {c: r for c, r in leaf_by_code.items() if c not in AGG_CODES}

def prot_item(name, yr):
    for c, r in leaf_codes.items():
        if r['Item'] == name:
            v = r['Y%d' % yr]
            return float(v) if v else 0.0
    return 0.0

ps_rows = []
for yr in YEARS:
    total = val('Grand Total', '674', yr)
    animal_total = float(leaf_by_code['2941']['Y%d' % yr])
    plant_total = float(leaf_by_code['2903']['Y%d' % yr])
    used = set()
    out = []
    for label, items, kind in GROUPS:
        if items is None:
            continue
        g = sum(prot_item(i, yr) for i in items)
        used.update(items)
        out.append((label, kind, g))
    # residual groups
    plant_named = sum(g for l, k, g in out if k == 'plant')
    animal_named = sum(g for l, k, g in out if k == 'animal')
    out.insert([l for l, _, _ in GROUPS].index('Other plant foods (sugar, spices, stimulants, drinks, aquatic plants)'), ('Other plant foods (sugar, spices, stimulants, drinks, aquatic plants)', 'plant', plant_total - plant_named))
    out.append(('Other animal products (animal fats, butter, honey, infant food)', 'animal', animal_total - animal_named))
    for label, kind, g in out:
        ps_rows.append([yr, label, kind, round(g, 2), round(100 * g / total, 1)])
    ps_rows.append([yr, 'All plant foods', 'plant total', round(plant_total, 2), round(100 * plant_total / total, 1)])
    ps_rows.append([yr, 'All animal foods', 'animal total', round(animal_total, 2), round(100 * animal_total / total, 1)])
    ps_rows.append([yr, 'All foods', 'total', round(total, 2), 100.0])

with open(os.path.join(OUT, 'data_protein_supply_by_source.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['year', 'item_group', 'protein_g_per_person_day', 'share_of_total', 'plant_or_animal', 'source_ids', 'evidence_label', 'confidence', 'notes'])
    for yr, label, kind, g, sh in ps_rows:
        note = 'FAOSTAT Food Balances (2010-), element 674 (protein supply quantity, g per capita per day); share of total is our calculation. Supply available for consumption, not intake.'
        if label.startswith('Other plant') or label.startswith('Other animal'):
            note += ' Residual: group total minus the named groups (our calculation).'
        if label == 'Milk and dairy (excluding butter)':
            note += ' The FAO milk series swings between years through residual and trade adjustments (DG-175).'
        if label == 'Eggs':
            note += ' FAO egg supply is probably too low against NSO egg output (DG-174).'
        w.writerow([yr, label, g, sh, kind, 'DIE-07', 'VN-direct', 'High', note])

# ---------- 2. self-sufficiency by food ----------
FOODS = [
    ('Rice', 'Rice and products', 'paddy equivalent (FBS production equals paddy output)'),
    ('Wheat', 'Wheat and products', 'grain equivalent'),
    ('Maize', 'Maize and products', 'grain equivalent'),
    ('Soybeans', 'Soyabeans', 'beans; excludes soybean meal, which FBS does not carry'),
    ('Pulses', 'Pulses', 'dry beans and peas'),
    ('Groundnuts', 'Groundnuts', 'shelled equivalent'),
    ('Vegetables', 'Vegetables', 'fresh weight'),
    ('Pigmeat', 'Pigmeat', 'carcass weight'),
    ('Poultry meat', 'Poultry Meat', 'carcass weight'),
    ('Bovine meat (beef and buffalo)', 'Bovine Meat', 'carcass weight; meat from imported live cattle counts as domestic production'),
    ('Edible offal', 'Offals, Edible', 'product weight'),
    ('All meat (excluding offal)', 'Meat', 'carcass weight'),
    ('Eggs', 'Eggs', 'shell weight'),
    ('Milk and dairy (excluding butter)', 'Milk - Excluding Butter', 'fresh milk equivalent'),
    ('Fish and seafood (all)', 'Fish, Seafood', 'live weight'),
    ('Freshwater fish', 'Freshwater Fish', 'live weight'),
    ('Marine fish (pelagic, demersal, other)', ['Pelagic Fish', 'Demersal Fish', 'Marine Fish, Other'], 'live weight'),
    ('Crustaceans', 'Crustaceans', 'live weight'),
    ('Cephalopods and molluscs', ['Cephalopods', 'Molluscs, Other'], 'live weight'),
]
# For 'Offals, Edible' leaf and 'Eggs' leaf, element rows are keyed by item name; the leaf and aggregate share the same values here.
def sval(item, el, yr):
    if isinstance(item, list):
        vals = [val(i, el, yr) for i in item]
        return None if all(v is None for v in vals) else sum(z(v) for v in vals)
    return val(item, el, yr)

ss_rows = []
for yr in YEARS:
    for label, item, basis in FOODS:
        P, I, E, DS, ST, FOOD, FEED = [sval(item, el, yr) for el in ('5511', '5611', '5911', '5301', '5072', '5142', '5521')]
        P, I, E = z(P), z(I), z(E)
        base = P + I - E
        idr = 100 * I / base if base > 0 else None
        ssr = 100 * P / base if base > 0 else None
        ss_rows.append([yr, label, round(P), round(I), round(E), round(z(DS)), round(z(FOOD)), round(z(FEED)), None if idr is None else round(idr, 1), None if ssr is None else round(ssr, 1), basis])

with open(os.path.join(OUT, 'data_self_sufficiency_by_food.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['year', 'food', 'production_kt', 'imports_kt', 'exports_kt', 'domestic_supply_kt', 'import_dependency_ratio', 'self_sufficiency_ratio', 'food_use_kt', 'feed_use_kt', 'source_ids', 'evidence_label', 'confidence', 'notes'])
    for r in ss_rows:
        yr, label, P, I, E, DS, FOOD, FEED, idr, ssr, basis = r
        note = ('FAOSTAT Food Balances (2010-), elements 5511, 5611, 5911, 5301, 5142, 5521. Ratios are our calculation on the FAO definitions: '
                'import dependency ratio = imports / (production + imports minus exports) x 100; self-sufficiency ratio = production / (production + imports minus exports) x 100. '
                'Domestic supply also nets out stock change, so it can differ from the ratio base. Basis: ' + basis + '.')
        if label == 'Wheat':
            note += ' Ratio above 100% because flour and noodles are re-exported.'
        if label in ('Rice', 'Fish and seafood (all)', 'Marine fish (pelagic, demersal, other)'):
            note += ' Part of the imports is processed and re-exported, so the import dependency ratio overstates imports eaten in Vietnam.'
        if label.startswith('Milk'):
            note += ' Milk series unstable between years (DG-175).'
        if label == 'Eggs':
            note += ' FAO egg production is far below NSO output (DG-174).'
        w.writerow([yr, label, P, I, E, DS, idr, ssr, FOOD, FEED, 'DIE-07', 'VN-direct', 'High' if label not in ('Eggs',) else 'Medium', note])

# ---------- 3. direct import share of protein supply, and the feed behind animal protein ----------
# 3a. direct import share: protein of each leaf item x its import share.
#   gross: min(1, IDR) ; net: max(0, (I-E)/(P+I-E)), capped at 1.
def shares(item, yr):
    P, I, E = z(val(item, '5511', yr)), z(val(item, '5611', yr)), z(val(item, '5911', yr))
    base = P + I - E
    if base <= 0:
        return 0.0, 0.0
    return min(1.0, I / base), max(0.0, min(1.0, (I - E) / base))

direct = {}
for yr in YEARS:
    g_gross = {'plant': 0.0, 'animal': 0.0}
    g_net = {'plant': 0.0, 'animal': 0.0}
    detail = []
    for c, r in leaf_codes.items():
        v = r['Y%d' % yr]
        if not v:
            continue
        p = float(v)
        if p == 0:
            continue
        kind = 'animal' if c in {'2731', '2732', '2733', '2734', '2735', '2736', '2737', '2740', '2743', '2744', '2745', '2761', '2762', '2763', '2764', '2765', '2766', '2767', '2769', '2781', '2782', '2848'} else 'plant'
        gs, ns = shares(r['Item'], yr)
        g_gross[kind] += p * gs
        g_net[kind] += p * ns
        detail.append((r['Item'], kind, p, gs, ns))
    direct[yr] = (g_gross, g_net, detail)

# 3b. feed behind domestic animal protein (2023 food supply, 2025 feed tables).
# Imported share of compound-feed ingredients, USDA Table 2, CY2025, tonnes.
# Crude protein, as fed: SBM 46%, DDGS 27%, other oilseed meals 30% (study conventions, app-f4 F4.3.4);
# maize 8.6% and polished rice 7.9% (Vietnamese Food Composition Table, DIE-12); dried cassava 3.0% (DIE-12);
# wheat grain 11.0% (Feedipedia 12.6% of DM at 87% DM, FBS-04); rice bran 13.3% (Feedipedia 14.8% of DM at 90.1% DM, FBS-05);
# 'rice bran, broken rice' taken at 10% (between broken rice 7.9% and bran 13.3%; mix unknown, our assumption);
# 'other protein meals' (fishmeal, animal meals; composition not given) 55%, range 45 to 65% (our assumption).
FEED_IMP = {'Soybean meal (incl. local crush of imported beans)': (7206000, 0.46), 'Corn': (9214000, 0.086), 'DDGS': (1550000, 0.27),
            'Feed wheat': (2580000, 0.11), 'Rice bran, broken rice (imported)': (545000, 0.10), 'Plant-based meal and bran': (1825000, 0.30),
            'Other protein meals': (650000, 0.55)}
FEED_LOC = {'Corn (local)': (1700000, 0.086), 'Rice bran, broken rice (local)': (2800000, 0.10), 'Cassava (local)': (550000, 0.03)}
imp_mass = sum(t for t, _ in FEED_IMP.values()); loc_mass = sum(t for t, _ in FEED_LOC.values())
imp_cp = sum(t * cp for t, cp in FEED_IMP.values()); loc_cp = sum(t * cp for t, cp in FEED_LOC.values())
m_mass = imp_mass / (imp_mass + loc_mass)
m_prot = imp_cp / (imp_cp + loc_cp)
# Sensitivity on crude-protein assumptions: low protein for imports and high for local, and the reverse.
LOWHIGH = {'Corn': (0.08, 0.094), 'DDGS': (0.25, 0.30), 'Feed wheat': (0.103, 0.125), 'Rice bran, broken rice (imported)': (0.079, 0.133),
           'Plant-based meal and bran': (0.15, 0.35), 'Other protein meals': (0.45, 0.65), 'Soybean meal (incl. local crush of imported beans)': (0.44, 0.48)}
LOWHIGH_LOC = {'Corn (local)': (0.08, 0.094), 'Rice bran, broken rice (local)': (0.079, 0.133), 'Cassava (local)': (0.024, 0.03)}
imp_lo = sum(t * LOWHIGH[k][0] for k, (t, _) in FEED_IMP.items()); loc_hi = sum(t * LOWHIGH_LOC[k][1] for k, (t, _) in FEED_LOC.items())
imp_hi = sum(t * LOWHIGH[k][1] for k, (t, _) in FEED_IMP.items()); loc_lo = sum(t * LOWHIGH_LOC[k][0] for k, (t, _) in FEED_LOC.items())
m_prot_lo = imp_lo / (imp_lo + loc_hi); m_prot_hi = imp_hi / (imp_hi + loc_lo)

# Compound-feed share of each animal food, from app-f4-balance-model (F4.3.3) and balance_assumptions.csv; 'fed' convention ours.
YR = 2023
COMP = {
    'Pigmeat': 0.81, 'Edible offal': 0.81, 'Poultry meat': 0.96, 'Eggs': 0.96,
    'Freshwater fish': 0.68,   # F4 'other fish' share; pangasius (1.00) is mostly exported
    'Crustaceans': 0.80,       # our weighting of whiteleg (1.00, 994 kt) and other shrimp (0.30, 387 kt), 2025 output
    'Bovine meat (beef and buffalo)': 0.0, 'Mutton, goat and other meat': 0.0, 'Milk and dairy (excluding butter)': 0.0,
    'Marine fish, cephalopods and molluscs (capture or unfed)': 0.0,
}
ITEMS = {
    'Pigmeat': ['Pigmeat'], 'Edible offal': ['Offals, Edible'], 'Poultry meat': ['Poultry Meat'], 'Eggs': ['Eggs'],
    'Freshwater fish': ['Freshwater Fish'], 'Crustaceans': ['Crustaceans'],
    'Bovine meat (beef and buffalo)': ['Bovine Meat'], 'Mutton, goat and other meat': ['Mutton & Goat Meat', 'Meat, Other'],
    'Milk and dairy (excluding butter)': ['Milk - Excluding Butter'],
    'Marine fish, cephalopods and molluscs (capture or unfed)': ['Demersal Fish', 'Pelagic Fish', 'Marine Fish, Other', 'Cephalopods', 'Molluscs, Other', 'Aquatic Animals, Others'],
}
rel_rows = []
tot = {'protein': 0, 'direct_gross': 0, 'direct_net': 0, 'dom_gross': 0, 'dom_net': 0, 'feed_mass_g': 0, 'feed_prot_g': 0, 'feed_mass_n': 0, 'feed_prot_n': 0, 'feed_prot_lo_n': 0, 'feed_prot_hi_g': 0}
for food, items in ITEMS.items():
    p = 0.0; dg = 0.0; dn = 0.0
    for it in items:
        code_r = [r for c, r in leaf_codes.items() if r['Item'] == it]
        pv = float(code_r[0]['Y%d' % YR]) if code_r and code_r[0]['Y%d' % YR] else 0.0
        gs, ns = shares(it, YR)
        p += pv; dg += pv * gs; dn += pv * ns
    c = COMP[food]
    dom_g = p - dg; dom_n = p - dn
    fm_g = dom_g * c * m_mass; fp_g = dom_g * c * m_prot
    fm_n = dom_n * c * m_mass; fp_n = dom_n * c * m_prot
    rel_rows.append([YR, food, round(p, 2), round(dn, 2), round(dg, 2), c, round(fm_n, 2), round(fp_g, 2)])
    tot['protein'] += p; tot['direct_gross'] += dg; tot['direct_net'] += dn
    tot['feed_mass_n'] += fm_n; tot['feed_prot_g'] += fp_g
    tot['feed_prot_lo_n'] += dom_n * c * m_prot_lo; tot['feed_prot_hi_g'] += dom_g * c * m_prot_hi
    tot['feed_mass_g'] += fm_g; tot['feed_prot_n'] += fp_n

with open(os.path.join(OUT, 'data_animal_protein_import_reliance.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['year', 'animal_food', 'protein_g_per_person_day', 'direct_import_g_low', 'direct_import_g_high', 'compound_feed_share', 'on_imported_feed_g_low', 'on_imported_feed_g_high', 'source_ids', 'evidence_label', 'confidence', 'notes'])
    for yr, food, p, dn, dg, c, lo, hi in rel_rows:
        note = ('Our calculation. Protein supply 2023 from FAOSTAT FBS. Direct imports: low = net imports share max(0, (imports minus exports) / (production + imports minus exports)); high = gross FAO import dependency ratio. '
                'On imported feed: domestic part x compound-feed share x imported share of compound-feed ingredients (low: by mass, %.1f%%, with net imports; high: by crude protein, %.1f%%, with gross imports), USDA Table 2 for 2025 applied to 2023 supply.' % (100 * m_mass, 100 * m_prot))
        if c == 0:
            note += ' Treated as feed-free (grazing, crop residues, capture or unfed): a lower bound, since dairy cows and fattened cattle eat some imported concentrate.'
        w.writerow([yr, food, p, dn, dg, c, lo, hi, 'DIE-07; MAC-01; FS-23', 'VN-direct', 'Low', note])
    w.writerow([YR, 'All animal foods in the table', round(tot['protein'], 2), round(tot['direct_net'], 2), round(tot['direct_gross'], 2), '', round(tot['feed_mass_n'], 2), round(tot['feed_prot_g'], 2), 'DIE-07; MAC-01; FS-23', 'VN-direct', 'Low', 'Our calculation; sum of the rows above. Excludes animal fats, butter, honey and infant food.'])

# ---------- print summary ----------
print('Population (thousand):', pop)
print('Imported share of compound-feed ingredients 2025: mass %.1f%%; crude protein %.1f%% (range %.1f to %.1f%%)' % (100 * m_mass, 100 * m_prot, 100 * m_prot_lo, 100 * m_prot_hi))
print('Imported CP Mt %.2f, local CP Mt %.2f' % (imp_cp / 1e6, loc_cp / 1e6))
for yr in YEARS:
    gg, gn, detail = direct[yr]
    total = val('Grand Total', '674', yr)
    print(yr, 'total %.1f g; direct imports gross: plant %.2f animal %.2f total %.2f (%.1f%%); net: plant %.2f animal %.2f total %.2f (%.1f%%)' % (
        total, gg['plant'], gg['animal'], gg['plant'] + gg['animal'], 100 * (gg['plant'] + gg['animal']) / total,
        gn['plant'], gn['animal'], gn['plant'] + gn['animal'], 100 * (gn['plant'] + gn['animal']) / total))
gg, gn, detail = direct[2023]
print('2023 detail (item, kind, g, gross share, net share), items >0.3 g or share>0.3:')
for it, k, p, gs, ns in sorted(detail, key=lambda x: -x[2] * x[3]):
    if p * gs > 0.05:
        print('  %-28s %-6s %6.2f  gross %5.1f%%  net %5.1f%%  -> %.2f / %.2f g' % (it, k, p, 100 * gs, 100 * ns, p * gs, p * ns))
print('Animal reliance 2023:', {k: round(v, 2) for k, v in tot.items()})
an = float(leaf_by_code['2941']['Y2023'])
print('Animal total 2023 %.2f; table covers %.2f' % (an, tot['protein']))
print('Low: direct net %.2f + feed (mass, net) %.2f = %.2f g = %.1f%% of animal protein' % (tot['direct_net'], tot['feed_mass_n'], tot['direct_net'] + tot['feed_mass_n'], 100 * (tot['direct_net'] + tot['feed_mass_n']) / an))
print('High: direct gross %.2f + feed (protein, gross) %.2f = %.2f g = %.1f%% of animal protein' % (tot['direct_gross'], tot['feed_prot_g'], tot['direct_gross'] + tot['feed_prot_g'], 100 * (tot['direct_gross'] + tot['feed_prot_g']) / an))
print('CP sensitivity: low-low %.2f g; high-high %.2f g' % (tot['direct_net'] + tot['feed_prot_lo_n'], tot['direct_gross'] + tot['feed_prot_hi_g']))


# ---------- 4. meat only, 2023, and S-BASE projection of meat protein resting on imports ----------
meat_items = ['Pigmeat', 'Poultry meat', 'Bovine meat (beef and buffalo)', 'Mutton, goat and other meat']
mp = sum(r[2] for r in rel_rows if r[1] in meat_items)
lo = sum(r[3] + r[6] for r in rel_rows if r[1] in meat_items)
hi = sum(r[4] + r[7] for r in rel_rows if r[1] in meat_items)
print('Meat 2023: protein %.2f g; on imports %.2f to %.2f g (%.1f%% to %.1f%%)' % (mp, lo, hi, 100 * lo / mp, 100 * hi / mp))

bo = list(csv.DictReader(open(os.path.join(OUT, '..', '..', '..', 'data', 'balance_outputs.csv'))))
def b(ind, yr, sc='S-BASE'):
    for r in bo:
        if r['scenario'] == sc and r['indicator'] == ind and r['year'] == str(yr):
            return float(r['value'])
SSR = {'pork': 0.961, 'poultry': 0.875, 'ruminant': 0.522}           # balance_assumptions.csv, held constant (QNT-01)
COMPY = {2025: {'pork': 0.81, 'poultry': 0.96}, 2030: {'pork': 0.88, 'poultry': 0.97}, 2035: {'pork': 0.91, 'poultry': 0.97},
         2040: {'pork': 0.94, 'poultry': 0.98}, 2050: {'pork': 0.97, 'poultry': 0.98}}   # F4.3.3 paths (2035 interpolated, poultry path 0.97 to 0.98)
proj = []
for sc in ('S-BASE', 'S-HIGH'):
    for yr in (2025, 2030, 2035, 2040, 2050):
        popn = b('population', yr, sc)
        q = {'pork': b('pc_pork_demand_kg_cwe', yr, sc), 'poultry': b('pc_poultry_demand_kg_cwe', yr, sc), 'ruminant': b('pc_ruminant_demand_kg_cwe', yr, sc)}
        tot_q = sum(q.values())
        res = {}
        for lab, m in (('mass', m_mass), ('protein', m_prot)):
            share = 0.0
            for k, v in q.items():
                c = COMPY[yr].get(k, 0.0)
                share += v * ((1 - SSR[k]) + SSR[k] * c * m)
            res[lab] = share / tot_q
        prot_kt = tot_q * popn * 0.15      # 0.15 kg protein per kg cwe (F4 convention; FBS 2023 implies 0.151)
        g_day = tot_q * 0.15 / 365 * 1000
        proj.append([sc, yr, round(tot_q, 1), round(g_day, 1), round(prot_kt), round(100 * res['mass'], 1), round(100 * res['protein'], 1), round(prot_kt * res['mass']), round(prot_kt * res['protein'])])
for p in proj:
    print(p)
with open(os.path.join(OUT, 'data_meat_protein_on_imports_projection.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['scenario', 'year', 'meat_kg_cwe_per_person', 'meat_protein_g_per_person_day', 'meat_protein_kt', 'share_on_imports_low_pct', 'share_on_imports_high_pct', 'meat_protein_on_imports_kt_low', 'meat_protein_on_imports_kt_high', 'source_ids', 'evidence_label', 'confidence', 'foresight_type', 'horizon_year', 'notes'])
    for sc, yr, q, g, kt, sl, sh, kl, kh in proj:
        ft = 'calibration (2025 base)' if yr == 2025 else 'estimate'
        w.writerow([sc, yr, q, g, kt, sl, sh, kl, kh, 'QNT-01; MAC-01; FS-23', 'VN-direct', 'Low', ft, yr,
                    'Our calculation. Meat per person and population from data/balance_outputs.csv (balance model, unchanged); 0.15 kg protein per kg carcass weight (F4 convention; FAOSTAT 2023 implies 0.151). '
                    'Share on imports = sum over pork, poultry and beef of demand x ((1 minus SSR) + SSR x compound-feed share x imported share of compound feed). SSR held at OECD-FAO 2025 values (0.961, 0.875, 0.522). '
                    'Compound-feed shares from F4.3.3 (pigs 0.81 to 0.97, poultry 0.96 to 0.98; ruminants 0). Imported share of compound feed held at 2025 values: low %.1f%% by mass, high %.1f%% by crude protein.' % (100 * m_mass, 100 * m_prot)])
