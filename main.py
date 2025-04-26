import asyncio
import json
from code.model_trail import groq_generate_summary
from code.emailer import generate_email_body, send_email
from dotenv import load_dotenv
import os

load_dotenv()

async def process():
    graph_client = None  # Placeholder
    sender_email = os.getenv("SENDER_EMAIL")
    file_path = "code/Economic_Sanctions_Transcript.json"  # Path to your JSON file

    # Load transcript (JSON)
    with open(file_path, 'r') as f:
        transcript_data = json.load(f)

    # Generate Summary
    summary_data = groq_generate_summary(transcript_data)

    # Send Emails
    for attendee in summary_data["attendees"]:
        html_body = generate_email_body(
            attendee["name"],
            attendee["summary"],
            summary_data["overall_summary"],
            attendee.get("tasks", [])
        )
        print(f"Email to {attendee['email']}:")
        print(html_body)
        print("-" * 80)
        # Uncomment when ready to send
        await send_email(graph_client, sender_email, attendee["email"], "Meeting Summary", html_body)

if __name__ == "__main__":
    asyncio.run(process())
