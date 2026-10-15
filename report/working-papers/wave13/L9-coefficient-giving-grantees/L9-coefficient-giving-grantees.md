# Coefficient Giving grantees with published research, screened for Vietnam

Line: L9, Coefficient Giving grantees with published research (wave 13). Source prefix: CGG. Date: 15 October 2026.

## Verdict

Coefficient Giving (formerly Open Philanthropy) has funded little published alternative-protein science that we could trace, and none of it is Vietnamese. The one paper that matters most is Humbird (2021), the cultivated-meat cost model the study already uses (COST-47). Its acknowledgements say Open Philanthropy funded it. The study quotes it correctly, but leaves out the parts that bear most on play T8: the author's own affordability target, the finding that amino acids cost far more than growth factors at scale, and the case where cheap protein hydrolysates cut cost from USD 37 to 22 per kg. We found no Coefficient Giving-funded fermentation cost model, no gas or methane protein paper, and no plant-protein result that changes T1 or T10. Yield class: **added a constraint** (to T8 and to how the study compares cultivated cost with retail meat), with **clean negatives** on fermentation cost, resilient-food protein and Vietnamese grantees, and one weak candidate public good (open flavour profiles of Vietnam's farmed fish).

## Headline findings

1. **Humbird (2021) was funded by Open Philanthropy, and the study's figures from it are right.** The acknowledgements read "This analysis was funded by Open Philanthropy". The fed-batch case gives USD 37 per kg of wet cell mass and the perfusion case USD 51 per kg, with USD 663 million of capital for 6.9 kt a year, as the study says [general, High, COST-47].
2. **The study does not yet carry Humbird's own affordability test.** He sets about USD 25 per kg of bulk cells as the cost of an affordable "sometimes" food, which he expects to reach about USD 50 per kg at the shelf. Both base cases exceed it. Only fed-batch with low-cost hydrolysate media (USD 22 per kg) gets under it, and he says suitable hydrolysates "do not exist today" [general, High, COST-47].
3. **For T8, media made from cheap protein hydrolysates matter more than growth factors.** At scale, amino acids add USD 19 per kg of cells and growth factors USD 3 per kg. Replacing amino acids with a USD 2 per kg hydrolysate removes almost USD 16 per kg [general, High, COST-47]. Vietnam has soy, rice bran and pangasius side streams, but we found no test of such hydrolysates on fish cells (our inference; open question).
4. **The "7 to 15 times retail meat" comparison understates the gap.** It sets a factory-gate cost against a shop price. On Humbird's own doubling from bulk cells to shelf, cultivated meat would sit about 15 to 29 times above Vietnamese retail lean pork and chicken breast (our calculation from COST-47, COST-39 and COST-40) [VN-direct, Low].
5. **We found no Coefficient Giving-funded techno-economic model for precision or biomass fermentation, and none for protein from methane, hydrogen or CO2.** Crossref lists 484 works for the funder and OpenAlex 2,411; neither holds such a paper. One well-known hydrogen-protein paper by the Alliance to Feed the Earth in Disasters (ALLFED) records a different funder [general, Medium, CGG-01; CGG-02; QNT-14].
6. **Coefficient Giving-funded resilient-food work at Pennsylvania State University does not give a protein route from residues.** Lime-treated plant residues gave up to 22% glucose and an edible alga, but the algae held only 5 to 10% protein; the authors say protein production "remains limited" [general, Medium, CGG-08]. This supports the study's view that conversion technology, not biomass, is the constraint for rice straw (ch21, section 21.5).
7. **Plant-protein grants (through the Foundation for Food and Agriculture Research, FFAR) target crops Vietnam does not grow.** They cover zein from maize, high-protein chickpea and higher-protein field pea (about 22% seed protein now, up to 34% judged possible) [general, Medium, CGG-05; CGG-06]. If higher-protein peas arrive, imported pea protein gets cheaper, which raises the bar for T10 (our inference).
8. **Coefficient Giving's 2026 call names fish Vietnam farms.** Its staff post lists flavour characterisation in carp, tilapia, milkfish, catfish and pond loach, wants open, pre-competitive data, and confirms the call grew from USD 10 million to USD 30 million. No awards are public yet [general, Medium, CGG-03; CAP-57].
9. **The only Open Philanthropy-tagged paper with a Vietnamese affiliation is about fish welfare.** A 2025 survey led from Tra Vinh University studied perceptions of aquatic animal welfare in South and South-Central Vietnam [VN-direct, Medium, CGG-14]. It is out of scope, but it shows a working channel between the funder and Vietnamese aquaculture academics.
10. **Grantee demand research supports the study's low displacement factors.** In a preregistered US menu experiment with 4,431 adults, adding one or two meat analogues cut meat choice by 1.14 and 2.14 percentage points, neither significant; a chicken-style analogue cut chicken choice by 3.65 points [general, High, CGG-11, tested]. This is diet-change research, out of scope as a solution.

## How the grantee list was built

Coefficient Giving funds "Alternatives to Animal Products" under its Farm Animal Welfare Fund. Its website returned HTTP 403 from its Cloudflare edge to this environment on every path, and old openphilanthropy.org grant URLs redirect there. We did not use mirrors, web archives, caches or third-party copies of the grants database. We used four routes.

| Route | What we did | What it gave |
|---|---|---|
| Crossref funder metadata | All 484 works for funder 100014895, downloaded with no personal identifier; titles screened with a keyword filter (extract in `raw_crossref_funder_works.csv`) | 35 loose topic matches: resilient-food work (Pennsylvania State University), diet-change studies (Stanford), farm-animal welfare, malaria gene drives. No alternative-protein science paper [CGG-01] |
| OpenAlex (MCP tools) | Funder F4320315389 (2,411 works): filtered by alternative-protein terms (35 works); full-text search for "Open Philanthropy" with alternative-protein terms (64 works); filtered by authors in Vietnam and five ASEAN countries (37 works) | Humbird (2021) and its 2020 preprint; Stanford demand studies; Penn State resilient food; one Vietnamese fish-welfare paper. Most full-text hits cite the funder rather than acknowledge it [CGG-02] |
| Grantee announcements | UC Berkeley Alt:Meat Lab; trade press on FFAR | USD 125,000 to Berkeley in 2019 [CGG-04]; FFAR's USD 1,012,500 pea project with "additional funding" from Open Philanthropy [CGG-05] |
| Press and funder staff writing | Coefficient Giving's staff post on the 2026 call | Topics, species, the rise from USD 10 million to 30 million, no awards yet [CGG-03] |

Seven WebSearch calls returned summaries of openphilanthropy.org and goodventures.org grant pages. Good Ventures is the foundation whose money Coefficient Giving advises on, so these are first-party records, but we saw them only as search summaries. We used them for three single grant facts that other routes had already surfaced, at Low confidence (CGG-17), and never as a listing. Summaries that drew on aggregators such as LongtermWiki were discarded.

Funder tags in Crossref and OpenAlex are incomplete. A paper can be funded by Coefficient Giving without a tag, so these counts are a floor.

## Detailed findings

### 1. Cultivated meat cost and scale-up (T8, section 10.8)

**Humbird (2021), "Scale-up economics for cultured meat".** We read the results, the concluding discussion and the acknowledgements through Scite's full text. The paper was commissioned and funded by Open Philanthropy [general, High, COST-47]. The study registers it twice (COST-47 and SCI-14, same DOI).

| Item | Humbird (2021) | Study's use | Check |
|---|---|---|---|
| Fed-batch cost | USD 37 per kg wet cell mass (24 x 20 m3 bioreactors) | USD 37 per kg | Right |
| Fed-batch cost lines at 100 kt a year of world output | Capital about USD 12 per kg; amino acids USD 19; growth factors USD 3; consumables, utilities and labour (95 staff) USD 3 | Amino acids about USD 19, growth factors about USD 3 (S12.11) | Right |
| Perfusion | USD 663 million total capital; about USD 23 per kg capital and overheads; 132 staff; USD 51 per kg; 96 x 2 m3 bioreactors; 6.9 kt a year | Same | Right |
| Capital charge | 15% a year (7.5% over 10 years) | 15% | Right |
| Nutrients at very large output | Cost tends to about USD 16 per kg | Not used | Gap |
| Hydrolysate case | USD 2 per kg hydrolysate replaces amino acids: fed-batch falls to USD 22 per kg | Not used | Gap |
| Affordability target | About USD 25 per kg of bulk cells, about USD 50 per kg at the shelf | Not used | Gap |
| Key assumption | Both cases assume a cell line with metabolism "significantly enhanced relative to a wild-type cell line" | Not stated | Gap |
| Conclusion | Metabolic efficiency and low-cost hydrolysate media are "necessary but insufficient"; capital cost reduction is "a secondary condition at best" | "Would likely preclude" affordability (S13.11.1) | Right, partial |

All rows: [general, High, COST-47].

What this means for Vietnam:

- **T8's research focus.** T8 lists serum-free adaptation, growth-factor expression and regulatory preparation. In the published model, growth factors are a small cost line at scale (USD 3 per kg) and amino acids a large one (USD 19 per kg). Hydrolysates from soy, rice bran or fish by-products are the lever that brings the fed-batch case under the author's target. Vietnam has those side streams and groups that already make protein hydrolysates, for example Nha Trang University's fish side-stream work (RD-52) and a 2025 mushroom protein hydrolysate study (RD-65). We found no test of a Vietnamese hydrolysate on fish cells (our inference). This adds a task and a kill test to T8; it does not raise T8's scores.
- **The study's growth-factor disagreement (DG-104) stands.** Growth factors are up to 95% of medium cost at today's prices and USD 3 to 4 per kg at scale; Humbird's "100 kTA" is world output used to price nutrients, not plant size. DG-104's wording "at 100 kt/yr" could be read as a plant size.
- **The retail comparison.** Section 9.5 and section 10.8 say USD 37 to 51 per kg is 7 to 15 times the retail price of lean pork (132,000 VND per kg, USD 5.08) or chicken breast (90,900 VND per kg, USD 3.50) [VN-direct, Medium, COST-39; COST-40]. That divides a factory-gate cost by a shop price. On Humbird's own doubling to the shelf, the cultivated product would be at least USD 74 to 102 per kg, about 15 to 29 times the Vietnamese retail price (our calculation, at 26,000 VND per USD) [VN-direct, Low].

**Other cultivated-meat work screened.** The UC Davis life-cycle assessment (FTB-26) lists the National Science Foundation and UC Davis as funders; Open Philanthropy appears in its text only as a citation [general, High, CGG-02]. Tufts University's Beefy-9 serum-free medium, a widely used open recipe, was funded by the National Institutes of Health, not Open Philanthropy. Its research-scale medium cost USD 148 to 217 per litre, against USD 290 per litre for serum medium [general, High, CGG-13]. The study's industry figure of USD 0.63 per litre (SCI-16) is for a different, commercial medium at larger scale. Rethink Priorities' cultivated-meat forecasts (HSC-18) and AI report (FTB-01) are widely thought to be Coefficient Giving-funded, but neither page we read names a funder, so we do not count them. The forecast numbers the study uses match the page: a 54% chance that world output stays under 100,000 t a year through 2051, from a panel of six [general, Medium, HSC-18].

### 2. Fermentation cost (T5, T7, P6)

We found no Coefficient Giving-funded techno-economic model for precision fermentation or biomass fermentation in Crossref, OpenAlex or the grantee announcements we could reach [general, Medium, CGG-01; CGG-02]. The mycoprotein model the study uses (Risner et al. 2023, COST-43) records no funder in OpenAlex, so we cannot link it to Coefficient Giving. This is a clean negative for gap 7 in S12 and gap 13 in S13 (a peer-reviewed food-protein precision-fermentation model): this funder's published portfolio does not fill it.

The 2026 call does fund work close to T7 and T1: off-flavour reduction in plant and fermentation-derived ingredients, fat systems, and enzymatic egg replacement [general, Medium, CGG-03]. Results are not public yet.

### 3. Single-cell and resilient-food protein (ch21)

**Methane, hydrogen and CO2.** We found no Coefficient Giving-funded paper on protein from gas. ALLFED's hydrogen-protein paper (QNT-14) records the Alaska Space Grant Program as funder [general, Medium, CGG-02].

**Residues.** Coefficient Giving funds a resilient-food group at Pennsylvania State University, probably from its catastrophic-risk work rather than the Farm Animal Welfare fund (our inference; not confirmed). Two papers bear on chapter 21's "carbon beyond cassava":

- If plant biomass were converted to food at 30% efficiency, 6.7 kg a day would give a family of four enough carbohydrate, but toxic or too-low levels of other nutrients. The authors suggest other sources, such as single-cell protein, for protein, fat and vitamins [general, Medium, CGG-07].
- An integrated route turned lime-treated residues into glucose (up to 22% of the residue on enzymatic hydrolysis) and acetate that grew an edible alga to 835 to 971 mg per litre. The algae held 30 to 31% lipid and only 5 to 10% protein. The authors call the system viable on life-cycle and cost grounds, but say protein production remains limited [general, Medium, CGG-08]. We read only the abstract, so the cost claim is not checked.

Both support the study's existing view: for Vietnam's 52 Mt a year of rice straw, the conversion technology is the constraint, and a residue route is a sugar route first (ch21, section 21.5). Neither changes a window or a number.

**Duckweed and seaweed.** A modelling paper finds duckweed yields at equatorial sites change less than 6% under global warming and stay at 19 to 20 t per ha a year even in severe post-catastrophe cooling [general, Medium, CGG-09]. That is consistent with the study's 10 to 30 t of dry matter per ha a year (DG-109), but the abstract does not say dry or fresh weight, so we do not use the number. A seaweed paper shows tropical seaweed could be scaled after a nuclear war, limited by how fast farms are built [general, Medium, CGG-10]. Both are catastrophe planning, not protein-security routes for Vietnam's normal economy.

### 4. Plant protein functionality (T1, T10)

Coefficient Giving co-funded FFAR's plant-protein programme:

| Grant | Purpose | Amount and date | Output screened | Vietnam angle |
|---|---|---|---|---|
| FFAR plant protein optimization | High-protein chickpea (NuCicer); corn zein for plant-based meat (Purdue University) | USD 444,000 over three years (June 2020) in one funder record; USD 250,000 for chickpea alone in another [general, Low, CGG-17] | Zein as a viscoelastic agent with calcium hydroxide to match the texture of meat and cheese (metadata only) [general, Low, CGG-06] | Weak. Vietnam has no zein industry; its ethanol plants run on cassava, whose distillers' grain holds 13 to 16% protein (RD-22) |
| FFAR and North Dakota State University, Plant Protein Enhancement Project | Breeding tools to raise pea seed protein | FFAR USD 1,012,500, with Open Philanthropy "additional funding" (August 2021) [general, Medium, CGG-05] | None | Indirect. Peas at up to 34% protein (from about 22%) would cheapen imported pea protein, the product T10 aims to replace |
| UC Berkeley Alt:Meat Lab | R&D on animal-product substitutes; Alt.Meat Challenge Lab (2019); plant-based meat manufacturing research (2024) | USD 125,000 (2019) [general, Medium, CGG-04]; USD 800,000 over two years (2024) [general, Low, CGG-17] | Screened by line L8 | See L8 |

None of these changes T1 or T10. The pea result is a signal to watch for T10's cost test.

### 5. Sensory and taste parity

Coefficient Giving's 2026 call frames taste as the main barrier and asks for pre-competitive research on four areas: off-flavours, fat systems, egg replacement, and flavour in "welfare-priority" fish (carp, tilapia, milkfish, catfish, pond loach), with open flavour profiles and better analytical and sensory methods (gas chromatography with mass spectrometry and with olfactometry, GC-MS and GC-O) [general, Medium, CGG-03]. Round 1 offered USD 0.1 to 1 million per award and round 2 USD 1 to 5 million; decisions are due by 30 November and 31 December 2026 [general, High, CAP-57]. Typical terms are two to three years [general, Medium, CGG-03].

The staff post cites NECTAR's Taste of the Industry reports, the largest blind tastings of plant-based meat. We could not confirm that Coefficient Giving funds NECTAR: its home page names no funder [general, Low, CGG-18]. The study already uses one NECTAR study (NOV-40, an APAC blended-mince test). US parity results do not transfer to Vietnamese dishes.

**The Vietnam angle is the fish.** Vietnam is the world's main pangasius producer (about USD 2.2 billion of exports a year, MAC-01) and farms tilapia, carp and pond loach. Vietnamese groups have done descriptive sensory work on cooked pangasius flavour [VN-direct, Low, CGG-15] and study off-flavour control in pond tilapia [VN-direct, Low, CGG-16]. An OpenAlex search of Vietnamese-affiliated papers on these species and flavour terms returned 17 results; in the 15 titles we read, none profiles their odour-active compounds. This is the basis for candidate CGG-C1 below.

### 6. Funder fit (section 25.4)

- Through public research metadata, we found no Coefficient Giving-funded alternative-protein research with a Vietnamese author. The only Open Philanthropy-tagged paper with a Vietnamese affiliation is a fish-welfare survey from Tra Vinh University (2025) [VN-direct, Medium, CGG-14; CGG-02]. Wave 7 also could not say whether the funder has made grants in Vietnam, for the same access reason.
- Grantee demand research (Stanford's Humane and Sustainable Food Lab, a University of Texas and University of Toronto team) is diet-change or consumer-ethics work. It is out of scope as a solution. As evidence, it supports the study's low displacement factors: menu additions barely moved meat choice [general, High, CGG-11, tested], and telling people about a new meat alternative lowered their moral objections to farming [general, High, CGG-12, tested].
- Advocacy and movement-building grants are out of scope; the fund's strategy includes movement building "especially in emerging economies" (AFN-02).

## Candidate public good

**CGG-C1. Open flavour and off-flavour profiles of Vietnam's farmed fish.** Full row in `data_candidates.csv`.

- **What.** A public dataset of the odour-active and taste compounds of cooked tra catfish, tilapia, carp and pond loach, with their main off-flavours, measured by GC-MS and GC-O and linked to a trained sensory panel.
- **Why Vietnam.** Vietnam farms these species at scale, so reference fish are easy to sample. Vietnamese groups already do fish sensory and off-flavour work. A funder with a fitting, stated scope exists, which section 25.4 found rare. No play or public good in the study covers flavour.
- **Must be true.** GC-O access in Vietnam or through a partner; a trained panel; an international co-applicant; a funding round open to Vietnamese teams; open publication.
- **Kill tests.** No open round by the end of 2027; no GC-O access; a team abroad publishes the same profiles first.
- **First users.** Plant-based and hybrid seafood makers abroad; Vietnamese surimi and fish-ball makers testing blends (line L4); pangasius and tilapia processors, who also gain off-flavour benchmarks for their own exports.
- **Scores** (1 to 5): market pull 1, Vietnam advantage 3, technical readiness 3, route to market 5, capital efficiency 5, defensibility 2, public value 2. Balanced score 3.05 (our calculation). Route and capital scores flatter any cheap research public good, which is why the study leaves P1 to P6 unscored. Read the score as "cheap and payable", not as a ranking above T9.
- **Overlap.** It formalises the advice already in S11.10 and overlaps line L4 (alternative seafood, GFI-105 and GFI-106). The lead should merge it with any L4 proposal.

## What this changes in the package

| Where | Current text or value | Proposed change | Evidence | Strength |
|---|---|---|---|---|
| ch09 section 9.5; ch10 section 10.8; S13.11.1 | USD 37 to 51 per kg of wet cells; 7 to 15 times retail lean pork or chicken breast | Keep the figures. Add Humbird's target (about USD 25 per kg of bulk cells, about USD 50 at the shelf), that both cases exceed it, and the hydrolysate case (USD 22 per kg). Say that 7 to 15 times sets factory cost against a shop price; on the author's doubling, about 15 to 29 times (our calculation) | COST-47; COST-39; COST-40 | moderate |
| ch26 T8; `plays.csv` T8 | Serum-free adaptation, growth-factor expression, regulatory preparation | Add hydrolysate media from Vietnamese side streams to T8's tasks; add to must-be-true that the model assumes an engineered cell line; add the kill test "no hydrolysate-based medium supports fish-cell growth over several passages within three years". Scores unchanged | COST-47; SCI-14 | moderate |
| `tea_benchmarks.csv` TEA-015, TEA-016; S12.11; COST-47 and SCI-14 notes | Full text read: Partial (excerpts) | Full text read: Yes. Add "Funded by Open Philanthropy (now Coefficient Giving)" and that 100 kt a year is world output, not plant size | COST-47 | strong |
| DG-104 claim B | "at 100 kt/yr" | "at 100 kt a year of world output" | COST-47 | weak |
| ch21 section 21.5; F3.1.6 | Technology, not biomass, is the constraint | Add the Penn State result: residue to glucose and algae, but algae at 5 to 10% protein; a residue route is a sugar route first | CGG-07; CGG-08 | weak |
| S11.10, S11.13; ch08; ch25 section 25.4 | Coefficient Giving topics fit Vietnamese seafood science | Add the species list (including pond loach), the call for open flavour data, no awards public yet, and the funder-fit finding (no Vietnamese alternative-protein grantee found; one fish-welfare paper). Note the site blocks cloud sessions | CGG-03; CGG-02; CGG-14; CAP-57 | moderate |
| ch26 section 26.4 | Four public goods | Consider CGG-C1, merged with any L4 proposal | CGG-03; CGG-15; CGG-16; MAC-01 | weak |
| ch13 "little displacement"; D7 | Most US plant-based buyers keep buying meat | Add the 2026 menu experiment (1.14 and 2.14 points, not significant; chicken analogue 3.65 points) | CGG-11 | moderate |
| `open_questions.csv` | n/a | Five new questions (see file) | CGG-03; COST-47; CGG-09 | moderate |

## Next-wave candidates

1. **Coefficient Giving's 2026 awards** (a deeper version of this line). Read the award list in January 2027 from a network that can reach the site. If any award covers catfish, tilapia or carp flavour, CGG-C1 becomes a partner project rather than a new one. Desk work can close it in one session.
2. **GC-O capacity in Vietnam** (a different kind of question: a phone and email check). Three laboratories. Decides whether CGG-C1 can run in Vietnam. Desk research cannot close it.
3. **Hydrolysate media for fish cells** (a different kind of question: a literature check, then a bench test). Belongs with line L3. A positive result would give T8 a Vietnamese input angle; a negative one would confirm "monitor".
4. **The full grantee list.** Only worth doing if the database becomes reachable. Further searching through metadata would be noise: we ran three independent routes and they agree.

Further desk work on Coefficient Giving grantees beyond these points would mostly add citations without changing a conclusion.

## Limits

- **Access gap.** coefficientgiving.org returned HTTP 403 on every path, including robots.txt, and old openphilanthropy.org grant URLs redirect there. We could not read the grants database, so the grantee list is incomplete and amounts come from grantees, press or (Low) search summaries. We did not use mirrors, archives, caches or third-party copies (for example LongtermWiki or grant listing sites).
- **Judgement call to review.** CGG-17 records search-engine summaries of the funder's and Good Ventures' own grant pages. We used them only for three single facts already surfaced by other routes, at Low confidence. The lead may prefer to drop them; nothing in the verdict depends on them.
- **Funder tags are incomplete.** Crossref and OpenAlex miss many acknowledgements, so "we found no" statements mean no tagged or acknowledged output, not proof of absence.
- **Full text read:** Humbird (2021, results, conclusion and acknowledgements) and Beefy-9 (in part). **Abstract only:** CGG-07 to CGG-12. **Metadata only:** CGG-06, CGG-14, CGG-15, CGG-16. The Penn State duckweed paper's full text was behind a publisher sign-in redirect, which we did not follow; the PubMed Central copy of Humbird showed a CAPTCHA, which we did not attempt; Wiley's direct PDF returned HTTP 403.
- **Not confirmed as grantees:** Rethink Priorities and NECTAR. We list them but do not count their outputs.
- **Budget.** Seven of 25 WebSearch calls used.

## Addendum (lead session, 15 October 2026): the funder's grant list

The funder's grant list was read in a separate browser session and reconciled with this line. See `cowork/RECONCILIATION.md`.

- **What it shows.** 61 grants in the focus area, worth USD 49.3 million. Only 9 are research or R&D. None names Vietnam or Southeast Asia.
- **Funding outside the focus area.** Several items above (resilient-food work, UC Davis, Tufts, NECTAR) were funded through other programmes or contracts.
- **Grant figures superseded.** The search-summary grant facts (CGG-17) are replaced by the list (CGG-19).
- **Four outputs added to the screen.** CGG-I25 to CGG-I28.
