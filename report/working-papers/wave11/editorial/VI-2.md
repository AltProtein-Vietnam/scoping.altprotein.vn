# VI-2: Vietnamese-page editor log for version 0.8

Editor: VI-2. Date: 2026-10-01. Files edited: `content/00-front/front-exec-summary-vi.md` and `content/00-front/front-prologue-vi.md`. No other content, data, tile, chart, register or manifest file edited. No commit or push.

Checks at the last run: `python3 tools/validate.py` 81 pages, 0 errors, 2 warnings (see "For the consolidating editor", item 1); `python3 tools/check_registers.py` 0 errors. A Unicode-aware script found no U+2013, U+2014 or other dash characters, no spaced hyphens and no curly quotes in either file; both files are NFC-normalised. "Phiên bản 0.7", the draft notice and "không dùng để trích dẫn" are unchanged.

## Token comparison (English against Vietnamese, in order)

A script extracts, in order, every citation `[@...]`, evidence tag, `{fx:...}`, `{dx:...}`, cross-link `[[...]]` and embed `{{kn:...}}` / `{{chart:...}}` from the page body, and compares the two sequences; it also compares the frontmatter `key_numbers`, `charts` and `related_data`.

| Pair | EN tokens | VI tokens | Differences | Frontmatter |
|---|---|---|---|---|
| front-exec-summary / -vi | 54 | 55 | Two, both deliberate: the opening line links `[[front-prologue-vi]]` where the English links `[[front-prologue]]`, and adds `[[app-r3-glossary]]` (bilingual glossary) at the end of that line | `key_numbers` identical, same order (32 tiles); `charts` [] in both; no embeds in either page |
| front-prologue / -vi | 221 | 221 | One, deliberate and already there: P.6 links `[[front-exec-summary-vi]]` where the English links `[[front-exec-summary]]` | `key_numbers`, `charts`, `related_data` identical |

Before editing, the prologue pair differed by 22 tokens (the four FI-3 additions); the summary pair differed in its whole food-security section and in the About links. A second script compared numbers (Vietnamese format normalised): every number in each English page appears in its Vietnamese page. The only extra digits in the Vietnamese pages are words written as digits in Vietnamese ("dưới 5 tuổi", "kế hoạch 5 năm", "6 đến 9 lần"), "CO2", "2026" in the report title, and "/100 g" after "10 g đạm" (the English implies per 100 g).

## front-exec-summary-vi

Rewritten in full as a Vietnamese version of the current English page, section by section, in the same order. Short sentences, main point first, plain words, each technical term explained on first use with the English term in brackets where it helps.

| section | change | type |
|---|---|---|
| Frontmatter | `summary` rewritten from the English: a security case, "có cơ sở nhưng hẹp"; two thirds of animal protein on imports; only domestic inputs reduce it; openings T1, T4, T5; firms buy ingredients; new-food clause. `key_numbers` replaced by the English list exactly (removed kn-fishmeal-aug-2026, kn-cost-fungal-feed, kn-efficiency-vs-alt, kn-vision-sbm-2050, kn-vision-microbial-share-2050; added kn-meat-intake-2020, kn-aerobic-volume, kn-imported-protein-ingredient-share, kn-hawkwood-regulatory-score and the 12 food-security tiles). `related_pages` mirror the English (adds front-at-a-glance, ch01, ch11, ch20, ch30, app-m5; keeps front-prologue-vi, front-exec-summary, app-r3-glossary as the language pair). `reading_time_min` 17 (unchanged; 5,694 syllables at the page's existing rate of about 340 a minute) | reframed for food |
| Opening | Draft notice moved above the italic line, as in English; italic line now also links the two-minute page (English only) | clear language only |
| Scope paragraph | "Trước hết là protein cho con người; thức ăn chăn nuôi chỉ là bối cảnh": replaces the v0.7 supply-case paragraph and "phạm vi gồm cả thực phẩm và thức ăn chăn nuôi" | reframed for food |
| Why Vietnam | Rebuilt on the English: meat intake 136,4 g against 50 to 80 g; 42%; about 90% of meat produced at home (2023) on imported feed; 99% and 74%; USD 10 billion; African swine fever; "lý do an ninh có cơ sở nhưng hẹp". Removed USD 11.3 billion seafood exports and the August 2026 fishmeal price | pruned feed |
| New section "An ninh lương thực: bằng chứng cho thấy gì, và không cho thấy gì" | Intro and seven bullets as in English: 19% to 23%, 61% to 71%, 97,5%, milk about 30% (FAO); 978.000 t, USD 2.0 billion, no origin subsidy, at most 1,6% by 2035; consumer pork +57,23% in 2020, licensed vaccines do not protect against recombinant strains (Bộ Nông nghiệp và Môi trường); no evidence of lower disease risk, culls 8,4 times the pigs spared; 84% from China, only domestic inputs reduce dependence; marine fish stock 22,1% lower; Resolution 34/NQ-CP has no import or protein indicator, national protein balance first | reframed for food |
| Findings 1 to 10 | Feed points removed as in English: insect meal and Chinese microbial protein (1); 269 feed mills (4); aquafeed trials and research-intensity ratio (5); livestock and aquafeed lists (6); fishmeal and soybean-meal comparators and aquafeed ingredient (8); "two families fit now" with microbial feed ingredients, and duckweed feed (9). Entobel now stated as an insect-feed deal outside the scope (7). Fungal cost now "đạm sinh khối nấm", 54 to 67% capital and maintenance, against food comparators (8). Detail cut as in English (imported cassava, Tay Ninh, Indonesia and Thailand, E10, state VC funds) | pruned feed |
| Demand 1 to 9 | Shortened as in English; meat-intake sentence moved to Why Vietnam; "giá lợn hơi" now "giá lợn hơi xuất chuồng" (producer price, FI-3 item 5); lean pork VND 71,000, seventh-month sales, Singapore servings, 84% non-GM premium, 22 of 67 recipes, Decision 3958, canteen meal price, hotels, HS 3504, Vinamilk, US 12.5% tariff, HS 1902.20 and USD 128 million, the BAP and 9,200 t yeast sentence all removed as in English | pruned feed / clear language only |
| Futures 1 to 5 | "nhiều thức ăn hỗn hợp" and smallholder pigs removed; 2 and 3 lead with meat protein people eat (1,01 to 1,45 Mt), soybean meal behind it, 4,5 t and 9,5 t per t, 0,4% in 2050; efficiency now one context sentence; 4 million ha abroad and omega-3 removed; 4 now USD 3,3 to 6,5 per kg in 2050 and the food window from about 2028 (fishmeal parity and 2040 to 2045 window removed); 5 axis now "nguồn đạm nhập khẩu (thức ăn chăn nuôi đằng sau thịt trong nước, và thực phẩm giàu đạm nhập khẩu)". World names kept as in v0.7 | reframed for food |
| Vision callout | Soybean-meal 7 to 9 Mt, microbial 4 to 8% and omega-3 15 to 50% goals removed; new vision from the English: measured, more diverse, more secure; 67.000 to 172.000 t, of which 59.000 to 147.000 t made in Vietnam; meat stays the main protein | reframed for food |
| What to do | "Mười hướng đi" to "Bảy hướng đi; ba hướng dẫn đầu với gần như mọi bộ trọng số" (T1, T4, T5); T2 removed; T9, T10, T7, T8 paragraph; three feed plays retired; four public goods (explained). Policy: four to three options (feed-list items removed; novel-food procedure in the decree added); public feed trials removed from outlays. Eleven to ten product profiles, twenty-one to twenty demand moves. Nine to seven no-regret moves, listed as in English | pruned feed |
| Actor check | Shortened to the six English bullets (start-up register detail, ethnic-minority stunting, animals spared, label thresholds cut) | clear language only |
| For each reader | Feed advice removed (Entobel template, feed-list fixes, listed feed materials, functional feed additives, soy-wastewater protein for shrimp, public feed trials); the four food-security sentences added (investors, policy, research, international) | pruned feed |
| What would change our view | Fishmeal item removed; tolling item now T5 and food-fermentation plays; microbial protein now "dùng cho thực phẩm"; new last item on measured zoonotic or antimicrobial-resistance risk | pruned feed |
| Closing and About | "Hai mươi" to "Mười tám câu hỏi ..., bốn câu trong số đó về an ninh lương thực"; "mười đợt (2.384 nguồn)" to "mười một đợt (2.474 nguồn)"; About links reduced to those in English (app-m2, app-m3, app-m4 dropped) | reframed for food |

## front-prologue-vi

Only the FI-3 prologue items were mirrored; everything else was left as E17 wrote it.

| section | change | type |
|---|---|---|
| Frontmatter | `related_data` + meat_dairy_imports.csv, origin_support.csv; `related_pages` + app-d8-demand-model (after ch22, as in English); `reading_time_min` 19 to 20 (7,007 syllables at the page's existing rate of about 342 a minute) | clear language only |
| Method note | Adds that the notes on disease risk and imported meat and dairy are in `working-papers/wave11/` (FI-3 item 1) | clear language only |
| P.3 item 2 | New paragraph after the swine fever sentence: a second source helps because it does not fail when animals fall sick; not the same as lowering disease risk (P.4); about 142.000 pigs spared in 2035 against 2025 culls 8,4 times that `[@MAC-01; @PAN-03]` `[[app-d8-demand-model]]` {VN-direct\|Low} {fx:estimate} (FI-3 item 2) | reframed for food |
| P.3 item 5 | "Các con số này cho thấy nguy cơ đến từ đâu; chúng không cho thấy việc thay thịt làm giảm nguy cơ đó (mục P.4)" after the 60% and 72% sentence (FI-3 item 3) | reframed for food |
| P.4 | New bullet "Nguy cơ dịch bệnh phụ thuộc vào cách chăn nuôi và buôn bán động vật" after "Chế biến và sức khỏe", with PAN-27, PAN-30, PAN-31, PAN-28, PAN-29 and the ch01 link, tags as in English (FI-3 item 4) | reframed for food |
| P.4 New dependencies | Adds the 84% from China sentence `[@BUY-02]` {VN-direct\|Medium}; conclusion narrowed to "cần nguyên liệu đầu vào trong nước, chứ không chỉ đổi sang sản phẩm khác hay đặt nhà máy ở Việt Nam" with links ch01 and ch16 (FI-3 item 5). **Conclusion narrowed** | reframed for food |
| P.6 | New paragraph after the soybean paragraph, before the tile: meat and dairy imports (978.000 t, USD 2.0 billion, USD 1.44 billion of dairy; frozen beef and Indian buffalo meat, skim milk powder; no origin price support for most imports; India taxes buffalo meat), MIM-04, MIM-05, MIM-12, MIM-01, MIM-15, MIM-16 with tags and {dx:revealed} as in English (FI-3 item 6) | reframed for food |
| P.2 table, blends row | Soy share already reads "22 trên 67 (33%)" (commit 14f47d1); checked, not changed | none |

## Unsure items and notes

- **Place names.** Following the brief, place and company names keep the unaccented form of the English text: "Nha Trang", "TP. Ho Chi Minh" (v0.7 had "TP. Hồ Chí Minh") and "đồng bằng sông Mekong" for Mekong Delta (v0.7 had "Đồng bằng sông Cửu Long"). Country names stay in standard Vietnamese (Việt Nam, Trung Quốc, Ấn Độ). A native reviewer may prefer the accented forms in Vietnamese text.
- **Additions for clarity, not new claims.** Glosses for textured soy, recombinant strains ("lai giữa hai kiểu gen vi rút", from ch01 section 1.3), feed conversion ratio (from the glossary), soybean meal, phytate and biosecurity. "Quốc hội" is named as the body that comments on and votes on the Food Safety Law (the English says only "first comments" and "vote"). "Bộ Nông nghiệp và Môi trường" renders "the agriculture ministry" (ch01: MAE's livestock and animal health department).
- **Terms.** "Benchmark path" and "stretch path" are now "lộ trình tham chiếu" and "lộ trình tham vọng", as in the prologue (v0.7 summary used "kịch bản tham chiếu"); "kịch bản" is kept for S-ALT and the four worlds. World names kept from v0.7 ("Nhà nhập khẩu an phận" for "Comfortable price-taker").
- **Reading times.** Both use the Vietnamese pages' own syllable rate, not the English 230 words a minute. The cover's "17 phút" for the summary now matches; the cover's "16 phút" for the prologue does not match 20 (cover not my file).

## For the consolidating editor

1. **Two tiles now unused.** `validate.py` warns that `kn-vision-microbial-share-2050` and `kn-vision-sbm-2050` are defined but not used: this page was the last to list them in its frontmatter. Retire or re-home them (brief section 2.7).
2. **Tile `pages` fields.** In `data/key-numbers.json`, front-exec-summary-vi should be dropped from the `pages` of the five removed tiles and added to the 16 added ones (list above).
3. **`site-manifest.json`** still holds the old summaries and reading times for front-exec-summary-vi (17, unchanged) and front-prologue-vi (now 20).
4. **Cover.** `front-cover.md` says "Tiếng Việt, 16 phút" for the prologue; the page now says 20.
5. **Changelog (M5.14).** Substantive changes: the Vietnamese summary now mirrors the English v0.8 summary (food-security section, seven plays, three policy steps, seven no-regret moves, new vision, eighteen unknowns, feed content removed); the Vietnamese prologue mirrors the FI-3 prologue items (disease-risk caveats, narrowed "new dependencies" conclusion, meat and dairy imports).
