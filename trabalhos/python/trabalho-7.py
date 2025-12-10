"""
# Trabalho 7

- Aluno: Pedro Henrique Rabis Diniz

Crie um programa que utiliza a interpolação quadrática para maximizar a função

$$
f(x) = -3 \cdot x^6 + 3 \cdot x^4 - 2 \cdot x + 5
$$

considerando os pontos de busca iniciais $-2$, $0$ e $1.5$. Estabeleça como critério de parada a precisão de $10^{-8}$ para o erro estimado

O arquivo em formato *.py* do progama deverá ser enviado para o e-mail josericardo@iftm.edu.br até a data prevista no Plano de Ensino com todos os parâmetros do algoritmo devidamente estabelecidos.
"""

# Bibliotecas utilizadas

import matplotlib.pyplot as plt
import numpy as np

# Espaço para armazenar os valores iniciais do problema

inicio = -3
fim = 2
criterio_parada = 1e-8

x_1, x_2, x_3, x_4, x_ant = (-2, 0, 1.5, 0, 0)
y_1, y_2, y_3, y_4, y_ant = (0, 0, 0, 0, 0)

# f(x) = -3x^6 + 3x^4 -2x +5
def funcao(x):
    return -3 * np.pow(x, 6) + 3 * np.pow(x, 4) - (2 * x) + 5

erro = 1

pontos_criticos = [[], []]

# Utiliza-se o critério de parada como mecanismos de se obter
# um resultado satisfatório para parar de procurar os pontos críticos
while(erro > criterio_parada):
    y_1 = funcao(x_1)
    y_2 = funcao(x_2)
    y_3 = funcao(x_3)

    numerador = (np.pow(x_2 - x_1, 2) * (y_2 - y_3) - np.pow((x_2 - x_3), 2) * (y_2 - y_1))
    denominador = (2 * (x_2 - x_1) * (y_2 - y_3) - (x_2 - x_3) * (y_2 - y_1))

    x_4 = x_2 - (numerador / denominador)
    y_4 = funcao(x_4)
    erro = (np.abs(x_4 - x_ant) / np.abs(x_4))

    if (y_4 > y_2):
        x_1 = x_2
    else:
        x_3 = x_2

    x_ant = x_4
    x_2 = x_4

pontos_criticos[0].append(x_4)
pontos_criticos[1].append(y_4)

print(f"{len(pontos_criticos[0])} pontos achados:")
print(pontos_criticos)

plt.plot(pontos_criticos[0], pontos_criticos[1], color='blue', marker='o') # Pontos das Raízes
plt.plot((-3, 2), (0, 0), color='black') # Reta do eixo X
plt.plot((0, 0), (-2, 8), color='black') # Reta do eixo Y

plt.title("Função original f(x) e seu(s) ponto(s) crítico(s)")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()
