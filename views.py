"""
Arquivo com as funções de view do Banco de dados
As funções retornam as tabelas resultantes de um SELECT no Banco de dados

"""


def VIEW_cliente_transporte(cursor):
    cursor.execute("SELECT * FROM cliente_transporte")
    dados = cursor.fetchall()
    colunas = [desc[0] for desc in cursor.description]
    return colunas, dados

def VIEW_Planos_PontosTuristicos(cursor):
    cursor.execute("SELECT * FROM Planos_PontosTuristicos")
    dados = cursor.fetchall()
    colunas = [desc[0] for desc in cursor.description]
    return colunas, dados


def VIEW_Clientes_Hoteis(cursor):
    cursor.execute("SELECT * FROM Clientes_Hoteis")
    dados = cursor.fetchall()
    colunas = [desc[0] for desc in cursor.description]
    return colunas, dados

