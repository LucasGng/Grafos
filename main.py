from fraxos.parser import Parser

if __name__ == "__main__":

    # def load_from_pajek(filename):
    #     with open(filename, 'r') as file:
    #         for line in file:
    #             print('gay')
    # grafo = load_from_pajek("grafo_matriz.net")

    parser = Parser("coisas/grafo_lista.net")
    parser.build_graph()

    print(parser.graph)
    
