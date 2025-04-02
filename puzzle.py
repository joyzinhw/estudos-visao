import heapq
from collections import deque

class QuebraCabeca:
    def __init__(self, estado, pai=None, movimento="", custo=0):
        self.estado = estado  
        self.pai = pai 
        self.movimento = movimento  
        self.custo = custo 
        self.posicao_vazia = self.estado.index(0)  

    def __lt__(self, outro):
        return self.custo < outro.custo

    def gerar_vizinhos(self):
        vizinhos = []
        movimentos = [("Cima", -3), ("Baixo", 3), ("Esquerda", -1), ("Direita", 1)]
        
        for movimento, deslocamento in movimentos:
            nova_posicao = self.posicao_vazia + deslocamento
            if self.movimento_valido(movimento, nova_posicao):
                novo_estado = self.estado[:]
                novo_estado[self.posicao_vazia], novo_estado[nova_posicao] = novo_estado[nova_posicao], novo_estado[self.posicao_vazia]
                vizinhos.append(QuebraCabeca(novo_estado, self, movimento, self.custo + 1))
        
        return vizinhos

    def movimento_valido(self, movimento, nova_posicao):
        if movimento == "Esquerda" and self.posicao_vazia % 3 == 0:
            return False
        if movimento == "Direita" and self.posicao_vazia % 3 == 2:
            return False
        if nova_posicao < 0 or nova_posicao >= 9:
            return False
        return True

    def estado_final(self):
        return self.estado == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def caminho(self):
        no, caminho = self, []
        while no:
            caminho.append(no.movimento)
            no = no.pai
        return caminho[::-1][1:]  


def heuristica(estado):
    objetivo = {val: (i // 3, i % 3) for i, val in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 0])}
    distancia = 0
    for i, val in enumerate(estado):
        if val != 0:
            x, y = i // 3, i % 3
            objetivo_x, objetivo_y = objetivo[val]
            distancia += abs(x - objetivo_x) + abs(y - objetivo_y)
    return distancia

# Busca Não Informada (BFS)
def busca_largura(estado_inicial):
    fila = deque([QuebraCabeca(estado_inicial)])
    visitados = set()
    esforco = 0

    while fila:
        no = fila.popleft()
        esforco += 1
        if no.estado_final():
            return no.caminho(), esforco
        
        visitados.add(tuple(no.estado))

        for vizinho in no.gerar_vizinhos():
            if tuple(vizinho.estado) not in visitados:
                fila.append(vizinho)
    
    return None, esforco

# Busca Informada (A* com heurística de Manhattan)
def busca_a_estrela(estado_inicial):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (heuristica(estado_inicial), QuebraCabeca(estado_inicial)))
    visitados = set()
    esforco = 0

    while fila_prioridade:
        _, no = heapq.heappop(fila_prioridade)
        esforco += 1
        if no.estado_final():
            return no.caminho(), esforco
        
        visitados.add(tuple(no.estado))

        for vizinho in no.gerar_vizinhos():
            if tuple(vizinho.estado) not in visitados:
                heapq.heappush(fila_prioridade, (vizinho.custo + heuristica(vizinho.estado), vizinho))
    
    return None, esforco


estado_inicial = [1, 2, 3, 4, 0, 5, 6, 7, 8]  

solucao_bfs, esforco_bfs = busca_largura(estado_inicial)
solucao_aestrela, esforco_aestrela = busca_a_estrela(estado_inicial)

print("Solução BFS:", solucao_bfs)
print("Esforço BFS:", esforco_bfs)
print("Solução A*:", solucao_aestrela)
print("Esforço A*:", esforco_aestrela)
