"""
crie um script que peça para o usuario digitar o nome de 5 bebidas, armezenando as informções em uma lista
exiba esses elementos em ordem alfabetica, usando laço for
"""
bebidas = []
print("Forneça o nome das  5 bebidas")
for i in range(5):
    bebida = str(input("Informe a bebida: ")).title()
    bebidas.append(bebida)
bebidas.sort()
print("Bebidas escolhidas.")
for bebida in bebidas:
    print(bebida)


