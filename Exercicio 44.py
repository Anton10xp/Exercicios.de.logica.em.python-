#Exercicio 44-
#Crie um programa que faça o computador jogar Jokenpô com você.

import random

opçoes = ["pedra", "papel", "tesoura"]

jogador = str(input("Digite: Pedra, Papel ou Tesoura:  "))

pc = random.choice(opçoes)

if jogador == pc:
    print("Empate")

elif (jogador == "pedra" and pc == "tesoura") or \
        (jogador == "papel" and pc == "pedra") or \
        (jogador == "tesoura" and pc == "papel"):
    print("Você venceu!")

else:
    print("Você perdeu!")