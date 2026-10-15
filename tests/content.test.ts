import assert from 'node:assert/strict';
import fs from 'node:fs';
import { test } from 'node:test';
import { renderMarkdown } from '../src/lib/markdown';
import {
  APPENDIX_GROUPS,
  PAGES,
  PAGE_BY_ID,
  ROLE,
  appendixCode,
  pageIdForPath,
  pagePath,
  localize,
  READING_ORDER,
} from '../src/lib/site';
import { MOVED_PAGES, WITHDRAWN_PATHS } from '../src/lib/redirects';
import { PLAY_ROWS, PRESETS, weightedScore } from '../src/lib/widgets';
import { cleanSnippet, searchRecords } from '../src/lib/search';
import { isEditorUser, isRestrictedPage } from '../src/lib/access';
import { coverPartAnswers, parseArgument } from '../src/lib/front';
import { STRINGS } from '../src/lib/i18n';

const seed = JSON.parse(fs.readFileSync('seed/seed.json', 'utf8'));
const entries: { id: string; data: { body: string } }[] = seed.content.pages;
const strip = (html: string) =>
  html.replace(/<code>[\s\S]*?<\/code>/g, '').replace(/<[^>]+>/g, ' ');

test('the seed holds every manifest page once, with its Markdown body', () => {
  assert.equal(entries.length, PAGES.length);
  assert.equal(entries.length, 80);
  assert.deepEqual(new Set(entries.map((e) => e.id)), new Set(PAGES.map((p) => p.id)));
  for (const e of entries) {
    const file = fs.readFileSync(
      `report/${JSON.parse(fs.readFileSync('report/site-manifest.json', 'utf8')).pages.find((p: { id: string }) => p.id === e.id).path}`,
      'utf8',
    );
    assert.ok(file.endsWith(e.data.body), `${e.id} body differs from the package`);
  }
});

test('every page renders with no unrendered report tokens', () => {
  for (const e of entries) {
    const r = renderMarkdown(e.data.body, {
      lang: 'en',
      pageId: e.id,
      contentLang: PAGE_BY_ID.get(e.id)!.lang,
    });
    const leftovers = strip(r.html).match(
      /\[@[A-Z]|\{(VN-direct|VN-adjacent|general)|\{fx:|\[\[[a-z]|\{\{(kn|chart):/g,
    );
    assert.equal(leftovers, null, `${e.id}: ${leftovers?.join(' ')}`);
    assert.ok(
      !/<script/i.test(
        r.html.replace(
          /<script type="application\/json" class="plays-data">[\s\S]*?<\/script>/,
          '',
        ),
      ),
      `${e.id} contains a script tag`,
    );
  }
});

// Tiles and charts carry their own (inline) evidence marks; leave them out when counting claims.
const withoutFigures = (html: string) =>
  html
    .replace(/<figure class="kn[\s\S]*?<\/figure>/g, '')
    .replace(/<figure class="chart[\s\S]*?<\/figure>/g, '');

test('every evidence tag becomes one evidence note, with foresight and demand tags kept', () => {
  for (const e of entries) {
    const body = e.data.body.replace(/`[^`]*`/g, '');
    const tags =
      body.match(/\{(VN-direct|VN-adjacent|general)\\?\|(High|Medium|Low)\}/g)?.length ?? 0;
    const fx =
      body.match(/\{fx:(trend|projection|estimate|signal|wildcard|vision)\}/g)?.length ?? 0;
    const dx = body.match(/\{dx:(stated|revealed|tested|inferred)\}/g)?.length ?? 0;
    const html = withoutFigures(renderMarkdown(e.data.body, { lang: 'en', pageId: e.id }).html);
    assert.equal(html.match(/data-kinds="ev[ "]/g)?.length ?? 0, tags, `${e.id}: evidence notes`);
    assert.ok((html.match(/class="evn-tag" data-fx=/g)?.length ?? 0) >= fx, `${e.id}: foresight`);
    assert.equal(html.match(/class="evn-tag" data-dx=/g)?.length ?? 0, dx, `${e.id}: demand`);
  }
});

test('vision tags appear only on the vision chapter', () => {
  for (const e of entries) {
    const html = withoutFigures(renderMarkdown(e.data.body, { lang: 'en', pageId: e.id }).html);
    if (e.id !== ROLE.vision) assert.ok(!html.includes('data-fx="vision"'), e.id);
  }
});

test('a citation and the tags after it form one claim: numbers in the text, one note', () => {
  const html = renderMarkdown(
    'Meat intake rose [@DIE-01; @DIE-02] {VN-direct|Medium} {dx:revealed}.',
    {
      lang: 'en',
    },
  ).html;
  assert.match(html, /rose<sup class="cite"><a href="#src-DIE-01"[^>]*>1<\/a>/);
  assert.equal(html.match(/class="evn"/g)?.length, 1);
  assert.match(html, /data-kinds="ev dx-revealed"/);
  assert.match(html, /<span class="evn-nums">1, 2<\/span>/);
  assert.match(html, /evidence about Vietnam \(VN-direct\)/);
});

test('citations are numbered in order and resolve to sources', () => {
  const e = entries.find((x) => x.id === 'ch01-why-vietnam')!;
  const r = renderMarkdown(e.data.body, { lang: 'en', pageId: e.id });
  assert.ok(r.citations.length > 10);
  const numbers = [...r.html.matchAll(/data-src="[^"]+"[^>]*>(\d+)<\/a>/g)].map((m) =>
    Number(m[1]),
  );
  let max = 0;
  for (const n of numbers) {
    assert.ok(n <= max + 1, 'citation numbers appear in order of first use');
    max = Math.max(max, n);
  }
  assert.equal(max, r.citations.length);
});

test('callouts are classified, with corrections styled consistently', () => {
  const all = entries
    .map((e) => renderMarkdown(e.data.body, { lang: 'en', pageId: e.id }).html)
    .join('\n');
  const corrections = entries
    .map((e) => e.data.body.match(/^> \*\*Correction[^*]*\*\*/gm)?.length ?? 0)
    .reduce((a, b) => a + b, 0);
  assert.ok(corrections > 0);
  assert.equal(all.match(/callout-correction/g)?.length, corrections);
  assert.ok(all.includes('callout-draft'));
  assert.ok(all.includes('callout-vision'));
  assert.ok(all.includes('callout-speculative'));
  assert.ok(!all.includes('<blockquote><p><strong>'));
});

test('tables keep escaped tag pipes inside cells', () => {
  const e = entries.find((x) => x.id === ROLE.plays)!;
  const html = renderMarkdown(e.data.body, { lang: 'en', pageId: e.id }).html;
  assert.match(
    html,
    /<td>Source: AltProtein Vietnam scoring|<p>Source: AltProtein Vietnam scoring/,
  );
  const rows = html.match(/<tr>[\s\S]*?<\/tr>/g)!;
  for (const row of rows) assert.ok(!row.includes('\\|'));
});

test('raw HTML is escaped except source anchors and line breaks', () => {
  const html = renderMarkdown(
    '<a id="MAC-04"></a> text <img src=x onerror=alert(1)> <br>\n\n<script>alert(1)</script>',
    { lang: 'en' },
  ).html;
  assert.ok(html.includes('id="MAC-04"'));
  assert.ok(!html.includes('<img'));
  assert.ok(!html.includes('<script'));
  assert.ok(html.includes('&lt;script&gt;'));
});

test('links reject javascript URLs', () => {
  const html = renderMarkdown('[x](javascript:alert(1))', { lang: 'en' }).html;
  assert.ok(!html.includes('javascript:'));
});

test('page paths round-trip, and the Vietnamese interface prefixes them', () => {
  for (const p of PAGES) assert.equal(pageIdForPath(pagePath(p.id)), p.id);
  assert.equal(pagePath('front-cover'), '/');
  assert.equal(pagePath('ch26-plays'), '/report/ch26-plays');
  assert.equal(pagePath('app-m1-method'), '/appendices/app-m1-method');
  // The Vietnamese pages are held back until the v1.0 translation pass; their addresses redirect.
  for (const [path, id] of Object.entries(WITHDRAWN_PATHS)) {
    assert.equal(pageIdForPath(path), undefined);
    assert.ok(PAGE_BY_ID.has(id), `${path} leads to a missing page`);
  }
  assert.ok(!PAGES.some((p) => p.lang === 'vi'));
  assert.equal(localize('/', 'vi'), '/vi');
  assert.equal(localize('/report/ch26-plays', 'vi'), '/vi/report/ch26-plays');
  assert.equal(localize('/files/data/companies.csv', 'vi'), '/files/data/companies.csv');
  assert.equal(localize('/downloads/x.zip', 'vi'), '/downloads/x.zip');
  assert.equal(READING_ORDER.length, PAGES.length);
});

test('balanced play scores match the table in chapter 11', () => {
  const balanced = PRESETS.find((p) => p.preset_id === 'balanced')!;
  const expected: Record<string, number> = {
    T1: 3.8,
    T2: 3.45,
    T3: 2.65,
    T4: 3.9,
    T5: 3.45,
    T6: 3.3,
    T7: 2.1,
    T8: 1.55,
    T9: 3.0,
    T10: 3.05,
  };
  for (const p of PLAY_ROWS)
    assert.equal(weightedScore(p, balanced).toFixed(2), expected[p.play_id].toFixed(2), p.play_id);
});

test('top three plays per preset match chapter 11', () => {
  const top = (id: string) => {
    const preset = PRESETS.find((p) => p.preset_id === id)!;
    return PLAY_ROWS.map((p) => [p.play_id, weightedScore(p, preset)] as const)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 2)
      .map(([k, v]) => `${k} ${v.toFixed(2)}`);
  };
  assert.deepEqual(top('investors'), ['T1 3.80', 'T4 3.50']);
  assert.deepEqual(top('startups'), ['T1 4.15', 'T4 3.85']);
  assert.deepEqual(top('research'), ['T4 4.15', 'T5 4.00']);
});

test('plays and public goods retired in v0.8 are not ranked or scored', async () => {
  const { CHARTS } = await import('../src/lib/charts');
  const { renderScenarioExplorer } = await import('../src/lib/widgets');
  assert.deepEqual(
    PLAY_ROWS.map((p) => p.play_id),
    ['T1', 'T4', 'T5', 'T7', 'T8', 'T9', 'T10'],
  );
  const heatmap = CHARTS['chart-play-robustness'].svg;
  const explorer = renderScenarioExplorer('en');
  assert.ok(heatmap.includes('>T1 ') && explorer.includes('<span class="rb-id">T1</span>'));
  for (const id of ['T2', 'T3', 'T6', 'P2', 'P3']) {
    assert.ok(!heatmap.includes(`>${id} `), `heatmap shows ${id}`);
    assert.ok(!explorer.includes(`<span class="rb-id">${id}</span>`), `explorer shows ${id}`);
  }
});

test('search finds glossary terms in either language; data rows only for editors', () => {
  assert.ok(searchRecords('protein thay the').some((r) => r.id === 'GL-001'));
  assert.ok(searchRecords('Emmay', 60, true).some((r) => r.kind === 'company'));
  assert.ok(!searchRecords('Emmay').some((r) => r.kind === 'company'));
  assert.ok(searchRecords('cassava').every((r) => r.access === 'public'));
  assert.equal(
    cleanSnippet('a [@MAC-04] b {VN-direct|High} c [[ch26-plays]] d {dx:revealed}'),
    'a b c Plays d',
  );
});

test('interface strings use no em or en dashes', () => {
  const text = JSON.stringify(STRINGS, (_k, v) => (typeof v === 'function' ? v(1, 'x') : v));
  assert.ok(!/[–—]/.test(text));
});

test('every chart spec is rendered, themed only through CSS variables', async () => {
  const { CHARTS } = await import('../src/lib/charts');
  const specs = JSON.parse(fs.readFileSync('report/charts/chart-specs.json', 'utf8')).charts as {
    id: string;
  }[];
  assert.equal(Object.keys(CHARTS).length, specs.length);
  for (const spec of specs) {
    const c = CHARTS[spec.id];
    assert.ok(c?.svg, spec.id);
    assert.ok(
      !/#[0-9a-f]{3,6}\b|rgb\(/i.test(c.svg.replace(/href="#[^"]*"/g, '')),
      `${spec.id} hardcodes a colour`,
    );
    assert.ok(!/[–—]/.test(c.svg + c.table), `${spec.id} has a dash`);
  }
});

test('every page the interface refers to by role exists', () => {
  for (const [role, id] of Object.entries(ROLE)) assert.ok(PAGE_BY_ID.has(id), `${role}: ${id}`);
  const manifest = JSON.parse(fs.readFileSync('report/site-manifest.json', 'utf8'));
  assert.equal(ROLE.vision, manifest.tokens.foresight_tag.vision_only_on);
});

test('pages moved in v0.6 redirect to pages that exist, and no old id is reused', () => {
  for (const [from, to] of Object.entries(MOVED_PAGES)) {
    assert.ok(PAGE_BY_ID.has(to), `${from} -> ${to}`);
    assert.ok(!PAGE_BY_ID.has(from), `${from} is a current page id`);
  }
});

test('appendix codes and groups follow the manifest', () => {
  assert.deepEqual(
    APPENDIX_GROUPS.map((g) => g.id),
    ['m', 's', 'd', 'f', 'r'],
  );
  assert.equal(appendixCode('app-s13-science'), 'S13');
  assert.equal(
    APPENDIX_GROUPS.flatMap((g) => g.pages).length,
    PAGES.filter((p) => p.section === 'appendix').length,
  );
});

test('demand evidence tags without a citation still make a note', () => {
  const html = renderMarkdown('Buyers pay more {VN-direct|High} {dx:revealed}.', {
    lang: 'en',
  }).html;
  assert.match(html, /class="evn-tag" data-dx="revealed"/);
  assert.match(html, /data-kinds="ev dx-revealed"/);
  assert.ok(!html.includes('<sup class="cite">'));
});

test('appendices M, S, D, F and registers R1, R2 are for editors; glossary and sources are public', () => {
  for (const p of PAGES) {
    const code = appendixCode(p.id) ?? '';
    const expected = p.section === 'appendix' && !['R3', 'R4'].includes(code);
    assert.equal(isRestrictedPage(p.id), expected, p.id);
  }
  assert.ok(!isRestrictedPage(ROLE.sources) && !isRestrictedPage(ROLE.glossary));
  assert.ok(isRestrictedPage(ROLE.openQuestions) && isRestrictedPage(ROLE.disagreements));
  assert.ok(isEditorUser({ role: 40 }) && isEditorUser({ role: 50 }));
  assert.ok(!isEditorUser({ role: 30 }) && !isEditorUser(undefined));
});

test('links to restricted pages are plain text for the public and links for editors', () => {
  const md = 'See [[app-s4-feedstocks]] and [[ch07-rules]] and [[app-r4-sources]].';
  const pub = renderMarkdown(md, { lang: 'en' }).html;
  assert.match(pub, /<span class="xref is-locked"[^>]*>Feedstock data sheets<\/span>/);
  assert.ok(!pub.includes('href="/appendices/app-s4-feedstocks"'));
  assert.ok(pub.includes('href="/report/ch07-rules"'));
  assert.ok(pub.includes('href="/appendices/app-r4-sources"'));
  const ed = renderMarkdown(md, { lang: 'en', editor: true }).html;
  assert.ok(ed.includes('href="/appendices/app-s4-feedstocks"'));
  // No public page links a restricted page.
  for (const e of entries.filter((x) => !isRestrictedPage(x.id))) {
    const html = renderMarkdown(e.data.body, { lang: 'en', pageId: e.id }).html;
    for (const m of html.matchAll(/href="\/appendices\/([a-z0-9-]+)/g))
      assert.ok(!isRestrictedPage(m[1]), `${e.id} links ${m[1]}`);
  }
});

test('the home page reads its argument from the two-minute summary and parts from the cover', () => {
  const body = (id: string) => entries.find((x) => x.id === id)!.data.body;
  const arg = parseArgument(body(ROLE.twoMinute));
  assert.ok(arg.lede?.lead.startsWith('Protein for people first'));
  assert.ok(arg.steps.length >= 5);
  assert.equal(arg.steps[0].lead, 'Why Vietnam');
  assert.ok(arg.steps.every((st) => st.pages.length > 0));
  assert.ok(arg.steps.some((st) => st.kn.length > 0));
  assert.ok(!arg.steps.some((st) => /Read next/.test(st.lead)));
  const parts = coverPartAnswers(body(ROLE.cover));
  assert.deepEqual(Object.keys(parts), ['I', 'II', 'III', 'IV', 'V']);
});

test('editor-only files are routed through the Worker and never shipped from public/', () => {
  const config = fs.readFileSync('wrangler.jsonc', 'utf8');
  // Top level and env.production both send /files/* to the Worker before the asset server.
  assert.equal(config.match(/"run_worker_first": \["\/files\/\*"\]/g)?.length, 2);
  const build = fs.readFileSync('scripts/build.mjs', 'utf8');
  assert.match(build, /--files-out/);
  assert.match(build, /dist\/client/);
  assert.ok(!fs.existsSync('public/data') && !fs.existsSync('public/downloads'));
});
