import os
import joblib

def save_model(model, scaler, model_dir="models"):
    """
    Saves trained model and scaler into /models folder
    """

    # Create folder if it doesn't exist
    os.makedirs(model_dir, exist_ok=True)

    # Save model
    model_path = os.path.join(model_dir, "best_model.pkl")
    joblib.dump(model, model_path)

    # Save scaler
    scaler_path = os.path.join(model_dir, "scaler.pkl")
    joblib.dump(scaler, scaler_path)

    print(f"Model saved at: {model_path}")
    print(f"Scaler saved at: {scaler_path}")


# -------------------------
# TEST RUN (optional)
# -------------------------
if __name__ == "__main__":
    print("This file is used to save trained models.")