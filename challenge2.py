import os
import smtplib
from email.message import EmailMessage

msg = EmailMessage()

sender_mail = "your_mail@gmail.com"  # replace with your actual email address
receiver_mail = "hr@ignitershub.com"

msg["Subject"] = "Challenge 3 completed"
msg["From"] = sender_mail
msg["To"] = receiver_mail

mail_body = """
Name: Manmohit Singh Bisht
Semester: 7th
Branch: CSE
Roll Number: 230180101030
"""
msg.set_content(mail_body)

image_path = "image.jpeg"
with open(image_path, "rb") as image_file:
    image_data = image_file.read()
    msg.add_attachment(
        image_data,
        maintype="image",
        subtype="jpeg",
        filename=os.path.basename(image_path),
    )

app_password = "xxxx xxxx xxxx xxxx"  # replace with actual google app password

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_mail, app_password)
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
