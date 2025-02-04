import PySimpleGUI as sg

def menu():
    layout = [[sg.Text("Selecione o que deseja fazer")],
              [sg.Button("Cadastrar Pessoa"), sg.Button("Cadastrar Hotel")]]

    window = sg.Window("BD", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break

    window.close()
menu()