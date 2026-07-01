import streamlit as st

def show_about():
    st.title("ℹ About")

    st.write("""
    This Customer Churn Prediction System is an AI-powered web application
    developed using Machine Learning and Streamlit.

    It helps businesses identify customers who are likely to leave
    and provides useful business insights.
    """)

    st.subheader("Technologies Used")

    st.write("""
    - Python
    - Pandas
    - NumPy
    - Scikit-Learn
    - XGBoost
    - Streamlit
    - Plotly
    """)