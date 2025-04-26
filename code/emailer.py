def generate_email_body(name, personal_summary, overall_summary, tasks):
    task_html = "<ul>" + "".join(f"<li>{t}</li>" for t in tasks) + "</ul>" if tasks else "<p>No tasks assigned.</p>"
    html_body = f"""
    <html><body>
    <p>Hi <b>{name}</b>,</p>
    <p>{personal_summary}</p>
    <h3>Meeting Summary:</h3><p>{overall_summary}</p>
    <h4>Tasks:</h4>{task_html}
    <p>– NextMOM AI Assistant</p>
    </body></html>
    """
    return html_body

async def send_email(graph_client, sender_email, recipient_email, subject, html_body):
    message = {
        "message": {
            "subject": subject,
            "body": {"contentType": "HTML", "content": html_body},
            "toRecipients": [{"emailAddress": {"address": recipient_email}}]
        },
        "saveToSentItems": "false"
    }
    await graph_client.users.by_user_id(sender_email).send_mail.post(body=message)


#Testing
