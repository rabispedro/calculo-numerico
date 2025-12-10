# Bibliotecas utilizadas

import matplotlib.pyplot as plt
import numpy as np

# Espaço para armazenar os valores iniciais do problema

# f(x) = e^(x) - 4 + (7/2 * cos(2x))
def funcao(x):
	return np.pow(np.e, x) - 4 + (3.5 * np.cos(2 * x))

intervalos = 1000
valores = np.linspace(0, 3, intervalos)
pontos = np.zeros(len(valores))
raizes = [[], []]

# O método de busca incremental testa o valor da função em intervalos uniformemente espaçados
# e encontra novos limites por meio da identificação de mudança de sinal entre os pontos vizinhos

pontos[0] = funcao(valores[0]) # Iniciando o primeiro valor, que será utilizado no laço
for i in range(1, intervalos):
	pontos[i] = funcao(valores[i]) # Calculando o valor do intervalo atual, ou seja, y = f(x)

	if(pontos[i] * pontos[i-1] < 0.0): # Condição da busca incremental
		print(f"Raiz em x = {valores[i]:.6f}")
		raizes[0].append(valores[i])
		raizes[1].append(pontos[i])

plt.plot(raizes[0], raizes[1], color='blue', marker='o') # Pontos das Raízes
plt.plot((0, 3), (0, 0), color='black') # Reta do eixo X
plt.plot((0, 0), (-5, 20), color='black') # Reta do eixo Y
plt.plot(valores, pontos, color='red') # Função original

plt.title("Função original f(x) e sua(s) raiz(es)")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()

