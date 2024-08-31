import openai

# Load sections from local files
def load_section(filename):
    with open(filename, 'r') as file:
        return file.read()

# Load all sections from local files
system_message = load_section("system_message.txt")
tone = load_section("tone.txt")
goal = load_section("goal.txt")
audience = load_section("audience.txt")
conceptualization_feedback = load_section("conceptualization_feedback.txt")
mechanics_development = load_section("mechanics_development.txt")
component_design = load_section("component_design.txt")
playtesting_iteration = load_section("playtesting_iteration.txt")
advanced_rules_scenarios = load_section("advanced_rules_scenarios.txt")
finalizing_rulebook = load_section("finalizing_rulebook.txt")
documentation_cards_abilities = load_section("documentation_cards_abilities.txt")
final_review_production = load_section("final_review_production.txt")
gameplay_examples = load_section("gameplay_examples.txt")
user_input = load_section("user_input.txt")

# Define prompt template
prompt_template = f"""
System Message / Context:
{system_message}

Tone:
{tone}

Goal:
{goal}

Audience:
{audience}

Conceptualization and Initial Feedback:
{conceptualization_feedback}

Game Mechanics and Rules Development:
{mechanics_development}

Component Design and Prototyping:
{component_design}

Playtesting and Iteration:
{playtesting_iteration}

Advanced Rules and Scenarios Development:
{advanced_rules_scenarios}

Finalizing the Rulebook:
{finalizing_rulebook}

Documentation of Cards and Abilities:
{documentation_cards_abilities}

Final Review and Production Preparation:
{final_review_production}

Gameplay Examples:
{gameplay_examples}

User Input:
{user_input}
"""

# OpenAI API call
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt_template,
    max_tokens=2000,
    temperature=0.7
)

print(response.choices[0].text)
