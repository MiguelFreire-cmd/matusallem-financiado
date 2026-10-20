from src.database.conexao import Conexao

class Usuario:
    def __init__ (self):
        pass


    @staticmethod
    def cadastrar(id_login:str, senha:str) -> bool: 



    
        conexao , cursor = Conexao(). conectar()
        try:
            if conexao == None:
                print("erro ao tentar conectar!!!")
                return False
            
            cursor.execute ("""
                            insert into tb_usuarios(id_login, senha)
                            values (%s, %s)
    """, [id_login,senha])

            conexao.commit()
            conexao.close()

            return True
        except Exception as erro:
            print(f"ERRO: {erro}")
            return False


    @staticmethod
    def verificar(id_login:str, senha:str) -> dict:
        conexao, cursor = Conexao(). conectar()

        if conexao == None:
            return None

        try:
            cursor.execute("""
                            select id_login, senha from tb_usuarios
                            where id_login = %s
                            and senha = %s
""",[id_login, senha])
            resultado = cursor.fetchone()
            conexao.close()

            return resultado
        
        except Exception as erro:
            print(f"ERRO: {erro}")
            
