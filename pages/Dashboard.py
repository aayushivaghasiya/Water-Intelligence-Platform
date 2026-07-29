import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Water Dashboard",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Water Intelligence Dashboard")


st.write(
    "AI based water monitoring and analysis dashboard."
)



# Dashboard Cards

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "💧 Water Status",
        "Normal"
    )


with col2:
    st.metric(
        "🚨 Risk Level",
        "Low"
    )


with col3:
    st.metric(
        "🌊 Groundwater",
        "25 m"
    )


with col4:
    st.metric(
        "🔧 Leakage",
        "No"
    )



st.divider()



# Load Dataset

try:

    df = pd.read_csv(
        "dataset/water_dataset.csv"
    )

    st.success(
        "Dataset Loaded Successfully ✅"
    )


except Exception as e:

    st.error(
        f"Dataset loading failed: {e}"
    )
    st.stop()



# Data Preview

st.subheader("📋 Water Data Preview")

st.dataframe(
    df.head(10)
)



# Charts

st.subheader("📈 Rainfall Analysis")


st.line_chart(
    df["Rainfall"]
)



st.subheader("🌊 Groundwater Level Trend")


st.line_chart(
    df["Groundwater_Level"]
)