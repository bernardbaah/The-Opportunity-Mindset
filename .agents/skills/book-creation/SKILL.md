---
name: book-creation
description: Complete workflow for writing, structuring, and producing a full non-fiction book for Bernard Baah — from project setup through chapter drafting, frameworks, Coonected integration, cover design, and reader export.
---

# Book Creation Skill

This skill auto-loads whenever a book project is active. It covers every phase from initial setup to final export.

---

## 1. Auto-Load Companion Files

Before doing any book work, always read these two files in full:

- `.agents/skills/book-creation/reference/author-context.md` — Bernard's voice, philosophy, platforms, and the Opportunity Flywheel
- `.agents/skills/book-creation/reference/chapter-format.md` — the exact chapter blueprint every chapter must follow

---

## 2. Project Setup

When starting a new book:

1. Create the directory structure:
   ```
   book/
     manuscript/
       part-01/
         ch-01-[slug].md
         ch-02-[slug].md
       part-02/
       ...
     frameworks/        # standalone framework explainers (Lifecycle, Equation, etc.)
     appendices/
     cover/
     exports/
   ```
2. Create `book/README.md` with: title, subtitle, author, part/chapter map, and status tracker.
3. Create `book/style-guide.md` with voice rules from `author-context.md`.

---

## 3. Chapter Drafting

Follow the exact blueprint in `chapter-format.md` for every chapter. Key rules:

- **Open with a story** — a real person, a named company, or a vivid scenario. Never open with a definition.
- **Every claim needs a reason** — no assertion without explanation or example.
- **Frameworks get their own callout box** — indented, titled, visually distinct in Markdown (use `>` blockquotes or `---` fenced sections).
- **"In Practice: Coonected" sidebar** — include only in chapters where Coonected is a natural fit (see author-context.md for the list). Never in psychology or pure evaluation chapters.
- **End every chapter** with: Summary → Quiz (3–5 questions) → Exercises (2–3 actionable) → Project (1 applied challenge) → Transition sentence to next chapter.

### Parallel drafting

When asked to write multiple chapters, dispatch independent subagents for each chapter (via the `delegation` skill) and merge results. Do not draft chapters serially if they are in different parts.

---

## 4. Signature Frameworks

The five frameworks below appear throughout the book. Each has a canonical definition — never paraphrase or alter the core formula:

| Framework | Canonical Form |
|---|---|
| Opportunity Lifecycle | Recognize → Evaluate → Create → Capture → Expand → Multiply → Share |
| Opportunity Equation | Opportunity = Need × Timing × Capability × Awareness × Action |
| Opportunity Pyramid | Survival → Stability → Growth → Influence → Transformation |
| Opportunity Compass | Purpose · Potential · Preparedness · Payoff |
| Opportunity Flywheel | Execution → Skills + Trust + Network + Resources → Greater Opportunities → repeat |

Introduce each framework the first time it appears with a full callout box. In later chapters, reference by name only.

---

## 5. Coonected Integration Rules

See `author-context.md` for the full list of strong-fit vs. weak-fit chapters.

**Always:**
- Frame Coonected as the *result* of the book's philosophy, not a product pitch
- Use the "In Practice: Coonected" sidebar format — short, boxed, at chapter end
- Let the principle come first; Coonected illustrates it

**Never:**
- Mention Coonected in the opening story of a chapter
- Describe features without connecting them to the chapter's principle
- Use promotional language ("industry-leading", "revolutionary", "game-changing")

---

## 6. Appendices

Standard appendices for every book:

- **Appendix A** — The Complete Opportunity Lifecycle (full diagram description)
- **Appendix B** — The Opportunity Equation Workbook (fill-in exercises)
- **Appendix C** — Recommended Reading
- **Appendix D** — About Coonected and the Filly Coder Ecosystem
- **Appendix E** — About the Author

---

## 7. Cover Design

When producing a cover concept:

1. Output a detailed text brief: dimensions (6×9 in, 300 dpi equivalent), front/back/spine layout, color palette, typography direction, tagline placement.
2. If image generation is available, generate the front cover using the `media-generation` skill.
3. Save to `book/cover/`.
4. Provide a download button or presentAsset link.

Cover aesthetic for Bernard's books: authoritative, clean, modern non-fiction — think HBR Press or Portfolio/Penguin. Primary palette: deep navy or charcoal + a single accent (gold, electric blue, or emerald). No stock-photo clichés.

---

## 8. Reader / Export

When the manuscript is complete:

1. Concatenate all chapter `.md` files in order into `exports/[book-slug]-full-manuscript.md`.
2. Produce a clean HTML version at `exports/[book-slug].html` with a table of contents, internal anchor links, and print-friendly CSS.
3. Present both via `presentAsset`.
4. Optionally produce a chapter-by-chapter word-count table in `book/README.md`.

---

## 9. Quality Checklist (run before marking any chapter done)

- [ ] Opens with a story, not a definition
- [ ] All five framework names used consistently (no paraphrasing)
- [ ] Coonected sidebar present only where appropriate
- [ ] Chapter ends with Summary, Quiz, Exercises, Project, Transition
- [ ] No promotional language for Coonected or Filly Coder products
- [ ] Voice matches author-context.md guidelines (direct, purposeful, grounded)
- [ ] Word count 2,500–4,000 words per chapter (flag if outside range)
