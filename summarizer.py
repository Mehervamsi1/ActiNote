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

full_prompt = f"""
You are a meeting assistant. Analyze the following Microsoft Teams meeting transcript and extract the following:
1. A concise summary of the entire meeting.
2. The main agenda(s) discussed.
3. The key takeaways or action items.
4. Determine whether a follow‐up meeting was discussed:
   - If yes, extract the proposed date, time, and purpose of the next meeting.
   - If no, respond with: "No follow‐up meeting discussed."

Provide your answer as a JSON object with these keys:
- summary (string)
- agendas (array of strings)
- action_items (array of strings)
- follow_up (object with keys "date", "time", "purpose", or the string "No follow-up meeting discussed")

Transcript:
{transcript}
"""

llm_response = chat_with_groq(client, full_prompt, model, {"type": "json_object"})
print(llm_response)
