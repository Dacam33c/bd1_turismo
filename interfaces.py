import PySimpleGUI as sg
import mysql.connector
from auxiliar import *
from views import *
import io
from PIL import Image

# Menu Principal
def menu(conexao, cursor):
    layout = [[sg.Text("Selecione o que deseja fazer")],
              [sg.Button("Cadastrar guia", size=(22,3)), sg.Button("Cadastrar Cliente", size=(22,3))],
              [sg.Button("Cadastrar Destino", size=(22,3)),sg.Button("Cadastrar Localização", size=(22,3))],
              [sg.Button("Cadastrar Hotel", size=(22,3)),sg.Button("Cadastrar Quarto", size=(22,3))],
              [sg.Button("Cadastrar Ponto Turístico", size=(22,3)), sg.Button("Cadastrar Transporte", size=(22,3))],
              [sg.Button("Cadastrar foto", size=(22,3)), sg.Button("Login", size=(22,3))],
              [sg.Button("Ver Clientes-Transportes", size=(22,3)), sg.Button("Ver Planos-Pontos turísticos", size=(22,3))],
              [sg.Button("Ver Clientes-Hoteis", size=(22,3)), sg.Button("Ver Foto", size=(22,3))],
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
        elif event == "Login":
            window.hide()
            cadastrar_login()
            window.un_hide()
        elif event == "Cadastrar foto":
            window.hide()
            cadastrar_imagem(conexao, cursor)
            window.un_hide()
        elif event == "Ver Clientes-Transportes":
            window.hide()
            cliente_transporte(cursor)
            window.un_hide()
        elif event == "Ver Planos-Pontos turísticos":
            window.hide()
            Planos_PontosTuristicos(cursor)
            window.un_hide()
        elif event == "Ver Clientes-Hoteis":
            window.hide()
            Clientes_Hoteis(cursor)
            window.un_hide()
        elif event == "Ver Foto":
            window.hide()
            VerImagem(cursor)
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
              [sg.Text("Senha", size=(15,1)), sg.InputText(key='senha', size=(20,1))],
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
            password="rafael18",
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
            password="rafael18",
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
              [sg.Text("Senha", size=(15,1)), sg.InputText(key='senha', size=(20,1))],
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
            password="rafael18",
            database="turismo"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")

            cliente = {
                'Pessoa' : [(values['cpf'],values['endereço'],values['nome'],values['nascimento'],values['telefone'])],
                'Cliente'   : [(values['cpf'], values['user'], values['desconto'],values['senha'])]
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
            password="rafael18",
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
            password="rafael18",
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
            password="rafael18",
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
            password="rafael18",
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
            password="rafael18",
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
            password="rafael18",
            database="turismo"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")

            transporte = {'transporte' : [ ( values['placa'], values['capacidade'],values['tipo'] )] }
            insertSql(transporte,conexao)
            conexao.close()
            sg.popup(f"transporte {values['placa']} cadastrado!")

    window.close()


def cadastrar_login():
    layout = [[sg.Text("Login")],
              [sg.Text("CPF", size=(10,1)), sg.InputText(key='cpf', size=(20,1))],
              [sg.Text("Senha", size=(10,1)), sg.InputText(key='senha', size=(20,1))],
              [sg.Button("Acessar"), sg.Button("Voltar")]]
    window = sg.Window("Login", layout)
    
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Acessar":
            try:

                cpfCliente = values['cpf']
                senhaCliente = values['senha']

                # Verificar se os campos foram preenchidos
                if not cpfCliente or not senhaCliente:
                    sg.popup("Por favor, insira CPF e senha!")
                    continue

                # Conectar ao banco de dados
                conexao = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="rafael18",
                    database="turismo"
                )

                if conexao.is_connected():
                    print("Conectado ao MySQL")

                # Query para verificar CPF e Senha
                sql = """
                    SELECT p.nome FROM Pessoa p
                    INNER JOIN Cliente c ON p.cpf = c.cpf
                    WHERE c.cpf = %s AND c.senha = %s;
                """

                cursor = conexao.cursor()
                cursor.execute(sql, (cpfCliente, senhaCliente))
                resultado = cursor.fetchone()

                if 'cursor' in locals():
                    cursor.close()
                if 'conexao' in locals() and conexao.is_connected():
                    conexao.close()

                if resultado:
                    sg.popup(f"Login efetuado: {resultado[0]}")
                    window.hide()
                    tela_user(values['cpf'])
                    window.un_hide()

                else:
                    sg.popup("Erro ao fazer Login")

            except mysql.connector.Error as err:
                sg.popup_error(f"Erro ao conectar ao MySQL: {err}")
                
    window.close()

def tela_user(cpf):

    conexao = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="rafael18",
                    database="turismo"
                )

    if conexao.is_connected():
        print("Conectado ao MySQL")

    cursor = conexao.cursor()
    cursor.execute("select nome from pessoa where cpf = " + cpf + ";")
    nome = cursor.fetchall()
        
    layout = [[sg.Text(f"Bem vindo {nome[0][0]}")],
              [sg.Button("Criar plano")],
              [sg.Combo(values=obter_dropdown2(cursor,cpf), readonly=True, size=(30, 6), key='excluir') , sg.Button("Editar plano"),sg.Button("Excluir plano")],
              [ sg.Button("Voltar")]]
    window = sg.Window("logado", layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Voltar":
            break
        elif event == "Editar plano":

            criar_plano(cpf,values['excluir'])
            
        elif event == "Excluir plano":
            idPlano = values['excluir']
            sql = 'delete from plano where ID = ' + str(idPlano) +';'
            cursor.execute(sql)
            conexao.commit()

            window['excluir'].update(values = obter_dropdown2(cursor,cpf))


            
        elif event == "Criar plano":
            criar_plano(cpf,0)

    window.close()

def cadastrar_imagem(conexao, cursor):
    layout = [
        [sg.Text("Escolha uma imagem para enviar ao banco de dados")],
        [sg.InputText(key="-FILE-", enable_events=True), sg.FileBrowse("Selecionar", file_types=(("Imagens", "*.png;*.jpg;*.jpeg"),))],
        [sg.Combo(values=obter_dropdown(cursor), readonly=True, size=(30, 6))],
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


def criar_plano(cpf,id):
    conexao = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="rafael18",
                    database="turismo"
                )

    if conexao.is_connected():
        print("Conectado ao MySQL")

    cursor = conexao.cursor()
    cursor.execute('select nome from destino;')
    opcoes = [linha[0] for linha in cursor.fetchall()]
    print(opcoes)
    destino = ['selecione um destino']

    layout = [
        [sg.Text("Destino:", size=(10,1)), sg.Combo(values=opcoes, readonly=True, size=(30, 6)),sg.Button("Confirmar Destino")],
        [sg.Text("Viagem:", size=(10,1)), sg.Combo(values=destino, readonly=True, size=(30, 6),key = '-Combo-'),sg.Button("Confirmar Viagem")],
        [sg.Text("tipo de veículo:", size=(10,1)), sg.Text("", size=(10,1),key ='t')],
        [sg.Text("placa:", size=(10,1)), sg.Text("", size=(10,1),key ='p')],
        [sg.Text("preço:", size=(10,1)), sg.Text("", size=(10,1),key ='pr')],
        [sg.Text("hora:", size=(10,1)), sg.Text("", size=(10,1),key ='h')],
        [sg.Text("Hotel:", size=(10,1)), sg.Combo(values=destino, readonly=True, size=(30, 6),key = 'hotel'),sg.Button("Confirmar Hotel")],
        [sg.Text("Tipo:", size=(10,1)), sg.Text("", size=(20,1),key ='tipoHotel')],
        [sg.Text("Endereço:", size=(10,1)), sg.Text("", size=(40,1),key ='endereçoHotel')],
        [sg.Text("Quarto:", size=(10,1)), sg.Combo(values=["selecione um hotel"], readonly=True, size=(30, 6),key = 'quarto'),sg.Button("Confirmar Quarto")],
        [sg.Text("Capacidade:", size=(10,1)), sg.Text("", size=(10,1),key ='capacidadeQuarto')],
        [sg.Text("Preço:", size=(10,1)), sg.Text("", size=(10,1),key ='preçoQuarto')],
        [sg.Text("Guia:", size=(10,1)), sg.Combo(values=["Selecione um Destino"], readonly=True, size=(30, 6),key = 'guia'),sg.Button("Confirmar Guia")],
        [sg.Text("Preço:", size=(10,1)), sg.Text("", size=(10,1),key ='preçoGuia')],
        [sg.Text("Total:", size=(10,1)), sg.Text("", size=(10,1),key ='total')],
        [sg.Button("Confirmar Plano"),sg.Button("Sair")]
    ]
    janela = sg.Window("Plano", layout)

    while True:
        evento, valores = janela.read()

        if evento == sg.WINDOW_CLOSED or evento == "Sair":
            break
        elif evento == "Confirmar Destino":
            sql = "select DataPartida,placa,preço,ID from viagens where nomeDestino = '" + valores[0] + "';"
            cursor.execute(sql)
            fetch = cursor.fetchall()
            data = [linha[0] for linha in fetch]
            idviagem = [linha[3] for linha in fetch]

            viagem = []

            for idex in range(len(idviagem)):
                viagem.append((idviagem[idex],data[idex]))

            janela["-Combo-"].update(values = viagem)

            sql = "SELECT Hotel.Nome,Hotel.CNPJ FROM Hotel JOIN Localizacao ON Hotel.endereco = Localizacao.endereco WHERE Localizacao.nomeDestino = '" + valores[0] + "';"
            cursor.execute(sql)
            fetch = cursor.fetchall()
            hotel = [linha[0] for linha in fetch]
        
            janela["hotel"].update(values = hotel)

            sql = "Select Guia.ID,P.nome from Guia join Pessoa P on Guia.CPF = P.CPF where Guia.nomeDestino = '" + valores[0] + "';"
            cursor.execute(sql)
            fetch = cursor.fetchall()

            idguia = [linha[0] for linha in fetch]
            nomeguia = [linha[1] for linha in fetch]

            guia = []

            
            for idex in range(len(idguia)):
                guia.append((idguia[idex],nomeguia[idex]))
            
            janela["guia"].update(values = guia)


        elif evento == 'Confirmar Viagem':
            sql = "select placa,preço,hora from viagens where DataPartida = '" + valores['-Combo-'][1] + "';"
            cursor.execute(sql)
            fetch = cursor.fetchall()
            placa = [linha[0] for linha in fetch]
            preçoViagem = [linha[1] for linha in fetch]
            hora = [linha[2] for linha in fetch]

            janela["p"].update(placa[0])
            janela["pr"].update(preçoViagem[0])
            janela["h"].update(hora[0])

            sql = "select tipo from transporte where placatransporte = '" + placa[0] + "';"
            cursor.execute(sql)
            fetch = cursor.fetchall()
            tipo = [linha[0] for linha in fetch]
            janela["t"].update(tipo[0])


        
        elif evento == 'Confirmar Hotel':
            sql = "select tipo,endereco,CNPJ from hotel where nome = '" + valores['hotel'] + "';"
            cursor.execute(sql)
            fetch = cursor.fetchall()
            tipo = [linha[0] for linha in fetch]
            endereço = [linha[1] for linha in fetch]
            hotelcnpj = [linha[2] for linha in fetch]

            janela["tipoHotel"].update(tipo[0])
            janela["endereçoHotel"].update(endereço[0])

            sql = "select numero from quarto where CNPJHotel = '" + hotelcnpj[0] + "';"
            cursor.execute(sql)
            fetch = cursor.fetchall()
            numero = [linha[0] for linha in fetch]
            janela["quarto"].update(values = numero)

        elif evento == 'Confirmar Quarto':
            sql = "select preco,capacidade from quarto where CNPJHotel = " + hotelcnpj[0] +" AND numero = " + str(valores['quarto']) + ";"
            cursor.execute(sql)
            fetch = cursor.fetchall()
            capacidade_quarto = [linha[1] for linha in fetch]
            preço_quarto = [linha[0] for linha in fetch]
            
            janela["capacidadeQuarto"].update(capacidade_quarto[0])
            janela["preçoQuarto"].update(preço_quarto[0])
        
        elif evento == 'Confirmar Guia':
            idGuia = valores['guia']

            if len(idGuia) >= 1:

                idGuia = str(valores['guia'][0])
            
            else:

                idGuia = 'null'

            sql = "select preço from guia where id = '" + idGuia + "';"
            cursor.execute(sql)
            fetch = cursor.fetchall()

            if idGuia != 'null':

                preço_guia = [linha[0] for linha in fetch]
                janela["preçoGuia"].update(preço_guia[0])
            
            else:

                preço_guia = 0
                janela["preçoGuia"].update(preço_guia)

            total = float(janela["preçoGuia"].get()) + float(janela["preçoQuarto"].get()) + float(janela['pr'].get())
            janela['total'].update(total)
        
        elif evento == "Confirmar Plano":
            
            conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rafael18",
            database="turismo"
            )

            if conexao.is_connected():
                print("Conectado ao MySQL")

            cursor = conexao.cursor()

            sql = "select ID from guia where id = '" + str(idGuia) + "';"

            cursor.execute(sql)
            fetch = cursor.fetchall()
            cpfguia = [linha[0] for linha in fetch]

            print(idguia)
            print(hotelcnpj)
            print(valores['quarto'])
            print(valores['-Combo-'][0])
            print(valores['guia'][0])

            if idguia:
                print(idguia)
                Plano = {'Plano' : [ ( cpf, valores['guia'][0], hotelcnpj[0], valores['quarto'], valores['-Combo-'][0] )] }

            else:

                Plano = {'Plano' : [ ( cpf, 'null', hotelcnpj[0], valores['quarto'], valores['-Combo-'][0] )] }

            if(id != 0):
                    sql = "UPDATE Plano SET CPFcliente = '" + cpf + "', IDguia = '" + str(valores['guia'][0]) + "', CNPJHotel = '" + hotelcnpj[0] + "', numeroQuarto = "+ str(valores['quarto']) + ", IDviagem = '"+ str(valores['-Combo-'][0]) +"' WHERE ID = '"+ str(id) +"';"
                    print(sql)
                    cursor = conexao.cursor()
                    cursor.execute(sql)
                    conexao.commit()
                    sg.popup("Plano Atualizado!")

            else:
                insertSql(Plano,conexao)
                sg.popup("Plano cadastrado!")

            conexao.close() 
            
    janela.close()

def cliente_transporte(cursor):
    colunas, dados = VIEW_cliente_transporte(cursor)
    layout = [
        [sg.Text("Tabela de Transportes")],
        [sg.Table(values=dados, headings=colunas, 
                auto_size_columns=True,
                justification="left",
                num_rows=min(10, len(dados)),  # Limita a exibição a 10 linhas
                key="-TABELA-")],
        [sg.Button("Atualizar"), sg.Button("Sair")]
    ]

    # Criar janela
    janela = sg.Window("Consulta ao Banco de Dados", layout)

    # Loop da interface
    while True:
        evento, valores = janela.read()
        
        if evento == sg.WINDOW_CLOSED or evento == "Sair":
            break
        elif evento == "Atualizar":
            colunas, dados = VIEW_cliente_transporte(cursor)
            janela["-TABELA-"].update(values=dados)

    janela.close()


def Planos_PontosTuristicos(cursor):
    colunas, dados = VIEW_Planos_PontosTuristicos(cursor)
    layout = [
        [sg.Text("Tabela de Pontos turísticos")],
        [sg.Table(values=dados, headings=colunas, 
                auto_size_columns=True,
                justification="left",
                num_rows=min(10, len(dados)),  # Limita a exibição a 10 linhas
                key="-TABELA-")],
        [sg.Button("Atualizar"), sg.Button("Sair")]
    ]

    # Criar janela
    janela = sg.Window("Consulta ao Banco de Dados", layout)

    # Loop da interface
    while True:
        evento, valores = janela.read()
        
        if evento == sg.WINDOW_CLOSED or evento == "Sair":
            break
        elif evento == "Atualizar":
            colunas, dados = VIEW_Planos_PontosTuristicos(cursor)
            janela["-TABELA-"].update(values=dados)

    janela.close()


def Clientes_Hoteis(cursor):
    colunas, dados = VIEW_Clientes_Hoteis(cursor)
    layout = [
        [sg.Text("Tabela de Clientes-hoteis")],
        [sg.Table(values=dados, headings=colunas, 
                auto_size_columns=True,
                justification="left",
                num_rows=min(10, len(dados)),  # Limita a exibição a 10 linhas
                key="-TABELA-")],
        [sg.Button("Atualizar"), sg.Button("Sair")]
    ]

    # Criar janela
    janela = sg.Window("Consulta ao Banco de Dados", layout)

    # Loop da interface
    while True:
        evento, valores = janela.read()
        
        if evento == sg.WINDOW_CLOSED or evento == "Sair":
            break
        elif evento == "Atualizar":
            colunas, dados = VIEW_Clientes_Hoteis(cursor)
            janela["-TABELA-"].update(values=dados)

    janela.close()


def VerImagem(cursor):
    pontos_turisticos = obter_dropdown(cursor)

    
    layout = [
        [sg.Text("Selecione um Ponto Turístico:")],
        [sg.Combo(pontos_turisticos, key="-PONTO-", readonly=True, size=(30, 6))],
        [sg.Button("Consultar")],
        [sg.Image(key="-IMAGEM-")],  # Espaço reservado para a imagem
        [sg.Text("", key="-MSG-", text_color="red")],
        [sg.Button("Voltar")]
    ]

    janela = sg.Window("Visualizador de Imagens", layout)

    # Loop de eventos
    while True:
        evento, valores = janela.read()
        
        if evento == sg.WINDOW_CLOSED or evento == "Voltar":
            break
        elif evento == "Consultar":
            ponto_selecionado = valores["-PONTO-"]
            
            if not ponto_selecionado:
                janela["-MSG-"].update("Por favor, selecione um ponto turístico.")
                janela["-IMAGEM-"].update(data=None)
            else:
                imagem_bytes = obter_imagem(ponto_selecionado, cursor)
                if imagem_bytes:
                    imagem_pil = Image.open(io.BytesIO(imagem_bytes))
                    imagem_pil.thumbnail((400, 400))  # Ajustar tamanho para exibição
                    bio = io.BytesIO()
                    imagem_pil.save(bio, format="PNG")
                    janela["-IMAGEM-"].update(data=bio.getvalue())
                    janela["-MSG-"].update("")
                else:
                    janela["-IMAGEM-"].update(data=None)
                    janela["-MSG-"].update("Nenhuma imagem encontrada para este ponto turístico.")

    janela.close()
#menu()