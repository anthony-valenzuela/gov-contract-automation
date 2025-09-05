"""
Send email alert when a new bid is found.
"""

import smtplib
from email.message import EmailMessage

def send_alert(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = "your_email@example.com"
    msg["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your_email@example.com", "your_password")  # Use app password/env vars!
        server.send_message(msg)

if __name__ == "__main__":
    send_alert("New LA County Bid", "A new bid was posted! Check the portal.", "your_team@example.com")
