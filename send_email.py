#!/Users/iyke/automation/CAC_Info/venv/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

# Email credentials and SMTP server configuration
sender_email = "iyke_97@yahoo.com"
receiver_email = "iyke497@gmail.com"
password = "suqznyxgwwsorgjt"  # Be cautious with your password 

# Create the MIME structure
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = f"Python Script run successfully: {sys.argv[1]} - {sys.argv[2]}"

# Email body
body = "Hello, this is a test email sent from a Python script using SMTP library."
message.attach(MIMEText(body, "plain"))

# Connect to Gmail's SMTP server
server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
server.starttls()  # Secure the connection

try:
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email has been sent successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    server.quit()
