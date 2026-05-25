# Exercicio 54-
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for i in range(5):
    v = float(input(f"Digite o peso da {i+1}° pesso: "))

    pesos.append(v)

maior = pesos[0]
menor = pesos[0]

for i in pesos:
    if i > maior:
        maior = i

print("O maior peso foi de: {}".format(maior))


for i in pesos:
    if i < menor:
        menor = i

print("O menor peso foi de: {}".format(menor))