import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 2.01, 0.01)
y = x**2

plt.plot(x, y)
plt.title("Plot of y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

