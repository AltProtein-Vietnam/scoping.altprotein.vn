"""Scale comparisons for wave 11 line L2 (our calculation).

Inputs and their sources:
- D-BENCH 2035 animals spared a year (national meat mix), summed over routes R2 to R5
  from data/demand_funder_units.csv: pigs 142,271; chickens and ducks 2,507,913.
- Pigs culled for ASF: 2019 over 5.9 million (PAN-03); 2025 about 1.2 million (MAC-01).
- Pig herd end 2025: 31.4 million; poultry flock end 2025: 584.9 million (MAC-12, MI-013, MI-015).
- Poultry dead or culled for HPAI, 1 Jan to 24 Jul 2026: over 349,400 (PAN-09).
- Recombinant ASF virus in 2025 typed samples: 158 of 200 (north), 32 of 42 (centre and
  Central Highlands), 6 of 10 (south) (PAN-33).
"""
pigs_spared_2035 = 142_271
poultry_spared_2035 = 2_507_913
culled_2019 = 5_900_000
culled_2025 = 1_200_000
herd_2025 = 31_400_000
flock_2025 = 584_900_000
hpai_birds_2026_jul = 349_400
rec = {"north": (158, 200), "centre": (32, 42), "south": (6, 10)}

print(f"2019 ASF culls / D-BENCH 2035 pigs spared: {culled_2019 / pigs_spared_2035:.1f}")
print(f"2025 ASF culls / D-BENCH 2035 pigs spared: {culled_2025 / pigs_spared_2035:.1f}")
print(f"2025 ASF culls as share of end-2025 herd: {culled_2025 / herd_2025:.1%}")
print(f"HPAI 2026 (to 24 Jul) birds as share of end-2025 flock: {hpai_birds_2026_jul / flock_2025:.2%}")
print(f"D-BENCH 2035 poultry spared / HPAI 2026 birds to 24 Jul: {poultry_spared_2035 / hpai_birds_2026_jul:.1f}")
r = sum(a for a, b in rec.values()); n = sum(b for a, b in rec.values())
print(f"Recombinant share, all 2025 typed samples: {r} of {n} = {r / n:.1%}")
