import mysql.connector
from interfaces import *

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="309320",
    database="turismo"
)



if conexao.is_connected():
    print("Conectado ao MySQL")



'''
função para facilitar a inserção de dados na tabela
recebe um dicionario no formato {nomeDaTabela : [(dados a serem inseridos)]
importante colocar os parentesis dentro da lista
a ordem das operações no dicionario nao importam, as chaves(tabelas) são reordenadas automáticamente para que nao de problema com FK
pode inserir varios dados em varias tabelas ao mesmo tempo
'''
def insertSql(dicionario,conexao):
    
    ordem_personalizada = ['Pessoa','Destino', 'Localizacao', 'Hotel',  'pontoTuristico', 'Transporte', 'Cliente', 'Guia', 'Quarto', 'onibus', 'Aviao', 'localDePartida', 'Plano']
    prioridade = {chave: i for i, chave in enumerate(ordem_personalizada)}
    dicionario = dict(sorted(dicionario.items(), key=lambda item: prioridade[item[0]]))
    print(dicionario)
    
    cursor = conexao.cursor()
    
    for key in dicionario.keys():
        #print(key)
        sql = "SELECT * FROM " + key
        cursor.execute(sql)
        nomes_colunas = cursor.column_names
        #print(nomes_colunas)
        
        cursor.fetchall()
        
        sql = "INSERT INTO " + key + " VALUES (" + ("%s," * (len(dicionario[key][0])-1)) + "%s)"
        #print(dicionario[key][0])
        #print(sql)
        
        cursor.execute(sql, dicionario[key][0])
        conexao.commit()
        
        

dicionarioValues = {
    "Pessoa" : [(1234, "endereçoteste", "Fulano", "2025-01-01", "6199999999")],
    "Hotel" : [('cnpj','tipo','nome','endereço')],
    "Destino": [('destino','nome')],
    "Localizacao" : [('endereço','nome')]
    
    
    }

insertSql(dicionarioValues,conexao)

        


#menu()
#cursor.close()
conexao.close()