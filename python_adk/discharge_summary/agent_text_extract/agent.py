from google.adk.agents import Agent
import google.generativeai as genai
import PyPDF2   
import easyocr
from PIL import Image
import io

def extract_text_from_image(image_path:str) ->str:
    reader = easyocr.Reader(['en'])
    image = Image.open(image_path)
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes = image_bytes.getvalue()
    result = reader.readtext(image_bytes, detail=0)
    raw_text = "\n".join(result)

    prompt = f"""
    The following text was extracted using OCR and may contain errors:
    {raw_text}

    Please correct spelling, fix formatting, and return only the cleaned text.
    """

   
    return prompt

# root_agent = Agent(
#     name="agent_text_extract",
#     description="Extract text from images",
#     model="gemini-2.0-flash",
#     instruction="Extract and clean text from the image and return only the cleaned text.",
#     tools=[extract_text_from_image],    
# )
