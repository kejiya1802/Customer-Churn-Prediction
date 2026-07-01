import os
print(os.getcwd())
file_path = "data/raw/Telco-Customer-Churn.csv"
print(os.path.exists(file_path))
if os.path.exists(file_path):
    print(os.path.getsize(file_path))