import streamlit as st
from streamlit_option_menu import option_menu


def show_prediction():

    st.title("🔮 Customer Churn Prediction")
    st.markdown("Predict whether a customer is likely to churn using our AI model.")

    # ---------------- Tabs ---------------- #
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "📝 Customer Details",
        "🤖 Predict",
        "📊 Results",
        "🧠 Explainability",
        "💡 Recommendations",
        "📜 History",
        "📄 Report"
    ])

    # ==========================================================
    # TAB 1 - CUSTOMER DETAILS
    # ==========================================================
    with tab1:

        st.header("📝 Customer Details")

        col1, col2 = st.columns(2)

        with col1:
            gender = st.selectbox("Gender", ["Male", "Female"])
            senior = st.selectbox("Senior Citizen", ["No", "Yes"])

        with col2:
            partner = st.selectbox("Partner", ["No", "Yes"])
            dependents = st.selectbox("Dependents", ["No", "Yes"])

        st.divider()

        col3, col4 = st.columns(2)

        with col3:
            phone = st.selectbox("Phone Service", ["Yes", "No"])
            internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
            online_security = st.selectbox("Online Security", ["Yes", "No"])
            online_backup = st.selectbox("Online Backup", ["Yes", "No"])

        with col4:
            device = st.selectbox("Device Protection", ["Yes", "No"])
            tech = st.selectbox("Tech Support", ["Yes", "No"])
            tv = st.selectbox("Streaming TV", ["Yes", "No"])
            movies = st.selectbox("Streaming Movies", ["Yes", "No"])

        st.divider()

        col5, col6 = st.columns(2)

        with col5:
            contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
            paperless = st.selectbox("Paperless Billing", ["Yes", "No"])

        with col6:
            payment = st.selectbox(
                "Payment Method",
                ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
            )

        st.divider()

        col7, col8, col9 = st.columns(3)

        with col7:
            tenure = st.number_input("Tenure (Months)", 0, 100, 1)

        with col8:
            monthly = st.number_input("Monthly Charges", 0.0, 500.0, 70.0)

        with col9:
            total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)

        st.success("✅ Customer details completed.")

    # ==========================================================
    # TAB 2 - PREDICT
    # ==========================================================
    with tab2:
        st.header("🤖 Predict")

        if st.button("🚀 Run Prediction"):
            st.success("Prediction started...")

            result = "Churn"  # placeholder model output

            st.session_state["prediction"] = result

            st.info(f"Model Prediction: {result}")

    # ==========================================================
    # TAB 3 - RESULTS
    # ==========================================================
    with tab3:
        st.header("📊 Prediction Results")

        if "prediction" in st.session_state:
            if st.session_state["prediction"] == "Churn":
                st.error("⚠ Customer is likely to CHURN")
            else:
                st.success("✅ Customer will STAY")
        else:
            st.warning("Run prediction first in Predict tab")

    # ==========================================================
    # TAB 4 - EXPLAINABILITY
    # ==========================================================
    with tab4:
        st.header("🧠 SHAP Explainability")

        st.markdown("Feature impact on prediction:")

        st.progress(70, text="Monthly Charges impact")
        st.progress(40, text="Tenure impact")
        st.progress(85, text="Contract type impact")

        st.info("SHAP visualization will be integrated after model training")

    # ==========================================================
    # TAB 5 - RECOMMENDATIONS
    # ==========================================================
    with tab5:
        st.header("💡 Business Recommendations")

        st.markdown("""
        - Offer discounts for high-risk customers  
        - Promote long-term contracts  
        - Improve fiber optic service quality  
        - Target electronic check users  
        """)

    # ==========================================================
    # TAB 6 - HISTORY
    # ==========================================================
    with tab6:
        st.header("📜 Prediction History")

        if "history" not in st.session_state:
            st.session_state.history = []

        if "prediction" in st.session_state:
            st.session_state.history.append(st.session_state["prediction"])

        st.write(st.session_state.history)

    # ==========================================================
    # TAB 7 - REPORT
    # ==========================================================
    with tab7:
        st.header("📄 Download Report")

        st.download_button(
            label="⬇ Download Report (PDF)",
            data="Sample Report - Churn Prediction",
            file_name="churn_report.txt"
        )