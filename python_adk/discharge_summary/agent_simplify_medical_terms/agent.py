from google.adk.agents import Agent

def simplify_medical_terms(discharge_summary: str) -> str:
    prompt = f"""
    Simplify the following discharge summary into patient-friendly language, like headings and subheadings, while preserving the original structure and meaning.:

    {discharge_summary}

    Guidelines:
    - Replace medical jargon with common terms
    - Keep structure intact
    - Maintain accuracy
    - Use bullet points or numbered lists if helpful
    - Return only the headings and subheadings
    - Ensure clarity and conciseness
    """
    return prompt

# root_agent = Agent(
#     name="agent_simplify_medical_terms",
#     description="Simplify discharge summary for patient understanding",
#     model="gemini-2.0-flash",
#     instruction="Simplify medical terms and return patient-friendly summary headings and subheadings.",
#     tools=[simplify_medical_terms],
# )