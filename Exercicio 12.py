#Exercicio 12
#Faça 1 programa que leia um salario de 1 funcionario e caucule o novo salario com:
# 15% de aumento

salario  = float(input("Digite o seu salario: "))

novosalario = salario + (salario * 15 /100)

print("O salario que antes era {:.2f} R$ agora é {:.2f} R$ ".format(salario,novosalario))
