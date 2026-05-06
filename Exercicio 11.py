#Exercicio 11
#Faça um programa que leia um preço de um produto e calcule o seu novo valor com
# 5% de desconto
produto = float(input("Digite o valor do produto: "))

desconto = produto - (produto * 5 / 100)

print("O produto que antes era {} R$ com o desconto será {} R$ ".format(produto,desconto))
