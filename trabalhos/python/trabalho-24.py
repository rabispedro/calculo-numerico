# Bibliotecas utilizadas

import matplotlib.pyplot as plt
import numpy as np

h = 0.25
steps = 5
x = np.linspace(0, 1, steps)

y_rk = np.zeros(steps)
y_rk[0] = 1

phi = lambda x, y : y * (x ** 3) - 1.5 * y

for i in range(len(x) - 1):
	k1 = phi(x[i], y_rk[i])
	k2 = phi(x[i] + h/2, y_rk[i] + (k1 * h) / 2)
	k3 = phi(x[i] + h/2, y_rk[i] + (k2 * h) / 2)
	k4 = phi(x[i] + h, y_rk[i] + (k3 * h))
	
	y_rk[i+1] = y_rk[i] + (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)

print(f"RK de 4ª Ordem: {y_rk}")

plt.plot(x, y_rk, color='green', marker='o', label="RK de 4ª Ordem")

plt.title("Derivada por Euller e RK de 4ª Ordem")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()

plt.show()
