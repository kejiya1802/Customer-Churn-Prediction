import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report


def test_model():

    # Load data
    df = pd.read_csv("data/processed/final_data.csv")

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    # Load model + scaler
    model = joblib.load("models/best_model.pkl")
    scaler = joblib.load("models/scaler.pkl")

    # Scale
    X_scaled = scaler.transform(X)

    # Predict
    y_pred = model.predict(X_scaled)

    # Results
    print("Model Evaluation")
    print("----------------")
    print("Accuracy:", accuracy_score(y, y_pred))
    print("\nClassification Report:\n", classification_report(y, y_pred))


if __name__ == "__main__":
    test_model()