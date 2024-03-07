class Graph():

    def __init__(self, directed, weighted, representation):

        self.directed = directed #boolean
        self.weighted = weighted #boolean
        self.representation = representation #string?

        if self.representation == "Matriz":

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
        
        elif self.representation == "Lista":
        
            self.vertex_list.update({vertex : {}}) #####
        
        else:
            #adicionar o vértice na matriz
            pass

        return True

    def check_edge(self, begin, end): #verfifica se exite arestas entre dois vértices desse grafo
        
        if self.check_vertex(begin):

            if end in self.vertex_list[begin].values(): ####

                print("a")
    
    def add_edge(self, begin, end, weight):

        if self.weighted == False: #se o grafo for sem peso, resete o peso para none
            weight = None
        
        #colocar no dicionario na chave "begin" o valor de "end" junto ao peso "weight"
            
        if self.check_vertex(begin) == False or self.check_vertex(end) == False:

            return False
        
        self.vertex_list[begin].update({end : weight})

        return True


    #def remove_vertex(self, vertex):

        #if self.check_vertex(vertex)

    def __str__(self):

        #verificar se é matriz ou lista antes de printar
        return f"Grafo {self.representation} {self.vertex_list}" ####

if __name__ == "__main__":

    Grafo_lista = Graph(False, True, "Lista")

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
    
    print(Grafo_lista)