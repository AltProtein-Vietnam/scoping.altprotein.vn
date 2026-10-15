declare namespace App {
  interface Locals {
    /** Interface language, from the optional /vi path prefix. */
    lang: 'en' | 'vi';
    /** Request path without the /vi prefix. */
    basePath: string;
    /** A signed-in Editor or Administrator. */
    canEdit: boolean;
    /** The editor view is on: restricted pages, data and files are shown. */
    editor: boolean;
  }
}

// The Workers runtime module, typed only for what the site uses (worker-configuration.d.ts holds
// the full runtime types for Wrangler, but `astro check` keeps the DOM types instead).
declare module 'cloudflare:workers' {
  export const env: {
    ASSETS: { fetch(request: Request | string): Promise<Response> };
  };
}
