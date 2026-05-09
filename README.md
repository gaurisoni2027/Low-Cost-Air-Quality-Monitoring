# Low-Cost Air Quality Monitoring System using Machine Learning Calibration

## Overview

This project focuses on improving the accuracy of low-cost air quality sensors using Machine Learning-based calibration techniques. The system compares raw sensor readings with reliable CPCB (Central Pollution Control Board) reference data and trains regression models to predict more accurate PM2.5 values.

Low-cost sensors are affordable and easy to deploy but often produce noisy and inconsistent readings. Through data preprocessing, feature engineering, and machine learning regression models, this project aims to improve the reliability of these sensors and make them more suitable for practical environmental monitoring applications.

---

# Objectives

- Collect environmental data from low-cost air quality sensors
- Obtain reference PM2.5 values from CPCB stations
- Preprocess and synchronize sensor and reference datasets
- Train Machine Learning models for calibration
- Improve PM2.5 prediction accuracy
- Compare multiple regression algorithms
- Evaluate performance using regression metrics and cross-validation

---

# Problem Statement

Traditional air quality monitoring stations provide highly accurate data but are expensive to install and maintain. Low-cost sensors offer an affordable alternative but suffer from:

- sensor drift
- environmental interference
- noisy readings
- lower precision

This project aims to bridge the gap between affordability and reliability by using Machine Learning models to calibrate low-cost sensor readings against CPCB reference data.

---

# Dataset Information

## Sensor Dataset

The sensor dataset contains environmental readings collected from low-cost sensors, including:

- Dust Sensor
- MQ135 Air Quality Sensor
- MQ7 Carbon Monoxide Sensor
- Temperature Sensor
- Humidity Sensor

## Reference Dataset

Reference PM2.5 readings were collected from CPCB monitoring stations and used as ground truth values for calibration.

---

# Workflow

## 1. Data Collection

Sensor readings and CPCB reference values were collected and stored in CSV format.

---

## 2. Data Preprocessing

The preprocessing stage included:

- handling missing values
- timestamp conversion
- formatting and cleaning data
- selecting relevant features
- removing invalid entries

---

## 3. Data Synchronization

Sensor data and CPCB data were synchronized using nearest timestamp matching.

```python
merged_df = pd.merge_asof(
    sensor_df,
    cpcb_df,
    on='time',
    direction='nearest',
    tolerance=pd.Timedelta("1h")
)
```

This ensured that sensor readings were matched with the closest available CPCB reference values.

---

## 4. Feature Engineering

### Input Features

- Temperature
- Humidity
- MQ135 Sensor Values
- MQ7 Sensor Values
- Dust Sensor Readings

### Target Variable

- PM2.5

---

# Machine Learning Models Used

## 1. Linear Regression

Linear Regression was used as a baseline model to understand linear relationships between sensor readings and PM2.5 values.

### Advantages
- Simple and interpretable
- Fast training

### Limitations
- Cannot effectively model complex nonlinear relationships

---

## 2. Random Forest Regression

Random Forest Regression combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### Advantages
- Handles nonlinear relationships
- Reduces variance
- Provides better generalization

---

## 3. Gradient Boosting Regression

Gradient Boosting Regression sequentially improves predictions by minimizing previous errors.

### Advantages
- High predictive performance
- Handles complex patterns effectively

---

# Cross Validation

K-Fold Cross Validation was implemented to improve model reliability and evaluate consistency across multiple data splits.

### Purpose of Cross Validation

- reduce overfitting
- improve model generalization
- evaluate stability of predictions
- obtain more reliable performance metrics

---

# Evaluation Metrics

The following regression metrics were used:

## R² Score

Measures how well the predicted values fit the actual values.

:contentReference[oaicite:0]{index=0}

Higher R² values indicate better model performance.

---

## Mean Absolute Error (MAE)

Measures the average absolute difference between predicted and actual values.

:contentReference[oaicite:1]{index=1}

Lower MAE indicates better accuracy.

---

## Root Mean Squared Error (RMSE)

Measures the square root of average squared prediction errors.

:contentReference[oaicite:2]{index=2}

Lower RMSE values indicate better prediction quality.

---

# Results

- Machine Learning calibration significantly improved PM2.5 prediction accuracy.
- Random Forest Regression and Gradient Boosting Regression performed better than Linear Regression.
- Cross-validation results demonstrated improved model consistency and reduced overfitting.
- Calibrated sensor readings aligned more closely with CPCB reference values.
- The project showed that low-cost sensors can provide more reliable environmental monitoring when combined with Machine Learning techniques.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook
- Google Colab
- Visual Studio Code

---


# Applications

- Smart city monitoring
- Low-cost environmental monitoring
- Educational research projects
- Real-time pollution analysis
- Distributed air quality sensing systems

---

# Future Improvements

- Real-time IoT integration
- Live AQI dashboard
- Edge device deployment
- Web/mobile monitoring platform
- Additional pollutant prediction models
- Cloud-based monitoring system
- Deep Learning-based calibration

---

# Conclusion

This project demonstrates that Machine Learning techniques can significantly improve the reliability of low-cost air quality sensors by calibrating them against CPCB reference data.

The results indicate that ensemble regression models such as Random Forest and Gradient Boosting can effectively reduce prediction errors and improve alignment with standard monitoring systems.

This approach provides a cost-effective solution for scalable environmental monitoring and highlights the potential of combining IoT and Machine Learning for smart pollution sensing applications.

---

# Author

## Gauri Soni
```