# Architecture Documentation Update Plan

## Goal
Update `docs/architecture.md` to accurately reflect the current state of the project after several major updates (TIL, Search, Mobile Styling, Content Refactoring).

## Proposed Changes

### [Architecture Document](file:///Users/divya/Documents/projects/astro-blog/docs/architecture.md)

#### 1. Project Structure
- Map `src/content/til/` and `src/pages/til/`.
- Mention `docs/{issue-number}/` folders for task documentation.

#### 2. Data Flow
- Add the `til` content collection.
- Explicitly mention the `YYYY/MM/` nesting in `src/content/blog/`.

#### 3. New Sections
- **Section 8: TIL (Today I Learned)**: Describe the purpose (quick notes), layout (sidebar tags), and separate RSS feed.
- **Section 9: Mobile-First Strategy**: Document the recent layout fixes (grid `minmax(0,1fr)`, standardized header sizes, and padding normalization).

#### 4. Styling Architecture
- Update with details about the global reset (`box-sizing`) and constrained grid columns to prevent horizontal overflow.

## Verification
- Cross-reference the documented paths and features with the actual codebase.
