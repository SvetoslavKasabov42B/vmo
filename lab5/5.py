import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Данни
days = np.array([1, 2, 3, 4, 5, 6, 7])
spam = np.array([2, 4, 4, 5, 6, 7, 8])

# Логистична функция
def logistic_function(x, A, k, x0):
    return A / (1 + np.exp(-k * (x - x0)))

# Нелинейна регресия
popt, pcov = curve_fit(logistic_function, days, spam, maxfev=5000)

# Извеждане на коефициентите
print('Коефициенти: A = {:.4f}, k = {:.2f}, x0 = {:.3f}'.format(*popt))

# Графика
x_vals = np.linspace(1, 10, 100)
y_vals = logistic_function(x_vals, *popt)

plt.plot(days, spam, 'ro', label='Данни')
plt.plot(x_vals, y_vals, 'b-', label='Модел')
plt.xlabel("Ден")
plt.ylabel("Брой спам съобщения")
plt.legend()
plt.show()

# Прогноза за 10-тия ден
spam_pred = round(logistic_function(10, *popt))
print(f"Прогнозен брой спам съобщения на 10-тия ден: {spam_pred}")

