#teste de funçoes que eu to aprendendo no boson
from pyparsing.ai.show_best_practices import __main__

#from RAIZ_QUADRADA import resultado


def calculo_mega_complexo(a,b):
    return (a ** 2 + 2*a*b + b**2)
a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
c = calculo_mega_complexo(a,b)
print(f"O valor, usando {a} e {b}, é igual a {c}")
def divisao(h,j,k):
     return 1*k + 2*j + 3*h

h = 1
j = 34
k = 6
#retorno = divisao(h,j,k)
print(divisao(h,j,k))
def quadrados(vals):
    valores = []
    for a in vals:
        valores.append(a **2)
    return valores

novos_valores = []
print("Informe os valores, informe -1 pra parar.")
while True:

    numeros = int(input("INFORME: "))
    if numeros == -1:
        break
    if numeros > 0:
        novos_valores.append(numeros)

resultado = quadrados(novos_valores)
print(f"Aqui está {resultado}")
# while True:
#     try:
#         nome = int(input("informe seu numero: "))
#         if nome = int:
#     except ValueError:
#         (print("Digite somente numeros."))
