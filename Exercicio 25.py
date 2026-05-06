#Exercicio 25-
#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input("Digite uma fase: ")).strip( ).upper( )

print("A letra A apareceu {} vezes ".format(frase.count("A")))
print("A posição que a letra A aparecu primeiro foi: {} ".format(frase.find("A") + 1 ))

print("A posição que a letra A apareceu por ultimo foi: {} ".format(frase.rfind("A") + 1 ))