from google.adk.agents import Agent
import google.generativeai as genai

def generate_discharge_summary(extracted_text: str) -> str:
    prompt = f"""
    Based on the following extracted medical text, generate a comprehensive discharge summary in JSON format.

    The JSON should have this structure:
    {{
        "patient_information": "",
        "admission_date_reason": "",
        "diagnosis": "",
        "treatment_provided": "",
        "medications": "",
        "discharge_instructions": "",
        "follow_up_care": ""
    }}

    Extracted Text:
    {extracted_text}

    Return ONLY JSON, do not include explanations or the raw extracted text.
    """
    return prompt

root_agent = Agent(
    name="agent_summary_generation",
    description="Generate structured discharge summary from medical text",
    model="gemini-2.0-flash",
    instruction="Generate a discharge summary in structured JSON format.",
    tools=[generate_discharge_summary],
)
