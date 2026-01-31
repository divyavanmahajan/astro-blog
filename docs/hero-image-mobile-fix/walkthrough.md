# Fixing Hero Image Display on Mobile

## Problem Summary

The blog post hero images were appearing on mobile devices, which was not desired. Investigation revealed two issues:

1. **Hero images were hardcoded in markdown content** instead of being displayed by the template
2. **Template CSS to hide images on mobile** only applied to `.post-hero img` elements, but the hardcoded images weren't wrapped in that class

## Solution Implemented

### 1. Updated Post Template

Modified [`[...slug].astro`](file:///Users/divya/Documents/projects/astro-blog/src/pages/posts/%5B...slug%5D.astro) to display hero images from the `heroImage` frontmatter field:

```astro
{post.data.heroImage && (
    <div class="post-hero">
        <img src={post.data.heroImage} alt={post.data.heroImageAlt || post.data.title} />
    </div>
)}
```

This ensures all hero images are wrapped with the `.post-hero` class, allowing the existing mobile CSS to properly hide them.

### 2. Removed Hardcoded Hero Images

Removed hardcoded hero image markdown from 6 blog posts:

- [racf-style-authorization-modern-java.md](file:///Users/divya/Documents/projects/astro-blog/src/content/blog/2026/01/racf-style-authorization-modern-java.md)
- [evolution-of-enterprise-java.md](file:///Users/divya/Documents/projects/astro-blog/src/content/blog/2026/01/evolution-of-enterprise-java.md)
- [rethinking-mainframe-modernization.md](file:///Users/divya/Documents/projects/astro-blog/src/content/blog/2026/01/rethinking-mainframe-modernization.md)
- [leadership-and-modernization-insights.md](file:///Users/divya/Documents/projects/astro-blog/src/content/blog/2026/01/leadership-and-modernization-insights.md)
- [ai-coding-assistants-skill-development.md](file:///Users/divya/Documents/projects/astro-blog/src/content/blog/2026/01/ai-coding-assistants-skill-development.md)
- [building-with-antigravity.md](file:///Users/divya/Documents/projects/astro-blog/src/content/blog/2026/01/building-with-antigravity.md)

All these posts had `heroImage` in their frontmatter, so the images will now be displayed via the template instead.

## Verification

Tested the changes locally using the dev server:

````carousel
![Desktop view showing hero image visible](file:///Users/divya/.gemini/antigravity/brain/9e4a9d33-682c-4297-bcc6-b5ea3a6f13e9/desktop_hero_visible_1769817642473.png)
<!-- slide -->
![Mobile view showing hero image hidden](file:///Users/divya/.gemini/antigravity/brain/9e4a9d33-682c-4297-bcc6-b5ea3a6f13e9/mobile_hero_hidden_1769817666043.png)
````

### Desktop (1200px width)
✅ Hero image displays correctly at the top of the post

### Mobile (375px width)
✅ Hero image is properly hidden via CSS media query `@media (max-width: 768px)`

## Before & After Comparison

### Before
- Hero images hardcoded in markdown: `![Alt text](/images/hero.png)`
- Mobile CSS couldn't hide them because they weren't wrapped in `.post-hero`
- Resulted in large images taking up screen space on mobile

### After
- Hero images displayed from `heroImage` frontmatter via template
- All hero images wrapped in `<div class="post-hero">` automatically
- Existing mobile CSS (`display: none`) properly hides them on mobile devices

## Browser Recording

![Browser verification recording](file:///Users/divya/.gemini/antigravity/brain/9e4a9d33-682c-4297-bcc6-b5ea3a6f13e9/hero_image_verification_1769817481737.webp)

The browser recording shows the complete verification process, resizing from desktop to mobile to confirm the hero image behavior.
