# L8 calculations (our calculation). Inputs read from UC Berkeley class pages (AML-19) and play_weight_presets.csv.
import csv, os
enrolled = {  # semester: enrolled, from classes.berkeley.edu pages read 2026-10-15
    "2019 Fall INDENG 185-007 Needfinding": 22,
    "2020 Spring INDENG 185-004 Product design": 39,
    "2020 Fall INDENG 185-003 Needfinding": 35,
    "2021 Spring INDENG 185-003 Product design": 27,
    "2021 Fall INDENG 185-001 Needfinding": 42,
    "2022 Spring INDENG 185-001 Product design": 34,
    "2023 Spring ENGIN 183C-001 Product design": 30,
    "2023 Fall ENGIN 183C-004 Needfinding": 36,
    "2024 Spring ENGIN 183C-001 Product design": 27,
}
tot = sum(enrolled.values())
print("Total enrolled, 9 food challenge labs, Fall 2019 to Spring 2024:", tot, "mean per semester:", round(tot / len(enrolled), 1))
pd = [v for k, v in enrolled.items() if "Product design" in k]
nf = [v for k, v in enrolled.items() if "Needfinding" in k]
print("Product design strand:", sum(pd), "over", len(pd), "; needfinding strand:", sum(nf), "over", len(nf))

# Candidate AML-C1 scores under every preset in data/play_weight_presets.csv
scores = dict(market_pull=2, vietnam_advantage=2, technical_readiness=4, route_clarity=4,
              capital_efficiency=5, defensibility=1, public_value=2)
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
with open(os.path.join(root, "data", "play_weight_presets.csv")) as f:
    rows = list(csv.DictReader(f))
print("Preset columns:", list(rows[0].keys()))
for r in rows:
    w = {k: float(v) for k, v in r.items() if k in scores and v not in ("", None)}
    if len(w) == 7:
        s = sum(scores[k] * w[k] for k in scores) / 100
        name = r.get("preset") or r.get("preset_id") or list(r.values())[0]
        print(f"AML-C1 {name}: {s:.2f}")
# sensitivity: public value 3 instead of 2, balanced weights
bal = dict(market_pull=15, vietnam_advantage=15, technical_readiness=15, route_clarity=15, capital_efficiency=15, defensibility=10, public_value=15)
for pv in (2, 3):
    s2 = dict(scores, public_value=pv)
    print("Balanced with public_value", pv, "=", sum(s2[k] * bal[k] for k in bal) / 100)
