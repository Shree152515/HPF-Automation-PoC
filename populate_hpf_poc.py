import os

# Base path
base_path = r"C:\Users\Harish\Documents\HPF_Automation\HPF-Automation-PoC"

# ---------------------------
# 1️⃣ Grant Tracker
# ---------------------------
grant_tracker_code = """import pandas as pd
from datetime import datetime

df = pd.read_csv("grant_disbursements.csv")
df['disbursement_date'] = pd.to_datetime(df['disbursement_date'])

summary = df.groupby(['focus_area','country'])['amount'].sum().reset_index()
summary.to_excel("grant_summary_report.xlsx", index=False)

summary_text = "Executive Summary of Grant Disbursements:\\n"
for i, row in summary.iterrows():
    summary_text += f"- {row['focus_area']} in {row['country']}: ${row['amount']}\\n"

with open("grant_summary_text.txt", "w") as f:
    f.write(summary_text)

print("Grant Tracker PoC completed!")"""

grant_tracker_readme = """# Grant Tracker PoC
Tracks grant disbursements and generates summary reports.
- Input: grant_disbursements.csv
- Output: grant_summary_report.xlsx, grant_summary_text.txt
- Run: python grant_tracker.py"""

with open(os.path.join(base_path,"1_Grant_Tracker","grant_tracker.py"),"w") as f:
    f.write(grant_tracker_code)
with open(os.path.join(base_path,"1_Grant_Tracker","README.md"),"w") as f:
    f.write(grant_tracker_readme)

# ---------------------------
# 2️⃣ Project KPI Dashboard
# ---------------------------
kpi_dashboard_code = """import pandas as pd

df = pd.read_excel("project_participation.xlsx")
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['project_name','beneficiary_id'])

kpi = df.groupby(['project_name','country']).agg(
    beneficiaries=('beneficiary_id','nunique'),
    events=('event_id','nunique')
).reset_index()

kpi.to_excel("project_kpi_dashboard.xlsx", index=False)
print("KPI Dashboard saved as project_kpi_dashboard.xlsx")"""

kpi_dashboard_readme = """# Project KPI Dashboard
Aggregates project participation and events.
- Input: project_participation.xlsx
- Output: project_kpi_dashboard.xlsx
- Run: python kpi_dashboard.py"""

with open(os.path.join(base_path,"2_Project_KPI_Dashboard","kpi_dashboard.py"),"w") as f:
    f.write(kpi_dashboard_code)
with open(os.path.join(base_path,"2_Project_KPI_Dashboard","README.md"),"w") as f:
    f.write(kpi_dashboard_readme)

# ---------------------------
# 3️⃣ Document Archiving
# ---------------------------
doc_archiver_code = """import os, shutil

incoming_folder = "incoming_docs"
archive_folder = "archive"
files = os.listdir(incoming_folder)

for fname in files:
    if fname.lower().endswith(('.pdf','.docx')):
        try:
            parts = fname.split('_')
            project, date, doc_type = parts[0], parts[1], parts[2].split('.')[0]
            dest_folder = os.path.join(archive_folder, project, date)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(os.path.join(incoming_folder,fname), os.path.join(dest_folder,fname))
            print(f"Moved {fname} -> {dest_folder}")
        except Exception as e:
            print(f"Error processing {fname}: {e}")

print("Document archiving completed!")"""

doc_archiver_readme = """# Document Archiving
Organizes project documents automatically.
- Input: files in incoming_docs/
- Output: archive/ProjectName/Date/
- Run: python doc_archiver.py"""

with open(os.path.join(base_path,"3_Document_Archiving","doc_archiver.py"),"w") as f:
    f.write(doc_archiver_code)
with open(os.path.join(base_path,"3_Document_Archiving","README.md"),"w") as f:
    f.write(doc_archiver_readme)

# ---------------------------
# 4️⃣ Deadline Reminder
# ---------------------------
reminder_system_code = """import pandas as pd
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
    body = f"Dear Team,\\n\\nThis is a reminder that the task '{row['task']}' for project '{row['project']}' is due on {row['deadline_date'].date()}."
    filename = f"reminder_{row['project']}_{row['task'].replace(' ','_')}.txt"
    with open(os.path.join(mock_folder,filename),"w") as f:
        f.write(f"Subject: {subject}\\nTo: {row['responsible_email']}\\n\\n{body}")
    
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

print("Deadline Reminder PoC completed!")"""

reminder_system_readme = """# Deadline Reminder
Generates upcoming task reminders.
- Input: foundation_deadlines.csv
- Output: mock reminders in mock_reminders/
- Optional: can send real emails via SMTP
- Run: python reminder_system.py"""

with open(os.path.join(base_path,"4_Deadline_Reminder","reminder_system.py"),"w") as f:
    f.write(reminder_system_code)
with open(os.path.join(base_path,"4_Deadline_Reminder","README.md"),"w") as f:
    f.write(reminder_system_readme)

# ---------------------------
# 5️⃣ AI-Assisted Grant Reports
# ---------------------------
ai_report_code = """import pandas as pd
import os

df = pd.read_csv("grant_summary.csv")
output_folder = "project_reports"
os.makedirs(output_folder, exist_ok=True)

for idx, row in df.iterrows():
    report_text = f\"\"\"Project Report: {row['project_name']}
Focus Area: {row['focus_area']}
Budget: ${row['budget']}

Milestones Achieved:
{row['milestones']}

Outcomes:
{row['outcomes']}

Summary:
The {row['project_name']} project under {row['focus_area']} has successfully achieved its planned milestones and delivered meaningful outcomes.
\"\"\"
    filename = os.path.join(output_folder, f"{row['project_name']}_report.txt")
    with open(filename,"w") as f:
        f.write(report_text.strip())
    print(f"Report generated: {filename}")

print("AI-Assisted Grant Reports PoC completed!")"""

ai_report_readme = """# AI-Assisted Grant Reports
Auto-generates project reports.
- Input: grant_summary.csv
- Output: project_reports/
- Run: python ai_report_generator.py"""

with open(os.path.join(base_path,"5_AI_Grant_Reports","ai_report_generator.py"),"w") as f:
    f.write(ai_report_code)
with open(os.path.join(base_path,"5_AI_Grant_Reports","README.md"),"w") as f:
    f.write(ai_report_readme)

print("All Python scripts and README files populated successfully!")
