#Exercicio 49-
#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contador = 0
for i in range(1,7):
    numero = (int(input("Digite o {}° valor: ".format(i))))
    if numero % 2 == 0:
        soma = soma + numero
        contador = contador + 1
print("você me informou {} numeros pares e soma entre eles é igual a: {} ".format(contador,soma))

