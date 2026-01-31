# Standardize TIL Headers on Mobile

## Proposed Changes

### [TIL index page](file:///Users/divya/Documents/projects/astro-blog/src/pages/til/index.astro)
- Update `.til-title` on mobile to `font-size: 1rem` and `text-transform: uppercase`.
- Reduce `.til-header` margin/padding on mobile.
- Tighten `.til-list` gap and `.til-entry` padding on mobile.

### [TIL single post page](file:///Users/divya/Documents/projects/astro-blog/src/pages/til/%5B...slug%5D.astro)
- Update `.til-post-header h1` on mobile to `font-size: 1rem` and `text-transform: uppercase`.
- Update `.til-content :global(h2)` and `.til-content :global(h3)` on mobile to `font-size: 1.05rem` and `text-transform: uppercase`.
- Reduce `.til-post-header` margin-bottom and padding-bottom on mobile.
- Reduce vertical spacing between headers and paragraphs in `.til-content`.

## Verification Plan

### Manual Verification
- View TIL index and single post pages in mobile viewport (375px) using browser tool.
- Confirm header sizes match blog posts.
