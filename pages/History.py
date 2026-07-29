import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Prediction History")

file = "reports/prediction_history.csv"

if os.path.exists(file):

    df = pd.read_csv(file)

    st.success(f"Total Records : {len(df)}")

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download History CSV",
        csv,
        "prediction_history.csv",
        "text/csv"
    )

else:

    st.warning("No prediction history found.")