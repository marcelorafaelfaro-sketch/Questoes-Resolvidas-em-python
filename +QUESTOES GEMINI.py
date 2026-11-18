"""
Conceito: Fatiamento de strings ([::-1]), padronização de caracteres e condicionais
Crie um programa que receba uma palavra ou frase, remova os espaços e caracteres especiais,
e verifique se ela é um palíndromo
(lê-se da mesma forma de trás para a frente, como "arara" ou "socorram me subi no onibus em marrocos").

"""
# palindromo = input("Informe a palavra: ").lower()
# print(palindromo)
# versao_texto_limpo = palindromo.replace(" ","")
# print(versao_texto_limpo)
# texo_inver = versao_texto_limpo[::-1]
# print(texo_inver)
# if versao_texto_limpo == texo_inver:
#     print(f"A palavra {versao_texto_limpo} é um palindromo")
# else:
#     print(f"Sua palavra |{versao_texto_limpo}| não é palindromo")
#for letra in palindromo:

"""
Sequência de Fibonacci
Conceito: Laço while ou for, atribuição múltipla e atualização simultânea de variáveis.
Enunciado: Solicite ao usuário um número inteiro $N$ e exiba os primeiros $N$ termos da sequência de Fibonacci
(0, 1, 1, 2, 3, 5, 8, 13).
"""
#fibonaci = int(input("Informe o numero e irei colocar ele na sequencia de fibo: "))
# ate_onde_ir = int(input("Informe até onde deve ir: "))
# termo1 = 1
# termo2 = 1
# for i in range(0,ate_onde_ir):
#     fibonaci = termo1 + termo2
#     termo1 = termo2
#     termo2 = fibonaci
#     print(fibonaci)

"""
1. Manipulação de Carrinho (Listas)
Crie um programa que inicie com uma lista vazia de produtos.
Permita que o usuário adicione 3 produtos à lista.
Em seguida, peça ao usuário para digitar o nome de um produto para remover. 
Se o produto estiver na lista, remova-o e exiba a lista atualizada;
caso contrário, exiba uma mensagem avisando que o produto não foi encontrado.


"""
# while True:
#     compras = []
#     print("---COMPRAS---")
#     print("INFORME 3 ITENS.")
#     compras.append(input("Informe o item1: "))
#     compras.append(input("Informe o item2: "))
#     compras.append(input("Informe o item3: "))
#     removedor = input("Qual item deseja remover? ")
#     if removedor in compras:
#         compras.remove(removedor)
#         print("Item removido com sucesso")
#         print(compras)
#     else:
#         print("NENHUM ITEM ENCONTRADO")
    #print(compras)

"""
Filtro de Pares e Ímpares (Listas)
Objetivo: Preenchimento condicional de listas em laços.
Peça ao usuário 10 números inteiros.
Armazene os números pares em uma lista chamada pares
e os ímpares em uma lista chamada impares
Ao final, exiba o conteúdo de ambas as listas e o tamanho de cada uma usando len().
"""
#
# pares = []
# impares = []
# print("Informe 10 valores inteiros.")
# for quantidade in range(1,11):
#     numero = int(input("Informe os numeros: "))
#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)
# print(pares)
# print(impares)
# print(len(pares))
# print(len(impares))

"""
Registrador de Posições Geográficas (Tuplas)
Objetivo: Criação, exibição e desempacotamento de tuplas
Crie uma estrutura onde o usuário informa o nome de uma cidade
a latitude e a longitude.Armazene a latitude e longitude em uma tupla coordenadas = (lat, lon)
Ao final, exiba uma mensagem formatada
extraindo os dados diretamente da tupla por desempacotamento.

"""
#
# nome_cidade = input("Informe o nome da cidade: ")
# lat = float(input("INFORME A LATITUDE: "))
# lon = float(input("INFORME A LONGITUDE: "))
# cordenadas = (lat, lon)
# lat, lon = cordenadas
# print(f"A cidade {nome_cidade} tem a latitude como {lat} e a longitude como {lon}")
"""
4.Analisador de Notas e Desempenho (Listas + Tuplas)
Peça 4 notas de um aluno e guarde-as em uma lista.
Crie uma função ou bloco de código que calcule o menor valor,
o maior valor e a média das notas. Retorne esses três resultados agrupados dentro de uma única tupla
(menor, maior, media) e exiba-os na tela.
"""
# notas_alunos = []
# for vezes in range(1,5):
#     nota = float(input("Informe a nota: "))
#     notas_alunos.append(nota)
#
# print(notas_alunos)
# minimo = min(notas_alunos)
# print(f"Aqui está o minimo de suas notas: {minimo}")
# maximo = max(notas_alunos)
# print(f"Aqui está o maximo de suas notas: {maximo}")
# media = sum(notas_alunos) / len(notas_alunos)
# print(f"Aqui está a media de suas notas: {media}")
# geral = (minimo, maximo, media)
# minimo, maximo, media = geral
# print(f"Aqui está seu geral {geral}")
"""
5. Relatório de Preços de Produtos (Lista de Tuplas)

Crie uma lista contendo 4 tuplas, onde cada tupla possui a estrutura ("Nome do Produto", preco)
Escreva um laço for que percorra essa lista e imprima um relatório formatado em colunas
(ex.: Teclado ....... R$ 150.00), exibindo no final qual é o produto mais caro da lista.
"""
itens =[
    ("Teclado",150),
    ("Mouse",50),
    ("Fone", 25),
    ("Tripé", 75)

]
print(itens)
print("Lista completa:")
print(itens)
print("\nFazendo a varredura:")
for produtinhos, valor in itens:
    print(f"O produto {produtinhos} custa R$ {valor},00")