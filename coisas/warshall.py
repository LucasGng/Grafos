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
                mat_warshall[i][k] = mat_warshall[i][k] or (mat_warshall[i][j] and mat_warshall[j][k]) 

    return mat_warshall

if __name__ == '__main__':
    # criando o grafo com 4 vertices
    mat = constroi_matriz(4)

    ix_A = 0
    ix_B = 1
    ix_C = 2
    ix_D = 3

    # cria arestas (direcionado)
    mat[ix_A][ix_B] = 1 # A -> B
    mat[ix_A][ix_C] = 1 # A -> C
    mat[ix_B][ix_C] = 1 # B -> C
    mat[ix_C][ix_D] = 1 # C -> D
    mat[ix_D][ix_B] = 1 # D -> B

    print(mat)
    print("warshall:")
    print(warshall(mat))

#print(constroi_matriz(5))

