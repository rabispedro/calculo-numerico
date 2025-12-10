# Bibliotecas utilizadas

import matplotlib.pyplot as plt
import numpy as np

# Espaço para armazenar os valores iniciais do problema

aproximacao_inicial = -8
criterio_parada = 0.00001
intervalo_confianca = 0.0001
fator_pertubacao = 0.000001

# f(x) = x^{5} /{3} - x^{4} + x + 1
def funcao(x):
	return (np.pow(x, 5) / 3) - np.pow(x, 4) + x + 1

# Derivada aproximada
def derivada_funcao(x):
	# return x - ((fator_pertubacao * funcao(x)) / (funcao(x + fator_pertubacao) - funcao(x)))
	return (np.pow(x, 4) * 5 / 3) - (4 * np.pow(x, 3)) + 1

raizes = [[], []]

contador_maximo = 200

# Primeira iteracao
atual = funcao(aproximacao_inicial)
auxiliar = atual
derivada = derivada_funcao(atual)


# Utiliza-se o critério de parada e o contador máximo como mecanismos de se obter
# um resultado satisfatório para parar de procurar a raiz

while(contador_maximo > 0):
	atual = funcao(atual)

	print(f"Atual: ({atual:6f})\tAuxiliar: ({auxiliar:6f})\tDerivada: ({derivada:6f})")

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
	derivada = derivada_funcao(auxiliar)

	contador_maximo -= 1


print(f"{len(raizes[0])} pontos achados:")
print(raizes)

plt.plot(raizes[0], raizes[1], color='blue', marker='o') # Pontos das Raízes
plt.plot((-1, 3), (0, 0), color='black') # Reta do eixo X
plt.plot((0, 0), (-5, 20), color='black') # Reta do eixo Y

plt.title("Função original f(x) e sua(s) raiz(es)")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()