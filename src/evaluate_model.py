import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve
)
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("data/processed/final_data.csv")

X = df.drop("Churn", axis=1)
y = df["Churn"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Load scaler and model
scaler = joblib.load("models/scaler.pkl")
model = joblib.load("models/best_model.pkl")

# Scale data
X_test = scaler.transform(X_test)

# Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# -------------------------
# CONFUSION MATRIX
# -------------------------
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# -------------------------
# CLASSIFICATION REPORT
# -------------------------
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# -------------------------
# ROC-AUC SCORE
# -------------------------
roc_score = roc_auc_score(y_test, y_prob)
print("ROC-AUC Score:", roc_score)

# -------------------------
# ROC CURVE PLOT
# -------------------------
fpr, tpr, _ = roc_curve(y_test, y_prob)

plt.figure()
plt.plot(fpr, tpr, label=f"AUC = {roc_score:.2f}")
plt.plot([0, 1], [0, 1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()