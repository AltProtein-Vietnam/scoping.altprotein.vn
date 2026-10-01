"""L3 (SEC) calculations. Reads the study's balance assumptions (read-only) and the
UN Comtrade extract in raw/. Writes nothing outside this folder. Standard library only.

Part A: imported soybean-meal protein embodied in 1 kg of pork and poultry meat protein,
        using the balance model's own 2025 calibration (tools/balance_model.py, not run;
        its calibration steps are repeated here without writing outputs).
Part B: soy protein needed to deliver 1 kg of protein through plant-protein foods.
Part C: what the study's demand path (D-BENCH, 2035) means for imported soy protein.
"""
import importlib.util, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
spec = importlib.util.spec_from_file_location("bm", os.path.join(ROOT, "tools", "balance_model.py"))
bm = importlib.util.module_from_spec(spec); spec.loader.exec_module(bm)  # main() not called
P = bm.Params(bm.ASSUMPTIONS)
g = lambda n: P.get(n, "S-BASE", 2025)

# ---- Part A: repeat the model's 2025 calibration of soybean-meal (SBM) inclusion ----
feed_lv = g("base_feed_livestock_mt")
feed = {"pig": feed_lv * g("feed_share_pig"), "poultry": feed_lv * g("feed_share_poultry"),
        "other_livestock": feed_lv * g("feed_share_other_livestock")}
aq25 = {sp: g(f"base_aq_{sp}_kt") for sp in bm.AQ_SPECIES}
fcr_aq = {sp: g(f"fcr_{sp}") for sp in bm.FED_AQ}
share_of25 = g("compound_share_otherfish_2025")
def aq_share(sp):
    if sp in ("pangasius", "whiteleg"): return 1.0
    if sp == "othershrimp": return min(1.0, g("compound_share_othershrimp"))
    return min(1.0, share_of25 * g("compound_share_otherfish_index"))
raw_aq = sum(aq25[sp] / 1000 * fcr_aq[sp] * aq_share(sp) for sp in bm.FED_AQ)
k_aq = g("base_aquafeed_mt") / raw_aq
for sp in bm.FED_AQ:
    feed[sp] = aq25[sp] / 1000 * fcr_aq[sp] * aq_share(sp) * k_aq
sbm_raw = sum(feed[k] * g(f"sbm_incl_{k}") for k in feed)
sbm_cal = g("base_sbm_feed_use_mt") / sbm_raw
print(f"SBM calibration factor (2025): {sbm_cal:.3f}")
print(f"Calibrated SBM inclusion: pig {g('sbm_incl_pig')*sbm_cal:.3f}, poultry {g('sbm_incl_poultry')*sbm_cal:.3f}")

sbm_cp = g("sbm_cp"); meat_cp = g("protein_per_kg_meat_cwe")
res = {}
for sp, fcr, dress in (("pig", g("fcr_pig"), g("dressing_pork")),
                       ("poultry", g("fcr_poultry_meat"), g("dressing_poultry"))):
    incl = g(f"sbm_incl_{sp}") * sbm_cal
    # kg feed per kg carcass; whole-herd FCR applied to all feed (compound and other)
    feed_per_kg_cwe = fcr / dress
    sbm_per_kg_cwe = feed_per_kg_cwe * incl
    soyprot_per_kg_meatprot = sbm_per_kg_cwe * sbm_cp / meat_cp
    res[sp] = soyprot_per_kg_meatprot
    print(f"{sp}: feed {feed_per_kg_cwe:.2f} kg/kg cwe; SBM {sbm_per_kg_cwe:.3f} kg/kg cwe; "
          f"imported soy protein per kg meat protein {soyprot_per_kg_meatprot:.2f} kg")
# Note: applying compound-feed inclusion to all pig feed overstates SBM for the non-compound
# share (about 19% of pig feed in 2025, BLA-111 note). Lower bound: scale pig by 0.81.
print(f"pig, compound share only (x0.81): {res['pig']*0.81:.2f} kg")

# ---- Part B: soy protein per kg of protein in plant-protein food ----
# Direct use: protein in a soy food comes from the bean; the recovery of bean protein into
# the food depends on the process. We use recovery 0.5 to 1.0 (our assumption, no source;
# textured soy keeps most bean protein, tofu and isolates lose some to okara and whey):
for rec in (0.5, 1.0):
    print(f"soy food: imported soy protein per kg food protein at recovery {rec}: {1/rec:.2f} kg")

# ---- Part C: D-BENCH 2035 (ch18): about 2.35 kt meat protein displaced ----
displaced = 2.35  # kt meat protein, D-BENCH 2035 (ch18 section 18.4)
lo = min(res.values()) * 0.81 if False else min(res['pig']*0.81, res['poultry'])
hi = max(res.values())
print(f"Imported soy protein no longer fed for 2.35 kt of displaced meat protein: "
      f"{displaced*lo:.1f} to {displaced*hi:.1f} kt")
print(f"Soy protein needed if the displacing food is soy-based (recovery 0.5 to 1.0): "
      f"{displaced:.2f} to {displaced/0.5:.1f} kt")
sbm_2025_prot = g("base_sbm_feed_use_mt") * sbm_cp * 1000  # kt protein
print(f"Soybean-meal protein fed in 2025: {sbm_2025_prot:.0f} kt; net saving as share: "
      f"{(displaced*lo-displaced/0.5)/sbm_2025_prot*100:.3f}% to {(displaced*hi-displaced)/sbm_2025_prot*100:.3f}%")
print(f"Net change in imported soy protein, soy-based substitute: {displaced*lo-displaced/0.5:.1f} to {displaced*hi-displaced:.1f} kt saved")
print(f"If the substitute uses only domestic protein inputs: {displaced*lo:.1f} to {displaced*hi:.1f} kt saved, "
      f"{displaced*lo/sbm_2025_prot*100:.2f}% to {displaced*hi/sbm_2025_prot*100:.2f}% of 2025 SBM protein fed")
