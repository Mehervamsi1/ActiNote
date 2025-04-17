from docx import Document
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def chat_with_groq(client, prompt, model, response_format):
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

# --- new helper to load the transcript ---
def load_transcript(path):
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

# Use a raw‐string literal or double backslashes for Windows paths:
transcript_path = r"C:\Users\sa2324\OneDrive - UNT System\Desktop\Projects\Transcript Teams Meet Sample.docx"
transcript = load_transcript(transcript_path)

groq_key = os.getenv('GROQ_API_KEY')
client = Groq(api_key=groq_key)
model = "llama3-8b-8192"

# load the prompt template
with open("meeting_prompt.txt", "r", encoding="utf-8") as f:
    prompt_template = f.read()

# inject your transcript text
full_prompt = prompt_template.format(transcript=transcript)


llm_response = chat_with_groq(client, full_prompt, model, {"type": "json_object"})
print(llm_response)
