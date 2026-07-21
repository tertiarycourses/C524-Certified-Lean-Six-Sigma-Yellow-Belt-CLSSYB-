# non-wsq-courseware-gen

Use `non-wsq-courseware-build`. Generate the PPT, Learner Guide, Lesson Plan and connected labs, run the generator, then invoke `non-wsq-courseware-qa`. Never modify WSQ-prefixed or unprefixed shared tooling.

## Concept-first, NOT lab-focused

The deck and Learner Guide are **knowledge products first**. Labs practise the
knowledge; they never replace it. A deck that is mostly lab step slides is a
build failure — regenerate it.

1. **Do deep research before authoring.** For every topic/domain, research the
   subject properly (web search, authoritative references, standard texts of
   the discipline) and distil the actual body of knowledge: definitions,
   principles, models, formulas, worked examples, history/context, common
   mistakes, and how practitioners really use each tool. Never author concept
   slides from the lab steps alone.
2. **Teach the concept before every lab — with visuals.** Every lab block must
   be preceded by a full concept section that explains the theory the lab
   practises: what the tool/idea is, why it exists, how it works, a worked
   example, and when/when not to use it. Each concept section needs at least
   one visual — a flow diagram, framework graphic, annotated worked example,
   comparison table, or asset image — not just bullet text. A lab appearing
   with no preceding concept section is a QA failure.
3. **Keep a concept-heavy slide ratio.** Concept/knowledge slides should
   clearly outnumber lab-step slides (aim ≥ 60% concept). Lab slides in the
   deck cover the objective, context and key steps — the fine-grained
   click-by-click detail lives in the `labs/*.md` files, not the deck.
4. **Never explain a lab in one-liners.** Wherever a lab is introduced (deck
   lab-overview slide, LG, LP, labs README), explain it in full sentences and
   short paragraphs: what the learner will build, which concepts it applies,
   why it matters in practice, and what the finished outcome looks like.
   A bare one-line title or a single-sentence description is not acceptable.
5. **Concept depth in the Learner Guide.** The LG mirrors the deck: each topic
   gets a proper explanatory write-up (multi-paragraph prose with the visuals
   referenced), followed by the lab activity. The LG must read as a
   self-contained study text, not a lab manual.

## Mirror the WSQ courseware when one exists

If the course has a **WSQ counterpart** (a `TGS-*` repo for the same subject),
mirror it rather than authoring from scratch. The non-WSQ course is the same
course minus the funding/compliance layer — it must not be a thinner course.

1. **Locate the WSQ source.** Look for a sibling `TGS-*` repo of the same
   subject (same course title / certification). If none exists, author normally
   from the course outline and skip the rest of this section.
2. **Mirror the structure 1:1** — the same labs (same count, same order, same
   titles), the same topic/domain spine, the same slide sections, the same LG
   depth and LP schedule shape, and the same `courseware/assets/`. Do not
   consolidate, drop or re-scope labs to make the course smaller. In
   particular, carry over **all** the WSQ deck's concept/knowledge slides —
   they are the core of the course.
3. **Then strip the WSQ layer.** Remove every funded-course element:

   | Strip | Replace with |
   |---|---|
   | Written Assessment, PP, case study, marking guides | nothing — non-WSQ has **no assessment** |
   | "Briefing for Assessment" + "Assessment Flow" slides | the **How You'll Learn** flow |
   | TRAQOM survey slides | nothing |
   | Digital attendance (AM/PM/Assessment QR) slides | nothing |
   | 75% attendance rule, funding/subsidy/SkillsFuture/SSG text | nothing |
   | WSQ Skills Framework / TSC code slides | nothing |
   | `TGS-` course reference on covers/footers | the plain non-WSQ code (e.g. `C913`) |
   | Assessment time in the LP schedule | reallocated to lab/practice time |
   | "open book / assessment" wording in portal, schedule, wrap-up, checklist slides | learning/practice wording |

4. **Reallocate, don't shrink.** Time freed by removing assessment and admin
   blocks goes back into hands-on lab and recap time, so each training day
   still totals its full instructional hours.
5. **Verify with `non-wsq-courseware-qa`**, which fails the build on any leaked
   WSQ/SSG/TRAQOM/attendance/assessment content — and also flags a deck that
   is lab-step-dominated or has labs with no preceding concept section.
