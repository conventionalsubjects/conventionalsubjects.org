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
3. **Core Tags** — The 4 approved tags + optional context types
4. **Due Date Format** — Recommended formats (ISO 8601 preferred) + anti-patterns
5. **Escalation Ladder** — 5-stage progression with principles
6. **Anti-Patterns** — Common mistakes with bad examples
7. **Best Practices** — Concise dos
8. **Inbox Snapshot** — Real-world multi-tag example

## Editing Rules

**Consistency Checks Before Any Edit**:
- Every tag used in examples must be defined in Core Tags or Optional Context Types
- Due-date examples must use only the "Recommended formats" list
- Urgency is expressed as `[TAG:URGENT]` context type, never tag stacking like `[URGENT ACTION]`
- Scopes must stay short and standardized (reject lengthy scopes like `[UPDATE:finance-billing-ops-integration]`)

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
- Scopes: `[TAG:TYPE]` - lowercase type, short and standardized
- Dates: `| Due Mar 15` or `| Due 2026-03-15` (ISO for global teams)
- No abbreviations or shortcuts in core examples (keep them explicit for clarity)

## Git & Commits

- Use [Conventional Commits](https://www.conventionalcommits.org/)
- Examples:
  - `docs: clarify tag stacking guidance`
  - `fix: align due-date examples to recommended formats`
  - `feat: add context type for new organizational pattern`

---

**TL;DR for Agents**: This is a minimalist spec that resists feature creep. Every edit should reinforce the principle: "less is more." When in doubt, remove rather than add.
