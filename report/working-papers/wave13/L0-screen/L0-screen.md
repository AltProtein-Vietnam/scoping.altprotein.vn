# Wave 13, L0: the solutions screen and fold-in (lead session)

Line: L0, screen and consolidation (wave 13). Source prefix: GSD. Date: 2026-10-15.

## Verdict

We checked 170 published solutions for Vietnam:
- the 112 entries of the Good Food Institute's Solutions Database;
- 58 publications, research outputs and grants from The Protein Project, the Berkeley Alt:Meat Lab and Coefficient Giving's grantees.

None displaces the leading plays (T1, T4, T5). Most items are already covered (30) or are frontier work Vietnam would buy rather than make (55). Thirty-three strengthen an existing play, public good, move or rule. Five candidates were proposed. Three are listed in chapter 26 but not ranked (T11, T12, P7), and two were folded into existing moves (RM-09, RM-14).

Yield class: **added a constraint**, plus **added a candidate** and **closed a question**. The screen sharpened conditions (T1 finance, T10 raw material, P4 function), corrected one rule (Decree 43/2026 on genetic resources) and added two routes to "do not recommend". It did not change a headline conclusion.

## What the lead did

1. **Catalogue.** Read all 112 entries through the GFI site's public listing API (`wp-json/wp/v2/solutions_database`) on 15 October 2026, built `../gfi_solutions_catalogue.csv` and assigned each entry to a line. GFI's full text stayed in the session scratchpad, not in the repository.
2. **Brief.** Wrote `../BRIEF.md` with seven fixed verdicts and the test "make it, buy it or leave it". The editor later asked for three more sources, which became lines L7 to L9 (addendum in the brief).
3. **Sources.** Registered GFI's database and its two ASAP reports once (GSD-01 to GSD-04), so lines did not register 112 pages.
4. **Fold-in.** Folded the results in with the scripts in this folder:
   - `fold_registers.py`: sources, R4, the bibliography, the open-question and disagreement registers, and R1 and R2;
   - `build_screen.py`: `data/solutions_screen.csv`;
   - `build_s14.py`: Appendix S14.

   The 102 proposed changes are in `changes_all.csv`, each tagged with the editor group that applied it. Four editor sessions applied groups B to E on disjoint pages, and the lead applied group A (chapter 26, `plays.csv`, the registers, the front pages and the method and changelog pages).
5. **Duplicate.** SLS-09 was the same paper as the existing source RD-52 (same DOI), so citations were pointed at RD-52 and SLS-09 was not registered.

## Editorial decisions

- **T11 hybrid fish cakes and fish balls (from L4) is not ranked.**
  - **Scores.** 2, 3, 4, 5, 5, 2, 3; balanced 3.50. It would place third or fourth under every preset and push T5 out of the top three under four presets (our calculation from `play_weight_presets.csv`).
  - **Why not ranked.** Its score comes from ease of entry, not demand (market pull 2). Taste panels abroad reject blends above 30 to 40% replacement, and a leading Korean maker, Dongwon F&B, is moving to 80% fish or more.
  - **Test before ranking.** A maker trial and a sensory panel (OQ-491).
- **T12 domestic food-grade soybean and mung bean (from L7) is not ranked.**
  - **Scores.** Balanced 3.50.
  - **Why not ranked.** Domestic beans cost about 1.4 to 2.3 times imports, and no Vietnamese farm-margin data exists.
  - **Test before ranking.** A farm-economics test and conditional buyer contracts (OQ-510, OQ-511).
- **P7, a characterised food-strain set (from L2), is a candidate public good.** It enters the list when a host collection agrees standard licence terms and three firms ask for strains (OQ-482, OQ-483).
- **AML-C1, a buyer-set product challenge lab (from L8), joins RM-09** with L6's senior-engineer and operator tracks. It scored 2.95 balanced, and it is a skills measure rather than a public good.
- **CGG-C1, open flavour profiles of Vietnam's farmed fish (from L9), joins RM-14.** It overlaps L4. Its score of 3.05 is inflated by route and capital scores that any cheap public good gets.
- **CGG-17 is kept at Low.** It records search summaries of the funder's own grant pages, which this environment could not open. It supports three single grant facts already surfaced by other routes, and nothing in the verdict rests on it. A browser-based check of the grant list (`../COWORK-PROMPT-coefficient-giving.md`) should replace it.
- **Two figures that look in conflict are not.** brief-research's "at most 9% of food use" is today's domestic share of food soybean. L7's "76% to 95%" is what the 2010 planted area would supply. Both stay, each with its basis.

## Next-wave candidates

Almost every open point now needs a call, a quote or a trial, not more desk research. The cheapest next steps, by owner:

- **Fish-cake makers and VASEP.** Would two makers run a 10 to 20% substitution trial? (OQ-491 to OQ-494). This decides T11.
- **Vinasoy and two tofu makers.** Domestic bean tonnage, premium and contract terms (OQ-511), and a farm-economics test with an agricultural university (OQ-510). This decides T12.
- **VTCC and FIRI.** Licence terms and charges for food strains (OQ-483) and the Decree 43/2026 Form 12 contract (OQ-482). This decides P7.
- **Lessors, banks and the Ho Chi Minh City guarantee fund.** Terms for a T1-scale line (OQ-498 to OQ-503).
- **YERA.** Plant size and spare capacity (OQ-484), for T5.
- **Fermentation plants.** How they train operators, and whether they would take outside trainees (OQ-504), for RM-09.
- **Coefficient Giving.** Its 2026 taste awards and any 2027 round (OQ-519). The grant list itself was read in a browser session and reconciled (`../L9-coefficient-giving-grantees/cowork/RECONCILIATION.md`; OQ-522 closed).

## Limits

- The GFI database is mostly from 2021. Lines checked whether gaps had been filled since, but not exhaustively.
- coefficientgiving.org returned HTTP 403 from its Cloudflare edge to this environment on every path. The old openphilanthropy.org grant URLs redirect there. We did not use mirrors, archives or third-party copies of the grants database.
- The public OpenAlex API was out of its shared daily budget on 15 October 2026, so lines used the OpenAlex connector or Crossref instead.
- Verdicts are our judgement on desk evidence. They are tagged Low wherever they rest on one press report or a search summary.

## Addendum: Coefficient Giving browser check (15 October 2026)

The editor ran the Cowork prompt in a browser and returned the funder's grant list: 61 grants, 7 outputs and notes. The lead reconciled it with line L9 (`../L9-coefficient-giving-grantees/cowork/RECONCILIATION.md`) and folded it in.

- **Registers.** Six sources (CGG-19 to CGG-24). Four new screen items (CGG-I25 to CGG-I28), so the screen now holds 170 items. OQ-522 closed; OQ-524 and DG-398 added; DG-396 and DG-397 updated.
- **Data.** New data file `coefficient_giving_grants.csv`.
- **Pages.** Changes in S14, S11, ch08, ch13, ch25 and M1.16. CGG-17 is no longer needed for any grant fact.

