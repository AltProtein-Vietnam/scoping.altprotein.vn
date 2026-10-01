"""Pulls and tabulates the UN Comtrade data used in L1 (wave 11).

Raw responses are in raw/. Calls used (public preview API, no key, no personal identifiers):
  Vietnam-reported imports from world, one call per year 2015 to 2024:
    https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=704&period=<Y>&cmdCode=0102,0201,0202,0203,0204,0206,0207,0209,0210,0401,0402,0403,0404,0405,0406,0504&flowCode=M&partnerCode=0
  Vietnam-reported imports by partner, 2019 and 2023:
    ...reporterCode=704&period=<Y>&cmdCode=0102,0202,0203,0206,0207,0402,0401,0404,0405,0406&flowCode=M
  Mirror: partner-reported exports to Vietnam (partnerCode=704, flowCode=X), 2023 to 2025, reporters
    842,699,76,36,276,616,410,554,124,528,724,251,56,643,764 (Russia 643 returned no rows).
Vietnam had not reported 2024 or 2025 to Comtrade at the time of access (2026-10-01).
"""
import json, glob
from collections import defaultdict

def world_series():
    tab = defaultdict(dict)
    for f in sorted(glob.glob('raw/vnm_M_world_*.json')):
        for r in json.load(open(f))['data']:
            tab[r['cmdCode']][r['refYear']] = (r.get('netWgt'), r.get('primaryValue'))
    return tab

if __name__ == '__main__':
    t = world_series()
    for c in sorted(t):
        for y in sorted(t[c]):
            nw, v = t[c][y]
            print(c, y, None if not nw else round(nw / 1000, 1), round(v / 1e6, 1))
