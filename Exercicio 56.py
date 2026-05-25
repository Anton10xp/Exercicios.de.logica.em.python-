#Exercicio 56-

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Digite o seu sexo [M/F]: ")).upper()

while sexo != "M" and sexo != "F":
    print("Sexo invalido digite M (para masculino) ou F (para feminino) !")
    sexo = str(input("Digite um sexo valido [M/F]:  ")).upper()

if sexo == "M":
    print("Sexo registrado: Masculino")

elif sexo == "F":
    print("Sexo registrado: Feminino")