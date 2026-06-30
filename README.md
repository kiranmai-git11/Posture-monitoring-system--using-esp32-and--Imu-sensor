# 🧍 Smart Posture Monitoring System using ESP32 & MPU6050

A real-time posture monitoring system that uses an **ESP32**, **MPU6050 IMU sensor**, and a **Machine Learning Decision Tree model** to detect incorrect body posture and provide instant feedback through a buzzer.

---

## 📖 Overview

Poor sitting posture can lead to long-term health issues such as back pain, neck strain, and reduced productivity. This project presents a low-cost, portable, and real-time posture monitoring system that continuously analyzes body movements using an MPU6050 IMU sensor.

The collected gyroscope data is processed by an ESP32 microcontroller using a trained Machine Learning Decision Tree model. When incorrect posture is detected, the system immediately activates a buzzer to alert the user, encouraging healthy posture habits.

---

## ✨ Features

- Real-time posture monitoring
- Machine Learning-based posture classification
- ESP32 microcontroller implementation
- MPU6050 IMU sensor integration
- Instant buzzer alert for incorrect posture
- Lightweight and low-cost solution
- Portable and suitable for everyday use

---

## 🛠️ Hardware Components

| Component | Purpose |
|-----------|---------|
| ESP32 | Main microcontroller |
| MPU6050 IMU Sensor | Measures body movement and orientation |
| Buzzer | Provides posture alert |
| Jumper Wires | Hardware connections |
| USB Cable | Programming ESP32 |

---

## 💻 Software & Tools

- Arduino IDE
- Google Colab
- Python
- Scikit-learn
- micromlgen


---

## ⚙️ Working Principle

The system continuously monitors the user's posture using an MPU6050 IMU sensor. The gyroscope values are transmitted to the ESP32 through I²C communication. A Decision Tree Machine Learning model, trained using Scikit-learn and exported with micromlgen, runs directly on the ESP32 to classify the posture.

If the detected posture is incorrect, the ESP32 immediately activates a buzzer to notify the user.

### System Workflow

```
User Movement
      │
      ▼
MPU6050 IMU Sensor
      │
      ▼
ESP32 Microcontroller
      │
      ▼
Decision Tree ML Model
      │
      ▼
Posture Classification
      │
      ├──────────────┐
      ▼              ▼
Normal         Incorrect
                     │
                     ▼
              Buzzer Alert
```

---

## 🧠 Machine Learning Workflow

The machine learning model was developed using Python in Google Colab.

### Steps

1. Collect posture data from the MPU6050 sensor.
2. Prepare and clean the dataset.
3. Train a Decision Tree Classifier using Scikit-learn.
4. Evaluate the trained model.
5. Export the trained model as `posture_model.h` using **micromlgen**.
6. Deploy the model on the ESP32 for real-time inference.

### Dataset Features

| Feature | Description |
|---------|-------------|
| GX | Gyroscope X-axis |
| GY | Gyroscope Y-axis |
| GZ | Gyroscope Z-axis |

### Output Classes

- ✅ Normal
- ⬅️ Bending Left
- ➡️ Bending Right
- ⬆️ Bending Forward
- ⬇️ Bending Backward
- ↺ Twisting Left
- ↻ Twisting Right
