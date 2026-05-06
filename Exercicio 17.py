#Exercicio 17
#Faça um programa que leia um angulo, e mostre o valor do seno, cosseno e a tangente desse angulo
import math

angulo = float(input("Digite Angulo: "))

seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print("O angulo de {} tem o Seno de {:.2f} ".format(angulo,seno))
print ("O angulo de {} tem o Cosseno de {:.2f} ".format(angulo,cos))
print("O angulo de {} tem a Tangente de {:.2f} ".format(angulo,tang))

print("Fim do programa! ")