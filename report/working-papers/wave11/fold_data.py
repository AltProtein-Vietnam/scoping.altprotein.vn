"""Copy wave 11 line data tables into data/ and document them (run from the repository root).

Adds a stable record_id where a table has none, checks for dashes, writes the
file to data/, rebuilds the "Files added in the food-security round (v0.8)"
section of data/data-dictionary.md and adds entries to site-manifest.json
(data). Safe to re-run.
"""
import csv, json, os, re

BASE = 'working-papers/wave11'
DASH = re.compile('[–—]')
# (line folder, source file, target file, id prefix, purpose, used on)
TABLES = [
    ('L4-protein-for-people', 'data_protein_supply_by_source.csv', 'protein_supply_by_source.csv', 'PSS',
     'Protein supply per person per day by food group, Viet Nam, 2010, 2015, 2020 and 2023 (FAO food balance sheets), with shares of the total.',
     'ch01, ch11, ch22'),
    ('L4-protein-for-people', 'data_self_sufficiency_by_food.csv', 'self_sufficiency_by_food.csv', 'SSF',
     'Production, imports, exports, domestic supply, food and feed use, import dependency and self-sufficiency ratios by food, Viet Nam, 2010 to 2023 (FAO food balance sheets; ratios our calculation on FAO definitions).',
     'ch01, ch11, ch22'),
    ('L4-protein-for-people', 'data_animal_protein_import_reliance.csv', 'animal_protein_import_reliance.csv', 'AIR',
     'Animal protein per person per day by food, with the part imported directly and the part from domestic animals and fish raised on imported compound feed (low and high cases; our calculation).',
     'ch01, ch22'),
    ('L4-protein-for-people', 'data_meat_protein_on_imports_projection.csv', 'meat_protein_on_imports_projection.csv', 'MPI',
     'Meat protein people eat to 2050 on the balance model scenarios, and the share resting on imports directly or through feed (our estimate; scenarios, not forecasts).',
     'ch22'),
    ('L2-disease-pandemic', 'data_disease_shocks.csv', 'disease_shocks.csv', 'DSH',
     'Animal-disease and zoonotic events that hit the protein people eat in Viet Nam (African swine fever, avian influenza, Streptococcus suis and others): losses, price effects and human cases.',
     'ch01, ch20, F2'),
    ('L3-security-exposures', 'data_security_exposures.csv', 'security_exposures.csv', None,
     'Food-security exposures of the protein people eat, the evidence for each, and whether alternative protein for food would reduce it, given where its inputs come from.',
     'ch01, ch20, ch23'),
    ('L3-security-exposures', 'data_route_input_origin.csv', 'route_input_origin.csv', None,
     'Alternative-protein routes by where their protein, carbon, nitrogen, energy, equipment and strains come from, and the effect on import dependence.',
     'ch01, ch10'),
    ('L3-security-exposures', 'data_import_concentration.csv', 'protein_import_concentration.csv', None,
     'Concentration of origins for protein foods and inputs Viet Nam imports: value, tonnage, top origins, top-three share and Herfindahl index by HS code.',
     'ch01, ch20'),
    ('L1-meat-imports', 'data_meat_dairy_imports.csv', 'meat_dairy_imports.csv', 'MDI',
     'Viet Nam imports of meat, edible offal, live cattle and dairy by year and product, with main origins and share of consumption.',
     'ch01, ch16'),
    ('L1-meat-imports', 'data_origin_support.csv', 'origin_support.csv', 'OSU',
     'Producer support in the main origins of Viet Nam\'s meat and dairy imports (OECD producer support estimates and other measures) by country and commodity.',
     'ch01'),
]

COL = {
    'record_id': 'Stable row ID.', 'year': 'Year the value refers to.', 'item_group': 'FAO food balance sheet item or group.',
    'protein_g_per_person_day': 'Protein supply, g per person per day (supply basis, not intake).',
    'share_of_total': 'Share of total protein supply.', 'plant_or_animal': 'Plant or animal food.',
    'food': 'Food or commodity.', 'production_kt': 'Production, kt.', 'imports_kt': 'Imports, kt.', 'exports_kt': 'Exports, kt.',
    'domestic_supply_kt': 'Domestic supply quantity, kt (production plus imports minus exports, with stock change).',
    'import_dependency_ratio': 'Imports / (production + imports minus exports) x 100 (FAO definition; our calculation).',
    'self_sufficiency_ratio': 'Production / (production + imports minus exports) x 100 (FAO definition; our calculation).',
    'food_use_kt': 'Food use, kt.', 'feed_use_kt': 'Feed use, kt.', 'animal_food': 'Animal food.',
    'direct_import_g_low': 'Imported directly, g per person per day, low case (net imports).',
    'direct_import_g_high': 'Imported directly, g per person per day, high case (gross imports on the import dependency ratio).',
    'compound_feed_share': 'Share of output raised on compound feed (assumption; see the working paper).',
    'on_imported_feed_g_low': 'From domestic animals raised on imported feed, g per person per day, low case.',
    'on_imported_feed_g_high': 'From domestic animals raised on imported feed, g per person per day, high case.',
    'scenario': 'Balance model scenario (S-BASE trend and others).', 'meat_kg_cwe_per_person': 'Meat, kg carcass weight per person.',
    'meat_protein_g_per_person_day': 'Meat protein, g per person per day (supply basis).', 'meat_protein_kt': 'Meat protein, kt a year.',
    'share_on_imports_low_pct': 'Share of meat protein resting on imports, low case, %.',
    'share_on_imports_high_pct': 'Share of meat protein resting on imports, high case, %.',
    'meat_protein_on_imports_kt_low': 'Meat protein resting on imports, kt, low case.',
    'meat_protein_on_imports_kt_high': 'Meat protein resting on imports, kt, high case.',
    'foresight_type': 'Foresight type (trend, projection, estimate, signal, wildcard).', 'horizon_year': 'Horizon year.',
    'event': 'Event.', 'years': 'Year or years.', 'species': 'Species affected.', 'losses': 'Animals or output lost.',
    'price_effect': 'Effect on prices.', 'human_cases': 'Human cases and deaths, where relevant.',
    'exposure': 'Exposure.', 'protein_food_affected': 'Protein food affected.', 'evidence_of_exposure': 'Evidence that the exposure is real.',
    'does_alt_protein_for_food_reduce_it': 'Whether alternative protein for food would reduce the exposure, and how much at the study\'s scale.',
    'inputs_domestic_or_imported': 'Whether the relevant inputs are domestic or imported.',
    'route': 'Alternative-protein route.', 'protein_input': 'Main protein input.', 'protein_input_origin': 'Where the protein input comes from.',
    'carbon_nitrogen_energy': 'Carbon, nitrogen and energy inputs and their origin.', 'equipment_strain_ip': 'Equipment, strains and know-how and their origin.',
    'main_inputs_domestic_or_imported': 'Whether the main inputs are domestic or imported.', 'effect_on_import_dependence': 'Effect on import dependence.',
    'hs_code': 'Harmonised System (HS) code.', 'product': 'Product.', 'value_usd_m': 'Import value, USD million.', 'net_weight_t': 'Net weight, t.',
    'top_origins_value_share': 'Main origins with their share of value.', 'top3_share_pct': 'Share of the top three origins, %.',
    'hhi_value': 'Herfindahl-Hirschman index of origin concentration (by value).', 'n_partners': 'Number of origin countries.',
    'source_ids': 'Source IDs in sources.csv, separated by semicolons.', 'evidence_label': 'VN-direct, VN-adjacent or general.',
    'confidence': 'High, Medium or Low.', 'notes': 'Notes, caveats and calculation inputs.',
}

dd_path = 'data/data-dictionary.md'
dd = open(dd_path, encoding='utf-8').read()
dd = re.sub(r'\n## Files added in the food-security round \(v0\.8\).*?(?=\n## |\Z)', '', dd, flags=re.S)
summary_rows, details = [], []
man = json.load(open('site-manifest.json', encoding='utf-8'))
for folder, src, dst, pfx, purpose, used in TABLES:
    sp = os.path.join(BASE, folder, src)
    if not os.path.exists(sp):
        print('skip (not ready):', sp)
        continue
    with open(sp, newline='', encoding='utf-8') as f:
        rd = csv.DictReader(f)
        fields, rows = list(rd.fieldnames), list(rd)
    if 'record_id' not in fields:
        fields = ['record_id'] + fields
        for i, r in enumerate(rows, 1):
            r['record_id'] = f'{pfx}-{i:03d}'
    for r in rows:
        for k, v in r.items():
            if v and DASH.search(v):
                r[k] = DASH.sub(' to ', v)
    with open(os.path.join('data', dst), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n', extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)
    summary_rows.append(f'| {dst} | {len(rows)} | {purpose} Used in {used}. |')
    lines = [f'### {dst}', '', purpose, '', f'Rows: {len(rows)}. Columns: {len(fields)}. From `{BASE}/{folder}/`.', '',
             '| Column | Meaning | Example |', '|---|---|---|']
    for c in fields:
        ex = (rows[0].get(c, '') if rows else '').replace('|', '/')
        ex = ex[:80] + ' ...' if len(ex) > 80 else ex
        lines.append(f'| `{c}` | {COL.get(c, c.replace("_", " ").capitalize() + ".")} | {ex} |')
    details.append('\n'.join(lines))
    man['data'][dst[:-4]] = f'data/{dst}'

section = ('\n## Files added in the food-security round (v0.8)\n\n'
           'Built on 1 October 2026 from the wave 11 research lines (`working-papers/wave11/`). Version 0.8 also added '
           'rows to `sources.csv` (wave 11 prefixes), `open_questions.csv` (from OQ-447), `disagreements.csv` (from DG-353) '
           'and `key-numbers.json`, and status columns to the play, move and policy files.\n\n'
           '| File | Rows | Purpose |\n|---|---|---|\n' + '\n'.join(summary_rows) + '\n\n' + '\n\n'.join(details) + '\n')
dd = dd.rstrip('\n') + '\n' + section
open(dd_path, 'w', encoding='utf-8').write(dd)
with open('site-manifest.json', 'w', encoding='utf-8') as f:
    json.dump(man, f, ensure_ascii=False, indent=1)
print('tables written:', len(summary_rows))
