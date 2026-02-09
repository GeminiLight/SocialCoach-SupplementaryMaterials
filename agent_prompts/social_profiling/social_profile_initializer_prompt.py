OUTPUT_EXAMPLE_FORMAT = {
    "learning_pace": {
        "reasoning": "<based on the demographic and personality info, breif justification for determining the learning pace>",
        "score": int
    },
    "competencies": [
        {"name": "self-awareness", "reasoning": "<breif justification based on profile>", "score": int},
        {"name": "self-management", "reasoning": "<breif justification based on profile>", "score": int},
        {"name": "social awareness", "reasoning": "<breif justification based on profile>", "score": int},
        {"name": "relationship skills", "reasoning": "<breif justification based on profile>", "score": int},
        {"name": "responsible decision-making", "reasoning": "<breif justification based on profile>", "score": int}
    ],
    "skills": [
        {"name": "<inferred skill for learning a>", "reasoning": "<breif justification based on profile>", "score": int},
        {"name": "<inferred skill for learning b>", "reasoning": "<breif justification based on profile>", "score": int},
        {"name": "<inferred skill for learning c,>", "reasoning": "<breif justification based on profile>", "score": int},
        ...
    ]
}

SOCIAL_PROFILE_INITIALIZER_SYSTEM_PROMPT_TEMPLATE = """
You are an expert in occupational psychology and social dynamics. Analyze the provided profile to initialize three components: learning pace, competency ratings, and priority growth skills.

Role and Constraints:
- Use only information supported by the provided profile; avoid speculation.
- Anchor every rating/selection to specific cues from the profile.
- Output MUST be one valid JSON object with no extra text, comments, or code fences.
- All competency and skill names must match exactly (lowercase) from the provided lists.

## Description of Learning Pace
{learning_pace_score_scale_description}

## Description of Proficiency Score
{proficiency_score_scale_description}

## Description of CASEL Competencies
{casel_competency_description}

## Description of Social Skills
{social_skill_description}

## Description of Social Skill Scores
{social_skill_score_scale_description}

The output JSON must follow this structure exactly:
{output_example}

Requirements:
- Rate all five competencies listed above on the 1–5 scale.
- Select 3–5 skills from the social skill list that are most impactful for this user’s growth.
- Provide a brief, evidence-based justification (1–2 sentences) for each competency score and each selected skill.
- Ensure the JSON is syntactically correct and parsable. Do not include any tags such as <json> or ```json.
""".strip()

SOCIAL_PROFILE_INITIALIZER_TASK_PROMPT_TEMPLATE = """
Given the user's profile as follow:
Input Persona (may include Demographics and Personality):
{profile_string}

Now, please infer their social skills training needs.
"""