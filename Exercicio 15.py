#Exercicio 15
#Faça um programa que leia um numero real no teclado e mostre
#Sua porção inteira
numero = float(input("Digite um numero real: "))

import math

print("O número digitado foi {} e a sua porção inteira é {} ".format(numero,math.trunc(numero)))

print("Fim do Programa! ")
