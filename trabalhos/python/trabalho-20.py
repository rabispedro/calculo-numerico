# Bibliotecas utilizadas

import matplotlib.pyplot as plt
import numpy as np

h = 0.25
steps = 5
x = np.linspace(0, 1, steps)

y_euller = np.zeros(steps)
y_euller[0] = 1

phi = lambda x, y : y * (x ** 3) - 1.5 * y

for i in range(len(x) - 1):
	y_euller[i+1] = y_euller[i] + phi(x[i], y_euller[i]) * h

print(f"Euller: {y_euller}")

plt.plot(x, y_euller, color='blue', marker='o', label="Euller")

plt.title("Derivada por Euller")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()

plt.show()