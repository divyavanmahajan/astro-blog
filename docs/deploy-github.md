# Deploy to GitHub Pages

This guide explains how to configure your repository and project to deploy to GitHub Pages.

## 1. Default Deployment (Subdirectory)

By default, if your repository is named `my-project` (e.g., `astro-blog`), GitHub Pages serves your site at `https://<username>.github.io/my-project/`.

### Configuration
The project is configured for root domain deployment:
- **Repo Name**: `username.github.io` (e.g., `divyavanmahajan.github.io`)
- **Config**: `base: '/'` (in `astro.config.mjs`)

## 2. Root Domain Deployment

To serve your site at the root of your user page (`https://<username>.github.io/`), you must follow these specific steps:

### Step 1: Rename the Repository
1.  Go to your repository **Settings** on GitHub.
2.  Rename the repository to exactly:
    **`<username>.github.io`** 
    *(e.g., `divyavanmahajan.github.io`)*

### Step 2: Update Configuration
You need to tell Astro that the site is now at the root.

**Option A: Using Environment Variables (Recommended)**
1.  Go to your repository **Settings** > **Secrets and variables** > **Actions** > **Variables**.
2.  Create a new repository variable:
    -   **Name**: `BASE`
    -   **Value**: `/`
3.  (Optional) Create another variable for `SITE` if you want to be explicit, though `astro.config.mjs` usually falls back to the github.io URL.

**Option B: Edit Config File**
Edit `astro.config.mjs` directly:
```js
export default defineConfig({
    site: 'https://divyavanmahajan.github.io',
    base: '/',
});
```

### Step 3: Trigger Deployment
Push a commit (or an empty commit) to trigger the GitHub Action:
```bash
git commit --allow-empty -m "fix: trigger deploy for root path"
git push
```

## Troubleshooting
-   **404 on CSS/JS**: This usually means the `base` path in `astro.config.mjs` doesn't match the actual URL path where GitHub is serving the site.
-   **Empty Page**: Check the Console for 404 errors on assets.
