# E17-prologue-vi: editorial log for version 0.8

Editor: E17-prologue-vi. Date: 2026-10-01. File edited: `content/00-front/front-prologue-vi.md` (Vietnamese prologue only). No other file edited.

Checks: `python3 tools/validate.py` reports 0 errors (2 warnings, none in this file). No em or en dash in the file (checked with a Unicode-aware script; plain `grep "[–—]"` gives byte-level false positives on Vietnamese text in a non-UTF-8 shell locale). The text is NFC-normalised.

Token check: a script extracted every citation, evidence tag, foresight and demand tag, cross-link and embed, in order, from the English and Vietnamese pages. The two sequences are identical (199 tokens each). The one difference is deliberate and was already there: P.6 links to `[[front-exec-summary-vi]]` where the English links to `[[front-exec-summary]]`. No number was changed. Vietnamese number formatting (0,83; 10.000) is kept as before. "Phiên bản 0.7" and the draft notice do not appear in the page body and were not touched. No tile or chart was added or removed.

## front-prologue-vi

| section | change | type |
|---|---|---|
| Frontmatter | `summary` adds "và vì sao nghiên cứu này bàn về protein cho con người"; `reading_time_min` 16 to 19 (about 6,700 syllables against 5,600 before, same rate as the old value); `related_pages` adds ch26-plays, ch22-protein-balance-2050, app-s6-feed-market, app-f6-aquafeed-feedstock-futures, app-m5-changelog. Title, key_numbers, charts unchanged | clear language only |
| Opening box | "Tóm lại trong một đoạn" becomes "**Tóm tắt.**" with six bullets, as in English. New scope bullet: made for food and feed worldwide; this study is about protein for people; feed only as context (the hidden import behind meat, eggs, milk and farmed fish). Motives: "an ninh lương thực và thức ăn chăn nuôi, dùng đất và thức ăn hiệu quả hơn" becomes "an ninh lương thực, dùng đất và cây trồng tốt hơn" | reframed for food |
| Method note | Adds that the prologue changes no finding, and explains the label "general" | clear language only |
| P.1 | Split into Protein, Chất lượng protein (PDCAAS, DIAAS and FAO written out), DIAAS values, crude protein (nucleic acids explained). "Protein thay thế" now "theo cách hiểu thông thường" covers food and feed; removed "Định nghĩa này cố ý bao gồm cả thức ăn chăn nuôi"; soybean meal and fishmeal explained. New paragraph "Phạm vi của chúng tôi: protein cho con người" pointing to P.6. Novel-food definitions turned into a bullet list (EU, Singapore, Mỹ, Việt Nam), same claims and citations. EFSA abbreviation dropped (used once) | reframed for food |
| P.2 table | Cells shortened and split into sentences. Insects row: "chỉ là mốc so sánh (benchmark), không phải khuyến nghị". Traditional plant row: "đang chiếm lĩnh thị trường" becomes "sản phẩm đã có chỗ đứng" (matches English "established product"). Bioreactor, scaffold, mycoprotein, heme explained. Insect row now says "nhà máy thức ăn chăn nuôi", as the English always did. Feed rows kept as global background, as in English | clear language only |
| P.2 after table | New paragraph "Ở đây, phần dùng làm thức ăn chăn nuôi chỉ là bối cảnh" (two sentences, as in English) | reframed for food |
| P.2 cost bullets | Deleted the Calysseo Chongqing sentence `[@FTG-06] {VN-adjacent\|Medium}`; the table row keeps the halt with FTG-06. "Bình duyệt" replaced by "đăng trên tạp chí khoa học có phản biện"; titer explained | pruned feed |
| P.3 intro | Actor motives as a bullet list. "an ninh lương thực và thức ăn chăn nuôi" becomes "an ninh lương thực", with "an ninh lương thực bao gồm cả thức ăn chăn nuôi nhập khẩu đứng sau thịt, trứng, sữa và cá nuôi mà người dân ăn" | reframed for food |
| P.3 item 1 | Split into two paragraphs; "Sản lượng thịt, sữa và trứng của thế giới tăng 17%" (adds "của thế giới", mirroring E16) | clear language only |
| P.3 item 2 | Reordered, main point first: more sources of protein for people mean fewer points of failure; then African swine fever (explained); then "Thức ăn chăn nuôi là điểm yếu còn lại" with the soybean-export and fishmeal sentences (numbers and citations unchanged). "USDA" written out | reframed for food |
| P.3 item 3 | Heading "Đất đai và thức ăn chăn nuôi" becomes "Đất đai và cây trồng" | clear language only |
| P.3 items 4 to 7 | Sentences split; CO2e, antimicrobials, antimicrobial resistance and bioeconomy explained; WHO written out; Group 1 and 2A wording simplified | clear language only |
| P.4 | "Người tiêu dùng" split into "Người tiêu dùng" and "Dự báo"; GFI introduced at first use; dry matter, micronutrient, kcal, LDL, life-cycle study, median and "prima facie" explained; sentences split | clear language only |
| P.5 boom, markets, rules, strategies | Paragraphs split; Nasdaq, Euromonitor, notes, "no questions" letters (FDA abbreviation removed), regulatory sandbox, cellular agriculture, DKK and China's No. 1 Central Document explained; China bullet split into China and Korea, Thailand and Japan; Singapore goal now "về sản xuất trong nước" (as English) | clear language only |
| P.5 Feed | Retitled "Thức ăn chăn nuôi: chỉ là thông tin nền"; opens with the context sentence and link to `[[app-s6-feed-market]]`. Deleted the Peru anchovy quota sentence `[@HSC-29] {general\|Medium}`. Soybean meal and fishmeal prices and the Shougang LanzaTech sentence kept as background | pruned feed |
| P.6 heading | "Việt Nam ở đâu trong bức tranh này" becomes "Việt Nam ở đâu, và nghiên cứu này bàn về điều gì" | retitled |
| P.6 strengths | Removed "những nhà máy thức ăn chăn nuôi đã mua nguyên liệu protein thay thế"; pilot capacity explained | pruned feed |
| P.6 conclusion | "doanh nghiệp đang sản xuất thực phẩm và thức ăn chăn nuôi" becomes "doanh nghiệp đang làm thực phẩm, không phải dưới dạng thương hiệu tiêu dùng"; "supply case" explained (rests on how the country makes its protein, not on consumer fashion) | reframed for food |
| P.6 scope | New paragraph "Nghiên cứu này bàn về protein cho con người": five questions as bullets; feed as context; feed ingredients not something to make; earlier drafts assessed them, with links to S6, F6 and M5 | reframed for food |
| P.6 plays | New paragraph "Việt Nam có thể làm gì trước": plays are all about food; three lead, without play codes (as English); hub and pilot and tolling explained. Wording aligned with the Vietnamese executive summary (đạm thực vật tạo cấu trúc, tinh bột sắn thành đường lên men, lên men thử nghiệm và gia công dùng chung) | reframed for food |
| P.7 table | New rows: Protein cho con người; Thức ăn chăn nuôi; Mycoprotein; Gia công (tolling). SBM and fishmeal row: context, the study does not aim to make feed that replaces them. B2B row: food only, written out. Titer row: "yếu tố then chốt" becomes "một yếu tố chính". Scenario row explains S-ALT and D-BENCH and links ch22 (wording from the Vietnamese executive summary: "kịch bản tham chiếu"). Play row: seven plays, all about protein for people | reframed for food |

Language: written in short sentences with the main point first, plain words where they exist (for example "làm ra", "dùng", "bắt đầu" rather than "triển khai", "tận dụng", "khả dĩ", "chiếm lĩnh"), each technical term explained at first use with the English term in brackets where useful. Full diacritics throughout.

## Unsure items

- **"World output ... 17%".** Mirrors E16's addition of "World" ("của thế giới"). E16 did not re-read PRB-04; neither did I.
- **Heme gloss.** "một protein hãng dùng để tạo vị" mirrors E16's plain-language gloss; it is not a separately sourced claim.
- **Fishmeal context kept.** The P.3 fishmeal supply and price sentence stays, as in English. If the consolidating editor prunes it from the English page, prune it here too.
- **"truyền thống đạm thực vật vững mạnh"** renders "a strong plant-protein tradition"; a native reviewer may prefer other wording.
- **Reading time.** 19 minutes keeps the old syllable rate of the Vietnamese page (about 350 syllables a minute); the English page uses 230 words a minute.
- **Site manifest.** `site-manifest.json` still holds the old summary and reading time for front-prologue-vi. The consolidating editor should sync it.
