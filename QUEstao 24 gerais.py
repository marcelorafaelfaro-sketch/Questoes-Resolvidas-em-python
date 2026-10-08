"""
Escreva um programa que gere os 20 primeiros termos da série de Fibonacci.
Nesta série, os dois primeiros termos são 1 e os próximos são a soma dos dois
anteriores. Veja: 1, 1, 2, 3, 5, 8, 13
--------------------------------------------

Escreva um programa que calcule a soma dos números pares, menores que 1000,
da série de Fibonacci.
"""
#fibonaci = 0
termo1 = 1
termo2 = 1
pares_somados = 0
print(termo1)
print(termo2)
while termo1 < 1000:
    fibonaci = termo1 + termo2
    termo1 = termo2
    termo2 = fibonaci
    print(fibonaci)
    if termo1 % 2 == 0:
        pares_somados += termo1


        if termo1 % 2 == 0:
            pares_somados += 1

print(f"O resultado é {pares_somados}")