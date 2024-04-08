from fraxos.grafoh import Graph

class Parser():
    def __init__(self, file):
        self.file = file 
        self.lines = []
        self.configs = []
        self.parts = []
        self.graph = None
        self.named_vertices = {}

    

    def read_file(self):
        with open(self.file, "r") as file:
            self.lines = file.readlines()


    def parse_configs(self):
        for line in self.lines:
            if line.startswith("%"):
                info = [line.replace("%", "").strip().split("=")]
                extract = []
                for i in info:
                    extract.append({i[0]: i[1].capitalize()})
                self.configs.append(extract.pop())
            

        print("congigs", self.configs)
            

    def parse_parts(self):
        
        
        for i in range(len(self.lines)):
            if self.lines[i].startswith('*'):
                part = []
                for j in range(i+1, len(self.lines)):
                    if not self.lines[j].startswith('*'):
                        part.append(self.lines[j].replace("\n", "").strip().split(" "))
                    else:
                        break
                self.parts.append(part)

        print("self.parts", self.parts)
        


    def setup_graph(self):
        print(self.configs)

        self.graph = Graph(
            self.configs[0]['directed'],
            self.configs[1]['weighted'],
            self.configs[2]['representation'].upper()
        )

        
        print(self.configs[0]['directed'],
            self.configs[1]['weighted'],
            self.configs[2]['representation'].upper())
        

    def build_graph(self):

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

                
            try:
                self.graph.save_to_pajek('save_graph.net')
            except:
                print("Erro ao salvar grafo")

        except:
            print("Erro ao construir grafo")
