# Mobile Layout Optimization

Refine the blog's mobile experience by compacting the header, implementing a hamburger menu, and optimizing post listing density.

## Proposed Changes

### Header Component
#### [MODIFY] [Header.astro](file:///Users/divya/Documents/projects/astro-blog/src/components/Header.astro)
- Add a `<button id="menu-toggle">` on mobile containing a hamburger icon and "Menu" text.
- Wrap title and toggle in a primary header bar for mobile.
- Hide `.site-subtitle` on mobile.
- Apply `display: none` to the `.menu` on mobile by default, and `display: block/flex` (absolute positioned dropdown) when a `.is-open` class is present.
- Reduce `.site-title` font-size to match body text (~1rem) on mobile.

### Page Templates (Standardizing Mobile Post View)
#### [MODIFY] [index.astro](file:///Users/divya/Documents/projects/astro-blog/src/pages/index.astro)
- Update `@media (max-width: 768px)` styles:
    - `.post-entry`: `margin-bottom: 1px`, `padding: 0.75rem`.
    - `.entry-title`: `font-size: 1.1rem`.
    - `.entry-thumbnail`: `width: 24px`, `height: 24px`.
    - `.entry-content`: Maintain `flex-direction: row` even on mobile to keep 24px thumb to the left of text.

#### [MODIFY] [tags/[tag].astro](file:///Users/divya/Documents/projects/astro-blog/src/pages/tags/%5Btag%5D.astro)
#### [MODIFY] [categories/[category].astro](file:///Users/divya/Documents/projects/astro-blog/src/pages/categories/%5Bcategory%5D.astro)
#### [MODIFY] [series/[series].astro](file:///Users/divya/Documents/projects/astro-blog/src/pages/series/%5Bseries%5D.astro)
- Sync the above CSS/HTML structure changes to maintain consistency.

## Verification Plan

### Automated Tests
- Use the browser tool to capture screenshots at mobile viewport widths (e.g., 375px).
- Verify subtitle is hidden.
- Verify "Menu" button is present and clickable (requires interaction in subagent).

### Manual Verification
- Check the dropdown menu behavior on a mobile device or simulation.
- Verify the 1px gap between post boxes is visually correct.
