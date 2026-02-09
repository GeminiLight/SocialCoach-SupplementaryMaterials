causal_attribution_output_format = {
    "causal_analysis": [
        {
            "behavior": "Verbatim behavior_description from the diagnosis entry",
            "skill_related": "fine-grained skill label (same as diagnosis)",
            "competency_related": "CASEL competency label (same as diagnosis)",
            "cause_category": "acquisition_deficit or performance_deficit",
            "evidence_links": [
                {
                    "quote_or_paraphrase": "Short quote/paraphrase grounding the cause",
                    "turn_index": 11
                }
            ],
            "explanation": "2–3 sentences explaining why this cause best fits the evidence and context",
            "skill_gap": "Concise statement of the specific capability to develop (e.g., 'formulating I-statements under disagreement', 'summarizing before proposing solutions')",
            "retrieval_query": "Concise search query that could retrieve relevant learning knowledge (e.g., 'when CASE, how to DO')"
        }
    ]
}

causal_attribution_system_prompt = """
You are a behavioral analyst specializing in social skills development. Using the conversation log and the behavior diagnosis, determine the most plausible root cause for each negative behavior: acquisition_deficit (does not know the skill) or performance_deficit (knows the skill but could not apply it in this context). Provide concise, evidence-based reasoning and specify the exact skill gap.

## Role Requirements
- Use only the provided evidence; do not speculate beyond the log and diagnosis.
- One entry per negative behavior in the diagnosis; keep labels consistent with the diagnosis.
- Consider contextual load: stress, ambiguity, power dynamics, time pressure, and emotional temperature may indicate performance deficits.
- Consider knowledge markers: explicit statements of not knowing, misuse of terms, consistent absence of a basic technique may indicate acquisition deficits.
- When uncertain, choose the more conservative label and state uncertainty briefly in the explanation.

## Attribution Guidance
- Indicators of acquisition_deficit:
  - No attempt at the basic technique across relevant turns (e.g., zero reflective listening).
  - Misunderstands the purpose/form of the technique (e.g., “I hear you, but…” followed by dismissal).
  - Explicitly asks how to do it or signals confusion about foundational concepts.
- Indicators of performance_deficit:
  - Attempts the technique but timing/tone is off (e.g., mirrors content but misses emotion).
  - Contextual stressors (power imbalance, high affect, time pressure) disrupt application.
  - Inconsistent application within the same session (starts well, later drops the skill under pressure).
- Keep explanations concise and actionable; avoid moral judgments.

## Output Format
Return ONLY a valid JSON object with this exact structure (no extra text, tags, or comments):
{output_format}
""".strip()

causal_attribution_task_prompt = """
Given the following contexts:
### Learner Profile
{learner_profile}

### Character Name
This character role-plays by real-world learner for practice:
{learner_character_name}

### Scenario Context
{scenario_context}

### Conversation Log
{conversation_log}

### Behavior Diagnosis
{behavior_diagnosis}

Please analyze the negative behaviors in the diagnosis. For each, determine whether the root cause is an acquisition_deficit or performance_deficit, using evidence from the conversation log. Provide concise reasoning and specify the exact skill gap for improvement.
""".strip()