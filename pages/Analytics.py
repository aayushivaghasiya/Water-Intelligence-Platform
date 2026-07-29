import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Water Analytics")

try:
    df = pd.read_csv("dataset/water_dataset.csv")

    st.dataframe(df.head())

    st.subheader("Temperature Trend")

    fig = px.line(
        df,
        x="Date",
        y="Temperature",
        title="Temperature Over Time"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Reservoir Level")

    fig2 = px.line(
        df,
        x="Date",
        y="Reservoir_Level",
        title="Reservoir Level"
    )

    st.plotly_chart(fig2, use_container_width=True)

except Exception as e:
    st.error(f"Error loading dataset: {e}")