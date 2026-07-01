import streamlit as st

def show_home():

    # ---------------- HERO ----------------
    st.markdown("""
    <div class="hero">
        <h1>Customer Churn Prediction</h1>
        <h3>AI Powered Customer Retention Platform</h3>
        <p>
            Predict customer churn, analyze customer behaviour,
            and improve customer retention using Machine Learning.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    active_card = "overview"

    col1, col2, col3 = st.columns(3)

    # ===========================
    # Overview
    # ===========================
    with col1:

        if st.button("📊 Overview", use_container_width=True):
            active_card = "overview"

        st.markdown("""
        <div class="card">
            <h3>📊 Overview</h3>
            <p>Dashboard summary metrics and KPIs.</p>
        </div>
        """, unsafe_allow_html=True)

    # ===========================
    # Customers
    # ===========================
    with col2:

        if st.button("👥 Customers", use_container_width=True):
            active_card = "customers"

        st.markdown("""
        <div class="card">
            <h3>👥 Customers</h3>
            <p>Customer demographics and behaviour analysis.</p>
        </div>
        """, unsafe_allow_html=True)

    # ===========================
    # Churn
    # ===========================
    with col3:

        if st.button("📉 Churn", use_container_width=True):
            active_card = "churn"

        st.markdown("""
        <div class="card">
            <h3>📉 Churn Analysis</h3>
            <p>Churn trends, risk factors and retention insights.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.divider()

    # ---------------- CONTENT ----------------

    if active_card == "overview":

        st.subheader("📊 Dashboard Overview")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Customers", "7043")
        c2.metric("Churn Rate", "26.5%")
        c3.metric("Retention", "73.5%")
        c4.metric("Revenue", "$16.1M")

    elif active_card == "customers":

        st.subheader("👥 Customer Analytics")

        st.info("""
• Analyze customer demographics

• Monitor customer tenure

• Study customer services

• Understand customer behaviour
""")

    elif active_card == "churn":

        st.subheader("📉 Churn Insights")

        st.warning("""
High Risk Customers

• Month-to-Month Contract

• High Monthly Charges

• Fiber Optic Internet

• Electronic Check Payment

• Short Tenure Customers
""")

    st.success("✅ Welcome to the AI Powered Customer Churn Prediction Dashboard.")