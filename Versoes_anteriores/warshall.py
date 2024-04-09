def constroi_matriz(n_vertices):
    return [[0] * n_vertices for _ in range(n_vertices)]

def copia_matriz(matriz):
    n_vertices = len(matriz)
    copia = constroi_matriz(n_vertices)

    for i in range(n_vertices):
        for j in range(n_vertices):
            copia[i][j] = matriz[i][j]

    return copia

def pega_peso(matriz, v_a, v_b):
    return matriz[v_a][v_b]

def warshall(matriz):
    # matriz de fechamento transitivo
    mat_warshall = copia_matriz(matriz)
    
    for k in range(len(mat_warshall)):
        for i in range(len(mat_warshall)):
            for j in range(len(mat_warshall)):
                mat_warshall[i][j] = mat_warshall[i][j] or (mat_warshall[i][k] and mat_warshall[k][j]) 

    return mat_warshall

def show(matriz):
    for i in matriz:
        print(i)

if __name__ == '__main__':
    # criando o grafo com 4 vertices
    mat = constroi_matriz(5)

    A = 0
    B = 1
    C = 2
    D = 3
    E = 4

    # cria arestas (direcionado)
    # mat[A][B] = 1 # A -> B
    # mat[A][C] = 1 # A -> C
    # mat[B][C] = 1 # B -> C
    # mat[C][D] = 1 # C -> D
    # mat[D][B] = 1 # D -> B

    mat[A][B] = 1 # A -> B
    mat[B][E] = 1 # B -> E
    mat[B][C] = 1 # B -> C
    mat[E][D] = 1 # E -> D

    show(mat)
    print("warshall:")
    show(warshall(mat))

#print(constroi_matriz(5))

