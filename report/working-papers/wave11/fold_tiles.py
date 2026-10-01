"""Update and add stat tiles in data/key-numbers.json for version 0.8 (run from the repository root).

Updates count tiles changed by the human-food refocus, adds wave 11 tiles and
the new vision tiles. `pages` lists are rebuilt from the content folder at the
end of consolidation by sync_pages(); new tiles start with their primary page.
Safe to re-run.
"""
import json, os, re

P = 'data/key-numbers.json'
kn = json.load(open(P, encoding='utf-8'))
by = {e['id']: e for e in kn}

UPDATES = {
    'kn-plays-count': dict(value='7 plays and 4 public goods', value_low=7, value_high=7,
        context='Our count from plays.csv (October 2026): seven businesses or programmes for protein people eat, each with conditions, kill tests, first customers and a horizon, plus four public goods that lower the cost of all of them. Three feed plays and two feed public goods assessed earlier are kept in the file as the record but no longer recommended.',
        as_of='Oct 2026', version='0.8'),
    'kn-top-play-balanced': dict(context='The cassava-starch-to-sugar hub (T4) and domestic textured plant protein (T1) lead under balanced weights; shared pilot and tolling fermentation (T5) follows at 3.45. Scores are our judgement, not an investment rating.',
        as_of='Oct 2026', version='0.8'),
    'kn-policy-options-count': dict(value='33 options (19 ranked)', context='Our count from policy_options.csv (October 2026): 33 options, of which chapter 27 ranks 19; nine earlier options are superseded by more specific ones and five feed options are kept as the record but no longer ranked.',
        as_of='Oct 2026', version='0.8'),
    'kn-low-effort-options': dict(value='13 of 19 ranked options', value_low=13, value_high=13,
        context='Derived from policy_options.csv: ranked options rated Low effort (a letter, guidance or list update), as of October 2026. The report text does not state this total; ranks 1 and 2 are low effort.',
        as_of='Oct 2026', version='0.8'),
    'kn-no-regret-moves': dict(value='7 of 21 moves', value_low=7, value_high=7,
        context='A national protein balance; a new-food route with deadlines; shared food-grade pilot capacity; a protein-quality laboratory and price series; residue-carbon rules and a by-product atlas; climate-proof siting; process-engineering skills. Five feed moves tested earlier are no longer recommended. Our judgement.',
        version='0.8'),
    'kn-no-regret-plays': dict(value='2 of 11, both public infrastructure', value_low=2, value_high=2,
        context='A protein-quality laboratory and an open cost model and price series. Seven more plays and public goods hold in every world with conditions; one is a bet; one is a research option. Our judgement.',
        version='0.8'),
}

COMMON = dict(derived=True, evidence='VN-direct', version='0.8')
NEW = [
    dict(id='kn-animal-protein-on-imports', label='Animal protein people eat that rests on imports, directly or through feed',
         label_vi='Tỷ lệ đạm động vật trong khẩu phần phụ thuộc nhập khẩu, trực tiếp hoặc qua thức ăn chăn nuôi',
         value='61% to 71%', value_low=61, value_high=71, unit='% of animal protein supply', as_of='2023',
         context='Imported meat, offal, milk and fish, plus domestic pork, poultry, eggs and farmed fish attributed to imported compound feed (82% of feed ingredients by weight and about 93% by protein were imported in 2025). FAO food balance sheets, supply basis. Our calculation.',
         source_ids=['DIE-07', 'MAC-01', 'FS-23'], confidence='Low', primary_page='ch01-why-vietnam'),
    dict(id='kn-protein-supply-imported', label='Protein supply that is imported food',
         label_vi='Tỷ lệ đạm trong nguồn cung thực phẩm đến trực tiếp từ thực phẩm nhập khẩu',
         value='19% to 23%', value_low=19, value_high=23, unit='% of protein supply', as_of='2023',
         context='Net to gross import basis on FAO food balance sheets; 11% to 13% in 2010. Soybeans, wheat, maize, milk, beef, offal, poultry, groundnuts and beans carry most of it. Our calculation.',
         source_ids=['DIE-07'], confidence='Medium', demand_evidence_type='revealed', primary_page='ch01-why-vietnam'),
    dict(id='kn-soybean-import-dependence', label='Import dependence of soybeans, the base of tofu and soy milk',
         label_vi='Tỷ lệ phụ thuộc nhập khẩu của đậu tương, nguyên liệu làm đậu phụ và sữa đậu nành',
         value='97.5%', value_low=97.5, value_high=97.5, unit='% (import dependency ratio)', as_of='2023',
         context='Soy foods supply 4.9 g of protein per person per day, about 181,000 t of protein a year; domestic beans (48 kt) could cover at most 9% of the 533 kt used as food. Our calculation from FAO food balance sheets.',
         source_ids=['DIE-07'], confidence='High', primary_page='ch11-protein-diet'),
    dict(id='kn-milk-self-sufficiency', label='Milk and dairy self-sufficiency',
         label_vi='Tỷ lệ tự cung sữa và sản phẩm sữa',
         value='about 30%', value_low=30, value_high=30, unit='% (milk equivalent)', as_of='2023',
         context='Production over production plus imports minus exports, FAO food balance sheets; the FAO milk series swings between years, so read it as a level, not a trend. Decision 309/QD-TTg targets domestic raw milk meeting 60% to 65% of processing demand by 2030, a different basis. Our calculation.',
         source_ids=['DIE-07', 'APR-11'], confidence='Medium', primary_page='ch01-why-vietnam'),
    dict(id='kn-meat-protein-on-imports-2050', label='Meat protein resting on imports in 2050, trend scenario',
         label_vi='Tỷ lệ đạm từ thịt phụ thuộc nhập khẩu năm 2050, kịch bản xu hướng',
         value='79% to 87%', value_low=79, value_high=87, unit='% of meat protein', as_of='2050',
         context='Balance model trend scenario (S-BASE): about 1,446 kt of meat protein in 2050, of which 1,136 to 1,261 kt rests on imports directly or through feed (69% to 77% in 2023). Self-sufficiency and imported feed shares held at 2025 values. Our estimate; a scenario, not a forecast.',
         source_ids=['QNT-01', 'MAC-01', 'DIE-07'], confidence='Low', foresight_type='estimate', horizon='2050',
         primary_page='ch22-protein-balance-2050'),
    dict(id='kn-asf-recombinant-share', label='Recombinant African swine fever virus in typed samples, northern Vietnam',
         label_vi='Tỷ lệ chủng vi rút dịch tả lợn châu Phi tái tổ hợp trong mẫu giám sát ở miền Bắc',
         value='79%', value_low=79, value_high=79, unit='% of typed samples', as_of='2025',
         context='158 of 200 samples; 76% in the centre and Central Highlands, 60% in the south. MAE says the three licensed vaccines, made from genotype II virus, have no protective effect against the recombinant strains (official letter 2481/CNTY-DT, September 2025).',
         source_ids=['PAN-33'], derived=False, confidence='High', primary_page='ch20-drivers-2050'),
    dict(id='kn-h5n1-human-cases', label='Human H5N1 cases in Vietnam since 2003',
         label_vi='Số ca mắc cúm A(H5N1) ở người tại Việt Nam từ năm 2003',
         value='130 cases (65 deaths)', value_low=130, value_high=130, unit='cases', as_of='6 Sep 2026',
         context='None in 2026 to 6 September; 1 in 2025; 2 in 2020 to 2024. WHO judges sustained human-to-human spread unlikely at present.',
         source_ids=['PAN-01', 'PAN-02'], derived=False, confidence='High', primary_page='app-f2-drivers-signals'),
    dict(id='kn-asf-culls-vs-spared', label='Pigs culled for African swine fever in 2025, against pigs the benchmark demand path spares in 2035',
         label_vi='Số lợn tiêu hủy do dịch tả lợn châu Phi năm 2025 so với số lợn được tránh giết mổ theo kịch bản D-BENCH năm 2035',
         value='8.4 times', value_low=8.4, value_high=8.4, unit='times', as_of='2025 and 2035',
         context='About 1.2 million pigs culled in 2025 against about 142,000 pigs spared a year in 2035 on the benchmark path (D-BENCH); 41.5 times for the 2019 epidemic. Alternative protein at the scale demand supports does not change disease exposure. Our calculation.',
         source_ids=['MAC-01', 'PAN-03'], confidence='Low', foresight_type='estimate', horizon='2035',
         demand_evidence_type='inferred', primary_page='ch01-why-vietnam'),
    dict(id='kn-china-share-plant-protein-ingredients', label="China's share of imported food plant-protein ingredients",
         label_vi='Tỷ trọng của Trung Quốc trong lượng nguyên liệu đạm thực vật nhập khẩu',
         value='84%', value_low=84, value_high=84, unit='% of tonnage (HS 3504, 2106.10, 1109)', as_of='2025',
         context='53,976 of 64,248 t reaching Vietnam, partner-reported (our calculation). Alternative protein made from these ingredients moves dependence to China rather than reducing it.',
         source_ids=['BUY-02'], confidence='Medium', demand_evidence_type='revealed', primary_page='ch01-why-vietnam'),
    dict(id='kn-pork-price-2020', label='Consumer pork price rise in 2020, after African swine fever',
         label_vi='Giá thịt lợn tiêu dùng tăng năm 2020, sau dịch tả lợn châu Phi',
         value='57.23%', value_low=57.23, value_high=57.23, unit='% on 2019 (consumer price index item)', as_of='2020',
         context='1.94 points of a 3.23% rise in the consumer price index. In 2022, the year world feed prices peaked, pork fell 10.68% and food rose 1.62%: consumers felt disease more than imported feed.',
         source_ids=['SEC-08', 'SEC-09'], derived=False, confidence='High', demand_evidence_type='revealed', primary_page='ch01-why-vietnam'),
    dict(id='kn-marine-stock-fall', label='Fall in marine fish standing stock',
         label_vi='Mức suy giảm trữ lượng nguồn lợi hải sản',
         value='22.1%', value_low=22.1, value_high=22.1, unit='% (2016 to 2020 against 2000 to 2005)', as_of='2020',
         context='About 3.95 Mt in 2016 to 2020; capture still rose from 3.26 Mt (2016) to 3.83 Mt (2024). Policy aims to cut capture about 27% by 2030; FAO projects climate losses of 2.8% to 11.7% of catch potential by 2050.',
         source_ids=['SEC-06', 'SEC-07'], derived=False, confidence='Medium', primary_page='ch20-drivers-2050'),
    dict(id='kn-vision-protein-new-routes-2050', label='Vision: protein from new routes, 2050',
         label_vi='Tầm nhìn: lượng đạm từ các kênh mới năm 2050',
         value='about 67,000 to 172,000 t of protein a year', value_low=66.7, value_high=171.5, unit='kt protein', as_of='vision',
         context='A goal, not a forecast: the benchmark (D-BENCH) and stretch (D-STRETCH) paths of the demand model. Routes: import substitution (about two-thirds on the benchmark path), upgraded chay, blends, canteen dishes, analogues, plant drinks and exports. The stretch path assumes conditions not yet seen anywhere. Drift path: about 10.7 kt.',
         source_ids=['BUY-02', 'GLB-09', 'GT-12', 'QNT-01'], confidence='Low', foresight_type='vision', horizon='2050',
         demand_evidence_type='inferred', primary_page='ch24-vision-2050'),
    dict(id='kn-vision-made-in-vietnam-2050', label='Vision: protein made in Vietnam for the home market, 2050',
         label_vi='Tầm nhìn: lượng đạm sản xuất tại Việt Nam cho thị trường trong nước năm 2050',
         value='about 59,000 to 147,000 t of protein a year', value_low=59.15, value_high=146.51, unit='kt protein', as_of='vision',
         context='Demand model, benchmark to stretch path (routes R1 to R6). Only import substitution applies an explicit domestic share; the other routes count protein of any origin, so this is the upper, model reading. Most of it is plant protein processed in Vietnam in place of imported ingredients.',
         source_ids=['BUY-02', 'GT-12', 'QNT-01'], confidence='Low', foresight_type='vision', horizon='2050',
         demand_evidence_type='inferred', primary_page='ch24-vision-2050'),
    dict(id='kn-vision-domestic-ingredient-share-2050', label='Vision: domestic share of food plant-protein ingredients, 2050',
         label_vi='Tầm nhìn: tỷ lệ nguyên liệu đạm thực vật cho thực phẩm do doanh nghiệp trong nước cung cấp năm 2050',
         value='40% to 60%', value_low=40, value_high=60, unit='% of the ingredient pool', as_of='vision',
         context='Share of the food plant-protein ingredient pool (textured soy, gluten, isolates; about 35,000 to 40,000 t of product in 2025, mostly from China) supplied by domestic makers: demand-model assumptions for the benchmark and stretch paths. 25% to 45% in 2035; drift path 10% in 2050. Made from imported soy, this moves rather than removes import dependence.',
         source_ids=['BUY-02', 'BRD-05', 'BRD-06'], confidence='Low', foresight_type='vision', horizon='2050',
         demand_evidence_type='inferred', primary_page='ch24-vision-2050'),
]

for i, upd in UPDATES.items():
    by[i].update(upd)
ids = {e['id'] for e in kn}
for t in NEW:
    e = dict(COMMON)
    e.update(t)
    e.setdefault('pages', [e['primary_page']])
    order = ['id', 'label', 'label_vi', 'value', 'value_low', 'value_high', 'unit', 'as_of', 'context', 'source_ids',
             'derived', 'evidence', 'confidence', 'primary_page', 'pages', 'foresight_type', 'horizon',
             'demand_evidence_type', 'version']
    e = {k: e[k] for k in order if k in e}
    if e['id'] in ids:
        old = by[e['id']]
        e['pages'] = old.get('pages', e['pages'])
        old.clear(); old.update(e)
    else:
        kn.append(e); by[e['id']] = e

with open(P, 'w', encoding='utf-8') as f:
    json.dump(kn, f, ensure_ascii=False, indent=1)
print(len(kn), 'tiles')
