print("irei calcular o desconto a partir da quantidade de roupas compradadas")
roupas = int(input("Informe quantas roupas você comprou: "))
total = float(input("Informe o preço da sua compra: "))
if (roupas <= 5):
    print("Você recebeu um desconto de 3%")
    desconto1 = (total * (1-3/100))
    print (f"Sua compra foi de {desconto1}")
elif (roupas <= 10 ):
        print("Você recebeu um desconto de 5%")
        desconto2 = (total * (1-5/100))
        print (f"Sua compra foi de {desconto2:.2f}")
else:
    desconto3 = (total * (1-7/100))
    print(f"Sua compra foi de {desconto3:.2f}")

