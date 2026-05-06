#Exercicio 07
#Faça um programa que leia um valor em metros e converta ele em:
#Todas as outras medidas possiveis

m = int(input("Digite um valor em metros: "))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print("{} metros é igual a {} km ".format(m,km))
print(f" {m} metros é igual a {hm} Hm ")
print("{} metros é igual a {} Dam ".format(m,dam))
print(f" {m} metros é igual a {dm} Dm ")
print(f" {m} metros é igual a {cm} Cm ")
print(f" {m} metros é igual a {mm} Mm ")

#OBS (Fiz os Prints de duas formas(Mas pelo fato de eu mostrar que sei fazer das duas formas.)