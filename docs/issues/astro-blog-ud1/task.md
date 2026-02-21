# Task: Add pubDate to Recent Posts in Sidebar

## Objective
Enhance the "Recent Posts" widget in the sidebar by displaying the publication date for each listed post.

## Details
- **File**: `src/components/Sidebar.astro`
- **Change**: Add a `<time>` or `<span>` element within the `<li>` items to display `post.data.pubDate`.
- **Formatting**: Use a compact date format (e.g., "Feb 21, 2026").
