from src.preprocessing import load_raw_data, clean_data, save_cleaned_data
from src.feature_engineering import create_features
from src.train_model import train_models
from src.test_model import test_model
from src.visualization import load_data, plot_churn_distribution, plot_tenure_vs_churn, plot_monthly_charges, plot_correlation


def run_pipeline():
    print("\n🚀 Starting Customer Churn ML Pipeline\n")

    # -------------------------
    # STEP 1: DATA LOADING
    # -------------------------
    print("📥 Loading raw data...")
    df = load_raw_data()

    # -------------------------
    # STEP 2: DATA CLEANING
    # -------------------------
    print("🧹 Cleaning data...")
    df_clean = clean_data(df)

    # -------------------------
    # STEP 3: SAVE CLEANED DATA
    # -------------------------
    print("💾 Saving cleaned data...")
    save_cleaned_data(df_clean)

    # -------------------------
    # STEP 4: FEATURE ENGINEERING
    # -------------------------
    print("⚙ Feature engineering...")
    df_features = create_features(df_clean)

    # -------------------------
    # STEP 5: MODEL TRAINING
    # -------------------------
    print("🤖 Training models...")
    train_models(df_features)

    # -------------------------
    # STEP 6: MODEL TESTING
    # -------------------------
    print("🧪 Testing model...")
    test_model()

    # -------------------------
    # STEP 7: VISUALIZATION
    # -------------------------
    print("📊 Generating visualizations...")
    df_viz = load_data()

    plot_churn_distribution(df_viz)
    plot_tenure_vs_churn(df_viz)
    plot_monthly_charges(df_viz)
    plot_correlation(df_viz)

    print("\n✅ Pipeline Completed Successfully!")


# -------------------------
# RUN MAIN
# -------------------------
if __name__ == "__main__":
    run_pipeline()