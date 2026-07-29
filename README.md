# 💧 Water Intelligence Platform

## 🤖 AI-Powered Water Resource Monitoring System

## 📌 Project Overview

Water Intelligence Platform is an AI-powered water management solution designed to improve water resource monitoring using Machine Learning and data analytics.

The system analyzes environmental and water-related parameters to predict water shortage risks, estimate groundwater levels, detect pipeline leakage conditions, and generate intelligent reports for better water management decisions.

The platform helps in:

- 💧 Predicting water shortage risks
- 🌊 Estimating groundwater levels
- 🔧 Detecting possible water leakage conditions
- 🌦 Providing weather-based insights
- 📄 Generating AI-powered water analysis reports


---
## 🌐 Live Demo

**🚀 Streamlit Application:**  
https://water-intelligence-platform-cstzcbpjjx8c2fdhraebrp.streamlit.app/

# 🚀 Features

## 💧 Water Shortage Prediction

- Predicts water shortage risk using Machine Learning algorithms.
- Classifies water conditions into:
  - Low Risk
  - Medium Risk
  - High Risk


## 🌊 Groundwater Level Prediction

- Uses Linear Regression to estimate groundwater levels.
- Helps in understanding future groundwater availability.


## 🔧 Leakage Detection

- Monitors pipeline-related parameters.
- Detects possible leakage conditions using AI-based analysis.


## 🌦 Live Weather Integration

- Fetches real-time weather information using Weather API.
- Provides environmental insights for better prediction.


## 📊 Data Visualization

Interactive dashboards for:

- Reservoir level monitoring
- Groundwater status analysis
- Weather parameter visualization
- Prediction insights


## 📄 AI Report Generation

- Generates downloadable PDF prediction reports.
- Provides summarized water analysis results.


---

# 🧠 Machine Learning Models

## 🌲 Random Forest Classifier

Used for:

- Water Shortage Risk Prediction

Input Features:

- Temperature
- Rainfall
- Humidity
- Water Consumption
- Reservoir Level
- Groundwater Level
- Pressure
- Flow Rate
- Leakage Status


## 📈 Linear Regression

Used for:

- Groundwater Level Prediction


---

# 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Plotly
- Joblib
- OpenWeather API


---

# 📸 Application Screenshots


## 🏠 Dashboard

![Dashboard](screenshots/Water%20Intelligence%20Dashboard.png)


## 💧 Water Prediction

![Prediction](screenshots/AI%20Water%20Intelligence%20Prediction.png)


## 🔧 Leakage Detection

![Leakage Detection](screenshots/AI%20Water%20Leakage%20Detection.png)


## 📊 Analytics

![Analytics](screenshots/Water%20Analytics.png)


## 🌦 Live Weather

![Weather](screenshots/Live%20Weather.png)


---

# 📂 Project Structure
Water-Intelligence-Platform
│
├── app.py
├── generate_dataset.py
├── requirements.txt
│
├── dataset/
│ └── water_dataset.csv
│
├── model/
│ ├── train_model.py
│ ├── random_forest.pkl
│ ├── linear_regression.pkl
│ ├── risk_encoder.pkl
│ └── leakage_encoder.pkl
│
├── pages/
│ ├── Dashboard.py
│ ├── Prediction.py
│ ├── Leakage.py
│ ├── Analytics.py
│ ├── History.py
│ └── About.py
│
├── utils/
│ ├── preprocessing.py
│ ├── prediction.py
│ ├── weather.py
│ ├── rainfall_model.py
│ ├── pdf_report.py
│ └── report.py
│
├── reports/
│ ├── Water_Report.pdf
│ └── prediction_history.csv
│
└── screenshots/
└── Application screenshots


---

# 👩‍💻 Team Members

Developed as a Hackathon Group Project by:

- Aayushi Vaghasiya
- yashvi gelani 
- panthi thummar
- dhara radadiya


---

# 🏆 Project Category

Artificial Intelligence | Machine Learning | Water Resource Management


---

# 📌 Future Enhancements

- IoT sensor integration for real-time water monitoring
- Advanced deep learning models for prediction improvement
- Mobile application support
- Automated smart water management recommendations