"""Explore the FAOSTAT FBS extract for Viet Nam (area 237). Prints protein supply and balance elements."""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'raw', 'faostat_fbs_vnm_2010_2023.csv')
rows = list(csv.DictReader(open(SRC)))
def get(item, el, yr):
    for r in rows:
        if r['Item'] == item and r['Element Code'] == el:
            v = r['Y%d' % yr]
            return float(v) if v not in ('', None) else None
    return None
items = ['Grand Total','Vegetal Products','Animal Products','Cereals - Excluding Beer','Rice and products','Wheat and products','Maize and products','Starchy Roots','Pulses','Beans','Peas','Pulses, Other and products','Soyabeans','Groundnuts','Oilcrops','Treenuts','Vegetables','Fruits - Excluding Wine','Meat','Pigmeat','Poultry Meat','Bovine Meat','Mutton & Goat Meat','Meat, Other','Offals','Offals, Edible','Eggs','Milk - Excluding Butter','Fish, Seafood','Freshwater Fish','Demersal Fish','Pelagic Fish','Marine Fish, Other','Crustaceans','Cephalopods','Molluscs, Other','Aquatic Animals, Others','Aquatic Products, Other','Miscellaneous','Infant food','Sugar & Sweeteners','Alcoholic Beverages','Spices','Stimulants','Vegetable Oils','Animal fats']
for yr in (2010, 2015, 2020, 2023):
    print('==', yr)
    for it in items:
        p = get(it, '674', yr)
        if p is not None:
            print(f"{it:30s} prot {p:7.2f}  kg {get(it,'645',yr)}")
print()
for it in ['Rice and products','Wheat and products','Maize and products','Soyabeans','Pulses','Groundnuts','Pigmeat','Poultry Meat','Bovine Meat','Mutton & Goat Meat','Offals','Eggs','Milk - Excluding Butter','Fish, Seafood','Freshwater Fish','Crustaceans','Demersal Fish','Pelagic Fish','Marine Fish, Other','Cephalopods','Molluscs, Other','Vegetables','Meat']:
    for yr in (2010, 2015, 2020, 2023):
        P, I, E, S, F, Fe, Pr, St = [get(it, e, yr) for e in ('5511','5611','5911','5301','5142','5521','5131','5072')]
        print(f"{it:25s} {yr} P {P} I {I} E {E} DS {S} food {F} feed {Fe} proc {Pr} stock {St}")
