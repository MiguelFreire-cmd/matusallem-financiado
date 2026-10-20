import mysql.connector

class Conexao:
    def __init__(self):
        pass
    @staticmethod
    def conectar():
        try:
            #criar a conexão com o banco de dados MySQLit
            conexao = mysql.connector.connect(host="localhost",
                                            port = 3306,
                                            user = "root",
                                            password = "root",
                                            database = "matusallem_financiado")
            cursor = conexao.cursor()

            return conexao, cursor
        except Exception as erro:
            print(f"ERRO: {erro}")
            return None, None