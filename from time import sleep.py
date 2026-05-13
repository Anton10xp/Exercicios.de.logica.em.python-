LINHAS = 4
COLUNAS = 7


matriz = [0] + LINHAS

print(matriz)

for i in range(LINHAS):
    matriz [i] = [0] * COLUNAS


for i in range(LINHAS):
    for j in range(COLUNAS):
        matriz[i][j] = i + j   
    

print(matriz)