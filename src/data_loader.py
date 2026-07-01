import pandas as pd
import os

def load_raw_data():
    file_path = "data/raw/Telco-Customer-Churn.csv"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at: {file_path}")
    
    df = pd.read_csv(file_path)
    return df


def load_cleaned_data():
    file_path = "data/processed/cleaned_data.csv"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Cleaned dataset not found at: {file_path}")
    
    df = pd.read_csv(file_path)
    return df


def load_final_data():
    file_path = "data/processed/final_data.csv"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Final dataset not found at: {file_path}")
    
    df = pd.read_csv(file_path)
    return df


# Quick test run
if __name__ == "__main__":
    df = load_raw_data()
    print("Raw data loaded:", df.shape)

    df2 = load_cleaned_data()
    print("Cleaned data loaded:", df2.shape)

    df3 = load_final_data()
    print("Final data loaded:", df3.shape)