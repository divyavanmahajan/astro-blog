---
title: "How This Blog Deploys to Cloudflare"
description: "TIL about the multi-target deployment strategy of this blog, utilizing Cloudflare Pages and environment variables."
pubDate: 2026-02-01
tags: ["cloudflare", "astro", "deployment", "cicd"]
draft: false
---

Today I learned (or rather, documented) how this specific blog project manages its deployment to Cloudflare. It uses a robust multi-target strategy that ensures the site is highly available and correctly configured across different hosting environments.

## The Cloudflare Components

This project primarily utilizes **Cloudflare Pages**, which provides:
- **Fast, Global CDN**: Content is served from the edge, minimizing latency.
- **Seamless Git Integration**: Cloudflare connects directly to the GitHub repository and triggers a build on every push to the `main` branch.
- **Environment Variables**: Crucial for coordinating between different deployment targets.

## The Deployment Strategy

We maintain a dual-deployment setup where the site is hosted on both **GitHub Pages** and **Cloudflare Pages**. 

### 1. Unified Configuration
To support both platforms, we've updated `astro.config.mjs` to be environment-aware. We use `process.env` to dynamically set the `site` and `base` properties:

```javascript
export default defineConfig({
    site: process.env.SITE || 'https://divyavanmahajan.github.io',
    base: process.env.BASE || '/',
    // ...
});
```

### 2. Cloudflare Pages Setup
In the Cloudflare Dashboard, we configure the project with the following environment variables:
- `BASE`: `/` (since it's served from the root domain)
- `SITE`: `https://vanmahajan.de` (or the `.pages.dev` URL)

When Cloudflare triggers a build (`npm run build`), Astro picks up these variables and generates the correct internal links for the root-level deployment.

### 3. Automatic Builds
The workflow is simple:
1. Push code to the `main` branch.
2. **GitHub Actions** builds and deploys to GitHub Pages (configured for the subdirectory).
3. **Cloudflare Pages** detects the push and building-and-deploys to the Cloudflare CDN (configured for the root).

## Why this approach?

This setup gives us the best of both worlds: the reliability of GitHub Pages and the performance of Cloudflare's global edge network. By using environment variables, we maintain a single codebase that adapts perfectly to its hosting context.
