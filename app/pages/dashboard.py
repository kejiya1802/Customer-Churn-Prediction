import streamlit as st
import pandas as pd

def show_dashboard():

    st.title("📊 Dashboard")

    df = pd.read_csv("data/processed/cleaned_data.csv")

    st.subheader("Dataset Overview")

    st.dataframe(df.head())

    st.write("Rows :", df.shape[0])

    st.write("Columns :", df.shape[1])