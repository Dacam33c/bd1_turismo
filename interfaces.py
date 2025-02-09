import PySimpleGUI as sg
import mysql.connector
from auxiliar import *

# Menu Principal
def menu(conexao, cursor):
    layout = [[sg.Text("Selecione o que deseja fazer")],
              [sg.Button("Cadastrar guia"), sg.Button("Cadastrar Cliente")],
              [sg.Button("Cadastrar Destino"),sg.Button("Cadastrar Localização")],
              [sg.Button("Cadastrar Hotel"),sg.Button("Cadastrar Quarto")],
              [sg.Button("Cadastrar Ponto Turístico")],
              [sg.Button("Cadastrar Transporte")],
              [sg.Button("Cadastrar foto")],
              [sg.Button("Sair")]]

    window = sg.Window("BD", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Sair":
            break
        elif event == "Cadastrar guia":
            window.hide()  # Esconde a tela principal
            cadastrar_guia()
            window.un_hide()  # Reexibe a tela principal ao voltar
        elif event == "Cadastrar Hotel":
            window.hide()
            cadastrar_hotel()
            window.un_hide()
        elif event == "Cadastrar Destino":
            window.hide()
            cadastrar_destino()
            window.un_hide()
        elif event == "Cadastrar Cliente":
            window.hide()
            cadastrar_cliente()
            window.un_hide()
        elif event == "Cadastrar Localização":
            window.hide()
            cadastrar_Localizacao()
            window.un_hide()
        elif event == "Cadastrar Quarto":
            window.hide()
            cadastrar_quarto()
            window.un_hide()
        elif event == "Cadastrar Ponto Turístico":
            window.hide()
            cadastrar_turistico()
            window.un_hide()
        elif event == "Cadastrar Transporte":
            window.hide()
            cadastrar_transporte()
            window.un_hide()
        elif event == "Cadastrar Viagem":
            window.hide()
            cadastrar_viagem()
            window.un_hide()
        elif event == "Cadastrar foto":
            window.hide()
            cadastrar_imagem(conexao, cursor)
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
            
            conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="309320",
            database="turismo"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")
            
            pessoa = {'Pessoa' : [(values['cpf'],values['endereço'],values['nome'],values['nascimento'],values['telefone'])]}
            insertSql(pessoa,conexao)
            conexao.close()
            
            window.hide()
            
            if values['guia']:
                cadastrar_guia()
            elif values['cliente']:
                pass

            window.un_hide()

    window.close()

#Tela Cadastro de Pessoa 
def cadastrar_guia():
    layout = [[sg.Text("Cadastro de guia")],
              [sg.Text("CPF", size=(15,1)), sg.InputText(key='cpf', size=(20,1))],
              [sg.Text("Nome", size=(15,1)), sg.InputText(key='nome', size=(20,1))],
              [sg.Text("Data de nascimento", size=(15,1)), sg.InputText(key='nascimento', size=(20,1))],
              [sg.Text("Endereço", size=(15,1)), sg.InputText(key='endereço', size=(20,1))],
              [sg.Text("Telefone", size=(15,1)), sg.InputText(key='telefone', size=(20,1))],
              [sg.Text("Destino", size=(15,1)), sg.InputText(key='destino', size=(20,1))],
              [sg.Text("Preço", size=(15,1)), sg.InputText(key='preço', size=(20,1))],
              [sg.Button("Salvar"), sg.Button("Voltar")]]

    window = sg.Window("Cadastrar Guia", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Salvar":
            
            conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="309320",
            database="turismo"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")

            guia = {
                'Pessoa' : [(values['cpf'],values['endereço'],values['nome'],values['nascimento'],values['telefone'])],
                'Guia'   : [(values['cpf'], values['destino'], values['preço'])]
                }
            insertSql(guia,conexao)
            
            conexao.close()
            
            sg.popup(f"guia {values['nome']} cadastrado!")

    window.close()

def cadastrar_cliente():
    layout = [[sg.Text("Cadastro de cliente")],
              [sg.Text("CPF", size=(15,1)), sg.InputText(key='cpf', size=(20,1))],
              [sg.Text("Nome", size=(15,1)), sg.InputText(key='nome', size=(20,1))],
              [sg.Text("Data de nascimento", size=(15,1)), sg.InputText(key='nascimento', size=(20,1))],
              [sg.Text("Endereço", size=(15,1)), sg.InputText(key='endereço', size=(20,1))],
              [sg.Text("Telefone", size=(15,1)), sg.InputText(key='telefone', size=(20,1))],
              [sg.Text("Nome de usuário", size=(15,1)), sg.InputText(key='user', size=(20,1))],
              [sg.Text("Desconto", size=(15,1)), sg.InputText(key='desconto', size=(20,1))],
              [sg.Button("Salvar"), sg.Button("Voltar")]]

    window = sg.Window("Cadastrar cliente", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Salvar":
            
            conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="309320",
            database="turismo"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")

            cliente = {
                'Pessoa' : [(values['cpf'],values['endereço'],values['nome'],values['nascimento'],values['telefone'])],
                'Cliente'   : [(values['cpf'], values['user'], values['desconto'])]
                }
            insertSql(cliente,conexao)
            
            conexao.close()
            
            sg.popup(f"cliente {values['nome']} cadastrado!")

    window.close()

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
            
            conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="309320",
            database="turismo"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")

            hotel = {'Hotel' : [(values['cnpj'],values['tipo'],values['nome'],values['endereço'])]}
            insertSql(hotel,conexao)
            conexao.close()
            sg.popup(f"Hotel {values['nome']} cadastrado!")

    window.close()

def cadastrar_destino():
    layout = [[sg.Text("Cadastro de destino")],
              [sg.Text("Nome", size=(10,1)), sg.InputText(key='nome', size=(20,1))],
              [sg.Text("tipo", size=(10,1)), sg.InputText(key='tipo', size=(20,1))],
              [sg.Button("Salvar"), sg.Button("Voltar")]]
    window = sg.Window("Cadastrar destino", layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Salvar":
            
            conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="309320",
            database="turismo"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")

            destino = {'Destino' : [(values['tipo'],values['nome'])]}
            insertSql(destino,conexao)
            conexao.close()
            sg.popup(f"destino {values['nome']} cadastrado!")

    window.close()


def cadastrar_Localizacao():
    layout = [[sg.Text("Cadastro de localização")],
              [sg.Text("endereço", size=(10,1)), sg.InputText(key='endereço', size=(20,1))],
              [sg.Text("destino", size=(10,1)), sg.InputText(key='destino', size=(20,1))],
              [sg.Button("Salvar"), sg.Button("Voltar")]]
    window = sg.Window("Cadastrar localização", layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Salvar":
            
            conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="309320",
            database="turismo"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")

            loc = {'Localizacao' : [(values['endereço'],values['destino'])]}
            insertSql(loc,conexao)
            conexao.close()
            sg.popup(f"localização {values['endereço']} cadastrada!")

    window.close()

def cadastrar_quarto():
    layout = [[sg.Text("Cadastro de Quarto")],
              [sg.Text("CNPJ do hotel", size=(10,1)), sg.InputText(key='cnpj', size=(20,1))],
              [sg.Text("número do quarto", size=(10,1)), sg.InputText(key='numero', size=(20,1))],
              [sg.Text("preço", size=(10,1)), sg.InputText(key='preço', size=(20,1))],
              [sg.Text("capacidade", size=(10,1)), sg.InputText(key='capacidade', size=(20,1))],
              [sg.Button("Salvar"), sg.Button("Voltar")]]
    window = sg.Window("Cadastrar quarto", layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Salvar":
            
            conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="309320",
            database="turismo"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")

            quarto = {'Quarto' : [ ( values['numero'], values['cnpj'],values['preço'],values['capacidade'] ) ] }
            insertSql(quarto,conexao)
            conexao.close()
            sg.popup(f"quarto {values['numero']} cadastrado!")

    window.close()

def cadastrar_turistico():
    layout = [[sg.Text("Cadastro de Ponto turístico")],
              [sg.Text("nome", size=(10,1)), sg.InputText(key='nome', size=(20,1))],
              [sg.Text("preço", size=(10,1)), sg.InputText(key='preço', size=(20,1))],
              [sg.Text("destino", size=(10,1)), sg.InputText(key='destino', size=(20,1))],
              [sg.Button("Salvar"), sg.Button("Voltar")]]
    window = sg.Window("Cadastrar ponto turístico", layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Salvar":
            
            conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="309320",
            database="turismo"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")

            ponto = {'pontoTuristico' : [ ( values['nome'], values['preço'],values['destino'] )] }
            insertSql(ponto,conexao)
            conexao.close()
            sg.popup(f"ponto {values['nome']} cadastrado!")

    window.close()

def cadastrar_transporte():
    layout = [[sg.Text("Cadastro de Transporte")],
              [sg.Text("placa", size=(10,1)), sg.InputText(key='placa', size=(20,1))],
              [sg.Text("capacidade", size=(10,1)), sg.InputText(key='capacidade', size=(20,1))],
              [sg.Text("tipo", size=(10,1)), sg.InputText(key='tipo', size=(20,1))],
              [sg.Button("Salvar"), sg.Button("Voltar")]]
    window = sg.Window("Cadastrar ponto transporte", layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Salvar":
            
            conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="309320",
            database="turismo"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")

            transporte = {'transporte' : [ ( values['placa'], values['capacidade'],values['tipo'] )] }
            insertSql(transporte,conexao)
            conexao.close()
            sg.popup(f"transporte {values['placa']} cadastrado!")

    window.close()

def cadastrar_imagem(conexao, cursor):
    layout = [
        [sg.Text("Escolha uma imagem para enviar ao banco de dados")],
        [sg.InputText(key="-FILE-", enable_events=True), sg.FileBrowse("Selecionar", file_types=(("Imagens", "*.png;*.jpg;*.jpeg"),))],
        [sg.Button("Enviar"), sg.Button("Sair")]
    ]
    janela = sg.Window("Enviar imagem", layout)

    while True:
        evento, valores = janela.read()

        if evento == sg.WINDOW_CLOSED or evento == "Sair":
            break
        elif evento == "Enviar":
            caminho_imagem = valores["-FILE-"]
            if caminho_imagem:
                nome_imagem = caminho_imagem.split("/")[-1]  # Obtém apenas o nome do arquivo
                salvar_imagem(nome_imagem, caminho_imagem, conexao, cursor)
            else:
                sg.popup("Por favor, selecione uma imagem! ⚠")
    janela.close()

#menu()