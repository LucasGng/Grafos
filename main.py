from fraxos.parser import Parser

if __name__ == "__main__":

    parser = Parser("arquivos/grafo_lista.net") # nome do arquivo a ser lido
    parser.build_graph()

    print(parser.graph)
    
