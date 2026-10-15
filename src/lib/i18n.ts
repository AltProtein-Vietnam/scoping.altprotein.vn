// Interface text in English and Vietnamese. Report text stays in English, except the Vietnamese
// executive summary, the Vietnamese prologue, the bilingual glossary and the key-number labels.
// Writing rules (report/STYLE.md): plain English, British spelling, no em or en dashes.
export type Lang = 'en' | 'vi';

const en = {
  skip: 'Skip to content',
  siteName: 'AltProtein Vietnam',
  studyTitle: 'Alternative protein in Vietnam',
  studySub: 'A supply-side scoping study',
  draft: (v: string) => `Draft ${v}`,
  draftNotice: 'This report is a draft and subject to change.',
  home: 'Home',
  summary: 'Summary',
  briefs: 'For your role',
  report: 'The report',
  contents: 'Contents',
  allContents: 'All contents',
  search: 'Search',
  searchPlaceholder: 'Search the report and glossary',
  menu: 'Menu',
  close: 'Close',
  theme: 'Theme',
  themeNames: { auto: 'automatic', light: 'light', dark: 'dark' } as Record<string, string>,
  switchToLabel: 'Xem giao diện tiếng Việt',
  minRead: (n: number) => `${n} min read`,
  minutes: (n: number) => `${n} min`,
  onThisPage: 'On this page',
  inThisPart: 'In this part',
  previous: 'Previous',
  next: 'Next',
  related: 'Read next',
  sourcesCited: 'Sources cited on this page',
  sourcesCitedHint:
    'Numbers in the text link here. Every source is also listed in the full source list.',
  allSources: 'Full source list',
  keyNumbers: 'Key numbers',
  derived: 'Our calculation',
  source: 'Source',
  sources: 'Sources',
  showData: 'Show the data',
  hideData: 'Hide the data',
  chartUnavailable: 'This chart is not available in this build.',
  contextAndSources: 'Context and sources',
  readChapter: 'Read the chapter',
  evidence: 'Evidence',
  howToRead: 'How to read the evidence',
  visionNotForecast: 'Vision, not forecast',
  print: 'Print',
  answer: 'In brief',
  writtenFor: 'Written for',
  chapter: (n: number | string) => `Chapter ${n}`,
  part: (n: string) => `Part ${n}`,
  appendix: (code: string) => `Appendix ${code}`,
  brief: 'Brief',
  frontMatter: 'Summary',

  // Evidence marks -----------------------------------------------------------------------
  scope: {
    direct: 'Vietnam',
    adjacent: 'Comparable country',
    general: 'Global',
  } as Record<string, string>,
  scopeLong: {
    direct: 'evidence about Vietnam (VN-direct)',
    adjacent: 'evidence from a comparable country, with the transfer stated (VN-adjacent)',
    general: 'global evidence, not specific to Vietnam (general)',
  } as Record<string, string>,
  conf: { high: 'High', medium: 'Medium', low: 'Low' } as Record<string, string>,
  confLong: {
    high: 'high confidence: a primary source was read',
    medium: 'medium confidence: a reputable secondary source, or a primary source read in part',
    low: 'low confidence: a single claim, press, company marketing or our derivation from weak inputs',
  } as Record<string, string>,
  fx: {
    trend: 'trend',
    projection: 'projection',
    estimate: 'estimate',
    signal: 'signal',
    wildcard: 'wildcard',
    vision: 'vision',
  } as Record<string, string>,
  fxLong: {
    trend: 'observed change expected to continue',
    projection: 'a published model result or an official target',
    estimate: 'our own calculation from stated assumptions',
    signal: 'an emerging development that may or may not scale',
    wildcard: 'a low-probability, high-impact event',
    vision: 'normative: what we think should happen, not a forecast',
  } as Record<string, string>,
  dx: { stated: 'stated', revealed: 'revealed', tested: 'tested', inferred: 'inferred' } as Record<
    string,
    string
  >,
  dxLong: {
    stated: 'what people say: surveys, focus groups, stated intentions',
    revealed: 'what people or firms do: sales, prices, trade, menus, shelves',
    tested: 'tastings, real-money auctions, choice experiments or field trials',
    inferred: 'our inference or calculation',
  } as Record<string, string>,
  evidenceLabel: 'Evidence',
  foresightLabel: 'Forward-looking',
  demandLabel: 'Demand evidence',
  confidenceLabel: 'confidence',
  legendTitle: 'How sure are we?',
  legendIntro:
    'Every claim in the report carries a mark for the kind of evidence behind it and how confident we are. On wide screens the marks sit in the margin beside the claim; select a number to see its sources.',
  legendScope: 'Where the evidence comes from',
  legendConf: 'Confidence',
  legendFx: 'Claims about the future',
  legendDx: 'Claims about demand',
  legendMore: 'The full explanation, with the codes and scenario names',

  // Navigation by question -----------------------------------------------------------------
  parts: {
    i: { nav: 'Why Vietnam', question: 'Why Vietnam?' },
    ii: { nav: 'What it could make', question: 'What could Vietnam make?' },
    iii: { nav: 'Who would buy', question: 'Who would buy it?' },
    iv: { nav: '2035 and 2050', question: 'What could 2035 and 2050 look like?' },
    v: { nav: 'What to do', question: 'What should be done?' },
  } as Record<string, { nav: string; question: string }>,
  chaptersCount: (n: number) => `${n} chapters`,
  reportIntro:
    'Thirty chapters in five parts. Each part answers one question, and each chapter opens with its answer.',
  briefsIntro:
    'Six short briefs, one per audience: what the study means for you, and where to read next.',
  appendicesHeading: 'Appendices',
  appendicesIntro:
    'The detailed evidence by theme: method and record (M), context and supply (S), demand (D), futures (F) and registers (R).',
  appendicesPublic:
    'While the report is a draft, the evidence appendices and the registers of open questions and disagreements are shared with reviewers only. The glossary and the full source list are open to everyone.',

  // Home -------------------------------------------------------------------------------
  homeReadSummary: 'Executive summary',
  homeReadVi: 'Tóm tắt tiếng Việt',
  homeNewcomers: 'New to alternative protein?',
  homeArgument: 'The argument',
  homeArgumentIntro: (n: number) =>
    `The whole report in ${n} steps. Each step shows its main number and links to the chapter with the evidence.`,
  homeEvidenceIn: 'Evidence in',
  homeForYou: 'Read it for your role',
  homeForYouIntro:
    'Each brief says what the study means for one kind of reader. Choose your role to see a reading path through the report.',
  homeAudienceAll: 'Everyone',
  homePath: 'Your reading path',
  homeReport: 'The report, part by part',
  homeReportIntro: 'Thirty chapters in five parts. Each part answers one question.',
  homeHowWeKnow: 'How we know',
  homeAbout: 'About this study',

  // Access ------------------------------------------------------------------------------
  lockedTitle: 'This page is for reviewers',
  lockedText:
    'While the report is a draft, the evidence appendices, the registers of open questions and disagreements, and the data tables are shared with reviewers only. The chapters, briefs and summaries carry the findings, and every source is listed.',
  lockedKind: {
    evidence: 'Evidence appendix',
    register: 'Register',
    record: 'Method and record',
  } as Record<string, string>,
  lockedSignIn: 'Editor sign in',
  lockedBack: 'Read the report',
  lockedLink: 'Shared with reviewers while the report is a draft',
  editorView: 'Editor view',
  editorViewText: 'You can see the appendices, registers, data and files that the public cannot.',
  publicView: 'Public view',
  publicViewText: 'You are seeing the site as the public does.',
  toPublic: 'See the public view',
  toEditor: 'Back to the editor view',
  workbench: 'Workbench',
  cms: 'Edit in the CMS',
  forReviewers: 'For reviewers',

  // Workbench --------------------------------------------------------------------------
  wbTitle: 'Workbench',
  wbIntro:
    'Everything that is shared with reviewers but not with the public: the evidence appendices, the registers, the data tables and the downloads.',
  wbAppendices: 'Appendices',
  wbRegisters: 'Registers as tables',
  wbData: 'Data',
  wbDownloads: 'Downloads',
  wbCms: 'Content management',
  wbCmsText:
    'Page text is edited in the CMS. Structure, data, charts and key numbers come from the report package and change with a deploy.',

  // Data browser (editors) -------------------------------------------------------------
  dataHeading: 'Data',
  dataIntro:
    'Every table behind the report, with the column descriptions from the data dictionary. Filter, sort and download as CSV.',
  dataFeatured: 'Most used tables',
  dataChart: 'Chart data',
  reportData: 'Report data',
  rows: 'rows',
  columns: 'Columns',
  columnsCount: (n: number) => `${n} columns`,
  column: 'Column',
  meaning: 'Meaning',
  file: 'File',
  purpose: 'Purpose',
  download: 'Download CSV',
  downloads: 'Downloads',
  downloadData: 'All data, sources and tools (zip)',
  downloadWorking: 'Working papers from research waves 1 to 13 (zip)',
  downloadMarkdown: 'Report text as Markdown (zip)',
  dataDictionary: 'Data dictionary (Markdown)',
  filter: 'Filter rows',
  filterPlaceholder: 'Type to filter…',
  loadMore: 'Show more rows',
  usedIn: 'Used in',
  noJs: 'The interactive table needs JavaScript. You can still download the CSV.',
  asTable: 'As a table',
  registerViews: {
    openQuestions: 'Filter the open questions',
    disagreements: 'Filter the disagreements',
    glossary: 'Search the glossary',
    sources: 'Filter the sources',
  } as Record<string, string>,

  // Search -----------------------------------------------------------------------------
  searchHeading: 'Search',
  searchResults: (n: number, q: string) => `${n} results for “${q}”`,
  searchNone: (q: string) => `Nothing found for “${q}”. Try a shorter or different word.`,
  searchHint: 'Search the full text of the summaries, chapters and briefs, and the glossary.',
  searchHintEditor:
    'Search the full text of every page, the glossary, companies, facilities, open questions, disagreements and policy options.',
  allKinds: 'All',
  kinds: {
    page: 'Page',
    glossary: 'Glossary',
    company: 'Company',
    facility: 'Facility',
    question: 'Open question',
    disagreement: 'Disagreement',
    policy: 'Policy option',
  } as Record<string, string>,
  filterByType: 'Filter by type',

  // Glossary ---------------------------------------------------------------------------
  glossaryHeading: 'Glossary',
  glossaryIntro: 'Terms used in the report, in English and Vietnamese.',
  glossaryFilter: 'Find a term in English or Vietnamese',
  glossaryCount: (n: number, total: number) => `${n} of ${total} terms`,
  category: 'Category',
  allCategories: 'All categories',

  // About ------------------------------------------------------------------------------
  about: 'About this study',
  editorSignIn: 'Editor sign in',
  notAdvice: 'Scoping research. Not investment, legal or engineering advice.',
  footerLine:
    'An evidence-tagged scoping study of what Vietnam could make for people to eat, from what, under which rules, at what cost, and who would buy it.',
  footerReport: 'The report',
  footerReference: 'Reference',
  footerAbout: 'About',
  twoMinutes: 'The report in two minutes',
  atAGlance: 'At a glance',
  faq: 'Questions people ask',
  sourcesPage: 'Sources',
  notFound: 'Page not found',
  notFoundText: 'We could not find that page. It may have moved when the report was regrouped.',
  backHome: 'Back to the home page',
  previewNote: 'Editor preview: unpublished changes.',
  exitPreview: 'Exit preview',
  pageInVi: 'This page is in Vietnamese.',
  pageInEn: 'Nội dung trang này bằng tiếng Anh.',
  readEnSummary: 'Read the English summary',
  readEnPrologue: 'Read the English prologue',
  readViSummary: 'Đọc bản tóm tắt tiếng Việt',
  readViPrologue: 'Đọc lời mở đầu tiếng Việt',

  // Plays and scenarios (chapters 26 and 23) ---------------------------------------------
  plays: {
    heading: 'Re-rank the plays',
    intro:
      'Choose a preset or move the sliders. The score is the sum of each criterion score times its weight, divided by 100.',
    preset: 'Weight preset',
    custom: 'Custom',
    weights: 'Weights',
    total: 'Total weight',
    reset: 'Reset',
    score: 'Score',
    rank: 'Rank',
    select: 'Select a play to see its card.',
    what: 'What it is',
    whyVietnam: 'Why Vietnam',
    mustBeTrue: 'What must be true',
    killTests: 'Kill tests',
    firstCustomers: 'First customers',
    partners: 'Partners',
    horizon: 'Horizon',
    capital: 'Capital',
    staticNote: 'Balanced weights. Turn on JavaScript to change the weights.',
  },
  scenarios: {
    heading: 'Explore the four worlds',
    intro:
      'Select a world to see its picture of 2050, the signposts that would tell you it is arriving, and how each play fares in it.',
    picture: 'The picture in 2050',
    signposts: 'Signposts',
    playScores: 'Plays in this world',
    axes: 'Axes',
  },
};

type Dict = typeof en;

const vi: Dict = {
  ...en,
  skip: 'Chuyển đến nội dung',
  studyTitle: 'Protein thay thế tại Việt Nam',
  studySub: 'Nghiên cứu xác định phạm vi phía cung',
  draft: (v: string) => `Bản thảo ${v}`,
  draftNotice: 'Báo cáo này là bản dự thảo và có thể thay đổi.',
  home: 'Trang chủ',
  summary: 'Tóm tắt',
  briefs: 'Dành cho bạn',
  report: 'Báo cáo',
  contents: 'Mục lục',
  allContents: 'Toàn bộ mục lục',
  search: 'Tìm kiếm',
  searchPlaceholder: 'Tìm trong báo cáo và bảng thuật ngữ',
  menu: 'Mục lục',
  close: 'Đóng',
  theme: 'Giao diện',
  themeNames: { auto: 'tự động', light: 'sáng', dark: 'tối' },
  switchToLabel: 'View the interface in English',
  minRead: (n: number) => `${n} phút đọc`,
  minutes: (n: number) => `${n} phút`,
  onThisPage: 'Trong trang này',
  inThisPart: 'Trong phần này',
  previous: 'Trang trước',
  next: 'Trang sau',
  related: 'Đọc tiếp',
  sourcesCited: 'Nguồn được trích dẫn trong trang',
  sourcesCitedHint:
    'Các số trong bài dẫn đến danh sách này. Mọi nguồn cũng có trong danh sách nguồn đầy đủ.',
  allSources: 'Danh sách nguồn đầy đủ',
  keyNumbers: 'Số liệu chính',
  derived: 'Tính toán của nhóm nghiên cứu',
  source: 'Nguồn',
  sources: 'Nguồn',
  showData: 'Xem số liệu',
  hideData: 'Ẩn số liệu',
  chartUnavailable: 'Biểu đồ này chưa có trong bản dựng này.',
  contextAndSources: 'Bối cảnh và nguồn',
  readChapter: 'Đọc chương',
  evidence: 'Bằng chứng',
  howToRead: 'Cách đọc nhãn bằng chứng',
  visionNotForecast: 'Tầm nhìn, không phải dự báo',
  print: 'In',
  answer: 'Tóm lược',
  writtenFor: 'Dành cho',
  chapter: (n: number | string) => `Chương ${n}`,
  part: (n: string) => `Phần ${n}`,
  appendix: (code: string) => `Phụ lục ${code}`,
  brief: 'Bản tóm lược',
  frontMatter: 'Tóm tắt',

  scope: { direct: 'Việt Nam', adjacent: 'Nước tương đồng', general: 'Toàn cầu' },
  scopeLong: {
    direct: 'bằng chứng về Việt Nam (VN-direct)',
    adjacent: 'bằng chứng từ một nước tương đồng, có nêu giả định chuyển đổi (VN-adjacent)',
    general: 'bằng chứng chung, không riêng Việt Nam (general)',
  },
  conf: { high: 'Cao', medium: 'Trung bình', low: 'Thấp' },
  confLong: {
    high: 'độ tin cậy cao: đã đọc nguồn gốc',
    medium: 'độ tin cậy trung bình: nguồn thứ cấp uy tín, hoặc đọc một phần nguồn gốc',
    low: 'độ tin cậy thấp: một nhận định đơn lẻ, báo chí, tiếp thị của doanh nghiệp hoặc suy ra từ dữ liệu yếu',
  },
  fx: {
    trend: 'xu hướng',
    projection: 'dự phóng',
    estimate: 'ước tính',
    signal: 'tín hiệu',
    wildcard: 'biến cố hiếm',
    vision: 'tầm nhìn',
  },
  fxLong: {
    trend: 'thay đổi đã quan sát được và dự kiến tiếp tục',
    projection: 'kết quả mô hình đã công bố hoặc mục tiêu chính thức',
    estimate: 'tính toán của nhóm từ các giả định đã nêu',
    signal: 'diễn biến mới nổi, có thể lan rộng hoặc không',
    wildcard: 'biến cố xác suất thấp, tác động lớn',
    vision: 'chuẩn tắc: điều chúng tôi cho là nên xảy ra, không phải dự báo',
  },
  dx: { stated: 'được nêu', revealed: 'bộc lộ', tested: 'được thử', inferred: 'suy luận' },
  dxLong: {
    stated: 'điều người ta nói: khảo sát, thảo luận nhóm, ý định',
    revealed: 'điều người ta hoặc doanh nghiệp làm: doanh số, giá, thương mại, thực đơn, kệ hàng',
    tested: 'nếm thử, đấu giá bằng tiền thật, thí nghiệm lựa chọn hoặc thử nghiệm thực địa',
    inferred: 'suy luận hoặc tính toán của nhóm',
  },
  evidenceLabel: 'Bằng chứng',
  foresightLabel: 'Hướng tới tương lai',
  demandLabel: 'Bằng chứng về nhu cầu',
  confidenceLabel: 'độ tin cậy',
  legendTitle: 'Chúng tôi chắc chắn đến đâu?',
  legendIntro:
    'Mỗi nhận định trong báo cáo có một dấu cho loại bằng chứng và mức độ tin cậy. Trên màn hình rộng, các dấu nằm ở lề cạnh nhận định; chọn một con số để xem nguồn.',
  legendScope: 'Bằng chứng đến từ đâu',
  legendConf: 'Độ tin cậy',
  legendFx: 'Nhận định về tương lai',
  legendDx: 'Nhận định về nhu cầu',
  legendMore: 'Giải thích đầy đủ, kèm bảng mã và tên kịch bản',

  parts: {
    i: { nav: 'Vì sao Việt Nam', question: 'Vì sao là Việt Nam?' },
    ii: { nav: 'Có thể làm gì', question: 'Việt Nam có thể sản xuất gì?' },
    iii: { nav: 'Ai sẽ mua', question: 'Ai sẽ mua?' },
    iv: { nav: '2035 và 2050', question: 'Năm 2035 và 2050 có thể ra sao?' },
    v: { nav: 'Nên làm gì', question: 'Nên làm gì?' },
  },
  chaptersCount: (n: number) => `${n} chương`,
  reportIntro:
    'Ba mươi chương trong năm phần. Mỗi phần trả lời một câu hỏi, và mỗi chương mở đầu bằng câu trả lời. Nội dung báo cáo bằng tiếng Anh.',
  briefsIntro:
    'Sáu bản tóm lược ngắn, mỗi bản cho một nhóm độc giả: nghiên cứu có ý nghĩa gì với bạn và nên đọc tiếp ở đâu.',
  appendicesHeading: 'Phụ lục',
  appendicesIntro:
    'Bằng chứng chi tiết theo chủ đề: phương pháp và hồ sơ (M), bối cảnh và phía cung (S), phía cầu (D), tương lai (F) và các sổ đăng ký (R).',
  appendicesPublic:
    'Trong giai đoạn dự thảo, các phụ lục bằng chứng và sổ đăng ký câu hỏi mở, điểm bất đồng chỉ được chia sẻ với người góp ý. Bảng thuật ngữ và danh sách nguồn đầy đủ được công khai.',

  homeReadSummary: 'Tóm tắt (tiếng Anh)',
  homeReadVi: 'Đọc tóm tắt tiếng Việt',
  homeNewcomers: 'Lời mở đầu cho người mới',
  homeArgument: 'Lập luận',
  homeArgumentIntro: (n: number) =>
    `Toàn bộ báo cáo trong ${n} bước. Mỗi bước có con số chính và liên kết đến chương chứa bằng chứng. Nội dung bằng tiếng Anh.`,
  homeEvidenceIn: 'Bằng chứng trong',
  homeForYou: 'Đọc theo vai trò của bạn',
  homeForYouIntro:
    'Mỗi bản tóm lược nói nghiên cứu có ý nghĩa gì với một nhóm độc giả. Chọn vai trò của bạn để xem lộ trình đọc gợi ý.',
  homeAudienceAll: 'Tất cả',
  homePath: 'Lộ trình đọc gợi ý',
  homeReport: 'Báo cáo theo từng phần',
  homeReportIntro: 'Ba mươi chương trong năm phần. Mỗi phần trả lời một câu hỏi.',
  homeHowWeKnow: 'Cơ sở của các kết luận',
  homeAbout: 'Về nghiên cứu này',

  lockedTitle: 'Trang này dành cho người góp ý',
  lockedText:
    'Trong giai đoạn dự thảo, các phụ lục bằng chứng, sổ đăng ký câu hỏi mở và điểm bất đồng, cùng các bảng dữ liệu chỉ được chia sẻ với người góp ý. Các chương, bản tóm lược và bản tóm tắt nêu các kết luận, và mọi nguồn đều được liệt kê.',
  lockedKind: {
    evidence: 'Phụ lục bằng chứng',
    register: 'Sổ đăng ký',
    record: 'Phương pháp và hồ sơ',
  },
  lockedSignIn: 'Đăng nhập biên tập',
  lockedBack: 'Đọc báo cáo',
  lockedLink: 'Chỉ chia sẻ với người góp ý trong giai đoạn dự thảo',
  editorView: 'Chế độ biên tập',
  editorViewText:
    'Bạn đang xem cả phụ lục, sổ đăng ký, dữ liệu và tệp mà công chúng không xem được.',
  publicView: 'Chế độ công khai',
  publicViewText: 'Bạn đang xem trang như công chúng.',
  toPublic: 'Xem như công chúng',
  toEditor: 'Về chế độ biên tập',
  workbench: 'Bàn làm việc',
  cms: 'Sửa trong CMS',
  forReviewers: 'Cho người góp ý',

  wbTitle: 'Bàn làm việc',
  wbIntro:
    'Mọi thứ được chia sẻ với người góp ý nhưng không công khai: phụ lục bằng chứng, sổ đăng ký, bảng dữ liệu và tệp tải về.',
  wbAppendices: 'Phụ lục',
  wbRegisters: 'Sổ đăng ký dạng bảng',
  wbData: 'Dữ liệu',
  wbDownloads: 'Tải về',
  wbCms: 'Quản lý nội dung',
  wbCmsText:
    'Văn bản các trang được sửa trong CMS. Cấu trúc, dữ liệu, biểu đồ và số liệu chính lấy từ gói báo cáo và thay đổi khi triển khai.',

  dataHeading: 'Dữ liệu',
  dataIntro:
    'Toàn bộ bảng số liệu của báo cáo, kèm mô tả cột từ từ điển dữ liệu. Có thể lọc, sắp xếp và tải về dạng CSV.',
  dataFeatured: 'Các bảng dùng nhiều nhất',
  dataChart: 'Số liệu biểu đồ',
  reportData: 'Dữ liệu của báo cáo',
  rows: 'dòng',
  columns: 'Các cột',
  columnsCount: (n: number) => `${n} cột`,
  column: 'Cột',
  meaning: 'Ý nghĩa',
  file: 'Tệp',
  purpose: 'Mục đích',
  download: 'Tải CSV',
  downloads: 'Tải về',
  downloadData: 'Toàn bộ dữ liệu, nguồn và công cụ (zip)',
  downloadWorking: 'Tài liệu làm việc của các đợt nghiên cứu 1 đến 13 (zip)',
  downloadMarkdown: 'Văn bản báo cáo dạng Markdown (zip)',
  dataDictionary: 'Từ điển dữ liệu (Markdown)',
  filter: 'Lọc dòng',
  filterPlaceholder: 'Gõ để lọc…',
  loadMore: 'Xem thêm dòng',
  usedIn: 'Dùng trong',
  noJs: 'Bảng tương tác cần JavaScript. Bạn vẫn có thể tải tệp CSV.',
  asTable: 'Dạng bảng',
  registerViews: {
    openQuestions: 'Lọc các câu hỏi mở',
    disagreements: 'Lọc các điểm bất đồng',
    glossary: 'Tìm trong bảng thuật ngữ',
    sources: 'Lọc các nguồn',
  },

  searchHeading: 'Tìm kiếm',
  searchResults: (n: number, q: string) => `${n} kết quả cho “${q}”`,
  searchNone: (q: string) => `Không tìm thấy kết quả cho “${q}”. Hãy thử từ ngắn hơn hoặc từ khác.`,
  searchHint:
    'Tìm trong toàn văn các bản tóm tắt, các chương, các bản tóm lược và bảng thuật ngữ. Nội dung báo cáo bằng tiếng Anh.',
  searchHintEditor:
    'Tìm trong toàn văn các trang, bảng thuật ngữ, doanh nghiệp, cơ sở sản xuất, câu hỏi mở, điểm bất đồng và phương án chính sách.',
  allKinds: 'Tất cả',
  kinds: {
    page: 'Trang',
    glossary: 'Thuật ngữ',
    company: 'Doanh nghiệp',
    facility: 'Cơ sở',
    question: 'Câu hỏi mở',
    disagreement: 'Điểm bất đồng',
    policy: 'Phương án chính sách',
  },
  filterByType: 'Lọc theo loại',

  glossaryHeading: 'Thuật ngữ',
  glossaryIntro: 'Các thuật ngữ dùng trong báo cáo, bằng tiếng Anh và tiếng Việt.',
  glossaryFilter: 'Tìm thuật ngữ tiếng Anh hoặc tiếng Việt',
  glossaryCount: (n: number, total: number) => `${n} trên ${total} thuật ngữ`,
  category: 'Nhóm',
  allCategories: 'Tất cả nhóm',

  about: 'Về nghiên cứu này',
  editorSignIn: 'Đăng nhập biên tập',
  notAdvice: 'Nghiên cứu xác định phạm vi. Không phải tư vấn đầu tư, pháp lý hay kỹ thuật.',
  footerLine:
    'Nghiên cứu xác định phạm vi có gắn nhãn bằng chứng: Việt Nam có thể sản xuất loại protein nào cho người dân ăn, từ nguyên liệu nào, theo quy định nào, với chi phí bao nhiêu, và ai sẽ mua.',
  footerReport: 'Báo cáo',
  footerReference: 'Tra cứu',
  footerAbout: 'Giới thiệu',
  twoMinutes: 'Báo cáo trong hai phút',
  atAGlance: 'Tổng quan nhanh',
  faq: 'Câu hỏi thường gặp',
  sourcesPage: 'Nguồn',
  notFound: 'Không tìm thấy trang',
  notFoundText:
    'Chúng tôi không tìm thấy trang này. Có thể trang đã được chuyển khi báo cáo được sắp xếp lại.',
  backHome: 'Về trang chủ',
  previewNote: 'Bản xem trước của biên tập viên: nội dung chưa xuất bản.',
  exitPreview: 'Thoát',

  plays: {
    heading: 'Xếp hạng lại các hướng đi',
    intro:
      'Chọn một bộ trọng số hoặc kéo thanh trượt. Điểm bằng tổng điểm từng tiêu chí nhân trọng số, chia cho 100.',
    preset: 'Bộ trọng số',
    custom: 'Tùy chỉnh',
    weights: 'Trọng số',
    total: 'Tổng trọng số',
    reset: 'Đặt lại',
    score: 'Điểm',
    rank: 'Hạng',
    select: 'Chọn một hướng đi để xem chi tiết.',
    what: 'Nội dung',
    whyVietnam: 'Vì sao là Việt Nam',
    mustBeTrue: 'Điều kiện cần đúng',
    killTests: 'Phép thử loại bỏ',
    firstCustomers: 'Khách hàng đầu tiên',
    partners: 'Đối tác',
    horizon: 'Thời gian',
    capital: 'Vốn',
    staticNote: 'Trọng số cân bằng. Bật JavaScript để thay đổi trọng số.',
  },
  scenarios: {
    heading: 'Khám phá bốn thế giới',
    intro:
      'Chọn một thế giới để xem bức tranh năm 2050, các dấu hiệu báo trước và kết quả của từng hướng đi.',
    picture: 'Bức tranh năm 2050',
    signposts: 'Dấu hiệu báo trước',
    playScores: 'Các hướng đi trong thế giới này',
    axes: 'Các trục',
  },
};

export const STRINGS: Record<Lang, Dict> = { en, vi };

export function t(lang: Lang): Dict {
  return STRINGS[lang];
}

/** Vietnamese labels for navigation groups and audiences (report content stays in English). */
const VI_LABELS: Record<string, string> = {
  'Method and record (M1 to M5)': 'Phương pháp và hồ sơ (M1 đến M5)',
  'Context and supply evidence (S1 to S14)': 'Bằng chứng về bối cảnh và phía cung (S1 đến S14)',
  'Demand evidence (D1 to D8)': 'Bằng chứng về phía cầu (D1 đến D8)',
  'Futures evidence (F1 to F6)': 'Bằng chứng về tương lai (F1 đến F6)',
  'Registers (R1 to R4)': 'Các sổ đăng ký (R1 đến R4)',
  investors: 'Nhà đầu tư',
  policy: 'Nhà hoạch định chính sách',
  startups: 'Startup và nhà sáng lập',
  manufacturers: 'Doanh nghiệp thực phẩm và thức ăn chăn nuôi',
  research: 'Trường đại học và viện nghiên cứu',
  international: 'Tổ chức quốc tế',
  'vietnamese-readers': 'Độc giả tiếng Việt',
  newcomers: 'Người mới tìm hiểu',
};

const EN_AUDIENCE: Record<string, string> = {
  'vietnamese-readers': 'Vietnamese readers',
  newcomers: 'New to alternative protein',
};

export function label(text: string, lang: Lang): string {
  return lang === 'vi' ? (VI_LABELS[text] ?? text) : text;
}

export function audienceLabel(key: string, lang: Lang, fallback?: string): string {
  if (lang === 'vi') return VI_LABELS[key] ?? fallback ?? key;
  return fallback ?? EN_AUDIENCE[key] ?? key;
}
