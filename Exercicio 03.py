#Exercicio 03
#Faça um programa que leia algo pelo teclado e mostre na telao seu:
#tipo primitivo, e todas as informações possíveis sobre ela.

algo = input("Digite algo: ")

print("O tipo primitivo é: ",type(algo))
print("Ele só tem espaços? ", algo.isspace( ))
print("É um número? ", algo.isnumeric( ))
print("É alfabético? ", algo.isalpha( ))
print("É alfanumerico? ", algo.isalnum( ))
print("Está em maiusculo? ", algo.isupper( ))
print("Está em minusculo? ", algo.islower( ))
print("Está capitalizada? ", algo.istitle( ))