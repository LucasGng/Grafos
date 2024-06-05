from pygraph.grafo import Graph
import pandas as pd
import time


grafo_teste = Graph(False,True,"LISTA")

grafo_teste.add_vertex("A")
grafo_teste.add_vertex("B")
grafo_teste.add_vertex("C")
grafo_teste.add_vertex("D")
grafo_teste.add_vertex("E")

grafo_teste.add_edge("A", "B", 3)
grafo_teste.add_edge("B", "C", 5)
grafo_teste.add_edge("E", "D", 6)
grafo_teste.add_edge("B", "E", 2)


# --------------------------------------------------------
        
        
arquivo_csv = 'arquivos/tabela_artigos_limpa.csv'

df = pd.read_csv(arquivo_csv, sep=',')
grafo_teste_csv = Graph(False,True,"LISTA")

for i in df['NOMES_AJUSTADOS']:
    nomes = eval(i)
    grafo_teste_csv.array_to_graph(nomes)


# 1. =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# start_time = time.time()

# degr_centrality = grafo_teste_csv.degree_centrality()
# ceytroem_ordenado = dict(sorted(degr_centrality.items(), key=lambda item: item[1]))
# print(ceytroem_ordenado)

# end_time = time.time()
# execution_time = end_time - start_time
# print("Tempo de execução degree_centrality():", execution_time, "segundos")


# 2. =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# start_time = time.time()

# extract_comp = grafo_teste_csv.component_extraction()
# print(len(extract_comp[0]))

# end_time = time.time()
# execution_time = end_time - start_time
# print("Tempo de execução component_extraction():", execution_time, "segundos")


# 3. =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# start_time = time.time()

# grafo_teste_csv.distribution_of_degree()

# end_time = time.time()
# execution_time = end_time - start_time
# print("Tempo de execução distribution_of_degree():", execution_time, "segundos")


# 4. =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# start_time = time.time()

# degr_centrality = grafo_teste_csv.degree_centrality()
# degr_centrality_ord = dict(sorted(degr_centrality.items(), key=lambda item: item[1]))
# print(degr_centrality_ord)

# end_time = time.time()
# execution_time = end_time - start_time
# print("Tempo de execução degree_centrality():", execution_time, "segundos")


# 5. =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# start_time = time.time()

# between_centrality = grafo_teste_csv.betweenness_centrality()
# between_centrality_ord = dict(sorted(between_centrality.items(), key=lambda item: item[1]))
# print(between_centrality_ord)

# end_time = time.time()
# execution_time = end_time - start_time
# print("Tempo de execução betweenness_centrality():", execution_time, "segundos")


# 6. =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# start_time = time.time()

# close_centrality = grafo_teste_csv.closeness_centrality()
# close_centrality_ord = dict(sorted(close_centrality.items(), key=lambda item: item[1]))
# print(close_centrality_ord)

# end_time = time.time()
# execution_time = end_time - start_time
# print("Tempo de execução closeness_centrality():", execution_time, "segundos")



# 7. =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# start_time = time.time()

# eccentricity = grafo_teste_csv.get_eccentricity()
# print(eccentricity)

# end_time = time.time()
# execution_time = end_time - start_time
# print("Tempo de execução get_eccentricity():", execution_time, "segundos")



# 8. =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# start_time = time.time()

# print(f"diametro: {grafo_teste_csv.get_diameter()}")

# end_time = time.time()
# execution_time_diameter = end_time - start_time
# print("Tempo de execução get_diameter(): ", execution_time_diameter, "segundos")

# -------------------------

# start_time = time.time()

# print(f"diametro: {grafo_teste_csv.get_radius()}")

# end_time = time.time()
# execution_time_radius = end_time - start_time
# print("Tempo de execução get_redius(): ", execution_time_radius, "segundos")
# print(f"Total: {execution_time_diameter + execution_time_radius}")


# 9. =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# start_time = time.time()

# between_centrality_edges = grafo_teste_csv.edge_betweenness_centrality()
# between_centrality_edges_ord = dict(sorted(between_centrality_edges.items(), key=lambda item: item[1]))
# print(between_centrality_edges_ord)

# end_time = time.time()
# execution_time = end_time - start_time
# print("Tempo de execução edge_betweenness_centrality():", execution_time, "segundos")


# 10. =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# start_time = time.time()

# print(grafo_teste_csv.average_geodesic_distances())

# end_time = time.time()
# execution_time = end_time - start_time
# print("Tempo de execução:", execution_time, "segundos")


# 11. =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# start_time = time.time()

# extract = grafo_teste_csv.component_extraction()
# grafo_teste_csv.girvan_newman(4)

# end_time = time.time()
# execution_time = end_time - start_time
# print("Tempo de execução girvan_newman():", execution_time, "segundos")


