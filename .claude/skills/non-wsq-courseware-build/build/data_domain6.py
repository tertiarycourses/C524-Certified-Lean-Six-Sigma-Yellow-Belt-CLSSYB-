"""Topic 6 — Control — Hold the Gain (CONTROL). Labs: 10, 14."""

DOMAIN6 = [
    dict(
        num=10, topic=6,
        title='Control Plan, A3 Summary, Handover, and Certification Readiness',
        objective='Recommend control actions to sustain process performance (A5)',
        desc='Hold the gain. Build a control plan that names the metric, the target, the monitoring frequency, the owner and the reaction plan — then tell the whole improvement story on a single A3 page and hand it over.',
        build='A control plan, an A3 one-page summary, a handover checklist and a readiness plan.',
        services='Control plan, SPC thinking, visual management, A3 report, handover',
        lab_type='Core',
        steps=[
            ('Create the control plan: metric, target, monitoring method, frequency, owner, reaction plan.', ''),
            ('Define the visual management approach — board, dashboard or huddle — that keeps it visible.', ''),
            ('Specify the reaction plan: exactly what happens when a metric falls outside target.', ''),
            ('Write the A3 summary: background, current state, goal, analysis, countermeasures, results, follow-up.', ''),
            ('Prepare the handover checklist so the process owner can sustain it without you.', ''),
            ('Complete your personal certification readiness plan — which topics need most review.', ''),
        ],
        test='Every control plan row has a named owner and a reaction plan, and your A3 fits on one page.',
    ),
    dict(
        num=14, topic=6,
        title='Descriptive Statistics and Implementation Planning',
        objective='Summarise data numerically and plan the rollout (A4, A5)',
        desc='Close the loop. Compute the measures of central tendency and dispersion that describe your data, then convert the selected countermeasures into a dated implementation plan with owners and barriers identified.',
        build='A descriptive statistics summary and a dated implementation plan.',
        services='Mean, median, range, standard deviation, implementation planning',
        lab_type='Elective',
        steps=[
            ('Compute the mean and median for your assignment-time data and compare them.', ''),
            ('Compute the range and standard deviation to describe the spread.', ''),
            ('Explain what the mean-versus-median difference reveals about outliers and skew.', ''),
            ('Write the implementation plan: action, owner, date, barriers and mitigation.', ''),
        ],
        test='You can explain why the mean and median differ in your data, and every implementation action has an owner and a date.',
    ),
]
