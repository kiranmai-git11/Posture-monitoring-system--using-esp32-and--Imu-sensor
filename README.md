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
