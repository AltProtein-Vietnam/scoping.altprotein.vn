import site from '../generated/site.json';
import type { Lang } from './i18n';

export type Section = 'front' | 'report' | 'brief' | 'appendix';

export interface PageMeta {
  id: string;
  title: string;
  short_title: string;
  heading: string;
  section: Section;
  part: string | null;
  order: number;
  lang: string;
  bilingual: boolean;
  summary: string;
  subtitle: string | null;
  audiences: string[];
  reading_time_min: number | null;
  key_numbers: string[];
  charts: string[];
  related_data: string[];
  related_pages: string[];
}

export interface NavItem {
  label?: string;
  page?: string;
  lang?: string;
  href?: string;
  children?: NavItem[];
}

export const SITE = site as unknown as {
  title: string;
  publisher: string;
  version: string;
  status: string;
  draft_notice: { en: string; vi: string; placement: string };
  versions: { version: string; date: string; earlier_label?: string; note: string }[];
  audiences: Record<string, string>;
  audience_paths: Record<string, string[]>;
  nav: NavItem[];
  pages: PageMeta[];
};

export const PAGES = SITE.pages;
export const PAGE_BY_ID = new Map(PAGES.map((p) => [p.id, p]));
/** Audiences with a reading path: the six tagged audiences, then newcomers and Vietnamese readers. */
export const AUDIENCES = [
  ...Object.keys(SITE.audiences).filter((a) => a in SITE.audience_paths),
  ...Object.keys(SITE.audience_paths).filter((a) => !(a in SITE.audiences)),
];

/** Front pages have short, readable paths; everything else lives under its section. */
const FRONT_PATHS: Record<string, string> = {
  'front-cover': '/',
  'front-exec-summary': '/summary',
  'front-two-minute': '/two-minutes',
  'front-at-a-glance': '/at-a-glance',
  'front-prologue': '/prologue',
  'front-how-to-read': '/how-to-read',
  'front-faq': '/faq',
};

/**
 * Pages the interface links to or enhances by role. Page ids change when the report is
 * regrouped, so they live here in one place, and a test checks that every one exists.
 */
export const ROLE = {
  cover: 'front-cover',
  twoMinute: 'front-two-minute',
  summary: 'front-exec-summary',
  atAGlance: 'front-at-a-glance',
  prologue: 'front-prologue',
  howToRead: 'front-how-to-read',
  faq: 'front-faq',
  method: 'app-m1-method',
  futuresMethod: 'app-m2-futures-method',
  demandMethod: 'app-m3-demand-method',
  changelog: 'app-m5-changelog',
  openQuestions: 'app-r1-open-questions',
  disagreements: 'app-r2-disagreements',
  glossary: 'app-r3-glossary',
  sources: 'app-r4-sources',
  plays: 'ch26-plays',
  policy: 'ch27-policy-options',
  scenarios: 'ch23-scenarios-2050',
  vision: 'ch24-vision-2050',
  robustMoves: 'ch28-robust-moves',
  productTargets: 'ch25-demand-to-frontier',
  actorCheck: 'ch29-actor-check',
} as const;

/** Pages that show the draft banner (the brief: the cover and the summary pages). */
export const DRAFT_BANNER_PAGES = new Set<string>([
  ROLE.cover,
  ROLE.twoMinute,
  ROLE.summary,
  ROLE.atAGlance,
]);
const SECTION_PATHS: Record<Section, string> = {
  front: '',
  report: '/report',
  brief: '/briefs',
  appendix: '/appendices',
};

export function pagePath(id: string): string {
  if (FRONT_PATHS[id]) return FRONT_PATHS[id];
  const page = PAGE_BY_ID.get(id);
  if (!page) throw new Error(`Unknown page ${id}`);
  return `${SECTION_PATHS[page.section]}/${id}`;
}

const PATH_TO_ID = new Map(PAGES.map((p) => [pagePath(p.id), p.id]));
export function pageIdForPath(pathname: string): string | undefined {
  const clean = pathname.length > 1 ? pathname.replace(/\/+$/, '') : pathname;
  return PATH_TO_ID.get(clean);
}

/** Prefix an internal path with the interface language. */
export function localize(path: string, lang: Lang): string {
  if (
    lang === 'en' ||
    /^(https?:|mailto:|#)/.test(path) ||
    (path.startsWith('/data/') && /\.\w+$/.test(path))
  )
    return path;
  if (
    path.startsWith('/downloads/') ||
    path.startsWith('/files/') ||
    path.startsWith('/workbench/view') ||
    path.startsWith('/_emdash')
  )
    return path;
  return path === '/' ? '/vi' : `/vi${path}`;
}

export function href(id: string, lang: Lang, anchor?: string): string {
  return localize(pagePath(id), lang) + (anchor ? `#${anchor}` : '');
}

/** Pages in reading order (the order of the navigation tree). */
export const READING_ORDER: string[] = (() => {
  const ids: string[] = [];
  const walk = (items: NavItem[]) =>
    items.forEach((item) => {
      if (item.page && !ids.includes(item.page)) ids.push(item.page);
      if (item.children) walk(item.children);
    });
  walk(SITE.nav);
  for (const p of PAGES) if (!ids.includes(p.id)) ids.push(p.id);
  return ids;
})();

export function neighbours(id: string) {
  const i = READING_ORDER.indexOf(id);
  const prev = i > 0 ? PAGE_BY_ID.get(READING_ORDER[i - 1]) : undefined;
  const next =
    i >= 0 && i < READING_ORDER.length - 1 ? PAGE_BY_ID.get(READING_ORDER[i + 1]) : undefined;
  return { prev, next };
}

export const PARTS = [
  ...new Set(PAGES.filter((p) => p.section === 'report').map((p) => p.part as string)),
];

export function chapterNumber(id: string): number | null {
  const m = /^ch(\d+)-/.exec(id);
  return m ? Number(m[1]) : null;
}

/** Appendix code, such as M1, S13 or R4. */
export function appendixCode(id: string): string | null {
  const m = /^app-([a-z]\d*)-/.exec(id);
  return m ? m[1].toUpperCase() : null;
}

/** Appendix groups (M, S, D, F, R) in navigation order, from the manifest. */
export const APPENDIX_GROUPS: { id: string; label: string; pages: string[] }[] = (
  SITE.nav.find((n) => n.label === 'Appendices')?.children ?? []
).map((g) => ({
  id: (g.children?.[0]?.page ? (appendixCode(g.children[0].page) ?? '') : '')
    .replace(/\d+$/, '')
    .toLowerCase(),
  label: g.label ?? '',
  pages: (g.children ?? []).map((c) => c.page!).filter(Boolean),
}));

/** Anchor id for a report part, such as part-iii. */
export function partId(part: string): string {
  return `part-${part.split('.')[0].toLowerCase()}`;
}

// Parts as questions -----------------------------------------------------------------------

export interface PartInfo {
  /** "i" to "v": used in URLs (/report/part-ii) and interface strings. */
  key: string;
  /** Roman numeral as written in the manifest ("II"). */
  numeral: string;
  /** The manifest's part label ("II. Supply: what Vietnam can make"). */
  label: string;
  chapters: PageMeta[];
}

export const PART_LIST: PartInfo[] = PARTS.map((label) => {
  const numeral = label.split('.')[0];
  return {
    key: numeral.toLowerCase(),
    numeral,
    label,
    chapters: PAGES.filter((p) => p.section === 'report' && p.part === label).sort(
      (a, b) => a.order - b.order,
    ),
  };
});
export const PART_BY_KEY = new Map(PART_LIST.map((p) => [p.key, p]));

export function partOf(id: string): PartInfo | undefined {
  const page = PAGE_BY_ID.get(id);
  return page?.part ? PART_LIST.find((p) => p.label === page.part) : undefined;
}

export function partPath(key: string): string {
  return `/report/part-${key}`;
}

/** Front pages that belong under "Summary" in the navigation. */
export const SUMMARY_PAGES = new Set<string>([
  ROLE.twoMinute,
  ROLE.summary,
  ROLE.atAGlance,
  ROLE.prologue,
  ROLE.howToRead,
  ROLE.faq,
]);

/** Which top navigation item a page sits under. */
export function navKey(id: string): string | undefined {
  const page = PAGE_BY_ID.get(id);
  if (!page) return undefined;
  if (page.section === 'report') return `part-${partOf(id)?.key}`;
  if (page.section === 'brief') return 'briefs';
  if (page.section === 'appendix')
    return id === ROLE.glossary || id === ROLE.sources ? 'reference' : 'workbench';
  if (SUMMARY_PAGES.has(id)) return 'summary';
  return undefined;
}
