# numero = int(input("Informe o numero e eu irei contar a partir dele até 100: "))
# while (numero <=99):
#     print(numero)
#     numero += 1
# print (numero)
#EXEMPLO DE MEDIA USANDO FOR E IN
#CONSEGUI OTIMIZAR O METODO PRA CONSEGUIR QUANTAS VARIAVEIS O USUARIO PEDIR
# numeros = int(input("Informe quantas variaveis teram: "))
# for i in range(numeros):
#     input(f"Informe n{i+1}: ")
# media_dos_termos = (range(i)/i)
# print(f"O resultado é {media_dos_termos}")


#TESTE PARA LAÇO WHILE FOR
# while True:
#     nome = input("Informe seu nome, ou aperte x para fechar: ")
#     if (nome == "x" or nome == "X"):
#         print("TCHAU")
#         break
#     print(f"Olá, {nome}, tenha um bom dia!")
# print(f"Até logo")


#TESTE PARA LAÇO FOR I IN
# meu_nome = "Marcelo"
# for letra in meu_nome:
#     print(letra)

#
# for numero in range(20,1,-1):
#     print(numero*2)
# nome = input("Informe seu nome por favor: ")
# for i in range(1,10):
#     print(f"{i+1},{nome}")

#LAÇO FOR I IN PORÉM USANDO EXCLUSÃO DE ITENS ESPECIFICOS
# itens_do_meu_quarto = ("PC", "Celular", "Cama","Mesa")
# for item in itens_do_meu_quarto:
#     if item == "Cama":
#         continue
#     if item == "Mesa":
#         continue
#     print(item)

# #Exemplo de laço for e in, juntos!
# for contador_ext in range(1,6):
#     print(f"\nOlá, [{contador_ext}]")
#     for contador_inter in range(5,0,-1):
#         print(f"Fala {contador_inter}")
# print("FIM")
#

import random
for a in range(1,7):
    print(f"\nConjunto [{a}]")
    for b in range(5):
        numero_aleatorio = random.randint(1,100)
        print(f"O resultado é {numero_aleatorio}")
