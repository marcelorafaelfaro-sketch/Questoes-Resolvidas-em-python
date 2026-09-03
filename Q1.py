"""
Faça um programa para ler o valor de uma conta em um restaurante/Lanchonete,
depois disso o programa deve perguntar quanto em porcentagem você quer dar de
gorjeta, o programa ao final deve informar o total a ser pago e quanto desse total é
o valor da gorjeta.
Exemplo: Quanto foi sua conta: 100
Quanto você deseja dar de gorjeta, em porcentagem: 10
Total a ser pago: R$110 sendo R$10 de gorjeta
"""

print("OLA INFORME O VALOR DA SUA COMPRA E EM SEGUIDA O QUANTO QUER DAR DE GORJETA, EM %")
valor = int(input("Informe o valor da sua compra: "))
gorjeta_porcento = int(input("Informe o valor da gorjeta em porcentagem: "))
total_gorjeta = valor * (gorjeta_porcento/100)
print(f"Sua compra deu {valor} e você escolheu dar {gorjeta_porcento}% e ficou {total_gorjeta:.1f} de gorjeta")
