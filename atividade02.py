##### sem o inicio

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

def criar_grafo_visibilidade(inicio, obstaculos):
    G = nx.Graph()
    obstaculos_poligonos = [box(x1, y1, x2, y2) for (x1, y1, x2, y2) in obstaculos]


    vertices = set()
    for (x1, y1, x2, y2) in obstaculos:
        vertices.update([
            (x1, y1), (x1, y2), (x2, y1), (x2, y2)
        ])


    vertices.add(inicio)


    for v in vertices:
        G.add_node(v)


    lista_vertices = list(vertices)
    for i in range(len(lista_vertices)):
        for j in range(i + 1, len(lista_vertices)):
            v1, v2 = lista_vertices[i], lista_vertices[j]
            linha = LineString([v1, v2])
            if all(not linha.crosses(obs) and not linha.within(obs) for obs in obstaculos_poligonos):
                G.add_edge(v1, v2)

    return G

def plotar(limite, obstaculos, G, inicio):
    plt.figure(figsize=(8, 8))
    plt.xlim(0, limite)
    plt.ylim(0, limite)


    for (x1, y1, x2, y2) in obstaculos:
        plt.fill([x1, x2, x2, x1], [y1, y1, y2, y2], 'gray')


    for (u, v) in G.edges():
        x = [u[0], v[0]]
        y = [u[1], v[1]]
        plt.plot(x, y, color='lightblue', linestyle='--', linewidth=0.7)


    plt.scatter(*inicio, color='green', s=100, label='Início')

    plt.legend()
    plt.grid()
    plt.title("Grafo de Visibilidade com Obstáculos")
    plt.show()


limite = 20
tamanho_obstaculo = 2
num_obstaculos = 10
inicio = (0, 0)


obstaculos = gerar_obstaculos(num_obstaculos, tamanho_obstaculo, limite)
G = criar_grafo_visibilidade(inicio, obstaculos)
plotar(limite, obstaculos, G, inicio)




##### sem o inicio
# import numpy as np
# import matplotlib.pyplot as plt
# import networkx as nx
# import random
# from shapely.geometry import LineString, box

# def gerar_obstaculos(num_obstaculos, tamanho, limite):
#     obstaculos = []
#     while len(obstaculos) < num_obstaculos:
#         x = random.randint(0, limite - tamanho)
#         y = random.randint(0, limite - tamanho)
#         novo_obstaculo = (x, y, x + tamanho, y + tamanho)
#         if all(abs(x - ox) > tamanho or abs(y - oy) > tamanho for ox, oy, _, _ in obstaculos):
#             obstaculos.append(novo_obstaculo)
#     return obstaculos

# def criar_grafo_de_visibilidade(pontos, obstaculos):
#     G = nx.Graph()
#     obstaculos_poligonos = [box(x1, y1, x2, y2) for (x1, y1, x2, y2) in obstaculos]

#     for i in range(len(pontos)):
#         for j in range(i + 1, len(pontos)):
#             p1, p2 = pontos[i], pontos[j]
#             linha = LineString([p1, p2])
#             # olha se cruza ou está dentro de algum obstáculo
#             if all(not linha.crosses(obs) and not linha.within(obs) for obs in obstaculos_poligonos):
#                 G.add_edge(p1, p2)

#     return G


# # desenha 
# def plotar_grafo(pontos, obstaculos, G):
#     plt.figure(figsize=(8, 8))
    

#     for (x1, y1, x2, y2) in obstaculos:
#         plt.fill([x1, x2, x2, x1], [y1, y1, y2, y2], 'gray')
    

#     for u, v in G.edges:
#         x_vals, y_vals = zip(u, v)
#         plt.plot(x_vals, y_vals, 'lightblue', linestyle='--', linewidth=0.8)


#     x, y = zip(*pontos)
#     plt.scatter(x, y, color='black', s=10)

#     plt.xlim(0, limite)
#     plt.ylim(0, limite)
#     plt.title("Grafo de Visibilidade com Obstáculos (Apenas Vértices dos Obstáculos)")
#     plt.grid(True)
#     plt.show()

# limite = 20
# tamanho_obstaculo = 2
# num_obstaculos = 10


# obstaculos = gerar_obstaculos(num_obstaculos, tamanho_obstaculo, limite)


# pontos = []
# for (x1, y1, x2, y2) in obstaculos:
#     pontos.extend([(x1, y1), (x1, y2), (x2, y1), (x2, y2)])

# G = criar_grafo_de_visibilidade(pontos, obstaculos)
# plotar_grafo(pontos, obstaculos, G)
