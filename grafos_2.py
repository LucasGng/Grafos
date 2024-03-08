class Graph():

    def __init__(self, directed, weighted, representation):

        self.directed = directed #boolean
        self.weighted = weighted #boolean
        self.representation = representation #string?

        if self.representation == "MATRIZ":
            self.matrix = [[]]
        
        else:
            self.vertex_list = {}#dicionário de vértices ("nome": {"nome" : peso, ...})
    

    def check_vertex(self, vertex): #verifica se os vértices existem no grafo

        if vertex in self.vertex_list: ####
            return True
        else:
            return False

    def indegree(self, vertex): #vertex a ser verificado

        counter = 0

        for i in self.vertex_list.values:####

            for j in self.vertex_list.values: #procurar pelas chaves no valores de cada vertex ####
                print(j)
                if j == vertex:
                    counter+=1

        return counter

    def outdegree(self, vertex):

        return len(self.vertex_list[vertex]) #####
    
    def add_vertex(self, vertex):

        if self.check_vertex(vertex):
            return False
        
        elif self.representation == "LISTA":
        
            self.vertex_list.update({vertex : {}}) #####

            print(f"vértive {vertex} adicionado") #remover dps
        
        else:
            #adicionar o vértice na matriz
            pass

        return True

    def check_edge(self, begin, end): #verfifica se exite arestas entre dois vértices desse grafo
        
        if self.check_vertex(begin) == False or self.check_vertex(end) == False:
            return False

        elif end in self.vertex_list[begin].keys(): ####
            return True
    
    def add_edge(self, begin, end, weight):

        if self.check_vertex(begin) == False or self.check_vertex(end) == False:
            return False

        elif end in self.vertex_list[begin].keys() or begin in self.vertex_list[end].keys():

            print("already exists") #remover depois
            return False
        
        elif self.weighted == False: #se o grafo for sem peso, resete o peso para none
            weight = None
        
        if self.representation == "LISTA":          
        #colocar no dicionario na chave "begin" e "end" o valor de "end" e "begin" junto ao peso "weight"
            self.vertex_list[begin].update({end : weight})

            if self.directed == False: # se não for direcionado deve-se adicinar no dicionário de chegada tbm
                self.vertex_list[end].update({begin : weight})
            
            print("aresta criada com sucesso") #remover dpss
        
        else: #inserir na matriz como o valor do peso, 0 para sem peso

            pass

        return True

    #def remove_vertex(self, vertex):

        #if self.check_vertex(vertex)
    
    def remove_edge(self, begin, end):

        if self.check_vertex(begin) == False or self.check_vertex(end) == False:
            return False
        
        elif self.representation == "LISTA":
        
            if end in self.vertex_list[begin].keys():

                del self.vertex_list[begin][end]
                del self.vertex_list[end][begin]

                return True
        
        else:
            #remover da matriz
            pass

    def edit_edge(self,begin, end):

        if self.check_vertex(begin) == False or self.check_vertex(end) == False:
            return False
        
        else:
            pass


    def __str__(self):

        #verificar se é matriz ou lista antes de printar
        return f"Grafo {self.representation} {self.vertex_list}" ####

if __name__ == "__main__":

    Grafo_lista = Graph(False, True, "LISTA")

    if Grafo_lista.add_vertex("A"):
        print("Adicionado")
    else:
        print("Não adicionado")

    if Grafo_lista.add_vertex("A"):
        print("Adicionado")
    else:
        print("Não adicionado")
    
    if Grafo_lista.add_vertex("B"):
        print("Adicionado")
    else:
        print("Não adicionado")
  
    if Grafo_lista.add_edge("A", "B", 5):
        print("Criado aresta")
    else:
        print("Não criado aresta")
    
    if Grafo_lista.add_edge("A", "C", 4):
        print("Criado aresta")
    else:
        print("Não criado aresta")
    
    if Grafo_lista.check_edge("A", "B"):
        print("Aresta encontrada")
    else:
        print("Aresta não encontrada")

    if Grafo_lista.check_edge("A", "C"):
        print("Aresta encontrada")
    else:
        print("Aresta não encontrada")
    
    if Grafo_lista.add_vertex("C"):
        print("Adicionado")
    else:
        print("Não adicionado")

    if Grafo_lista.add_edge("A", "C", 4):
        print("Criado aresta")
    else:
        print("Não criado aresta")

    if Grafo_lista.add_vertex("C"):
        print("Adicionado")
    else:
        print("Não adicionado")

    print(Grafo_lista)

    if Grafo_lista.remove_edge("A", "B"):
        print("Removido aresta")
    else:
        print("Não removido aresta")

    if Grafo_lista.remove_edge("A", "B"):
        print("Removido aresta")
    else:
        print("Não removido aresta")
        
    if Grafo_lista.add_edge("A", "C", 4):
        print("Criado aresta")
    else:
        print("Não criado aresta")

    print(Grafo_lista)