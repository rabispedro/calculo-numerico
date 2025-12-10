# Bibliotecas utilizadas

import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy as np

f = lambda x : 0.2 + 25 * x - 200 * x ** 2 + 675 * x ** 3 - 900 * x ** 4 + 400 * x ** 5

inicio, fim = 0, 2

intervalo_simpson = 100
x_simpson = np.linspace(inicio, fim, intervalo_simpson)
y_simpson = np.zeros(intervalo_simpson)

for i in range(len(x_simpson)):
	soma_par = 0
	soma_impar = 0

	for j in range(0, intervalo_simpson, 2):
		soma_par += f(x_simpson[j])

	for j in range(1, intervalo_simpson, 2):
		soma_impar += f(x_simpson[j])

	y_simpson[i] = (fim - inicio) * (f(inicio) + 4 * soma_impar + 2 * soma_par + f(fim)) / (3*intervalo_simpson)

plt.plot(x_simpson, f(x_simpson), color='red', label="Função")
plt.plot(x_simpson, y_simpson, color='blue', marker='o', label="Simpson")

plt.title("Integral por 1/3 de Simpson")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.show()

resultado, erro = quad(f, inicio, fim)

print(f"Regra de 1/3 de Simpson com 100 intervalos: {y_simpson[-1]}")
print(f"Integral definida: {resultado}")

