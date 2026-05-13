#Calculando valores

linhas = 3
colunas = 3

matriz1 = [ [1,2,3],
            [4,5,6],
            [7,8,9],
            ]

matriz2 = [[7,8,7],
           [6,5,4],
           [32,5,1],
           ]

soma = [None] * linhas

for i in range(linhas):
    soma[i] = [None] * colunas

for i in range(linhas):
    for j in range(colunas):
        soma[i][j] = matriz1[i][j] + matriz2[i][j]

for i in range(linhas):
    for j in range(colunas):
        print(soma[i][j], end= " ")

    print( )