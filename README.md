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

---

# 📁 Project Structure

```
posture-monitoring-system-esp32/
│
├── Arduino_Code/
│   ├── posture_monitor.ino
│   └── posture_model.h
│
├── ML_Model/
│   ├── posture_training.ipynb
│   └── posture.csv
│
├── Images/
│
├── PPT/
│   └── posture_presentation.pptx
│
└── README.md
```

---

# 🚀 Getting Started

## Prerequisites

Before running this project, install:

- Arduino IDE
- ESP32 Board Package
- Python 3.x
- Google Colab (for model training)

### Required Arduino Libraries

- Wire
- MPU6050
- EloquentTinyML
- micromlgen (used in Google Colab)

---

# 🔌 Hardware Connections

| MPU6050 | ESP32 |
|----------|-------|
| VCC | 3.3V |
| GND | GND |
| SDA | GPIO21 |
| SCL | GPIO22 |

| Buzzer | ESP32 |
|----------|-------|
| Positive (+) | GPIO25 |
| Negative (-) | GND |

---

# ▶️ How to Run

### Step 1

Train the Decision Tree model using the provided Google Colab notebook.

### Step 2

Generate the `posture_model.h` file using **micromlgen**.

### Step 3

Open the Arduino project in Arduino IDE.

### Step 4

Upload the code to the ESP32.

### Step 5

Open the Serial Monitor at **115200 baud rate**.

### Step 6

Wear or position the IMU sensor correctly and monitor posture in real time.

When an incorrect posture is detected, the buzzer will immediately alert the user.

---

# 📊 Results

The developed system successfully detects different body postures in real time using gyroscope data from the MPU6050 sensor. The trained Decision Tree model accurately classifies the user's posture into one of the predefined categories.

### Detected Postures

| Posture | Alert |
|----------|-------|
| ✅ Normal | No |
| ⬆️ Bending Forward | Yes |
| ⬇️ Bending Backward | Yes |
| ⬅️ Bending Left | Yes |
| ➡️ Bending Right | Yes |
| ↺ Twisting Left | Yes |
| ↻ Twisting Right | Yes |

When an incorrect posture is detected, the ESP32 activates the buzzer to provide immediate feedback to the user.

---

# 🎯 Applications

- Smart wearable health devices
- Student posture monitoring
- Office workstation ergonomics
- Healthcare and physiotherapy
- Fitness and yoga training
- Elderly posture assistance

---

# 🔮 Future Enhancements

- Mobile application for live posture monitoring
- Bluetooth/Wi-Fi notifications
- Cloud-based posture analytics
- OLED display integration
- Rechargeable wearable design
- Improved Machine Learning models with larger datasets
- Long-term posture history tracking

---

# 👩‍💻 Project Team

**Mini Project**

- K. Kiranmai
- K. Shravyanjali
- P. Varshini
- N. Akshitha

Department of Electronics and Communication Engineering

---

# 🙏 Acknowledgements

We sincerely thank our project guide and the Department of Electronics and Communication Engineering for their continuous support and valuable guidance throughout this mini project.

---

# 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving this repository a star!

---

# 📷 Project Gallery

## Circuit Diagram

![Circuit Diagram](Images/circuit.jpeg)

The circuit consists of an ESP32 microcontroller connected to an MPU6050 IMU sensor via I²C communication and a buzzer for real-time posture alerts.

---

## Serial Monitor Output

![Serial Monitor](Images/serial_monitor.jpeg)

The Serial Monitor displays the gyroscope readings (GX, GY, GZ) along with the predicted posture class in real time.

---

# 🎥 Project Demonstration

A short demonstration of the working posture monitoring system is available below.

➡️ [Watch Demo Video](Images/demo.mp4)

