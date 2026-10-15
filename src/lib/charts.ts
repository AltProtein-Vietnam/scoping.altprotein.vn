import chartsJson from '../generated/charts.json';
import { t, type Lang } from './i18n';
import { evidenceBadge, escapeHtml } from './html';
import { renderPlaysTool } from './widgets';

export interface ChartOutput {
  id: string;
  type: string;
  title: string;
  subtitle?: string;
  svg: string;
  table: string;
  notes?: string;
  alt: string;
  source_ids: string[];
  evidence?: string;
  confidence?: string;
  interactive?: boolean;
}

export const CHARTS = chartsJson as unknown as Record<string, ChartOutput>;

/**
 * Some notes in chart-specs.json are instructions to the site builder rather than notes for readers.
 * These are shown instead (null hides the note); the specs themselves are unchanged.
 */
const READER_NOTES: Record<string, string | null> = {
  'chart-feedstock-map':
    'Shown as a province-by-stream matrix. Tay Ninh (cassava starch) and the Mekong Delta (aquaculture by-products) are highlighted.',
  'chart-timeline': null,
  'chart-route-to-market':
    'Green: self-declaration or listed feed. Amber: self-declaration with legal risk, or aquafeed trial ambiguity. Red: GMO closed-production, cultivated or new microbial biomass.',
  'chart-plays-scoring':
    'Scores are judgements, not ratings. The feed plays retired in version 0.8 (T2, T3 and T6) are not shown. The candidate plays added in version 0.10 (T11 and T12) are listed in section 26.8 but not ranked.',
  'chart-sbm-scenarios-2050':
    'The vision band shown in earlier versions is dropped: soybean-meal need is no longer a vision goal.',
  'chart-sbm-tornado': 'Bars run from the low-case to the high-case value.',
  'chart-play-robustness': null,
};
export const readerNote = (c: ChartOutput) => (c.id in READER_NOTES ? READER_NOTES[c.id] : c.notes);

const PLAYS_FALLBACK: ChartOutput = {
  id: 'chart-plays-scoring',
  type: 'interactive-bar',
  title: 'Seven plays, scored with weights you can change',
  svg: '',
  table: '',
  alt: '',
  source_ids: [],
};

export interface FigureOptions {
  editor?: boolean;
  /** Leave out the interactive plays tool and show the static ranking (the home page). */
  staticOnly?: boolean;
  /** Leave out the notes line (compact figures on the home page). */
  compact?: boolean;
}

export function renderChartFigure(
  id: string,
  lang: Lang,
  cite: (ids: string[]) => string,
  opts: FigureOptions = {},
): string {
  const s = t(lang);
  const c = CHARTS[id] ?? (id === 'chart-plays-scoring' ? PLAYS_FALLBACK : undefined);
  const e = escapeHtml;
  if (!c)
    return `<figure class="chart chart-missing wide" id="${e(id)}"><p>${e(s.chartUnavailable)}</p></figure>`;
  const interactive = id === 'chart-plays-scoring' && !opts.staticOnly;
  const body = interactive
    ? renderPlaysTool(lang, c.svg, Boolean(opts.editor))
    : `<div class="chart-body">${c.svg}</div>`;
  const note = !opts.compact && readerNote(c);
  const srcLabel =
    c.source_ids.length > 1 ? s.sources : c.source_ids.length ? s.source : s.evidence;
  return `<figure class="chart chart-${e(c.type)} wide" id="${e(id)}" aria-labelledby="${e(id)}-cap">
<div class="chart-head"><p class="chart-title" id="${e(id)}-cap" lang="en">${e(c.title)}</p>${c.subtitle ? `<p class="chart-sub" lang="en">${e(c.subtitle)}</p>` : ''}</div>
${body}
<figcaption class="chart-foot">${note ? `<p class="chart-notes" lang="en">${e(note)}</p>` : ''}<p class="chart-src"><span class="chart-src-label">${e(srcLabel)}</span>${c.source_ids.length ? ` ${cite(c.source_ids)}` : ''}${c.evidence && c.confidence ? ` ${evidenceBadge(c.evidence, c.confidence, lang)}` : ''}</p>
${c.table ? `<details class="chart-data"><summary><span class="show">${e(s.showData)}</span><span class="hide">${e(s.hideData)}</span></summary><div class="table-wrap" tabindex="0" role="region" aria-label="${e(c.title)}">${c.table}</div></details>` : ''}
</figcaption>
</figure>`;
}
