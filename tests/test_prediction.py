import joblib
import pandas as pd

# Load model + scaler
model = joblib.load("models/best_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Load training feature columns (IMPORTANT FIX)
df_train = pd.read_csv("data/processed/final_data.csv")
feature_columns = df_train.drop("Churn", axis=1).columns

# -------------------------
# SAMPLE INPUT (RAW)
# -------------------------
sample_customer = {
    "gender": 1,
    "SeniorCitizen": 0,
    "Partner": 1,
    "Dependents": 0,
    "tenure": 24,
    "MonthlyCharges": 70,
    "TotalCharges": 1600
}

# Convert to DataFrame
input_df = pd.DataFrame([sample_customer])

# -------------------------
# ALIGN FEATURES (KEY FIX)
# -------------------------
input_df = pd.get_dummies(input_df)

# Add missing columns
for col in feature_columns:
    if col not in input_df.columns:
        input_df[col] = 0

# Reorder columns to match training
input_df = input_df[feature_columns]

# -------------------------
# SCALE + PREDICT
# -------------------------
input_scaled = scaler.transform(input_df)

prediction = model.predict(input_scaled)[0]
probability = model.predict_proba(input_scaled)[0][1]

# -------------------------
# OUTPUT
# -------------------------
print("Customer Churn Prediction Test")
print("------------------------------")

if prediction == 1:
    print("Result: Customer WILL CHURN ⚠")
else:
    print("Result: Customer WILL STAY ✅")

print("Churn Probability:", round(probability, 4))