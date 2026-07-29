import pandas as pd
import joblib

# Load encoder
leakage_encoder = joblib.load("model/leakage_encoder.pkl")


def preprocess_input(data):

    data = data.copy()

    # Convert Yes/No into encoded value
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

    df = pd.DataFrame([data])

    return df[features]