import pickle
import numpy as np

# Load the trained model
filename = 'trained_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Collect the sensor data and image data for the new food product
sensor_data = [temperature, humidity, light exposure, packaging]
image_data = [captured_image]

# Preprocess the sensor data and image data if needed
# ...

# Use the trained model to predict the freshness of the food product
prediction = loaded_model.predict(np.array([sensor_data + image_data]))