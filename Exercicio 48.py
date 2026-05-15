#Exercicio 48-
#Faça uma tabuada de um número que o úsuario escolher usando o for como laço.

numero = int(input("Digite um número inteiro: "))

for i in range(0,10):
    print(f"A tabuada de {numero} x {i} = {numero * i} ")