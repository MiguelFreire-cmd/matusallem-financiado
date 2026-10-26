from src.database.conexao import Conexao
class Categoria:
    def __int__(self):
        pass
    @staticmethod
    def adicionar(tipo:str ,id_login:str) -> int:
        conexao, cursor = Conexao().conectar
        if not conexao:
            print("erro ao tentar conectar")
            return None
        try:
            cursor.execute("""
                            INSERT INTO tb_categorias(tipo, id_login)
                            VALUES (%s, %s);
                            """,
                            [id_login, tipo])
            id_categoria = cursor.lasrowid
            conexao.commit()
            conexao.close()
            return  id_categoria
        except Exception as e:
            print(f"Erro ao Inserir: {e}!")
            return None