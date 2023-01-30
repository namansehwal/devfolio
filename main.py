import pyserial
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Collect sensor data
ser = pyserial.Serial('COM3')
sensor_data = []
while True:
    line = ser.readline().strip().decode('utf-8')
    if line:
        data = [float(x) for x in line.split(',')]
        sensor_data.append(data)

# Collect image data
import cv2
import os

def extract_features(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray.flatten()

image_data = []
for filename in os.listdir('images'):
    img = cv2.imread(os.path.join('images', filename))
    features = extract_features(img)
    image_data.append(features)

# Combine sensor and image data
data = np.hstack((sensor_data, image_data))
df = pd.DataFrame(data, columns=['temperature', 'humidity', 'light', 'packaging', 'image_features'])

# Train the model
X = df.drop('freshness', axis=1)
y = df['freshness']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
score = model.score(X_test, y_test)
print(f'Accuracy: {score}')