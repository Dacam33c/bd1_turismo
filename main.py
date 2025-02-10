import mysql.connector
from interfaces import *


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha123",
    database="turismo"
)

if conexao.is_connected():
    print("Conectado ao MySQL")
cursor = conexao.cursor()

menu(conexao, cursor)
cursor.close()
conexao.close()