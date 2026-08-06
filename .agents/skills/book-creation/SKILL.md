---
name: book-creation
description: Complete workflow for writing, structuring, and producing a full non-fiction book for Bernard Baah — from project setup through chapter drafting, frameworks, Coonected integration, cover design, and reader export.
---

# Book Creation Skill

This skill auto-loads whenever a book project is active. Read `reference/author-context.md` and `reference/chapter-format.md` in full before writing any content.

---

## Phase 1 — Setup

### File Structure

Create everything inside a `book/` directory:

```
book/
  index.html              ← Book reader UI
  cover/
    index.html            ← Cover A (primary, dark/navy)
    index_variant2.html   ← Cover B
    index_variant3.html   ← Cover C
  00_outline.md
  01_preface.md
  02_introduction.md
  03_about.md
  04_chapter01.md
  05_chapter02.md
  ...                     ← 2-digit zero-padded prefix on every file
  NN_conclusion.md
  NN_appendix_a.md  through  NN_appendix_f.md
  NN_bonus_resources.md
```

Every file uses a 2-digit zero-padded numeric prefix. The `CHAPTERS` array in `index.html` must exactly match the files written to disk.

### Workflow

Set up a single workflow named **"Book Reader"** running:

```
python3 -m http.server 5000 --directory book
```

Port 5000 → external port 80. Output type: webview. Use the workflows skill to configure this.

### Book Reader (`book/index.html`)

A self-contained HTML file that:

- Fetches and renders all `.md` files using **marked.js** (CDN)
- Has a fixed left sidebar with part/chapter navigation and a search box
- Uses navy `#0a1628` + gold `#c9a84c` color scheme
- Has Previous / Next buttons in a top bar
- Shows a gold progress bar at the top of the viewport
- Supports keyboard navigation (← → arrow keys)
- Renders all markdown: blockquotes, tables, images, code blocks
- The `CHAPTERS` array must exactly match actual files on disk

---

## Phase 2 — Front Matter (write all four in parallel)

| File | Contents |
|---|---|
| `00_outline.md` | Full TOC — all part titles, chapter titles, brief descriptions |
| `01_preface.md` | ~1,500 words — why this book, why now, who it's for |
| `02_introduction.md` | Sets up the book's central argument and structure |
| `03_about.md` | About the book + full author bio |

---

## Phase 3 — Chapters (write in parallel batches of 3–4)

See `reference/chapter-format.md` for the exact blueprint. Every chapter must contain:

**A. Opening**
- Two epigraphs: one famous quote + one original quote attributed to Bernard Baah
- Vivid real-world story (300–500 words): named person or company, specific facts, globally diverse

**B. Body**
- 5–8 main `##` sections; sub-sections use `###`
- 5+ Pexels image embeds (exact format in chapter-format.md)
- 2+ markdown tables comparing frameworks, data, or options
- 1+ ASCII/text diagram or structured framework visualization
- 2 case studies per chapter (`## Case Study: Name`) — real outcomes, real companies
- Examples from Africa, Asia, Latin America — not only US/Europe

**C. End Matter (required on EVERY chapter, no exceptions)**
- `## Chapter Summary` — 6–8 bold-term bullets
- `## End-of-Chapter Quiz` — 10 questions, multiple choice with one ✓ per question
- `## Exercises` — 4 exercises (individual, research, hands-on, synthesis)
- `## Projects` — 2–3 projects that produce something shareable
- Transition sentence: *"In the next chapter, we [specific preview]."*

Chapter length: ~3,000–5,000 words body + ~1,500 words end matter

---

## Phase 4 — Back Matter (write in parallel after all chapters)

| File | Contents |
|---|---|
| `NN_conclusion.md` | 1,500–2,000 words — synthesis, call to action, final vision. Give it a memorable title. |
| `NN_appendix_a.md` | Categorized tools directory — 10 categories × 10 tools, with pricing notes |
| `NN_appendix_b.md` | Step-by-step practitioner guide relevant to the book's topic |
| `NN_appendix_c.md` | Skills framework — layered stack from beginner to expert |
| `NN_appendix_d.md` | Self-assessment / readiness tool (individual, organizational, community) |
| `NN_appendix_e.md` | Global resources directory — international orgs, regional bodies, learning platforms |
| `NN_appendix_f.md` | Glossary A–Z — plain-language definitions of 60+ key terms |
| `NN_bonus_resources.md` | 100 ideas, personal workbook, canvas, scorecard, recommended reading |

---

## Phase 5 — Book Covers (three variants in `book/cover/`)

Each HTML cover file:

- 8.5 × 11 in viewport with CSS scaling
- Contains: title, "Bernard Baah" author credit, "Filly Coder · AI Future Series" tagline
- Download button using **html2canvas** that exports at 2550 × 3300px (KDP ready)
- Three visual variants: dark/navy primary + 2 alternatives

No volume numbers. No publisher imprint. KDP trim size: 8.5 × 11 inches.

---

## Signature Frameworks

Use these exact canonical forms — never paraphrase:

| Framework | Canonical Form |
|---|---|
| **Opportunity Flywheel** | Discover → Learn → Build → Connect → Create → Reinvest |
| **Opportunity Lifecycle** | Recognize → Evaluate → Create → Capture → Expand → Multiply → Share |
| **Opportunity Equation** | Opportunity = Need × Timing × Capability × Awareness × Action |
| **Opportunity Pyramid** | Survival → Stability → Growth → Influence → Transformation |
| **Opportunity Compass** | Purpose · Potential · Preparedness · Payoff |

The **Opportunity Flywheel** is Bernard's signature framework — reference it explicitly early in the book, then use it as a recurring lens throughout.

---

## Coonected Integration Rules

See `reference/author-context.md` for chapter-level fit guidance.

- Treat Coonected, Filly Jobs, Filly Learning, etc. the same as Coursera or LinkedIn — natural case study references, never promotional
- Use the **"In Practice: Coonected"** sidebar at the end of strong-fit chapters
- Never mention in opening stories or psychology/evaluation chapters
- Platforms are illustrations of principles; the frameworks are the star

---

## Core Themes (weave through every chapter)

1. AI augments human intelligence — it doesn't replace it
2. Talent is evenly distributed; opportunity is not — fix this
3. Access > ownership
4. AI reduces barriers to education, entrepreneurship, employment, and wealth
5. The future belongs to continuous learners
6. Technology should create inclusive prosperity, not widen inequality
7. Networks create opportunities; AI strengthens networks at scale

---

## Completion Checklist

Before declaring the book done, verify:

- [ ] Every chapter has all end-matter (summary + quiz + exercises + projects + transition sentence)
- [ ] Every chapter has ≥ 5 Pexels image embeds
- [ ] Book reader `CHAPTERS` array matches actual files on disk
- [ ] Conclusion references the book's central framework
- [ ] All 6 appendices + bonus resources are written
- [ ] Three cover variants exist in `book/cover/`
- [ ] "Book Reader" workflow is running; preview shows the full book

---

## Writing Voice

| Guideline | Rule |
|---|---|
| Tone | Optimistic but not unrealistic |
| Approach | Evidence-based and accessible |
| Register | Inspirational, never promotional |
| Utility | Practical — actionable frameworks throughout |
| Geography | Global; include Africa, Asia, Latin America in every chapter |
| Time horizon | Long-term trends, not short-term hype |
| Audience | Entrepreneurs, educators, policymakers, leaders, investors, students |

**On AI:** Not a magic fix-all, not an existential threat. A powerful general-purpose technology whose impact depends on how it is designed, governed, and applied.
