import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

# -----------------------------
# CACHE DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/cleaned_data.csv")


def show_visualization():

    df = load_data()

    st.title("📊 Data Visualization Center")
    st.markdown("Interactive dashboard for Customer Churn Prediction.")

    # ============================================================
    # MAIN SIDEBAR
    # ============================================================
    main_section = st.sidebar.selectbox(
        "📂 Choose Category",
        [
            "📊 Dashboard Overview",
            "📈 Customer Analytics",
            "📉 Churn Analysis",
            "💰 Revenue Analysis",
            "🌐 Service Analysis",
            "📊 Advanced Analytics",
            "📋 Dataset Explorer",
            "💡 Business Insights"
        ]
    )

    sub_section = None

    # ============================================================
    # SUB MENUS
    # ============================================================
    if main_section == "📊 Dashboard Overview":
        sub_section = st.sidebar.radio("📁 Options", ["Summary Metrics", "Charts"])

    elif main_section == "📈 Customer Analytics":
        sub_section = st.sidebar.radio("📁 Options", ["Demographics", "Tenure Analysis"])

    elif main_section == "📉 Churn Analysis":
        sub_section = st.sidebar.radio("📁 Options", ["Service Impact", "Payment Impact"])

    elif main_section == "💰 Revenue Analysis":
        sub_section = st.sidebar.radio("📁 Options", ["Monthly Charges", "Total Charges"])

    elif main_section == "🌐 Service Analysis":
        sub_section = st.sidebar.selectbox(
            "📁 Choose Service",
            ["PhoneService","OnlineSecurity","OnlineBackup",
             "DeviceProtection","TechSupport","StreamingTV","StreamingMovies"]
        )

    elif main_section == "📊 Advanced Analytics":
        sub_section = st.sidebar.radio("📁 Options", ["Correlation Heatmap", "Feature Explorer"])

    # ============================================================
    # DASHBOARD OVERVIEW
    # ============================================================
    if main_section == "📊 Dashboard Overview":

        if sub_section == "Summary Metrics":
            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Total Customers", len(df))
            c2.metric("Churn Customers", len(df[df["Churn"] == "Yes"]))
            c3.metric("Active Customers", len(df[df["Churn"] == "No"]))

            churn_rate = round((len(df[df["Churn"] == "Yes"]) / len(df)) * 100, 2)
            c4.metric("Churn Rate", f"{churn_rate} %")

        elif sub_section == "Charts":
            col1, col2 = st.columns(2)

            with col1:
                st.plotly_chart(px.pie(df, names="Churn"), use_container_width=True)

            with col2:
                st.plotly_chart(px.histogram(df, x="Contract", color="Churn"),
                                 use_container_width=True)

    # ============================================================
    # CUSTOMER ANALYTICS
    # ============================================================
    elif main_section == "📈 Customer Analytics":

        if sub_section == "Demographics":
            col1, col2 = st.columns(2)

            with col1:
                st.plotly_chart(px.histogram(df, x="gender", color="Churn"))

            with col2:
                st.plotly_chart(px.histogram(df, x="SeniorCitizen", color="Churn"))

        elif sub_section == "Tenure Analysis":
            st.plotly_chart(px.box(df, x="Churn", y="tenure", color="Churn"))

    # ============================================================
    # CHURN ANALYSIS
    # ============================================================
    elif main_section == "📉 Churn Analysis":

        if sub_section == "Service Impact":
            st.plotly_chart(px.histogram(df, x="InternetService", color="Churn"))

        elif sub_section == "Payment Impact":
            st.plotly_chart(px.histogram(df, x="PaymentMethod", color="Churn"))

    # ============================================================
    # REVENUE ANALYSIS
    # ============================================================
    elif main_section == "💰 Revenue Analysis":

        if sub_section == "Monthly Charges":
            st.plotly_chart(px.box(df, x="Churn", y="MonthlyCharges"))

        elif sub_section == "Total Charges":
            st.plotly_chart(px.box(df, x="Churn", y="TotalCharges"))

    # ============================================================
    # SERVICE ANALYSIS
    # ============================================================
    elif main_section == "🌐 Service Analysis":

        st.plotly_chart(px.histogram(df, x=sub_section, color="Churn"))

    # ============================================================
    # ADVANCED ANALYTICS
    # ============================================================
    elif main_section == "📊 Advanced Analytics":

        if sub_section == "Correlation Heatmap":
            numeric = df.select_dtypes(include="number")
            corr = numeric.corr()

            fig = ff.create_annotated_heatmap(
                z=corr.values,
                x=list(corr.columns),
                y=list(corr.index),
                annotation_text=corr.round(2).values,
                colorscale="Viridis"
            )

            st.plotly_chart(fig)

        elif sub_section == "Feature Explorer":
            feature = st.selectbox("Select Feature", df.columns)

            if df[feature].dtype == "object":
                st.plotly_chart(px.histogram(df, x=feature, color="Churn"))
            else:
                st.plotly_chart(px.histogram(df, x=feature))

    # ============================================================
    # DATASET EXPLORER
    # ============================================================
    elif main_section == "📋 Dataset Explorer":

        st.dataframe(df)
        st.write("Rows :", df.shape[0])
        st.write("Columns :", df.shape[1])
        st.write(df.isnull().sum())

    # ============================================================
    # BUSINESS INSIGHTS
    # ============================================================
    elif main_section == "💡 Business Insights":

        st.success("""
✔ Month-to-month contracts have highest churn  
✔ High monthly charges increase churn  
✔ Long tenure customers stay longer  
✔ Fiber optic users churn more  
✔ Electronic check users churn more  
""")