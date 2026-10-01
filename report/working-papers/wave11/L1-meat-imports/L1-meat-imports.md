# Imported meat, offal and dairy, and the subsidy hypothesis

Line: L1 Imported meat, offal and dairy, and the subsidy hypothesis (wave 11). Source prefix: MIM. Date: 2026-10-01.

## Verdict

The subsidy hypothesis does not hold. Vietnam does import a growing amount of meat and dairy (978.3 kt of meat and meat products worth USD 2.0 billion in 2025, up 12% in value, and USD 1.44 billion of dairy, up 27%), but the dependence is concentrated in beef and buffalo meat (32 to 48% imported) and dairy (domestic fresh milk meets about 40% of demand), while pork is about 96% domestic and poultry 83 to 89%. The origins that ship most of this give little or no commodity-specific support (OECD producer NPC 1.00 for US, Brazilian, Australian and New Zealand meat and milk in 2022 to 2024), the largest origin by value (India, buffalo meat) taxes its producers, and the 2015 WTO Nairobi decision required agricultural export subsidies to end (between 2015 and 2023, depending on the member and product); Russia's pork, which benefits from border protection and cheaper policy-driven feed, is the one partial exception. Imports are cheap mainly because of a large production-cost gap and the export of low-value cuts and by-products, not because of subsidies, and no trade-defence petition on meat or dairy has ever been filed. Yield class: **closed a question** (the subsidy hypothesis, with a mostly clean negative, and the meat-import part of OQ-009), with a smaller **added a constraint**: ch01 gains a second, food-side import exposure in beef, buffalo meat and dairy that alternative protein for food, at the study's benchmark scale (about 1.6% of imported meat protein at most), would not materially reduce.

## Headline findings

1. **Meat imports reached 978.3 kt and USD 2.004 billion in 2025** (customs, via MOIT's Department of Import and Export), up 11.6% in volume and 12.2% in value; January to July 2026 was up another 11.4% in volume (595.7 kt) [VN-direct, Medium, MIM-04; MIM-10, revealed]. By value, imports grew about fivefold between 2015 and 2023 (USD 301 million to USD 1,506 million, Vietnam-reported) with the step change in the 2019 to 2020 swine fever years [VN-direct, High, MIM-01, revealed].
2. **What is imported is mostly cheap cuts, by-products and buffalo meat:** poultry meat and by-products 36.77% of 2025 volume (about 360 kt), Indian frozen buffalo meat 17.68% of volume and 31.85% of value (about 173 kt), pork 183.4 kt (Russia 48%, Brazil 31%), plus pig and bovine offal [VN-direct, Medium, MIM-05; MIM-06, revealed].
3. **Import shares by food (2025) differ widely:** pork 3.7 to 4.5%, poultry 11 to 17% depending on whether by-products count, beef and buffalo 32% (USDA) to 48% (OECD-FAO). Dairy is the most import-dependent: domestic fresh milk meets about 40% of demand (association claim) and dairy imports were USD 1.44 billion (+27.3%), 30.5% from New Zealand [VN-direct, Medium, MIM-03; MIM-05; MIM-06; QNT-01; MIM-12; Low, MIM-13].
4. **Imported meat is much cheaper per kilogram:** frozen pork landed at USD 1,638 per t in January to July 2026 (about VND 42,600 per kg), roughly half the carcass-equivalent price of domestic pigs; imported poultry and by-products at about VND 26,500 per kg (our calculations; different products) [VN-direct, Medium, MIM-09; MIM-07, revealed].
5. **The gap is structural, not subsidised:** Vietnamese farm-gate pigmeat prices in 2024 were 1.6 to 2.8 times those of Brazil, Russia, the United States and the EU, and the bovine price about 5 times India's (OECD) [general and VN-direct, Medium, MIM-15].
6. **Origin support is low for what Vietnam buys:** producer NPC 1.00 (no price support) in 2022 to 2024 for US poultry, pigmeat, beef and milk, Brazilian poultry and beef, Australian and New Zealand meat and milk; India's bovine NPC 0.78 to 0.90 (taxed). Support shows up in the EU (poultry 1.30 to 1.45, beef 1.20 to 1.59) and Russia (pigmeat 1.19 to 1.65, plus an implicit feed transfer of USD 212 to 791 million a year), working through border protection rather than export payments [general, High, MIM-15; MIM-16].
7. **Export subsidies are banned** under the 2015 WTO Nairobi decision (developed members at once, swine and dairy exceptions to 2020; developing members by 2018 to 2023) [general, High, MIM-17]. We found no study measuring whether origin support lowers the price of meat landed in Vietnam.
8. **No trade-defence case on meat or dairy has ever been opened.** MOIT officials saw "clear signs" of dumping in US chicken legs, Brazilian chicken and Korean spent hens in 2020, but no petition was filed because the foreign-invested integrators holding about 70% of industrial poultry output did not join [VN-direct, Low, MIM-24; MIM-08; Medium, MIM-25].
9. **Tariffs are modest and falling:** MFN 10% on frozen pork, 8% on offal, 14% on boneless beef and buffalo, 15% on frozen chicken legs since Decree 73/2025, 2 to 5% on milk powder; EVFTA takes EU frozen pork to 0% after 7 years and chicken after 10 [VN-direct, High, MIM-20; Medium, REG2-21; MIM-21; MIM-22].
10. **Alternative protein for food would barely touch these imports.** Imported meat carried roughly 147 kt of protein in 2025; the benchmark path displaces 2.35 kt of meat protein by 2035, at most about 1.6% of that even if all of it came out of imports. High-protein plant milks deliver 1.29 kt of protein by 2035 against about 48 kt of protein in 2023 milk powder imports. Feet, offal, bone-in poultry and buffalo meat for *phở* have no alternative-protein substitute; frozen pork and mechanically deboned meat for processors are the only real overlap (our calculations, Low) [VN-direct, Low, DMO-0273; DMO-0267; MIM-27, inferred].

## Detailed findings

All our calculations are reproduced by `calculations.py` in this folder; the Comtrade pulls are documented in `comtrade_pull.py`, and raw API responses are in `raw/`.

### 1. Volumes, values and origins (UN Comtrade, Vietnam-reported, 2015 to 2023)

Vietnam has reported its trade to UN Comtrade up to 2023. At the time of access (2026-10-01) there were no Vietnam-reported rows for 2024 or 2025. For 2024 and 2025 we use mirror data (what the exporting countries report as shipped to Vietnam) and Vietnamese customs figures relayed in the press.

Vietnam-reported imports, all origins, USD million (our sums of the HS 4-digit lines; raw files in `raw/vnm_M_world_<year>.json`, script `comtrade_pull.py`) [VN-direct, High, MIM-01]:

| Year | Meat and edible offal (0201 to 0210, excluding 0205 and 0208) | Dairy (0401 to 0406) | Live bovine animals (0102) |
|---|---|---|---|
| 2015 | 301 | 525 | 454 |
| 2016 | 349 | 471 | 350 |
| 2017 | 352 | 593 | 316 |
| 2018 | 529 | 621 | 350 |
| 2019 | 789 | 649 | 615 |
| 2020 | 1,237 | 666 | 686 |
| 2021 | 1,385 | 755 | 510 |
| 2022 | 1,525 | 844 | 241 |
| 2023 | 1,506 | 793 | 199 |

Vietnam-reported tonnages are not shown because they are incomplete (next paragraph).

Origins in 2023, Vietnam-reported, shares of import value (raw file `raw/vnm_M_partners_2023.json`) [VN-direct, High, MIM-01]:

| HS line | Value 2023, USD million | Main origins (share of value) |
|---|---|---|
| 0202 frozen bovine meat (mostly Indian buffalo meat) | 676 | India 72.4%, Australia 10.3%, Canada 8.9%, United States 5.3% |
| 0203 pork | 286 | Russia 45.5%, Brazil 36.6%, Germany 5.8% |
| 0206 edible offal of pigs and bovines | 211 | Germany 21.9%, Russia 20.1%, India 16.9%, Australia 10.0%, Poland 7.8% |
| 0207 poultry meat and offal | 279 | United States 35.7%, Korea 24.3%, Poland 14.4%, Brazil 10.2% |
| 0102 live bovine animals | 199 | Australia 95.2% |
| 0402 milk and cream, concentrated (milk powder) | 478 | New Zealand 52.0%, United States 20.5%, France 8.2%, Belgium 6.9% |
| 0405 butter and milk fat | 66 | New Zealand 90.5% |
| 0406 cheese | 81 | New Zealand 30.3% |

**Vietnam-reported net weights look incomplete.** For the same 2023 flows, exporters report larger tonnages than Vietnam does at similar values: India reports 192,180 t of frozen bovine meat (0202) shipped to Vietnam against 75,537 t in Vietnam's report (values USD 565 million and USD 489 million); the United States reports 117,694 t of poultry (0207) against 54,382 t (values USD 119 million and USD 100 million) (raw file `raw/mirror_X_to_VNM_2023.json`) [VN-direct, High, MIM-01; MIM-02]. Values agree far better than weights, and the Vietnam-reported unit values (USD 6.5 per kg for Indian bovine meat, USD 1.8 per kg for US poultry) are implausibly high for these products. We therefore use Vietnam-reported values, and for tonnage we prefer Vietnamese customs totals as relayed by the Department of Import and Export (below) or mirror data. We do not average them.

**2024 and 2025, mirror data (exporter-reported, USD million and t)** [VN-direct, High, MIM-02]:

| HS line | 2024 | 2025 |
|---|---|---|
| 0202 from India | 595 (179,720 t) | 624 (170,561 t) |
| 0203 from Brazil | 124 (52,427 t) | 145 (57,317 t) |
| 0206 from India | 156 (49,045 t) | 187 (51,759 t) |
| 0206 from Germany | 40 (39,351 t) | 52 (52,839 t) |
| 0207 from the United States | 157 (136,865 t) | 110 (69,025 t) |
| 0207 from Korea | 73 (57,098 t) | 75 (57,070 t) |
| 0207 from Poland | 56 (44,985 t) | 42 (37,379 t) |
| 0207 from Brazil | 9 (12,029 t) | 27 (26,157 t) |
| 0402 from New Zealand | 148 (48,568 t) | 231 (66,049 t) |
| 0102 from Thailand | 55 (25,245 t) | 232 (106,060 t) |
| 0102 from Australia | 112 (32,144 t) | 76 (17,643 t) |

Russia, the largest pork supplier since 2023, does not report to Comtrade, so mirror totals understate pork.

### 1b. Vietnamese customs totals for 2025 and January to July 2026 (relayed by MOIT's Department of Import and Export and the press)

- **2025:** 978.3 kt of "meat and meat products" (*thịt và các sản phẩm từ thịt*) worth USD 2.004 billion, up 11.6% in volume and 12.2% in value on 2024 [VN-direct, Medium, MIM-04; MIM-05; MIM-06]. By volume, poultry meat and by-products were 36.77% (about 360 kt, our calculation) and frozen buffalo meat 17.68% (about 173 kt, our calculation; 31.85% of value) [VN-direct, Medium, MIM-05]. Pork (fresh, chilled, frozen) was 183.4 kt worth USD 418.54 million, up 18.75% in volume, at an average of USD 2,273 per t (down 2.8%); Russia supplied 48.44% and Brazil 30.91% [VN-direct, Medium, MIM-06]. India was the largest origin of all meat: 188.7 kt, USD 681.32 million, 19.29% of volume (188.7 / 978.3; about 34% of value, our calculation) [VN-direct, Medium, MIM-04; MIM-05]. The customs buffalo-meat tonnage (about 173 kt) is close to India's own export figure for frozen bovine meat to Vietnam in 2025 (170,561 t), which supports the customs tonnages over the Vietnam-reported Comtrade weights.
- A second press report of MAE figures gives about USD 1.95 billion for 2025, with buffalo meat 31% of value, pork 21.6%, poultry and by-products 18.06%, beef 13.7% and offal 12.8%, and India at 168 kt and USD 601.8 million [VN-direct, Low, MIM-07]. The two differ (USD 1.95 billion against USD 2.004 billion; India 168 kt against 188.7 kt), probably because one is a preliminary or 11-month figure. We take the customs figure relayed by the Department of Import and Export and log the difference.
- **India in 2026.** About 108,200 t of meat, mostly frozen buffalo, worth USD 462.8 million came from India in the first half of 2026 (about USD 4.28 per kg, our calculation); in the second quarter volume rose 40.9% and value 78.3% year on year [VN-direct, Medium, MIM-26]. Indian buffalo meat export prices rose from USD 3,236 per t (2024 to 2025) to USD 4,392 per t in the second quarter of 2026 [VN-direct, Low, MIM-28]. One report puts Vietnam's intake of Indian buffalo meat at about 300,000 t a year, far above customs (188.7 kt of all meat from India in 2025) and India's own Comtrade report (222 kt of frozen bovine meat and offal) [VN-direct, Low, MIM-28; MIM-04; MIM-02]. We keep the customs figure and log the gap: it may reflect shipments routed through Vietnam that never enter its customs records.
- **January to July 2026:** 595.7 kt worth more than USD 1.7 billion, up 11.4% in volume and 32.4% in value on the same period of 2025. Poultry meat and by-products 217,371 t at about VND 26,500 per kg; pork 112,090 t (up 27.1%) at USD 1,638 per t (down 38.4% on a year earlier; about VND 42,600 per kg at 26,000 VND per USD, our conversion; the press gives about VND 42,000); buffalo meat about 112,500 t [VN-direct, Medium, MIM-10; MIM-11; MIM-09].

**Growth.** By Vietnam-reported value, meat and offal imports rose about fivefold from USD 301 million in 2015 to USD 1,506 million in 2023 (our sum, MIM-01), and the customs figure for 2025 is USD 2.004 billion (MIM-04). The steps up came in 2019 and 2020, when African swine fever cut the pig herd, and imports did not fall back afterwards [VN-direct, High, MIM-01, revealed]. Live cattle imports fell from USD 686 million (2020) to USD 199 million (2023) as Australian supply tightened, then Thailand's reported exports of live cattle to Vietnam jumped to USD 232 million (106,060 t) in 2025 [VN-direct, High, MIM-01; MIM-02]. Dairy imports (0401 to 0406) rose from USD 525 million in 2015 to USD 793 million in 2023 by Vietnam's report [VN-direct, High, MIM-01], and customs gives USD 1.44 billion for "milk and milk products" in 2025, up 27.3%, with New Zealand at 30.5% [VN-direct, Medium, MIM-12]. The customs dairy group is wider than HS 0401 to 0406 (it probably includes some preparations), so the two series are not comparable.

**What is imported (2023 detail at HS 6-digit, Vietnam-reported values)** [VN-direct, High, MIM-01]:

| Line | What it is | USD million, 2023 |
|---|---|---|
| 0202.30 | Frozen boneless bovine meat (Indian buffalo meat dominates) | 660 |
| 0203.29 | Frozen pork cuts, other than hams and shoulders | 279 |
| 0207.14 | Frozen chicken cuts and offal (leg quarters, wings, feet, mechanically deboned meat) | 213 |
| 0206.49 | Frozen pig offal (other than livers) | 149 |
| 0206.29 | Frozen bovine offal | 55 |
| 0207.12 | Frozen whole chickens (includes spent hens) | 54 |
| 0402.10 | Skim milk powder (fat 1.5% or less) | 332 |
| 0402.21 | Whole milk powder | 139 |

Vietnam-reported weights for these lines are incomplete (see above), so we do not quote 2023 tonnages from them.

### 2. Share of domestic consumption

| Food (2025) | Imports | Domestic production | Import share of supply | Source and basis |
|---|---|---|---|---|
| Pork | 183.4 kt (customs, product weight) | about 3,897 kt carcass (NSO live weight times 0.723, BLA-030) | about 4.5% (our calculation; mixes product and carcass weight) | MIM-06; MAC-14 |
| Pork | 151 kt CWE | 3,935 kt CWE | 3.7% of consumption (151 / 4,073) | USDA PSD, MIM-03 |
| Pork | | | 3.9% (OECD-FAO self-sufficiency 96.1%) | QNT-01 (BLA-033) |
| Poultry | about 360 kt meat and by-products (customs, 36.77% of 978.3 kt) | about 1,821 kt carcass (NSO live weight times 0.70, BLA-031) | about 16.5% (our calculation; includes feet and other by-products) | MIM-05; MAC-14 |
| Chicken | 175 kt | 1,430 kt | 11.0% of consumption (175 / 1,595) | USDA PSD, MIM-03 |
| Poultry | | | 12.5% (OECD-FAO self-sufficiency 87.5%) | QNT-01 (BLA-034) |
| Beef and buffalo | about 173 kt buffalo meat plus beef (tonnage not reported) | about 320 kt (OECD-FAO 2025 production 321.5 kt) | above 35% (our calculation, Low) | MIM-05; QNT-01 |
| Beef and veal | 135 kt CWE | 285 kt CWE | 32.1% of consumption (135 / 420) | USDA PSD, MIM-03 |
| Beef | | | 47.8% (OECD-FAO self-sufficiency 52.2%) | QNT-01 (BLA-035) |
| Milk | USD 1.44 billion of milk and milk products | 1.3 Mt fresh milk (MAC-14) | domestic fresh milk meets about 40% of demand (association claim) | MIM-12; MIM-13 |

Readings:

- **Pork is about 96% domestic on every source.** Imports are 4 to 5% of supply, though rising fast (+18.75% in 2025, +27.1% in January to July 2026) [VN-direct, Medium, MIM-06; MIM-10; MIM-03; QNT-01, revealed].
- **Poultry is 11 to 17% imported** depending on whether feet, offal and spent hens are counted. The customs basis gives the higher figure. We take USDA's 11% for chicken meat and the customs-based 16.5% for all poultry meat and by-products as two different measures, and do not average them [VN-direct, Medium, MIM-03; MIM-05].
- **Beef and buffalo meat are the most import-dependent meats: about one third to one half imported.** USDA puts it at 32% (2025), OECD-FAO at 48%. Part of the Indian buffalo meat landed in Vietnam has historically moved on to China informally (MIM-14), so the share eaten in Vietnam is uncertain. Imported live cattle (Australia, Thailand) are slaughtered in Vietnam and counted as domestic production, which hides further dependence [VN-direct, Medium, MIM-03; QNT-01; MIM-14].
- **Dairy is the most import-dependent protein food overall:** domestic fresh milk meets about 40% of demand on the dairy association's figure, against national targets of 70 to 72% of processing needs by 2030 [VN-direct, Low, MIM-13, claim].
- **All meat together.** Imports of 978.3 kt of meat and meat products in 2025 compare with roughly 6.0 Mt of domestic carcass meat (pork 3.9 Mt, poultry 1.8 Mt, bovine about 0.3 Mt; our calculation), so imports are roughly one-seventh of meat supply by weight. The figure overstates the share of meat eaten, because imports include feet, offal and re-exported buffalo meat and are counted in product weight [VN-direct, Low, MIM-04; MAC-14; QNT-01, inferred].

### 3. Prices, producer complaints and trade defence

**Imported meat lands well below the domestic price per kilogram, but it is a different product.**

| Product | Imported (CIF, before duty and VAT) | Domestic comparator | Gap | Evidence |
|---|---|---|---|---|
| Pork, frozen (2025 average) | USD 2,273 per t, about VND 59,100 per kg at 26,000 VND per USD | Live pig VND 62,000 to 69,000 per kg in early January 2026, about VND 85,800 to 95,400 per kg carcass equivalent at the package dressing yield of 0.723 (BLA-030) | imported about 31 to 38% cheaper (our calculation) | [VN-direct, Medium, MIM-06; MIM-07, revealed] |
| Pork, frozen (January to July 2026) | USD 1,638 per t, about VND 42,600 per kg | same | about 50 to 55% cheaper (our calculation) | [VN-direct, Medium, MIM-09; MIM-07, revealed] |
| Poultry meat and by-products (January to July 2026) | about VND 26,500 per kg | Fresh farm-gate chicken | "30 to 40% cheaper" (Southeast Livestock Association claim); farmers losing at least VND 30,000 per bird (claim) | [VN-direct, Low, MIM-10, claim] |
| Chicken parts (2020) | VND 18,000 to 25,000 per kg wholesale (US leg quarters cheapest) | Domestic white broilers VND 21,000 to 22,000 per kg live, cost at least VND 35,000 per kg (association) | | [VN-direct, Low, MIM-08; MIM-24, claim] |
| Indian meat, mostly frozen buffalo (H1 2026) | 108,200 t for USD 462.8 million, about USD 4.28 per kg (our calculation) | We found no matched domestic beef wholesale price | | [VN-direct, Medium, MIM-26, revealed] |

The comparison flatters imports: the imported pork is frozen cuts and trimmings rather than warm whole carcasses, the CIF price excludes the 10% MFN duty, VAT, cold storage and distribution, and imported poultry includes feet, wings and spent hens that have no domestic equivalent at the same price. Vietnamese shoppers pay a premium for fresh meat (about 80% of fresh meat value still goes through traditional channels [VN-direct, Low, CHN-18], see DG-223), so frozen imports compete mainly in processing, catering and restaurants.

**The structural cost gap is large and does not depend on subsidies.** OECD farm-gate producer prices for pigmeat in 2024 were USD 3,714 per t in Vietnam against USD 1,306 in Brazil, USD 1,910 in Russia, USD 2,137 in the United States and USD 2,256 in the EU, so Vietnamese pig producers received 1.6 to 2.8 times the price in the origin countries (our calculation from MIM-15). For bovine meat the 2024 Vietnamese producer price (USD 6,862 per t) was about 5 times India's (USD 1,353 per t) [VN-direct and general, Medium, MIM-15, revealed]. The press explanation in 2026 matches this: Brazil and the United States have cheap maize and soy and very large scale, and "feet, wings, certain by-products that export markets don't consider high-value products sell very well in Vietnam" [VN-direct, Low, MIM-11].

**Complaints.** Producer complaints about cheap imported poultry date from 2014 (Southeast Livestock Association). In 2020 officials of MOIT's Trade Remedies Authority said there were "clear signs" of dumping in US chicken legs, Brazilian chicken and Korean spent hens, but that no petition had been lodged: a petition needs producers with at least 25% of output, and the foreign-invested integrators that hold about 70% of industrial poultry output (CP, Japfa, Emivest) would not supply data [VN-direct, Low, MIM-08; MIM-24]. In September 2026 the Southeast and Dong Nai livestock associations again blamed cheap imports for losses, and the Vietnam Livestock Association called for stricter import rules, but none of the 2026 articles mentions a trade-defence petition, and one attributes cheap imports to scale, feed and by-products rather than subsidies or dumping [VN-direct, Low, MIM-10; MIM-11].

**Trade defence.** The Trade Remedies Authority's list of Vietnam's own investigations (about 50 cases: steel, chemicals, fibres, film, sugar, MSG) includes no case on meat, poultry, offal or dairy [VN-direct, Medium, MIM-25]. Vietnam has used trade remedies on an agricultural product (sugar), so the absence for meat reflects the lack of a petition, not a lack of tools. We found no safeguard or anti-subsidy action on meat or dairy.

### 4. The subsidy hypothesis

**What the WTO allows.** Under the 2015 Nairobi Ministerial Decision on Export Competition, developed members eliminated export subsidies immediately (with exceptions for some processed, dairy and swine products to the end of 2020), developing members by the end of 2018 (some to the end of 2022), and developing members could cover export marketing and transport costs until the end of 2023. Export credits are limited to 18 months [general, High, MIM-17]. So direct export subsidies on meat and dairy to Vietnam should no longer exist from WTO members that comply. India's export schemes (including MEIS) were found to be prohibited export subsidies by a WTO panel in 2019; the dispute ended by mutual agreement in 2023 [general, High, MIM-18]. We found no MEIS or RoDTEP rate for buffalo meat in what we read, so we cannot say whether buffalo meat benefited.

**Producer support at the main origins (OECD, 2022 to 2024).** The producer nominal protection coefficient (NPC) compares the price farmers receive (including output payments) with the border price; 1.00 means no price support. The %PSE is all support to farmers, of any kind, as a share of gross farm receipts [MIM-15; MIM-16]:

| Origin and what it sends Vietnam | Producer NPC, 2022 / 2023 / 2024 | Total %PSE (all farming), 2022 to 2024 | Reading |
|---|---|---|---|
| United States: poultry leg quarters, offal, milk powder | poultry 1.00 / 1.00 / 1.00; pigmeat 1.00; beef 1.00; milk 1.00 | 6.8 to 7.2% | No commodity price support for any product it ships to Vietnam; maize and soybean NPC 1.00 |
| Brazil: pork, chicken | poultry 1.00 all years; pigmeat 1.00 / 1.00 / 1.66 | 4.4 to 7.5% | No support for poultry. Pigmeat shows a price gap in 2024 (domestic price above export parity; market price support USD 2.79 billion). OECD books USD 0.72 billion of it as budgetary transfers, but that equals the gap times exported volume (USD 520.8 per t times 1.39 Mt; our check), an accounting identity rather than an identified payment |
| Russia: pork, offal, poultry | pigmeat 1.65 / 1.30 / 1.19; poultry 1.07 / 1.04 / 1.01; beef 1.17 / 1.18 / 1.13 | 3.3 to 4.8% | Border protection keeps the domestic pig price above the export price. Grain export restrictions also cut domestic maize prices (maize NPC 0.61 to 0.85), which OECD counts as an implicit feed transfer to pig producers of USD 212 million (2024) to USD 791 million (2022) |
| EU (Germany, Poland, Spain, Netherlands): pig offal, pork, poultry, milk powder | pigmeat 1.00 / 1.04 / 1.02; poultry 1.30 / 1.45 / 1.41; beef 1.20 / 1.46 / 1.59; milk 1.00 | 14.9 to 17.2% | Tariffs raise EU poultry and beef prices above world prices; pigmeat and milk near world prices. Large decoupled payments are not tied to any product |
| India: buffalo meat, buffalo offal | beef and veal 0.90 / 0.82 / 0.78; milk 0.60 / 0.73 / 0.61 | -19.6 to -10.0% | Negative support: producers receive less than the border price. Buffalo meat is a by-product of the dairy herd |
| Korea: spent hens (whole frozen chicken) | poultry 1.00 / 1.21 / 1.00; pigmeat 1.70 to 1.76 | 40.1 to 41.1% | Heavily supported farm sector overall, but little poultry price support in 2022 and 2024; spent hens are a by-product of egg production |
| Australia: live cattle, beef, milk powder | all 1.00 (milk 2022 missing in the extract) | 2.4 to 3.1% | No support |
| New Zealand: milk powder, butter, cheese | all 1.00 | 0.7 to 1.6% | No support |
| Canada: pork, offal, beef | pigmeat 1.00; beef 1.00 / 1.01 / 1.03 | 7.7 to 9.1% | No support for what it ships (its supply-managed dairy is not exported to Vietnam in volume) |

Evidence: [general, High, MIM-15; MIM-16, revealed]. Raw extracts: `raw/oecd_comm_selected.csv`, `raw/oecd_comm_feed_npc.csv`, `raw/oecd_pse_selected.csv`.

Readings:

1. **For most of what Vietnam imports, the origin gives no commodity-specific support.** US poultry, Brazilian poultry, Australian cattle and beef, New Zealand and US milk powder and Canadian pork all show an NPC of 1.00 in 2022 to 2024. Indian buffalo meat, the largest single import by value, is negatively supported. India alone supplied about 34% of the 2025 import value (our calculation from MIM-04) [general, High, MIM-15; VN-direct, Medium, MIM-04].
2. **Where support exists it mostly works by keeping imports out of the origin market, which raises domestic prices there.** This can make it attractive to sell surplus or low-value cuts abroad below the domestic price (price discrimination), which is what MOIT officials called "signs of dumping" in 2020. It is not a payment that lowers the export price, and no Vietnamese authority has tested it [general, Medium, MIM-15; MIM-24, inferred].
3. **Russia is the one clear case of support that lowers production cost.** Russian pig producers get border protection and cheaper feed through grain export restrictions (OECD's negative excess feed cost). Russia supplied 48% of Vietnam's pork imports in 2025, about 89 kt (our calculation from MIM-06) [general, High, MIM-15; VN-direct, Medium, MIM-06]. Russian veterinary data put pork exports to Vietnam at 52,300 t in 2025 [VN-adjacent, Low, MIM-19]; the gap with Vietnamese customs is unexplained (probably product coverage).
4. **We found no study that measures how much origin support lowers the price at which meat reaches Vietnam.** The evidence above is about support in general, not about the Vietnam trade.
5. **The cost gap is the bigger force.** Vietnamese farm-gate pig prices in 2024 were 1.7 times the US price and 2.8 times the Brazilian price, although US pig producers received no price support at all (our calculation from MIM-15). Removing all origin support would not close that gap.

**Verdict on the hypothesis.** The claim "Vietnam relies on subsidised imported meat protein" is not supported. Vietnam imports little of its pork (4 to 5%), a moderate share of its poultry (11 to 17%, much of it by-products), and a large share of its beef and buffalo meat (32 to 48%) and dairy (about 60%). The origins of most of these imports give no commodity-specific price support, and the largest origin by value (India) taxes its producers rather than supports them. Russia's pork is the exception, at about 89 kt or 9% of 2025 meat import volume (our calculation).

### 5. Tariffs

`data/tariffs.csv` has no meat or dairy lines. MFN applied rates in 2023 (WITS TRAINS, national lines averaged per HS 6-digit) [VN-direct, High, MIM-20]:

| HS 6-digit | Product | MFN 2023 | Later change found |
|---|---|---|---|
| 0201.30 / 0202.30 | Boneless beef, fresh or frozen (includes buffalo meat) | 14% | none found |
| 0203.22 / 0203.29 | Frozen pork, hams and other cuts | 10% | none found |
| 0206.29 / 0206.49 | Frozen bovine and pig offal | 8% | none found |
| 0207.12 | Frozen whole chickens | 40% | none found |
| 0207.14 | Frozen chicken cuts and offal | 20% | frozen chicken legs cut to 15% by Decree 73/2025/ND-CP (31 March 2025) [VN-direct, Medium, REG2-21; MIM-21] |
| 0402.10 / 0402.21 | Skim and whole milk powder | 2 to 5% | none found |
| 0405.10 | Butter | 13% | none found |
| 0406.90 | Cheese | 5% | none found |
| 0102.29 | Live cattle (not for breeding) | 5% | none found |

In 2019 the MFN rate on fresh or chilled pork was 25% and on frozen chicken cuts 20%; the Ministry of Finance proposed cuts because African swine fever had pushed up pork prices and shifted demand to chicken [VN-direct, Medium, MIM-23]. Frozen pork was at 10% by 2023 (MIM-20).

**FTA phase-downs.** Under EVFTA, duties on EU beef reach 0% after 3 years, frozen pork after 7 years, other pork after 9 years and chicken after 10 years; about 44% of dairy lines are free at once or after 3 years and the rest after 5 years [VN-direct, Medium, MIM-22]. With entry into force in 2020, that puts EU frozen pork at 0% by about 2027 and EU chicken by about 2030 (our reading of the year count). For CPTPP we found only a search snippet saying frozen pork reaches 0% in year 8 and fresh pork in year 10 (Low, not read). We could not read year-by-year rates under CPTPP, RCEP, AANZFTA, AIFTA (India) or the Vietnam to Eurasian Economic Union FTA (Russia): the national trade repository (VNTR) loads them by script, and WITS returned no preferential rows. A Russian trade newsletter credits the Vietnam to EAEU FTA for Russian pork's growth (claim, Low, MIM-19).

**What this means.** Tariffs on the largest import lines are modest (8 to 15%) and falling under FTAs. The OECD measures show no effective price protection for Vietnamese pig producers (NPC 1.00 in 2022 to 2024) but substantial protection for beef (NPC 1.32 to 1.48), while Vietnamese poultry producers receive less than the OECD border reference price (NPC 0.52 to 0.60) [VN-direct, Medium, MIM-15]. The poultry figure may partly reflect the incomplete import weights we found in Vietnam's Comtrade data, which would overstate the import unit value OECD uses as a reference (our inference, Low).

### 6. Could alternative protein for human food substitute for these imports?

| Import | What it is used for | Plausible alternative-protein substitute? | Scale at the study's benchmark path |
|---|---|---|---|
| Frozen pork cuts and trimmings (183 kt, 2025) | processing (sausage, *giò chả* pork rolls, meatballs), catering, restaurants | Partly. Processors already extend meat with soy: 22 of 67 Vissan meat formulations list soy (ch14). A domestic extender or blend ingredient replaces some lean, which may be imported or domestic. | Hybrid processed meat (route R3) displaces about 0.7 kt of meat protein by 2035 (D-BENCH, DMO-0258), against roughly 27 kt of protein in 2025 pork imports (183.4 kt times 0.15, our calculation) |
| Poultry leg quarters, wings, feet; spent hens (about 360 kt) | cheap fresh-cooked dishes, street food, kitchens; feet as a snack | Mostly no. Bone-in parts and feet are eaten as themselves; alternative protein is a different product. Mechanically deboned meat for sausages is the exception (same as pork above). | none modelled |
| Frozen buffalo meat (about 173 kt) | restaurants, *phở*, collective kitchens, processing, dried meat; some moves on to China | Only in processed and catering uses; not in *phở* or dried meat sold as meat | none modelled |
| Pig and bovine offal | traditional dishes | No | none |
| Milk powder (about 150 kt a year) | reconstituted milk drinks, yoghurt, confectionery, infant and child formula | Partly for drinks: plant milks compete with dairy milk drinks. Not for infant formula. | High-protein plant milks (R6) deliver about 1.29 kt of protein by 2035 (DMO-0267), against about 48 kt of protein in 2023 milk powder imports (our calculation: 108,786 t skim at 36.2% protein plus 34,132 t whole at 26.3%, MIM-01; MIM-27) |

**Scale check.** Imported meat and meat products carried roughly 147 kt of protein in 2025 (978.3 kt times the package's 0.15 kg protein per kg, DMA-001; our calculation, Low because imports are product weight with bone and offal). The benchmark demand path delivers 19.05 kt of protein from domestic or novel sources by 2035 but displaces only 2.35 kt of meat protein (DMO-0271; DMO-0273). Even if every displaced tonne came out of imports, that is about 1.6% of today's imported meat protein (our calculation). Alternative protein for food at the study's scale would make no material difference to meat or dairy import dependence. It does not increase it either, except that the cheapest extender today is imported Chinese textured soy (FTR-32; ch14), so a blend made with imported soy swaps one import for another.

**Where the overlap is real.** The imported product most like an alternative-protein target is frozen pork and mechanically deboned meat bought by processors and kitchens. That is the same buyer the study already prioritises for blends (ch14, ch16). Imported frozen pork at about VND 42,600 per kg CIF (2026) is cheaper than domestic lean, so it lowers the price a blend ingredient must beat. A processor using imported trimmings at that price has less to save from extension than one buying domestic lean (our inference, Low).

## What this changes in the package

| Where | Current text or value | Proposed change | Evidence | Strength |
|---|---|---|---|---|
| `ch01-why-vietnam`, new short section after 1.2 (or in 1.3) | No page examines imported meat, offal or dairy | Add "A second import exposure: meat and dairy for people": 978.3 kt and USD 2.004 billion of meat and meat products in 2025 (+12.2% in value), USD 1.44 billion of dairy (+27.3%); import shares pork 4 to 5%, poultry 11 to 17%, beef and buffalo 32 to 48%, dairy about 60%; main origins India, Russia, Brazil, United States, Korea, Poland, Germany, New Zealand | MIM-04; MIM-05; MIM-06; MIM-03; QNT-01; MIM-12; MIM-13 | moderate |
| `ch01-why-vietnam` section 1.6 (what the case rests on) | Supply security rests on feed imports | Add one sentence: the hypothesis that Vietnam relies on subsidised imported meat is not supported; most imported meat and milk comes from origins with no commodity price support (OECD NPC 1.00) or, for Indian buffalo meat, negative support; Russia's pork is the partial exception; alternative protein for food at benchmark scale would displace at most about 1.6% of imported meat protein | MIM-15; MIM-16; MIM-17; DMO-0273 | moderate |
| `front-prologue` P.6 and both executive summaries | Feed is "the hidden import behind the meat" | Add that Vietnam also imports finished meat and dairy (figures above), concentrated in beef, buffalo meat and milk powder, and that this import is not driven by origin subsidies | as above | weak |
| `app-f4-balance-model` and `data/balance_assumptions.csv` BLA-033 to BLA-035 (notes only) | Self-sufficiency held constant from OECD-FAO 2025: pork 0.961, poultry 0.875, beef 0.522 | Keep the values. Add to notes: 2025 customs and USDA data agree for pork (3.7 to 4.5% imported); poultry including by-products is about 16.5% imported on a customs basis (self-sufficiency about 0.835, near the SENS-LOW 2040 value of 0.825); beef self-sufficiency is 0.68 on USDA against 0.52 on OECD-FAO; meat imports grew 11.6% in 2025 and 11.4% in January to July 2026, so "held constant" may be optimistic for poultry and beef | MIM-03; MIM-05; MIM-06; MIM-10 | weak |
| `data/open_questions.csv` OQ-009 | open: "Meat and offal imports in 2025 (volume and value); seafood export volume in 2025" | Partly closed: meat and meat products 978.3 kt, USD 2.004 billion (customs); pork 183.4 kt, USD 418.54 million; seafood export volume still open | MIM-04; MIM-06 | strong |
| `data/tariffs.csv` | No meat or dairy lines | Add 0202.30 (14%), 0203.29 (10%), 0206.49 (8%), 0207.14 (20% in 2023; frozen legs 15% from Decree 73/2025), 0402.10 and 0402.21 (2 to 5%), with EVFTA years to 0% (beef 3, frozen pork 7, chicken 10) | MIM-20; REG2-21; MIM-21; MIM-22 | moderate |
| `ch14-frontier-demand` 14.4 and `ch16-business-buyers` (blend economics) | Lean trimmings priced from domestic live hog | Add a note: imported frozen pork landed at about VND 42,600 per kg (CIF, January to July 2026), well below domestic lean; processors using imported trimmings save less from extension. Frozen pork and mechanically deboned meat for processors are the only imports that blends could plausibly displace | MIM-09; MIM-11; MIM-26 | weak |
| `data/disagreements.csv` and Appendix R2 | none on meat imports | Add the seven disagreements in `disagreements.csv` (2025 totals by agency; poultry and beef import shares by source; Indian and Russian volumes; Comtrade weights; 2026 pork outlook) | this line | moderate |
| New data files `data/meat_dairy_imports.csv` and `data/origin_support.csv` | none | Publish the two tables from this line with data-dictionary entries; reference from ch01 and app-f4 | this line | moderate |

## Next-wave candidates

1. **Where Indian buffalo meat ends up** (deeper version of this line). How much of the 170 to 190 kt landed each year is eaten in Vietnam, and how much moves on to China? This decides whether bovine import dependence is about 30% or nearer 50%. Desk research is unlikely to close it; the cheapest route is calls to two or three importers and to USDA's Hanoi office, or customs transit data from MOF. Result would change the beef figure in ch01 and app-f4.
2. **Who buys imported frozen pork and mechanically deboned meat** (different kind of question: buyers, not trade). Shares going to processors (Vissan, Masan, CP, Ha Long Canfoco), restaurant chains and industrial kitchens. Needs phone calls. If processors are the main buyers, blends compete with imported, not domestic, lean, which changes the saving a blend offers in ch14 and ch16.
3. **Year-by-year FTA rates to 2035 for the top 10 meat and dairy lines** (deeper, desk-closable with a browser). VNTR shows them but loads them by script; a person with a browser can read them in about an hour. Would complete `data/tariffs.csv`; unlikely to change a conclusion.
4. **Milk powder end uses** (different kind). Shares used for reconstituted liquid milk, formula and ingredients; decides how much plant milk could substitute. Ask the Vietnam Dairy Association or the two largest processors.
5. **Russian export support for pork** (deeper, partly desk-closable in Russian). Whether transport-cost or export-promotion subsidies apply to pork shipped to Vietnam, and the Vietnam to EAEU FTA rate for pork. Low priority: Russia's pork is about 9% of meat import volume.

Further desk work on the subsidy question would be noise: the OECD data already cover the main origins, and the remaining uncertainty is about Vietnamese buyers and onward trade, which need calls.

## Limits

- **No Vietnam-reported Comtrade data for 2024 or 2025.** We used mirror data and customs totals relayed by the press. Customs releases from the Department of Import and Export were read only as press reports (MIM-04 to MIM-06, MIM-09, MIM-10); we did not reach the customs statistics portal itself.
- **Vietnam-reported Comtrade weights are incomplete** for several meat lines (for example Indian buffalo meat and US poultry in 2023), so we did not use them; values look sound.
- **USDA FAS GAIN:** we found no Vietnam Livestock and Products, Poultry and Products or Dairy and Products annual for 2024 to 2026 (we probed report numbers 1 to 70 for VM2025 and VM2026, and 1 to 14 and 51 to 70 for VM2024, under the Hanoi and Ho Chi Minh City posts through the GAIN download API, and found none under those titles). USDA PSD numbers were used instead.
- **Codex milk powder standard** (fao.org, CXS 207-1999) returned HTTP 403; we used USDA FoodData Central composition instead.
- **nhachannuoi.vn** returned HTTP 503 for the January 2026 meat market bulletin and for the Dong Nai Livestock Association interview on cheap beef (https://nhachannuoi.vn/pho-chu-tich-hiep-hoi-chan-nuoi-dong-nai-thit-bo-gia-re-dang-lam-meo-mo-thi-truong/).
- **Preferential tariffs:** WITS TRAINS returned no partner rows; VNTR loads FTA schedules by script, so CPTPP, RCEP, AANZFTA, AIFTA and Vietnam to EAEU rates were not read. The CPTPP pork years rest on a search snippet only.
- **Search-snippet-only items** (not used as findings): customs fraud cases in which imported buffalo meat was declared as trimmings at about half its value (VnEconomy, 2025), and a Russian newsletter crediting the Vietnam to EAEU FTA for pork growth.
- **WebFetch summaries:** several Vietnamese press articles were read through an automated summary; where a summary gave an internally inconsistent number (for example a USD 2.95 per kg unit price for Indian meat in MIM-26), we did not use it.
- **Price comparisons** set CIF import prices against live-pig-based carcass equivalents and association claims; products differ (frozen cuts and by-products against fresh whole birds and carcasses), so the gaps are indicative only.
- WebSearch calls used: 14 of about 30.
