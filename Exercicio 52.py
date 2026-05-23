#Exercício 53-
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite a frase: ")).strip()

palavras = frase.split()

tudojunto = "".join(palavras)

reverse = ""

for i in range(len(tudojunto) - 1, -1, -1):
    reverse = reverse + tudojunto[i]

print("O inverso da Frase {} é {}".format(tudojunto, reverse))

if reverse == tudojunto:
    print("A frase é Palindromo!")

else:
    print("A frase não é palindromo!")

print("Fim!")