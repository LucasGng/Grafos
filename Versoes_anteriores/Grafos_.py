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
        # criar lista de predecessores
        pi = {}
        # criar lista de custos
        custos_acumulados = {}
        for vertice in self.vertices:
            custos_acumulados[vertice] = +1e10
            pi[vertice] = None

        custos_acumulados[v_a] = 0
            

        prioridades = []
        for vertice in self.vertices:
            prioridades.append(vertice)

        while len(prioridades) > 0:
            no_atual = self.extract_min(prioridades, custos_acumulados)
            if no_atual is None:
                break
            prioridades.remove(no_atual)

            # laço para verificar vizinhos
            for vizinho in self.pega_vizinhos(no_atual):
                custo = custos_acumulados[no_atual] + self.pega_peso(no_atual, vizinho)
                # se o novo custo for menor que o custo que já encontramos antes, substituimos
                if custo < custos_acumulados[vizinho]:
                    # substituindo o custo para chegar no vizinho
                    custos_acumulados[vizinho] = custo
                    # criando link entre o vizinho e o no_atual
                    pi[vizinho] = no_atual
            # Com o laço finalizado, a busca acabou e nesse momento precisamos criar o caminho entre o no_inicial e o no_final
        caminho = []
        custo_total = 1e10
        # encontrei um caminho? basicamente eu preciso verificar se o no_final tem um predecessor
        if pi[v_b] != None:
            custo_total = custos_acumulados[v_b]
            # montando o caminho ao retornar na estrutura de predecessores
            no_atual = v_b
            while no_atual != None:
                caminho.insert(0,no_atual)
                no_atual = pi[no_atual]
        return (caminho, custo_total)
    
    # Função que recebe a lista de prioridades e a lista de custos acumulados
    # o objetivo da função é retornar o vertice com menor custo acumulado até o momento
    def extract_min(self, prioridades, custos_acumulados):
        v_menor_custo = None
        min_weight = +1e10
        for vertice in prioridades:
            if custos_acumulados[vertice] <= min_weight:
                min_weight = custos_acumulados[vertice]
                v_menor_custo = vertice
        return v_menor_custo

    def pega_vizinhos(self, vertice):
        if self.representacao == "matriz":
            pass
        else:
            vizinhos = []
            if vertice in self.vertices:
                for (vizinho, peso) in self.vizinhos[vertice]:
                    vizinhos.append(vizinho)
        return vizinhos

    def pega_peso(self, v_a, v_b):
        peso_encontrado = +1e10

        if v_a in self.vertices and v_b in self.vertices:
            for (vizinho, p) in self.vizinhos[v_a]:
                if vizinho == v_b:
                    peso_encontrado = p
                    break
        return peso_encontrado
    
    def busca_profundidade(self, vertice_inicial, vertice_final):
        # Utiliza PILHA
        stack = []

        # lista de visitados
        visitados = []

        # adicionar o elemento inicial na estrutura
        stack.append(vertice_inicial)

        # Enquanto houverem elementos na estrutura
        while len(stack) > 0:
            # Pega o ultimo elemento da estrutura
            vertice_atual = stack.pop(-1)

            # adiciona o vertice atual nos visitados
            if vertice_atual not in visitados:
                visitados.append(vertice_atual)

            # adicionar os visinhos a pilha
            for vizinho in sorted(self.pega_vizinhos(vertice_atual)):
                # se o vizinho ainda nao foi visitado 
                if vizinho not in visitados:
                    # adiciona ele na pilha
                    stack.append(vizinho)

            # verificar se não chegamos no vertice final
            if vertice_atual == vertice_final:
                break

        # retorno dos visitados
        return visitados
    
    def busca_largura(self, vertice_inicial, vertice_final):
        # Utiliza FILA
        queue = []

        # lista de visitados
        visitados = []

        # adicionar o elemento inicial na estrutura
        queue.append(vertice_inicial)

        # Enquanto houverem elementos na estrutura
        while len(queue) > 0:
            # Pega o ultimo elemento da estrutura
            vertice_atual = queue.pop(0)

            # adiciona o vertice atual nos visitados
            if vertice_atual not in visitados:
                visitados.append(vertice_atual)

            # adicionar os visinhos a pilha
            for vizinho in sorted(self.pega_vizinhos(vertice_atual)):
                # se o vizinho ainda nao foi visitado 
                if vizinho not in visitados:
                    # adiciona ele na pilha
                    queue.append(vizinho)

            # verificar se não chegamos no vertice final
            if vertice_atual == vertice_final:
                break

        # retorno dos visitados
        return visitados   

    def eh_conectado(self):
        # TODO: warshall
        # existe algum 0? -> não é conectado
        # caso contrário, é conectado
        return True

    def prim(self):
        # TODO: Implementar função que determina se o grafo é conexo ou não
        if eh_conectado():
            # lista de vetices e antecessores
            predecessores = {}
            pesos = {}
            for vertice in self.lista_vertices:
                predecessores[vertice] = None
                pesos[vertice] = +1e10

            
            # criando lista de vertices que existem no grafo original
            q = [x for x in self.lista_vertices]
            
            while len(q) > 0:
                # encontrar o vértice ainda não adicionado que tenha o menor peso
                u = self.extract_min(q, pesos)

                # removendo o vértice da lista de vértices
                q.remove(u)

                for vizinho in self.pega_vizinhos(u):
                    peso = self.pega_peso(u, vizinho)
                    if vizinho in q and peso < pesos[vizinho]:
                        predecessores[vizinho] = u
                        pesos[vizinho] = peso
            # monta novo grafo com as conexões e pesos encontrados
            g_prim = Grafo(self.representacao, False, ponderado=True)

            # copiar vertices originais
            for vertice in self.lista_vertices:
                g_prim.adiciona_vertice(vertice)
            
            # adiciona as arestas
            custo_acumulado = 0
            for vertice_inicio in predecessores.key():
                vertice_final = predecessores[vertice_inicio]
                if vertice_final is not None:
                    g_prim.cria_aresta(vertice_inicio,vertice_final, pesos[vertice_inicio])
                    custo_acumulado += pesos[vertice_inicio]

            # retorna a MST
            return g_prim, custo_acumulado
    

    
if __name__ == '__main__':
    g = Grafo("lista", False, ponderado=True)
    g.adiciona_vertice("A")
    g.adiciona_vertice("B")
    g.adiciona_vertice("C")
    g.adiciona_vertice("D")
    g.adiciona_vertice("E")

    g.cria_aresta('A', 'B',2)
    g.cria_aresta('A', 'C',4)
    g.cria_aresta('B', 'C',6)
    g.cria_aresta('C', 'D',1)
    g.cria_aresta('D', 'E',2)
    g.cria_aresta('C', 'E',3)

    print(g)
    print("Busca em Profundidade (A->E):")
    print(g.busca_profundidade("A", "E"))

    print("Busca em Largura (A->E):")
    print(g.busca_largura("A", "E"))

    print("Prim MST:")
    g_mst, custo = g.prim()
    print(f'MST = {g_mst}\n custo = {custo}')
    # g = Grafo("lista", True, ponderado=True)
    # g.cria_aresta('A', 'B', peso=5)
    # g.cria_aresta('B', 'C', peso=2)
    # g.cria_aresta('C', 'D', peso=1)
    # g.cria_aresta('D', 'E', peso=2)
    # g.cria_aresta('C', 'E', peso=8)
    # print(g)
    # caminho, custo = g.dijkstra('A', 'E')
    # print(f"Menor caminho entre A e E: {caminho} com custo: {custo}")
    # print(f"vizinhos de A: {g.pega_vizinhos('A')}")
    # print(g)