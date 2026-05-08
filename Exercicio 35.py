#Exercicio 35-
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salario: "))
anos = int(input("Digite em quantos anos você irá pagara a casa: "))

prestacao = valor / (anos * 12)
taxa = salario * 0.30

if prestacao <= taxa:
    print("O seu financiamento foi APROVADO! Valor da parcela: {:.2f} R$ / mês ".format(prestacao))
else:
    print("Infelizmente o seu financiamento NÃO foi aprovado! ")
