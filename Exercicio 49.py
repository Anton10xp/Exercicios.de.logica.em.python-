#Exercicio 49-
#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

cont = 0
soma = 0
for i in range(6):
    cont = cont + 1
    numero = int(input("Digite o {}° número inteiro: ".format(cont)))

    if numero % 2 == 0:
        soma = soma + numero
    
print("A soma dos números impares é: {}".format(soma))

  