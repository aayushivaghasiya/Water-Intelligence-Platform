from utils.prediction import (
    predict_water_shortage,
    predict_groundwater,
    get_recommendation
)

import streamlit as st
import plotly.graph_objects as go

from utils.report import save_prediction
from utils.pdf_report import generate_pdf
from utils.weather import get_weather


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Water Intelligence Platform",
    page_icon="💧",
    layout="wide"
)


# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

.hero{
    background:#eaf7ff;
    padding:25px;
    border-radius:15px;
    text-align:center;
}


.hero h2{
    color:#0077b6;
    font-size:30px;
}


.hero p{
    font-size:17px;
}


.card{
    background:white;
    padding:15px;
    border-radius:12px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
}


.card h2{
    color:#0077b6;
}

</style>

""", unsafe_allow_html=True)



# -----------------------------
# Header
# -----------------------------

st.markdown(
"""
<h1 style="text-align:center; color:#0077b6;">
💧 Water Intelligence Platform
</h1>

<p style="text-align:center; font-size:18px;">
AI powered system for water shortage prediction,
groundwater monitoring and smart water management.
</p>
""",
unsafe_allow_html=True
)





# -----------------------------
# Features
# -----------------------------

st.subheader("🚀 AI Features")


c1,c2,c3,c4 = st.columns(4)


with c1:
    st.info(
        "💧\n\nWater Shortage\nPrediction"
    )


with c2:
    st.info(
        "🌊\n\nGroundwater\nForecast"
    )


with c3:
    st.info(
        "🔧\n\nLeakage\nDetection"
    )


with c4:
    st.info(
        "🌦\n\nWeather\nAnalysis"
    )


# -----------------------------
# Live Weather
# -----------------------------

st.divider()

st.subheader("🌍 Live Weather")


city = st.text_input(
    "Enter City",
    value="Surat"
)


if st.button("🌦 Get Live Weather"):

    weather = get_weather(city)


    if weather:

        st.success(
            f"Weather Loaded: {weather['name']}"
        )


        w1, w2, w3 = st.columns(3)


        with w1:

            st.metric(
                "🌡 Temperature",
                f"{weather['main']['temp']} °C"
            )


        with w2:

            st.metric(
                "💧 Humidity",
                f"{weather['main']['humidity']} %"
            )


        with w3:

            st.metric(
                "Pressure",
                f"{weather['main']['pressure']} hPa"
            )


        st.info(
            f"Condition: {weather['weather'][0]['description'].title()} | "
            f"Wind: {weather['wind']['speed']} m/s"
        )


    else:

        st.error(
            "City not found. Check city name."
        )
# -----------------------------
# Input
# -----------------------------

st.subheader("📥 Enter Water Parameters")

a, b, c = st.columns(3)

with a:

    temperature = st.number_input(
        "🌡 Temperature",
        min_value=-50.0,
        value=30.0,
        step=1.0
    )

    rainfall = st.number_input(
        "🌧 Rainfall",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    humidity = st.number_input(
        "💧 Humidity",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=1.0
    )

with b:

    water_consumption = st.number_input(
        "🚰 Water Consumption",
        min_value=0.0,
        value=250.0,
        step=1.0
    )

    reservoir = st.number_input(
        "🏞 Reservoir Level",
        min_value=0.0,
        max_value=100.0,
        value=50.0,
        step=1.0
    )

    groundwater = st.number_input(
        "🌊 Groundwater Level",
        min_value=0.0,
        value=20.0,
        step=1.0
    )

with c:

    pressure = st.number_input(
        "📈 Pressure",
        min_value=0.0,
        value=70.0,
        step=1.0
    )

    flow_rate = st.number_input(
        "💦 Flow Rate",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

    leakage = st.selectbox(
        "🔧 Leakage Status",
        ["No", "Yes"]
    )
# -----------------------------
# Prediction
# -----------------------------

if st.button("🤖 Generate Prediction"):


    data = {

        "Temperature":temperature,
        "Rainfall":rainfall,
        "Humidity":humidity,
        "Water_Consumption":water_consumption,
        "Reservoir_Level":reservoir,
        "Groundwater_Level":groundwater,
        "Pressure":pressure,
        "Flow_Rate":flow_rate,
        "Leakage_Status":leakage

    }


    risk = predict_water_shortage(data)

    groundwater_prediction = predict_groundwater(data)


    recommendations = get_recommendation(
        risk,
        groundwater_prediction
    )


    save_prediction({

        "Temperature":temperature,
        "Risk":risk,
        "Groundwater":groundwater_prediction

    })


    st.divider()


    st.subheader("📊 Prediction Result")


    r1,r2,r3 = st.columns(3)


    with r1:
        st.metric(
            "Water Risk",
            risk
        )


    with r2:
        st.metric(
            "Groundwater",
            f"{groundwater_prediction} m"
        )


    with r3:
        st.metric(
            "Leakage",
            leakage
        )



    # -----------------------------
    # Charts
    # -----------------------------


    st.subheader("📊 Water Resource Overview")


    x,y = st.columns(2)


    with x:

        fig1 = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=reservoir,
                title={"text":"Reservoir Level"},
                gauge={
                    "axis":{"range":[0,100]}
                }
            )
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )



    with y:

        fig2 = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=groundwater_prediction,
                title={"text":"Groundwater Level"},
                gauge={
                    "axis":{"range":[0,50]}
                }
            )
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )



    st.subheader("📈 Weather Parameters")


    fig3 = go.Figure()


    fig3.add_scatter(
        x=[
            "Temperature",
            "Humidity",
            "Rainfall"
        ],

        y=[
            temperature,
            humidity,
            rainfall
        ],

        mode="lines+markers"
    )


    st.plotly_chart(
        fig3,
        use_container_width=True
    )



    # Recommendations

    st.subheader("🤖 AI Recommendations")


    for rec in recommendations:

        st.success(rec)



    # PDF

    pdf = generate_pdf(data)


    with open(pdf,"rb") as f:

        st.download_button(
            "📄 Download PDF Report",
            f,
            "Water_Report.pdf",
            "application/pdf"
        )