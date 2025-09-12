# from agent_summary_generation import generate_discharge_summary
# from agent_simplify_medical_terms import simplify_medical_terms
# from agent_text_extract import extract_text_from_image


from agent_text_extract.agent import extract_text_from_image
from agent_summary_generation.agent import generate_discharge_summary
from agent_simplify_medical_terms.agent import simplify_medical_terms
from google.adk.agents import Agent

async def run_text_extract(image_path: str) -> str:
    """Extract text from a medical document image at the provided file path."""
    return extract_text_from_image(image_path)

async def run_summary_generation(text: str) -> str:
    """Generate a professional discharge summary from extracted medical text."""
    return generate_discharge_summary(text)

async def run_medical_simplification(text: str) -> str:
    """Simplify the discharge summary into patient-friendly language while preserving accuracy."""
    return simplify_medical_terms(text)



root_agent = Agent(
    name="main_agent",
    description="Main coordinator for discharge summary creation.",
    model="gemini-2.0-flash",
    instruction=(
        "You MUST use tools to complete the task in this order when possible: "
        "1) run_text_extract(image_path) -> returns extracted text. "
        "2) run_summary_generation(text) -> returns professional discharge summary. "
        "3) run_medical_simplification(text) -> simplify the professional summary for patients. "
        "If user already provides text, start at step 2. Always perform step 3 after step 2. "
        "Return BOTH: (A) a machine-readable JSON and (B) a human-readable structured text with headings/subheadings. "
        "JSON (no markdown): {\"status\": \"complete\"|\"error\", \"steps\": [string], \"results\": {\"extracted_text\": string|null, \"professional_summary_text\": string|null, \"patient_friendly_text\": string|null}, \"error\": string|null}. "
        "Structured Text format (plain text with headings and subheadings, no JSON):\n"
        "Discharge Summary\n"
        "Patient Information\n"
        "- Name: ...\n"
        "- Age: ...\n"
        "- Sex: ...\n"
        "Admission Details\n"
        "- Admission Date: ...\n"
        "- Reason for Admission: ...\n"
        "Diagnosis\n"
        "- Primary Diagnosis: ...\n"
        "- Secondary Diagnoses: ...\n"
        "Treatment Provided\n"
        "- Procedures: ...\n"
        "- Medications During Stay: ...\n"
        "Medications on Discharge\n"
        "- Medication Name | Dosage | Frequency | Duration\n"
        "Discharge Instructions\n"
        "- Diet: ...\n"
        "- Activity: ...\n"
        "- Warning Signs: ...\n"
        "Follow-up Care\n"
        "- Next Appointment: ...\n"
        "- Tests to be Done: ...\n"
        "Patient-Friendly Summary\n"
        "- What Happened: ...\n"
        "- What You Need to Do: ...\n"
        "- When to Seek Help: ...\n"
        "Ensure clear headings and bullet points as shown."
    ),
    tools=[
        run_text_extract,
        run_summary_generation,
        run_medical_simplification,
    ],
)
