class Grafo:

    def __init__(self, representacao, direcionado, ponderado):
        self.representacao = representacao
        self.direcionado = direcionado
        self.ponderado = ponderado
        # constroi lista de vertices e arestas
        self.vertices = []

        # Cria estrututura de representacao
        if self.representacao == "matriz":
            #construa a matriz
            pass
        else:
            #construa a lista de adjacencia
            # chave = Vertice
            # valor = Lista de vertices vizinhos e os pesos
            self.vizinhos = {}
    


    def adiciona_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            # se estou usando a representacao de lista e o vertice é novo, crio uma lista vazia para os vizinhos
            if self.representacao != "matriz":
                self.vizinhos[vertice] = []
    
    def __str__(self):
        arestas = "Arestas:\n"
        for vertice in self.vizinhos.keys():
            arestas += f"{vertice} \t {self.vizinhos[vertice]}\n"
        return f"Vertices: {self.vertices}\n{arestas}"

    def cria_aresta(self, v_a, v_b, peso=1):
        # verifica se os vertices existem
        if v_a in self.vertices and v_b in self.vertices:
            if self.representacao == 'matriz':
                pass
            else:
                self.vizinhos[v_a].append((v_b, peso))
                if not self.direcionado:
                    # cria conexao no outro sentido
                    self.vizinhos[v_b].append((v_a, peso))

    def atualiza_peso(self, v_a, v_b, novo_peso):
        pass
    
    def existe_aresta(self, v_a, v_b):
        if v_a in self.vertices and v_b in self.vertices:
            # pego a lista de todos os vizinhos de A
            for t in self.vizinhos[v_a]:
                # se eu encontrar o B, é vizinho :)
                if t[0] == v_b:
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

    def dijkstra(self, v_a, v_b):
        pass
    
if __name__ == '__main__':
    g = Grafo("lista", False, False)
    g.adiciona_vertice("A")
    g.adiciona_vertice("B")
    g.cria_aresta('A', 'B')
    print(g)