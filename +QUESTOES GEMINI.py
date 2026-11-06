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
compras = []
print("---COMPRAS---")
print("INFORME 3 ITENS.")
compras.append(input("Informe o item1: "))
compras.append(input("Informe o item2: "))
compras.append(input("Informe o item3: "))
removedor = input("Qual item deseja remover? ")
if removedor in compras:
    compras.remove(removedor)
    print("Item removido com sucesso")
    print(compras)
else:
    print("NENHUM ITEM ENCONTRADO")
#print(compras)