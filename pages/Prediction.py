import streamlit as st
import joblib
import pandas as pd


st.set_page_config(
    page_title="AI Water Prediction",
    page_icon="💧",
    layout="wide"
)


st.title("💧 AI Water Intelligence Prediction")

st.write(
    "Enter environmental and water parameters to generate AI predictions."
)


# Load Models

try:

    water_model = joblib.load(
        "model/random_forest.pkl"
    )

    groundwater_model = joblib.load(
        "model/linear_regression.pkl"
    )

    leakage_encoder = joblib.load(
        "model/leakage_encoder.pkl"
    )

    risk_encoder = joblib.load(
        "model/risk_encoder.pkl"
    )


    st.success("AI Models Loaded Successfully ✅")


except Exception as e:

    st.error(f"Model loading failed: {e}")
    st.stop()



# User Inputs

col1, col2, col3 = st.columns(3)


with col1:

    temperature = st.number_input(
        "🌡 Temperature",
        value=30.0
    )

    rainfall = st.number_input(
        "🌧 Rainfall",
        value=100.0
    )

    humidity = st.number_input(
        "💧 Humidity",
        value=60.0
    )


with col2:

    consumption = st.number_input(
        "🚰 Water Consumption",
        value=5000.0
    )

    reservoir = st.number_input(
        "🏞 Reservoir Level",
        value=50.0
    )

    groundwater = st.number_input(
        "🌊 Current Groundwater Level",
        value=25.0
    )


with col3:

    pressure = st.number_input(
        "📈 Pressure",
        value=50.0
    )

    flow = st.number_input(
        "💦 Flow Rate",
        value=80.0
    )


    leakage = st.selectbox(
        "🔧 Leakage Status",
        ["No", "Yes"]
    )



# Prediction Button

if st.button("🚀 Generate AI Prediction"):


    # Encode Leakage

    leakage_encoded = leakage_encoder.transform(
        [leakage]
    )[0]


    # -------------------------
    # Water Shortage Prediction
    # -------------------------

    water_input = pd.DataFrame(
        [[
            temperature,
            rainfall,
            humidity,
            consumption,
            reservoir,
            groundwater,
            pressure,
            flow,
            leakage_encoded
        ]],
        columns=[
            "Temperature",
            "Rainfall",
            "Humidity",
            "Water_Consumption",
            "Reservoir_Level",
            "Groundwater_Level",
            "Pressure",
            "Flow_Rate",
            "Leakage_Status"
        ]
    )


    risk_prediction = water_model.predict(
        water_input
    )


    risk = risk_encoder.inverse_transform(
        risk_prediction
    )[0]


    st.subheader("🚨 Water Shortage Risk")


    if risk == "High":

        st.error(
            "High Water Shortage Risk 🚨"
        )

    elif risk == "Medium":

        st.warning(
            "Medium Water Shortage Risk ⚠️"
        )

    else:

        st.success(
            "Low Water Shortage Risk ✅"
        )



    # -------------------------
    # Groundwater Prediction
    # -------------------------

    groundwater_input = pd.DataFrame(
        [[
            temperature,
            rainfall,
            humidity,
            consumption,
            reservoir,
            pressure,
            flow
        ]],
        columns=[
            "Temperature",
            "Rainfall",
            "Humidity",
            "Water_Consumption",
            "Reservoir_Level",
            "Pressure",
            "Flow_Rate"
        ]
    )


    groundwater_result = groundwater_model.predict(
        groundwater_input
    )


    st.subheader("🌊 Groundwater Level Prediction")


    st.info(
        f"Estimated Groundwater Level: {groundwater_result[0]:.2f}"
    )


    # -------------------------
    # AI Recommendation
    # -------------------------

    st.subheader("🤖 AI Recommendation")


    if risk == "High":

        st.write(
            "Reduce water consumption and monitor groundwater level regularly."
        )

    elif risk == "Medium":

        st.write(
            "Maintain water usage and check reservoir conditions."
        )

    else:

        st.write(
            "Water condition is normal. Continue regular monitoring."
        )