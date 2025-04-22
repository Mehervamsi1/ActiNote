#################### File reading Test ########################
from docx import Document
from main import chat_with_groq
from groq import Groq
import os

def read_docx_transcript(file_path):
    try:
        doc = Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        transcript_local = "\n".join(full_text)
        return transcript_local
    except Exception as e:
        print(f"Error reading the .docx file: {e}")
        return None
    
    
file_path = "code\Transcript Teams Meet Sample.docx"

transcript_local = read_docx_transcript(file_path)

if transcript_local:
    print("Successfully read transcript:")
    print(transcript_local[:500])  # print preview of the first 500 chars
else:
    print("Could not read the transcript.")

groq_key= os.getenv('grok_api')
client = Groq(api_key=groq_key)
model = "llama3-8b-8192"

prompt = str(transcript_local)+"\n\nCan you please summarize this?"

full_prompt=str(transcript_local)+"\n\nCan you please summarize this?"

llm_response = chat_with_groq(client, full_prompt, model,{"type": "json_object"})
print(llm_response)
