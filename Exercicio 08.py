#Exercicio 08
#Faça um programa que cauque o quanto de dolar você pode comprar(obs: o Dolar no dia de hoje esta custando: 5,00)
reais = float(input("Digite o quanto de Dinheito em Reais você tem: "))

dolar = reais / 5.00

print("Com {:.2f} reais você pode comprar {:.2f} dollares ".format(reais,dolar))
