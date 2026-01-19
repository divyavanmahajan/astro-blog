# Client-Side Blog Search

## Overview

The blog includes a lightweight, client-side search feature that allows users to search through post titles and descriptions in real-time.

## Implementation

### Search Component

**Location**: `src/components/Search.astro`

**Features**:
- **Real-time search** with 300ms debounce for performance
- **Searches** post titles and descriptions
- **Highlights** matching text in yellow (`#fff3cd`)
- **Dropdown results** showing up to 5 matches
- **Keyboard support** (Escape to close)
- **Click outside** to close results
- **No results message** when no matches found

### How It Works

1. **Build Time**: All published posts are collected and passed to the Search component
2. **User Input**: Input is debounced (300ms delay) to avoid excessive filtering
3. **Filtering**: JavaScript filters posts where title or description contains the query (case-insensitive)
4. **Display**: Results shown in dropdown with highlighted matches
5. **Navigation**: Click result to navigate to post

### Integration

The Search component is integrated into the Sidebar widget:

```astro
<div class="widget search-widget">
    <h3 class="widget-title">Search</h3>
    <Search />
</div>
```

## Technical Details

- **No external dependencies** - uses vanilla JavaScript
- **Client-side only** - all post data loaded at page load
- **Filters draft posts** - only searches published content
- **Responsive** - dropdown has max-height with scroll
- **Accessible** - includes ARIA labels and keyboard navigation

## Limitations

- Searches only titles and descriptions (not full post content)
- Limited to 5 results maximum
- No advanced search features (AND/OR operators, fuzzy matching)
- All post data loaded on page (minimal impact with small number of posts)

## Styling

The search component uses the blog's CSS variables for consistency:
- Input border: `var(--color-border)`
- Focus border: `var(--color-primary)`
- Text color: `var(--color-text)`
- Font: `var(--font-body)`

## Future Enhancements

Potential improvements:
- Full-text search of post content
- Search by tags or categories
- Arrow key navigation through results
- Search history/recent searches
- Fuzzy matching for typos
