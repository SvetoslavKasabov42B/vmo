import tensorflow as tf

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(42)
X = np.random.rand(1000, 11) * [10, 1, 1, 20, 0.1, 60, 200, 1.005, 4, 1, 15]
y = np.random.rand(1000) * 10  # "Цената" или "качеството"

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(11,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

model.fit(X_train, y_train, epochs=50, batch_size=16, validation_data=(X_test, y_test), verbose=0)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
print("Средна абсолютна грешка:", mae)

new_data = np.array([
    [7.1, 0.16, 0.28, 14.3, 0.045, 39, 111, 0.99146, 3.19, 0.64, 10.2],
    [6.9, 0.19, 0.35, 6.4, 0.044, 19, 96, 0.9949, 3.51, 0.43, 9.7]
])

new_data_scaled = scaler.transform(new_data)

predictions = model.predict(new_data_scaled)
print("Предсказани цени за нови данни:")
print(predictions)

