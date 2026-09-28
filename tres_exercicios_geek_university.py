"""
1. Faça um programa que leia um número inteiro e imprima-o
2. Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.
3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.
"""
numero_inteiro = int(input("Informe o numero: "))
print(numero_inteiro)
print("Informe tres numeros e vou somar eles")
n1 = int(input("INnforme o numero 1: "))
n2 = int(input("INnforme o numero 2: "))
n3 = int(input("INnforme o numero 3: "))
soma_dos_3 = (n1 + n2 + n3)
print(soma_dos_3)
n1_quadrado = n1 ** 2
n2_quadrado = n2 ** 2
n3_quadrado = n3 ** 2
soma_dos_quadrados = n1_quadrado + n2_quadrado + n3_quadrado
print(f"{n1_quadrado} {n2_quadrado} {n3_quadrado} {soma_dos_quadrados}")
