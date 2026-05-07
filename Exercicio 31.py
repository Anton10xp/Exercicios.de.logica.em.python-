#Exercicio 31-
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Digite o ano que você quer ver: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print("O ano {} é BIXESTO ".format(ano))
else:
    print("O ano {} não é BIXESTO! ".forat(ano))
print("Fim do programa! ")
