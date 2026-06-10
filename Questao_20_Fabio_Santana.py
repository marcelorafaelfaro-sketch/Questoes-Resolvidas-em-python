#20)Escreva um programa que exiba a soma dos números múltiplos de 7 no intervalo
#[100, 200].
numero = int(input("Informe o numero: "))
operacao = 0
for multiplo in range(1,201):
    if multiplo % numero != 0:
        operacao = operacao + multiplo
        print(f"{numero} - {multiplo}")


