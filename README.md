# C524 Certified Lean Six Sigma Yellow Belt (CLSSYB)

Complete courseware for the Tertiary Infotech Academy **Certified Lean Six Sigma Yellow Belt** short course — a 2-day, hands-on programme that follows the DMAIC roadmap end to end using one continuous scenario, the **Contoso Service Desk**.

This is a **non-WSQ commercial short course**: there is no assessment, no SSG/SkillsFuture funding component and no attendance-tracking requirement. Learning is reinforced through hands-on labs, each with its own verification step.

## Course Information

- **Course Code:** C524
- **Course Title:** Certified Lean Six Sigma Yellow Belt (CLSSYB) Training
- **Duration:** 2 days · 8 training hours per day (16 hours)
- **Daily Timing:** 9:30 am – 6:30 pm (1-hour lunch; tea breaks within training time)
- **Level:** Beginner
- **Mode:** Instructor-led, hands-on Lean Six Sigma labs
- **Version:** v5 · 19 July 2026
- **Trainer:** Dr. Alfred Ang
- **Course Registration:** [Certified Lean Six Sigma Yellow Belt (CLSSYB)](https://www.tertiarycourses.com.sg/certified-lean-six-sigma-yellow-belt.html)
- **Reference:** The Council for Six Sigma Certification (CSSC), *Six Sigma: A Complete Step-by-Step Guide*

## Learning Outcomes

1. Define a project and establish the scope of work using Six Sigma's Define, Measure and Analyse phases.
2. Apply Lean and Six Sigma concepts — value, waste, defects and variation — to a work process.
3. Map a process using SIPOC, process maps and value stream maps to expose handoffs and waste.
4. Collect and analyse process data using check sheets, Pareto charts, run charts and basic metrics.
5. Identify root causes using 5 Whys, Fishbone analysis and evidence-based prioritisation.
6. Recommend improvement and control actions to sustain gains, and prepare for certification.

## Course Structure — the DMAIC roadmap

| # | Topic | Coverage | Labs |
|---|-------|----------|------|
| 1 | Six Sigma Foundations | 15% | 1 |
| 2 | Define — Scope the Problem | 25% | 2–5, 11 |
| 3 | Measure — Quantify Performance | 25% | 6, 12 |
| 4 | Analyze — Find the Root Cause | 20% | 7, 8 |
| 5 | Improve — Fix the Cause | 10% | 9, 13 |
| 6 | Control — Hold the Gain | 5% | 10, 14 |

## Labs

Every lab builds on the same Contoso Service Desk scenario, so outputs accumulate into one complete improvement package.

| # | Lab | DMAIC phase | Type |
|---|-----|-------------|------|
| 1 | [Yellow Belt Role, Certification Paths, and Improvement Scenario](labs/lab-01-yellow-belt-role-certification-paths-and-improvement-scenari.md) | FOUNDATIONS | Core |
| 2 | [Lean, Six Sigma, Waste, Voice of Customer, and Value](labs/lab-02-lean-six-sigma-waste-voice-of-customer-and-value.md) | DEFINE | Core |
| 3 | [SIPOC, Process Mapping, Handoffs, and SME Support](labs/lab-03-sipoc-process-mapping-handoffs-and-sme-support.md) | DEFINE | Core |
| 4 | [PDCA Small Improvement Project Charter](labs/lab-04-pdca-small-improvement-project-charter.md) | DEFINE | Elective |
| 5 | [DMAIC Overview, Problem Statement, Scope, and Stakeholders](labs/lab-05-dmaic-overview-problem-statement-scope-and-stakeholders.md) | DEFINE | Core |
| 6 | [Data Collection, KPIs, Check Sheets, and Basic Metrics](labs/lab-06-data-collection-kpis-check-sheets-and-basic-metrics.md) | MEASURE | Core |
| 7 | [Pareto, Run Charts, Variation, Yield, DPU, and DPMO](labs/lab-07-pareto-run-charts-variation-yield-dpu-and-dpmo.md) | ANALYZE | Core |
| 8 | [Root Cause Analysis with 5 Whys, Fishbone, and Evidence](labs/lab-08-root-cause-analysis-with-5-whys-fishbone-and-evidence.md) | ANALYZE | Core |
| 9 | [Countermeasures, 5S, Mistake Proofing, Standard Work, and Kaizen](labs/lab-09-countermeasures-5s-mistake-proofing-standard-work-and-kaizen.md) | IMPROVE | Core |
| 10 | [Control Plan, A3 Summary, Handover, and Certification Readiness](labs/lab-10-control-plan-a3-summary-handover-and-certification-readiness.md) | CONTROL | Core |
| 11 | [Affinity Diagram and Kano Analysis](labs/lab-11-affinity-diagram-and-kano-analysis.md) | DEFINE | Elective |
| 12 | [Value Stream Map and Takt Time](labs/lab-12-value-stream-map-and-takt-time.md) | MEASURE | Elective |
| 13 | [Solution Selection Matrix, Benchmarking, and FMEA](labs/lab-13-solution-selection-matrix-benchmarking-and-fmea.md) | IMPROVE | Elective |
| 14 | [Descriptive Statistics and Implementation Planning](labs/lab-14-descriptive-statistics-and-implementation-planning.md) | CONTROL | Elective |

See [labs/tools.md](labs/tools.md) for the browser-based problem-solving tools used in the labs.

## Repository Structure

```
.
├── courseware/                     Generated learner-facing artifacts
│   ├── *-v5.pptx / *-v5.pdf        Slide deck (153 slides, all-white house style)
│   ├── LP-*.docx / LP-*.pdf        Lesson Plan
│   ├── LG-*.docx / LG-*.pdf        Learner Guide
│   ├── assets/                     Images used by the deck
│   └── archive/                    Superseded versions (never deleted)
├── labs/                           14 lab worksheets + index + tools
├── reference/                      Source documents (not learner-facing)
├── LG-*.md                         Learner Guide Markdown mirror
└── .claude/skills/                 Single-source build pipeline (see below)
```

## Building the Courseware

All artifacts are generated from **one source of truth** — `course_data.py` plus `data_domain1.py` … `data_domain6.py` — so the deck, Lesson Plan, Learner Guide and labs can never drift apart.

```bash
# Full build: PPT + LP + LG as DOCX + PDF, with page-numbered tables of contents
bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
```

To change course content, edit the data modules and rebuild — never hand-edit the generated
`.pptx` / `.docx` files, as the next build will overwrite them.

### Quality check

```bash
python3 .claude/skills/non-wsq-courseware-qa/scan_prohibited.py .
```

Scans every generated artifact for content that must not appear in a non-WSQ course —
WSQ/SSG/SkillsFuture/TRAQOM references, digital attendance, course-funding language, TGS
course codes and any formal-assessment material — and reports each hit with its exact slide,
paragraph or line number.

## Included Skills

The `.claude/skills/` folder carries the reusable non-WSQ courseware toolchain:

| Skill | Purpose |
|-------|---------|
| `non-wsq-courseware-build` | Single-source pipeline generating the PPT, Lesson Plan and Learner Guide |
| `non-wsq-courseware-qa` | Prohibited-content scanner + completeness, alignment and visual checks |
| `non-wsq-lab-author` | Authoring standard for connected, self-verifying hands-on labs |

---

© 2026 Tertiary Infotech Academy Pte Ltd (UEN 201200696W). All rights reserved.
[www.tertiarycourses.com.sg](https://www.tertiarycourses.com.sg)
