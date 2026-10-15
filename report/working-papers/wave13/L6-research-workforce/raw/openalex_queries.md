# OpenAlex queries run by L6 (wave 13), 2026-10-15

Run through the OpenAlex MCP connector (the public API returned HTTP 429, daily budget exhausted, at 2026-10-15). No personal identifiers were sent.

## Q1. Countries of works funded by the Good Food Institute (funder F4320319426)

OQL: get countries that published works where funder is (F4320319426) and it's not retracted
Reproduce: https://api.openalex.org/?oql=get%20countries%20that%20published%20works%20where%20funder%20is%20(F4320319426)%20and%20it's%20not%20retracted

Total works: 270, 39 countries. United States 124; Brazil 46; China 36; Canada 18; Israel 16; Singapore 15; Australia 12; Denmark 11; United Kingdom 11; Netherlands 10; Portugal 8; India 7; Mexico 7; Serbia 6; Switzerland 5; Spain 5; Italy 5; Germany 4; France 4; Lebanon 4; Austria 2; Hong Kong 2; Japan 2; Malaysia 2; Sweden 2; then 1 each: UAE, Belgium, Chile, Costa Rica, Egypt, Honduras, Indonesia, Ireland, Iran, South Korea, Norway, Philippines, Russia, Turkey.
Vietnam: 0. Thailand: 0.
Funder record: Good Food Institute, 273 works, 66 awards.

## Q2. Funders acknowledged on Vietnam-affiliated food-protein works, 2015 to 2026

Filter: authorships.institutions.country_code:VN, publication_year > 2014, not retracted, title/abstract/keywords match: "protein isolate" OR "protein hydrolysate" OR "protein extraction" OR "plant protein" OR "single cell protein" OR mycoprotein OR "meat analogue" OR "meat analog" OR "plant-based meat" OR spirulina OR "yeast protein" OR "fishmeal replacement" OR "fish meal replacement" OR "recombinant protein" OR "Aspergillus oryzae" OR "cultured meat" OR "cultivated meat" (stemmed).
Reproduce: https://api.openalex.org/?oql=get%20funders%20that%20funded%20works%20where%20institution%20country%20is%20%5BVietnam%5D(VN)%20and%20it's%20not%20retracted%20and%20published%20after%202014%20and%20title-abstract-keywords%20has%20(stemmed%20%22Aspergillus%20oryzae%22%20OR%20stemmed%20%22cultivated%20meat%22%20OR%20stemmed%20%22cultured%20meat%22%20OR%20stemmed%20%22fish%20meal%20replacement%22%20OR%20stemmed%20%22fishmeal%20replacement%22%20OR%20stemmed%20%22meat%20analog%22%20OR%20stemmed%20%22meat%20analogue%22%20OR%20stemmed%20%22plant%20protein%22%20OR%20stemmed%20%22plant-based%20meat%22%20OR%20stemmed%20%22protein%20extraction%22%20OR%20stemmed%20%22protein%20hydrolysate%22%20OR%20stemmed%20%22protein%20isolate%22%20OR%20stemmed%20%22recombinant%20protein%22%20OR%20stemmed%20%22single%20cell%20protein%22%20OR%20stemmed%20%22yeast%20protein%22%20OR%20mycoprotein%20OR%20spirulina)

Total works: 525. Top funders: NAFOSTED (F4320309617) 36; VNU-HCM 18; VAST 14; MOET (Bộ Giáo dục và Đào tạo) 12; HCMC University of Technology and Education 11; National Research Foundation of Korea 11; Ministry of Science and Technology, Taiwan 10; Ministry of Science and Technology (VN) 8; Vingroup JSC (F4320318839) 7; Curtin University 5; VINIF (Quỹ Đổi mới sáng tạo Vingroup, F4320328994) 5; VNU Hanoi 5; National Pingtung University of Science and Technology 4; National Research Foundation 4; Austrian Science Fund 4; Ministry of Education 4; National Science and Technology Council 3; USAID 3; Sida 3; Nguyen Tat Thanh University 3; Duy Tan University 3; Tra Vinh University 3; HUST 3; Nha Trang University 3; European Commission 3.
Caveat: funder metadata in OpenAlex comes mostly from publisher deposits and is incomplete; many works carry no funder. Counts are lower bounds and comparable only with each other.

## Q3. Vietnam-affiliated works on alternative-protein terms since 2018, grouped by institution

Filter: authorships.institutions.country_code:VN, publication_year > 2017, title/abstract/keywords match (stemmed): "meat analogue" OR "meat analog" OR "plant-based meat" OR "meat substitute" OR "textured vegetable protein" OR "high moisture extrusion" OR "cultured meat" OR "cultivated meat" OR "alternative protein(s)" OR mycoprotein OR "single cell protein" OR "precision fermentation".
Reproduce: https://api.openalex.org/?oql=get%20works%20where%20institution%20country%20is%20%5BVietnam%5D(VN)%20and%20it's%20not%20retracted%20and%20published%20after%202017%20and%20title-abstract-keywords%20has%20(stemmed%20%22alternative%20protein%22%20OR%20stemmed%20%22alternative%20proteins%22%20OR%20stemmed%20%22cultivated%20meat%22%20OR%20stemmed%20%22cultured%20meat%22%20OR%20stemmed%20%22high%20moisture%20extrusion%22%20OR%20stemmed%20%22meat%20analog%22%20OR%20stemmed%20%22meat%20analogue%22%20OR%20stemmed%20%22meat%20substitute%22%20OR%20stemmed%20%22plant-based%20meat%22%20OR%20stemmed%20%22precision%20fermentation%22%20OR%20stemmed%20%22single%20cell%20protein%22%20OR%20stemmed%20%22textured%20vegetable%20protein%22%20OR%20mycoprotein)%3B%20then%2C%20group%20those%20works%20by%20exact%20institution

Total works: 69 (lower bound; includes off-topic records such as feed trials and out-of-scope topics).
Vietnamese institutions with 2 or more: Duy Tan University 6; Industrial University of Ho Chi Minh City (IUH) 6; Department of Animal Health 6; Institute of Biotechnology and Food Technology (IUH unit, may overlap with IUH) 6; Nong Lam University HCMC 5; VNU-HCM 4; HCMUT 4; Ton Duc Thang University 3; Vinh Long University of Technology Education 3; University of Science and Technology of Hanoi 3; Hanoi University of Industry 3; Tra Vinh University 3; HUST 3; Can Tho University 2; Van Hien University 2; HCMC International University 2; VNUA 2; HCMC University of Industry and Trade 2.
Foreign co-affiliations with 2 or more: Griffith 3; Kasetsart 3; Chiang Mai 3; Padua 2; Sunshine Coast 2; Western Australia 2; Korea University 2; NIMS 2; Curtin 2; King Saud 2; others.

## Q4. Same query restricted to IUH (I202539009, I4405277918) and Nong Lam (I79775147)

11 works. Food-protein records relevant to this line: IUH 2026 jackfruit meat-analogue pate (doi:10.1556/446.2026.00250); IUH 2026 high-moisture meat analogue with jackfruit fibre (doi:10.1007/s11694-026-04231-y, already registered as TIC-21); IUH 2024 book chapter on mushroom bio-based products (doi:10.2174/9789815196115124010007). The other records are feed trials, livestock disease or out-of-scope topics.
