import pandas as pd

df = pd.read_excel("project_participation.xlsx")
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['project_name','beneficiary_id'])

kpi = df.groupby(['project_name','country']).agg(
    beneficiaries=('beneficiary_id','nunique'),
    events=('event_id','nunique')
).reset_index()

kpi.to_excel("project_kpi_dashboard.xlsx", index=False)
print("KPI Dashboard saved as project_kpi_dashboard.xlsx")