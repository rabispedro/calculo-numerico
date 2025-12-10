# Bibliotecas utilizadas

import matplotlib.pyplot as plt
import numpy as np

h = 0.25
steps = 5
x = np.linspace(0, 1, steps)

y = np.zeros(steps)
y[0] = 1

print(x, y)

phi = lambda x, y : y * (x ** 3) - 1.5 * y

for i in range(len(x) - 1):
	preditora = y[i] + phi(x[i], y[i]) * h
	y[i+1] = y[i] + (h/2) * (phi(x[i], y[i]) + phi(x[i+1],preditora))

print(f"Heun: {y}")

plt.plot(x, y, color='blue', marker='o', label="Heun com iteracao")

plt.title("Derivada por Euller")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()

plt.show()
