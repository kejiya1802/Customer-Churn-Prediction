import pandas as pd
import os


# -------------------------
# LOAD RAW DATA
# -------------------------
def load_raw_data():
    file_path = "data/raw/Telco-Customer-Churn.csv"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)
    return df


# -------------------------
# CLEAN DATA
# -------------------------
def clean_data(df):

    df = df.copy()

    # Drop ID column
    if "customerID" in df.columns:
        df.drop("customerID", axis=1, inplace=True)

    # Fix TotalCharges issue
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Fill missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

    return df


# -------------------------
# SAVE CLEANED DATA
# -------------------------
def save_cleaned_data(df):
    os.makedirs("data/processed", exist_ok=True)
    path = "data/processed/cleaned_data.csv"
    df.to_csv(path, index=False)
    return path


# -------------------------
# RUN PIPELINE (OPTIONAL)
# -------------------------
if __name__ == "__main__":
    df = load_raw_data()
    print("Raw data shape:", df.shape)

    df = clean_data(df)
    print("Cleaned data shape:", df.shape)

    path = save_cleaned_data(df)
    print("Saved at:", path)