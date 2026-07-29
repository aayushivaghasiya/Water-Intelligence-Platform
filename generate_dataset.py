import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Create dataset folder if it doesn't exist
os.makedirs("dataset", exist_ok=True)

# Number of records
NUM_RECORDS = 1000

start_date = datetime(2023, 1, 1)

records = []

for i in range(NUM_RECORDS):

    date = start_date + timedelta(days=i)

    temperature = round(random.uniform(18, 45), 1)

    rainfall = round(random.uniform(0, 250), 1)

    humidity = random.randint(30, 95)

    water_consumption = random.randint(1500, 9000)

    reservoir_level = random.randint(20, 100)

    groundwater_level = round(random.uniform(5, 40), 1)

    pressure = round(random.uniform(20, 80), 1)

    flow_rate = round(random.uniform(30, 120), 1)

    leakage = "Yes" if pressure < 35 or flow_rate < 45 else "No"

    score = 0

    if rainfall < 30:
        score += 1

    if temperature > 36:
        score += 1

    if reservoir_level < 35:
        score += 1

    if groundwater_level > 30:
        score += 1

    if water_consumption > 7000:
        score += 1

    if score >= 4:
        risk = "High"

    elif score >= 2:
        risk = "Medium"

    else:
        risk = "Low"

    records.append([
        date.strftime("%Y-%m-%d"),
        temperature,
        rainfall,
        humidity,
        water_consumption,
        reservoir_level,
        groundwater_level,
        pressure,
        flow_rate,
        leakage,
        risk
    ])

columns = [
    "Date",
    "Temperature",
    "Rainfall",
    "Humidity",
    "Water_Consumption",
    "Reservoir_Level",
    "Groundwater_Level",
    "Pressure",
    "Flow_Rate",
    "Leakage_Status",
    "Water_Shortage_Risk"
]

df = pd.DataFrame(records, columns=columns)

df.to_csv("dataset/water_dataset.csv", index=False)

print("Dataset generated successfully!")
print(df.head())
print(f"\nTotal Records: {len(df)}")
