linhas = 4
colunas = 5

matriz = [1] * linhas

for i in range(linhas):
    matriz = [0] * colunas    
    
    
    for i in range(linhas):
        for j in range(colunas):
            matriz[i][j] = i + j

for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j], end= " ")
    
    print( )
