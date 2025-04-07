import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
from shapely.geometry import LineString, box

def gerar_obstaculos(num_obstaculos, tamanho, limite):
    obstaculos = []
    while len(obstaculos) < num_obstaculos:
        x = random.randint(0, limite - tamanho)
        y = random.randint(0, limite - tamanho)
        novo_obstaculo = (x, y, x + tamanho, y + tamanho)
        if all(abs(x - ox) > tamanho or abs(y - oy) > tamanho for ox, oy, _, _ in obstaculos):
            obstaculos.append(novo_obstaculo)
    return obstaculos

def criar_grafo(limite, obstaculos):
    G = nx.Graph()
    obstaculos_poligonos = [box(x1, y1, x2, y2) for (x1, y1, x2, y2) in obstaculos]

    for x in range(limite):
        for y in range(limite):
            G.add_node((x, y))

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1),  # cima, baixo, esquerda, direita
                (-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonais

    for x in range(limite):
        for y in range(limite):
            for dx, dy in direcoes:
                nx_, ny_ = x + dx, y + dy
                if 0 <= nx_ < limite and 0 <= ny_ < limite:
                    linha = LineString([(x, y), (nx_, ny_)])
                    if all(not linha.crosses(obs) and not linha.within(obs) for obs in obstaculos_poligonos):
                        G.add_edge((x, y), (nx_, ny_))

    # Remove nós que estão dentro dos obstáculos
    for (x1, y1, x2, y2) in obstaculos:
        for x in range(x1, x2):
            for y in range(y1, y2):
                if (x, y) in G:
                    G.remove_node((x, y))

    return G

def encontrar_caminho(G, inicio, fim):
    try:
        caminho = nx.astar_path(G, inicio, fim)
        return caminho
    except nx.NetworkXNoPath:
        return None

def plotar(limite, obstaculos, caminho, inicio, fim):
    plt.figure(figsize=(8, 8))
    plt.xlim(0, limite)
    plt.ylim(0, limite)
    for (x1, y1, x2, y2) in obstaculos:
        plt.fill([x1, x2, x2, x1], [y1, y1, y2, y2], 'gray')
    if caminho:
        x, y = zip(*caminho)
        plt.plot(x, y, marker='o', color='b', linestyle='-')
    plt.scatter(*inicio, color='green', s=100, label='Início')
    plt.scatter(*fim, color='red', s=100, label='Fim')
    plt.legend()
    plt.grid()
    plt.show()

# Parâmetros
limite = 20
tamanho_obstaculo = 2
num_obstaculos = 10
inicio = (0, 0)
fim = (limite-1, limite-1)

# Execução
obstaculos = gerar_obstaculos(num_obstaculos, tamanho_obstaculo, limite)
G = criar_grafo(limite, obstaculos)
caminho = encontrar_caminho(G, inicio, fim)
plotar(limite, obstaculos, caminho, inicio, fim)
