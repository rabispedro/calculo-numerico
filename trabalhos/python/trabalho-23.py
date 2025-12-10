# Bibliotecas utilizadas

import matplotlib.pyplot as plt
import numpy as np

# phi = y * t^3 - 1.5 * y
def funcao_incremento(t, y):
	return (y * (t ** 3)) + (-1.5 * y)

h = 0.25
t = 0
y = 1
y_ant = 1

inicio, fim = 0, 1
valores = [[], []]

i = inicio
while (i < fim):
    y_ant = y
    t_ant = t

    y_medio = y_ant + funcao_incremento(t_ant, y_ant) * (h/2)
    t_medio = t + (h/2)
    y = y_ant + funcao_incremento(t_medio, y_medio) * h
	
    t = t_ant + h
    valores[0].append(i)
    valores[1].append(y)

    i += h

for i in range(len(valores[0])):
    print(f"X: {valores[0][i]:6.6f}\tY: {valores[1][i]:6.6f}")

plt.plot(valores[0], valores[1], color='blue', marker='o') # Pontos da função

plt.title("Função original f(x) e su")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()
