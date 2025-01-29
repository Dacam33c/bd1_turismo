import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha123",
    database="turismo"
)

cursor = conexao.cursor()

if conexao.is_connected():
    print("Conectado ao MySQL")

comando = "INSERT INTO Pessoa (CPF, endereco, nome, dataDeNascimento, telefone) VALUES (%s, %s, %s, %s, %s)"
novo_registro = (1000, "Rua 1 Brasilia", "Fulano", "2025-01-01", "6199999999")

cursor.execute(comando, novo_registro)
conexao.commit()

print(f"Pessoa cadastrada, ID: {cursor.lastrowid}")
cursor.close()
conexao.close()