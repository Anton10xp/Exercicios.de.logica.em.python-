#exercicio 55-

 #Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.



total_idades = 0

homem_mais_velho_nome = ""
homem_mais_velho_idade = -1

mulheres_menos_20 = 0


for i in range(1, 5):
    print(f"\n--- Pessoa {i} ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()


    total_idades = total_idades + idade

    if sexo == "M":
        if idade > homem_mais_velho_idade:
            homem_mais_velho_idade = idade
            homem_mais_velho_nome = nome


    if sexo == "F":
        if idade < 20:
            mulheres_menos_20 = mulheres_menos_20 + 1


media = total_idades / 4

print("Média de idade do grupo:", media, "anos")

if homem_mais_velho_nome == "":
    print("Nenhum homem foi cadastrado.")
else:
    print("Homem mais velho:", homem_mais_velho_nome, "-", homem_mais_velho_idade, "anos")

print("Mulheres com menos de 20 anos:", mulheres_menos_20)