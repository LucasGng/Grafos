class Graph():

    def __init__(self, directed, weighted, representation):

        self.directed = directed #boolean
        self.weighted = weighted #boolean
        self.representation = representation #string?

        if self.representation == "MATRIZ":
            self.vertex_matrix = []
            self.array_name = {} #para indexar as colunas e linhas com o nome {"nome": index}
        
        elif self.representation == "LISTA":
            self.vertex_list = {}#dicionário de vértices ("nome": {"nome" : peso, ...})
    

    def check_vertex(self, vertex): #verifica se os vértices existem no grafo

        if self.representation == "LISTA":
            if vertex in self.vertex_list: ####
                return True
            else:
                return False
        
        elif self.representation == "MATRIZ": ###check in matrix

            if vertex in self.array_name: #procura pelo nome do vértice como a chave do dict
                return True
            else:
                return False

    def indegree(self, vertex): #vertex a ser verificado

        if self.check_vertex(vertex) == False:

            return False

        counter = 0

        if self.representation == "LISTA":

            if self.directed == True: #conta apenas os vértices de chegada

                for i in self.vertex_list:#itera sobre as chaves 

                    if i != vertex:

                        #print(i) #remover dps
                        for j in self.vertex_list[i]: #procurar pelas chaves no valores de cada vertex
                            
                            #print(j) #remover dps
                            if j == vertex:
                                counter+=1
            else:
                counter = len(self.vertex_list[vertex])
        
        elif self.representation == "MATRIZ":

            for array in self.vertex_matrix:

                for position in range(len(array)):

                    if position == self.array_name[vertex] and array[position] != None:

                        print(array[position]) #remover dps

                        counter+=1

        return counter

    def outdegree(self, vertex):

        if self.check_vertex(vertex) == False:
            
            return False

        if self.representation == "LISTA":

            return len(self.vertex_list[vertex]) #####
        
        elif self.representation == "MATRIZ": #outdegree in matrix

            counter = 0

            for i in self.vertex_matrix[self.array_name[vertex]]:

                print(i)

                if i != None:

                    counter+=1
        
            return counter

    def degree(self, vertex):

        if self.check_vertex(vertex) == False:
            
            return False
        
        counter = 0
        
        if self.representation == "LISTA":

            if self.directed == True:

                counter = len(self.vertex_list[vertex]) + self.indegree(vertex)
            
            else:
                counter = len(self.vertex_list[vertex]) #não direcionado mudo o que?
        
        elif self.representation == "MATRIZ": #degree na matriz

            if self.directed == True:

                counter = self.outdegree(vertex) + self.indegree(vertex)
            
            else:

                for i in self.vertex_matrix[self.array_name[vertex]]:

                    if i != None:

                        counter+=1
    
        return counter
    
    def add_vertex(self, vertex):

        if self.check_vertex(vertex):
            return False
        
        elif self.representation == "LISTA":
        
            self.vertex_list.update({vertex : {}}) #####

            print(f"vértive {vertex} adicionado") #remover dps
        
        elif self.representation == "MATRIZ":

            new_array = [] #cria um array para o vértice

            #adicionar o vértice na matriz e no dict, no caso do último, se adiciona junto ao seu index
            self.array_name.update({vertex : len(self.array_name)})

            for i in range(len(self.array_name)):
                new_array.append(None)

            for array in self.vertex_matrix:

                array.append(None) #adiciona um 0 para todo array já existente na matriz

            self.vertex_matrix.append(new_array)

        return True

    def check_edge(self, begin, end): #verfifica se exite arestas entre dois vértices desse grafo
        
        if self.check_vertex(begin) == False or self.check_vertex(end) == False:
            return False

        elif self.representation == "LISTA":
            
            if end in self.vertex_list[begin].keys(): ####
                return True
        
        elif self.representation == "MATRIZ": #check for both indexes and see if its not 0
            #check if in matriz
            if self.vertex_matrix[self.array_name[begin]][self.array_name[end]] != 0:

                print(self.array_name[begin]) #remover dps
                print(self.array_name[end]) #remover dps

                print("Aresta encontrada na matriz")
                return True
        return False
    
    def add_edge(self, begin, end, weight):

        if self.check_vertex(begin) == False or self.check_vertex(end) == False:

            return False
        
        elif self.weighted == False: #se o grafo for sem peso, resete o peso para 1
            
            weight = 1
        
        if self.representation == "LISTA":

            if end in self.vertex_list[begin].keys():

                print("--- already exists ---") #remover depois
                return False
            
            #colocar no dicionario na chave "begin" e "end" o valor de "end" e "begin" junto ao peso "weight"
            self.vertex_list[begin].update({end : weight})

            if self.directed == False: # se não for direcionado deve-se adicinar no dicionário de chegada tbm
                self.vertex_list[end].update({begin : weight})
            
            print("--- aresta criada com sucesso ---") #remover dpss
        
        elif self.representation == "MATRIZ": #inserir na matriz como o valor do peso, 0 para sem peso

            if self.vertex_matrix[self.array_name[begin]][self.array_name[end]] != None:

                 print("--- already exists ---") #remover depois
                 return False

            self.vertex_matrix[self.array_name[begin]][self.array_name[end]] = weight

            if self.directed == False: #adiciona no array de chagada tbm

                self.vertex_matrix[self.array_name[end]][self.array_name[begin]] = weight

        return True

    def remove_vertex(self, vertex):

        if self.check_vertex(vertex) == False:
            return False
        
        elif self.representation == "LISTA":

            del self.vertex_list[vertex]

            for key in self.vertex_list: #percorre as chaves e procura por restígios do vértice removido

                if vertex in self.vertex_list[key]:

                    print(f" -------- {self.vertex_list[key][vertex]} ------------")

                    del self.vertex_list[key][vertex]
            
            return True
        
        elif self.representation == "MATRIZ": #remove coluna e linha da matriz que corresponde ao vertice, reindexar tudo depois

            del self.vertex_matrix[self.array_name[vertex]]

            for i in self.vertex_matrix:

                for j in range(len(i)):

                    if j == self.array_name[vertex]:

                        del i[j]
            
            for v in self.array_name:

                if self.array_name[v] > self.array_name[vertex]:
                    self.array_name[v] -=1
            
            del self.array_name[vertex]

            return True #########################################################################################
    
    def remove_edge(self, begin, end):

        if self.check_vertex(begin) == False or self.check_vertex(end) == False:
            return False
        
        elif self.representation == "LISTA":
        
            if end in self.vertex_list[begin].keys(): #.keys

                del self.vertex_list[begin][end]

                if self.directed == False: #se for direcionado remove dos vizinhos do vertice de chegada tbm

                    del self.vertex_list[end][begin]

                return True
        
        elif self.representation == "MATRIZ":
            #remover da matriz
            if self.vertex_matrix[self.array_name[begin]][self.array_name[end]] != None:

                self.vertex_matrix[self.array_name[begin]][self.array_name[end]] = None

                if self.directed == False:#remove do array de chegada tbm

                    self.vertex_matrix[self.array_name[end]][self.array_name[begin]] = None
            
                return True

    def update_weight(self,begin, end, weight):

        if self.check_vertex(begin) == False or self.check_vertex(end) == False:
            return False
        
        elif self.weighted == False:

            if self.representation == "LISTA":
                weight = 1
            elif self.representation == "MATRIZ":
                weight = None
        
        if self.check_edge(begin, end) == False: #cria aresta já que não existe

            print("--- bruh need to create ---")

            self.add_edge(begin, end, weight)

            return True
        
        elif self.representation == "LISTA":

            self.vertex_list[begin][end] = weight

            if self.directed == False:
                self.vertex_list[end][begin] = weight

            print("--- PESO ATUALIZADO ---")
        
        elif self.representation == "MATRIZ": #atualizar peso na matriz

            print("Editar na matriz") #remover dps

            self.vertex_matrix[self.array_name[begin]][self.array_name[end]] = weight

            if self.directed == False:

                self.vertex_matrix[self.array_name[end]][self.array_name[begin]] = weight

            print(f"{self.array_name[begin]} --- {self.array_name[end]}")

        return True

    def get_weight(self, begin, end):

        if self.check_vertex(begin) == False or self.check_vertex(end) == False or self.check_edge(begin, end) == False:
            
            return None    

        elif self.representation == "LISTA":

            if end in self.vertex_list[begin]:
                return self.vertex_list[begin][end]
            else:
                return None
        
        elif self.representation == "MATRIZ": #verificar apenas o valor na matriz

            if self.vertex_matrix[self.array_name[begin]][self.array_name[end]] != None:

                return self.vertex_matrix[self.array_name[begin]][self.array_name[end]]
            else:
                return None
    
    #função que recebe lista de vértices e custos acumulados
    #objetivo de encontra o vértice com menor custo acumulado até o momento
    def extract_min(self, q, accumulated_cost):

        vertex_lower_cost = None
        min_weight = +1e10 #mudar dps

        for vertex in q:

            if accumulated_cost[vertex] < min_weight:

                min_weight = accumulated_cost[vertex]
                vertex_lower_cost = vertex
        
        return vertex_lower_cost

    def get_neighbors(self, vertex):

        if self.check_vertex(vertex) == False:

            return False
        
        elif self.representation == "LISTA":
            neighbors = {}

            for neighbor in self.vertex_list[vertex]:

                neighbors[neighbor] = self.vertex_list[vertex][neighbor]        

            return neighbors
        
        elif self.representation == "MATRIZ":

            neighbors = {}

            for index in range(len(self.vertex_matrix[self.array_name[vertex]])): #procura no array do vértice

                if self.vertex_matrix[self.array_name[vertex]][index] != None:

                    for key, value in self.array_name.items():

                        if value == index:
                            neighbors[key] = self.array_name[key]
            
            return neighbors

    def djikstra(self, begin, end):

        if self.check_vertex(begin) == False or self.check_vertex(end) == False:

            print("caminho impossivel")
            return [], None
    
        #lista de predecessores
        pi = {}
        #estrutura de custo acumulado
        accumulated_cost = {}

        vertices = {}

        if self.representation == "LISTA":

            vertices = self.vertex_list
        
        elif self.representation == "MATRIZ":

            vertices = self.array_name

        for vertex in vertices:

            accumulated_cost[vertex] = +1e10 #mudar depois
            
            pi[vertex] = None
        
        accumulated_cost[begin] = 0.0

        #lista de prioridade
        q = []

        for vertex in vertices:

            q.append(vertex)
        
        #loop principal verifica os pesos
        while len(q) > 0:
            #encontra o nó com menor custo até o momento
            current_node = self.extract_min(q, accumulated_cost)

            #nó não encontrado
            if current_node is None:
                break

            q.remove(current_node)

            #laço para verificar vizinhos
            for neighbor in self.get_neighbors(current_node):

                new_cost = accumulated_cost[current_node] + self.get_weight(current_node, neighbor) #aqui mudar?

                #se o novo custo for menor que o custo encontrado antes
                if new_cost < accumulated_cost[neighbor]:

                    #substitui o custo para chegar o vizinho
                    accumulated_cost[neighbor] = new_cost

                    #criando link entre o vizinho e  atual
                    pi[neighbor] = current_node
        
        #caminho entre o nó inicial e final
        path = []
        total_cost = 1e10

        if pi[end] != None:

            #caminho encontrado
            total_cost = accumulated_cost[end]

            #montando o caminho ao "retornar" na estrutura de predecessores
            current_node = end

            while current_node != None:
                
                path.insert(0, current_node)
                current_node = pi[current_node]

        #retorna                  
        return path, total_cost
    
    def depth_search(self, begin,end):
        #essa busca usa pilha
        stack = []

        visited = []

        stack.append(begin)

        #enquanto houver elementos na pilha
        while len(stack) > 0:

            current_vertex = stack.pop(-1)

            #adiciona o vértice atual nos visitados

            if current_vertex not in visited:

                visited.append(current_vertex)
            
            #adicions os vizinhos na pilha
            
            for neighbor in self.get_neighbors(current_vertex):

                if neighbor not in visited:

                    stack.append(neighbor)
            
            #verificar se não chegamos no vértice de destino
            if current_vertex == end:
                break
        
        return visited
    

    def width_search(self, begin,end):
        #essa busca usa fila
        queue = []

        visited = []

        queue.append(begin)

        #enquanto houver elementos na pilha
        while len(queue) > 0:

            current_vertex = queue.pop(0)

            #adiciona o vértice atual nos visitados

            if current_vertex not in visited:

                visited.append(current_vertex)
            
            #adicions os vizinhos na pilha
            
            for neighbor in self.get_neighbors(current_vertex):

                if neighbor not in visited:

                    queue.append(neighbor)
            
            #verificar se não chegamos no vértice de destino
            if current_vertex == end:
                break
        
        return visited

    def __str__(self):

        #verificar se é matriz ou lista antes de printar
        if self.representation == "LISTA":
            return f"Grafo {self.representation} {self.vertex_list}" ####
        elif self.representation == "MATRIZ":
            return f"{self.vertex_matrix}\n Vértices e index {self.array_name}"

if __name__ == "__main__":
 
                    #DIRECTED  WEIGHT = false
    Grafo_lista = Graph(True, True, "LISTA")

    if Grafo_lista.add_vertex("A"):
        print("Adicionado") ###
    else:
        print("Não adicionado")

    if Grafo_lista.add_vertex("A"):
        print("Adicionado")
    else:
        print("Não adicionado") ###
    
    if Grafo_lista.add_vertex("B"): 
        print("Adicionado") ###
    else:
        print("Não adicionado")
  
    if Grafo_lista.add_edge("A", "B", 5):
        print("Criado aresta") ###
    else:
        print("Não criado aresta")
    
    if Grafo_lista.add_edge("A", "C", 4):
        print("Criado aresta")
    else:
        print("Não criado aresta") ###
    
    if Grafo_lista.check_edge("A", "B"):
        print("Aresta encontrada") ####
    else:
        print("Aresta não encontrada")

    if Grafo_lista.check_edge("A", "C"):
        print("Aresta encontrada")
    else:
        print("Aresta não encontrada") ###
    
    if Grafo_lista.add_vertex("C"):
        print("Adicionado") ###
    else:
        print("Não adicionado")

    if Grafo_lista.add_edge("A", "C", 4):
        print("Criado aresta") ###
    else:
        print("Não criado aresta")

    if Grafo_lista.add_edge("C", "A", 30):
        print("Criado aresta se direcionado") #se direvionado
    else:
        print("Não criado aresta se nao direcionado") ### se nao direcionado

    if Grafo_lista.add_vertex("C"):
        print("Adicionado")
    else:
        print("Não adicionado") ###

    print(Grafo_lista.indegree("A")) ################################

    print(Grafo_lista)

    if Grafo_lista.remove_edge("A", "B"):
        print("Removido aresta") ###
    else:
        print("Não removido aresta")

    if Grafo_lista.remove_edge("A", "B"):
        print("Removido aresta")
    else:
        print("Não removido aresta") ###
        
    if Grafo_lista.add_edge("A", "C", 4):
        print("Criado aresta")
    else:
        print("Não criado aresta") ###

    
    if Grafo_lista.update_weight("B", "C", 5674):
        print("UPDATED AAAAAA")  ###
    else:
        print("NOT UPDATED")

    if Grafo_lista.update_weight("A", "C", 999):
        print("UPDATED") ###
    else:
        print("NOT UPDATED")

    print(Grafo_lista)

    if Grafo_lista.update_weight("B", "C", 233):
        print("UPDATED")###
    else:
        print("NOT UPDATED")
    
    print(Grafo_lista.get_weight("A", "C"))
    print(Grafo_lista.get_weight("C", "B"))
    print(Grafo_lista.get_weight("A", "B")) #none

    print(Grafo_lista)

    Grafo_lista.get_neighbors("C")

    if Grafo_lista.remove_vertex("A"):
        print("Vértice removido") ###
    else:
        print("Não foi possível remover o vértice")

    print(Grafo_lista)

    if Grafo_lista.remove_vertex("A"):
        print("Vértice removido")
    else:
        print("Não foi possível remover o vértice") ###

    if Grafo_lista.add_vertex("A"):
        print("Adicionado") ###
    else:
        print("Não adicionado") 

    if Grafo_lista.add_vertex("D"):
        print("Adicionado") ###
    else:
        print("Não adicionado") 
    
    if Grafo_lista.add_edge("A", "C", 5):
        print("Criado aresta") ###
    else:
        print("Não criado aresta") 

    if Grafo_lista.add_edge("B", "D", 9):
        print("Criado aresta") ###
    else:
        print("Não criado aresta") 

    if Grafo_lista.add_edge("C", "D", 30):
        print("Criado aresta") ###
    else:
        print("Não criado aresta") 
    
    print(Grafo_lista)

    print("----------------------------")
    print(Grafo_lista.indegree("B")) #########################
    print(Grafo_lista.outdegree("B")) #######################
    print(Grafo_lista.degree("B")) #########################

    print("----------------------------")
    path, cost = Grafo_lista.djikstra("A", "D")

    print(f"Caminho entre A e D{path} com peso {cost}")

    if Grafo_lista.add_vertex("E"):
        print("Adicionado") ###
    else:
        print("Não adicionado")

    if Grafo_lista.add_edge("C", "E", 2):
        print("Criado aresta") ###
    else:
        print("Não criado aresta") 
    

    if Grafo_lista.add_edge("A", "B", 2):
        print("Criado aresta") ###
    else:
        print("Não criado aresta") 
    
    print(Grafo_lista.depth_search("A", "E"))
    print(Grafo_lista.width_search("A", "E"))

    print(Grafo_lista)



    ####### fim lista #########################################################################
        
    Grafo_matriz = Graph(False, True, "MATRIZ")

    if Grafo_matriz.add_vertex("A"):
        print("Adicionado") ###
    else:
        print("Não adicionado")

    if Grafo_matriz.add_vertex("A"):
        print("Adicionado")
    else:
        print("Não adicionado") ###
    
    if Grafo_matriz.add_vertex("B"): 
        print("Adicionado") ###
    else:
        print("Não adicionado")
  
    if Grafo_matriz.add_edge("A", "B", 5):
        print("Criado aresta") ###
    else:
        print("Não criado aresta")
    
    if Grafo_matriz.add_edge("A", "C", 4):
        print("Criado aresta")
    else:
        print("Não criado aresta") ###

    if Grafo_matriz.add_vertex("C"):
        print("Adicionado")
    else:
        print("Não adicionado") ###

    if Grafo_matriz.add_edge("A", "B", 5):
        print("Criado aresta") ###
    else:
        print("Não criado aresta")
   
    if Grafo_matriz.add_edge("A", "C", 4):
        print("Criado aresta")
    else:
        print("Não criado aresta") ###

    
    if Grafo_matriz.add_edge("C", "A", 6):
        print("Criado aresta")
    else:
        print("Não criado aresta") ###

    if Grafo_matriz.add_edge("D", "A", 9):
        print("Criado aresta")
    else:
        print("Não criado aresta") ###
    
    if Grafo_matriz.add_vertex("D"):
        print("Adicionado")
    else:
        print("Não adicionado") ###
    
    if Grafo_matriz.add_edge("D", "A", 9):
        print("Criado aresta")
    else:
        print("Não criado aresta") ###

    if Grafo_matriz.add_edge("B", "C", 3):
        print("Criado aresta")
    else:
        print("Não criado aresta") ###
    
    if Grafo_matriz.check_edge("A", "C"):
        print("Aresta encontrada")
    else:
        print("Aresta não encontrada") ###
    
    print(Grafo_matriz)

    if Grafo_matriz.remove_edge("A", "B"):
        print("Removido aresta")
    else:
        print("Não removido aresta") ###

    if Grafo_matriz.update_weight("D", "C", 444):
        print("UPDATED")###
    else:
        print("NOT UPDATED")

    a, b = Grafo_matriz.djikstra("A", "B")

    print(f"Caminho entre A e D{a} com peso {b}")

    print(Grafo_matriz)


    if Grafo_matriz.remove_vertex("B"):
        print("Vértice removido")
    else:
        print("Não foi possível remover o vértice") ###

    print(Grafo_matriz)

    p, c = Grafo_matriz.djikstra("A", "B")

    print(f"Caminho entre A e B {p} com peso {c}")

    p, c = Grafo_matriz.djikstra("A", "A")

    print(f"Caminho entre A e A {p} com peso {c}")

    if Grafo_matriz.add_edge("A", "B", 5):
        print("Criado aresta") ###
    else:
        print("Não criado aresta")
    
    if Grafo_matriz.remove_vertex("B"):
        print("Vértice removido")
    else:
        print("Não foi possível remover o vértice") ###
    
    if Grafo_matriz.remove_vertex("C"):
        print("Vértice removido")
    else:
        print("Não foi possível remover o vértice") ###
    
    if Grafo_matriz.update_weight("A", "D", 2):
        print("UPDATED")###
    else:
        print("NOT UPDATED")

    print(Grafo_matriz)

    if Grafo_matriz.add_vertex("B"): 
        print("Adicionado") ###
    else:
        print("Não adicionado")
    
    if Grafo_matriz.add_vertex("C"): 
        print("Adicionado") ###
    else:
        print("Não adicionado")
    
    if Grafo_matriz.add_edge("A", "B", 5):
        print("Criado aresta") ###
    else:
        print("Não criado aresta")
    
    if Grafo_matriz.add_edge("B", "A", 9):
        print("Criado aresta") ###
    else:
        print("Não criado aresta")
    
    if Grafo_matriz.add_edge("C", "A", 3):
        print("Criado aresta") ###
    else:
        print("Não criado aresta")
    

    if Grafo_matriz.add_edge("D", "B", 10):
        print("Criado aresta") ###
    else:
        print("Não criado aresta")

    print(Grafo_lista.depth_search("A", "E"))
    print(Grafo_lista.width_search("A", "E"))

    print(Grafo_matriz.get_weight("A", "D"))
    print(Grafo_matriz.get_weight("D", "A"))
    print(Grafo_matriz.get_weight("B", "A"))
    print(Grafo_matriz)

    print(f"ingrau de A {Grafo_matriz.indegree('A')}") ################################
    print(f"ingrau de B {Grafo_matriz.indegree('B')}") ################################
    print(f"ingrau de D {Grafo_matriz.indegree('D')}") ################################

    print(f"outgrau de A {Grafo_matriz.outdegree('A')}") ################################
    print(f"outgrau de B {Grafo_matriz.outdegree('B')}") ################################
    print(f"outgrau de D {Grafo_matriz.outdegree('D')}") ################################

    print(f"grau de A {Grafo_matriz.degree('A')}") ################################
    print(f"grau de B {Grafo_matriz.degree('B')}") ################################
    print(f"grau de D {Grafo_matriz.degree('D')}") ################################