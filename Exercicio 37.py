#Exercicio 37-
#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if n1 > n2:
    print("O Primeiro valor: {} é maior que o segundo valor: {} ".format(n1,n2))

elif n1 > n2:
    print("O primeiro valor: {} é menor que o segundo valor: {} ".format(n1,n2))
    
else:
    print(f"O numero {n1} é igual ao numero {n2}")
