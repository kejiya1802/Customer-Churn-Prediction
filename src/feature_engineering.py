import pandas as pd
import os


def create_features(df):

    df = df.copy()

    # Convert target
    if "Churn" in df.columns:
        df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    # Binary encoding
    binary_cols = ["gender", "Partner", "Dependents", "PhoneService", "PaperlessBilling"]

    for col in binary_cols:
        if col in df.columns:
            df[col] = df[col].map({"Yes": 1, "No": 0, "Male": 1, "Female": 0})

    # One-hot encoding
    df = pd.get_dummies(df)

    # Save processed file
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/final_data.csv", index=False)

    print("Feature engineering completed!")
    print("Final shape:", df.shape)

    return df