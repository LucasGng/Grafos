from pygraph.grafo import Graph

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


print("----------------------------")

grafo_teste_warshall_list = Graph(True,False,"LISTA")

grafo_teste_warshall_list.add_vertex("A")
grafo_teste_warshall_list.add_vertex("B")
grafo_teste_warshall_list.add_vertex("C")
grafo_teste_warshall_list.add_vertex("D")
grafo_teste_warshall_list.add_vertex("E")

grafo_teste_warshall_list.add_edge("A", "B", 1)
grafo_teste_warshall_list.add_edge("B", "C", 1)
grafo_teste_warshall_list.add_edge("E", "D", 1)
grafo_teste_warshall_list.add_edge("B", "E", 1)

print(grafo_teste_warshall_list)               
print("Warshall:")
print(grafo_teste_warshall_list.warshall())

#grafo_teste_warshall.distribution_of_degree()

print("----------------------------")
print(grafo_teste_warshall_list)  
grafo_teste_warshall_list.save_to_pajek("grafo_teste_warshall_list.net")
newgrafo = Graph(filename="grafo_teste_warshall_list.net")
print(newgrafo)
print("----------------------------")


print("----------------------------")
grafo_teste = Graph(True,True,"MATRIZ")

grafo_teste.add_vertex("A")
grafo_teste.add_vertex("B")
grafo_teste.add_vertex("C")
grafo_teste.add_vertex("D")
grafo_teste.add_vertex("E")

grafo_teste.add_edge("A", "B", 3)
grafo_teste.add_edge("B", "C", 5)
grafo_teste.add_edge("E", "D", 6)
grafo_teste.add_edge("B", "E", 2)

print(grafo_teste)
grafo_teste.save_to_pajek("grafo_teste.net")
newgrafo = Graph(filename="grafo_teste.net")
print(newgrafo)
print("----------------------------")
# grafo_teste_warshall_list.distribution_of_degree()

