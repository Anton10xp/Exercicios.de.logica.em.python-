#Exercicio 30
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input("Digite a distancia da viagem em KM: "))

if distancia <= 200:
    preço = distancia * 0.50
    print("O valor a se pagar na passagem é de {} R$".format(preço))

else:
    preço = distancia * 0.45
    print("O valor a se pagar na passagem é de {} R$".format(preço))

print("Fim do programa! ")
