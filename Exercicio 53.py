#Exercício 54- 
#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import datetime

anoatual = datetime.now().year

cont = 0
contmaior = 0
contmenor = 0


for i in range(7):
    cont = cont + 1
    nascimento = int(input(f"Digite o ano de nascimento da {cont}° pessoa: "))

    idade = anoatual - nascimento


    if idade >= 18:
        contmaior = contmaior + 1


    else:
        contmenor = contmenor + 1

print("São {} pessoas maiores de idade".format(contmaior))
print("São {} pessoas menores de idade".format(contmenor))