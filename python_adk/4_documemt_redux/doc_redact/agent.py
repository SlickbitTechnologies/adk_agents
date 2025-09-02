from google.adk.agents import Agent 

import PyPDF2

def doc_redux_tool(file_path: str) -> dict:
    """Extract text from a document."""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return {"extracted_text": text}

root_agent=Agent(
    name="doc_redux",
    model="gemini-2.0-flash",
    description="A tool agent",
    instruction="""You're a specialist in document extraction.""",
    tools=[doc_redux_tool],
)