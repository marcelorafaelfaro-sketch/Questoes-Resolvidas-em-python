import math
"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.

"""
n1 = int(input("Informe o valor do primeiro numero: "))
n2 = int(input("Informe o valor do segundo numero: "))
if n1 > n2:
    print(f"o {n1} e maior que {n2}")
elif n1 == n2:
    print("Os numeros são iguais")
else:
    print(f"o {n2} e maior que {n1}")
n1_quadrado = int(input("Informe o numero pra eu ter a raiz quadrada dele: "))
if n1_quadrado > 0:
    print(math.sqrt(n1_quadrado))
elif n1_quadrado < 0:
    print("IMPOSSIVEL TER RAIZ REAL DE NUMEROS NEGATIVOS")

n_par_ou_impar = int(input("Informe um numero e direi se ele é par ou impar: "))
resultado = (n_par_ou_impar % 2)
if resultado == 0 :
    print(f"O seu {n_par_ou_impar} é par")
elif resultado != 0:
    print(f"Seu {n_par_ou_impar} é impar")
