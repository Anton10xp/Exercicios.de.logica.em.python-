#Melhore o jogo do DESAFIO 027 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint

pc = randint(0,10)

print("Vou pensar em um número entre 0 e 10 adivinhe... ")

acertou = False

tentativas = 0

while not acertou:
    resposta = int(input("Número errado, Tente novamente: "))
    
    tentativas = tentativas + 1

    if resposta == pc:
        acertou = True

print("Você acertou! ")
print(f"O número escolhido foi {pc}")
print(f"Você prescisou de {tentativas} para acertar!")


print("Fim! ")
