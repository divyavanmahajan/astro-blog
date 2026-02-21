# Walkthrough - Add pubDate to Recent Posts in Sidebar

## Changes Made

### 1. Updated Sidebar Component
- **File**: `src/components/Sidebar.astro`
- **Markup Change**: Added a `<span>` with the class `recent-post-date` to the "Recent Posts" list items. This span displays the `pubDate` formatted as `MMM DD, YYYY`.
- **CSS Change**: 
    - Forced `recent-post-title` to `display: block` to place the date on a new line.
    - Styled `recent-post-date` with a smaller font size (`0.75rem`) and a lighter color (`var(--color-text-light)` in uppercase) for a clean, subtle look.

## Verification
- Verified that the `pubDate` is correctly pulled from the post data.
- Ran `npm run build` to ensure no build errors.

## References
- Issue: astro-blog-ud1
