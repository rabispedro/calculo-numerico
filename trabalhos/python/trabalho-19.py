# Bibliotecas utilizadas

import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy as np

f = lambda x : 0.2 + 25 * x - 200 * x ** 2 + 675 * x ** 3 - 900 * x ** 4 + 400 * x ** 5

inicio, fim = 0, 2

intervalo_simpson = 101
x_simpson = np.linspace(inicio, fim, intervalo_simpson)
y_simpson = np.zeros(intervalo_simpson)

for i in range(len(x_simpson)):
	soma_multiplo = 0
	soma_nao_multiplo = 0

	for j in range(intervalo_simpson):
		if j % 3 == 0:
			soma_multiplo += f(x_simpson[j])
		else:
			soma_nao_multiplo += f(x_simpson[j])

	y_simpson[i] = 3 * (fim - inicio) * (f(inicio) + 3 * soma_nao_multiplo + 2 * soma_multiplo + f(fim)) / (8*intervalo_simpson)

plt.plot(x_simpson, f(x_simpson), color='red', label="Função")
plt.plot(x_simpson, y_simpson, color='blue', marker='o', label="Simpson")

plt.title("Integral por 1/3 de Simpson")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.show()

resultado, erro = quad(f, inicio, fim)

print(f"Regra de 3/8 de Simpson com {intervalo_simpson} intervalos: {y_simpson[-1]}")
print(f"Integral definida: {resultado}")
