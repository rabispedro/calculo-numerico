x = [10, 11, 12, 13, 14, 15]
y = [1400, 1900, 2500, 3250, 4200, 5400]

y_newton = [0 for _ in range(len(x))]

# Usando:
diferenca = lambda x1, x2 : (y[x1] - y[x2]) / (x1 - x2)

x1 = 0
x2 = 1
x3 = 3
x4 = 5

b1 = y[x1]
b2 = diferenca(x2, x1)
b3 = (diferenca(x3, x2) - b2) / (x3 - x1)
b4 = (((diferenca(x4, x3) - diferenca(x3, x2)) / (x4 - x2)) - b3) / (x4 - x1)

newton = lambda xi : b1 + b2 * (xi - x[x1]) + b3 * (xi - x[x1]) * (xi - x[x2]) + b4 * (xi - x[x1]) * (xi - x[x2]) * (xi - x[x3])

for i in range(len(x)):
	y_newton[i] = newton(x[i])

plt.plot(x, y_newton, color='blue', marker='o', label="Newton de 3ª Ordem")
plt.plot(x, y, color='red', label="Função Original")

plt.title("Polinômio Interpolador de Newton")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.show()

print(f"f(11.8) = {newton(11.8)}")