# Implementation Plan - Split AI Agent Trust blog post

## Proposed Changes

### Content Management
1.  **Trim `ai-agent-trust-observability.md`**:
    *   Keep Intro, "AI Agent Observability and Governance", and "Enterprise AI Use Cases Beyond Development".
    *   Remove moved sections.
    *   Add "The AI Agent Roadmap" section with links to other parts.

2.  **Create `ai-adoption-software-development-teams.md`**:
    *   Extract content from the original post.
    *   Set frontmatter: `series: "ai_agents-004"`, `heroImage: "/images/ai-agent-trust-observability-hero.png"`.

3.  **Create `ai-observability-platform-persona-prd.md`**:
    *   Extract content (Persona and PRD) from original post.
    *   Set frontmatter: `series: "ai_agents-005"`, `heroImage: "/images/ai-agent-trust-observability-hero.png"`.

4.  **Create `shadow-ai-agents-automation-debt.md`**:
    *   Expand from TIL `shadow-ai-agents-automation-debt.md` and Dataiku research in `experiments/shadow-ai-agent-risk-dataiku.md`.
    *   Set frontmatter: `series: "ai_agents-006"`, `heroImage: "/images/ai-agent-trust-observability-hero.png"`.

### Verification Plan
*   Run `npm run build` to ensure all posts are correctly generated and the series indices update.
*   Verify links between posts are correct.
