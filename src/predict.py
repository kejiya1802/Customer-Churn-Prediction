import pandas as pd
import joblib
import numpy as np

# -------------------------
# LOAD MODEL + SCALER
# -------------------------
model = joblib.load("models/best_model.pkl")
scaler = joblib.load("models/scaler.pkl")


def predict_churn(input_dict):
    """
    input_dict: dictionary with customer features
    returns: prediction + probability
    """

    # Convert input to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Ensure numeric
    input_df = input_df.apply(pd.to_numeric, errors='coerce').fillna(0)

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    return {
        "churn_prediction": int(prediction),
        "churn_probability": float(probability)
    }


# -------------------------
# TEST RUN
# -------------------------
if __name__ == "__main__":

    sample_input = {
        "gender": 1,
        "SeniorCitizen": 0,
        "Partner": 1,
        "Dependents": 0,
        "tenure": 12,
        "MonthlyCharges": 70,
        "TotalCharges": 800
    }

    result = predict_churn(sample_input)

    print("Prediction Result:")
    print(result)