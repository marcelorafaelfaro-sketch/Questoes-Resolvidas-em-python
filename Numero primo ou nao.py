"""
Escreva um programa que receba um número e informe se ele é primo.
Número Primo éaquele que só é divisível por 1 e por ele mesmo.

--------------------------------------------------------------

Escreva um programa que exiba os números primos no intervalo [100, 200], além
da soma destes números.
"""
# numero = int(input("Informe o numero e direi se ele é primo ou não: "))
# achar_primo = 0
# for i in range(1, numero+1):
#     if numero % i == 0:
#         achar_primo += 1
#
# if achar_primo == 2:
#     print("Esse numero é primo")
# else:
#     print("Nao é primo")
#------------------OUTRA QUESTAO--------------------------------
numero = 100
SOMAR_primos = 0
while numero <= 200:
    achar_primo = 0
    for i in range(1, numero + 1):
     if numero % i == 0:
        achar_primo += 1

    if achar_primo == 2:
        SOMAR_primos += numero
        print(f"Esse numero é primo {numero}")
    numero += 1

print(f"A soma de todos os primos no intervalo é: {SOMAR_primos}")



    # for i in range(100,200+1):
    #     if numero % 2 == 0:
    #         achar_primo += 1
    #         print(achar_primo)
    # if achar_primo == 2:
    #     print("Esse numero é primo")
    # else:
    #     print("Nao é primo")


