#Exercicio 33-
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o seu salario: "))

if salario >= 1250.00:
    aumento = salario + (salario * 10 /100)
    print("O seu novo salário com 10% de aumento é {:.2f} ".format(aumento))
else:
    aumento = salario + (salario * 15 /100)
    print("O seu novo salario com 15% de aumento é {:.2f} R$".format(aumento))