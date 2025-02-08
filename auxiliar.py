import mysql.connector


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