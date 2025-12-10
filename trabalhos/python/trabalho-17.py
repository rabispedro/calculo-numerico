# Bibliotecas utilizadas

import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy as np

f = lambda x : 0.2 + 25 * x - 200 * x ** 2 + 675 * x ** 3 - 900 * x ** 4 + 400 * x ** 5

inicio, fim = 0, 2

intervalo_trapezio = 100
x_trapezio = np.linspace(inicio, fim, intervalo_trapezio+1)
y_trapezio = np.zeros(intervalo_trapezio+1)

soma = 0
for i in range(len(x_trapezio)):
    soma += f(x_trapezio[i])
    y_trapezio[i] = (fim - inicio) * (f(inicio) + 2 * soma + f(fim)) / (2 * (intervalo_trapezio))

plt.plot(x_trapezio, f(x_trapezio), color='red', label="Função")
plt.plot(x_trapezio, y_trapezio, color='green', marker='o', label="Trapézio")

plt.title("Integral por Trapézio")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.show()

# Função de integral para verificar os valores
resultado, erro = quad(f, inicio, fim)

print(f"Regra do Trapézio com {intervalo_trapezio} intervalos: {y_trapezio[-1]}")
print(f"Integral definida: {resultado}")
