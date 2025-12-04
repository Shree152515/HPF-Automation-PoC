import pandas as pd
import os

df = pd.read_csv("grant_summary.csv")
output_folder = "project_reports"
os.makedirs(output_folder, exist_ok=True)

for idx, row in df.iterrows():
    report_text = f"""Project Report: {row['project_name']}
Focus Area: {row['focus_area']}
Budget: ${row['budget']}

Milestones Achieved:
{row['milestones']}

Outcomes:
{row['outcomes']}

Summary:
The {row['project_name']} project under {row['focus_area']} has successfully achieved its planned milestones and delivered meaningful outcomes.
"""
    filename = os.path.join(output_folder, f"{row['project_name']}_report.txt")
    with open(filename,"w") as f:
        f.write(report_text.strip())
    print(f"Report generated: {filename}")

print("AI-Assisted Grant Reports PoC completed!")