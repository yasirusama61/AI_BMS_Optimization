from PyQt5 import QtWidgets, QtCore
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from models import predict_soc, predict_temperature
import numpy as np
import pandas as pd

# Dummy data for testing
data = pd.read_csv("data/simulated_battery_data_realistic.csv")
sequence_length = 100
features = ['Voltage', 'Current', 'SOC', 'SOH', 'Temperature', 'PumpDutyCycle', 'FanSpeed', 'LiquidLevel', 'AmbientTemp']
data = data[features].iloc[:sequence_length].values


class BatteryPerformanceCanvas(FigureCanvas):
    """Matplotlib canvas for visualizing SOC and temperature trends."""

    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(figsize=(5, 3))
        super().__init__(self.fig)
        self.setParent(parent)

    def update_plot(self, soc_values, temp_values, time_steps):
        """Update the plot with new SOC and temperature values."""
        self.ax.clear()
        self.ax.plot(time_steps, soc_values, label="SOC (%)", color="blue")
        self.ax.plot(time_steps, temp_values, label="Temperature (°C)", color="red")
        self.ax.set_title("Battery Performance")
        self.ax.set_xlabel("Time Step")
        self.ax.set_ylabel("Value")
        self.ax.legend()
        self.draw()


class BatteryManagementGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Battery Management System")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        layout = QtWidgets.QVBoxLayout()

        # Mode Selection
        self.mode_label = QtWidgets.QLabel("Select Mode:")
        self.mode_selector = QtWidgets.QComboBox()
        self.mode_selector.addItems(["Balanced", "Performance", "Eco", "Custom"])
        self.mode_selector.currentIndexChanged.connect(self.change_mode)

        # Real-Time SOC and Temperature Labels
        self.soc_label = QtWidgets.QLabel("SOC: -")
        self.temp_label = QtWidgets.QLabel("Temperature: -")

        # Start Simulation Button
        self.start_button = QtWidgets.QPushButton("Start Simulation")
        self.start_button.clicked.connect(self.run_simulation)

        # Canvas for Battery Performance Visualization
        self.canvas = BatteryPerformanceCanvas(self)

        # Add widgets to layout
        layout.addWidget(self.mode_label)
        layout.addWidget(self.mode_selector)
        layout.addWidget(self.soc_label)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

        # Initialize state
        self.mode = "Balanced"
        self.time_step = 0
        self.soc_values = []
        self.temp_values = []

    def change_mode(self):
        """Change the current mode based on user selection."""
        self.mode = self.mode_selector.currentText()
        print(f"Mode changed to: {self.mode}")

    def run_simulation(self):
        """Simulate battery performance updates."""
        self.soc_values = []
        self.temp_values = []
        self.time_step = 0

        # Simulate SOC and temperature for 100 steps
        for _ in range(100):
            # Generate random input data for predictions
            input_data = np.expand_dims(data[self.time_step % sequence_length], axis=0)
            soc = predict_soc(input_data)
            temp = predict_temperature(input_data)

            # Update SOC and temperature values
            self.soc_values.append(soc)
            self.temp_values.append(temp)

            # Update labels
            self.soc_label.setText(f"SOC: {soc:.2f} %")
            self.temp_label.setText(f"Temperature: {temp:.2f} °C")

            # Update plot
            time_steps = list(range(len(self.soc_values)))
            self.canvas.update_plot(self.soc_values, self.temp_values, time_steps)

            # Simulate real-time delay
            QtCore.QCoreApplication.processEvents()
            QtCore.QThread.msleep(100)
            self.time_step += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = BatteryManagementGUI()
    gui.show()
    sys.exit(app.exec_())
