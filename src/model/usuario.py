from src.database.conexao import Conexao

class Usuario:
    def __init__ (self):
        pass


    @staticmethod
    def cadastrar(login:str, senha:str) -> bool: 



    
        conexao , cursor = Conexao(). conectar()
        try:
            if conexao == None:
                print("erro ao tentar conectar!!!")
                return False
            
            cursor.execute ("""
                            insert into tb_usuarios(login, senha)
                            values (%s, %s)
    """, [login,senha])

            conexao.commit()
            conexao.close()

            return True
        except Exception as erro:
            print(f"ERRO: {erro}")
            return False


    @staticmethod
    def verificar(login:str, senha:str) -> dict:
        conexao, cursor = Conexao(). conectar()

        if conexao == None:
            return None

        try:
            cursor.execute("""
                            select login, senha from matusallem_financiado
                            where login = %s
                            and senha = %s
""",[login, senha])
            resultado = cursor.fetchone()
            conexao.close()

            return resultado
        
        except Exception as erro:
            print(f"ERRO: {erro}")
            return {}
