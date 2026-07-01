import pandas as pd
import joblib
import shap
import numpy as np

# Load dataset
df = pd.read_csv("data/processed/final_data.csv")

X = df.drop("Churn", axis=1)

# Ensure numeric clean data
X = X.apply(pd.to_numeric, errors='coerce').fillna(0)

# Load model
model = joblib.load("models/best_model.pkl")

# -------------------------
# SAFE SHAP (MODEL AGNOSTIC)
# -------------------------
explainer = shap.KernelExplainer(model.predict, X.sample(100))
shap_values = explainer.shap_values(X.sample(50))

# -------------------------
# PLOTS
# -------------------------
shap.summary_plot(shap_values, X.sample(50))
shap.summary_plot(shap_values, X.sample(50), plot_type="bar")

print("SHAP analysis completed successfully!")