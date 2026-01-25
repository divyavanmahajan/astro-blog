# Astro Blog Architecture

## 1. Technical Overview

This project is a static site generated using **[Astro](https://astro.build/)**. It prioritizes performance by shipping zero JavaScript to the client by default, hydrating components only when necessary (though this project currently uses vanilla HTML/CSS).

### Core Stack
-   **Framework**: Astro v4
-   **Templating**: `.astro` components (JSX-like syntax)
-   **Styling**: CSS Variables (Theme-based) + Scoped CSS
-   **Content**: Markdown with Frontmatter + Astro Content Collections

## 2. Project Structure

```text
/
├── public/             # Static assets (images, favicon)
├── src/
│   ├── components/     # UI building blocks
│   │   ├── Header.astro        # Site header with navigation
│   │   ├── Footer.astro        # Site footer with social links
│   │   ├── Sidebar.astro       # Sidebar with widgets
│   │   ├── Search.astro        # Client-side search component
│   │   ├── TableOfContents.astro # Post navigation TOC
│   │   ├── SeriesNav.astro     # Series navigation for multi-part posts
│   │   └── ProfileImage.astro  # Circular profile image
│   ├── content/        # Markdown content source
│   │   └── blog/       # Blog posts (organized by YYYY/MM/)
│   │   └── config.ts   # Content Collection Schema (Zod)
│   ├── layouts/        # Page wrappers (BaseLayout.astro)
│   ├── pages/          # File-based routing
│   │   ├── index.astro         # Homepage
│   │   ├── about.astro         # About page
│   │   ├── categories/         # Category overview and dynamic pages
│   │   ├── series/             # Series overview and dynamic pages
│   │   └── posts/
│   │       └── [...slug].astro # Dynamic Post pages
│   └── styles/         # Global CSS (Variables, Reset)
├── docs/               # Project documentation
│   ├── architecture.md # Technical architecture
│   ├── spec.md         # Requirements specification
│   ├── search.md       # Search implementation
│   └── styling.md      # Design system
├── astro.config.mjs    # Astro configuration (Site URL, Base path)
└── .github/            # CI/CD Workflows
```

## 3. Data Flow

1.  **Authoring**: Content is written in Markdown files in `src/content/blog/ (organized by YYYY/MM/)`.
2.  **Validation**: `src/content/config.ts` defines a **Zod schema**. Astro validates all frontmatter at build time, preventing broken builds due to missing fields (e.g., missing `title` or invalid `date`).
3.  **Collection API**: Pages query data using `getCollection('blog')`.
4.  **Routing**:
    -   `index.astro` pulls all published posts and displays them, including series badges for multi-part content.
    -   `[...slug].astro` generates a unique page for every post found in the collection.
    -   `categories/index.astro` and `categories/[category].astro` provide category-based discovery.
    -   `series/index.astro` and `series/[series].astro` provide series-based discovery.

## 4. Deployment Pipeline

The site is designed for **Multi-Target Deployment**.

### A. GitHub Pages (Primary)
-   **Configuration**: `astro.config.mjs` sets `base: '/'` to support root path serving.
-   **Workflow**: `.github/workflows/deploy.yml`
    1.  **Trigger**: Push to `main`.
    2.  **Build**: separate job runs `npm run build` on Ubuntu.
    3.  **Upload**: Build artifacts (`dist/` folder) are uploaded to GitHub Actions.
    4.  **Deploy**: GitHub Pages Deployment action pushes artifacts to the static website environment.

### B. Cloudflare Pages (Simultaneous)
-   **Configuration**: Connects directly to the GitHub Repository.
-   **Build Command**: `divya npm run build` (or `npm run build`)
-   **Output Directory**: `dist`
-   **Note on Base Path**: If serving from a distinct domain (e.g., `blog.example.com`), Cloudflare builds might need a different `base` path configuration or environment variable overrides compared to the GitHub Pages subdirectory setup.

## 5. Search Functionality

The blog includes a lightweight client-side search feature implemented in `src/components/Search.astro`.

**Key Features:**
- Real-time search with debounced input (300ms)
- Searches post titles and descriptions
- Displays up to 5 results in a dropdown
- Highlights matching text
- No external dependencies (vanilla JavaScript)

See [search.md](./search.md) for detailed implementation.

## 6. Series Navigation

The blog supports multi-part series posts through the `SeriesNav` component, allowing readers to navigate between related posts in a logical sequence.

**Key Features:**
- Automatic series detection from frontmatter `series` field
- Sequential ordering based on series ID format (`name-###`)
- Visual indication of current position in series
- Renders only when 2+ posts exist in a series
- Displays before TOC and after post content
- Site-wide series overview page at `/series`
- Series indicators on the homepage post list
- Support for spaces in series titles (replaces `_` and `-`)

**Implementation:**
- Component: `src/components/SeriesNav.astro`
- Overview Page: `src/pages/series/index.astro`
- Individual Pages: `src/pages/series/[series].astro`
- Series ID Format: `{series-name}-{sequence}` (e.g., `mainframe-modernization-001`)
- Layout Integration: `src/pages/posts/[...slug].astro` and `src/pages/index.astro`

**Technical Details:**
- Queries all posts via `getCollection('blog')`
- Filters by series name prefix
- Sorts by parsed sequence number
- Highlights current post with "You are here" badge
- Provides navigation links to all other posts in series

See [series-navigation.md](./series-navigation.md) for complete documentation.

## 7. Styling Architecture

-   **Global Styles**: `src/styles/global.css` defines CSS Variables (`--color-primary`, `--font-sans`) which control the widespread look and feel (The "Mainroad" theme).
-   **Scoped Styles**: Each `.astro` component has a `<style>` block. These styles are scoped to the component (hashed classes) to prevent side-effects, ensuring modularity.
