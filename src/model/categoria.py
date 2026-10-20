from src.database.conexao import Conexao
class Categoria:
    def __int__(self):
        pass
    @staticmethod
    def adicionar(categoria:str, login:str) -> int:
        conexao, cursor = Conexao().conectar
        if not conexao:
            print("erro ao tentar conectar")
            return None
        
        cursor.execute("""
                        INSERT INTO tb_categorias(nome_categoria, login,)
                        VALUES (%s, %s, %s)
                        """,
                        [categoria, login])
        
        conexao.commit()
        conexao.close()
        return