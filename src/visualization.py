import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# -------------------------
# LOAD DATA
# -------------------------
def load_data():
    df = pd.read_csv("data/processed/cleaned_data.csv")
    return df


# -------------------------
# CHURN DISTRIBUTION
# -------------------------
def plot_churn_distribution(df):
    plt.figure()
    sns.countplot(x="Churn", data=df)
    plt.title("Customer Churn Distribution")
    plt.xticks([0, 1], ["No Churn", "Churn"])
    plt.show()


# -------------------------
# TENURE VS CHURN
# -------------------------
def plot_tenure_vs_churn(df):
    plt.figure()
    sns.boxplot(x="Churn", y="tenure", data=df)
    plt.title("Tenure vs Churn")
    plt.xticks([0, 1], ["No Churn", "Churn"])
    plt.show()


# -------------------------
# MONTHLY CHARGES VS CHURN
# -------------------------
def plot_monthly_charges(df):
    plt.figure()
    sns.boxplot(x="Churn", y="MonthlyCharges", data=df)
    plt.title("Monthly Charges vs Churn")
    plt.xticks([0, 1], ["No Churn", "Churn"])
    plt.show()


# -------------------------
# CORRELATION HEATMAP
# -------------------------
def plot_correlation(df):
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), cmap="coolwarm", linewidths=0.5)
    plt.title("Feature Correlation Heatmap")
    plt.show()


# -------------------------
# RUN ALL PLOTS
# -------------------------
if __name__ == "__main__":
    df = load_data()

    print("Data loaded:", df.shape)

    plot_churn_distribution(df)
    plot_tenure_vs_churn(df)
    plot_monthly_charges(df)
    plot_correlation(df)