// Who sees what. Public readers get the summaries, the chapters, the briefs, the glossary and
// the source list. Signed-in Editors and Administrators also get the evidence appendices (M, S,
// D, F), the open questions and disagreements registers (R1, R2), the data browser and every
// downloadable file. The rule lives here so pages, links, search and the sitemap agree.
import { PAGE_BY_ID, ROLE, appendixCode } from './site';

/** EmDash role numbers: subscriber 10, contributor 20, author 30, editor 40, admin 50. */
export const EDITOR_ROLE = 40;

/** Appendices that stay public: the glossary and the source list every citation links to. */
const PUBLIC_APPENDICES = new Set<string>([ROLE.glossary, ROLE.sources]);

export function isEditorUser(user?: { role: number } | null): boolean {
  return Boolean(user && user.role >= EDITOR_ROLE);
}

/** Pages only editors may read. */
export function isRestrictedPage(id: string): boolean {
  const page = PAGE_BY_ID.get(id);
  if (!page) return false;
  return page.section === 'appendix' && !PUBLIC_APPENDICES.has(id);
}

export function canReadPage(id: string, editor: boolean): boolean {
  return editor || !isRestrictedPage(id);
}

/** Why a page is restricted, for the sign-in notice: register or evidence appendix. */
export function restrictedKind(id: string): 'register' | 'record' | 'evidence' | null {
  if (!isRestrictedPage(id)) return null;
  const code = appendixCode(id) ?? '';
  if (code.startsWith('R')) return 'register';
  if (code.startsWith('M')) return 'record';
  return 'evidence';
}

/** URL prefix for files served only to editors (CSV, JSON, Markdown, zip). */
export const FILES_PREFIX = '/files';

/** Cookie an editor sets to see the site as the public does. */
export const VIEW_COOKIE = 'apv_view';
