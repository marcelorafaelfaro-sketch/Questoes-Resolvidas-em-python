""""
Escreva um programa para calcular 1/2 + 2/3 + 3/4 +...+ n/n +1 com uma
determinada entrada n pelo console (n>0).
Exemplo: Se o seguinte n for fornecido como entrada para o programa: 5
Então, a saída do programa deverá ser: 3.55

"""
contador = 0
quantas_vezes = int(input("Informe quantas vezes será feito a operação: "))
for i in range(1,quantas_vezes + 1):
    contador += i/(i+1)
    #contador += operacao
    print(f'Aqui está {contador:.2f}')
