"""
Arquivo com as funções de view do Banco de dados
As funções retornam as tabelas resultantes de um SELECT no Banco de dados

"""

def VIEW_cliente_transporte(cursor):
    cursor.execute("SELECT * FROM cliente_transporte")
    dados = cursor.fetchall()
    colunas = [desc[0] for desc in cursor.description]
    return colunas, dados