#Exercicio 10
#Faça um programa que calcule a area de uma parede e diga ao pintor quanto de tinta irá gastar (sabendo que cada litro de tinda pinta 2 metros quadrados)

altura = float(input("Digite a Altura da parede: "))
largura = float(input("Digite a Largura da parede: "))

area = altura * largura
tinta = area / 2

print("A area da parede é {} E será preciso pra pintar {} ".format(area,tinta))