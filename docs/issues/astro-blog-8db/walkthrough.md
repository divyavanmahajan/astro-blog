# Walkthrough - rsync Exclude Patterns

## Changes Made

### 1. Updated Blog Post
- **File**: `src/content/blog/2026/02/imac-disk-recovery-external-ssd-rsync.md`
- **New Section**: Added "Excluding Volatile and Cloud Data".
- **Content**: 
    - Documented the need to exclude `Library/Containers` to avoid transferring millions of tiny cache files.
    - Documented excluding `Library/Mobile Documents` to prevent iCloud sync issues.
    - Added a code block demonstrating the `--exclude` flag usage.

## Verification
- Verified markdown formatting and link consistency.
- Successful `npm run build` check.

## References
- Issue: astro-blog-8db
