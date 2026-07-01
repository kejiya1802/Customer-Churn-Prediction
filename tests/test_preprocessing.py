import sys
import os

# -------------------------
# FIX PATH FIRST (IMPORTANT)
# -------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from src.preprocessing import load_raw_data


# -------------------------
# TEST RAW DATA LOAD
# -------------------------
def test_raw_data():
    df = load_raw_data()

    print("Raw Data Loaded Successfully")
    print("Shape:", df.shape)

    assert df is not None
    assert df.shape[0] > 0


# -------------------------
# TEST DATA FILE PATHS
# -------------------------
def test_file_paths():

    raw_path = "data/raw/Telco-Customer-Churn.csv"
    processed_path = "data/processed/cleaned_data.csv"

    print("Checking file paths...")

    assert os.path.exists(raw_path), "Raw dataset missing!"
    print("Raw dataset exists ✔")

    assert os.path.exists(processed_path), "Processed dataset missing!"
    print("Processed dataset exists ✔")


# -------------------------
# TEST CLEANED DATA
# -------------------------
def test_cleaned_data():

    df = pd.read_csv("data/processed/cleaned_data.csv")

    print("Cleaned Data Loaded Successfully")
    print("Shape:", df.shape)

    assert "customerID" not in df.columns
    assert df.isnull().sum().sum() == 0

    print("No missing values ✔")
    print("No customerID column ✔")


# -------------------------
# RUN TESTS
# -------------------------
if __name__ == "__main__":
    test_raw_data()
    test_file_paths()
    test_cleaned_data()

    print("\nAll preprocessing tests passed successfully ✔")