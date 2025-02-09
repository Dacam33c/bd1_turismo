import mysql.connector
import PySimpleGUI as sg


'''
função para facilitar a inserção de dados na tabela
recebe um dicionario no formato {nomeDaTabela : [(dados a serem inseridos)]
importante colocar os parentesis dentro da lista
a ordem das operações no dicionario nao importam, as chaves(tabelas) são reordenadas automáticamente para que nao de problema com FK
pode inserir varios dados em varias tabelas ao mesmo tempo
'''
def insertSql(dicionario,conexao):
    
    ordem_personalizada = ['Pessoa','Destino', 'Localizacao', 'Hotel',  'pontoTuristico','pontoFoto','transporte','Viagens', 'Cliente', 'Guia', 'Quarto', 'Plano']
    prioridade = {chave: i for i, chave in enumerate(ordem_personalizada)}
    dicionario = dict(sorted(dicionario.items(), key=lambda item: prioridade[item[0]]))
    
    cursor = conexao.cursor()
    
    for key in dicionario.keys():
        #print(key)
        sql = "SELECT * FROM " + key
        cursor.execute(sql)
        nomes_colunas = cursor.column_names
        #print(nomes_colunas)
        temId = 0
        cursor.fetchall()
        
        if(nomes_colunas[0] == "ID"):
            nomes_colunas = nomes_colunas[1:]
        
        textoColunas = ",".join(nomes_colunas)
        
        sql = "INSERT INTO " + key + " (" + textoColunas + ") " + " VALUES (" + ("%s," * (len(dicionario[key][0])-1)) + "%s)"
        #print(dicionario[key][0])
        #print(sql)
        
        cursor.execute(sql, dicionario[key][0])
        conexao.commit()
'''
dicionarioValues = {
    "Pessoa" : [(1234, "endereçoteste", "Fulano", "2025-01-01", "6199999999")],
    "Hotel" : [('cnpj','tipo','nome','endereço')],
    "Destino": [('destino','nome')],
    "Localizacao" : [('endereço','nome')]
    
    
    }

insertSql(dicionarioValues,conexao)
'''

# Função para converter imagem para arquivo binário
def img_to_blob(caminho):
    with open(caminho, 'rb') as arquivo:
        return arquivo.read()

def salvar_imagem(nome, caminho, conexao, cursor):
    try:
        img_convertida = img_to_blob(caminho)
        query = "INSERT INTO pontoFoto (Nome, foto) VALUES (%s, %s)"
        cursor.execute(query, (nome, img_convertida))
        conexao.commit()
        sg.popup("Imagem salva com sucesso")
    except Exception as e:
        sg.popup(f"Falha ao salvar imagem: {e}")

# Função para obter Nome dos pontos turísticos para usar no Menu Dropdown de salvar imagem
def obter_dropdown(cursor):
    cursor.execute("SELECT Nome from pontoTuristico")
    opcoes = [linha[0] for linha in cursor.fetchall()]
    return opcoes