# AI Battery Management System (AI BMS) – Battery Performance Optimization

## Project Overview
This project is part of the **AI Battery Management System (AI BMS)** initiative. The goal is to develop a **real-time mode selection interface** that allows users to optimize battery performance, efficiency, and longevity. Users can choose between several operational modes, including **Performance Mode**, **Eco Mode**, **Balanced Mode**, and **Custom Mode**, with dynamic adjustments to parameters such as cooling, fan speed, and temperature settings.

### Features
- **Mode Switching**: Users can select operational modes that dynamically adjust system parameters like fan speed and cooling temperature.
- **Custom Mode**: Users can personalize parameters such as fan speed and temperature thresholds, and see real-time effects on battery performance.
- **Dynamic Updates**: Real-time graphs display the impact of mode changes on performance, efficiency, and battery longevity.
- **Auto Adjustments**: AI models automatically switch modes based on operating conditions.
- **Application**: This feature will be used in **electric vehicles** and **energy storage systems** to optimize battery performance in real time, enhancing both **efficiency** and **lifespan**.

## Technologies Used
- **Programming Language**: Python
- **GUI Framework**: PyQt5/Tkinter
- **Real-time Visualization**: Matplotlib
- **AI Models**: Custom models for predicting and optimizing battery behavior
- **Data Handling**: Pandas, Numpy

## Project Structure
```plaintext
AI_BMS_Optimization/
│
├── data/               # Raw and processed data
│   ├── raw/            # Store your initial datasets
│   └── processed/      # Processed or cleaned data
│
├── src/                # Source code
│   ├── gui.py          # GUI development using PyQt/Tkinter
│   ├── models.py       # AI models for battery optimization
│   ├── mode_selection.py # Core logic for different modes
│   ├── data_processing.py # Scripts for data cleaning and feature extraction
│
├── visualization/      # Matplotlib visualizations
│   └── performance_visuals.py # Real-time graphs displaying performance metrics
│
├── docs/               # Documentation files
│   └── README.md        # Project description and usage instructions
│
├── .gitignore          # Git ignore file
└── requirements.txt    # List of dependencies
```

### Modes

- **Performance Mode**: Prioritizes high battery performance by increasing cooling, which may reduce battery lifespan.
- **Eco Mode**: Maximizes battery longevity and energy efficiency by lowering the cooling speed and regulating power usage.
- **Balanced Mode**: Provides a middle ground between performance and efficiency.
- **Custom Mode**: Allows users to define their own parameters such as fan speed, cooling thresholds, and more.

### How It Works

- Real-Time Data: The system collects real-time data from the battery, including temperature, voltage, SOC (State of Charge), current, fan speed, and pump duty cycle.
- AI Models: The AI models predict and optimize battery behavior based on real-time data and user-selected modes.
- Graphical Interface: Users interact with a GUI developed using PyQt/Tkinter, where they can switch between modes and observe real-time impacts on performance via Matplotlib plots.

### Dynamic Mode Switching

The AI models automatically adjust the battery system settings based on the selected mode and current operating conditions. In Custom Mode, users can manually adjust the settings and observe the changes in real-time.


### Installation
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
