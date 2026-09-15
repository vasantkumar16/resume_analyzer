import smtplib
from email.mime.text import MIMEText
from config import Config


def send_decision_email(to_email, candidate_name, job_title, decision):
    if not to_email:
        raise ValueError("Candidate email is missing.")

    subject = (
        f"Application Update - {job_title}"
    )

    if decision == "selected":
        body = (
            f"Dear {candidate_name},\n\n"
            f"Congratulations! You have been shortlisted/selected for {job_title}. "
            "The recruiter will contact you with the next steps.\n\nRegards"
        )
    else:
        body = (
            f"Dear {candidate_name},\n\n"
            f"Thank you for your interest in {job_title}. "
            "After reviewing your application, we will not be moving forward at this time.\n\n"
            "Regards"
        )

    if not Config.MAIL_ENABLED:
        return "Email sending is disabled. Configure SMTP in .env to send real emails."

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = Config.SMTP_FROM or Config.SMTP_USERNAME
    message["To"] = to_email

    with smtplib.SMTP(Config.SMTP_HOST, Config.SMTP_PORT) as server:
        server.starttls()
        server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
        server.send_message(message)

    return "Email sent successfully."
