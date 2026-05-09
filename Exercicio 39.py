#Exercicio 39-
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))

media = (n1+n2) / 2

if media < 5:
    print("A media entre {} e {} é {}. Aluno REPROVADO! ".format(n1,n2,media))

elif media > 5 and media < 6.9:
    print("A media entre {} e {} é {}. Aluno de RECUPERAÇÃO! ".format(n1,n2,media))

else:
    print("A media entre {} e {} é {}. Aluno Aprovado! ".format(n1,n2,media))