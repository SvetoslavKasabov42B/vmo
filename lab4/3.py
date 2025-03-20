import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load CSV file
imoti_data = pd.read_csv('houses_prices.csv', sep=',')

# Extract features (X) and target variable (y)
X = imoti_data[['Area']].values  # Reshape for sklearn
y = imoti_data['Price'].values

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Get regression parameters
slope = model.coef_[0]  # b (наклон)
intercept = model.intercept_  # a (свободен член)
r2 = r2_score(y, model.predict(X))  # R² (коефициент на детерминация)

# Predict price for an area of 75 m²
predicted_price = model.predict([[75]])[0]

# Print results
print(f'Линейно уравнение: y = {slope:.2f}x + {intercept:.2f}')
print(f'Коефициент на детерминация (R²): {r2:.3f}')
print(f'Прогнозна цена за 75 кв.м: {predicted_price:.2f} евро')

# Plot the regression line
plt.scatter(X, y, color='blue', label='Данни')
plt.plot(X, model.predict(X), color='red', label='Регресионна линия')
plt.scatter([[75]], [[predicted_price]], color='green', marker='o', label='Прогноза (75 кв.м)')
plt.xlabel('Площ (кв.м)')
plt.ylabel('Цена (евро)')
plt.legend()
plt.title('Линеен регресионен модел за цени на имоти')
plt.show()

