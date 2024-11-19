import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from models import predict_soc, predict_temperature  # Ensure models.py has these functions

# Step 1: Load and preprocess data
data = pd.read_csv('data/battery_data_realistic.csv')

# Convert 'Time' to datetime format
data['Datetime'] = pd.to_datetime(data['Time'], unit='s', origin='2024-01-01')
data = data.drop(columns=['Time'])

# Step 2: Add new feature (SOC change rate)
data['SOC_change'] = data['SOC'].diff().fillna(0)

# Step 3: Select features
features = ['Voltage', 'Current', 'SOC', 'SOH', 'Temperature', 'PumpDutyCycle', 'FanSpeed', 'LiquidLevel', 'AmbientTemp', 'SOC_change']

# Normalize features
scaler = MinMaxScaler()
data[features] = scaler.fit_transform(data[features])

# Define sequence length
sequence_length = 100

# Create sequences for real-time predictions
def create_sequences(data, sequence_length):
    X = []
    for i in range(len(data) - sequence_length):
        X.append(data[features].iloc[i:i+sequence_length].values)
    return np.array(X)

X = create_sequences(data, sequence_length)

# Step 4: Define Mode Logic
modes = {
    'Performance': {
        'cooling_threshold': 35,
        'max_current': 50,
        'max_temp': 40,
    },
    'Eco': {
        'cooling_threshold': 30,
        'max_current': 20,
        'max_temp': 35,
    },
    'Balanced': {
        'cooling_threshold': 33,
        'max_current': 35,
        'max_temp': 37,
    }
}

def select_mode(predicted_temp, predicted_soc, current, mode='Balanced'):
    mode_params = modes[mode]
    
    # Cooling adjustments
    cooling_intensity = 'High' if predicted_temp > mode_params['cooling_threshold'] else 'Low'
    
    # Adjust current based on mode constraints
    adjusted_current = min(current, mode_params['max_current'])
    
    # Temperature warnings
    if predicted_temp > mode_params['max_temp']:
        print(f"Warning: Exceeding temperature limit in {mode} mode")
    
    return cooling_intensity, adjusted_current

# Step 5: Use Pre-trained Models for Predictions
for i in range(len(X)):
    # Predict SOC and temperature using pre-trained models
    predicted_soc = predict_soc(X[i])
    predicted_temp = predict_temperature(X[i])
    
    # Select mode and adjust parameters
    current_mode = 'Balanced'
    cooling_intensity, adjusted_current = select_mode(predicted_temp, predicted_soc, current=40, mode=current_mode)
    
    # Print results for each step
    print(f"Step {i}: Mode: {current_mode}, Predicted Temp: {predicted_temp:.2f}°C, Cooling: {cooling_intensity}, Adjusted Current: {adjusted_current:.2f} A")

# Step 6: Visualize Results
# (For demonstration purposes, replace these with actual data from your models)
y_pred = [predict_soc(x) for x in X]  # Predicted SOC
y_test = data['SOC'][sequence_length:].values  # Actual SOC for comparison

# Plot Actual vs Predicted SOC
plt.figure(figsize=(10, 6))
plt.plot(y_test, label='Actual SOC', color='b')
plt.plot(y_pred, label='Predicted SOC', color='r', linestyle='--')
plt.title('Actual vs Predicted SOC')
plt.xlabel('Time Step')
plt.ylabel('SOC')
plt.legend()
plt.show()
