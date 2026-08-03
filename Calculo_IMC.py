#Programa que calcula o IMC
print("Olá irei calcular seu IMC e irei informar a situação de seu peso")
altura =float(input("Informe sua altura, em metros: "))
peso =float(input("Informe seu peso, em quilogramas: "))
IMC =  (peso/(altura**2))
print(f"O valor do seu IMC é {IMC:.2f}")
if (IMC < 20):
    print("Você está Abaixo do peso")
elif (IMC >=20 and IMC <= 25):
    print("Você está no peso ideal")
else:
    print("Você está em sobrepeso")