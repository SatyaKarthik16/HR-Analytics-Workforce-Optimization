📄 etl_hr.py – Load & Clean HR Data


import pandas as pd

def load_and_clean_hr_data(filepath):
    df = pd.read_csv(filepath)
    df['HireDate'] = pd.to_datetime(df['HireDate'])
    df['EngagementScore'] = df['EngagementScore'].clip(1, 5)
    df['Tenure'] = pd.to_datetime("2025-06-01") - df['HireDate']
    df['Tenure'] = df['Tenure'].dt.days // 365
    return df

if __name__ == "__main__":
    df = load_and_clean_hr_data("data/synthetic_hr_data.csv")
    print(df.head())
