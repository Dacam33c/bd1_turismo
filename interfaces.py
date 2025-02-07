import PySimpleGUI as sg

# Menu Principal
def menu():
    layout = [[sg.Text("Selecione o que deseja fazer")],
              [sg.Button("Cadastrar Pessoa"), sg.Button("Cadastrar Hotel")],
              [sg.Button("Sair")]]

    window = sg.Window("BD", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Sair":
            break
        elif event == "Cadastrar Pessoa":
            window.hide()  # Esconde a tela principal
            cadastrar_pessoa()
            window.un_hide()  # Reexibe a tela principal ao voltar
        elif event == "Cadastrar Hotel":
            window.hide()
            cadastrar_hotel()
            window.un_hide()

    window.close()

# Tela Inicial de Cadastro de Pessoas
def cadastrar_pessoa():
    layout = [[sg.Text("Cadastro de Pessoa")],
              [sg.Text("CPF", size=(15,1)), sg.InputText(key='cpf', size=(20,1))],
              [sg.Text("Nome", size=(15,1)), sg.InputText(key='nome', size=(20,1))],
              [sg.Text("Data de nascimento", size=(15,1)), sg.InputText(key='nascimento', size=(20,1))],
              [sg.Text("Endereço", size=(15,1)), sg.InputText(key='endereço', size=(20,1))],
              [sg.Text("Telefone", size=(15,1)), sg.InputText(key='telefone', size=(20,1))],
              [sg.Radio("Guia", "tipo_usuario", key="guia", default=True, size=(10,1)), sg.Radio("Cliente", "tipo_usuario", key="cliente", default=False, size=(10,1))],
              [sg.Button("Avançar"), sg.Button("Voltar")]]
    
    window = sg.Window("Cadastrar Pessoa", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Avançar":
            window.hide()
            
            if values['guia']:
                cadastrar_guia()
            elif values['cliente']:
                pass

            window.un_hide()

    window.close()

#Tela Cadastro de Pessoa 
def cadastrar_guia():
    layout = [[sg.Text("Guia")],
              [sg.Button("Voltar")]]

    window = sg.Window("Cadastrar Guia", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Salvar":
            sg.popup(f"Guia {values['guia']} cadastrado!")

# Tela Cadastro de Hotel
def cadastrar_hotel():
    layout = [[sg.Text("Cadastro de Hotel")],
              [sg.Text("Nome", size=(10,1)), sg.InputText(key='nome', size=(20,1))],
              [sg.Text("CNPJ", size=(10,1)), sg.InputText(key='cnpj', size=(20,1))],
              [sg.Text("Tipo", size=(10,1)), sg.InputText(key='tipo', size=(20,1))],
              [sg.Text("Endereço", size=(10,1)), sg.InputText(key='endereço', size=(20,1))],
              [sg.Button("Salvar"), sg.Button("Voltar")]]
    
    window = sg.Window("Cadastrar Hotel", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Salvar":
            sg.popup(f"Hotel {values['nome']} cadastrado!")

    window.close()

#menu()