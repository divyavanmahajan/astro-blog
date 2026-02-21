# Implementation Plan - rsync Exclude Patterns

## 1. Update Blog Content
- Edit `src/content/blog/2026/02/imac-disk-recovery-external-ssd-rsync.md`.
- Add a new sub-section "Excluding Volatile and Cloud Data".
- Explain why `Library/Containers` and `Library/Mobile Documents` should be excluded.
- Provide a code snippet showing the `--exclude` syntax.

## 2. Review and Verification
- Ensure the paths are accurate.
- Run `npm run build` to verify the site generation.

## 3. Finalize
- Create walkthrough.
- Commit, close issue, and push.
