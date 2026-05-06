#Exercicio 21-
# Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input("Digite o seu nome completo: ")).strip( )

print("Seu nome em maiusculo é {} ".format(nome.upper( )))
print("Seu nome em minusculo é {} ".format(nome.lower( )))
print("O seu nome tem ao todo {} letras ".format(len(nome)- nome.count(" ")))
print("O seu priemrio nome tem {} ".format(nome.find(" ")))
