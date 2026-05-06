#Exercicio 14
#Faça um programa que pergunte quantos km o carro andou e a quatidade de dias que o carro foi alugado
#calcule o preço a pagar sabendo que o carro custa 60 reais por dia e 0.15 centavos por km rodado

dias = int(input("Digite o tanto de dias que o carro ficou alugado: "))
km = int(input("Digite o tanto de Km que você percorru: "))

valorfinal = (dias * 60) + (km * 0.15)

print("O total a se pagar é de {} R$ ".format(valorfinal))
