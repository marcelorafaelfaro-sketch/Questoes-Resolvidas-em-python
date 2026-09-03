"""
Desafio: Escreva um programa que receba a hora de saída de um estudante do estágio (ex: 18) e o tempo estimado de trânsito até a UFRA em minutos (ex: 35).
 O programa deve calcular se ele chegará a tempo para a aula das 18:30.

Saída esperada: Exibir "Chegará a tempo!" ou "Aviso: Chegará atrasado em X minutos!".
"""

#hora_saindo = input(int("Olá informe que horas você está saindo da sua casa e eu irei calcular se chegará atrasado ou não: "))
velocidade = float(input("Informe a velocidade,em km/h, com que você vai se deslocar até la: "))
espaco = float(input("Informe a distancia,em km, até chegar la: "))
tempo = (espaco / velocidade) * 60
if tempo > 30:
    print(f"Você chegará atrasado, levará {tempo:.2f} minutos.")
else:
    print(f"Voce chegará a tempo, levará {tempo:.2f}minutos")