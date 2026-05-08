#Exercicio 36-
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input("Digite um numero inteiro: "))

conversor = int(input("Escolha a sua opção para conversão: " \
"(1)- BINARIO" \
"  (2)- OCTAL" \
"  (3)- HEXADECIMAL:   "
"    "))

if conversor == 1:
    print("O número {} em BINARIO é {} ".format(numero, bin(numero)[2:]))

elif conversor == 2:
    print("O número {} é OCTAL é {} ".format(numero, oct(numero)[2:]))

elif conversor == 3:
    print("O número {} em HEXADECIMAL é {} ".format(numero, hex(numero)[2:]))