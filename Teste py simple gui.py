import PySimpleGUI as sg
sg.theme("Reddit")
desenho_legal = [
    [sg.Text("Nome: "), sg.InputText(), ],
    [sg.Submit(), sg.Button("Sair")],
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


janela_aberta.close()