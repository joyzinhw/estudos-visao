import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random

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
    G = nx.grid_2d_graph(limite, limite)
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

def plotar(limite, obstaculos, caminho):
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

limite = 20
tamanho_obstaculo = 3
num_obstaculos = 50
inicio = (0, 0)
fim = (limite-1, limite-1)

obstaculos = gerar_obstaculos(num_obstaculos, tamanho_obstaculo, limite)
G = criar_grafo(limite, obstaculos)
caminho = encontrar_caminho(G, inicio, fim)
plotar(limite, obstaculos, caminho)
