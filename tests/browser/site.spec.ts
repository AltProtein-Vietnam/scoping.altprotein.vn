import { test, expect, type Page } from '@playwright/test';
import seed from '../../seed/seed.json' with { type: 'json' };
import site from '../../src/generated/site.json' with { type: 'json' };

test.beforeAll(async ({ request }) => {
  const response = await request.post('/_emdash/api/setup/dev-bypass');
  expect(response.ok()).toBeTruthy();
});

const FRONT: Record<string, string> = {
  'front-cover': '/',
  'front-exec-summary': '/summary',
  'front-two-minute': '/two-minutes',
  'front-at-a-glance': '/at-a-glance',
  'front-prologue': '/prologue',
  'front-how-to-read': '/how-to-read',
  'front-faq': '/faq',
};
const SECTION: Record<string, string> = {
  report: '/report',
  brief: '/briefs',
  appendix: '/appendices',
};
const pathOf = (id: string) => {
  const page = site.pages.find((p) => p.id === id)!;
  return FRONT[id] ?? `${SECTION[page.section]}/${id}`;
};
// Appendices other than the glossary (R3) and the source list (R4) are for editors.
const restricted = (id: string) =>
  id.startsWith('app-') && id !== 'app-r3-glossary' && id !== 'app-r4-sources';

// The dev sign-in answers with a page that redirects in the browser; a navigation right after it
// can race that redirect. Signing in through the context's request API sets the session cookie
// without navigating.
async function signIn(page: Page) {
  const response = await page.request.get('/_emdash/api/auth/dev-bypass?redirect=/');
  expect(response.ok()).toBeTruthy();
  expect((await page.request.get('/workbench')).status()).toBe(200);
}

async function brokenAnchors(page: Page) {
  return page
    .locator('main a[href^="#"]')
    .evaluateAll((links) =>
      links
        .map((a) => decodeURIComponent(a.getAttribute('href')!.slice(1)))
        .filter((id) => id && !document.getElementById(id)),
    );
}

test('every public page loads with working anchors; restricted pages need sign-in', async ({
  page,
}) => {
  test.setTimeout(300000);
  for (const entry of seed.content.pages) {
    const response = await page.goto(pathOf(entry.id));
    if (restricted(entry.id)) {
      expect(response?.status(), entry.id).toBe(403);
      await expect(page.locator('h1')).toContainText('This page is for reviewers');
      continue;
    }
    expect(response?.status(), entry.id).toBe(200);
    await expect(page.locator('h1').first()).toBeVisible();
    expect(await brokenAnchors(page), entry.id).toEqual([]);
    // No link on a public page leads to a page only editors can read.
    const links = await page
      .locator('main a[href^="/appendices/"]')
      .evaluateAll((as) => as.map((a) => a.getAttribute('href')!.split(/[#?]/)[0]));
    for (const href of links) expect(restricted(href.split('/').pop()!), href).toBe(false);
  }
});

test('editors can read every page, including the appendices', async ({ page }) => {
  test.setTimeout(240000);
  await signIn(page);
  for (const entry of seed.content.pages.filter((e) => restricted(e.id))) {
    const response = await page.goto(pathOf(entry.id));
    expect(response?.status(), entry.id).toBe(200);
    await expect(page.locator('.editor-bar')).toBeVisible();
    expect(await brokenAnchors(page), entry.id).toEqual([]);
  }
});

test('routes, redirects, the Vietnamese interface and the draft notice', async ({ request }) => {
  const sitemap = await request.get('/sitemap.xml');
  expect(sitemap.status()).toBe(200);
  const xml = await sitemap.text();
  expect(xml).toContain('/report/ch26-plays');
  expect(xml).toContain('/report/part-iii');
  expect(xml).toContain('/appendices/app-r4-sources');
  expect(xml).not.toContain('app-s4-feedstocks');
  expect(xml).not.toContain('/data');
  expect((await request.get('/sitemap-pages.xml')).status()).toBe(404);
  expect((await request.get('/report/no-such-page')).status()).toBe(404);
  const old = await request.get('/chapters/1-anything', { maxRedirects: 0 });
  expect(old.status()).toBe(301);
  expect(old.headers()['location']).toBe('/report');
  const p = await request.get('/pages/ch26-plays', { maxRedirects: 0 });
  expect(p.headers()['location']).toBe('/report/ch26-plays');
  // Pages that moved when the report was regrouped in v0.6.
  const movedChapter = await request.get('/report/ch11-plays', { maxRedirects: 0 });
  expect(movedChapter.status()).toBe(301);
  expect(movedChapter.headers()['location']).toBe('/report/ch26-plays');
  const movedAppendix = await request.get('/vi/appendices/app-t-sources', { maxRedirects: 0 });
  expect(movedAppendix.headers()['location']).toBe('/vi/appendices/app-r4-sources');
  // The Vietnamese summary and prologue are held back until the v1.0 translation pass.
  const summaryVi = await request.get('/tom-tat', { maxRedirects: 0 });
  expect(summaryVi.status()).toBe(302);
  expect(summaryVi.headers()['location']).toBe('/summary');
  const prologueVi = await request.get('/vi/loi-mo-dau', { maxRedirects: 0 });
  expect(prologueVi.headers()['location']).toBe('/vi/prologue');
  expect((await request.get('/report/ch26-plays?_preview=invalid')).status()).toBe(403);
  const vi = await request.get('/vi/report/ch26-plays');
  expect(vi.status()).toBe(200);
  const html = await vi.text();
  expect(html).toContain('<html lang="vi"');
  expect(html).toContain(site.draft_notice.vi);
  expect(html).toContain('href="/vi/report/ch27-policy-options"');
  const home = await (await request.get('/')).text();
  expect(home).toContain('This report is a draft and subject to change.');
  // The manifest's draft notice appears in the banner and the footer.
  expect(home.split(site.draft_notice.en).length - 1).toBeGreaterThanOrEqual(2);
  expect(home).not.toContain('Suggested citation');
  for (const path of [
    '/report',
    '/report/part-i',
    '/report/part-v',
    '/briefs',
    '/appendices',
    '/glossary',
    '/about',
    '/search?q=cassava',
    '/vi',
    '/vi/report/part-ii',
  ])
    expect((await request.get(path)).status(), path).toBe(200);
});

test('data, files and the EmDash search API are closed to the public', async ({ playwright }) => {
  const anon = await playwright.request.newContext({ baseURL: 'http://127.0.0.1:4321' });
  for (const path of [
    '/data',
    '/data/companies',
    '/workbench',
    '/files/data/companies.csv',
    '/files/data/charts/technology_fit.csv',
    '/files/downloads/altprotein-vn-data.zip',
    '/files/downloads/altprotein-vn-working-papers.zip',
    '/files/downloads/altprotein-vn-report-markdown.zip',
    '/_emdash/api/search?q=cassava',
    '/_emdash/api/search/suggest?q=cas',
  ])
    expect((await anon.get(path)).status(), path).toBe(403);
  // Addresses of the files before v0.10 lead to the gated ones.
  const zip = await anon.get('/downloads/altprotein-vn-data.zip', { maxRedirects: 0 });
  expect(zip.status()).toBe(301);
  expect(zip.headers()['location']).toBe('/files/downloads/altprotein-vn-data.zip');
  const csv = await anon.get('/data/companies.csv', { maxRedirects: 0 });
  expect(csv.headers()['location']).toBe('/files/data/companies.csv');
  // Search shows the public pages and the glossary only.
  const search = await (await anon.get('/search?q=Vedan')).text();
  expect(search).not.toContain('/data/companies?q=');
  const pages = await (await anon.get('/search?q=feedstock')).text();
  expect(pages).not.toContain('href="/appendices/app-s4-feedstocks"');
  await anon.dispose();
});

test('editors get the data browser, files and search across the data', async ({ page }) => {
  await signIn(page);
  await page.goto('/workbench');
  await expect(page.locator('h1')).toHaveText('Workbench');
  const file = await page.request.get('/files/data/companies.csv');
  expect(file.status()).toBe(200);
  expect(file.headers()['content-type']).toContain('text/csv');
  expect(file.headers()['cache-control']).toContain('no-store');
  expect((await page.request.get('/files/downloads/altprotein-vn-data.zip')).status()).toBe(200);
  expect((await page.request.get('/_emdash/api/search?q=cassava')).status()).toBe(200);
  await page.goto('/data/companies');
  await expect(page.locator('.dt-count')).toContainText('98');
  await page.getByLabel('Filter rows').fill('Vedan');
  await expect(page.locator('.dt-wrap tbody tr').first()).toContainText('Vedan');
  await page.goto('/search?q=Vedan');
  await expect(page.locator('.results a[href*="/data/companies"]').first()).toBeVisible();
});

test('an editor can switch to the public view and back', async ({ page }) => {
  await signIn(page);
  await page.goto('/appendices/app-s4-feedstocks');
  await expect(page.locator('.editor-bar')).toContainText('Editor view');
  await page.getByRole('link', { name: 'See the public view' }).click();
  await expect(page.locator('h1')).toContainText('This page is for reviewers');
  await expect(page.locator('.editor-bar')).toContainText('Public view');
  await page.getByRole('link', { name: 'Back to the editor view' }).click();
  await expect(page.locator('h1')).toContainText('Feedstock data sheets');
});

test('the home page lays out the argument with numbers, charts and links', async ({ page }) => {
  await page.goto('/');
  const steps = page.locator('.steps > .step');
  expect(await steps.count()).toBeGreaterThanOrEqual(5);
  await expect(steps.first().locator('h3')).toHaveText('Why Vietnam');
  await expect(steps.first().locator('.kn-hero')).toBeVisible();
  await expect(steps.first().locator('.chart')).toBeVisible();
  await expect(steps.first().locator('.step-links a').first()).toHaveAttribute(
    'href',
    '/report/ch01-why-vietnam',
  );
  await expect(page.locator('.part-card')).toHaveCount(5);
  await expect(page.locator('.brief-card')).toHaveCount(6);
});

test('a citation opens its sources, and evidence notes sit beside the text', async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto('/report/ch01-why-vietnam');
  const note = page.locator('.prose > p .evn').first();
  await expect(note).toBeVisible();
  const text = await page.locator('.prose > p').first().boundingBox();
  const box = await note.boundingBox();
  expect(box!.x).toBeGreaterThan(text!.x + text!.width);
  await page.locator('.prose > p sup.cite a').first().click();
  await expect(page.locator('#pop')).toBeVisible();
  await expect(page.locator('#pop li').first()).toContainText('DIE-01');
  await page.keyboard.press('Escape');
  await expect(page.locator('#pop')).toBeHidden();
});

test('plays can be re-ranked and opened', async ({ page }) => {
  await page.goto('/report/ch26-plays');
  const bars = page.locator('.plays-bars li');
  // v0.8 retired the feed plays (T2, T3 and T6); the v0.10 candidates are not ranked.
  await expect(bars).toHaveCount(7);
  await expect(page.locator('#play-T2')).toHaveCount(0);
  await expect(page.locator('#play-T11')).toHaveCount(0);
  await expect(bars.first()).toContainText('T4');
  await page.locator('select[name="preset"]').selectOption('startups');
  await expect(bars.first()).toContainText('T1');
  await expect(bars.first()).toContainText('4.15');
  await page.locator('input[name="public_value"]').fill('50');
  await expect(page.locator('select[name="preset"]')).toHaveValue('custom');
  await bars.first().locator('button').click();
  await expect(page.locator('.play-card[open]')).toHaveCount(1);
  await expect(page.locator('.play-card[open]')).toContainText('What must be true');
});

test('scenario explorer works with the keyboard', async ({ page }) => {
  await page.goto('/report/ch23-scenarios-2050');
  const tabA = page.getByRole('tab', { name: /Regional workshop/ });
  await expect(tabA).toHaveAttribute('aria-selected', 'true');
  // Seven plays and four public goods; the five retired in v0.8 are not scored.
  await expect(page.locator('#scen-panel-A .scen-plays li')).toHaveCount(11);
  await tabA.focus();
  await page.keyboard.press('ArrowRight');
  await expect(page.getByRole('tab', { name: /Security build-out/ })).toHaveAttribute(
    'aria-selected',
    'true',
  );
  await expect(page.locator('#scen-panel-C')).toBeVisible();
  await expect(page.locator('#scen-panel-A')).toBeHidden();
});

test('audience choice shows a reading path and persists', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('button', { name: /Investors/ }).click();
  await expect(page.locator('[data-audience-path="investors"]')).toBeVisible();
  // Reading paths leave out pages the public cannot open.
  await expect(
    page.locator('[data-audience-path="investors"] a[href*="app-s11-capital"]'),
  ).toHaveCount(0);
  await page.goto('/report');
  await expect(page.locator('html')).toHaveAttribute('data-audience', 'investors');
  await expect(page.locator('main [data-aud].is-for-you').first()).toBeVisible();
});

test('no public page scrolls sideways on a phone', async ({ page }) => {
  test.setTimeout(300000);
  await page.setViewportSize({ width: 390, height: 844 });
  const paths = [
    '/',
    '/report',
    '/report/part-ii',
    '/briefs',
    '/glossary',
    '/about',
    '/search?q=soy',
    ...seed.content.pages.filter((e) => !restricted(e.id)).map((e) => pathOf(e.id)),
  ];
  for (const path of paths) {
    await page.goto(path);
    expect(
      await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth),
      path,
    ).toBe(true);
  }
});

test('theme toggle, menu and print', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('/report/ch03-regional');
  await page.getByRole('button', { name: /Menu/ }).click();
  await expect(page.locator('#drawer')).toBeVisible();
  await page.keyboard.press('Escape');
  await expect(page.locator('#drawer')).toBeHidden();
  await page.locator('[data-theme-toggle]').click();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'light');
  await page.locator('[data-theme-toggle]').click();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'dark');
  await page.emulateMedia({ media: 'print' });
  await expect(page.locator('.masthead')).toBeHidden();
});
