# Book Creation Instructions
## Bernard Baah / Filly Coder · AI Future Series

Copy and paste this entire block into a Replit chat when starting a new book, then follow it with: **"Book title: [your title]. Here is the table of contents: [paste]"**

The agent will work through all phases without stopping between them.

---

## The Message to Paste

```
The table of contents I shared is for this book. Begin building it immediately
following all instructions below — do not confirm, do not wait.

Book title: [YOUR TITLE HERE]
Subtitle:   [YOUR SUBTITLE HERE]
Author: Bernard Baah
Series tagline: Filly Coder · AI Future Series

Start with Phase 1 (file structure + workflow + book reader), then Phase 2
(front matter), then write chapters in parallel batches of 3–4.
Do not stop between phases.
```

---

## What the Agent Will Do

### Phase 1 — Setup

**File structure inside `book/`:**
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

**Workflow:** "Book Reader" running `python3 -m http.server 5000 --directory book`

**Book reader (`book/index.html`):**
- Fetches and renders all `.md` files using marked.js (CDN)
- Fixed left sidebar with navigation + search
- Navy `#0a1628` + gold `#c9a84c` color scheme
- Previous / Next buttons, gold progress bar, keyboard navigation (← →)

---

### Phase 2 — Front Matter (written in parallel)

| File | Contents |
|---|---|
| `00_outline.md` | Full TOC with part titles, chapter titles, brief descriptions |
| `01_preface.md` | ~1,500 words — why this book, why now, who it's for |
| `02_introduction.md` | Central argument and book structure |
| `03_about.md` | About the book + full author bio |

---

### Phase 3 — Chapters (parallel batches of 3–4)

**Every chapter contains:**

**A. Opening**
- Two epigraphs: one famous quote + one original quote attributed to Bernard Baah
- Vivid real-world story (300–500 words): named person/company, specific facts, globally diverse

**B. Body (3,000–5,000 words)**
- 5–8 `##` sections; sub-sections use `###`
- ≥ 5 Pexels image embeds (exact format below)
- ≥ 2 markdown tables (framework comparisons, data, options)
- ≥ 1 ASCII/text diagram or framework visualization
- 2 case studies (`## Case Study: Name`) — real outcomes, at least one non-US/European
- Examples from Africa, Asia, Latin America — not only US/Europe
- "In Practice: Coonected" sidebar where contextually appropriate

**Pexels image format (exact):**
```
![Alt text](https://images.pexels.com/photos/PHOTO_ID/pexels-photo-PHOTO_ID.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)
*Figure N.X: Caption. (Source: Pexels)*
```

**C. End Matter (~1,500 words — required on every chapter)**

```markdown
## Chapter Summary
- **Bold term** — one-sentence takeaway [6–8 bullets]

## End-of-Chapter Quiz
**1.** Question
- a) Option
- b) Option
- c) Correct answer ✓
- d) Option
[10 questions total, one ✓ per question]

## Exercises
**Exercise N.1 — Title** [individual/reflective]
**Exercise N.2 — Title** [research/comparative]
**Exercise N.3 — Title** [hands-on/practical]
**Exercise N.4 — Title** [synthesis/debate]

## Projects
**Project N.1 — Title** [produces something shareable]
**Project N.2 — Title**
[optional Project N.3]

*In the next chapter, we [specific preview of Chapter N+1].*
```

---

### Phase 4 — Back Matter (parallel, after all chapters)

| File | Contents |
|---|---|
| `NN_conclusion.md` | 1,500–2,000 words — synthesis, call to action, memorable title |
| `NN_appendix_a.md` | Tools directory — 10 categories × 10 tools, pricing notes |
| `NN_appendix_b.md` | Step-by-step practitioner guide |
| `NN_appendix_c.md` | Skills framework — beginner to expert |
| `NN_appendix_d.md` | Self-assessment / readiness tool |
| `NN_appendix_e.md` | Global resources directory |
| `NN_appendix_f.md` | Glossary A–Z — 60+ key terms |
| `NN_bonus_resources.md` | 100 ideas, workbook, canvas, scorecard, reading list |

---

### Phase 5 — Book Covers (3 variants in `book/cover/`)

Each HTML cover:
- 8.5 × 11 in viewport with CSS scaling
- Title + "Bernard Baah" + "Filly Coder · AI Future Series" tagline
- Download button using html2canvas at 2550 × 3300px (KDP ready)
- Three variants: dark/navy primary + 2 alternatives

---

## Signature Frameworks (canonical — never paraphrase)

| Framework | Formula |
|---|---|
| **Opportunity Flywheel** *(signature)* | Discover → Learn → Build → Connect → Create → Reinvest |
| **Opportunity Lifecycle** | Recognize → Evaluate → Create → Capture → Expand → Multiply → Share |
| **Opportunity Equation** | Opportunity = Need × Timing × Capability × Awareness × Action |
| **Opportunity Pyramid** | Survival → Stability → Growth → Influence → Transformation |
| **Opportunity Compass** | Purpose · Potential · Preparedness · Payoff |

The Opportunity Flywheel is the primary framework — introduce it early, reference throughout.

---

## Filly Coder Platforms (natural case studies — not promotional)

| Platform | Purpose |
|---|---|
| **Coonected** | Flagship Global Progress Network — AI-powered ecosystem for jobs, mentors, investors, courses, communities |
| **Filly Jobs** | AI-powered employment & career platform |
| **Filly Learning** | AI-powered lifelong learning / courses |
| **Filly Tutor** | Global tutoring marketplace with AI matching |
| **Filly Edu** | School management platform |
| **Filly HR** | HR management with AI insights |

Treat these the same as Coursera or LinkedIn. Never promotional.

---

## Core Themes (woven through every chapter)

1. AI augments human intelligence — it doesn't replace it
2. Talent is evenly distributed; opportunity is not — fix this
3. Access > ownership
4. AI reduces barriers to education, entrepreneurship, employment, and wealth
5. The future belongs to continuous learners
6. Technology should create inclusive prosperity, not widen inequality
7. Networks create opportunities; AI strengthens networks at scale

**On AI:** Not a magic fix-all, not an existential threat. A powerful general-purpose technology whose impact depends on how it is designed, governed, and applied.

---

## Writing Voice

| | |
|---|---|
| Tone | Optimistic but not unrealistic |
| Approach | Evidence-based and accessible |
| Register | Inspirational, never promotional |
| Utility | Practical — actionable frameworks throughout |
| Geography | Global; Africa, Asia, Latin America in every chapter |
| Audience | Entrepreneurs, educators, policymakers, leaders, investors, students |

---

## Completion Checklist

- [ ] Every chapter has all end-matter (summary + quiz + exercises + projects + transition)
- [ ] Every chapter has ≥ 5 Pexels image embeds
- [ ] Book reader `CHAPTERS` array matches actual files on disk
- [ ] Conclusion references the book's central framework
- [ ] All 6 appendices + bonus resources written
- [ ] Three cover variants in `book/cover/`
- [ ] "Book Reader" workflow running; preview shows full book

---

*Skill files: `.agents/skills/book-creation/` — auto-load in every session on this project.*
*AI Future Series — Bernard Baah / Filly Coder*
