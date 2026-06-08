from turtledemo.round_dance import stop

print("Bem vindo a calculadora de média e faltas.")

primeira_nota = float(input("Informe a primeira nota: "))

segunda_nota = float(input("Informe a segunda nota: "))

numeros_faltas = int(input("Informe o número de faltas: "))

media = (primeira_nota + segunda_nota)/2
# if (numeros_faltas >= 10):
#     print("Você está reprovado.")
print(f"Sua média foi {media}")
if (numeros_faltas >= 10):
    print("ALUNO REPROVADO POR FALTAS")
elif(media >= 7):
    print("Parábens, você passou!")
elif(media <= 5):
    print("Infelizmente você não passou...")

else:
    print("Infelizmente você não passou...")
