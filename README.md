# 🚗 ML-Based Smart Vehicle Dashboard for Real-Time Monitoring and Predictive Alerts

A Machine Learning-based Smart Vehicle Dashboard that combines **Embedded Systems, IoT, and Artificial Intelligence** to monitor vehicle parameters in real time, classify driving behavior, and generate predictive maintenance alerts.

---

## 📖 Project Overview

Modern vehicles generate large amounts of operational data that can be used to improve driver safety and vehicle maintenance. This project transforms a conventional vehicle dashboard into an intelligent monitoring system capable of analyzing vehicle conditions and predicting driving behavior.

The system monitors key vehicle parameters including:

- 🚗 Speed
- 🌡️ Temperature
- 🔋 Battery Level
- ⛽ Fuel Level
- 🛑 Braking Status
- 📳 Vibration Level

A **Random Forest Machine Learning model** analyzes these parameters and classifies driving behavior into:

- ✅ Safe
- ⚠️ Normal
- 🚨 Aggressive

The dashboard also provides predictive maintenance recommendations based on vehicle operating conditions.

---

## ✨ Features

- Real-time vehicle parameter monitoring
- Machine Learning-based driving behavior classification
- Vehicle health assessment
- Predictive maintenance alerts
- IoT dashboard integration using Blynk
- Low-cost embedded system implementation using ESP32
- Scalable architecture for future intelligent transportation systems

---

## 🛠️ Technologies Used

### Programming
- Python

### Machine Learning
- Scikit-learn
- Random Forest Classifier

### Data Processing
- Pandas
- NumPy

### Embedded Systems
- ESP32

### IoT Platform
- Blynk IoT

---

## 📂 Repository Structure

```
ML-Smart-Vehicle-Dashboard/
│
├── train_model.py
├── driver_ai.py
├── driver_ai_live.py
├── driver_data.csv
├── driver_model.pkl
├── label_encoder.pkl
└── README.md
```

---

## 🤖 Machine Learning Workflow

1. Collect vehicle parameter data
2. Preprocess the dataset
3. Train a Random Forest classifier
4. Save the trained model
5. Load the trained model
6. Predict driving behavior using real-time vehicle parameters
7. Generate vehicle health assessment and maintenance recommendations

---

## 📊 Machine Learning Model

**Algorithm:** Random Forest Classifier

### Input Features

- Speed
- Temperature
- Battery Level
- Fuel Level
- Brake Status
- Vibration Level

### Output Classes

- Safe
- Normal
- Aggressive

---

## 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/saiaakankssha/ML-Smart-Vehicle-Dashboard.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Train the model

```bash
python train_model.py
```

### Run prediction

```bash
python driver_ai.py
```

or

```bash
python driver_ai_live.py
```

---

## 📸 Results

The dashboard successfully demonstrates the following outputs.

### 🟢 Safe Driving Dashboard

![Safe Dashboard](https://github.com/Gurukiranbh/ML-Smart-Vehicle-Dashboard/blob/main/outputs/safe_dashboard.png.jpeg)

---

### 🔴 Aggressive Driving Dashboard

![Aggressive Dashboard](outputs/aggressive_dashboard.jpeg)

---

### ⚠️ Reckless Driving Dashboard

![Reckless Dashboard](outputs/reckless_dashboard.jpeg)

---

### 🤖 Machine Learning Prediction

![ML Output](outputs/ml_output.jpeg)
## 🔮 Future Scope

- GPS-based vehicle tracking
- Camera-based driver monitoring
- Cloud database integration
- Mobile application support
- Advanced Deep Learning models
- Fleet management support
- Electric vehicle monitoring

---

## 📚 Project Information

**Project Title**

**ML-Based Smart Vehicle Dashboard for Real-Time Monitoring and Predictive Alerts**

**Domain**

- Machine Learning
- Embedded Systems
- Internet of Things (IoT)
- Intelligent Transportation Systems

---

## 👩‍💻 Author

**Gurukiran BH**

B.E. Electronics and Communication Engineering  
R V College of Engineering, Bengaluru
