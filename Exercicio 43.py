#Exercicio 43-
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

preco = float(input("Digite o valor da compra: "))

opçoes = int(input("Digite a opção que deseja realizar o pagamento:\n" \
"OPÇÃO (1): À Vista pix / Dinheiro / Cheque\n" \
"OPÇÃO (2): À Vista no cartão: 5% de Desconto\n" \
"OPÇÃO (3): No cartão em ATÉ 2x (sem juros)\n" \
"OPÇÃO (4): No Cartão em 3x ou mais com (20 % de juros)\n"))

if opçoes == 1:
    desconto = (preco * 10) / 100
    preçofinal = preco - desconto
    print("Sua compra de {:.2f} R$ fica {:.2f} R$ (Com 10 % de desconto)".format(preco,preçofinal))

elif opçoes == 2:
    desconto = (preco * 5) / 100
    preçofinal = preco - desconto
    print("A sua compra de {:.2f} R$ fica {:.2f} R$ (Com 5% de desconto)".format(preco,preçofinal))

elif opçoes == 3:
    parcela = preco / 2
    print("A sua compra de {:.2f} R$ fica 2x de {:.2f} ".format(preco,parcela))

else:
    juros = (preco * 20) / 100
    preçofinal = preco + juros
    print("A sua compra de {:.2f} fica {:.2f} (Com 20% de Juros) ".format(preco,preçofinal))

print("FIM")