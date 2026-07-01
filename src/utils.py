import numpy as np
import pandas as pd
import joblib


# -------------------------
# LOAD MODEL & SCALER
# -------------------------
def load_model(model_path="models/best_model.pkl"):
    return joblib.load(model_path)


def load_scaler(scaler_path="models/scaler.pkl"):
    return joblib.load(scaler_path)


# -------------------------
# PREPROCESS INPUT
# -------------------------
def preprocess_input(input_dict, scaler):
    """
    Converts user input into model-ready format
    """

    df = pd.DataFrame([input_dict])

    # Convert everything to numeric safely
    df = df.apply(pd.to_numeric, errors='coerce').fillna(0)

    # Scale data
    scaled_data = scaler.transform(df)

    return scaled_data


# -------------------------
# PREDICTION FUNCTION
# -------------------------
def make_prediction(model, data):
    """
    Returns prediction + probability
    """

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }


# -------------------------
# TEST RUN
# -------------------------
if __name__ == "__main__":

    model = load_model()
    scaler = load_scaler()

    sample_input = {
        "gender": 1,
        "SeniorCitizen": 0,
        "Partner": 1,
        "Dependents": 0,
        "tenure": 10,
        "MonthlyCharges": 70,
        "TotalCharges": 800
    }

    processed = preprocess_input(sample_input, scaler)
    result = make_prediction(model, processed)

    print("Prediction Result:", result)