
class Grafo:

    def __init__(self, representacao, direcionado, ponderado):
        self.representacao = representacao
        self.direcionado = direcionado
        self.ponderado = ponderado
        # constroi lista de vertices
        self.lista_vertices = []
        # cria estrutura de representacao
        if self.representacao == 'matriz':
            # construo a matriz
            pass
        else: # lista
            # construo a lista de adjacencias
            # chave = vertice
            # valor = lista de vizinhos e os pesos
            self.dict_vizinhos = {}
    def adiciona_vertice(self, vertice):
        if vertice not in self.lista_vertices:
            self.lista_vertices.append(vertice)
            # se estou usando representacao de lista e
            # o vertice é novo, criamos uma lista vazia
            # de vizinhos para ele
            if self.representacao != 'matriz':
                self.dict_vizinhos[vertice] = []

    def cria_aresta(self, vertice_a, vertice_b, peso=1):
        # verifico se os vertices existem
        if vertice_a in self.lista_vertices and \
                vertice_b in self.lista_vertices:
            if self.representacao == 'matriz':
                pass
                # implementar depois
            else: #lista
                self.dict_vizinhos[vertice_a].\
                    append((vertice_b, peso))
                if not self.direcionado:
                    # cria conexao no sentido oposto tb
                    self.dict_vizinhos[vertice_b].\
                        append((vertice_a, peso))

    def remove_vertice(self, vertice_a):
        pass

    def remove_aresta(self, vertice_a, vertice_b):
        pass

    def atualiza_peso(self, vertice_a, vertice_b, peso):
        pass

    def existe_aresta(self, vertice_a, vertice_b):
        # verifico se os dois vertices existem
        if vertice_a in self.lista_vertices and \
                vertice_b in self.lista_vertices:
            # pego a lista de todos os vizinhos de A
            for t in self.dict_vizinhos[vertice_a]:
                # se eu encontrar o B, é vizinho :)
                if t[0] == vertice_b:
                    return True
        return False

    def indegree(self, vertice):
        pass

    def outdegree(self, vertice):
        pass

    def degree(self, vertice):
        pass

    def warshall(self):
        pass

    def dijkstra(self, vertice_a, vertice_b):  # vertice saida e vertice chegada
        pi = {}

        custos_acumulados = {}

        for vertice in self.lista_vertices:
            custos_acumulados[vertice] = +1e10
            pi[vertice] = None
        
        custos_acumulados[vertice_a] = 0

        q = []
        for vertice in self.lista_vertices:
            q.append(vertice)

        while len(q) > 0:
            no_atual = self.extract_min(q, custos_acumulados)

            if no_atual is None:
                break
            q.remove(no_atual)
            
            for vizinho in self.pega_vizinho(no_atual):
                novo_custo = custos_acumulados[no_atual] + self.pega_peso(no_atual, vizinho)

                if novo_custo < custos_acumulados[vizinho]:
                    custos_acumulados[vizinho] = novo_custo
                    pi[vizinho] = no_atual

        caminho = []
        custo_total = 1e10

        if pi[vertice_b] != None:
            custo_total = custos_acumulados[vertice_b]

            no_atual = vertice_b
            while no_atual != None:
                caminho.insert(0, no_atual)
                no_atual = pi[no_atual]

        return caminho, custo_total


    def extract_min(self, q, pesos_acumulados):
        vertice_menor_custo = None
        min_weight = +1e10

        for vertice in q:
            if pesos_acumulados[vertice] < min_weight:
                vertice_menor_custo = vertice
                min_weight = pesos_acumulados[vertice]

        return vertice_menor_custo


    def pega_vizinho(self, vertice):
        vizinhos = []
        for (vizinho, peso) in self.dict_vizinhos[vertice]:
            vizinhos.append(vizinho)

        return vizinhos
    
    def pega_peso(self, vertice_a, vertice_b):
        peso_encontrado = +1e10
        if vertice_a in self.lista_vertices and \
                vertice_b in self.lista_vertices:
            for (vizinho, peso) in self.dict_vizinhos[vertice_a]:
                if vizinho == vertice_b:
                    peso_encontrado = peso
                    break

        return peso_encontrado
    
    def busca_profundidade(self, vertice_inicial, vertice_final):
        stack = []
        visitados = []
        stack.append(vertice_inicial)

        while len(stack) > 0:
            vertice_atual = stack.pop(-1)
            if vertice_atual not in visitados:
                visitados.append(vertice_atual)
            for vizinho in sorted(self.pega_vizinho(vertice_inicial)):
                if vizinho not in visitados:
                    stack.append(vizinho)

                if vertice_atual == vertice_final:
                    break

        return visitados
    
    def busca_largura(self, vertice_inicial, vertice_final):
        queue = []
        visitados = []
        queue.append(vertice_inicial)

        while len(queue) > 0:
            vertice_atual = queue.pop(0)
            if vertice_atual not in visitados:
                visitados.append(vertice_atual)
            for vizinho in sorted(self.pega_vizinho(vertice_inicial)):
                
                if vizinho not in visitados:
                    queue.append(vizinho)

                if vertice_atual == vertice_final:
                    break

        return visitados

    def __str__(self):
        ret =  f'Vértices: {self.lista_vertices}\n'
        ret += 'Arestas:\n'
        for vertice in self.dict_vizinhos.keys():
            ret += f'{vertice} \t {self.dict_vizinhos[vertice]}\n'
        return ret
    
    def eh_conectado(self):
        return True


    def prim(self):

        if self.eh_conectado():

            predessessores = {}
            pesos = {}

            for vertice in self.lista_vertices:
                predessessores[vertice] = None
                pesos[vertice] = +1e10

            q = [x for x in self.lista_vertices]

            while len(q) > 0:
                no_atual = self.extract_min(q, pesos)

                q.remove(no_atual)

                for vizinho in self.pega_vizinho(no_atual):
                    peso = self.pega_peso(no_atual, vizinho)

                    if vizinho in q and peso < pesos[vizinho]:
                        predessessores[vizinho] = no_atual
                        pesos[vizinho] = peso

            g_prim = Grafo(self.representacao,
                           direcionado=False,
                           ponderado=True)
            
            for vertice in self.lista_vertices:
                g_prim.adiciona_vertice(vertice)

            custo_acumolado = 0

            for vertice_inicio in predessessores.keys():
                vertice_fim = predessessores[vertice_inicio]
                if vertice_fim is not None:
                    g_prim.cria_aresta(vertice_inicio, vertice_fim, pesos[vertice_inicio])
                    custo_acumolado += pesos[vertice_inicio]
            return g_prim
            




if __name__ == '__main__':
    g = Grafo('lista',
              direcionado=False,
              ponderado=True)
    g.adiciona_vertice('A')
    g.adiciona_vertice('B')
    g.adiciona_vertice('E')
    g.adiciona_vertice('D')
    g.adiciona_vertice('C')
    g.cria_aresta('A', 'B', peso=15)
    g.cria_aresta('A', 'C', peso=4)
    g.cria_aresta('B', 'C', peso=2)
    g.cria_aresta('C', 'D', peso=1)
    g.cria_aresta('D', 'E', peso=2)
    g.cria_aresta('C', 'E', peso=8)
    print(g)


    print(g.busca_largura('A', 'E'))
    print(g.busca_profundidade('A', 'E'))
    # caminho, custo = g.dijkstra('A', 'E')
    # print(f'{caminho}, {custo}')
    g.prim()


