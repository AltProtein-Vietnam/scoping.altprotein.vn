# Editor log E14-part5c: chapters 29 and 30

Editor: E14-part5c. Date: 2026-10-01. Files edited: `content/01-report/ch29-actor-check.md`, `content/01-report/ch30-unknowns.md`. Both pass `tools/validate.py` (0 errors) and contain no em or en dashes. No data files, tiles or charts edited. No inbound anchors to either page (checked with `grep -rn "ch29-actor-check#\|ch30-unknowns#" content`), so section headings could be reworded; section numbers are unchanged.

## ch29-actor-check

| section | change | type |
|---|---|---|
| Frontmatter | Summary split into shorter sentences; "incumbents" now "the firms that already make food". `reading_time_min` 11 to 13 (the text is longer because terms are now explained). Title, key numbers, charts and related pages unchanged. | clear language only |
| Opening | `**In one paragraph.**` replaced by `**In brief.**` with six bullets. Same numbers and findings; the label-rule and sugar-tax findings kept in a short bullet. | clear language only |
| 29.1 | Actor table: abbreviations written out (GFI, National University of Singapore, Asia Research and Engagement, Animal Charity Evaluators, International Finance Corporation, MOET, Ministry of Agriculture and Environment, Asian Development Bank). Counts unchanged. | clear language only |
| 29.2 | Heading now "What Part III missed: different kinds of question". *chay*, offtake and CO2e explained. | clear language only |
| 29.3 feed paragraph | Heading "Feed demand is revealed but priced low" now "Feed demand exists but is priced low". Kept the inactive-yeast import fact (about 9,200 t, food and feed together, 2025, 95% at about USD 1.1 per kg) with `[@FBA-17]`. **Removed** the clause that the ASC feed standard neither requires nor rewards microbial protein and the BAP feed-mill standard only counts aquatic-microorganism meal, together with `@FBA-01` and `@FBA-05`. **Removed** the recommendation that a Vietnamese microbial feed ingredient must beat imported yeast; replaced by one line saying play T2 was retired in version 0.8 because feed is now context only. | pruned feed |
| 29.3 other paragraphs | Long sentences split and paragraphs kept to five sentences or fewer; trade-agreement codes (ACFTA, ATIGA, AKFTA, RCEP) written as words; "venture thesis" now "venture bet" (as in chapter 25); "must" kept only for the legal label rule; HS chapter 19, rules of origin, co-packer, stunting, GMO, meat analogue, extender explained; label findings set as a bullet list. "No founder has yet tried" now "In our register, no founder has yet tried". Correction callout unchanged. | clear language only |
| 29.4 | Already about protein for people; added one line saying the feed finding no longer leads to an action. Funder bullet split into sub-bullets; "kill test" and "equal-saving blind test" explained. | reframed for food |
| 29.5 | **Removed** the table row "Which mills import feed yeast, and would they trial a Vietnamese product against it? / Names T2's buyers"; replaced by a line below the table saying this question was retired in version 0.8 because feed is now context only. T1 and *nước giải khát* explained. | pruned feed |
| 29.6 | Main point first; "clean negatives" now "clear negative answers". | clear language only |

Citation tokens: all kept exactly except `[@FBA-17; @FBA-01; @FBA-05]`, which became `[@FBA-17]` when the feed-standards clause was removed (FBA-17 is the Comtrade mirror-import series for HS 2102.20, so it stays on the yeast claim it supports). Every evidence, `{fx:}` and `{dx:}` tag, embed and cross-link kept.

## ch30-unknowns

| section | change | type |
|---|---|---|
| Frontmatter | Summary: "twenty unknowns" now "fourteen unknowns that matter most for protein for people"; "a phone call to a feed mill" now "a phone call to a starch factory or food maker". `reading_time_min` 6 to 7. | reframed for food |
| Opening | `**In brief.**` with five bullets; says fourteen unknowns remain and six feed-only unknowns sit as context. Demand-questions callout set as a bullet list (content unchanged). | clear language only |
| 30.1 heading | "The twenty unknowns that matter most" now "The fourteen unknowns that matter most". | retitled |
| 30.1 table | **Six feed-only unknowns removed from the ranked list** and moved to a "Context: feed" note below it: former 3 (aquafeed raw-material rule, OQ-043), 5 (fishmeal share in shrimp and pangasius feed, OQ-002), 6 (Chinese microbial protein in feed, OQ-034), 11 (official aquafeed output by species, OQ-003), 12 (whether the 2030 industrial feed target covers aquafeed, OQ-127) and 19 (VAT status of new feed ingredients, OQ-089). The remaining fourteen keep their relative order and are renumbered 1 to 14. In the "Who to ask" detail for the removed items, the HS codes 2309.90 and 2102.20 and the importer name were dropped. | pruned feed |
| 30.1 Unblocks column | Retired plays removed: former 4 (tolling) "T2, T3, T5" now "T5"; former 9 (cassava pulp) "T3, T4" now "T4". Play and public-good codes decoded in a list above the table. Abbreviations explained (GMO, Ministry of Agriculture and Environment, Singapore Food Agency, EECi, National Institute for Food Control, HALCERT, Ministry of Science and Technology); "Scenario 3" named (Regulated regional hub, chapter 19); Tay Ninh given its former units. | reframed for food |
| 30.1 Reading | Rewritten for the new numbering: items 1 and 2 rules; items 3 to 7 decide the economics of T1, T4 and T5, the three plays that lead; items 8 to 14 testing, cooling costs, pilot plants and export routes. The old line "Items 11 and 12 affect how large the future feed-protein market looks" removed. | reframed for food |
| 30.2 | Table refocused on protein for people and reordered. **Removed rows:** displaceable fishmeal pool (350 to 450 kt against 120 to 245 kt) and fishmeal price (USD 1,600 against USD 1,794 per t). Aquafeed volume moved out of the table into a feed-context sentence that keeps both figures (3.9 to 4.8 Mt against 6.5 Mt) and the link to chapter 1. Kept rows: import tonnage, titer benchmark, Hawkwood cost structure, E10 start date, Entobel financing (now labelled an insect-feed deal cited for its deal structure). Titer, E10, mirror data and the Hawkwood study explained. | pruned feed |
| 30.3 | Active voice; WITS written out; "Cost stacks" explained. No limits removed. | clear language only |
| 30.4 | "feed mills" removed from the list of readers who can help; "food makers" and "fermentation plants" added. | reframed for food |

Citation and tag tokens: none removed or changed (the table carried none). New cross-links: `[[app-r1-open-questions]]` and `[[ch19-outlook-2035]]`.

## Tiles and charts removed

None. Both pages keep their existing tiles and chart (`kn-actor-check`, `kn-school-plant-days`, `kn-fta-duty-china`, `kn-funder-fit`, `kn-animals-spared-2035`, `chart-actor-coverage`, `kn-open-questions`, `kn-disagreements`). None is a feed tile.

## Unsure or for the consolidating editor

1. **"Twenty unknowns" repeats elsewhere.** `front-exec-summary.md` (line 136: "The twenty unknowns that matter most") and `front-exec-summary-vi.md` (line 137: "Hai mươi câu hỏi ...") still say twenty. Chapter 30 now lists fourteen, before any wave 11 unknowns are added. Update once the final count is known.
2. **`priority_rank` in `data/open_questions.csv`** still holds the version 0.7 ranks (1 to 20, including the six feed questions), and `unblocks` still lists T2 and T3 for OQ-026 and OQ-015. Chapter 30's source line says the order follows `priority_rank` with the feed-only questions removed and renumbered. Appendix R1 says its "Priority" column shows the chapter 30 rank, so the two now differ unless the data is renumbered.
3. **`app-m4-actor-check-waves.md` line 101** still lists "the names of feed-yeast importers (T2)" among the most valuable questions. It needs the same retirement line as chapter 29 section 29.5.
4. **`ch22-protein-balance-2050.md` and `app-f4-balance-model.md`** cite "[[ch30-unknowns]], OQ-127" in a correction. OQ-127 is now in chapter 30's feed-context note, not the ranked list, so the link still resolves and makes sense.
5. **FBA-01 and FBA-05** are no longer cited in chapter 29. When I checked, they were still cited in chapter 17 and Appendices D6, S6 and R2, so they should stay in the source registers.
6. I took "(Chapter 19)" in the dumplings sentence to mean chapter 19 of the harmonised system tariff codes, not report chapter 19. HS 1902.20 is in that chapter, and the rule-of-origin source is the EU-Vietnam agreement's product rules.
7. I spelled out the laboratory NIFC but left NACEFA and CASE as laboratory names. I could not confirm their full names from a source I read in this session.
