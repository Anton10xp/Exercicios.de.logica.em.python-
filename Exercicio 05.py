#Exercicio 05
#Faça um programa que leia um numero e mostre o seu dobro, triplo e raiz quadrada
import math
n = int(input("Digite um número: "))

dobro = n * 2
triplo = n * 3
raiz = math.sqrt(n)

print("O dobro de {} é {} ".format(n,dobro))
print("O triplo de {} é {} ".format(n,triplo))
print("A raiz de {} é {} ".format(n,raiz))
