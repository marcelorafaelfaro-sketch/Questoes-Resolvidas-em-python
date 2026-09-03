"""
Escreva um programa que receba dois números inteiros e calcule a soma dos
números pares entre eles.
Exemplo : suponha que os números sejam 100 e 200 , você tem que
calcular a soma dos pares entre 100 e 200.
"""
numero1 = int(input("Informe o primeiro numero: "))
numero2 = int(input("Informe o segundo numero: "))
soma = 0
for i in range(numero1,numero2+1):
    if i % 2 ==0:
        soma = soma + i
        #print(f"{soma}")
print(f"{soma}")