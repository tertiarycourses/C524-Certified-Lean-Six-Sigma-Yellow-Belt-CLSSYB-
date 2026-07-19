"""Topic 4 — Analyze — Find the Root Cause (ANALYZE). Labs: 7, 8."""

DOMAIN4 = [
    dict(
        num=7, topic=4,
        title='Pareto, Run Charts, Variation, Yield, DPU, and DPMO',
        objective='Analyse process performance data to quantify and prioritise (A3, A4)',
        desc='Turn collected data into decisions. Apply the Pareto principle to find the vital few categories, use a run chart to see behaviour over time, and calculate the standard Six Sigma process metrics.',
        build='A Pareto chart, a run chart and calculated yield, DPU, DPO, DPMO and sigma level.',
        services='Pareto Chart tool (collaborative',
        lab_type='Core',
        steps=[
            ('Build the Pareto table: category, count, percentage and cumulative percentage.', ''),
            ('In your group, open the collaborative Pareto tool — one member creates the session and shares the code, then everyone joins, brainstorms and votes to produce the live Pareto chart.', ''),
            ('Identify the vital few categories driving about 80% of the problem.', ''),
            ('Export your assignment-time data as CSV and plot a run chart in NovaSPC.', ''),
            ('Interpret the run chart for trend, shift, cluster and oscillation patterns.', ''),
            ('Calculate yield, DPU, DPO and DPMO from your defect data.', ''),
            ('Convert DPMO to a sigma level and interpret what it says about the process.', ''),
            ('Distinguish common-cause from special-cause variation and why the response differs.', ''),
        ],
        test='Your cumulative percentage column reaches 100%, and you can state the sigma level with the DPMO it came from.',
    ),
    dict(
        num=8, topic=4,
        title='Root Cause Analysis with 5 Whys, Fishbone, and Evidence',
        objective='Identify root causes of variation using structured analysis (A3)',
        desc='Move from symptom to cause. Apply the 5 Whys to drill past the obvious, organise candidate causes on a Fishbone diagram, then test each candidate against the evidence you actually collected.',
        build='A completed 5 Whys chain, a Fishbone diagram and an evidence-tested cause shortlist.',
        services='5 Whys tool, Fishbone tool, 5M categories, brainstorming, multi-voting',
        lab_type='Core',
        steps=[
            ('Write the problem statement precisely — the effect you are explaining.', ''),
            ('Complete a 5 Whys chain with the online 5 Whys tool, continuing until you reach an actionable cause.', ''),
            ('Build a Fishbone diagram with the online Fishbone tool using the 5M categories: Manpower, Method, Machine, Material, Measurement.', ''),
            ('Brainstorm candidate causes into each category — no evaluation during generation.', ''),
            ('Use multi-voting to shortlist the most likely causes as a team.', ''),
            ('Test each shortlisted cause against your Lab 7 data — does the evidence support it?', ''),
            ('State why the team must not jump straight to solutions.', ''),
        ],
        test='Each shortlisted root cause is supported by named evidence, and your 5 Whys chain ends at something you can act on.',
    ),
]
