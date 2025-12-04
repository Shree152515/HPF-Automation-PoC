import pandas as pd
from datetime import datetime, timedelta
import os
import smtplib
from email.mime.text import MIMEText

SEND_EMAIL = False
SMTP_SERVER = "smtp.office365.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@hpf.org"
PASSWORD = "YOUR_PASSWORD"

df = pd.read_csv("foundation_deadlines.csv")
df['deadline_date'] = pd.to_datetime(df['deadline_date'])
today = pd.to_datetime("today")
upcoming = df[(df['deadline_date'] >= today) & (df['deadline_date'] <= today + timedelta(days=7))]

mock_folder = "mock_reminders"
os.makedirs(mock_folder, exist_ok=True)

for idx, row in upcoming.iterrows():
    subject = f"Reminder - {row['task']}"
    body = f"Dear Team,\n\nThis is a reminder that the task '{row['task']}' for project '{row['project']}' is due on {row['deadline_date'].date()}."
    filename = f"reminder_{row['project']}_{row['task'].replace(' ','_')}.txt"
    with open(os.path.join(mock_folder,filename),"w") as f:
        f.write(f"Subject: {subject}\nTo: {row['responsible_email']}\n\n{body}")
    
    if SEND_EMAIL:
        try:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = SENDER_EMAIL
            msg['To'] = row['responsible_email']
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SENDER_EMAIL, PASSWORD)
                server.send_message(msg)
            print(f"Email sent to {row['responsible_email']}")
        except Exception as e:
            print(f"Failed to send email: {e}")

print("Deadline Reminder PoC completed!")