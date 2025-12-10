# Bibliotecas utilizadas

import matplotlib.pyplot as plt
import numpy as np

x = [-1, 0, 1, 2]
y = [7, 4, 1, 4]

y_lagrange = [0 for _ in range(len(x))]

# Usando:
x1 = 0
x2 = 1
x3 = 2
x4 = 3

L1 = lambda xi : (xi - x2) / (x1 - x2)
L2 = lambda xi: (xi - x1) / (x2 - x1)

lagrange = lambda xi : L1(xi) * y[x1] + L2(xi) * y[x2]

for i in range(len(x)):
	y_lagrange[i] = lagrange(x[i])

plt.plot(x, y_lagrange, color='blue', marker='o', label="Lagrange de 3ª Ordem")
plt.plot(x, y, color='red', label="Função Original")

plt.title("Polinômio Interpolador de Newton")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.show()

i = -100
while (i <= 100):
	if (lagrange(i) < 5.1 and lagrange(i) > 4.999):
		print(f"f({i}) == {lagrange(i)}")
		break
	i += 0.01