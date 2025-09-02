from google.adk.agents import Agent
import PyPDF2
import re

def dock_text_tool(file_path: str) -> dict:
    """Extract text from a document."""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": str(e)}

    
    metadata_patterns = {
        "agreement_date": r'\b\d{2}/\d{2}/\d{4}\b',  # Dates in DD/MM/YYYY
        "expiry_date": r'Expiry Date[:\s]+(\d{2}/\d{2}/\d{4})',
        "amounts": r'₹\s?\d+(?:,\d{3})*(?:\.\d+)?',
        "contact_emails": r'\b[\w\.-]+@[\w\.-]+\.\w+\b',
        "party_names": r'Party[:\s]+([A-Z][a-zA-Z &]+)'  # Example pattern
    }

    metadata = {}
    for field, pattern in metadata_patterns.items():
        matches = re.findall(pattern, text)
        metadata[field] = matches

    return {
        "extracted_text": text,
        "metadata": metadata
    }
root_agent=Agent(
    name="dock_text",
    model="gemini-2.0-flash",
    description="A tool agent",
    instruction="""You're a specialist in document extraction.""",
    tools=[dock_text_tool],
)