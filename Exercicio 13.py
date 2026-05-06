#Exercicio 13
#Faça um programa que leia uma temperatura em celsius e converta ela para °F
c = float(input("Digite a temperatura em °C: "))

f = (9 * c / 5) + 32

print("A temperatura {} °C convertida em °F é {} ".format(c,f))