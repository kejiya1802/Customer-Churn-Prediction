import pandas as pd
import os

file_path = "data/raw/Telco-Customer-Churn.csv"

print("File exists:", os.path.exists(file_path))

df = pd.read_csv(file_path)

print(df.head())
print(df.shape)