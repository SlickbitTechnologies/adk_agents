from google.adk.agents import Agent
import PyPDF2

def doc_ai_tool(file_path: str, pii_fields: list[str], task: str = "redact") -> dict:
    """
    Unified document processing tool:
    - Extracts text from PDF
    - Redacts PII if task == 'redact'
    - Summarizes if task == 'summarize'
    - QA if task == 'qa'
    """
    
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = "".join(page.extract_text() for page in reader.pages)

    return {
        "text": text,
        "pii_fields": pii_fields,
        "task": task
    }


root_agent = Agent(
    name="doc_redact",
    model="gemini-2.0-flash",
    description="Extract, redact, summarize, and QA documents in one tool",
    instruction=(
        "You are a document AI specialist. "
        "Use the tool input:\n"
        "{\n"
        '    "task": "redact",\n'
        '    "redacted_text": "<redacted_text>"\n'
        "  }\n\n"
        # "- If task == 'redact': redact sensitive fields defined in 'pii_fields', return 'redacted_text' .\n"
        "- If task == 'summarize': generate a summary, return 'summary'.\n"
        "- If task == 'qa': prepare the document for answering user queries, return 'qa_ready'.\n"
        "Always output in structured JSON."
    ),
    tools=[doc_ai_tool],
)
