# 💧 Water Intelligence Platform

## 🤖 AI-Powered Water Resource Monitoring System

Water Intelligence Platform is an AI-powered solution that leverages Machine Learning and data analytics to improve water resource monitoring and management. The platform predicts water shortage risks, estimates groundwater levels, detects pipeline leakage, provides weather insights, and generates AI-powered reports for better decision-making.

---

## 🌐 Live Demo

🚀 **Streamlit Application**  
https://water-intelligence-platform-cstzcbpjjx8c2fdhraebrp.streamlit.app/

---

# 📌 Project Overview

The Water Intelligence Platform helps monitor and analyze water resources using Artificial Intelligence and Machine Learning.

### The platform provides:

- 💧 Water Shortage Risk Prediction
- 🌊 Groundwater Level Prediction
- 🔧 Water Leakage Detection
- 🌦 Live Weather Information
- 📊 Interactive Analytics Dashboard
- 📄 AI-generated PDF Reports
- 📜 Prediction History Tracking

---

# 🚀 Features

## 💧 Water Shortage Prediction

- Predicts future water shortage risk using Machine Learning.
- Classifies water conditions into:
  - Low Risk
  - Medium Risk
  - High Risk

## 🌊 Groundwater Level Prediction

- Estimates groundwater level using Linear Regression.
- Supports water resource planning.

## 🔧 Leakage Detection

- Detects possible pipeline leakage based on pressure and flow rate.
- Helps reduce water loss.

## 🌦 Live Weather Integration

- Fetches real-time weather information using the OpenWeather API.
- Displays environmental conditions affecting water availability.

## 📊 Interactive Dashboard

Visualizes:

- Reservoir Level
- Groundwater Level
- Weather Information
- Prediction Results
- Historical Records

## 📄 AI Report Generation

- Generates downloadable PDF reports.
- Saves prediction history automatically.

---

# 🧠 Machine Learning Models

## 🌲 Random Forest Classifier

Used for:

- Water Shortage Risk Prediction

### Input Features

- Temperature
- Rainfall
- Humidity
- Water Consumption
- Reservoir Level
- Groundwater Level
- Pressure
- Flow Rate
- Leakage Status

---

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

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/aayushivaghasiya/Water-Intelligence-Platform.git
```

Move to the project folder:

```bash
cd Water-Intelligence-Platform
```

Install required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 📖 How to Use

1. Open the application.
2. Navigate to the Prediction page.
3. Enter the required environmental and water parameters.
4. Click **Generate Prediction**.
5. View:
   - Water Shortage Risk
   - Groundwater Prediction
   - AI Recommendations
6. Download the generated PDF report.

---

# 📊 Dataset

The project uses a custom dataset containing water resource and environmental parameters.

Dataset includes:

- Temperature
- Rainfall
- Humidity
- Water Consumption
- Reservoir Level
- Groundwater Level
- Pressure
- Flow Rate
- Leakage Status

The dataset is used to train Machine Learning models for water prediction and analysis.

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

```text
Water-Intelligence-Platform
│
├── app.py
├── generate_dataset.py
├── requirements.txt
│
├── dataset/
│   └── water_dataset.csv
│
├── model/
│   ├── train_model.py
│   ├── random_forest.pkl
│   ├── linear_regression.pkl
│   ├── risk_encoder.pkl
│   └── leakage_encoder.pkl
│
├── pages/
│   ├── Dashboard.py
│   ├── Prediction.py
│   ├── Leakage.py
│   ├── Analytics.py
│   ├── History.py
│   └── About.py
│
├── utils/
│   ├── preprocessing.py
│   ├── prediction.py
│   ├── weather.py
│   ├── rainfall_model.py
│   ├── pdf_report.py
│   └── report.py
│
├── reports/
│   ├── Water_Report.pdf
│   └── prediction_history.csv
│
└── screenshots/
    └── Project Screenshots
```

---

# 👩‍💻 Team Members

Developed as a Hackathon Group Project by:

- Aayushi Vaghasiya
- Yashvi Gelani
- Panthi Thummar
- Dhara Radadiya

---

# 🏆 Project Category

**Artificial Intelligence | Machine Learning | Water Resource Management**

---

# 🎯 Future Enhancements

- IoT sensor integration for real-time water monitoring
- Deep Learning-based prediction models
- Mobile application support
- Smart notification system
- Cloud database integration
- Real-time sensor data analysis
- Automated water conservation recommendations

---

# 📜 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub.