import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Air Quality Monitoring Dashboard",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------
st.title("🌍 Low-Cost Air Quality Monitoring System")
st.markdown("Machine Learning Based Calibration & AQI Prediction Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("merged_data.csv")
    return df

merged_df = load_data()

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("Dashboard Controls")

num_rows = st.sidebar.slider(
    "Select number of rows to display",
    10,
    500,
    100
)

# -----------------------------
# DATA PREVIEW
# -----------------------------
st.subheader("📊 Dataset Preview")

st.dataframe(merged_df.tail(num_rows))

# -----------------------------
# LATEST SENSOR VALUES
# -----------------------------
st.subheader("📡 Latest Sensor Readings")

latest = merged_df.iloc[-1]

col1, col2, col3 = st.columns(3)

col1.metric("MQ7", round(latest['mq7'], 2))
col2.metric("MQ135", round(latest['mq135'], 2))
col3.metric("Dust", round(latest['dust'], 2))

col4, col5 = st.columns(2)

col4.metric("Temperature", round(latest['temperature_x'], 2))
col5.metric("Humidity", round(latest['humidity_x'], 2))

# -----------------------------
# AQI SECTION
# -----------------------------
st.subheader("🌫 AQI Status")

aqi_value = latest['aqi_calculated']

if aqi_value <= 50:
    status = "Good"
elif aqi_value <= 100:
    status = "Satisfactory"
elif aqi_value <= 200:
    status = "Moderate"
elif aqi_value <= 300:
    status = "Poor"
elif aqi_value <= 400:
    status = "Very Poor"
else:
    status = "Severe"

st.metric(
    label="Predicted AQI",
    value=round(aqi_value, 2),
    delta=status
)

# -----------------------------
# AQI TREND GRAPH
# -----------------------------
st.subheader("📈 AQI Trend Over Time")

fig1, ax1 = plt.subplots(figsize=(12,5))

ax1.plot(
    merged_df['aqi'].values,
    label='Actual AQI'
)

ax1.plot(
    merged_df['aqi_calculated'].values,
    label='Predicted AQI'
)

ax1.set_xlabel("Samples")
ax1.set_ylabel("AQI")
ax1.legend()

st.pyplot(fig1)

# -----------------------------
# ACTUAL VS PREDICTED GRAPH
# -----------------------------
st.subheader("🎯 Actual vs Predicted AQI")

fig2, ax2 = plt.subplots(figsize=(7,6))

ax2.scatter(
    merged_df['aqi'],
    merged_df['aqi_calculated']
)

# Ideal prediction line
ax2.plot(
    [merged_df['aqi'].min(), merged_df['aqi'].max()],
    [merged_df['aqi'].min(), merged_df['aqi'].max()],
)

ax2.set_xlabel("Actual AQI")
ax2.set_ylabel("Predicted AQI")
ax2.set_title("AQI Prediction Performance")

st.pyplot(fig2)

# -----------------------------
# MODEL PERFORMANCE TABLE
# -----------------------------
st.subheader("🤖 Model Performance Comparison")

results = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest",
        "Gradient Boosting"
    ],

    "R2 Score": [
        0.49,
        0.98,
        0.82
    ],

    "RMSE": [
        33.74,
        5.65,
        12.10
    ],

    "MAE": [
        27.53,
        1.85,
        8.40
    ]
})

st.table(results)

# -----------------------------
# FEATURE IMPORTANCE SECTION
# -----------------------------
st.subheader("🧠 Features Used for Prediction")

features = [
    'mq7',
    'mq135',
    'dust',
    'mq7_smooth',
    'mq135_smooth',
    'dust_smooth',
    'temperature_x',
    'humidity_x'
]

feature_df = pd.DataFrame({
    "Features": features
})

st.table(feature_df)

# -----------------------------
# PROJECT DESCRIPTION
# -----------------------------
st.subheader("📚 About the Project")

st.write("""
This project focuses on improving the reliability of low-cost air quality sensors
using machine learning techniques.

Sensor readings collected using MQ-series gas sensors and dust sensors were merged
with CPCB reference station data. Multiple regression models such as Linear Regression,
Random Forest, and Gradient Boosting were trained to predict pollutant concentrations
and estimate AQI values.

The dashboard provides visualization of sensor readings, AQI trends,
prediction performance, and model evaluation metrics.
""")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("Developed for Minor Project | Low-Cost Air Quality Monitoring System")