# Contributing to Conventional Subjects

Thanks for your interest in improving the spec. This document explains how to contribute and documents the reasoning behind key decisions — so we don't relitigate closed questions and so you can make informed suggestions.

## How to Contribute

- **Bug reports and suggestions**: Open a GitHub issue
- **Changes to the spec**: Open an issue first to discuss before submitting a PR — spec changes affect anyone who has adopted it
- **Site-only fixes** (typos, formatting, broken markup): PRs are welcome without a prior issue

## Key Decisions and Rationale

### Due dates stay outside the brackets

Format: `[ACTION] Summary | Due Mar 15` — not `[ACTION | Due Mar 15]`

The brackets define the tag. Putting a date inside them makes the tag variable, which breaks filterability: searching for `[ACTION]` would no longer consistently match all action emails regardless of whether they have a deadline. The `| Due` suffix is its own searchable pattern and keeps the two concerns independent.

### Tag stacking is an anti-pattern

`[ACTION][REMINDER]` is explicitly discouraged. One tag per subject, always. If you need to signal urgency, use a context type: `[ACTION:URGENT]`. The escalation ladder handles progressive urgency through tag and deadline changes across separate emails — not by combining tags in a single subject.

### `:TYPE` is always ALL CAPS

Both action qualifiers (`[ACTION:REVIEW]`) and topic scopes (`[UPDATE:PLATFORM]`) use ALL CAPS. A single casing rule is simpler than distinguishing between qualifier types at write time. It also keeps everything inside `[]` visually consistent.

### Topic scopes are team-defined, not from a fixed list

Action qualifiers (REVIEW, DECISION, APPROVAL) come from a known vocabulary because they describe a finite set of things a recipient might need to do. Topic scopes (PLATFORM, FINANCE, SECURITY) describe what an email is about, which varies by organization. Prescribing them would make the spec less portable.

### The core tag list is intentionally small

Four tags: `[ACTION]`, `[REMINDER]`, `[FYI]`, `[UPDATE]`. The value of the system comes from everyone using the same tags. Every tag added increases the surface area people have to learn and the chance of inconsistent use. If you feel something is missing, consider whether a context type or a topic scope covers the need first.

## What's Out of Scope

- Adding new core tags (the list is fixed by design)
- Prescribing specific topic scope vocabularies (these belong to each organization)
- Formatting rules for email body content (the spec covers subjects only)
