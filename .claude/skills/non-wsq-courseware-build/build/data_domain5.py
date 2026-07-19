"""Topic 5 — Improve — Fix the Cause (IMPROVE). Labs: 9, 13."""

DOMAIN5 = [
    dict(
        num=9, topic=5,
        title='Countermeasures, 5S, Mistake Proofing, Standard Work, and Kaizen',
        objective='Recommend improvement actions that address the proven root cause (A5)',
        desc='Generate and select countermeasures that attack the root cause you proved — not the symptom. Apply the core Lean improvement tools: 5S, poka-yoke, visual management, standard work and Kaizen.',
        build='A prioritised countermeasure set with a 5S plan, a poka-yoke design and standard work.',
        services='Brainstorming, 5S, poka-yoke, visual management, standard work, Kaizen',
        lab_type='Core',
        steps=[
            ('Generate countermeasures for each proven root cause — quantity before quality.', ''),
            ('Prioritise using an impact vs effort matrix to find the quick wins.', ''),
            ('Apply 5S thinking — Sort, Set in order, Shine, Standardise, Sustain — including to digital work.', ''),
            ('Design one poka-yoke that makes the error difficult or impossible to make.', ''),
            ('Draft standard work so the improved method is repeatable by anyone.', ''),
            ('Plan a Kaizen event or pilot to test the countermeasure at small scale first.', ''),
            ('Distinguish a containment countermeasure from a permanent solution.', ''),
        ],
        test='Every countermeasure traces back to a proven root cause, and your poka-yoke prevents rather than detects the error.',
    ),
    dict(
        num=13, topic=5,
        title='Solution Selection Matrix, Benchmarking, and FMEA',
        objective='Evaluate and de-risk candidate solutions before implementation (A5, K2)',
        desc='Three Improve-phase tools from the original course. Score solutions against weighted criteria, benchmark against outstanding practice, and use FMEA to find how a proposed change could fail before it does.',
        build='A scored solution selection matrix, a benchmarking summary and an FMEA with RPN.',
        services='Solution selection matrix, benchmarking, FMEA, RPN scoring',
        lab_type='Elective',
        steps=[
            ('Agree the selection criteria and weight each by importance.', ''),
            ('Score every candidate solution against the weighted criteria and rank the results.', ''),
            ('Benchmark your process against an internal or external reference and note the gap.', ''),
            ('Build an FMEA: failure mode, effect, cause, then score Severity, Occurrence and Detection.', ''),
            ('Calculate RPN = S x O x D and address the highest-RPN failure modes first.', ''),
        ],
        test='Your matrix ranks solutions by weighted score, and every FMEA row has an RPN and an action for the highest scores.',
    ),
]
