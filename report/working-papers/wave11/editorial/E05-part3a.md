# Editor log E05-part3a (version 0.8)

Editor: E05-part3a. Date: 2026-10-01. Files: `content/01-report/ch11-protein-diet.md`, `content/01-report/ch12-chay-baseline.md`.

Both chapters were already about protein for people. Neither contained a feed argument or a mention of a retired play (T2, T3, T6, P2, P3, TPP-11), so nothing was pruned for feed. The work was clear language to the GOV.UK standard.

Checks after editing:

- `python3 tools/validate.py`: 0 errors (2 warnings, both in other editors' tiles or charts).
- No em or en dashes (checked with Python for U+2013 and U+2014; the brief's grep command gives false positives on Vietnamese letters in a byte locale).
- Compared with the v0.7 baseline (commit 4dd602c): every citation token, evidence tag, `{fx:}` tag, `{dx:}` tag, cross-link and embed is identical in both files. No number was changed. The only numbers added are repeats of existing ones, the survey year, and the standard rate of 26,000 VND per USD stated for the USD column.
- No other page links to an anchor in either chapter. Appendix D1 cites "section 11.2" by number, so all section numbers are kept.

## ch11-protein-diet

| Section | Change | Type |
|---|---|---|
| Frontmatter | Summary split into two plain sentences, with the same facts. `reading_time_min` stays at 16. Key numbers and charts unchanged. | clear language only |
| Opening box | `**In one paragraph.**` (12 sentences) became `**In brief.**` with six short bullets. All headline numbers kept exactly: 136.4 g, 50 to 80 g, 42% and twice the 1990 share, 18% and 32% stunting, 40% eating soy foods, VND 34,000 to 45,000, about VND 71,000, VND 542,000 to 622,000, and 70%. **Removed:** the clause "Health guidance asks people to eat legumes daily". The body does not support it: the Ten tips say nuts and seeds daily, and Decision 1982 names legumes without "daily". "Red meat in moderation" is kept. | clear language only (one unsupported clause dropped) |
| How to read Part III | Callout split into short sentences, one per tag type. | clear language only |
| 11.1 | Abbreviations and terms explained: FAO, OECD-FAO, food balance sheets, carcass weight, Mt. Over-long paragraphs split, with each citation kept on its claim. "Who eats more" now opens with its main point. | clear language only |
| 11.2 | Stunting, serum zinc, complementary feeding and DIAAS (with its young-child and older-child patterns) explained. "Agenda" removed. The two consequences are now bullets with front-loaded labels. **Province name:** "Yen Bai (now Lao Cai)" became "Lao Cai (former Yen Bai)", following the style guide. | clear language only |
| 11.3 | Retitled "Protein is cheap: the price ladder a new protein has to climb" ("must" kept only for legal requirements). VHLSS and UHT explained. Added a sentence giving the 26,000 VND per USD rate behind the existing USD column. "Order of magnitude" kept. | retitled (section heading); clear language only |
| 11.4 | Retitled "Protein is a topping, filling or side dish". The section's conclusion, which was its last sentence, now comes first. Bullets given front-loaded labels. | retitled (section heading); clear language only |
| 11.5 | Retitled "When pork prices jump, people switch to other animal protein, not tofu". "Extender" defined in the glossary's words and "cross-price elasticity" explained. "Frontier actors" became "makers of new protein" and "therefore" became "so". | retitled (section heading); clear language only |
| 11.6 | Retitled "Health and food safety: strong worries, smaller changes in behaviour". The two Ministry of Health documents are now bullets and "prioritising" became "favouring". | retitled (section heading); clear language only |
| 11.7 | Retitled "Vietnam eats more meat than its income predicts". PPP is written out as purchasing power parity, with its meaning. "Novel protein" became "a new protein". | retitled (section heading); clear language only |
| 11.8 | Retitled "What this means for new protein" (was "for the frontier"). "B2B routes" became "selling through foodservice and other businesses". Phytate and absorption band explained. The long reader bullets are split into sentences. | retitled (section heading); clear language only |

The page title, id, tiles, charts and all headline numbers and citations are unchanged, so chapter 1 can keep drawing on this chapter as its evidence base.

## ch12-chay-baseline

| Section | Change | Type |
|---|---|---|
| Frontmatter | Summary trimmed to two sentences. "Served by tofu, soy milk, mushrooms and cheap mock meat" was dropped there, but stays in the In brief box and the title. `reading_time_min` changed from 16 to 17 (glosses added words). | clear language only |
| Opening box | `**In one paragraph.**` (10 sentences) became `**In brief.**` with six bullets. All numbers kept: 7.9%, two to three times, 20 to 40%, about 30% keeping 2 to 3 days, 2.5%, about a third, about 5%, and about 25,000 t. *cơm chay*, *bún chay* and *thực phẩm chay* glossed. | clear language only |
| 12.1 | "Unmeasured" became "not measured" in the heading. "Probability survey" became "random-sample survey". Person-day and recall day defined, and *Vu Lan* glossed. The DQQ ceiling bullet is split in two (a new bullet, "Vietnam is mid-region on meat-free days"). | clear language only |
| 12.2 | Retitled "Chay sales follow the lunar calendar" (was "The lunar calendar in the till"). The conclusion now comes before its confidence note. HS code and offering trays explained in table cells; column counts unchanged. "Feed included" kept: it is a fact about the trade data, not a feed argument. Correction callout kept verbatim. | retitled (section heading); clear language only |
| 12.3 | Retitled "The incumbent is large and mostly flat; soy milk grows". Foody explained. The market-size sentence now leads with "We do not use". | retitled (section heading); clear language only |
| 12.4 | Retitled "Chay buyers accept mock meat; their worry is safety". Sangha, Bodhisattva precepts, allium (onion family), botulism, PCR and TCVN explained. "Key split" became "main split". The trust paragraph is split, and "Meat in chay is a latent rumour, not a live scandal" became its own bold-led paragraph, "a background rumour, not a live scandal". Correction callout kept verbatim. | retitled (section heading); clear language only |
| 12.5 | Retitled "Chay is cheap per kilogram but expensive per gram of protein" (was "dear per gram"). "Deliver protein" became "supply protein". | retitled (section heading); clear language only |
| 12.6 | Retitled "Chay is a ready channel, but not a route to less meat". The channel and resistance paragraphs became bullets. **Restructured the displacement arithmetic:** the result (about 25,000 t, with its unchanged tags) now comes first, followed by four steps. S-ALT explained as Part IV's large alternative-protein scenario. "Organised promotion" became "organised campaigns". Co-packer defined. | retitled (section heading); clear language only |
| 12.7 | Retitled "What this means for new protein" (was "for the frontier"). *giò* and *nem* glossed, and "10 g đạm/100 g" translated. The reader bullets are split into shorter sentences. "Target safety inspections" became "Time safety inspections". | retitled (section heading); clear language only |

No tiles or charts were removed from either page.

## Unsure, or for the consolidating editor

1. **Glosses written by me without a citation.** These are general knowledge, but worth a check against the glossary:
   - *Vu Lan*: "festival for parents and ancestors".
   - *giò*: "steamed rolls".
   - *nem*: "fried or fermented rolls" (the meaning differs between north and south).
   - Sangha: "the organised Buddhist community".
   - Bodhisattva precepts: "a set of vows".
   - V-Label: "an international vegetarian and vegan label".
2. **Appendix D1 (not my file) differs from chapter 12 in three places:**
   - Line 536 still writes "Yen Bai (now Lao Cai)". The style-guide form is "Lao Cai (former Yen Bai)".
   - About line 523, D1 says "Gallup holds the interview dates". Chapter 12 says this is "not confirmed".
   - D1 says "only an effect larger than a doubling would be detectable". Chapter 12 says "even a doubling would be only borderline detectable".
3. **Survey fieldwork dates.** The APR-36 source row gives 13 Dec 2021 to 12 Jan 2022. Both chapters keep 13 November to 12 December 2021, the position taken in DG-296. No change made.
4. **The legumes clause.** I dropped "eat legumes daily" from the chapter 11 opening box because the body does not support it. It is not repeated elsewhere in the package (grep checked).
5. **A shared scratchpad helper was overwritten.** My comparison script was overwritten by another editor's script of the same name (`cmp.py`). I reran the checks with a uniquely named copy, so the results above stand. The work-in-progress commit 7fbb7e1 already holds an intermediate version of my two files. The final versions are in the working tree.
