# Bibliotecas utilizadas

import matplotlib.pyplot as plt
import numpy as np

# Espaço para armazenar os valores iniciais do problema

# f(x) = e^(x) - 4 + (7/2 * cos(2x))
def funcao(x):
	return np.pow(np.e, x) - 4 + (3.5 * np.cos(2 * x))

# Equação da reta é uma hipotenusa entre 2 pontos
def falsa_posicao(inferior, superior):
	return superior - ((funcao(superior) * (inferior - superior)) / (funcao(inferior) - funcao(superior)))

criterio_parada = 0.1

raizes = [[], []]

inferior = 0.0
superior = 3.0
meio = falsa_posicao(inferior, superior)

y_inferior = funcao(inferior)
y_meio = funcao(meio)
y_superior = funcao(superior)

retas = []

# O método da falsa posição é um método intervalar.
# Ela determina a próxima posição não através da divisão ao meio,
# mas ligando as extremidades com uma linha reta e determinando a localização onde a linha reta intercepta o eixo x.
# O valor de xr (raíz estimada), substitui qualquer uma das duas estimativas iniciais
# e produz um valor de funçao com o mesmo sinal que f(xr).


while (inferior > meio and inferior < superior):
	print(f"Intervalo: [{inferior}, {superior}]: ({inferior}, {y_inferior}) e ({superior}, {y_superior})")
	print(f"Falsa Posicao: ({falsa_posicao(inferior, superior)}, {funcao(falsa_posicao(inferior, superior))})")
	inferior = (inferior + superior) / 2 # Procura próximo valor com reta atravessando o eixo x
	meio = falsa_posicao(inferior, superior)
	retas = [(meio, superior), (funcao(meio), funcao(superior))] # Última reta encontrada para plotar no grafico

while (abs(y_meio) > criterio_parada): # Procura pela raiz
	meio = falsa_posicao(inferior, superior)

	y_inferior = funcao(inferior)
	y_meio = funcao(meio)
	y_superior = funcao(superior)

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
plt.plot(tuple(retas[0]), tuple(retas[1]), color='green') # Reta do eixo Y
# plt.plot(valores, pontos, color='red') # Função original

plt.title("Função original f(x) e sua(s) raiz(es)")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()