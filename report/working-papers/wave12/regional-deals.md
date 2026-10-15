# Wave 12: regional alternative-protein deals, East and Southeast Asia (v0.9)

Research note for version 0.9. Run on 15 October 2026 as one desk research round (web search and fetch), to fill the gaps in the deal log (`deals.csv`, Vietnam-linked) with deals elsewhere in East Asia (China, Japan, South Korea, Taiwan, Hong Kong, Mongolia) and Southeast Asia (Singapore, Thailand, Vietnam, Malaysia, Indonesia, the Philippines, Cambodia, Laos, Myanmar, Brunei, Timor-Leste). South Asia was out of scope.

## Scope rules

- In scope: protein for people in the study's families (plant-based, fermentation, cultivated meat and seafood, microalgae, blends) and the infrastructure that makes them (pilot plants, contract manufacturers, equipment, media), plus relevant funds, grants and DFI tickets.
- Feed-only deals kept as context, in a separate group.
- Traditional products without a new industrial protein line excluded.
- Window: 2019 to October 2026, with priority on 2023 to 2026.

## Outputs

- `data/regional_deals.csv`: 43 rows (36 in the main record, 3 public programmes, 2 outbound deals by regional investors and 2 feed-only deals as context). Each row has its source IDs (prefix RDL, `sources.csv`) and a confidence label.
- Appendix S11, section S11.6, and chapter 8, section 8.1, summarise the record.
- Disagreements DG-374 to DG-377 and open questions OQ-474 to OQ-476.

## Rules applied

- Amounts are as reported by the source, converted to USD by the source, not by us. Where sources disagree, both figures are kept and logged in Appendix R2; we do not average them.
- Confidence: High where a company or investor release, a regulatory filing or the investor's own disclosure was read; Medium for reputable trade press; Low for a single database entry (PitchBook, Tracxn, Dealroom, CB Insights, Startup Intros) or a single press claim.
- Totals by country add figures of mixed confidence and leave out undisclosed rounds. They are indicative only.

## What could not be found

Rounds in 2024 to 2026 for Phuture Foods and Cell AgriTech (Malaysia), WTH Foods (Philippines), Float Foods, Sophie's Bionutrients, Allozymes, Prefer, Meatiply, Fermbox Bio and Esco Aster (Singapore), Hey Maet, Zhenmeat and Starfield after 2021 (China), CP Foods, Betagro and Mitr Phol fermentation (Thailand), and Green Monday after 2020 (Hong Kong). Dedicated searches of the Proparco, FMO, BII and DEG disclosure portals were not completed. Coverage of China after 2023 is thin, so the totals understate RMB activity.

## Not used

Rows whose only support was a source not retrieved in this round (for example a Bloomberg item relayed by a blog, a Cultivated X listing or an aggregator page without a named source) were left out of the data file rather than entered without a source.
