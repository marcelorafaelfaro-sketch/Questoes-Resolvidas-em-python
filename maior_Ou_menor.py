# Escreva um programa que receba três números inteiros e informe qual deles é o
#maior.
print("OLA ME INFORME 3 NUMEROS E EU DIREI QUAL DELES É MAIOR")
N1 = int(input("Informe o numero1:"))
N2 = int(input("Informe o numero2:"))
N3 = int(input("Informe o numero3:"))
if (N1 > N2):
    print(f"O numero {N1} é o maior de todos")
elif (N2 > N2):
    print(f"O numero {N2} é o maior de todos")
else:
    print(f"O maior numero é o {N3}")

#Escreva um programa que aceite uma frase como entrada e informe o
#numero de vogais presentes na frase.
print("Irei calcular quantas vogais tem a sua frase\n")
frase = input("Informe a frase: ").lower()
contador = 0

for letra in frase:
    if letra in "aeiouáéíóú":
        contador += 1
print(f"Sua frase tem {contador}")
