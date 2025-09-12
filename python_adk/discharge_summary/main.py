from fastapi import FastAPI,UploadFile,File
import shutil
from agent_text_extract.agent import extract_text_from_image
from agent_summary_generation.agent import generate_discharge_summary
from agent_simplify_medical_terms.agent import simplify_medical_terms

app=FastAPI()

@app.post("/extract_text/")
async def process_document(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_image(temp_file)

    professional_summary = generate_discharge_summary(extracted_text)

    patient_friendly = simplify_medical_terms(professional_summary)

    return {
        "status": "complete",
        "steps": ["text_extracted", "summary_generated", "simplified"],
        "results": {
            "extracted_text": extracted_text,
            "professional_summary_text": professional_summary,
            "patient_friendly_text": patient_friendly,
        },
        "error": None
    }
