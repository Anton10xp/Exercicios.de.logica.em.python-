#Exercicio 27-
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

pc = randint(0,5)

print("Vou pensar em um número entre 0 e 5 adivinhe... ")

sorteado = int(input('Adivinhe o número que eu pensei: '))

if sorteado == pc:
    print("Acertou, parabéns! ")
    print("O número escolhido foi {} ".format(pc))

else:
    print("Errou! O número escolhido foi {} ".format(pc))



