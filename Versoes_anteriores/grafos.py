class Graph():

    def __init__(self, directed, weighted, representation):

        self.directed = directed #boolean
        self.weighted = weighted #boolean
        self.representation = representation #string?
        self.vertexList = [] #lista de vértices (nome)
        self.edgeList=[] #lista de arestas (nome)
    
    def ingrau(self, v_name): #vertex name

        counter = 0

        if self.directed == True: #se for direcionado é preciso verificar se a aresta sai do vértice
            for i in v_name.neighbors:

                if i.end == v_name:
                    counter+=1
        
        else:
            counter = len(v.neighbors) #em não direcionado ingrau e outgrau são iguais à quantidade de vizinhos

        return counter
    
    def add_vertex(self, name):

        if name in self.edgeList:
            return False
        else:
            self.edgeList.append(name)
            return True

    def check_vertex(self, name): #verifica se os vértices existem no grafo

        if name in self.vertexList:
            return True
        else:
            return False


    def check_edge(self, begin, end): #verfifica se exite arestas entre dois vértices desse grafo
        
        #mudar pq tá uma merda
        if(self.check_vertex(begin) and self.check_vertex(end) and end in [x[0] for x in begin.neighbors]):
            return True
        else:
            return True

class Vertex():

    def __init__(self, name):

        self.name = name
        self.neighbors = [] #tupla(linked list), de todos os vizinhos deste vértice  

    def create_edge(self, end, weight):

        self.neighbors.append((end,weight)) #mudar pra objeto?
        print(f"Edge created between {self.name} and {end} with weight {weight}!")
        
class Edge():

    def __init__(self, name, begin_v, end_v, weight): #nome, vetor de saida, vetor de chegada

        self.name = name
        self.begin_v = begin_v
        self.end_v = end_v
        self.weight = weight

if __name__ == "__main__":

    Grafo_lista = Graph(False, True, "Lista")

    #print(">> MENU DE OPÇÕES\n\n1.Criar Grafo\n2.Criar Vértice\n3.Verificar vértice")
    #search for vertex name in graph's vertexList, execute the according method based on that certain vertex