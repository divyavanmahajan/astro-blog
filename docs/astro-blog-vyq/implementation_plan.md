# Compact vertical whitespace on blog home page (astro-blog-vyq)

The goal of this issue is to reduce the excessive vertical whitespace on the blog home page to improve content density and ensure more posts are visible above the fold.

## User Review Required

> [!IMPORTANT]
> This change will affect the overall visual density of the home page. Please review the proposed spacing adjustments once implemented.

## Proposed Changes

### [Home Page]

#### [MODIFY] [index.astro](file:///Users/divya/Documents/projects/astro-blog/src/pages/index.astro)
- **Compact Layout**:
    - Reduce `.post-entry` margin-bottom from `2rem` to `1rem`.
    - Reduce `.post-entry` padding from `2rem` to `1.25rem`.
    - Reduce `.entry-title` font-size slightly and margin-bottom.
- **Content Clamping & Inline "Read more..."**:
    - Use `position: relative` and `max-height` (calculated as 3 lines) on the summary container.
    - Position `.read-more-link` absolutely at the bottom-right corner.
    - Add a background gradient to `.read-more-link` (from transparent to white) to "fade out" the text behind it, creating a seamless inline look at the end of the 3rd line.
    - Ensure the link is always visible regardless of text length.
- **Thumbnail Adjustments**:
    - Set `.entry-thumbnail` height to exactly match 3 lines of text (`3 * line-height`).
    - Keep `aspect-ratio: 1/1` for the image.

## Verification Plan

### Manual Verification
- View the blog home page locally.
- Verify that descriptions are limited to 3 lines.
- Verify that thumbnails are smaller and match the text height.
- Verify that "Read more..." appears integrated.
- Verify overall vertical density is higher.
