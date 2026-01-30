# Series Navigation Feature

## Overview

The series navigation feature allows blog posts to be organized into sequential series, providing readers with clear navigation between related posts and context about their position within a series.

## Frontmatter Configuration

### Series ID Format

The `series` field in frontmatter follows the pattern: `{series-name}-{sequence-number}`

- **series-name**: Alphanumeric identifier for the series (use hyphens or underscores to separate words)
- **sequence-number**: Three-digit zero-padded number (001, 002, 003, etc.)

### Example

```yaml
---
title: 'Part 1: Introduction to Mainframe Modernization'
pubDate: 2026-01-25
series: "mainframe-modernization-001"
---
```

```yaml
---
title: 'Part 2: RACF-Style Authorization'
pubDate: 2026-01-25
series: "mainframe-modernization-002"
---
```

## Series Naming Conventions

### Good Series Names

- `mainframe-modernization` - Clear, descriptive
- `react-hooks-guide` - Technology-focused
- `startup-journey` - Narrative series
- `performance-optimization` - Topic-based

### Avoid

- Single words without context: `tutorial`
- Overly long names: `the-complete-comprehensive-guide-to-everything`
- Special characters: `web_dev@2024`

## Component Behavior

The `SeriesNav` component automatically:

1. **Detects series membership** - Parses the series ID from frontmatter
2. **Finds all related posts** - Queries all blog posts with matching series names
3. **Sorts by sequence** - Orders posts by their sequence numbers
4. **Highlights current post** - Visually indicates "You are here"
5. **Conditionally renders** - Only displays if:
   - The post has a `series` field
   - There are 2+ posts in the series

## Placement

The `SeriesNav` component appears in two locations:

1. **Before Table of Contents** - Gives readers immediate context
2. **After post content** - Enables easy navigation to next post in series
3. **Home Page** - Posts that are part of a series show a "Part of: [Series Name]" badge.
4. **Series Overview** - Site-wide list of all series at `/series`.

## Visual Design

### Layout
- **Clean bordered layout** - Matches the Table of Contents aesthetic
- **Series header** - Shows "Part X of Y in the {series name} series" with dark header and red links
- **Ordered list** - Numbered posts in sequence
- **Current post badge** - "You are here" indicator
- **Interactive links** - Hover effects on navigable posts

### Responsive Behavior
- Full information on desktop
- Condensed padding and font sizes on mobile
- Touch-friendly link targets

## Implementation Files

### Component
- **Path**: `/src/components/SeriesNav.astro`
- **Props**:
  - `currentSeries?: string` - The series ID from frontmatter
  - `currentSlug: string` - The current post's slug for highlighting

### Integration
- **File**: `/src/pages/posts/[...slug].astro`
- **Usage**:
  ```astro
  <SeriesNav currentSeries={post.data.series} currentSlug={post.slug} />
  ```

## Example Series Structure

### Mainframe Modernization Series

```
mainframe-modernization-001: "Rethinking Mainframe Modernization: Are We Just Reinventing the Wheel?"
mainframe-modernization-002: "Implementing RACF-Style Authorization in Modern Java Applications"
mainframe-modernization-003: (Future post) "CICS Transaction Patterns in Spring Boot"
mainframe-modernization-004: (Future post) "Batch Processing: Mainframe vs. Cloud Native"
```

## Adding Posts to a Series

### Step 1: Plan Your Series

1. Choose a descriptive series name (e.g., `mainframe-modernization`)
2. Outline all planned posts
3. Assign sequence numbers starting from 001

### Step 2: Create Posts

Add the `series` field to each post's frontmatter:

```yaml
---
title: "Your Post Title"
pubDate: 2026-01-25
series: "your-series-name-001"
# ... other frontmatter fields
---
```

### Step 3: Verify

1. Build the site: `npm run build`
2. Check that the SeriesNav appears on all series posts
3. Verify links work correctly
4. Confirm current post is highlighted

## Best Practices

### Series Planning

1. **Plan ahead** - Outline all posts before starting
2. **Consistent naming** - Use the same series name across all posts
3. **Sequential numbering** - Don't skip sequence numbers
4. **Logical flow** - Ensure posts build on each other

### Content Guidelines

1. **Standalone value** - Each post should provide value independently
2. **Cross-reference** - Link between related concepts in different posts
3. **Progressive complexity** - Start simple, build to advanced topics
4. **Consistent style** - Maintain similar tone and structure

### Maintenance

1. **Update all posts** - If renaming a series, update all posts
2. **Fill gaps** - If you skip a number, readers will notice
3. **Archive carefully** - If removing a post, reassign sequence numbers
4. **Document intent** - Add series overview in first post

## Technical Details

### Series Detection Algorithm

```typescript
// Parse series ID
const [seriesName, currentSequence] = currentSeries.split('-');

// Find all posts in series
const seriesPosts = allPosts
    .filter(post => post.data.series?.startsWith(seriesName + '-'))
    .map(post => ({
        ...post,
        sequence: parseInt(post.data.series?.split('-')[1] || '0')
    }))
    .sort((a, b) => a.sequence - b.sequence);
```

### Null Handling

The component gracefully handles:
- Posts without a `series` field (renders nothing)
- Single post in a series (renders nothing)
- Invalid series format (renders nothing)

## Styling Customization

The component uses CSS custom properties from your global theme. To customize:

```css
/* In your global CSS */
.series-nav {
    /* Override gradient */
    background: linear-gradient(135deg, #your-color-1 0%, #your-color-2 100%);
}
```

## Future Enhancements

Potential additions to consider:
- Series metadata (description, cover image)
- Progress indicators (visual progress bar)
- Estimated reading time for entire series
- Series landing pages
- RSS feeds per series
- Series search/filtering

## Troubleshooting

### Series Nav Not Appearing

**Check:**
1. Is `series` field present in frontmatter?
2. Are there 2+ posts with matching series names?
3. Is the series ID format correct (`name-###`)?
4. Is the component imported in the page template?

### Wrong Post Order

**Check:**
1. Are sequence numbers sequential?
2. Are they zero-padded (001, not 1)?
3. Do all posts use the exact same series name prefix?

### Current Post Not Highlighted

**Check:**
1. Is `currentSlug` being passed correctly?
2. Does the slug match the post's actual slug?
3. Check browser console for errors

## Accessibility

The component includes:
- Semantic `<nav>` element with `aria-label`
- Ordered list (`<ol>`) for sequential content
- Clear visual and textual indicators of current position
- Keyboard navigation support (native link focus)

## SEO Considerations

Series navigation:
- **Improves internal linking** - Better site structure
- **Reduces bounce rate** - Encourages exploration
- **Increases time on site** - Readers stay for entire series
- **Provides context** - Search engines understand content relationships

## Example: Complete Implementation

```yaml
---
title: 'Understanding React Hooks: Part 1 - useState'
description: 'Learn the fundamentals of the useState hook in React'
pubDate: 2026-01-25
category: 'development'
tags: ['react', 'hooks', 'javascript']
author: 'Divya van Mahajan'
series: "react-hooks-guide-001"
---

# Understanding React Hooks: Part 1 - useState

This is the first in a series exploring React Hooks in depth...
```

---

**Created**: 2026-01-25  
**Version**: 1.0  
**Status**: Active
