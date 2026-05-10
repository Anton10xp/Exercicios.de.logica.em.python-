#Exercicio 41-
#Refaça o DESAFIO 034 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print("Os segmentos digitados PODEM forma um Triângulo! ")

    if r1 == r2 == r3:
        print("O tipo desse triângulo é EQUILÁTERO! ")

    elif r1 != r2 != r3 != r1:
        print("O tipo desse triângulo é ISÓSCELES! ")

    else:
        print("O tipo desse triângulo é Escaleno!")
    

else:
    print("Os segmentos digitados acima NÃO podem formar um triângulo! ")