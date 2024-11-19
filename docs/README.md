# 🚀 **AI Battery Management System (AI BMS) – Battery Performance Optimization**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-PyQt5%2FTkinter-green)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-orange)](#)

---

## 🌟 **Project Overview**
This project is part of the **AI Battery Management System (AI BMS)** initiative. The goal is to develop a **real-time mode selection interface** that allows users to optimize battery performance, efficiency, and longevity. 

Users can choose between several operational modes, including:
- **⚡ Performance Mode**
- **🌱 Eco Mode**
- **⚖️ Balanced Mode**
- **🛠️ Custom Mode**

Modes dynamically adjust parameters such as **cooling**, **fan speed**, and **temperature settings**.

---

## 📊 User Interface Prototype

Below is a prototype of the **AI Battery Management System (AI BMS)** optimization interface:

![UI Prototype](images/ui_prototype.png)

### Key Features of the Interface:

1. **Mode Selection**:
   - Users can choose between:
     - ⚡ **Performance Mode**: Maximize performance at the potential expense of battery life.
     - 🌱 **Eco Mode**: Optimize energy efficiency and extend battery life.
     - ⚖️ **Balanced Mode**: A middle ground between performance and efficiency.
     - 🛠️ **Custom Mode**: Configure user-defined parameters.

2. **Custom Mode Settings**:
   - Options to adjust:
     - **Cooling Mode** (Normal, Silent, Aggressive)
     - **Fan Speed** via slider
     - **Flow Rate** via slider
     - **Temperature Threshold** via slider
   - Enable/Disable advanced settings:
     - ✅ Overheat Protection
     - ✅ Fast Charging

3. **Impact Visualizations**:
   - **Performance Impact**: Bar chart showing mode-specific performance effects.
   - **Efficiency Impact**: Highlights energy efficiency in each mode.
   - **Longevity Impact**: Demonstrates how modes affect battery lifespan.

4. **Interactive Controls**:
   - **Apply, Save, Cancel** buttons for user actions.
   - Real-time visualization of the selected mode's impact.

---

## ✨ **Features**
- 🔄 **Mode Switching**: Users can select operational modes that dynamically adjust system parameters like fan speed and cooling temperature.
- 🛠️ **Custom Mode**: Users can personalize parameters such as fan speed and temperature thresholds, and see real-time effects on battery performance.
- 📈 **Dynamic Updates**: Real-time graphs display the impact of mode changes on performance, efficiency, and battery longevity.
- 🤖 **Auto Adjustments**: AI models automatically switch modes based on operating conditions.
- 🚗 **Applications**: Used in **electric vehicles** and **energy storage systems** to optimize battery performance in real time.

---

## 🛠️ **Technologies Used**
- **Programming Language**: 🐍 Python
- **GUI Framework**: PyQt5 / Tkinter
- **Real-time Visualization**: Matplotlib 📊
- **AI Models**: SOC estimation and temperature prediction using LSTM
- **Data Handling**: Pandas, NumPy

---

## 📂 **Project Structure**
```plaintext
AI_BMS_Optimization/
│
├── data/               # Data storage
│   ├── raw/            # Raw input data
│   ├── processed/      # Preprocessed data ready for use
│   └── sample_input.csv # Example data for testing
│
├── src/                # Source code
│   ├── gui.py          # GUI implementation (PyQt/Tkinter)
│   ├── real_time_mode_switching.py # Core script for mode switching
│   ├── models.py       # Includes SOC and temperature prediction models
│   ├── utils.py        # Helper functions (e.g., data preprocessing)
│
├── docs/               # Documentation
│   └── README.md       # Description, usage, and instructions
│
├── tests/              # Test scripts
│   ├── test_models.py  # Unit tests for SOC and temperature models
│
├── requirements.txt    # Dependencies
└── .gitignore          # Ignore unnecessary files
```

### 🔄 **Modes**

| **Mode**            | **Description**                                                                                  |
|----------------------|--------------------------------------------------------------------------------------------------|
| ⚡ **Performance**   | Prioritizes maximum battery performance by increasing cooling and fan speed, potentially reducing battery lifespan. |
| 🌱 **Eco**           | Focuses on battery longevity and energy efficiency by lowering cooling intensity and regulating power usage. |
| ⚖️ **Balanced**      | Strikes a balance between performance and efficiency with moderate cooling and power settings.    |
| 🛠️ **Custom**        | Empowers users to define parameters like fan speed and cooling thresholds, observing real-time effects. |

---

### 🧠 **How It Works**

1. **Real-Time Data Collection**:
   - The system continuously monitors and collects real-time battery parameters, including:
     - 🌡️ **Temperature**
     - ⚡ **Voltage**
     - 🔋 **SOC (State of Charge)**
     - 🔄 **Current**
     - 🌬️ **Fan Speed**
     - 💧 **Pump Duty Cycle**

2. **AI-Powered Predictions**:
   - AI models predict key battery metrics such as:
     - SOC (State of Charge)
     - Temperature trends
   - Predictions help dynamically optimize battery performance and longevity.

3. **Interactive Graphical Interface**:
   - The GUI, built with **PyQt5/Tkinter**, allows users to:
     - Seamlessly switch between modes.
     - Visualize real-time impacts on battery performance via dynamic Matplotlib plots.

---

### 🤖 **Dynamic Mode Switching**

- **AI-Driven Adjustments**:
  - The system automatically adjusts cooling intensity, fan speed, and other parameters based on:
    - The **selected mode** (Performance, Eco, Balanced, or Custom).
    - **Predicted SOC and temperature** from AI models.
  
- **Custom Mode**:
  - Users can manually fine-tune settings like cooling thresholds and fan speeds.
  - The system provides real-time feedback to help users evaluate their custom configurations.


### 🚀 Installation
To set up the project locally, follow these steps:

1. Clone the repository:

`git clone https://github.com/yasirusama61/AI_BMS_Optimization.git`
`cd AI_BMS_Optimization`

2. Install the dependencies 

`pip install -r requirements.txt`

3. **Run the GUI**: To start the GUI for the mode selection interface, run:

`python src/gui.py`

### Data Used
- **Battery Operation Data**: Voltage, Current, SOC, Temperature, Pump Duty Cycle, and Fan Speed.
- **Environmental Data**: Ambient temperature data (Tx) to dynamically adjust system performance.
- **Historical Performance Data**: Used to train the AI models on performance metrics under different conditions.


## 📊 Real-Time Output Example

The AI Battery Management System (AI BMS) provides real-time predictions and dynamically adjusts battery parameters based on the selected mode. Below is an example of the output generated during a simulation:

### 🔍 **Highlighted Output**

- **Mode**: Balanced
- **Predicted Temperature (°C)**: Real-time temperature predictions using the AI model.
- **Cooling**: Cooling intensity automatically adjusted (`Low` or `High`).
- **Adjusted Current (A)**: Battery current modified dynamically.
- **Warnings**: Alerts for exceeding critical thresholds.

---

### 🖼️ **Sample Output**

| **Step** | **Mode**      | **Predicted Temp** | **Cooling** | **Adjusted Current** | **Warnings**                                         |
|----------|---------------|--------------------|-------------|-----------------------|-----------------------------------------------------|
| 0        | Balanced      | 25.21°C           | Low         | 35.00 A              |                                                     |
| 1        | Balanced      | 34.70°C           | High        | 35.00 A              |                                                     |
| 2        | Balanced      | 38.89°C           | High        | 35.00 A              | ⚠️ Exceeding temperature limit in Balanced mode     |
| 3        | Balanced      | 32.04°C           | Low         | 35.00 A              |                                                     |
| 4        | Balanced      | 34.95°C           | High        | 35.00 A              |                                                     |
| 13       | Balanced      | 36.47°C           | High        | 35.00 A              | ⚠️ Exceeding temperature limit in Balanced mode     |
| 14       | Balanced      | 37.52°C           | High        | 35.00 A              | ⚠️ Exceeding temperature limit in Balanced mode     |
| 22       | Balanced      | 36.20°C           | High        | 35.00 A              | ⚠️ Exceeding temperature limit in Balanced mode     |

---

### 🚨 **What These Outputs Show**

1. **Real-Time Adjustments**:
   - The system adjusts cooling intensity and current dynamically based on real-time predictions.
   - `High Cooling` is activated when the predicted temperature exceeds the mode's threshold.

2. **Warnings**:
   - Alerts (`⚠️`) indicate when critical thresholds (e.g., temperature limits) are exceeded.

3. **Insight into Mode Functionality**:
   - The `Balanced Mode` prioritizes stability with controlled cooling and current.

---

### 📝 **Insights for Developers**

- The table demonstrates the AI system's capability to adapt to dynamic battery conditions in real time.
- Warnings help highlight potential issues that require attention, such as exceeding the temperature threshold.

## 🤝 Contributing
We welcome contributions! Please feel free to fork the repository, submit pull requests, or report issues.