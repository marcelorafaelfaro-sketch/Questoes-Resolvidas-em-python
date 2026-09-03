"""
Faça um algoritmo para ler o ano de nascimento de uma pessoa e informar quantos
anos ela tem. Após isso, o algoritmo deve imprimir uma mensagem segundo a tabela
abaixo:
ABAIXO DE 18 ANOS = MENOR DE IDADE
DE 18 A 50 = MAIOR DE IDADE
MAIOR DE 50 = SENIOR
"""
while True:
    ano_de_nascimento = int(input("Informe a sua data de nascimento: "))
    idade = 2026 - ano_de_nascimento
#print(idade)
    if idade < 18:
        print(f"Você tem {idade} MENOR DE IDADE")
    elif idade > 18 and idade <= 50:
        print(f"Você tem {idade} MAIOR DE IDADE")
    else:
        print(f"Você tem {idade} SENIOR")