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

# def criar_grafo_visibilidade(inicio, fim, obstaculos):
#     from shapely.geometry import Point

#     G = nx.Graph()
#     obstaculos_poligonos = [box(x1, y1, x2, y2) for (x1, y1, x2, y2) in obstaculos]

#     # Coletar os vértices dos obstáculos
#     vertices = set()
#     for (x1, y1, x2, y2) in obstaculos:
#         vertices.update([
#             (x1, y1), (x1, y2), (x2, y1), (x2, y2)
#         ])

#     # Adicionar início e fim
#     vertices.add(inicio)
#     vertices.add(fim)

#     # Adicionar vértices ao grafo
#     for v in vertices:
#         G.add_node(v)

#     # Verificar todos os pares de vértices e adicionar aresta se possível
#     lista_vertices = list(vertices)
#     for i in range(len(lista_vertices)):
#         for j in range(i + 1, len(lista_vertices)):
#             v1, v2 = lista_vertices[i], lista_vertices[j]
#             linha = LineString([v1, v2])
#             if all(not linha.crosses(obs) and not linha.within(obs) for obs in obstaculos_poligonos):
#                 G.add_edge(v1, v2)

#     return G

# def encontrar_caminho(G, inicio, fim):
#     try:
#         caminho = nx.astar_path(G, inicio, fim)
#         return caminho
#     except nx.NetworkXNoPath:
#         return None

# def plotar(limite, obstaculos, G, caminho, inicio, fim):
#     plt.figure(figsize=(8, 8))
#     plt.xlim(0, limite)
#     plt.ylim(0, limite)

#     # Obstáculos
#     for (x1, y1, x2, y2) in obstaculos:
#         plt.fill([x1, x2, x2, x1], [y1, y1, y2, y2], 'gray')

#     # Arestas do grafo
#     for (u, v) in G.edges():
#         x = [u[0], v[0]]
#         y = [u[1], v[1]]
#         plt.plot(x, y, color='lightblue', linestyle='--', linewidth=0.7)

#     # Caminho final
#     if caminho:
#         x, y = zip(*caminho)
#         plt.plot(x, y, marker='o', color='blue', linestyle='-', linewidth=2)

#     # Pontos de início e fim
#     plt.scatter(*inicio, color='green', s=100, label='Início')
#     plt.scatter(*fim, color='red', s=100, label='Fim')

#     plt.legend()
#     plt.grid()
#     plt.title("Grafo de Visibilidade com Obstáculos")
#     plt.show()

# # Parâmetros
# limite = 20
# tamanho_obstaculo = 2
# num_obstaculos = 10
# inicio = (0, 0)
# fim = (19, 19)

# # Execução
# obstaculos = gerar_obstaculos(num_obstaculos, tamanho_obstaculo, limite)
# G = criar_grafo_visibilidade(inicio, fim, obstaculos)
# caminho = encontrar_caminho(G, inicio, fim)
# plotar(limite, obstaculos, G, caminho, inicio, fim)


##### teste baseado no outro
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

def criar_grafo_de_visibilidade(pontos, obstaculos):
    G = nx.Graph()
    obstaculos_poligonos = [box(x1, y1, x2, y2) for (x1, y1, x2, y2) in obstaculos]

    for i in range(len(pontos)):
        for j in range(i + 1, len(pontos)):
            p1, p2 = pontos[i], pontos[j]
            linha = LineString([p1, p2])
            # olha se cruza ou está dentro de algum obstáculo
            if all(not linha.crosses(obs) and not linha.within(obs) for obs in obstaculos_poligonos):
                G.add_edge(p1, p2)

    return G


# desenha 
def plotar_grafo(pontos, obstaculos, G):
    plt.figure(figsize=(8, 8))
    

    for (x1, y1, x2, y2) in obstaculos:
        plt.fill([x1, x2, x2, x1], [y1, y1, y2, y2], 'gray')
    

    for u, v in G.edges:
        x_vals, y_vals = zip(u, v)
        plt.plot(x_vals, y_vals, 'lightblue', linestyle='--', linewidth=0.8)


    x, y = zip(*pontos)
    plt.scatter(x, y, color='black', s=10)

    plt.xlim(0, limite)
    plt.ylim(0, limite)
    plt.title("Grafo de Visibilidade com Obstáculos (Apenas Vértices dos Obstáculos)")
    plt.grid(True)
    plt.show()

limite = 20
tamanho_obstaculo = 2
num_obstaculos = 10


obstaculos = gerar_obstaculos(num_obstaculos, tamanho_obstaculo, limite)


pontos = []
for (x1, y1, x2, y2) in obstaculos:
    pontos.extend([(x1, y1), (x1, y2), (x2, y1), (x2, y2)])

G = criar_grafo_de_visibilidade(pontos, obstaculos)
plotar_grafo(pontos, obstaculos, G)
