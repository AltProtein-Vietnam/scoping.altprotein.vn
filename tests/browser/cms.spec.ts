import { test, expect, request as apiRequest } from '@playwright/test';

const baseURL = 'http://127.0.0.1:4321';

test('editor can save, privately preview and publish a page; reseeding preserves edits', async ({
  page,
  request,
}) => {
  test.setTimeout(180000);
  const editor = await apiRequest.newContext({
    baseURL,
    extraHTTPHeaders: { Origin: baseURL, 'X-EmDash-Request': '1' },
  });
  expect((await editor.post('/_emdash/api/setup/dev-bypass')).ok()).toBeTruthy();
  const endpoint = '/_emdash/api/content/pages/ch30-unknowns';
  const originalResponse = await editor.get(endpoint);
  expect(originalResponse.ok()).toBeTruthy();
  const original = (await originalResponse.json()).data.item;
  const marker = 'Local acceptance test paragraph.';
  const body = original.data.body.replace(/\n## /, `\n${marker}\n\n## `);
  try {
    const saved = await editor.put(endpoint, { data: { data: { ...original.data, body } } });
    expect(saved.ok(), await saved.text()).toBeTruthy();
    await page.goto('/report/ch30-unknowns');
    await expect(page.locator('.prose')).not.toContainText(marker);
    const previewResponse = await editor.post(endpoint + '/preview-url', { data: {} });
    expect(previewResponse.ok()).toBeTruthy();
    const preview = (await previewResponse.json()).data.url as string;
    expect(preview).toContain('/pages/ch30-unknowns');
    expect((await request.get(preview)).status()).toBe(403);
    const privatePreview = await editor.get(preview);
    expect(privatePreview.status()).toBe(200);
    expect(await privatePreview.text()).toContain(marker);
    expect(privatePreview.headers()['cache-control']).toContain('no-store');
    expect((await editor.post(endpoint + '/publish', { data: {} })).ok()).toBeTruthy();
    await page.reload();
    await expect(page.locator('.prose')).toContainText(marker);
    await editor.post('/_emdash/api/setup/dev-bypass');
    await page.reload();
    await expect(page.locator('.prose')).toContainText(marker);
    expect((await editor.get(endpoint + '/revisions')).ok()).toBeTruthy();
    await page.context().addCookies((await editor.storageState()).cookies);
    await page.goto(`/_emdash/admin/content/pages/${original.id}`);
    await page
      .getByRole('button', { name: 'Get Started', exact: true })
      .click({ timeout: 5000 })
      .catch(() => {});
    await page.waitForLoadState('networkidle');
    await expect(page.locator('textarea').first()).toBeVisible({ timeout: 30000 });
  } finally {
    const restored = await editor.put(endpoint, { data: { data: original.data } });
    expect(restored.ok(), await restored.text()).toBeTruthy();
    expect((await editor.post(endpoint + '/publish', { data: {} })).ok()).toBeTruthy();
    await editor.dispose();
  }
});

test('editors can edit a page in EmDash edit mode; drafts stay out of other views', async ({
  page,
  request,
}) => {
  test.setTimeout(120000);
  const editor = await apiRequest.newContext({
    baseURL,
    extraHTTPHeaders: { Origin: baseURL, 'X-EmDash-Request': '1' },
  });
  expect((await editor.post('/_emdash/api/setup/dev-bypass')).ok()).toBeTruthy();
  const path = '/summary';
  const endpoint = '/_emdash/api/content/pages/front-exec-summary';
  const originalResponse = await editor.get(endpoint);
  expect(originalResponse.ok()).toBeTruthy();
  const original = (await originalResponse.json()).data.item;
  // A draft of the body with the same length as the published one: it shares the published
  // page's render-cache key, so it must not be cached when edit mode shows it.
  const bodyMarker = 'qzx';
  const body = original.data.body.replace(/(?<=\n[A-Z][^\n]*?) the /, ` ${bodyMarker} `);
  expect(body).not.toBe(original.data.body);
  expect(body.length).toBe(original.data.body.length);
  const summaryMarker = 'Summary edited in edit mode.';
  try {
    const saved = await editor.put(endpoint, { data: { data: { ...original.data, body } } });
    expect(saved.ok(), await saved.text()).toBeTruthy();
    const session = (await editor.storageState()).cookies;
    await page
      .context()
      .addCookies([...session, { name: 'emdash-edit-mode', value: 'true', url: baseURL }]);
    await page.goto(path);
    await expect(page.locator('#emdash-toolbar')).toHaveAttribute('data-edit-mode', 'true');
    const ref = async (selector: string) =>
      JSON.parse((await page.locator(selector).first().getAttribute('data-emdash-ref')) ?? '{}');
    expect(await ref('article.doc')).toEqual(
      expect.objectContaining({ collection: 'pages', id: original.id, hasDraft: true }),
    );
    expect((await ref('article.doc')).field).toBeUndefined();
    expect((await ref('.doc-head h1')).field).toBe('body');
    expect((await ref('.lede')).field).toBe('summary');
    expect((await ref('.prose')).field).toBe('body');
    await expect(page.locator('.prose')).toContainText(` ${bodyMarker} `);
    await expect(page.locator('#emdash-tb-status')).toContainText('Unpublished changes');
    // The toolbar shows the draft's status, so the preview-link note is not shown.
    await expect(page.locator('.page-note.is-preview')).toHaveCount(0);

    // The summary is shown as stored, so it is edited in place and saved to the draft.
    await page.locator('.lede').click();
    await expect(page.locator('.lede[data-emdash-editing]')).toBeVisible();
    const put = page.waitForResponse(
      (r) => r.url().includes('/_emdash/api/content/pages/') && r.request().method() === 'PUT',
    );
    await page.keyboard.type(summaryMarker);
    await page.keyboard.press('Enter');
    expect((await put).ok()).toBeTruthy();
    await page.reload();
    await expect(page.locator('.lede')).toHaveText(summaryMarker);

    // The body is Markdown with report tokens, so its text opens the entry in the CMS instead.
    const popup = page.waitForEvent('popup');
    await page.locator('.prose p').first().click();
    const admin = await popup;
    expect(admin.url()).toContain(`/_emdash/admin/content/pages/${original.id}?field=body`);
    await admin.close();

    // Outside edit mode, editors and visitors see the published page.
    await page.context().clearCookies({ name: 'emdash-edit-mode' });
    await page.goto(path);
    await expect(page.locator('#emdash-toolbar')).toHaveAttribute('data-edit-mode', 'false');
    await expect(page.locator('[data-emdash-ref]')).toHaveCount(0);
    await expect(page.locator('.prose')).not.toContainText(` ${bodyMarker} `);
    await expect(page.locator('.lede')).toHaveText(original.data.summary);
    const visitor = await (await request.get(path)).text();
    expect(visitor).not.toContain(` ${bodyMarker} `);
    expect(visitor).not.toContain(summaryMarker);
    expect(visitor).not.toContain('data-emdash-ref="');
  } finally {
    const discarded = await editor.post(endpoint + '/discard-draft', { data: {} });
    expect(discarded.ok(), await discarded.text()).toBeTruthy();
    await editor.dispose();
  }
});
