import math as M
l = M.pi
print("VOLUME DO CILINDRO.")
valor_cilindro_raio = float(input( "Informe valor do raio do cilindro: "))
valor_cilindro_altura = float(input("Informe valor da altura do cilindro: "))
Fatoriado = int(input("Informe o valor: "))

area_do_cilindro = (l * valor_cilindro_raio**2 * valor_cilindro_altura)
print(f"O volume do cilindro é {area_do_cilindro:.1f} ")
print("UMA BRINCADEIRA, AQUI O FATORIAL DO VALOR QUE VOCE OBTEVE")
fat = M.factorial(Fatoriado)
print(fat)