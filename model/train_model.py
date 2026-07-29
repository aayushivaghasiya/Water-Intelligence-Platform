import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("dataset/water_dataset.csv")

print("Dataset Loaded Successfully!")
print(df.head())

# -----------------------------
# Encode Categorical Columns
# -----------------------------
le_leakage = LabelEncoder()
df["Leakage_Status"] = le_leakage.fit_transform(df["Leakage_Status"])

le_risk = LabelEncoder()
df["Water_Shortage_Risk"] = le_risk.fit_transform(df["Water_Shortage_Risk"])

# Save encoders
joblib.dump(le_leakage, "model/leakage_encoder.pkl")
joblib.dump(le_risk, "model/risk_encoder.pkl")

# -----------------------------
# Feature Selection
# -----------------------------
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

X = df[features]

# -----------------------------
# Random Forest (Classification)
# -----------------------------
y_class = df["Water_Shortage_Risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_class,
    test_size=0.2,
    random_state=42
)

rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

rf.fit(X_train, y_train)

prediction = rf.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("\nRandom Forest Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report\n")
print(classification_report(y_test, prediction))

# Save Model
joblib.dump(rf, "model/random_forest.pkl")

# -----------------------------
# Linear Regression
# Predict Groundwater Level
# -----------------------------

reg_features = [
    "Temperature",
    "Rainfall",
    "Humidity",
    "Water_Consumption",
    "Reservoir_Level",
    "Pressure",
    "Flow_Rate"
]

X_reg = df[reg_features]

y_reg = df["Groundwater_Level"]

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg,
    y_reg,
    test_size=0.2,
    random_state=42
)

lr = LinearRegression()

lr.fit(X_train_reg, y_train_reg)

pred = lr.predict(X_test_reg)

mse = mean_squared_error(y_test_reg, pred)

r2 = r2_score(y_test_reg, pred)

print("\nLinear Regression Results")

print("MSE :", round(mse,2))

print("R2 Score :", round(r2,2))

joblib.dump(lr, "model/linear_regression.pkl")

print("\n===================================")
print("Models Saved Successfully")
print("===================================")