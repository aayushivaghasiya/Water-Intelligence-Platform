
from pathlib import Path
import joblib
import pandas as pd

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "model"

# Load Models
rf_model = joblib.load(MODEL_DIR / "random_forest.pkl")
lr_model = joblib.load(MODEL_DIR / "linear_regression.pkl")

# Load Encoders
leakage_encoder = joblib.load(MODEL_DIR / "leakage_encoder.pkl")
risk_encoder = joblib.load(MODEL_DIR / "risk_encoder.pkl")

# Load Models
rf_model = joblib.load("model/random_forest.pkl")
lr_model = joblib.load("model/linear_regression.pkl")

# Load Encoders
leakage_encoder = joblib.load("model/leakage_encoder.pkl")
risk_encoder = joblib.load("model/risk_encoder.pkl")


def predict_water_shortage(input_data):

    data = input_data.copy()

    # Encode Leakage Status
    data["Leakage_Status"] = leakage_encoder.transform(
        [data["Leakage_Status"]]
    )[0]

    features = [
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

    X = pd.DataFrame([data])[features]

    prediction = rf_model.predict(X)

    return risk_encoder.inverse_transform(prediction)[0]


def predict_groundwater(input_data):

    X = [[
        input_data["Temperature"],
        input_data["Rainfall"],
        input_data["Humidity"],
        input_data["Water_Consumption"],
        input_data["Reservoir_Level"],
        input_data["Pressure"],
        input_data["Flow_Rate"]
    ]]

    prediction = lr_model.predict(X)

    return round(float(prediction[0]), 2)


def get_recommendation(risk, groundwater):

    recommendations = []

    if risk == "High":
        recommendations.extend([
            "⚠ High Water Shortage Risk",
            "💧 Reduce water consumption",
            "🌧 Start rainwater harvesting",
            "🏞 Monitor reservoir daily"
        ])

    elif risk == "Medium":
        recommendations.extend([
            "⚠ Moderate Water Shortage Risk",
            "🚰 Use water efficiently",
            "📊 Monitor groundwater regularly"
        ])

    else:
        recommendations.extend([
            "✅ Water resources are stable",
            "👍 Continue monitoring"
        ])

    if groundwater < 15:
        recommendations.append("⚠ Groundwater level is critically low")

    elif groundwater < 25:
        recommendations.append("🟡 Groundwater level needs attention")

    else:
        recommendations.append("🟢 Groundwater level is healthy")

    return recommendations