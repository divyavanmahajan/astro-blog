# LinkedIn Integration Specification

## Overview

This specification defines the automated LinkedIn cross-posting functionality for the Astro blog. The system will automatically generate LinkedIn-ready content (both articles and posts) from blog posts that have the `linkedin: true` frontmatter attribute.

## Goals

1. **Automatic Article Generation**: When a blog post is marked with `linkedin: true`, automatically generate LinkedIn article content during the build process
2. **Manual Post Creation**: Provide formatted post text that can be manually copied and posted to LinkedIn
3. **Update Support**: Regenerate content when blog posts are updated, with update summaries
4. **Content Tracking**: Track LinkedIn article URLs in blog post frontmatter

## User Workflow

### Initial Publication

1. Author adds `linkedin: true` to a blog post's frontmatter
2. Build process automatically generates LinkedIn-ready files in `linkedin/` directory
3. Author manually creates LinkedIn article using generated HTML/rich-text content
4. Author copies LinkedIn article URL and adds it to blog post frontmatter as `linkedinArticleUrl: "https://..."`
5. Author manually creates LinkedIn post using generated post text file
6. Commit changes (including generated files and updated frontmatter)

### Updating Published Content

1. Author updates blog post content
2. Build process regenerates LinkedIn files (full content + update summary)
3. Author manually updates LinkedIn article with regenerated content
4. Author optionally posts update summary as a new LinkedIn post or comment
5. Commit changes

## Frontmatter Schema

### Required Fields for LinkedIn Integration

```yaml
---
title: "Blog Post Title"
description: "Brief description of the post"
linkedin: true  # Enables LinkedIn integration
---
```

### Optional Fields

```yaml
---
linkedinMessage: "Custom message for LinkedIn post instead of description"
linkedinArticleUrl: "https://www.linkedin.com/pulse/article-slug-author-name"
---
```

### Field Descriptions

- **`linkedin`** (boolean): When `true`, triggers LinkedIn content generation
- **`linkedinMessage`** (string, optional): Custom message for the LinkedIn post. If not provided, uses `description`
- **`linkedinArticleUrl`** (string, optional): URL of the published LinkedIn article. Added manually after publishing

## Content Generation

### LinkedIn Article Content

The generated article should include:

1. **Full blog post content** including:
   - Title
   - Table of contents (converted to LinkedIn-compatible format)
   - All body content
   - Code blocks (formatted for LinkedIn)
   - Images (with absolute URLs to divyavanmahajan.github.io)

2. **Format conversions**:
   - Markdown → LinkedIn-compatible HTML
   - Relative image URLs → Absolute URLs (`https://divyavanmahajan.github.io/...`)
   - Code blocks → LinkedIn code formatting
   - Table of contents component → Plain HTML list with anchor links

3. **Output formats**:
   - **HTML file**: Clean HTML suitable for LinkedIn's HTML editor
   - **Rich text file**: Formatted text optimized for LinkedIn's visual editor

### LinkedIn Post Content

The generated post should include:

1. **Post structure**:
   ```
   [Title]
   
   [Excerpt/LinkedInMessage]
   
   Read the full article: [LinkedInArticleUrl or placeholder]
   ```

2. **Content sources**:
   - Title: From `title` frontmatter
   - Excerpt: From `linkedinMessage` if present, otherwise `description`
   - Link: From `linkedinArticleUrl` if present, otherwise placeholder text

3. **Auto-generation fallback**:
   - If `description` is missing, auto-generate from first paragraph of blog post

### Update Summary

When a blog post with existing `linkedinArticleUrl` is updated, generate an update summary:

```
📝 Article Update

I've updated my article "[Title]" with:
- [Auto-detected changes summary]

Read the updated article: [LinkedInArticleUrl]
```

The update summary should:
- Detect major changes (new sections, significant edits)
- Provide a brief, human-readable summary
- Include link to the LinkedIn article

## File Structure

### Generated Files Location

All generated LinkedIn content will be stored in:

```
linkedin/
├── [blog-post-slug]/
│   ├── article.html          # HTML version for LinkedIn HTML editor
│   ├── article.txt           # Rich text version for visual editor
│   ├── post.txt              # LinkedIn post text
│   └── update-summary.txt    # Update summary (if article was updated)
```

### File Naming

- Use blog post slug (filename without extension) as directory name
- Consistent file names across all posts: `article.html`, `article.txt`, `post.txt`, `update-summary.txt`

### Git Tracking

- All files in `linkedin/` directory should be committed to git
- Provides history of published content
- Enables tracking of what was actually posted to LinkedIn

## Technical Implementation

### Technology Stack

- **Node.js script**: Integrates with existing Astro/npm ecosystem
- **Integration point**: Astro build process (via integration or build hook)
- **Dependencies**: 
  - Markdown parser (likely already available via Astro)
  - HTML sanitizer/formatter
  - File system utilities (Node.js built-in)

### Build Integration

1. **Astro Integration**: Create custom Astro integration that runs during build
2. **Hook**: `astro:build:done` or similar lifecycle hook
3. **Process**:
   - Scan all blog posts in `src/content/blog/`
   - Filter posts with `linkedin: true`
   - Generate LinkedIn content for each
   - Write files to `linkedin/` directory
   - Log summary of generated files

### NPM Scripts

Add to `package.json`:

```json
{
  "scripts": {
    "linkedin": "node scripts/generate-linkedin.js",
    "build": "astro build && npm run linkedin"
  }
}
```

## Content Transformation Rules

### Images

- **Relative URLs**: Convert to absolute URLs
  - `/images/foo.png` → `https://divyavanmahajan.github.io/images/foo.png`
  - `./foo.png` → `https://divyavanmahajan.github.io/blog/[slug]/foo.png`
- **Already absolute URLs**: Keep as-is
- **Missing images**: Log warning, include broken link in output

### Code Blocks

- Preserve syntax highlighting information
- Format for LinkedIn's code block support:
  ```html
  <pre><code class="language-javascript">
  // code here
  </code></pre>
  ```
- Ensure proper escaping of HTML entities

### Links

- Convert relative links to absolute:
  - `/about` → `https://divyavanmahajan.github.io/about`
  - `./other-post` → `https://divyavanmahajan.github.io/blog/other-post`
- External links: Keep as-is

### Table of Contents

- Convert Astro `<TableOfContents>` component to plain HTML list
- Generate anchor links that work in LinkedIn articles
- Format as nested `<ul>` with `<a>` tags

### Special Markdown Features

- **Alerts/Callouts**: Convert to blockquotes or emphasized paragraphs
- **Embeds**: Convert to links
- **Custom components**: Best-effort conversion to standard HTML

### Text Formatting

- **Bold**: `**text**` → `<strong>text</strong>`
- **Italic**: `*text*` → `<em>text</em>`
- **Headings**: Preserve hierarchy (H1-H6)
- **Lists**: Preserve ordered/unordered structure
- **Blockquotes**: Convert to `<blockquote>`

## Error Handling

### Missing Required Fields

- **No `title`**: Error, skip post
- **No `description` or `linkedinMessage`**: Auto-generate from first paragraph
- **No `linkedinArticleUrl` on update**: Generate update summary with placeholder

### Invalid Content

- **Malformed markdown**: Log error, attempt best-effort conversion
- **Broken image links**: Log warning, include in output
- **Unsupported HTML**: Strip or convert to supported tags

### File System Errors

- **Cannot create directory**: Error, halt build
- **Cannot write file**: Error, log and continue with other posts
- **Permission issues**: Error with clear message

## Validation & Testing

### Content Validation

- Ensure all generated HTML is valid
- Verify all image URLs are absolute and valid
- Check that code blocks are properly formatted
- Validate that links are not broken

### Manual Testing Checklist

1. Generate content for a simple blog post
2. Generate content for a post with images
3. Generate content for a post with code blocks
4. Generate content for a post with table of contents
5. Test update flow (regenerate after edit)
6. Verify all URLs are absolute and point to divyavanmahajan.github.io

### Automated Tests

- Unit tests for markdown → HTML conversion
- Unit tests for URL transformation
- Integration test for full content generation
- Snapshot tests for generated output

## Future Enhancements

### Potential Improvements (Out of Scope for V1)

1. **Browser automation**: Investigate Puppeteer/Playwright for fully automated posting
2. **Official API**: Monitor LinkedIn API access policies, migrate if access becomes available
3. **Analytics tracking**: Add UTM parameters to links for tracking
4. **Hashtag generation**: Auto-generate hashtags from tags/categories
5. **Image optimization**: Resize/optimize images for LinkedIn
6. **Scheduling**: Queue posts for optimal posting times
7. **Cross-platform**: Extend to other platforms (Medium, Dev.to, etc.)

## Success Criteria

The implementation will be considered successful when:

1. ✅ Blog posts with `linkedin: true` automatically generate LinkedIn content during build
2. ✅ Generated content includes both HTML and rich text formats
3. ✅ Generated post text is ready to copy and paste
4. ✅ All images use absolute divyavanmahajan.github.io URLs
5. ✅ Code blocks are properly formatted for LinkedIn
6. ✅ Table of contents is converted to plain HTML
7. ✅ Update summaries are generated for posts with existing LinkedIn URLs
8. ✅ All generated files are committed to git
9. ✅ Documentation is complete and clear
10. ✅ Manual testing confirms content pastes correctly into LinkedIn

## References

- [LinkedIn Article Publishing Guidelines](https://www.linkedin.com/help/linkedin/answer/a549082)
- [LinkedIn API Documentation](https://docs.microsoft.com/en-us/linkedin/)
- [Astro Integrations API](https://docs.astro.build/en/reference/integrations-reference/)
