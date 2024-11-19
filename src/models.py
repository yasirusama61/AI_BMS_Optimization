import tensorflow as tf
import numpy as np

# Load pre-trained models
SOC_MODEL_PATH = "models/soc_lstm_model.h5"
TEMP_MODEL_PATH = "models/temperature_model.h5"

# Load SOC model
soc_model = tf.keras.models.load_model(SOC_MODEL_PATH)

# Load Temperature model
temp_model = tf.keras.models.load_model(TEMP_MODEL_PATH)

def predict_soc(input_features):
    """Predict SOC using the pre-trained SOC model."""
    input_features = np.expand_dims(input_features, axis=0)
    return soc_model.predict(input_features)[0][0]

def predict_temperature(input_features):
    """Predict Temperature using the pre-trained Temperature model."""
    input_features = np.expand_dims(input_features, axis=0)
    return temp_model.predict(input_features)[0][0]
