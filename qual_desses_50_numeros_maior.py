import random
maior = 0
for i in range(1,51):
    aleatorio = random.randint(1,50)
    print(aleatorio)
    if aleatorio > maior:
        maior = aleatorio

print(f"O maior numero daqui é o {maior}")