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
questao6 = 0
for numeroquestao6 in range(1,6):
    ngeral = int(input("Informe o numero: "))
    if ngeral > ngeral:
       questao6 += ngeral
    print(questao6)
# maior = max(ngeral)
# menor = min(ngeral)
print(f"O maior é ")
