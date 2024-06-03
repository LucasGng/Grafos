# from pygraph.grafo import Graph

class Parser():
    def __init__(self, file):
        # Atributo com o nome do arquivo
        self.file = file 
        # Atributo para salvar as linhas numa lista
        self.lines = []
        # Atributo para salvar as configurações do grafo  (direcionado, ponderado e representação)
        self.configs = []
        # Atributo para salvar as partes do grafo (vértices e arestas)
        self.parts = []
        # Atributo para gerar o grafo
        self.graph = None
        # Atributo para salvar os vértices nomeados
        self.named_vertices = {}

    

    def read_file(self):
        # Metodo para abrir o arquivo
        with open(self.file, "r") as file:
            self.lines = file.readlines()


    def parse_configs(self):
        # Metodo para extrair as configurações do grafo (direcionado, ponderado e representação)

        for line in self.lines:
            if line.startswith("%"):
                info = [line.replace("%", "").strip().split("=")]
                extract = []
                for i in info:
                    extract.append({i[0]: i[1].capitalize()})
                self.configs.append(extract.pop())
            

        # print(self.configs)
            

    def parse_parts(self):
        # Metodo para extrair as partes do grafo (vértices e arestas)
        
        for i in range(len(self.lines)):
            if self.lines[i].startswith('*'):
                part = []
                for j in range(i+1, len(self.lines)):
                    if not self.lines[j].startswith('*'):
                        part.append(self.lines[j].replace("\n", "").strip().split(" "))
                    else:
                        break
                self.parts.append(part)

        # print(self.parts)
        


    def setup_graph(self):
        # Metodo para criar o grafo
        # print(self.configs)

        print(self.configs)

        self.graph = Graph(
            self.configs[0]['directed'],
            self.configs[1]['weighted'],
            self.configs[2]['representation'].upper()
        )
        

    def build_graph(self):
        # Metodo para construir o grafo de acordo com o arquivo

        try:
            self.read_file()
            self.parse_configs()
            self.setup_graph()
            self.parse_parts()
            

            self.named_vertices =  {v[0]: v[1] for v in self.parts[0]}
            print(self.named_vertices)

            for vertice in self.parts[0]:
                self.graph.add_vertex(vertice[1])

            for aresta in self.parts[1]:
                self.graph.add_edge(
                    self.named_vertices[aresta[0]],
                    self.named_vertices[aresta[1]],
                    int(aresta[2]) if self.configs[1]['weighted'] == 'True' else '0'
                )

   
        except:
            print("Erro ao construir grafo")