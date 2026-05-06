#Exercicio 04
#Faça um programa que leia um numero e mostre o seu antecessor e sucessor
numero = int(input("Digite um numero: "))

sucessor  = numero + 1
antecessor = numero - 1

print("O sucessor de ",numero," é", sucessor)
print("O antecessor de {} é {} ".format(numero,antecessor))