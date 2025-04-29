import json
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API"))
transcript_data='code/trail_meeting.json'

# def groq_generate_summary(transcript_data):
#     # transcript_data is a list of {"time", "speaker", "message"}

#     transcript_text = "\n".join(
#         [f"[{entry['time']}] {entry['speaker']}: {entry['message']}" for entry in transcript_data]
#     )

#     prompt = f"""
#     You are a smart meeting assistant.
    
#     Here is the meeting transcript:

#     {transcript_text}

#     Summarize the meeting and output JSON format with:
#     - overall_summary
#     - attendees: each with name, email, their discussion summary, and any assigned tasks (if any).

#     Respond ONLY with JSON.
#     """

#     response = client.chat.completions.create(
#         model="llama3-8b-8192",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.2
#     )

#     try:
#         text = response.choices[0].message.content.strip()
#         if text.startswith("{"):
#             return json.loads(text)
#         else:
#             print("Groq did not return valid JSON:", text)
#             return {}
#     except Exception as e:
#         print("Error parsing Groq response:", e)
#         return {}
    
# groq_generate_summary(transcript_data)


#+____________________________________________________________________________________________


# def groq_generate_summary(transcript_path):
#     # Load JSON file
#     with open(transcript_path, 'r') as file:
#         full_data = json.load(file)

#     discussion_entries = full_data["meeting"]["discussion"]

#     # Create readable transcript
#     transcript_text = "\n".join(
#         [f"{entry['speaker']}: {entry['message']}" for entry in discussion_entries]
#     )

#     prompt = f"""
#     You are a smart meeting assistant.

#     Here is the meeting transcript:

#     {transcript_text}

#     Summarize the meeting and output JSON format with:
#     - overall_summary
#     - attendees: each with name, email, their discussion summary, and any assigned tasks (if any).

#     Respond ONLY with JSON.
#     """

#     response = client.chat.completions.create(
#         model="llama3-8b-8192",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.2
#     )

#     try:
#         text = response.choices[0].message.content.strip()
#         if text.startswith("{"):
#             return json.loads(text)
#         else:
#             print("Groq did not return valid JSON:", text)
#             return {}
#     except Exception as e:
#         print("Error parsing Groq response:", e)
#         return {}

# # Call with file path
# groq_generate_summary('code/trail_meeting.json')


#_______________________________________________________________________

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API"))

def groq_generate_summary(transcript_path):
    with open(transcript_path, 'r') as file:
        full_data = json.load(file)

    discussion = full_data["meeting"]["discussion"]
    participants = full_data["meeting"]["participants"]

    transcript_text = "\n".join([f"{entry['speaker']}: {entry['message']}" for entry in discussion])

    prompt = f"""
    You are a smart meeting assistant.

    Here is the meeting transcript:

    {transcript_text}

    Summarize the meeting and output JSON format with:
    - overall_summary
    - attendees: each with name, email, their discussion summary, and any assigned tasks (if any).

    Respond ONLY with JSON.
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    print("RAW RESPONSE FROM GROQ:\n", response.choices[0].message.content)

    text = response.choices[0].message.content.strip()
    return json.loads(text) if text.startswith("{") else {}