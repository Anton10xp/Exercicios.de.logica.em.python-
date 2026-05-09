#Exercicio 38-
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nascimento = int(input("Digite o seu ano de nascimento: "))

idade = 2026 - nascimento

anodoalistamento = nascimento + 18

print("Quem nasceu em {} tem {} anos em 2026".format(nascimento, idade))

if idade == 18:
    print("Você tem que se alistar imediatamente! ")

elif idade > 18:
    saldo = idade - 18
    print("Você deveria ter se alista ha: {} anos ".format(saldo))

elif idade < 18:
    saldo = 18 - idade
    print("Você irá se alistar daqui ha {} anos ".format(saldo))