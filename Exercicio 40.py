#Exercicio 40-
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

from datetime import datetime

anoatual = datetime.now().year

nascimento = int(input("Digite o seu ano de nascimento: "))

idade = anoatual - nascimento

if idade <= 9:
    print("Quem tem {} anos Mirim ".format(idade))

elif idade <= 14:
    print("quem tem {} anos Infatil ".format(idade))

elif idade <= 19:
    print("Quem tem {} anos é Júnior ".format(idade))

elif idade <= 25:
    print("Quem tem {} anos é Sênior ".format(idade))

else:
    print("Quem tem {} anos é ".format(idade))
