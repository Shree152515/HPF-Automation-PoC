# HPF Automation PoC

5 Python automation scripts that remove manual administrative work from grant management operations. Built as a proof of concept for a foundation managing international projects across education, conservation and arts.

Each script targets one specific bottleneck in the grant lifecycle and can be run independently.

---

## The 5 scripts

### 1. Grant Tracker
Reads a CSV of grant disbursements, groups totals by focus area and country, and outputs two files: a formatted Excel summary report and a plain text executive summary.

- Input: grant_disbursements.csv
- Output: grant_summary_report.xlsx, grant_summary_text.txt
- Run: python grant_tracker.py

### 2. Project KPI Dashboard
Reads project participation data from Excel, deduplicates beneficiary and event records, and produces a clean KPI dashboard showing unique beneficiaries and events per project per country.

- Input: project_participation.xlsx
- Output: project_kpi_dashboard.xlsx
- Run: python kpi_dashboard.py

### 3. Document Archiving
Scans an incoming documents folder for PDF and DOCX files, parses each filename for project name and date, and automatically moves files into a structured archive folder organised by project and date.

- Input: files in incoming_docs/ named as Project_Date_Type.pdf
- Output: archive/ProjectName/Date/
- Run: python doc_archiver.py

### 4. Deadline Reminder
Reads a CSV of upcoming tasks and deadlines, filters for anything due within the next 7 days, and generates reminder text files per task. Can optionally send real emails via SMTP by setting SEND_EMAIL to True.

- Input: foundation_deadlines.csv
- Output: reminder text files in mock_reminders/
- Optional: live email delivery via SMTP (Office365)
- Run: python reminder_system.py

### 5. Automated Grant Report Generator
Reads a project summary CSV and generates a formatted text report for each project, filling in focus area, budget, milestones and outcomes from the data. Removes the need to manually write the same report structure repeatedly.

- Input: grant_summary.csv
- Output: one .txt report per project in project_reports/
- Run: python ai_report_generator.py

---

## Tech stack

- Python 3
- pandas (data processing and aggregation)
- openpyxl (Excel read/write)
- smtplib (email delivery)
- os / shutil (file system automation)

## How to install dependencies

pip install pandas openpyxl

## What this demonstrates

- Data aggregation and grouping with pandas
- File system automation with os and shutil
- Scheduled-style deadline monitoring
- Template-driven document generation
- End-to-end automation of repetitive admin workflows
