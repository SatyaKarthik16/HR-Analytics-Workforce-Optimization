📄 analytics_hr.py – KPI Calculations & Summaries



import pandas as pd

def calculate_kpis(df):
    attrition_rate = df['LeftCompany'].mean()
    avg_engagement = df['EngagementScore'].mean()
    avg_training = df['TrainingHours'].mean()

    print(f"Attrition Rate: {attrition_rate:.2%}")
    print(f"Average Engagement Score: {avg_engagement:.2f}")
    print(f"Average Training Hours: {avg_training:.2f}")

if __name__ == "__main__":
    df = pd.read_csv("data/synthetic_hr_data.csv")
    calculate_kpis(df)
