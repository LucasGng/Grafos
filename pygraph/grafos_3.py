import time
import matplotlib.pyplot as plt

class Graph():

    def __init__(self, directed, weighted, representation):

        self.directed = directed #boolean
        self.weighted = weighted #boolean
        self.representation = representation #string

        if self.representation == "MATRIZ":
            self.vertex_matrix = []
            self.array_name = {} #para indexar as colunas e linhas com o nome do vértice {"vértice": index}
        
        elif self.representation == "LISTA":
            self.vertex_list = {}#dicionário de vértices ("vértice": {"vizinho" : peso, ...})
    

    def check_vertex(self, vertex): #verifica se os vértices existem no grafo

        if self.representation == "LISTA":
            if vertex in self.vertex_list: #se já existir
                return True
            else:
                return False
        
        elif self.representation == "MATRIZ": 

            if vertex in self.array_name: #procura pelo nome do vértice como a chave do dicionário
                return True
            else:
                return False

    def indegree(self, vertex): #função que retorna o indegree

        if self.check_vertex(vertex) == False:
            return False

        counter = 0

        if self.representation == "LISTA":

            if self.directed == True: #conta apenas os vértices de chegada

                for i in self.vertex_list:#itera sobre as chaves do vertex_list

                    if i != vertex: #procura por todos vértices que não são o selecionado

                        for j in self.vertex_list[i]: #procurar pelas chaves nos vizinhos de cada vertex
                            
                            if j == vertex: #se o vértice for encontrado como chegada de um de seus vizinhos
                                counter+=1
            else:
                counter = len(self.vertex_list[vertex]) #conta todos as arestas conectadas em não direcionado
        
        elif self.representation == "MATRIZ":

            for array in self.vertex_matrix: #itera sobre os arrays da matriz

                for position in range(len(array)): #procura pelos elementos do array

                    #se a posição corresponder ao índice do vértice escolhido e não for nulo
                    if position == self.array_name[vertex] and array[position] != None:

                        #print(array[position]) #remover dps
                        counter+=1

        return counter

    def outdegree(self, vertex): #função que calcula o outdegree

        if self.check_vertex(vertex) == False:
            
            return False

        if self.representation == "LISTA":

            return len(self.vertex_list[vertex]) #retorna todas as arestas que saem do vértice escolhido
        
        elif self.representation == "MATRIZ":

            counter = 0

            for i in self.vertex_matrix[self.array_name[vertex]]: #itera sobre elementos do array do vértice escolhido

                #print(i)

                if i != None: #se houver aresta

                    counter+=1
        
            return counter

    def degree(self, vertex): #função de degree

        if self.check_vertex(vertex) == False:
            
            return False
        
        counter = 0
        
        if self.representation == "LISTA":

            if self.directed == True:

                counter = len(self.vertex_list[vertex]) + self.indegree(vertex) #direcionado soma o outdegree e indegree
            
            else:
                counter = len(self.vertex_list[vertex]) #mesmo do outgree em não direcionado
        
        elif self.representation == "MATRIZ":

            if self.directed == True:

                counter = self.outdegree(vertex) + self.indegree(vertex) 
            
            else:

                for i in self.vertex_matrix[self.array_name[vertex]]: 

                    if i != None: #ocorrências de todos que não None

                        counter+=1
    
        return counter
    
    def add_vertex(self, vertex):

        if self.check_vertex(vertex):
            return False
        
        elif self.representation == "LISTA":
        
            self.vertex_list.update({vertex : {}}) #atualiza no dicionário o novo vértice sem vizinhos

            #print(f"vértive {vertex} adicionado") #remover dps
        
        elif self.representation == "MATRIZ":

            new_array = [] #cria um array para o vértice

            #adicionar o vértice na matriz e no dict, no caso do último, se adiciona na posição de seu index no dict
            self.array_name.update({vertex : len(self.array_name)})

            for i in range(len(self.array_name)): #preenche o novo array com valores None
                new_array.append(None)

            for array in self.vertex_matrix:

                array.append(None) #adiciona um None para todo array já existente na matriz

            self.vertex_matrix.append(new_array)

        return True

    def check_edge(self, begin, end): #verfifica se exite arestas entre dois vértices desse grafo
        
        if self.check_vertex(begin) == False or self.check_vertex(end) == False:
            return False

        elif self.representation == "LISTA":
            
            if end in self.vertex_list[begin].keys(): #verifica se o vértice de chegada é vixinho do saída
                return True
        
        elif self.representation == "MATRIZ": 
            #verifica se o elemento na posição matriz[chegada][saída] for diferente de None
            if self.vertex_matrix[self.array_name[begin]][self.array_name[end]] != None:

                #print("Aresta encontrada na matriz")
                return True
        return False
    
    def add_edge(self, begin, end, weight):

        if self.check_vertex(begin) == False or self.check_vertex(end) == False:

            return False
        
        elif self.weighted == False: #se o grafo for sem peso, resete o peso para 1
            
            weight = 1
        
        if self.representation == "LISTA":

            if end in self.vertex_list[begin].keys(): #se o vértice de chegada já é vizinho do de saída
 
                return False
            
            #colocar no dicionario na chave "begin" o vértice "end" junto ao peso "weight"
            self.vertex_list[begin].update({end : weight})

            if self.directed == False: # se não for direcionado deve-se adicinar no dicionário de chegada também
                self.vertex_list[end].update({begin : weight})
            
        elif self.representation == "MATRIZ": #inserir na matriz como o valor do peso

            #se já existe
            if self.vertex_matrix[self.array_name[begin]][self.array_name[end]] != None:

                 #print("--- already exists ---") #remover depois
                 return False

            self.vertex_matrix[self.array_name[begin]][self.array_name[end]] = weight

            if self.directed == False: #adiciona no array de chagada também se não direcionado

                self.vertex_matrix[self.array_name[end]][self.array_name[begin]] = weight

        return True

    def remove_vertex(self, vertex): #função de remoção de vértice

        if self.check_vertex(vertex) == False:
            return False
        
        elif self.representation == "LISTA":

            del self.vertex_list[vertex] #delete o vértice do dicionário

            for key in self.vertex_list: #percorre as chaves e procura por restígios do vértice removido

                if vertex in self.vertex_list[key]: #se encontrar o vértice como vizinho de outros

                    del self.vertex_list[key][vertex]
            
            return True
        
        elif self.representation == "MATRIZ":

            del self.vertex_matrix[self.array_name[vertex]] #remove o array do vértice da matriz

            for i in self.vertex_matrix:

                for j in range(len(i)):  #percorre cada elemento de cada array da matriz

                    if j == self.array_name[vertex]: #se encontrar a posição do vértice removido

                        del i[j]
            
            for v in self.array_name:

                #para cada vértice com índice maior que o removido, subtraia um para a reindexação
                if self.array_name[v] > self.array_name[vertex]: 
                    self.array_name[v] -=1
            
            del self.array_name[vertex]

            return True 
    
    def remove_edge(self, begin, end): #função que remove uma aresta

        if self.check_vertex(begin) == False or self.check_vertex(end) == False:
            return False
        
        elif self.representation == "LISTA":
        
            if end in self.vertex_list[begin].keys(): #se o vértice de chagada já é vizinho do de saída

                del self.vertex_list[begin][end] #remova-o

                if self.directed == False: #se não for direcionado remove a aresta dos vizinhos do vertice de chegada tbm

                    del self.vertex_list[end][begin]

                return True
        
        elif self.representation == "MATRIZ":
            #se a aresta existir
            if self.vertex_matrix[self.array_name[begin]][self.array_name[end]] != None:

                #deixe como None
                self.vertex_matrix[self.array_name[begin]][self.array_name[end]] = None

                if self.directed == False:#remove do array de chegada também se não for direcionado

                    self.vertex_matrix[self.array_name[end]][self.array_name[begin]] = None
            
                return True

    def update_weight(self,begin, end, weight): #função que atualiza o peso da aresta

        if self.check_vertex(begin) == False or self.check_vertex(end) == False:
            return False
        
        elif self.weighted == False: #se não for ponderado o peso será 1
            weight = 1
        
        if self.check_edge(begin, end) == False: #cria aresta se não existe

            self.add_edge(begin, end, weight)

            return True
        
        elif self.representation == "LISTA":

            self.vertex_list[begin][end] = weight #atualiza o peso do vizinho "end" do vértice de saída "begin"

            if self.directed == False: #se não for direcionado também atualiza na lista de vizinhos do vértice de chegada
                self.vertex_list[end][begin] = weight
        
        elif self.representation == "MATRIZ": #atualizar peso na matriz

            #atualiza na matriz o peso com o índice do vértice de saída e vértice de chegada
            self.vertex_matrix[self.array_name[begin]][self.array_name[end]] = weight

            if self.directed == False: #se não for direcionado

                #atualiza na matriz o peso com o índice do vértice de chegada e vértice de saída
                self.vertex_matrix[self.array_name[end]][self.array_name[begin]] = weight

        return True

    def get_weight(self, begin, end): #função que pega o peso de uma aresta entre dois vértices 

        if self.check_vertex(begin) == False or self.check_vertex(end) == False or self.check_edge(begin, end) == False:
            
            return None

        elif self.weighted == False: #se não houver peso retorne 1

            return 1    

        elif self.representation == "LISTA":

            if end in self.vertex_list[begin]: #verifique se o vértice de chegada é vizinho do vértice de saída
                return self.vertex_list[begin][end] #retorne o valor(peso) da aresta 
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

            if accumulated_cost[vertex] <= min_weight:

                min_weight = accumulated_cost[vertex]
                vertex_lower_cost = vertex
        
        return vertex_lower_cost

    def get_neighbors(self, vertex): #função que retorna os vizinhos de um vértice

        if self.check_vertex(vertex) == False:

            return False
        
        elif self.representation == "LISTA": #se for lista iteramos o dicionário vertex_list
            neighbors = {}

            for neighbor in self.vertex_list[vertex]: #itera sobre os vizinhos do vértice que passamos como parâmetro

                neighbors[neighbor] = self.vertex_list[vertex][neighbor]#colocamos cada vizinho de "vertex" em neighbors        

            return neighbors
        
        elif self.representation == "MATRIZ": #se for marriz iteramos o dicionário array_name

            neighbors = {}

            for index in range(len(self.vertex_matrix[self.array_name[vertex]])): #procura no array do vértice

                #se o valor do index for diferente de None, encontramos um vizinho
                if self.vertex_matrix[self.array_name[vertex]][index] != None:

                    #procura pelo vértice com o index diferente de None na matriz
                    for key, value in self.array_name.items():
                        
                        #colocamos em neighbors o vértice corresponente ao índice "index" da matriz
                        if value == index:
                            neighbors[key] = self.array_name[key] 
            
            return neighbors

    def djikstra(self, begin, end):

        start_djikstra = time.time()

        if self.check_vertex(begin) == False or self.check_vertex(end) == False:

            #print("caminho impossivel")
            return [], None, 0
    
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
        end_djikstra = time.time()
        finish = end_djikstra - start_djikstra

        return path, total_cost, finish
    
    def depth_search(self, begin,end):
        #essa busca usa pilha

        start_depth = time.time()
        if self.check_vertex(begin) == False or self.check_vertex(end) == False:
            
            #print("caminho impossivel")
            return [], 0

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
        
        end_depth = time.time()

        finish_depth = end_depth - start_depth

        return visited, finish_depth
    
    def width_search(self, begin,end):
        #essa busca usa fila

        start_width = time.time()

        if self.check_vertex(begin) == False or self.check_vertex(end) == False:
            
            #print("caminho impossivel")
            return [], 0

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
        
        end_width = time.time()

        finish_width = end_width - start_width
        
        return visited, finish_width

    def isConnected(self):

        #chama a função de warshall e análisa se todos os eleentos são diferentes de 0
        warshall = self.warshall()
        warshall_matrix = warshall.vertex_matrix
        for i in range(len(warshall_matrix)):
            for j in range(len(warshall_matrix)):
                if warshall_matrix[i][j] == None:
                    return False

        return True

    def prim(self):

        if self.directed == True or self.weighted == False:
            return None

        if self.isConnected(): #se o grafo for conectado

            #lista de vértices e antecessores
            predecessors = {}
            weights = {}
            #criando lista de vértices que existem no grafo original
            q = []
            if self.representation == "LISTA":
                for i in self.vertex_list.keys():

                    q.append(i)
                    predecessors[i] = None
                    weights[i] = 1e10

            elif self.representation == "MATRIZ":
                for k in self.array_name.keys():

                    q.append(k)
                    predecessors[k] = None
                    weights[k] = 1e10
            
            while len(q) > 0:

                #encontrar o vértice ainda não adicionado que tenha o menor peso
                u = self.extract_min(q, weights)

                q.remove(u)

                for neighbor in self.get_neighbors(u):

                    w = self.get_weight(u, neighbor)

                    if neighbor in q and w < weights[neighbor]:

                        predecessors[neighbor] = u

                        weights[neighbor] = w
            #print(predecessors)
            #print(weights)

            g_prim = Graph(False, True, self.representation)

            #copiar vértices originais
            if self.representation == "LISTA":
                for vertex_l in self.vertex_list.keys():
                    g_prim.add_vertex(vertex_l)

            elif self.representation == "MATRIZ":
                for vertex_m in self.array_name.keys():

                    print(vertex_m)
                    g_prim.add_vertex(vertex_m)
            
            for vertex_begin in predecessors.keys():

                vertex_end = predecessors[vertex_begin]

                if vertex_end is not None:

                    g_prim.add_edge(vertex_begin, vertex_end, weights[vertex_begin])
            
            return g_prim
        
    def warshall(self):
    # matriz de fechamento transitivo

        if self.representation == "MATRIZ":
            mat_warshall = self.vertex_matrix.copy()
            matrix_graph = self
        else:
            # Se a representação for lista, cria um grafo de matriz para fazer a operação
            matrix_graph = Graph(self.directed, self.weighted, "MATRIZ")
            for vertex in self.vertex_list.keys():
                matrix_graph.add_vertex(vertex)

            for vertex in self.vertex_list.keys():
                for neighbor in self.vertex_list[vertex].keys():
                    matrix_graph.add_edge(vertex, neighbor, self.vertex_list[vertex][neighbor])
            
            # Atribui a matriz do grafo de lista a variável mat_warshall
            mat_warshall = matrix_graph.vertex_matrix.copy()

        # Algoritmo de Warshall
        for k in range(len(mat_warshall)):
            for i in range(len(mat_warshall)):
                for j in range(len(mat_warshall)):
                    mat_warshall[i][j] = mat_warshall[i][j] or (mat_warshall[i][k] and mat_warshall[k][j]) 

        # Cria Novo Grafo com a matriz de Warshall
        Warshall = Graph(matrix_graph.directed, matrix_graph.weighted, "MATRIZ")
        for vertex in matrix_graph.array_name.keys():
            Warshall.add_vertex(vertex)
        
        # Cria um dicionario com o nome dos vertices equivalente pro indice
        index_name = {}
        for vertex, index in matrix_graph.array_name.items():
            index_name[str(index)] = vertex

        for i in range(len(matrix_graph.vertex_matrix)):
            for j in range(len(matrix_graph.vertex_matrix)):
                if mat_warshall[i][j] != None:
                    Warshall.add_edge(index_name[str(i)], index_name[str(j)], mat_warshall[i][j])

        return Warshall
    
    def eulerian_test(self):
        # Se for direcionado, verifica se o grau de entrada é igual ao grau de saída e se é conectado
        if self.directed == True:
            for vertex in self.vertex_list.keys():
                if self.indegree(vertex) != self.outdegree(vertex):
                    return False
            if self.isConnected():
                return True

        # Se não for direcionado, verifica se o grau de todos os vértices é par e se é conectado
        else:
            if self.isConnected():
                for vertex in self.vertex_list.keys():
                    if self.degree(vertex) % 2 != 0:
                        return False
                return True
            return False
        
    def distribution_of_degree(self):
        degrees = []

        if self.representation == "LISTA":
            vertices = list(self.vertex_list.keys())
        elif self.representation == "MATRIZ":
            vertices = list(self.array_name.keys())

        for vertex in vertices:
            degrees.append(self.degree(vertex))

        plt.hist(degrees, bins=range(min(degrees), max(degrees) + 1), alpha=0.7, edgecolor='black', color='blue', linewidth=2)
        plt.title('Distribution of Degrees')
        plt.xlabel('Degree')
        plt.ylabel('Frequency')

        plt.savefig("degree_distribution.png")

    def __str__(self):

        idx_vertex = 0
        string_1 = ""
        string_2 = ""
        string_representation = "Nós: "
        #verificar se é matriz ou lista antes de printar
        if self.representation == "LISTA":

            for i in self.vertex_list.keys():

                string_1 += f"{i}({idx_vertex}), "
                string_2 += f"{i}({idx_vertex}): "

                for j in self.vertex_list[i].keys():

                    string_2 += f"{j}, "

                idx_vertex+=1

                string_2 = string_2[0:-2]+"\n"

            string_representation += string_1[0:-2]
            string_representation += "\nArestas(listas de adjacências):\n"
            string_representation += string_2
            
            #return f"Grafo {self.representation} {self.vertex_list}" ####
            
            return string_representation
        
        elif self.representation == "MATRIZ":

            for i in self.array_name.keys():

                string_1 += f"{i}({self.array_name[i]}), "
                string_2 += f"{i}({self.array_name[i]}): "

                for j in self.vertex_matrix[self.array_name[i]]:
                    
                    if j == None:

                        j = 0

                    string_2 += f"{j} "
                
                idx_vertex+=1
                string_2 += "\n"
            
            string_representation += string_1[0:-2]
            string_representation += "\nArestas(matriz):\n"
            string_representation += string_2

            return string_representation
                
            #return f"{self.vertex_matrix}\n Vértices e index {self.array_name}"

if __name__ == "__main__":
 
                    #DIRECTED  WEIGHT = false
    Grafo_lista = Graph(False, True, "LISTA")

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
        print("UPDATED")  ###
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
    path, cost, t = Grafo_lista.djikstra("A", "D")

    print(f"Caminho entre A e D{path} com peso {cost} e tempo de {t} segundos")

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

    if Grafo_lista.add_edge("D", "B", 2):
        print("Criado aresta") ###
    else:
        print("Não criado aresta") 

    print(Grafo_lista)

    print(f"MST = {Grafo_lista.prim()}")


    ####### fim lista #########################################################################
    print("-----------------  MATRIZ ----------------------")

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

    a, b, t = Grafo_matriz.djikstra("A", "B")

    print(f"Caminho entre A e D{a} com peso {b} com tempo de {t} segundos")

    print(Grafo_matriz)


    if Grafo_matriz.remove_vertex("B"):
        print("Vértice removido")
    else:
        print("Não foi possível remover o vértice") ###

    print(Grafo_matriz)

    p, c, t = Grafo_matriz.djikstra("A", "B")

    print(f"Caminho entre A e B {p} com peso {c} e tempo de conclusão {t} segundos")

    p, c, t = Grafo_matriz.djikstra("A", "A")

    print(f"Caminho entre A e A {p} com peso {c} e tempo de conclusão {t} segundos")

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

    print(Grafo_matriz.get_weight("A", "C"))

    print(f"MST = {Grafo_matriz.prim()}")

    print("---------------------------")
    grafo_teste_warshall = Graph(True,False,"MATRIZ")
    
    grafo_teste_warshall.add_vertex("A")
    grafo_teste_warshall.add_vertex("B")
    grafo_teste_warshall.add_vertex("C")
    grafo_teste_warshall.add_vertex("D")
    grafo_teste_warshall.add_vertex("E")

    grafo_teste_warshall.add_edge("A", "B", 1)
    grafo_teste_warshall.add_edge("B", "C", 1)
    grafo_teste_warshall.add_edge("E", "D", 1)
    grafo_teste_warshall.add_edge("B", "E", 1)

    print(grafo_teste_warshall)               
    print("Warshall:")
    print(grafo_teste_warshall.warshall())

    grafo_teste_warshall.distribution_of_degree()