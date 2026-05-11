#Exercicio 44-
#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

from time import sleep

itens = ("Tesoura","Papel","Pedra")

pc = randint(0,2)

opçoes = int(input("Digite a Opção que você deseja:\n" \
"OPÇÃO (0): PEDRA\n" \
"OPÇÃO (1): TESOURA\n" \
"OPÇÃO (2): PEDRA\n" \
"Digite:  "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)

print("O computador escolheu {} ".format(itens[pc]))
print("O jogador escolheu {} ".format(itens[opçoes]))

if pc == 0:
    if opçoes == 0:
        print("EMPATE!")
    elif opçoes == 1:
        print("JOGADOR VENCEU!")
    elif opçoes == 2:
        print("COMPUTADOR VENCEU!")
    else:
        print("Jogada INVÁLIDA! ")

elif pc == 1:
   
    if opçoes == 0:
       print("EMPATE!") 
    elif opçoes == 1:
        print("JOGADOR VENCEU!")
    elif opçoes == 2:
        print("COMPUTADOR VENCEU!")
    else:
        print("Jogada INVÁLIDA! ")

elif pc == 2:
    if opçoes == 0:
        print("EMPATE!")         
    elif opçoes == 1:
        print("JOGADOR VENCEU!") 
    elif opçoes == 2:
        print("COMPUTADOR VENCEU!")
    else:
        print("Jogada INVÁLIDA! ")
