"""
Questão 2.
Aluno: Leonam Yoshiaki Albuquerque Tsutsumi 2026001786
Aluno: Arthur Reis Da Silva 2026001893
Aluno:  Marcelo Rafael Nascimento Faro 2026001848
Escreva um programa que calcule e imprima os 20 primeiros termos da série de
Bergamacci. Nesta série, os três primeiros termos são 1 e os próximos são a soma
dos três anteriores.
Exemplo: dos 7 primeiros termos: 1, 1, 1, 3, 5, 9, 17

"""
termo1 = 1
termo2 = 1
termo3 = 1
print(termo1)
print(termo2)
print(termo3)

for i in range(1,18):
     bergamacci= termo1 + termo2 + termo3
     termo1 = termo2
     termo2 = termo3
     termo3 = bergamacci
     print(bergamacci)

