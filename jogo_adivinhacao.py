import random


print("=== Jogo de Adivinhação ===")
print("Estou pensando em um número de 1 a 100.")
print("Tente adivinhar! A cada tentativa, eu vou te dar uma dica.\n")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = input("Digite seu palpite: ")

    if not palpite.isdigit():
        print("Digite apenas números! Tente novamente.\n")
        continue

    palpite = int(palpite)
    tentativas += 1

    if palpite < 1 or palpite > 100:
        print("O número está entre 1 e 100. Tente um número dentro desse intervalo.\n")
    elif palpite < numero_secreto:
        print("Dica: o número secreto é MAIOR que isso!\n")
    elif palpite > numero_secreto:
        print("Dica: o número secreto é MENOR que isso!\n")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto}!")
        print(f"Você precisou de {tentativas} tentativa(s).")
        break