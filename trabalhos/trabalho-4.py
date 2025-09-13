"""
# Trabalho 4

- Aluno: Pedro Henrique Rabis Diniz

Crie um programa no python para encontrar raízes pelo método de iteração de ponto fixo simples da função $f(x) = e^{-x} - x$ com aproximação inicial 2

Envie o arquivo do programa em formato *.py* para o e-mail josericardo@iftm.edu.br até a data prevista no Plano de Ensino.
"""

# Bibliotecas utilizadas

import matplotlib.pyplot as plt
import numpy as np

# Espaço para armazenar os valores iniciais do problema

# f(x) = e^{-x} - x
def funcao(x):
	return np.pow(np.e, -x) - x

# Isolando -x, temos a funcao iteração e^{-x}
def funcao_iteracao(x):
	return np.pow(np.e, -x)

def derivada_funcao_iteracao(x):
	return -1 * np.pow(np.e, -x)

aproximacao_inicial = 2
criterio_parada = 0.00001
intervalo_confianca = 0.000001

raizes = [[], []]

contador_maximo = 200

# Primeira iteracao
atual = funcao_iteracao(aproximacao_inicial)
auxiliar = atual
derivada = derivada_funcao_iteracao(aproximacao_inicial)

# Utiliza-se o critério de parada e o contador máximo como mecanismos de se obter
# um resultado satisfatório para parar de procurar a raiz

while(auxiliar > criterio_parada and contador_maximo > 0):
	atual = funcao_iteracao(atual)

	# Encontrado divergencia na função
	if (derivada > 1 or derivada < -1):
		print("Divergente")
		break

	# Encontrado intervalo de confianca para convergencia
	if (np.abs(atual - auxiliar) < intervalo_confianca):
		raizes[0].append(atual)
		raizes[1].append(funcao(atual))
		break

	auxiliar = atual
	derivada = derivada_funcao_iteracao(auxiliar)

	contador_maximo -= 1


print(f"{len(raizes[0])} pontos achados:")
print(raizes)

plt.plot(raizes[0], raizes[1], color='blue', marker='o') # Pontos das Raízes
plt.plot((-1, 3), (0, 0), color='black') # Reta do eixo X
plt.plot((0, 0), (-5, 20), color='black') # Reta do eixo Y
# plt.plot(tuple(retas[0]), tuple(retas[1]), color='green') # Reta do eixo Y
# plt.plot(valores, pontos, color='red') # Função original

plt.title("Função original f(x) e sua(s) raiz(es)")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()
