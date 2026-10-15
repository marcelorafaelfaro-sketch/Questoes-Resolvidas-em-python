"""
4. Filtro de Números Pares
Escreva um programa que percorra os números de $1$ a $30$
O programa deve imprimir na tela apenas os números pares
e, ao final, mostrar quantos números pares foram encontrados no total.
"""
numeroquestao4 = 0
for i in range(1,31):
    if i% 2 == 0:
        numeroquestao4 += 1
        print(i)
print(f"Foram encontrados {numeroquestao4} de pares entre {range(1,31)}")
"""
5. Média de $N$ Notas de um Aluno
O programa deve perguntar ao usuário quantas notas ele deseja cadastrar (ex: $3$). 
Em seguida, use um laço para ler cada nota, somá-las e, no final, calcular a média.
Se a média for maior ou igual a $7.0$, exiba "Aprovado", senão exiba "Reprovado".
"""
# numeroquestao5 = 0
#
# n = int(input("Informe quantas notas voce tem: "))
# for quantas_vezes in range(1,n+1):
#     nota = float(input("Informe o valor das suas notas:"))
#     numeroquestao5 += nota
# media = (numeroquestao5/n)
# print(f"Sua media é igual a {media:.2f}")
# if media >= 7:
#     print("VOCE PASSOU")
# if media < 7:
#     print("REPROVOU")

"""
6. Maior e Menor Número
Peça para o usuário digitar $5$ números inteiros (um por um através de um laço).
O programa deve descobrir e exibir no final qual foi o maior e qual foi o menor número digitado.
"""
# maior = 0
# menor = 0
# questao6 = 0
# for numeroquestao6 in range(1,6):
#     ngeral = float(input(f"Informe o {numeroquestao6} numero: ").replace(",", "."))
#     #ngeral = float(input(f"Informe o {numeroquestao6} numero: ").replace(".",","))
#     if ngeral == 1:
#         maior = ngeral
#         menor = ngeral
#     else:
#         if ngeral > maior:
#             maior = ngeral
#         if ngeral < menor:
#             menor = ngeral
#
#
# # maior = max(ngeral)
# # menor = min(ngeral)
# print(f"O maior é {maior}")
# print(f"O menor é {menor}")

"""
7. Validação de Senha (Loop Indefinido)
Crie um programa que defina uma senha correta guardada em uma variável (ex: senha_correta = "python123").
O programa deve pedir a senha ao usuário continuamente usando o laço while.
Enquanto ele errar a senha, exiba a mensagem "Senha incorreta, tente novamente!".
Quando ele finalmente acertar, exiba "Acesso liberado!" e encerre o programa.
"""
# senha_questao_7 = "amosilvia"
# while True:
#     questao7 = str(input("Informe a senha: "))
#     if questao7 == senha_questao_7:
#         print("ACESSO LIBERADO.")
#         break
#     else:
#         print("ACESSO NEGADO.")

"""
8. Caixa Eletrônico (Soma até parar)
Crie um programa que leia vários números digitados pelo usuário até que ele digite o valor 0 (que serve como condição de parada).
Enquanto o número for diferente de zero, vá acumulando o total. Quando o usuário digitar 0
o programa deve encerrar o laço while e exibir a soma de todos os números digitados antes do zero.
"""
# numeroquestao8 = 0
# termocarregado = 0
# while True:
#     numeroquestao8 = int(input("Informe o numero: "))
#     termocarregado += numeroquestao8
#     if numeroquestao8 == 0:
#         break
#
# print(termocarregado)

"""
9. Lista de Compras sem Duplicatas
Crie um programa que use um laço for para pedir ao usuário o nome de $5$ produtos de mercado.
O programa deve guardar os produtos em uma lista Python,
mas atenção: se o produto já existir na lista, não adicione novamente
(avise "Produto já adicionado!"). No final, exiba a lista completa de compras na tela.
"""

# comprasdoJJ = []
# for zeze in range(1,6):
#     ascomprasdoJJ = input("Informe todos os produtos: ")
#     comprasdoJJ.append(ascomprasdoJJ)
#     #if ascomprasdoJJ == ascomprasdoJJ:
#         #print("ESSE ITEM JA ESTA NO CARRINHO")
# if ascomprasdoJJ == ascomprasdoJJ:
#     print("ESSE ITEM JA ESTA NO CARRINHO")
# print(comprasdoJJ)
#---------------------------------versao gemini-----------
comprasdoJJ = []

for zeze in range(1, 6):
    ascomprasdoJJ = input(f"Informe o produto {zeze}: ")

    if ascomprasdoJJ in comprasdoJJ:
        print("ESSE ITEM JÁ ESTÁ NO CARRINHO")
    else:
        comprasdoJJ.append(ascomprasdoJJ)

print("Lista final:", comprasdoJJ)




