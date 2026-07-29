import streamlit as st
import joblib


st.set_page_config(
    page_title="Leakage Detection",
    page_icon="🔧",
    layout="wide"
)


st.title("🔧 AI Water Leakage Detection")


st.write(
    "AI based water pipeline leakage detection system."
)


# Load Model

try:

    model = joblib.load(
        "model/random_forest.pkl"
    )

    st.success("AI Model Loaded Successfully ✅")


except Exception as e:

    st.error(f"Model loading failed: {e}")
    st.stop()



# Inputs

flow = st.number_input(
    "💦 Flow Rate",
    value=80.0
)


pressure = st.number_input(
    "📈 Pressure",
    value=50.0
)


consumption = st.number_input(
    "🚰 Water Consumption",
    value=5000.0
)



if st.button("🔍 Detect Leakage"):


    if flow < 50:

        st.error(
            "⚠️ Possible Leakage Detected"
        )

    else:

        st.success(
            "✅ No Leakage Detected"
        )