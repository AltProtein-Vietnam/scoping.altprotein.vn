import csv
hdr = open('../../../data/plays.csv', encoding='utf-8').readline().strip().split(',')
hdr = [h for h in hdr if h != 'status_v0_8'] + ['gfi_nos']
with open('data_candidates.csv','w',newline='',encoding='utf-8') as f:
    csv.writer(f).writerow(hdr)

oq = [
 ("What financing ratio, term, rate and down payment do licensed lessors (for example BIDV-SuMi Trust Leasing, Chailease, Vietcombank Leasing, Sacombank Leasing) offer for an imported food-extrusion line of USD 0.1 to 1.4 million, and will they do sale and leaseback on a chay maker's existing equipment?",
  "Decides whether leasing can carry the equipment part of a T1 line (ch08 section 8.7, T1 capital note).",
  "Phone three lessors with the T1 equipment list from t1_equipment_listings.csv and ask for an indicative term sheet.",
  "Vietnam Leasing Association; BIDV-SuMi Trust Leasing","medium",""),
 ("Will a bank put a domestic textured-protein supplier into an anchor buyer's supply-chain finance programme (for example CJ Foods Vietnam or Vissan), and at what advance ratio, rate and payment term?",
  "This is the concrete form of the 'trade finance' in the T1 advice; without an anchor, T1's working capital (USD 0.6 to 3.5 million) has no named source.",
  "Ask the supply-chain finance desk of BIDV or Vietcombank with a named anchor and a draft supply contract.",
  "BIDV; CJ Foods Vietnam; Vissan","high","OQ-306"),
 ("Does an arrangement in which competing chay makers jointly buy soy flour or textured protein, or a chay makers' cooperative that buys for members, fall under the price-fixing ban in Articles 11(1) and 12(1) of the Law on Competition 2018?",
  "Section 26.7 suggests pooled offtake from two or three chay makers; the legal form decides whether that advice carries risk.",
  "Written opinion from a competition lawyer, or an informal query to the National Competition Commission.",
  "National Competition Commission (MOIT)","medium",""),
 ("Does a textured-protein plant that processes imported defatted soy flour qualify for Decree 57/2018/ND-CP Article 11 processing support, or its replacement, and how is the 1.5 times value test measured?",
  "Support of up to VND 15 billion would cover a large share of a T1 line's installed cost; the replacement draft would cut it to 30% of investment.",
  "Ask the Department of Finance or the Department of Agriculture and Environment in Ho Chi Minh City or Tay Ninh (former Long An).",
  "Provincial Departments of Finance and of Agriculture and Environment; MAE","medium",""),
 ("Is the SME Development Fund lending in 2026, at what rate and loan cap, and does a supplier to a chay value chain count as a value-chain borrower under Decree 45/2024/ND-CP?",
  "A named state lender that fits T1 better than venture money; current terms are unknown.",
  "Call the SME Development Fund or one of its partner banks.",
  "SME Development Fund (Ministry of Finance)","low",""),
 ("What fees and priority sectors does the Ho Chi Minh City SME Credit Guarantee Fund apply under its May 2026 charter, and has it guaranteed any food-processing loan?",
  "A guaranteed loan could carry most of the installed cost of a T1 line in the city.",
  "Call the fund; read the full Decision 3204/QĐ-UBND.",
  "Ho Chi Minh City SME Credit Guarantee Fund","low",""),
]
with open('open_questions.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow("question,why_it_matters,cheapest_way_to_close,owner_org_to_ask,priority,closes_oq".split(','))
    w.writerows(oq)

dg = [
 ("Number of finance-leasing companies in Vietnam (2025)",
  "VCCI report of the Vietnam Leasing Association roundtable (14 August 2025): 9 companies, of which 8 operating, 1 suspended for restructuring and 2 bankrupt, which sums to 11 (SLK-04)",
  "Interview with the CEO of BIDV-SuMi Trust Leasing (4 August 2025): eight financial leasing companies operating (SLK-24)",
  "Eight operating companies; the total number licensed is unresolved.",
  "Both sources agree on eight operating; the VCCI total is internally inconsistent. Check the SBV list of credit institutions (sbv.gov.vn returned HTTP 403)."),
 ("Finance-leasing balance, mid 2025",
  "VND 41,700 billion at 30 June 2025, reported by 6 of 9 companies (SLK-04)",
  "About VND 47,000 billion for the whole sector, the association's estimate in the same report (SLK-04)",
  "Give both: VND 41,700 billion reported; VND 47,000 billion estimated.",
  "Different coverage, not a contradiction. End-2024: 'just over VND 40 trillion', about 0.26% of credit (SLK-24); 0.25% of credit at mid 2025 (SLK-04)."),
 ("Factoring balance in Vietnam",
  "About VND 16,000 billion, stated at the VNBA and IFC roundtable of 12 August 2025 (SLK-06)",
  "About VND 22,000 billion, attributed to VNBA in 2026 in a search snippet of a page we could not read (thitruongtaichinhtiente.vn, HTTP 403; not registered)",
  "Use VND 16,000 billion (August 2025), the figure read; the snippet may refer to a later date.",
  "Snippet-only evidence is Low. Re-check when the amended factoring circular is issued."),
]
with open('disagreements.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow("topic,claim_a,claim_b,position_taken,notes".split(','))
    w.writerows(dg)

kn = [
 ("Finance leases on production lines","Dư nợ cho thuê tài chính đối với dây chuyền sản xuất","6900","billion VND","2025-06-30",
  "Outstanding finance leases on production lines, about USD 265 million (our calculation at 26,000 VND per USD); down 0.58% from end 2024. Total finance-leasing balance VND 41,700 billion (6 of 9 companies).",
  "SLK-04","VN-direct","Medium","","",""),
 ("Factoring balance in Vietnam","Dư nợ bao thanh toán tại Việt Nam","16000","billion VND","2025-08",
  "About 0.1% of total credit of nearly VND 17 million billion (our calculation). Rules: Circular 20/2024/TT-NHNN; amendment drafted March 2026.",
  "SLK-06; SLK-05","VN-direct","Medium","","",""),
 ("Ho Chi Minh City SME credit guarantee cap per customer","Hạn mức bảo lãnh tối đa cho một khách hàng của Quỹ Bảo lãnh tín dụng doanh nghiệp nhỏ và vừa TP.HCM","34","billion VND","2026-05-29",
  "15% of actual charter capital (VND 227.9 billion) for investment loans, about USD 1.3 million (our calculation); guarantees up to 100% of a loan; owner's equity of at least 20% required (Decision 3204/QĐ-UBND).",
  "SLK-20","VN-direct","High","","",""),
 ("State support for a farm-produce processing plant","Mức hỗ trợ tối đa cho dự án cơ sở chế biến nông sản","15","billion VND","2018-04-17",
  "Decree 57/2018/ND-CP Art. 11: 60% of investment up to VND 15 billion (about USD 0.58 million) per project if processed value is at least 1.5 times raw value; a replacement draft (March 2026) would cap support at 30% of investment.",
  "SLK-21; SLK-23","VN-direct","High","","",""),
 ("Supply-chain finance advance for SMEs referred by an anchor buyer","Tỷ lệ tài trợ chuỗi cung ứng tối đa cho doanh nghiệp nhỏ và vừa do doanh nghiệp đầu mối giới thiệu","85","% of order value","2026-01-16",
  "BIDV SCFast 2026 (bank release), with inventory as collateral; package up to VND 15,000 billion; unsecured distributor limits up to VND 10 billion. IFC: suppliers typically paid 30 to 60 days after delivery.",
  "SLK-19; SLK-18","VN-direct","Medium","","",""),
]
with open('key_numbers.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow("label,label_vi,value,unit,as_of,context,source_ids,evidence,confidence,foresight_type,horizon,demand_evidence_type".split(','))
    w.writerows(kn)
print('ok')
