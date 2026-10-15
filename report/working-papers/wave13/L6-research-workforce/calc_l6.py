"""L6 (wave 13) calculations. Standard library only. Run: python3 calc_l6.py"""
FX = 26000  # VND per USD, study convention

# NAFOSTED 2023 (SLW-01)
nafosted_total_bn = 278.316      # VND billion approved for 284 projects starting 2023
ordinary_m = 950                 # VND million, average ordinary basic-research project
strong_bn = 3.0                  # VND billion, average strong-research-group project
applied_bn = (1.5, 1.6)          # VND billion, applied/potential/urgent projects
intl_bn = 1.5                    # VND billion, international cooperation project

print("NAFOSTED total approvals 2023: USD %.1f million" % (nafosted_total_bn * 1e9 / FX / 1e6))
print("Ordinary basic-research project: USD %.0f" % (ordinary_m * 1e6 / FX))
print("Strong-group project: USD %.0f" % (strong_bn * 1e9 / FX))
print("Applied project: USD %.0f to %.0f" % tuple(x * 1e9 / FX for x in applied_bn))
print("International cooperation project: USD %.0f" % (intl_bn * 1e9 / FX))

# RM-11 scale check: USD 5 to 15 million a year
for usd_m in (5, 15):
    vnd_bn = usd_m * 1e6 * FX / 1e9
    print("RM-11 USD %d M = VND %.0f bn = %.0f%% of NAFOSTED 2023 approvals" % (usd_m, vnd_bn, 100 * vnd_bn / nafosted_total_bn))

# A first directed call at NAFOSTED scale
call_ordinary_bn = 10 * ordinary_m / 1000
call_strong_bn = 3 * strong_bn
print("Directed call, 10 ordinary projects: VND %.1f bn = USD %.0f" % (call_ordinary_bn, call_ordinary_bn * 1e9 / FX))
print("Directed call, 3 strong-group projects: VND %.1f bn = USD %.0f" % (call_strong_bn, call_strong_bn * 1e9 / FX))

# Training cost benchmarks
ncsu_fee, ncsu_hours = 3100, 21          # SLW-09
print("NC State course: USD %.0f per hour per trainee" % (ncsu_fee / ncsu_hours))
print("Cohort of 20 at NC State fee: USD %d (fees only)" % (20 * ncsu_fee))
dom = {"HACCP and ISO 22000": (3_200_000, 18), "basic food testing": (4_200_000, 24)}  # SLW-16
for k, (fee, h) in dom.items():
    print("Domestic %s: USD %.0f per course, VND %.0f per hour" % (k, fee / FX, fee / h))
ratio = (ncsu_fee / ncsu_hours) / ((4_200_000 / 24) / FX)
print("Fee per hour ratio, NC State to domestic testing course: %.0f times" % ratio)

# Funder acknowledgements (SLW-02, Q2)
total = 525
for name, n in (("NAFOSTED", 36), ("VINIF", 5), ("Vingroup JSC", 7)):
    print("%s: %d of %d works = %.1f%%" % (name, n, total, 100 * n / total))
