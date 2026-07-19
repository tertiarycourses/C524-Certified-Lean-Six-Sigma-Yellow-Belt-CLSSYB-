"""Topic 3 — Measure — Quantify Performance (MEASURE). Labs: 6, 12."""

DOMAIN3 = [
    dict(
        num=6, topic=3,
        title='Data Collection, KPIs, Check Sheets, and Basic Metrics',
        objective='Plan and execute data collection against defined quality standards (A4)',
        desc='Replace anecdote with evidence. Define KPIs with unambiguous operational definitions, design a check sheet, plan the sampling approach, and understand which data type you are collecting — because the data type drives the tool.',
        build='A data collection plan, an operational definition set and a working check sheet.',
        services='KPI definition, operational definitions, check sheets, sampling, data types',
        lab_type='Core',
        steps=[
            ('Classify your data: continuous vs discrete, nominal vs ordinal — and why it matters.', ''),
            ('Define KPIs with operational definitions, data source and collection frequency.', ''),
            ('Design a check sheet capturing date, ticket ID, type, assignment time and defect category.', ''),
            ('Define mutually exclusive defect categories so every observation lands in exactly one.', ''),
            ('Plan sampling: how many, how often, by whom — and identify possible bias.', ''),
            ('State which KPI best reflects the customer pain point from your VOC work.', ''),
        ],
        test='Two different people reading your operational definition would record the same value for the same event.',
    ),
    dict(
        num=12, topic=3,
        title='Value Stream Map and Takt Time',
        objective='Quantify flow, lead time and takt time across the value stream (A3, A4)',
        desc='Extend process mapping into Lean metrics. Map the value stream with process and wait times, calculate process cycle efficiency, then compute takt time to see whether the process can meet customer demand.',
        build='A value stream map with lead time, process time and a calculated takt time.',
        services='Value stream mapping, lead time, WIP, takt time, cycle efficiency',
        lab_type='Elective',
        steps=[
            ('Map the value stream: each step with its process time and the wait time between steps.', ''),
            ('Total the value-added time and the lead time, then compute process cycle efficiency.', ''),
            ('Calculate takt time = available working time / customer demand.', ''),
            ('Compare cycle time against takt time to identify the bottleneck step.', ''),
        ],
        test='Your lead time equals the sum of all process and wait times, and takt time is expressed per unit.',
    ),
]
