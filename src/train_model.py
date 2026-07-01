import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


def train_models(df):

    # -------------------------
    # SPLIT DATA
    # -------------------------
    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -------------------------
    # SCALING
    # -------------------------
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # -------------------------
    # MODELS
    # -------------------------
    lr = LogisticRegression(max_iter=2000)
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    xgb = XGBClassifier(eval_metric='logloss')

    lr.fit(X_train, y_train)
    rf.fit(X_train, y_train)
    xgb.fit(X_train, y_train)

    # -------------------------
    # PREDICTIONS
    # -------------------------
    lr_pred = lr.predict(X_test)
    rf_pred = rf.predict(X_test)
    xgb_pred = xgb.predict(X_test)

    # -------------------------
    # ACCURACY
    # -------------------------
    print("Logistic Regression:", accuracy_score(y_test, lr_pred))
    print("Random Forest:", accuracy_score(y_test, rf_pred))
    print("XGBoost:", accuracy_score(y_test, xgb_pred))

    # -------------------------
    # SAVE BEST MODEL (XGBOOST)
    # -------------------------
    os.makedirs("models", exist_ok=True)

    joblib.dump(xgb, "models/best_model.pkl")
    joblib.dump(scaler, "models/scaler.pkl")

    print("Model saved successfully!")

    return xgb