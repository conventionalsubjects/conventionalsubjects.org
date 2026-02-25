# Conventional Subjects V1.0-BETA1

*Clear, predictable communication for your email subject lines*

---

## 🎯 Purpose

Conventional Subjects makes emails:

* Easier to scan
* Easier to filter
* Clear about intent
* Trustworthy about urgency

It is designed to reduce ambiguity — not add bureaucracy. It is also *not* a substitute for well-structured emails that properly convey context and intent.

The Conventional Subjects specification is designed to be a starting point, and can be used as-is, or remixed and adapted to suit particular nuances of your organization.

---

## 🧱 Standard Format

**Base**
`[TAG] Short summary`

```
[ACTION] Approve Q2 vendor contract
```

**Optional Context**
`[TAG:TYPE] Short summary`

```
[UPDATE:platform] Migration 80% complete
```

**Optional Deadline (actionable items only)**
`[TAG] Short summary | Due DATE`

```
[ACTION] Feedback on onboarding checklist | Due Mar 22
```

---

## 🏢 Example Inbox Snapshot

```
[ACTION] Approve 2026 marketing budget | Due Mar 15
[ACTION:REVIEW] Review lease compliance memo | Due Mar 22
[UPDATE:platform] Payments migration 90% complete
[FYI] Office closed Monday
[REMINDER] Security training | Due Mar 20
[UPDATE] Vendor selection finalized
```

**Core Principle**
Conventional Subjects should reduce cognitive load. If it feels heavy, simplify it.

---

## 🛑 When NOT to Tag

Do not tag:

* Casual 1:1 messages
* Active thread replies (unless updating the subject for escalation)
* Calendar invites
* Very small audiences
* Sensitive/emotional topics
* Micro-updates

**Rule of thumb**
If removing the tag does not create ambiguity, don't use one.

---

## 🧭 Core Tags 

This list of core tags has been kept small on purpose. These four tags form the core of Conventional Subjects:

[ACTION] [REMINDER] [FYI] [UPDATE]

There might be a tendency to keep adding more and more tags, but if you get to the point where you need a secret decoder ring to figure out your tagging system, you probably have too many (see optional tags below).

Conventional Subjects suggests the following tags as a starting point, separated into two different categories: 1) Things you are asking of others, and 2) Information you are sharing.

### Things you are asking of others:

**[ACTION]**
You are requesting that the recipient do something.

**[REMINDER]**
Follow-up on prior communication.

**Optional context with actions**

You can specify what kind of action by adding a context type: `[ACTION:TYPE]`.

Common types:

**[ACTION:DECISION]** — A decision is needed

**[ACTION:REVIEW]** — Review is needed

**[ACTION:APPROVAL]** — Approval is needed

**[REMINDER:URGENT]** — Urgent reminder, usually only used in the event of multiple escalations (see escalation ladder below).

Note: Good subject lines often don't need context added. Compare these two examples:

[ACTION] Review new Policies & Procedures
[ACTION:REVIEW] New Policies & Procedures

Some of this will come down to style preference, but less should be more when it comes to use of tags. Your organization should agree and remain consistent in its use of context types.

### Things you are sharing with others (that don't require action):

**[FYI]**
Awareness only.

**[UPDATE]**
You are sharing a status or progress update.


### 🛠 Optional Tags

Optional tags may be used outside of the core tags where they provide meaning, relevant information to your organization or team. For example, software engineering teams may find the following tags useful:

```
[RFC]
[POSTMORTEM]
[ISSUE]
[FIX]
```

---

## 📅 Due Date Format

Include deadlines only when:

* A real deadline exists
* Missing it has consequences
* It is not already handled via calendar invite

### Recommended formats

```
| Due Mar 15
| Due Fri 3/15
| Due 2026-03-15   (best for global teams)
```

Examples:

```
[ACTION] Review new Policies & Procedures | Due Mar 15
[ACTION:APPROVAL] Please review and approve comps for marketing campaign | Due 2026-03-15
```

### Avoid

```
ASAP
Due 3/4   (ambiguous internationally)
```

---

## 📈 Deadline Escalation Ladder (Advanced)

⚠️ **New to Conventional Subjects?** You can skip this section and come back later.

Deadlines escalate gradually and predictably.

### Stage 1 — Initial Assignment

```
[ACTION] Submit compliance report | Due Mar 15
```

Neutral tone. Clear deadline.

### Stage 2 — Reminder (3–5 days prior)

```
[REMINDER] Submit compliance report | Due Mar 15
```

Do not escalate urgency prematurely.

### Stage 3 — Due Soon (1–2 days prior)

```
[ACTION:URGENT] Submit compliance report | Due Mar 15
```

Escalate only if necessary.

### Stage 4 — Due Today

```
[ACTION:URGENT] Submit compliance report | Due Mar 15
```

No emotional language. No punctuation escalation.

### ⚫ Stage 5 — Overdue

```
[ACTION] Submit compliance report | Overdue
```

Use formal escalation only if it is required.

### Escalation Principles

* Escalate gradually
* Change only one variable at a time
* Preserve credibility of urgent tags
* Don't over-escalate within the same thread
* If subject escalation isn't working, escalate via conversation

---

## 🚫 Anti-Patterns

Avoid these common mistakes:

**❌ Tag stacking**

```
[ACTION][REMINDER]
```

Use one tag. Add urgency as a context type when needed (for example, `[ACTION:URGENT]`).

**❌ Hiding action inside [FYI]**

If someone must act, use `[ACTION]`.

**❌ Vague summaries**

```
[ACTION] Quick question
```

Be specific so subjects stand alone in search results.

**❌ Inventing new tags**

Stick to the approved list to preserve filterability.

**❌ Emotional formatting**

```
[CRITICAL!!!]
```

Stay calm and structured. Avoid punctuation escalation.

**❌ Over-scoping**

```
[UPDATE:finance-billing-ops-integration]
```

Keep scopes short and standardized.

---

## 🧠 Best Practices

* Tags are ALL CAPS
* Always bracketed
* Always first
* Keep summaries concise (≤ 60 characters when possible)
* Keep the approved tag list small
* Use urgency sparingly

---

> **Tip:** In most email clients you can search for `[ACTION]` or `| Due` to quickly find what needs attention.