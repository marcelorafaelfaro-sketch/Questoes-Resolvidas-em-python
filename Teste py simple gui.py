import PySimpleGUI as sg
def calculo_doido():
    numero = float(input("Informe o numero a ser multiplicado: "))
    numero_que_vai_encima = int(input("Informe o valor que será elevado: "))
    multipli = numero ** numero_que_vai_encima
    print(multipli)
    return calculo_doido()

sg.theme("Reddit")
desenho_legal = [
    [sg.Text("Nome: "), sg.InputText(), ],
    [sg.Submit(), sg.Button("Sair")],
    [sg.Button("OPERAÇÃO")],
    [sg.Button("OI")],[sg.Checkbox("CLIQUE EM MIM")]
]
janela_aberta = sg.Window("Teste de PYSIMPLEGUI",layout= desenho_legal, font=("Helvetica",24))
while True:
    evento, valores = janela_aberta.read()
    if evento == "Sair" or evento == sg.WIN_CLOSED:
        janela_aberta.close()
        break

    elif evento == ("OI"):
        print(" SIX SEVEN ")
        sg.popup("SIX SEVEN")
    elif evento == "OPERAÇÃO":
        sg.popup(calculo_doido())
        break

janela_aberta.close()


