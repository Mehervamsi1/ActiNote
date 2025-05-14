# def generate_email_body(name, personal_summary, overall_summary, tasks):
#     task_html = "<ul>" + "".join(f"<li>{t}</li>" for t in tasks) + "</ul>" if tasks else "<p>No tasks assigned.</p>"
#     html_body = f"""
#     <html><body>
#     <p>Hi <b>{name}</b>,</p>
#     <p>{personal_summary}</p>
#     <h3>Meeting Summary:</h3><p>{overall_summary}</p>
#     <h4>Tasks:</h4>{task_html}
#     <p>– NextMOM AI Assistant</p>
#     </body></html>
#     """
#     return html_body

# async def send_email(graph_client, sender_email, recipient_email, subject, html_body):
#     message = {
#         "message": {
#             "subject": subject,
#             "body": {"contentType": "HTML", "content": html_body},
#             "toRecipients": [{"emailAddress": {"address": recipient_email}}]
#         },
#         "saveToSentItems": "false"
#     }
#     await graph_client.users.by_user_id(sender_email).send_mail.post(body=message)


#Testing

import json

# Simulated Groq summary response
groq_response = {
    "overall_summary": "The team discussed the Full Stack Python Project updates, covering backend services, frontend development, infrastructure setup, and data science.",
    "attendees": [
        {
            "name": "Meher D",
            "email": "",
            "summary": "Backend services are coming along well...",
            "tasks": ["Finalize schema for 'user activity logs'"]
        },
        {
            "name": "Syam A",
            "email": "",
            "summary": "Frontend base is ready...",
            "tasks": []
        },
        {
            "name": "Daniel Martinez",
            "email": "",
            "summary": "Infrastructure setup is progressing...",
            "tasks": ["Finalize AWS architecture"]
        },
        {
            "name": "Emily Davis",
            "email": "",
            "summary": "Exploring smart recommendations...",
            "tasks": ["Get sample data from dev database"]
        }
    ]
}

# Original participant info from your JSON file
participants = [
    {"name": "Pragna P", "email": "PragnaP@AIReactor.onmicrosoft.com", "role": "Project Manager"},
    {"name": "Meher D", "email": "meherd@aieactor.onmicrosoft.com", "role": "Backend Developer"},
    {"name": "Syam A", "email": "syama@aireactor.onmicrosoft.com", "role": "Frontend Developer"},
    {"name": "Daniel Martinez", "email": "dm@AIReactor.onmicrosoft.com", "role": "DevOps Engineer"},
    {"name": "Emily Davis", "email": "ed@AIReactor.onmicrosoft.com", "role": "Data Scientist"}
]

# Inject emails from participants into Groq response
email_lookup = {p["name"]: p["email"] for p in participants}

for attendee in groq_response["attendees"]:
    if not attendee.get("email"):
        attendee["email"] = email_lookup.get(attendee["name"])

# Output the result to verify
print(json.dumps(groq_response["attendees"], indent=2))
