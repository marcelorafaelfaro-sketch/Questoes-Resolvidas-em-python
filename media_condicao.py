#programa que analisa se o aluno passou ou nao!
print("Irei fazer a media de 3 notas.")
n1 = float(input("escreva o valor do valor 1: "))
n2 = float(input("escreva o valor do valor 2: "))
n3 = float(input("escreva o valor do valor 3: "))
media = (n1 + n2 + n3)/3
print (f"Sua media é {media}")
if (media >= 6):
    print("Meus parabéns!,voce passou!")
else:
    print ("Infelizmente voce nao atingiu a nota minima.")