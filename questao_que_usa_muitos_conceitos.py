"""Questão 1
Aluno: Leonam Yoshiaki Albuquerque Tsutsumi 2026001839
Aluno: Marcelo Rafael Nascimento Faro 2026001848
Aluno: Arthur Reis da Silva 2026001893
"""
"""
Escreva um programa que receba números inteiros do usuário até que o valor -1 seja
digitado (o valor -1 serve apenas como flag de parada, e não deve ser processado).
Em seguida, o programa deve:
· Armazenar apenas os números positivos digitados em uma lista.
· Calcular e exibir a média aritmética dos valores armazenados.
· Identificar e exibir o maior e o menor número presente na lista, além da
quantidade de números pares digitados.
"""
numeros = []

while True:
    valor = int(input("Digite um número inteiro (-1 para sair): "))

    if valor == -1:
        break

    if valor > 0:
        numeros.append(valor)

if numeros:
    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    qtd_pares = len([x for x in numeros if x % 2 == 0])

    print(f"Números válidos: {numeros}")
    print(f"Média: {media:.1f}")
    print(f"Maior valor: {maior} | Menor valor: {menor}")
    print(f"Quantidade de pares: {qtd_pares}")
else:
    print("Nenhum número positivo foi digitado.")