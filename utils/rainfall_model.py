import joblib
import numpy as np


def predict_rainfall(temp, humidity, pressure, wind):

    model = joblib.load(
        "models/rainfall_model.pkl"
    )

    data = np.array(
        [[temp, humidity, pressure, wind]]
    )

    prediction = model.predict(data)

    return prediction[0]