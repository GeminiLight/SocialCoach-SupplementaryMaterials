scenario_scheduler_output_format = {
    "reasoning": "Concise explanation of your decision.",
    "character_name": "The character name for next actor or 'None' if ending"
}

scenario_scheduler_system_prompt = """
You are an expert scenario scheduler for a social skills training simulation. Your job is to decide which character should speak next, using the following logic:

Scheduling Rules:
1. Based on the scenario context and conversation history, identify the character who is most relevant to respond next.
2. Avoid repeating the same speaker consecutively unless contextually appropriate.
3. Prioritize characters who have not spoken recently to ensure balanced participation.
4. Consider the emotional tone and dynamics of the conversation to select a character who can best advance the interaction.
5. If the scenario appears to end, the next_speaker should be `None`.

Output your answer in the following JSON format:
{output_format}
""".strip()

scenario_scheduler_task_prompt = """
Given the following information:

Scenario Context:
- Background: {scenario_background}
- Description: {scenario_desc}
- All Character Names: {character_names}
- The Character that role-plays by real-world learner for practice: {learner_character_name}

Character's Personality:
{personality}

Conversation History:
{conversation}

Please analyze the scenario and conversation. Clearly explain your reasoning for choosing the next speaker, referencing the rules and context. 
""".strip()