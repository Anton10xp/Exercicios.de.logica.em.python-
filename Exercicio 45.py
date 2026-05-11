#Exercicio 45-
# Faça um programa que mostre na tela uma contagem regressiva de 10 até 0

from time import sleep

for contador in range(10, -1, -1):
    print(contador)
    sleep(0.5)