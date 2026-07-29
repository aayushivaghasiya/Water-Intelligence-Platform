import pandas as pd
import os


def save_prediction(data):

    file = "reports/prediction_history.csv"

    df = pd.DataFrame([data])

    if os.path.exists(file):
        df.to_csv(file, mode="a", header=False, index=False)
    else:
        df.to_csv(file, index=False)