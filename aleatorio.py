import random

# valor = random.randint(1,100)
# print(valor)
print("20 NUMEROS ALEATORIOS, NA FAIXA DE 1 A 100")
for i in range(20):
    n = random.randint(1,100)
    print(f"Aqui está seu número: {n}")

lista = [1,-1,0,10,11,12,13,-14,2,3,4,5,6,7,67]
escolha = random.choice(lista)
print(f"O seu numero é,baseado na lista escolhida: {escolha}")