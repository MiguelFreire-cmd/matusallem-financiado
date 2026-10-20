from src.database.conexao import Conexao

class Usuario:
    def __init__(self):
        pass

    @staticmethod
    def cadastrar(login:str, senha:str) -> bool:
        conexao, cursor = Conexao().conectar()

        cursor.execute("""
                        insert into tb_alunos
                       """)