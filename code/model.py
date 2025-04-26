import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("groq_api"))

transcript = "code\Economic_Sanctions_Transcript.json"

def groq_generate_summary(transcript):
    prompt = f"""
    You are a smart meeting assistant. Summarize the following meeting transcript:
    
    {transcript}

    Return JSON with:
    1. overall_summary
    2. attendees: name, email, summary, tasks (if any)
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192" ,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    try:
        text = response.choices[0].message.content.strip()
        summary_json = eval(text) if text.startswith("{") else {}
        return summary_json
    except Exception as e:
        print("Error parsing Groq response:", e)
        return {}


# def groq_summary_test(transcript):
#     prompt =f"""You have a transcript which will be given to you please extract overall 
#     summary attendees: name, email, summary, tasks (if any)"""

### Testing

text = groq_generate_summary(transcript)

print(text)