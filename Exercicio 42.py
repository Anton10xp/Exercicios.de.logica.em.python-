#Exercicio 42-
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

import math

peso = float(input("Digite o seu peso em (KG): "))

altura = float(input("Digite a sua altura em (METROS): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Quem tem o IMC = {:.2f} está Abaixo do Peso! ".format(imc))

elif imc > 18.5 and imc <= 25:
    print("Quem tem o IMC = {:.2f} está no Peso Ideal! ".format(imc))

elif imc > 25 and imc <= 30:
    print("Quem tem o IMC = {:.2f} está com Sobrepeso! ")

else:
    print("Quem tem o IMC = {:.2f} está com Obesidade Mórbida! ".format(imc))