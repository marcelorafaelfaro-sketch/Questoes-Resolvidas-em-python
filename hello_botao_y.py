# Programa que exibe "Hello World" quando o usuário apertar a tecla "y"

tecla = input('Aperte a tecla "y" e pressione Enter: ')

if tecla.lower() == 'y':
    print('Hello World')
else:
    print('Você não apertou a tecla "y".')
