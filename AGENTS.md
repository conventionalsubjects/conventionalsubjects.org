# Copilot Instructions: Conventional Subjects

## Purpose
Conventional Subjects is a specification (like Conventional Commits) for standardizing email subject lines to reduce ambiguity and cognitive load. The project is **V1.0-BETA1**: a foundational, openly adaptable template designed for any organization.

## Key Principles

**Minimalism as Safety**: Core tag set is deliberately small (4 tags). Resist adding new tags—expansion happens via optional scopes `[TAG:TYPE]`, not new bracketed tags. Every example and anti-pattern reinforces this: "If removing the tag doesn't create ambiguity, don't use one."

**One Variable per Escalation**: The escalation ladder changes only one element at a time (TAG type, or date). This prevents escalation fatigue and preserves credibility of urgent signals.

**Concrete Over Abstract**: Documentation leads with examples and anti-patterns (real mistakes to avoid), not rules. Compare good/bad subject lines directly rather than explaining theory.

## Specification Structure

1. **Purpose** — Why this exists and what problem it solves
2. **Standard Format** — Three patterns: base, scoped (context type), deadline
3. **Example Inbox Snapshot** — Real-world multi-tag example shown early to set context
4. **When NOT to Tag** — Boundaries set upfront to prevent over-application
5. **Core Tags** — The 4 approved tags + optional context types
6. **Team-Specific Tags** — Examples for Marketing, Sales, Operations, Leadership, Engineering
7. **Due Date Format** — Recommended formats (ISO 8601 preferred) + anti-patterns
8. **Anti-Patterns** — Common mistakes with bad examples
9. **Best Practices** — Concise dos with minimalism principle
10. **Escalation Ladder (Advanced)** — 5-stage progression (moved late, marked optional for beginners)
11. **Quick Reference** — One-page cheat sheet with format patterns and golden rule
12. **Getting Started** — 5-step adoption guide for organizations

## Editing Rules

**Consistency Checks Before Any Edit**:
- Every tag used in examples must be defined in Core Tags, Optional Context Types, or Team-Specific Tags
- Due-date examples must use only the "Recommended formats" list
- Urgency is expressed as `[TAG:URGENT]` context type, never tag stacking like `[URGENT ACTION]`
- Context types (like `[ACTION:REVIEW]`) must stay short and standardized
- Team-specific tags are examples only—not all teams need custom tags

**Writing Style**:
- Direct, conversational tone with emoji section headers
- Lead with examples before explanations
- Capitalize on anti-patterns: show the wrong way first, then explain why
- Summary length target: ≤60 characters (searchability principle)

**Version Strategy**:
- V1.0-BETA1 remains open to refinement before stable 1.0
- Changes that clarify ambiguities or fix inconsistencies within the current tag set are safe
- Introducing new core tags or breaking the escalation ladder requires major version bump (2.0)

## File Alignment

- **SPECIFICATION-V1.0-BETA1.md**: Source of truth for spec content
- **web/index.html**: Rendered semantic HTML version with styling
- Both must stay in sync; Markdown is editable, HTML is generated or manually mirrored

## Conventions

- Tags: `[TAG]` - uppercase, bracketed, always first in subject
- Context types: `[TAG:TYPE]` - lowercase type, short and standardized (e.g., `[ACTION:REVIEW]`)
- Dates: `| Due Mar 15` or `| Due 2026-03-15` (ISO for global teams)
- No abbreviations or shortcuts in core examples (keep them explicit for clarity)
- Escalation uses context-style urgency: `[ACTION:URGENT]` not `[URGENT ACTION]`

## Git & Commits

- Use [Conventional Commits](https://www.conventionalcommits.org/)
- Examples:
  - `docs: clarify tag stacking guidance`
  - `fix: align due-date examples to recommended formats`
  - `feat: add context type for new organizational pattern`

---

**TL;DR for Agents**: This is a minimalist spec that resists feature creep. Every edit should reinforce the principle: "less is more." When in doubt, remove rather than add.
