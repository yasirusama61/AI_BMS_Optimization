import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# Step 1: Load and preprocess data
data = pd.read_csv('data/simulated_battery_data_realistic.csv')

# Convert 'Time' to datetime format
data['Datetime'] = pd.to_datetime(data['Time'], unit='s', origin='2024-01-01')
data = data.drop(columns=['Time'])

# Step 2: Add new feature (SOC change rate)
data['SOC_change'] = data['SOC'].diff().fillna(0)

# Step 3: Select features and target
features = ['Voltage', 'Current', 'SOC', 'SOH', 'Temperature', 'PumpDutyCycle', 'FanSpeed', 'LiquidLevel', 'AmbientTemp', 'SOC_change']
target = 'SOC'

# Step 4: Normalize features
scaler = MinMaxScaler()
data[features] = scaler.fit_transform(data[features])

# Step 5: Prepare data for LSTM
sequence_length = 100

def create_sequences(data, target_column, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[features].iloc[i:i+sequence_length].values)
        y.append(data[target_column].iloc[i+sequence_length])
    return np.array(X), np.array(y)

X, y = create_sequences(data, target, sequence_length)

# Step 6: Split data into training and testing sets
split_index = int(0.8 * len(X))
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Step 7: Build the LSTM model
model = Sequential()
model.add(LSTM(100, return_sequences=False, input_shape=(sequence_length, len(features))))
model.add(Dropout(0.2))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Step 8: Train the model with early stopping and capture history
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test), callbacks=[early_stopping])

# Step 9: Mode Definitions
modes = {
    'Performance': {
        'cooling_threshold': 35,  # Start cooling when temperature exceeds 35°C
        'max_current': 50,  # Allow high discharge current
        'max_temp': 40,  # Allow battery to run hot
    },
    'Eco': {
        'cooling_threshold': 30,  # Start cooling at lower temperature
        'max_current': 20,  # Limit discharge current for efficiency
        'max_temp': 35,  # Keep temperature lower for longer battery life
    },
    'Balanced': {
        'cooling_threshold': 33,  # Medium cooling threshold
        'max_current': 35,  # Moderate current allowed
        'max_temp': 37,  # Moderate temperature threshold
    }
}

# Step 10: Mode Selection Logic
def select_mode(current_temp, soc, current, mode='Balanced'):
    # Get mode parameters
    mode_params = modes[mode]
    
    # Adjust cooling if temperature exceeds threshold
    if current_temp > mode_params['cooling_threshold']:
        cooling_intensity = 'High'  # Increase cooling (fan speed, pump duty cycle)
    else:
        cooling_intensity = 'Low'
    
    # Limit current draw in eco mode
    if current > mode_params['max_current']:
        current = mode_params['max_current']  # Cap the current to save battery
    
    # Ensure temperature stays within the limit
    if current_temp > mode_params['max_temp']:
        print(f"Warning: Exceeding temperature limit in {mode} mode")
    
    return cooling_intensity, current

# Step 11: Use the Model to Make Predictions and Adjust Modes Dynamically
y_pred = model.predict(X_test)  # Predict future SOC

# Simulate selecting modes based on predicted SOC and temperature
for i in range(len(y_pred)):
    predicted_temp = np.random.uniform(25, 40)  # Example: Random predicted temperature
    current_mode = 'Balanced'  # Select mode (you can change this based on real-time conditions)
    
    # Get cooling intensity and adjusted current based on the selected mode
    cooling_intensity, adjusted_current = select_mode(predicted_temp, soc=y_pred[i], current=40, mode=current_mode)
    
    # Print results for each step
    print(f"Step {i}: Mode: {current_mode}, Predicted Temp: {predicted_temp:.2f}, Cooling: {cooling_intensity}, Adjusted Current: {adjusted_current:.2f}")

# Step 12: Plot Actual vs Predicted SOC
plt.figure(figsize=(10, 6))
plt.plot(y_test, label='Actual SOC', color='b')
plt.plot(y_pred, label='Predicted SOC', color='r', linestyle='--')
plt.title('Actual vs Predicted SOC')
plt.xlabel('Time Step')
plt.ylabel('SOC')
plt.legend()
plt.show()

# Step 13: Plot Loss Curves
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Training Loss', color='b')
plt.plot(history.history['val_loss'], label='Validation Loss', color='r')
plt.title('Training and Validation Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
