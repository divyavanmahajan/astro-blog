# Implementation Plan - Add pubDate to Recent Posts in Sidebar

## 1. Modify Component
- Edit `src/components/Sidebar.astro`.
- Update the mapping of `posts` in the "Recent Posts" widget.
- Add a new `<span>` or `<small>` element for the date.
- Style the date to be subtle and placed below or next to the title.

## 2. Review and Verification
- Run `npm run dev` or `npm run build` to check the layout.
- Ensure the date is formatted correctly.

## 3. Finalize
- Create walkthrough.
- Commit, close issue, and push.
