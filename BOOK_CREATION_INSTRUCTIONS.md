# Book Creation Instructions
## For use with Replit Agent — Bernard Baah / Filly Coder

Paste this file (or its contents) as your first message in a new Replit session, then follow it with your book title and table of contents. The agent will handle the rest.

---

## Step 1 — Start a new Replit project

Open a fresh Replit project. The skill files in `.agents/skills/book-creation/` will auto-load, giving the agent your voice, format, and Coonected integration rules without you having to re-explain anything.

---

## Step 2 — Paste this message into the chat

```
I'm writing a book. Here are the details:

Book title: [YOUR TITLE HERE]
Subtitle: [YOUR SUBTITLE HERE]

Here is the table of contents:

[PASTE YOUR FULL TABLE OF CONTENTS HERE — parts, chapters, and subpoints]

Please:
1. Set up the full project file structure
2. Write all chapters in parallel using the standard chapter format
3. Apply the Coonected "In Practice" sidebar to appropriate chapters only
4. Use the Opportunity Lifecycle, Equation, Pyramid, Compass, and Flywheel frameworks where they fit
5. Produce a complete HTML reader with table of contents and a cover download button when done
```

---

## What the Agent Will Do Automatically

### Project Setup
- Creates `book/manuscript/part-XX/ch-XX-[slug].md` for every chapter
- Creates `book/README.md` with title, structure map, and chapter status tracker
- Creates `book/style-guide.md` with voice and tone rules

### Chapter Format (every chapter)
Each chapter follows this exact structure:
1. **Opening story** — a real person or scenario that embodies the chapter's idea (never a definition)
2. **Chapter introduction** — names the concept and states the core argument
3. **Body sections** — 3–5 headed sections with examples, reasoning, and framework callouts
4. **"In Practice: Coonected" sidebar** — only in chapters where it fits naturally (see below)
5. **Summary** — restates the argument + 3–5 key takeaways
6. **Quiz** — 5 questions (recall → application → synthesis)
7. **Exercises** — 2–3 actionable exercises
8. **Project** — 1 applied challenge with clear deliverable
9. **Transition sentence** — hooks the reader into the next chapter

Target: **2,700–4,200 words per chapter**

### Signature Frameworks
The agent knows these exact definitions and will use them consistently:

| Framework | Formula |
|---|---|
| Opportunity Lifecycle | Recognize → Evaluate → Create → Capture → Expand → Multiply → Share |
| Opportunity Equation | Opportunity = Need × Timing × Capability × Awareness × Action |
| Opportunity Pyramid | Survival → Stability → Growth → Influence → Transformation |
| Opportunity Compass | Purpose · Potential · Preparedness · Payoff |
| Opportunity Flywheel | Execution → Skills + Trust + Network + Resources → Greater Opportunities → repeat |

### Coonected Integration
The agent knows exactly where Coonected belongs and where it doesn't:

**Natural fits (sidebar included):**
- Ch 10 — Engineering Opportunity / Building platforms
- Ch 11 — Opportunity through relationships
- Ch 20 — Building Opportunity Systems
- Ch 21 — Becoming an Opportunity Magnet
- Ch 29 — AI and the Opportunity Explosion
- Ch 30 — Creating Opportunity at Scale

**Not used in:** psychology chapters (1–4) or risk/evaluation chapters (13–15)

### Appendices (auto-generated)
- A — The Complete Opportunity Lifecycle
- B — The Opportunity Equation Workbook
- C — Recommended Reading
- D — About Coonected and the Filly Coder Ecosystem
- E — About the Author

### Final Export
- Full manuscript as a single `.md` file
- Clean HTML reader with table of contents and internal navigation
- Cover design brief + generated cover image
- Download button for all exports

---

## Your Voice (pre-loaded — no need to repeat)

The agent already knows:
- You are **Bernard Baah**, Founder & CEO of Filly Coder
- Your core belief: success is determined by how well people recognize, create, and capture opportunity
- Your writing style: direct, grounded in examples, optimistic but honest — between Gladwell and Christensen
- What to avoid: clichés, promotional language, opening chapters with definitions
- Your philosophy: technology should expand human potential and democratize opportunity

---

## About Coonected (pre-loaded — no need to repeat)

The agent knows Coonected is:
- An AI-powered **Progress Network** (not a social network)
- Designed to help people make measurable progress through opportunity
- To be referenced as an **illustration of principles**, never a product pitch
- Featured via the **"In Practice: Coonected"** sidebar format in appropriate chapters only

---

## Tips

- **To write a single chapter:** "Write Chapter 5 in full."
- **To write all chapters in a part:** "Write all chapters in Part III in parallel."
- **To regenerate a section:** "Rewrite the opening story for Chapter 8 — make it set in Africa or Southeast Asia."
- **To check consistency:** "Review all Coonected sidebars across the manuscript and flag any that feel promotional."
- **To export:** "Produce the full HTML reader and cover for the book."

---

*This file is part of the Filly Coder / Bernard Baah book creation system. Skill files live in `.agents/skills/book-creation/`.*
