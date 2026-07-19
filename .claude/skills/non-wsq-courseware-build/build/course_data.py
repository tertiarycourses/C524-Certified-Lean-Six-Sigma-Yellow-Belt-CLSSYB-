"""
SINGLE SOURCE OF TRUTH — Certified Lean Six Sigma Yellow Belt (CLSSYB), C524.

NON-WSQ course: no assessment, no funding/SSG, no TRAQOM, no digital attendance
and no TGS- reference. The 165 minutes Day 2 previously spent on the WA + Case
Study are returned to teaching — the elective labs (11–14) are now delivered
in class rather than left as optional take-home practice.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Certified Lean Six Sigma Yellow Belt (CLSSYB) Training"
SHORT_TITLE  = "Certified Lean Six Sigma Yellow Belt (CLSSYB) Training"
COURSE_CODE  = "C524"
VERSION      = "v5"
VERSION_DATE = "19 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2
MODE         = "Instructor-led, hands-on Lean Six Sigma labs using the Contoso Service Desk scenario"

DARK_THEME = False

TRAINER_CERT     = "Certified Lean Six Sigma practitioner — process improvement, quality and data-driven problem solving."
TRAINER_DELIVERS = "Professional short courses on Lean Six Sigma, quality management, data and cloud."

ICE_BREAKER = [
    "Your name and organisation / role.",
    "A process in your work that frustrates you or your customers.",
    "What you want to be able to improve after this course.",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Define a project and establish the scope of work using Six Sigma's Define, Measure and Analyse phases.",
    "LO2: Apply Lean and Six Sigma concepts — value, waste, defects and variation — to a work process.",
    "LO3: Map a process using SIPOC, process maps and value stream maps to expose handoffs and waste.",
    "LO4: Collect and analyse process data using check sheets, Pareto charts, run charts and basic metrics.",
    "LO5: Identify root causes using 5 Whys, Fishbone analysis and evidence-based prioritisation.",
    "LO6: Recommend improvement and control actions to sustain gains, and prepare for certification.",
]
LO_TITLES = [
    "Define & Scope", "Lean & Six Sigma Concepts", "Process Mapping",
    "Data & Analysis", "Root Cause Analysis", "Improve & Control",
]

# ------------------------------------------------------------------ topics (DMAIC roadmap)
TOPICS = [
    dict(num=1, code="01", title="Six Sigma Foundations", weighting="15%",
         subtitle="Quality · Lean · Six Sigma · Lean Six Sigma · Belt roles · The DMAIC roadmap",
         concepts=[
            ("What is Quality", "Quality is conformance to customer requirements — not merely defect-free output."),
            ("What is Lean", "A method to maximise customer value by systematically removing waste and improving flow."),
            ("What is Six Sigma", "A data-driven method to reduce variation and defects — targeting 3.4 defects per million."),
            ("Lean Six Sigma", "The combined method: faster flow AND fewer defects, driven by data."),
            ("Belt roles", "White, Yellow, Green, Black and Master Black Belt — who does what on a project."),
            ("The DMAIC roadmap", "Define, Measure, Analyze, Improve, Control — the disciplined improvement path."),
         ]),
    dict(num=2, code="02", title="Define — Scope the Problem", weighting="25%",
         subtitle="VOC · CTQ · Project charter · Problem statement · Scope · SIPOC · Process mapping",
         concepts=[
            ("Voice of the Customer", "Capture customer needs in their own words before deciding anything."),
            ("Critical to Quality", "Translate each VOC need into a specific, measurable CTQ requirement."),
            ("Project charter", "Problem statement, goal, scope, team and benefit — the project's contract."),
            ("Problem statement", "Process, time period, measurable issue and impact — and never a solution."),
            ("SIPOC", "The macro as-is map: Suppliers, Inputs, Process, Outputs, Customers."),
            ("Process mapping", "Flowcharts and swimlanes expose the handoffs where delay and defects are born."),
         ]),
    dict(num=3, code="03", title="Measure — Quantify Performance", weighting="25%",
         subtitle="The 8 wastes · Data types · Data collection plan · Check sheets · Yield · DPMO · Sigma level",
         concepts=[
            ("The 8 wastes — DOWNTIME", "Defects, Overproduction, Waiting, Non-utilised talent, Transport, Inventory, Motion, Extra-processing."),
            ("Types of data", "Continuous vs discrete; nominal vs ordinal — the data type drives the tool choice."),
            ("Data collection plan", "What, who, when and how — with operational definitions to remove ambiguity."),
            ("Check sheets", "A simple structured form is the most reliable way to capture process data."),
            ("Process metrics", "Yield, DPU, DPO and DPMO quantify how well the process actually performs."),
            ("Sigma level", "Convert DPMO into a sigma level to benchmark the process against Six Sigma."),
         ]),
    dict(num=4, code="04", title="Analyze — Find the Root Cause", weighting="20%",
         subtitle="Variation · Pareto · Run charts · 5 Whys · Fishbone · Multi-voting · Evidence",
         concepts=[
            ("Variation", "Common cause is built into the process; special cause is an external, assignable signal."),
            ("Pareto analysis", "The 80/20 rule separates the vital few causes from the trivial many."),
            ("Run charts", "Plot the metric over time to reveal trend, shift, cluster and oscillation."),
            ("5 Whys", "Ask why repeatedly to drill from the symptom down to an actionable cause."),
            ("Fishbone diagram", "Organise candidate causes by category — Manpower, Method, Machine, Material, Measurement."),
            ("Evidence testing", "A cause is only a root cause when the data you collected supports it."),
         ]),
    dict(num=5, code="05", title="Improve — Fix the Cause", weighting="10%",
         subtitle="Countermeasures · 5S · Poka-Yoke · Standard work · Kaizen · Solution selection · Piloting",
         concepts=[
            ("Generating solutions", "Brainstorm widely against the proven root cause before evaluating anything."),
            ("Solution selection", "Score candidate solutions against weighted criteria before committing."),
            ("5S", "Sort, Set in order, Shine, Standardise, Sustain — for physical and digital work."),
            ("Poka-Yoke", "Mistake proofing makes the error difficult or impossible to make in the first place."),
            ("Standard work", "Document the improved method so anyone can repeat it the same way."),
            ("Piloting", "Test the change at small scale to expose issues before full rollout."),
         ]),
    dict(num=6, code="06", title="Control — Hold the Gain", weighting="5%",
         subtitle="Control plan · Visual management · SOPs · Huddles · A3 · Handover · Certification",
         concepts=[
            ("Control plan", "Metric, target, monitoring method, frequency, owner and reaction plan."),
            ("Process control", "A process is in control when it varies consistently within expected limits."),
            ("Visual management", "Boards and dashboards keep the improved performance visible to everyone."),
            ("Standard operating procedures", "Written instructions that lock in the improved method."),
            ("Team huddles", "Short, regular stand-ups that surface problems while they are still small."),
            ("A3 and handover", "One-page storytelling to summarise, hand over and sustain the improvement."),
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Six Sigma foundations, Define phase and process mapping",
    2: "Measure, Analyse, Improve and Control",
}

# ------------------------------------------------------------------ schedule
# 480 training minutes per day (lunch excluded). No assessment blocks — the
# 165 min Day 2 previously used for the WA + Case Study now delivers the
# elective labs (11–14) in class plus a consolidation workshop.
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:30","10:00",30,"admin","Welcome, course introduction and ground rules"),
        ("10:00","11:15",75,"topic","FOUNDATIONS — What is Quality; What is Lean; What is Six Sigma; Lean Six Sigma; belt roles; the DMAIC roadmap"),
        ("11:15","11:30",15,"break","Tea break"),
        ("11:30","12:30",60,"lab","Hands-on: "+lab_titles([1])),
        ("12:30","13:30",60,"lunch","Lunch break"),
        ("13:30","15:00",90,"topic","DMAIC · DEFINE — Voice of the Customer; VOC to CTQ translation; project charter; problem statement; scope; SIPOC; process mapping"),
        ("15:00","15:15",15,"break","Tea break"),
        ("15:15","18:00",165,"lab","Hands-on: "+lab_titles([2,3,4,5,11])),
        ("18:00","18:30",30,"recap","Day 1 recap and Q&A"),
     ]),
     2: (DAY_THEMES[2], [
        ("9:30","9:45",15,"recap","Day 1 recap"),
        ("9:45","11:00",75,"topic","DMAIC · MEASURE — the eight wastes (DOWNTIME); data types; data collection plan; check sheets; yield, DPU, DPO and DPMO; sigma level"),
        ("11:00","11:15",15,"break","Tea break"),
        ("11:15","12:30",75,"lab","Hands-on: "+lab_titles([6,12])),
        ("12:30","13:30",60,"lunch","Lunch break"),
        ("13:30","14:15",45,"topic","DMAIC · ANALYZE — common vs special cause variation; Pareto; run charts; 5 Whys; Fishbone; evidence testing"),
        ("14:15","15:15",60,"lab","Hands-on: "+lab_titles([7,8])),
        ("15:15","15:30",15,"break","Tea break"),
        ("15:30","16:00",30,"topic","DMAIC · IMPROVE — solution generation and selection; 5S; poka-yoke; standard work; kaizen; piloting"),
        ("16:00","17:00",60,"lab","Hands-on: "+lab_titles([9,13])),
        ("17:00","17:30",30,"topic","DMAIC · CONTROL — control plans; process control; visual management; SOPs; huddles; A3 and handover"),
        ("17:30","18:15",45,"lab","Hands-on: "+lab_titles([10,14])),
        ("18:15","18:30",15,"recap","Course recap, consolidation and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck overview section
COURSE_OVERVIEW = dict(
    section_title="Lean Six Sigma Fundamentals",
    concepts_title="What is Lean Six Sigma?",
    concepts=[
        ("Lean removes waste", "Maximise customer value by eliminating the effort the customer would never pay for."),
        ("Six Sigma reduces variation", "A data-driven method targeting 3.4 defects per million opportunities."),
        ("Together: fast and accurate", "Lean Six Sigma delivers faster flow AND fewer defects, driven by evidence."),
        ("Everyone has a belt role", "White, Yellow, Green, Black and Master Black Belt — the Yellow Belt supports."),
    ],
    framework_title="The DMAIC Roadmap",
    framework=[
        ("Define", "Scope the problem — VOC, CTQ, charter, problem statement, SIPOC."),
        ("Measure", "Quantify today's performance — data collection, check sheets, yield and DPMO."),
        ("Analyze", "Find the root cause — Pareto, run charts, 5 Whys and Fishbone."),
        ("Improve", "Fix the cause — countermeasures, 5S, poka-yoke, standard work and piloting."),
        ("Control", "Hold the gain — control plan, SOPs, visual management, A3 and handover."),
    ],
    statement=dict(
        headline="Improve the process, not the people.",
        body="Every tool in this course points at the process: measure what it actually does, find why it does it, and change the system so the improvement holds.",
        kicker="THE LEAN SIX SIGMA MINDSET"),
    pillars_title="One Scenario, One Complete Package",
    pillars=[
        ("Define & Measure", ["Contoso Service Desk", "VOC → CTQ, SIPOC", "Data collection plan"]),
        ("Analyze", ["Pareto and run charts", "5 Whys and Fishbone", "Evidence-tested root cause"]),
        ("Improve & Control", ["Countermeasures and 5S", "Control plan and SOPs", "A3 summary and handover"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Every lab uses one continuous scenario — the Contoso Service Desk, where IT tickets are slow to be assigned.",
        "Each lab produces a real artifact: a table, a map, a chart or a plan.",
        "Each lab ends with a 'Check your work' step so you can verify your own output.",
        "By the end your outputs form one complete improvement package, ready to reuse at work.",
    ],
)

NEXT_STEPS = dict(title="Continuing Your Lean Six Sigma Journey", items=[
    "Run a small improvement in your own workplace using the DMAIC roadmap and the templates from this course.",
    "Progress towards Green Belt — deeper statistics, hypothesis testing and full project leadership.",
    "Build the habit: measure before you change, and verify the gain held after you did.",
    "Share the A3 one-pager with your team so the improvement is visible and sustained.",
])

THANK_YOU = dict(
    body="You can now scope, measure, analyse, improve and control a real process improvement using the DMAIC roadmap.",
    kicker="IMPROVE THE PROCESS")

# ------------------------------------------------------------------ Learner Guide content
LG_INTRO = ("This Learner Guide accompanies the course Certified Lean Six Sigma Yellow Belt (CLSSYB) "
            "Training (C524), conducted by Tertiary Infotech Academy Pte Ltd. It follows the DMAIC "
            "roadmap end to end — Define, Measure, Analyze, Improve, Control — and provides "
            "step-by-step instructions for every hands-on lab.")
LG_INTRO2 = ("The course content is grounded in the body of knowledge published by The Council for Six "
             "Sigma Certification (CSSC) in 'Six Sigma: A Complete Step-by-Step Guide', so what you "
             "learn here matches the recognised Yellow Belt standard. Every lab uses one continuous "
             "scenario — the Contoso Service Desk, where IT tickets take too long to be assigned and "
             "employees must chase for status. By the end of the course your lab outputs form a "
             "complete improvement package: role definition, VOC/CTQ, process maps, data collection "
             "plan, analysis, root cause, countermeasures and a control plan.")

LG_SETUP = dict(
    needs=[
        "A laptop or tablet with a spreadsheet application (Microsoft Excel, Google Sheets or LibreOffice Calc).",
        "A web browser for the interactive problem-solving tools listed in labs/tools.md.",
        "Printed or digital copies of this Learner Guide and the lab worksheets.",
        "Pen and paper (or a whiteboard) — several labs are faster sketched by hand.",
        "Optional: a real process from your own workplace you would like to improve.",
    ],
    verify_text=("No software installation is required for this course. Before you begin, confirm you can "
                 "open a blank spreadsheet and reach the browser-based tools listed in labs/tools.md."),
    conventions=[
        "Every lab uses the same Contoso Service Desk scenario, so your outputs accumulate across the course.",
        "Each lab states what you will build; keep every output — later labs depend on earlier ones.",
        "Where a lab uses figures, the data is provided in the lab worksheet — no external data is needed.",
        "Use only process data you are authorised to share if you substitute your own workplace scenario.",
    ],
)
LAB_NOTE = "Use only process data you are authorised to use if you substitute your own workplace scenario."

LG_WRAPUP = dict(
    title="Wrap-Up — The DMAIC Roadmap and Sustaining the Gain",
    intro=("These cross-cutting themes run through every phase of the course. Study this section "
           "alongside the labs so the same approach transfers from the Contoso Service Desk scenario "
           "to a real improvement in your own workplace."),
    sections=[
        dict(title="The DMAIC roadmap", bullets=[
            "Define — establish the problem, the customer requirement (VOC to CTQ), the scope and the as-is process (SIPOC, process map).",
            "Measure — quantify today's performance with a data collection plan, check sheets, and metrics such as yield, DPU, DPO and DPMO.",
            "Analyze — separate common from special cause variation, then find the root cause with Pareto, run charts, 5 Whys and Fishbone.",
            "Improve — generate and select countermeasures, apply 5S, poka-yoke and standard work, and pilot before full rollout.",
            "Control — lock in the gain with a control plan, SOPs, visual management, team huddles and an A3 handover.",
        ]),
        dict(title="Habits that make improvement stick", bullets=[
            "Measure before you change — without a baseline you cannot prove the improvement worked.",
            "Attack the process, not the people — the system produces the result you are seeing.",
            "Test every candidate cause against the evidence before you call it a root cause.",
            "Standardise the improved method, or the process will drift back within weeks.",
            "Make performance visible — what is seen daily is what gets sustained.",
        ]),
    ],
)

LG_NEXT_STEPS = [
    "First pass: complete every lab, following the steps in each lab worksheet.",
    "Second pass: repeat the DMAIC cycle on a small process from your own workplace.",
    "Build your improvement package — keep the VOC/CTQ, maps, analysis, countermeasures and control plan together.",
    "Progress towards Green Belt for deeper statistics, hypothesis testing and full project leadership.",
]

LG_GLOSSARY = [
    ("Lean", "A method to maximise customer value by systematically removing waste and improving flow."),
    ("Six Sigma", "A data-driven method to reduce variation and defects, targeting 3.4 defects per million opportunities."),
    ("DMAIC", "Define, Measure, Analyze, Improve, Control — the disciplined Lean Six Sigma improvement roadmap."),
    ("VOC", "Voice of the Customer — customer needs captured in the customer's own words."),
    ("CTQ", "Critical to Quality — a specific, measurable requirement translated from a VOC need."),
    ("SIPOC", "A macro as-is process map: Suppliers, Inputs, Process, Outputs, Customers."),
    ("DOWNTIME", "The eight wastes: Defects, Overproduction, Waiting, Non-utilised talent, Transport, Inventory, Motion, Extra-processing."),
    ("Value-added", "An activity the customer would be willing to pay for, done right the first time."),
    ("Defect", "An output that fails to meet a CTQ requirement."),
    ("Variation", "The spread in process output; common cause is inherent, special cause is assignable."),
    ("Yield", "The proportion of units produced without defect."),
    ("DPU / DPO / DPMO", "Defects per unit, defects per opportunity, and defects per million opportunities."),
    ("Sigma level", "A benchmark of process capability derived from DPMO."),
    ("Pareto analysis", "The 80/20 rule — separating the vital few causes from the trivial many."),
    ("Run chart", "A plot of a metric over time, used to reveal trend, shift, cluster and oscillation."),
    ("5 Whys", "Asking why repeatedly to drill from a symptom down to an actionable root cause."),
    ("Fishbone diagram", "A cause-and-effect diagram organising candidate causes by category."),
    ("5S", "Sort, Set in order, Shine, Standardise, Sustain — workplace organisation for physical and digital work."),
    ("Poka-Yoke", "Mistake proofing — making an error difficult or impossible to make."),
    ("Standard work", "The documented best-known method so anyone can repeat it the same way."),
    ("Kaizen", "Continuous, incremental improvement driven by the people who do the work."),
    ("Control plan", "Metric, target, monitoring method, frequency, owner and reaction plan."),
    ("A3", "A one-page structured summary used to tell the improvement story and hand it over."),
    ("Takt time", "The rate of customer demand — available time divided by units required."),
    ("FMEA", "Failure Modes and Effects Analysis — scoring risk by severity, occurrence and detection."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1", "1 June 2026", "Initial release — CLSSYB 2-day lesson plan.", TRAINER),
    ("2", "15 June 2026", "Refreshed labs against the CSSC Yellow Belt reference.", TRAINER),
    ("3", "1 July 2026", "Aligned the schedule with the Contoso Service Desk case-study scenario.", TRAINER),
    ("4", "19 July 2026", "Major content expansion: course restructured to follow the DMAIC roadmap across six topics with 14 labs.", TRAINER),
    ("5", VERSION_DATE,
     "Converted to the non-funded commercial course standard; the course code is now C524. "
     "The 165 minutes previously reserved for formal evaluation on Day 2 are returned to teaching — elective labs 11-14 are now delivered in class. "
     "Rebuilt from a single source (course_data.py + data_domain1-6.py) via the non-wsq-courseware-build engine.",
     TRAINER),
]
