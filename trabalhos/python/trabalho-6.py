"""
# Trabalho 6

- Aluno: Pedro Henrique Rabis Diniz

Crie um programa que utiliza a razão áurea para maximizar a função

$$
f(x) = -3 \cdot x^6 + 3 \cdot x^4 - 2 \cdot x + 5
$$

Considerando o intervalo de busca inicial de $[-3; 2]$. Estabeleça como critério de parada a precisão de $10^{-8}$ para o erro estimado.

O arquivo em formato *.py* do progama deverá ser enviado para o e-mail josericardo@iftm.edu.br até a data prevista no Plano de Ensino com todos os parâmetros do algoritmo devidamente estabelecidos.
"""

# Bibliotecas utilizadas

import matplotlib.pyplot as plt
import numpy as np

# Espaço para armazenar os valores iniciais do problema

inicio = -3
fim = 2
criterio_parada = 1e-8

x_inicio, x_fim, y_inicio, y_fim = (0, 0, 0, 0)

# f(x) = -3x^6 + 3x^4 -2x +5
def funcao(x):
    return -3 * np.pow(x, 6) + 3 * np.pow(x, 4) - (2 * x) + 5

razao_aurea = (1 + np.sqrt(5)) / 2
diferencial = (razao_aurea - 1) * (fim - inicio)
x_opt = 1
erro = (2 - razao_aurea) * np.abs((fim - inicio) / x_opt) * 100

pontos_criticos = [[], []]

print(f"Razão Aurea: {razao_aurea:6f}\tDiferencial: {diferencial:6f}")

# Utiliza-se o critério de parada e o contador máximo como mecanismos de se obter
# um resultado satisfatório para parar de procurar os pontos críticos
while(inicio <= fim):
    print(f"Inicio: ({x_inicio:6f}, {y_inicio:6f})\tFim:({x_fim:6f}, {y_fim:6f})")

    x_inicio = inicio + diferencial
    x_fim = fim - diferencial

    diferencial = (razao_aurea - 1) * (fim - inicio)

    y_inicio = funcao(x_inicio)
    y_fim = funcao(x_fim)

    # Achou y_inicio mínimo
    if (y_inicio < y_fim):
        fim = x_inicio
    # Achou y_fim mínimo
    elif (y_fim < y_inicio):
        inicio = x_fim
    else:
        print(f"Pontos iguais")
        break

pontos_criticos[0].append(x_inicio)
pontos_criticos[1].append(y_inicio)

print(f"{len(pontos_criticos[0])} pontos achados:")
print(pontos_criticos)

plt.plot(pontos_criticos[0], pontos_criticos[1], color='blue', marker='o') # Pontos das Raízes
plt.plot((-3, 2), (0, 0), color='black') # Reta do eixo X
plt.plot((0, 0), (-2, 8), color='black') # Reta do eixo Y

plt.title("Função original f(x) e seu(s) ponto(s) crítico(s)")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()
