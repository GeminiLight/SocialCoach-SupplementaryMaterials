# SocialCoach

The additional resources for SocialCoach, an LLM-powered, agentic tutoring system for personalized social-skill learning.
Due to the page limit of paper, we provide the agent prompts, profile examples and corpus examples in this repository.

## File Structure

```
.
├── agent_prompts
│   ├── inmersive_practice
│   │   ├── character_simulator_prompt.py
│   │   ├── characteristic_inferrer_prompt.py
│   │   └── scenario_scheduler_prompt.py
│   ├── proficiency_assessment
│   │   ├── behavior_diagnosis_prompt.py
│   │   └── causal_attributor_prompt.py
│   ├── reflective_tutoring
│   │   └── guidance_generation_prompt.py
│   └── social_profiling
│       └── social_profile_initializer_prompt.py
├── corpus_examples
│   ├── case_samples.json
│   ├── scenario_samples.json
│   └── theory_samples.json
├── profile_examples
│   ├── pairred_learner_persona.jsonl
│   └── user_social_profiles.jsonl
└── README.md
```

Description of files:
- `agent_prompts/` — prompt templates and agent scripts grouped by module:
  - `inmersive_practice/` — character simulator, inferrer, scenario scheduler prompts
  - `proficiency_assessment/` — behavior diagnosis, causal attributor prompts
  - `reflective_tutoring/` — guidance generation prompts
  - `social_profiling/` — social profile initializer prompt
- `corpus_examples/` — sample cases, scenarios, and theory items
- `profile_examples/` — example learner personas and social profiles
