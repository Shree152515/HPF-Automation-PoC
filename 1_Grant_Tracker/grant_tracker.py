import pandas as pd
from datetime import datetime

df = pd.read_csv("grant_disbursements.csv")
df['disbursement_date'] = pd.to_datetime(df['disbursement_date'])

summary = df.groupby(['focus_area','country'])['amount'].sum().reset_index()
summary.to_excel("grant_summary_report.xlsx", index=False)

summary_text = "Executive Summary of Grant Disbursements:\n"
for i, row in summary.iterrows():
    summary_text += f"- {row['focus_area']} in {row['country']}: ${row['amount']}\n"

with open("grant_summary_text.txt", "w") as f:
    f.write(summary_text)

print("Grant Tracker PoC completed!")