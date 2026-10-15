import { Marked, type Tokens, type TokenizerAndRendererExtension } from 'marked';
import keyNumbersJson from '../generated/key-numbers.json';
import sourcesJson from '../generated/sources.json';
import { canReadPage } from './access';
import { t, type Lang } from './i18n';
import {
  demandBadge,
  escapeHtml,
  evidenceBadge,
  evidenceNote,
  foresightBadge,
  meter,
  scopeOf,
  type Evidence,
} from './html';
import { href, PAGE_BY_ID, ROLE, localize } from './site';
import { renderChartFigure } from './charts';
import { renderScenarioExplorer } from './widgets';

export { demandBadge, escapeHtml, evidenceBadge, foresightBadge };

export interface KeyNumber {
  id: string;
  label: string;
  label_vi?: string;
  value: string;
  unit?: string;
  as_of?: string;
  context?: string;
  source_ids?: string[];
  derived?: boolean;
  evidence?: string;
  confidence?: string;
  primary_page?: string;
  foresight_type?: string;
  demand_evidence_type?: string;
  horizon?: string | number;
}
export interface Source {
  t: string;
  a: string;
  d: string;
  u: string;
  y: string;
}
export const KEY_NUMBERS = keyNumbersJson as Record<string, KeyNumber>;
export const SOURCES = sourcesJson as Record<string, Source>;

export interface TocEntry {
  id: string;
  text: string;
  depth: number;
}
export interface RenderResult {
  html: string;
  heading: string | null;
  toc: TocEntry[];
  citations: string[];
}
export interface RenderOptions {
  lang: Lang;
  /** Language of the page content (the Vietnamese summary is `vi`). */
  contentLang?: string;
  pageId?: string;
  /** Editor view: links to restricted pages stay links. */
  editor?: boolean;
  /** Where citation numbers link: the page's own source list (default) or the full list. */
  citeTarget?: 'page' | 'sources';
}

export function slugify(text: string): string {
  return text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/đ/g, 'd')
    .replace(/<[^>]+>/g, '')
    .replace(/&[a-z]+;/g, '')
    .replace(/[^\w\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-');
}

export const stripTags = (html: string) =>
  html
    .replace(/<[^>]+>/g, '')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .trim();

const CALLOUT_KINDS: [RegExp, string][] = [
  [/^(draft for review|bản thảo)/i, 'draft'],
  [/^correction/i, 'correction'],
  [/^method note/i, 'method'],
  [/^(vision, not forecast|tầm nhìn)/i, 'vision'],
  [/^speculative/i, 'speculative'],
  [/^scenarios, not forecasts/i, 'scenarios'],
  [/^open question/i, 'question'],
  [/^read with care|^not legal advice/i, 'care'],
  [/^for (investors|policy makers)/i, 'audience'],
  [/^(how to|neutrality)/i, 'note'],
];

/** Labels of the answer-first paragraph that opens chapters ("In brief") and briefs. */
const ANSWER_LABELS = /^(In brief|The short version|Tóm lược|Tóm tắt)$/;

/** Per-render state shared by the extensions (reset for every page). */
interface State {
  opts: RenderOptions;
  citations: string[];
  toc: TocEntry[];
  slugs: Map<string, number>;
  heading: string | null;
}

function sourceTip(id: string): string {
  const s = SOURCES[id];
  return s ? `${s.a ? `${s.a}. ` : ''}${s.t}${s.d ? ` (${s.d})` : ''}` : id;
}

function citeLinks(state: State, ids: string[]): string {
  const { lang, citeTarget = 'page' } = state.opts;
  const links = ids.map((id) => {
    let n = state.citations.indexOf(id) + 1;
    if (!n) n = state.citations.push(id);
    const target = citeTarget === 'page' ? `#src-${escapeHtml(id)}` : href(ROLE.sources, lang, id);
    return `<a href="${target}" data-src="${escapeHtml(id)}" title="${escapeHtml(`${id}: ${sourceTip(id)}`)}">${n}</a>`;
  });
  return `<sup class="cite">${links.join('<span class="cite-sep">,</span>')}</sup>`;
}

/** The stat tile for a key number: value first, then what it measures, then how sure we are. */
function keyNumberTile(state: State, id: string, size: 'normal' | 'hero' = 'normal'): string {
  const k = KEY_NUMBERS[id];
  const { lang, contentLang, editor } = state.opts;
  const s = t(lang);
  if (!k) return `<div class="kn kn-missing">${escapeHtml(id)}</div>`;
  const useVi = (contentLang === 'vi' || lang === 'vi') && k.label_vi;
  const labelText = useVi ? k.label_vi! : k.label;
  const vision = k.foresight_type === 'vision';
  const primary =
    k.primary_page &&
    k.primary_page !== state.opts.pageId &&
    PAGE_BY_ID.has(k.primary_page) &&
    canReadPage(k.primary_page, Boolean(editor));
  const ev: Evidence = {
    label: k.evidence,
    confidence: k.confidence,
    fx: k.foresight_type,
    dx: k.demand_evidence_type,
  };
  const hasEv = Boolean((k.evidence && k.confidence) || k.foresight_type || k.demand_evidence_type);
  const scope = k.evidence ? scopeOf(k.evidence) : 'general';
  const long = k.value.length > 16 ? ' kn-long' : '';
  return `<figure class="kn${size === 'hero' ? ' kn-hero' : ''}${long}${vision ? ' kn-vision' : ''}" id="${escapeHtml(id)}" data-ev="${scope}">
<p class="kn-value">${escapeHtml(k.value)}</p>
<figcaption class="kn-label"${useVi ? ' lang="vi"' : ''}>${escapeHtml(labelText)}</figcaption>
<p class="kn-meta">${k.as_of ? `<span class="kn-asof">${escapeHtml(k.as_of)}</span>` : ''}${k.derived ? `<span class="kn-derived">${escapeHtml(s.derived)}</span>` : ''}${vision ? `<span class="kn-vision-label">${escapeHtml(s.visionNotForecast)}</span>` : ''}${hasEv ? evidenceNote(ev, lang, { inline: true }) : ''}</p>
${k.context ? `<details class="kn-more"><summary>${escapeHtml(s.contextAndSources)}</summary><p lang="en">${escapeHtml(k.context)}${k.source_ids?.length ? ` ${citeLinks(state, k.source_ids)}` : ''}</p>${primary ? `<p class="kn-page"><a href="${href(k.primary_page!, lang)}">${escapeHtml(PAGE_BY_ID.get(k.primary_page!)!.short_title)}</a></p>` : ''}</details>` : ''}
</figure>`;
}

const CITE_RE = /^\[@([A-Z0-9]+-\d+[a-z]?(?:;\s*@[A-Z0-9]+-\d+[a-z]?)*)\]/;
const TAG_RE =
  /^[ \t]*\{(?:(VN-direct|VN-adjacent|general)\\?\|(High|Medium|Low)|fx:(trend|projection|estimate|signal|wildcard|vision)|dx:(stated|revealed|tested|inferred))\}/;

function buildMarked(state: State): Marked {
  const { lang, editor = false } = state.opts;
  const s = t(lang);

  // A claim: a citation and the evidence tags that follow it, or tags on their own. They render
  // as one mark: superscript source numbers in the text and one evidence note.
  const claim: TokenizerAndRendererExtension = {
    name: 'claim',
    level: 'inline',
    start: (src) => {
      const i = src.search(/\[@|\{(VN-direct|VN-adjacent|general)\\?\||\{fx:|\{dx:/);
      return i < 0 ? undefined : i;
    },
    tokenizer(src) {
      let rest = src;
      let raw = '';
      let ids: string[] = [];
      const ev: Evidence = {};
      const c = CITE_RE.exec(rest);
      if (c) {
        raw = c[0];
        rest = rest.slice(raw.length);
        ids = c[1].split(/;\s*@/);
      }
      let tagged = false;
      for (;;) {
        const m = TAG_RE.exec(rest);
        if (!m) break;
        // Without a citation, the first tag must start right here (the start hook points at it).
        if (!c && !tagged && /^[ \t]/.test(rest)) break;
        // A second tag of a kind already seen belongs to the next claim.
        if ((m[1] && ev.label) || (m[3] && ev.fx) || (m[4] && ev.dx)) break;
        if (m[1]) {
          ev.label = m[1];
          ev.confidence = m[2];
        }
        if (m[3]) ev.fx = m[3];
        if (m[4]) ev.dx = m[4];
        raw += m[0];
        rest = rest.slice(m[0].length);
        tagged = true;
      }
      if (!c && !tagged) return;
      return { type: 'claim', raw, ids, ev };
    },
    renderer(token) {
      const ids = token.ids as string[];
      const ev = token.ev as Evidence;
      const cites = ids.length ? citeLinks(state, ids) : '';
      if (!ev.label && !ev.fx && !ev.dx) return cites;
      const nums = ids.map((id) => state.citations.indexOf(id) + 1);
      return cites + evidenceNote(ev, lang, { nums });
    },
  };
  const xref: TokenizerAndRendererExtension = {
    name: 'xref',
    level: 'inline',
    start: (src) => src.indexOf('[['),
    tokenizer(src) {
      const m = /^\[\[([a-z0-9-]+)(?:#([a-z0-9-]+))?\]\]/.exec(src);
      if (m) return { type: 'xref', raw: m[0], id: m[1], anchor: m[2] };
    },
    renderer(token) {
      const page = PAGE_BY_ID.get(token.id as string);
      if (!page) return `<span class="xref-missing">${escapeHtml(token.raw)}</span>`;
      if (!canReadPage(page.id, editor))
        return `<span class="xref is-locked" title="${escapeHtml(s.lockedLink)}">${escapeHtml(page.short_title)}</span>`;
      const attrs = page.lang === 'vi' && lang !== 'vi' ? ' hreflang="vi" lang="vi"' : '';
      return `<a class="xref" href="${href(page.id, lang, token.anchor as string | undefined)}"${attrs}>${escapeHtml(page.short_title)}</a>`;
    },
  };
  const inlineEmbed: TokenizerAndRendererExtension = {
    name: 'inlineEmbed',
    level: 'inline',
    start: (src) => src.indexOf('{{'),
    tokenizer(src) {
      const m = /^\{\{(kn|chart):([a-z0-9-]+)\}\}/.exec(src);
      if (m) return { type: 'inlineEmbed', raw: m[0], kind: m[1], id: m[2] };
    },
    renderer(token) {
      if (token.kind === 'kn') {
        const k = KEY_NUMBERS[token.id as string];
        return k ? `<strong class="kn-inline">${escapeHtml(k.value)}</strong>` : '';
      }
      return `<a href="#${escapeHtml(token.id as string)}">${escapeHtml(token.id as string)}</a>`;
    },
  };
  const embeds: TokenizerAndRendererExtension = {
    name: 'embeds',
    level: 'block',
    start: (src) => {
      const m = /(^|\n)[ \t]*\{\{(kn|chart):/.exec(src);
      return m ? m.index + m[1].length : undefined;
    },
    tokenizer(src) {
      const m = /^(?:[ \t]*(?:\{\{(?:kn|chart):[a-z0-9-]+\}\}[ \t]*)+(?:\n|$))+/.exec(src);
      if (!m) return;
      const items = [...m[0].matchAll(/\{\{(kn|chart):([a-z0-9-]+)\}\}/g)].map((x) => ({
        kind: x[1],
        id: x[2],
      }));
      return { type: 'embeds', raw: m[0], items };
    },
    renderer(token) {
      const out: string[] = [];
      let tiles: string[] = [];
      const flush = () => {
        if (tiles.length)
          out.push(
            `<div class="kn-grid wide" data-count="${tiles.length}">${tiles.join('')}</div>`,
          );
        tiles = [];
      };
      for (const item of token.items as { kind: string; id: string }[]) {
        if (item.kind === 'kn') tiles.push(keyNumberTile(state, item.id));
        else {
          flush();
          out.push(renderChartFigure(item.id, lang, (ids) => citeLinks(state, ids), { editor }));
          if (item.id === 'chart-scenarios-2050' && state.opts.pageId === ROLE.scenarios)
            out.push(renderScenarioExplorer(lang));
        }
      }
      flush();
      return out.join('\n');
    },
  };

  const marked = new Marked({ gfm: true });
  marked.use({ extensions: [embeds, claim, xref, inlineEmbed] });
  marked.use({
    renderer: {
      heading(this: any, token: Tokens.Heading) {
        const html = this.parser.parseInline(token.tokens);
        if (token.depth === 1 && state.heading === null) {
          state.heading = html;
          return '';
        }
        const text = stripTags(html);
        let id = slugify(text) || 'section';
        const seen = state.slugs.get(id) ?? 0;
        state.slugs.set(id, seen + 1);
        if (seen) id = `${id}-${seen}`;
        if (token.depth <= 3) state.toc.push({ id, text, depth: token.depth });
        const level = Math.min(Math.max(token.depth, 2), 6);
        // Section numbers ("1.1", "S4.2", "M5.16.1") are set apart so the titles scan.
        const numbered = html.replace(
          /^((?:[A-Z]\d+|\d+)(?:\.\d+)+)\s+/,
          '<span class="h-num">$1</span> ',
        );
        return `<h${level} id="${id}"><a class="anchor" href="#${id}" aria-hidden="true" tabindex="-1">#</a>${numbered}</h${level}>\n`;
      },
      blockquote(this: any, token: Tokens.Blockquote) {
        const inner: string = this.parser.parse(token.tokens);
        const m = /^<p><strong>([^<]+?)\.?<\/strong>\s*/.exec(inner.trim());
        if (!m) return `<blockquote>${inner}</blockquote>\n`;
        const labelText = m[1].replace(/\.$/, '');
        const kind = CALLOUT_KINDS.find(([re]) => re.test(labelText))?.[1] ?? 'note';
        const body = inner.trim().slice(m[0].length);
        const rest = body.startsWith('</p>') ? body.slice(4) : `<p>${body}`;
        return `<aside class="callout callout-${kind}" aria-label="${escapeHtml(labelText)}"><p class="callout-label">${escapeHtml(labelText)}</p>${rest}</aside>\n`;
      },
      table(this: any, token: Tokens.Table) {
        const cell = (c: Tokens.TableCell, tag: 'th' | 'td', i: number) => {
          const align = token.align[i] ? ` style="text-align:${token.align[i]}"` : '';
          return `<${tag}${tag === 'th' ? ' scope="col"' : ''}${align}>${this.parser.parseInline(c.tokens)}</${tag}>`;
        };
        const head = `<tr>${token.header.map((c, i) => cell(c, 'th', i)).join('')}</tr>`;
        const body = token.rows
          .map((row) => `<tr>${row.map((c, i) => cell(c, 'td', i)).join('')}</tr>`)
          .join('\n');
        const cols = token.header.length;
        return `<div class="table-wrap wide" data-cols="${cols}" tabindex="0" role="region" aria-label="${lang === 'vi' ? 'Bảng' : 'Table'}: ${escapeHtml(stripTags(this.parser.parseInline(token.header[0].tokens)))}"><table><thead>${head}</thead><tbody>${body}</tbody></table></div>\n`;
      },
      html(token: Tokens.HTML | Tokens.Tag) {
        const raw = token.raw;
        const anchor = /^<a id="([A-Za-z0-9_-]+)"><\/a>/.exec(raw.trim());
        if (anchor)
          return `<a id="${anchor[1]}" class="src-anchor"></a>${raw.trim().length > anchor[0].length ? escapeHtml(raw.trim().slice(anchor[0].length)) : ''}`;
        if (/^<a id="[A-Za-z0-9_-]+">$/.test(raw)) return raw.replace('>', ' class="src-anchor">');
        if (raw === '</a>') return raw;
        if (/^<br\s*\/?>$/i.test(raw)) return '<br>';
        return escapeHtml(raw);
      },
      link(this: any, token: Tokens.Link) {
        const text = this.parser.parseInline(token.tokens);
        const url = token.href;
        if (/^javascript:/i.test(url)) return text;
        const external = /^https?:\/\//.test(url);
        const target = external ? url : url.startsWith('/') ? localize(url, lang) : url;
        return `<a href="${escapeHtml(target)}"${token.title ? ` title="${escapeHtml(token.title)}"` : ''}${external ? ' rel="noopener" class="ext"' : ''}>${text}</a>`;
      },
    },
  });
  return marked;
}

/** Wrap the opening answer ("In brief" in chapters, "The short version" in briefs) in its box. */
function answerBox(html: string, lang: Lang): string {
  const m = /<p><strong>([^<]+?)\.<\/strong>\s*([\s\S]*?)<\/p>\n(<ul>[\s\S]*?<\/ul>\n)?/.exec(html);
  if (!m || !ANSWER_LABELS.test(m[1]) || m.index > 2000) return html;
  const [all, labelText, rest, list = ''] = m;
  const body = `${rest.trim() ? `<p>${rest}</p>` : ''}${list}`;
  const box = `<section class="answer" aria-label="${escapeHtml(labelText)}"><p class="answer-label">${escapeHtml(labelText || t(lang).answer)}</p>${body}</section>\n`;
  return html.slice(0, m.index) + box + html.slice(m.index + all.length);
}

/** Render a page body (Markdown with report tokens) to HTML. */
export function renderMarkdown(markdown: string, opts: RenderOptions): RenderResult {
  const state: State = { opts, citations: [], toc: [], slugs: new Map(), heading: null };
  let html = buildMarked(state).parse(markdown, { async: false }) as string;
  html = answerBox(html, opts.lang)
    // Superscripts and notes attach to the word before them.
    .replace(/[ \t]+(<sup class="cite">)/g, '$1')
    .replace(/[ \t]+(<span class="evn")/g, '$1');
  return { html, heading: state.heading, toc: state.toc, citations: state.citations };
}

/** Render an inline Markdown fragment (summaries, table cells in widgets). */
export function renderInline(markdown: string, opts: RenderOptions): string {
  const state: State = { opts, citations: [], toc: [], slugs: new Map(), heading: '' };
  return buildMarked(state).parseInline(markdown, { async: false }) as string;
}

/** A stat tile on its own (the home page), numbered against a page's citations. */
export function renderKeyNumber(
  id: string,
  opts: RenderOptions,
  size: 'normal' | 'hero' = 'normal',
): string {
  const state: State = { opts, citations: [], toc: [], slugs: new Map(), heading: '' };
  return keyNumberTile(state, id, size);
}

export { meter };

/** Plain text for search snippets and meta descriptions. */
export function plainText(markdown: string): string {
  return markdown
    .replace(/\[@[^\]]+\]/g, '')
    .replace(/\{(VN-direct|VN-adjacent|general)\\?\|(High|Medium|Low)\}/g, '')
    .replace(/\{fx:[a-z]+\}/g, '')
    .replace(/\{dx:[a-z]+\}/g, '')
    .replace(/\{\{(kn|chart):[a-z0-9-]+\}\}/g, '')
    .replace(
      /\[\[([a-z0-9-]+)(#[a-z0-9-]+)?\]\]/g,
      (_, id) => PAGE_BY_ID.get(id)?.short_title ?? id,
    )
    .replace(/<[^>]+>/g, '')
    .replace(/[*_`#>|]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}
