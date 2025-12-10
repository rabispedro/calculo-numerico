# Bibliotecas utilizadas

import matplotlib.pyplot as plt
import numpy as np

# Espaço para armazenar os valores iniciais do problema

# f(x) = e^(x) - 4 + (7/2 * cos(2x))
def funcao(x):
	return np.pow(np.e, x) - 4 + (3.5 * np.cos(2 * x))

criterio_parada = 0.0000001

raizes = [[], []]

inferior = 0.0
superior = 3.0
meio = (inferior + superior) / 2

y_inferior = funcao(inferior)
y_meio = funcao(meio)
y_superior = funcao(superior)

# O método da bissecção é uma variação do método de busca incremental em que o intervalo é sempre dividido ao meio
# Se uma função muda de sinal durante um intervalo, o valor da função no ponto médio é avaliado
# A localização da raiz é então determinada como estando dentro do sub-intervalo em que ocorre a mudança de sinal
# O erro absoluto é reduzido por um fator de 2 para cada iteração

while ((y_inferior * y_superior) > 0): # Procura pelo primeiro sub-intervalo com diferença de sinais
	# print(f"Intervalo: [{inferior}, {superior}]: ({inferior}, {y_inferior}) e ({superior}, {y_superior})")

	meio = (inferior + superior) / 2

	y_inferior = funcao(inferior)
	y_meio = funcao(meio)
	y_superior = funcao(superior)

	if (y_inferior * y_meio) < 0:
		superior = meio
	else:
		inferior = meio

while (abs(y_meio) > criterio_parada): # Procura pela raiz
	meio = (inferior + superior) / 2

	y_inferior = funcao(inferior)
	y_meio = funcao(meio)
	y_superior = funcao(superior)

	# print(f"Inferior: ({inferior}, {y_inferior})\tMeio: ({meio}, {y_meio})\tSuperior: ({superior}, {y_superior})")

	# Houve mudança de sinal entre o inicio e o meio
	if ((y_inferior * y_meio) < 0):
		superior = meio
	# Houve mudança de sinal entre o meio e o fim
	else:
		inferior = meio
	
raizes[0].append(meio)
raizes[1].append(y_meio)

print(f"{len(raizes[0])} pontos achados:")
print(raizes)

plt.plot(raizes[0], raizes[1], color='blue', marker='o') # Pontos das Raízes
plt.plot((-1, 3), (0, 0), color='black') # Reta do eixo X
plt.plot((0, 0), (-5, 20), color='black') # Reta do eixo Y
# plt.plot(valores, pontos, color='red') # Função original

plt.title("Função original f(x) e sua(s) raiz(es)")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()