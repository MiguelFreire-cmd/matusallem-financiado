from src.database.conexao import Conexao
class Categoria:
    def __int__(self):
        pass
    @staticmethod
    def adicionar(tipo:str ,id_login:str) -> int:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("erro ao tentar conectar")
            return None
        
        try:
            cursor.execute("""
                            INSERT INTO tb_categorias(tipo, id_login)
                            VALUES (%s, %s);
                            """,
                            [tipo, id_login ])
            
            id_categoria = cursor.lastrowid
            conexao.commit()
            conexao.close()
            return  id_categoria
        
        except Exception as e:
            print(f"Erro ao Inserir: {e}!")
            return None
        
    @staticmethod
    def excluir(id_categoria:int) -> bool:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("erro ao tentar conectar")
            return False
        
        try:
            cursor.execute("""
                            DELETE FROM tb_categorias
                            Where id_categoria = %s;""",
                            [id_categoria])
            
            conexao.commit()
            conexao.close()
            return True

        except Exception as e:
            print(f"Erro ao Inserir: {e}!")
            return False
    @staticmethod
    def recuperar(id_login:str) -> list:
        conexao, cursor = Conexao().conectar()

        if not conexao:
            print("erro ao tentar conectar")
            return None
        
        try:
            cursor.execute("""
                            select id_categoria, tipo, id_login from tb_categorias
                            where id_login = %s

                            
""", [id_login])
            resultado = cursor.fetchall()
            conexao.close()
            return resultado

        except Exception as e:
            print(f"Erro ao Inserir: {e}!")