
# 📡 Project 1: Real-Time Environmental Data Logger and Visualizer

> A project-based robotics learning project that measures ambient light using an LDR sensor, streams real-time analog data from an Arduino to Python, processes the incoming signal, and visualizes it live using Matplotlib.

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Arduino](https://img.shields.io/badge/Arduino-Uno-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Overview

Most beginner Arduino projects start with blinking an LED.

For my first robotics project, I wanted to build a complete sensing pipeline instead.

This project demonstrates how a physical sensor interacts with electronics, how a microcontroller converts analog signals into digital values, how those values are transmitted through serial communication, and finally how Python processes and visualizes the data in real time.

The objective was not simply to read an LDR sensor, but to understand every engineering layer involved in the process.

---

# 🎯 Project Goal

Build a complete real-time sensing system that:

- Measures ambient light using an LDR
- Converts resistance into voltage using a voltage divider
- Samples the voltage using Arduino's ADC
- Sends sensor readings to a computer over serial communication
- Reads data using Python (PySerial)
- Processes incoming data efficiently
- Displays a scrolling real-time graph using Matplotlib

---

# 🛠 Hardware Used

- Arduino Uno
- LDR (Light Dependent Resistor)
- 10kΩ Resistor
- Breadboard
- Jumper Wires
- USB Cable

---

# 💻 Software Stack

- Arduino IDE
- Python 3
- PySerial
- Matplotlib
- Collections (deque)

---

# 🧠 Engineering Concepts Covered

This project covers much more than reading a sensor.

## Electronics

- Voltage Divider
- Analog Voltage Measurement
- ADC (Analog-to-Digital Conversion)
- Sensor Characteristics
- Basic Breadboard Wiring

## Embedded Systems

- Arduino Analog Inputs
- Serial Communication
- Baud Rate
- Data Transmission
- Sensor Sampling

## Python

- PySerial
- Real-Time Data Acquisition
- Rolling Buffer using deque
- Matplotlib Animation
- Efficient Graph Updates

## Signal Processing

- Sensor Noise
- Exponential Moving Average (EMA)
- Signal Smoothing

## Real-Time Systems

- Processing Latency
- Serial Buffer Management
- Buffer Overflow
- Non-blocking GUI Programming

---

# ⚙ System Workflow

```
Ambient Light
      │
      ▼
     LDR
      │
      ▼
Voltage Divider
      │
      ▼
 Arduino ADC
      │
      ▼
 Serial Communication
      │
      ▼
     Python
      │
      ▼
 Signal Processing
      │
      ▼
Real-Time Visualization
```

---

# 📈 Features

- Real-time sensor monitoring
- Live scrolling graph
- Fixed-size rolling window
- Efficient memory usage
- Non-blocking visualization
- Noise reduction using EMA
- Continuous serial data acquisition

---

# 📂 Project Structure

```
Project-1/
│
├── Arduino/
│   └── ldr_sensor.ino
│
├── Python/
│   └── realtime_visualizer.py
│
├── Documentation/
│   └── Project1_Real-Time_Environmental_Data_Logger_and_Visualizer.pdf
│
├── Images/
│   ├── circuit.png
│   ├── setup.jpg
│   └── graph.png
│
├── Video/
│   └── demo.mp4
│
└── README.md
```

---

# 🚀 How to Run

## 1. Upload Arduino Code

Upload the Arduino sketch to your Arduino Uno.

---

## 2. Install Python Dependencies

```bash
pip install pyserial matplotlib
```

---

## 3. Update Serial Port

Windows

```python
COM3
```

Linux

```python
/dev/ttyACM0
```

---

## 4. Run

```bash
python realtime_visualizer.py
```

---

# 📊 Output

The application continuously displays

- Live ADC readings
- Scrolling graph
- Real-time sensor response
- Smoothed sensor signal

Covering the LDR causes the graph to immediately respond, demonstrating changes in ambient light intensity.

---

# 📚 Documentation

A complete engineering document is included explaining every concept used in this project, including:

- Voltage Divider Mathematics
- ADC Quantization
- Serial Communication
- Baud Rate Calculations
- Buffer Overflow Analysis
- Exponential Moving Average
- Real-Time Visualization
- Matplotlib Animation
- Python Code Walkthrough

---

[![Watch Demo](https://img.shields.io/badge/▶-Watch%20Demo-red?logo=youtube)](https://youtu.be/RplWNiwVUJc)
[![Documentation](https://img.shields.io/badge/📄-Documentation-blue)](Documentation/Project1_Real-Time_Environmental_Data_Logger_and_Visualizer.pdf)


# 🎥 Project Demonstration

Click the image below to watch the complete project demonstration.

[![Project Demo](https://img.youtube.com/vi/RplWNiwVUJc/maxresdefault.jpg)](https://youtu.be/RplWNiwVUJc)

> 📺 Demonstration includes:
> - Hardware setup
> - LDR sensor response
> - Arduino serial communication
> - Python real-time visualization
> - Live graph updates
---

# 🎯 Learning Outcome

By completing this project, I gained practical experience with:

- Hardware interfacing
- Embedded programming
- Analog electronics
- Serial communication
- Python hardware integration
- Signal processing
- Real-time systems
- Data visualization

More importantly, I learned how these individual topics combine into a complete robotics sensing pipeline.

---

# 🚧 Future Improvements

- Multiple sensor support
- Temperature and humidity sensors
- Data logging to CSV
- Interactive dashboard
- Wireless communication
- MQTT integration
- ROS2 integration
- Raspberry Pi implementation

---

# 📌 Repository Series

This repository is part of my **Project-Based Robotics Learning Journey**.

✅ Project 1/38: Real-Time Environmental Data Logger and Visualizer

More robotics projects will be added as I continue learning.

---

# 🤝 Connect

If you have suggestions, improvements, or feedback, feel free to open an issue or connect with me on LinkedIn.

If you found this project helpful, consider giving the repository a ⭐.
