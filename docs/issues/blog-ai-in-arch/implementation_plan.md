# Implementation Plan: AI in Architecture Blog Series

1. **Understand Initial Requirements**
   - User requested a blog series starting with a post about "Building Knowledge Graphs", SAP LeanIX, Neo4j, and LLM reasoning.
   - Identified the need to comply with local `/create-blog` workflow.

2. **Drafting Post 1**
   - **Path**: `src/content/blog/2026/04/accelerating-enterprise-architecture-knowledge-graphs-llm.md`
   - **Focus**: Introduction to Knowledge Graphs, LeanIX structure, and Neo4j integration concept.
   - **Frontmatter**: `draft: false`, category: AI, series: ai_in_arch.

3. **Drafting Post 2**
   - **Path**: `src/content/blog/2026/04/building-the-leanix-neo4j-integration.md`
   - **Focus**: Practical guide on using `uvx dvm-leanix`, mapping relations, and loading data using idempotent Cypher `MERGE` scripts.
   - **Frontmatter**: `draft: true`, matching categories and series tags.

4. **Drafting Post 3**
   - **Path**: `src/content/blog/2026/04/connecting-neo4j-to-ai-agents-with-mcp.md`
   - **Focus**: The culmination of the series, showing how to connect Neo4j to Copilot/Claude using the Model Context Protocol.
   - **Frontmatter**: `draft: true`, matching categories and series tags.

5. **Completion and Commits**
   - Added these docs (task, plan, walkthrough).
   - Ensure `git pull --rebase` and `git push` are run at completion per project guidelines.
