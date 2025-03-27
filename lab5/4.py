import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# Дефиниране на таблицата с данни
data = {
    'Разходи за реклама': [2, 3, 4, 5, 6, 7],
    'Продадени бройки': [10, 29, 66, 127, 218, 345]
}
df = pd.DataFrame(data)

# Визуализация на данните в графика
plt.scatter(df['Разходи за реклама'], df['Продадени бройки'], color='red')
plt.xlabel('Разходи за реклама (хил. лв.)')
plt.ylabel('Продадени бройки')
plt.title('Продажби спрямо разходите за реклама')
plt.show()

# Разделяне на данните
X = df.iloc[:, 0:1].values
y = df.iloc[:, 1].values

# Полиномиална трансформация
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Обучение на модела
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)

# Визуализация на резултатите
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X_poly), color='blue')
plt.xlabel('Разходи за реклама (хил. лв.)')
plt.ylabel('Продадени бройки')
plt.title('Полиномен регресионен модел')
plt.show()

# Прогноза за нови данни
X_test = np.array([8, 9, 10]).reshape(-1, 1)
X_test_poly = poly.transform(X_test)
y_pred = lin_reg.predict(X_test_poly)

# Извеждане на прогнозите
print("Прогнозирани продажби за разходи 8, 9, 10 хил. лв.:")
print(y_pred)

