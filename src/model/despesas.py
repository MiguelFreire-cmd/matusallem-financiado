from src.database.conexao import Conexao

class Despesa:
    def __init__(self):
        pass

    @staticmethod
    def adicionar(id_login:str, id_categoria:int, data:str, hora:int, descricao:str, valor:int) -> int:
            conexao, cursor = Conexao().conectar()
            
            if conexao == None:
                print("Erro ao tentar conectar na tb_despesas!")
                return None
    
            try:
                cursor.execute("""
                            INSERT INTO tb_despesas(id_categoria, id_login, data, hora, descricao, valor)
                            VALUES (%s, %s,%s, %s, %s, %s);
                            """,
                            [id_categoria,id_login, data, hora, descricao, valor])
                id_categoria=cursor.lastrowid
                conexao.commit()
                conexao.close()
    
                return id_categoria
            except Exception as erro:
                print(f"ERRO AO ADICIONAR: {erro}")
                return None


    @staticmethod
    def excluir(id_despesa:int) -> bool:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("Erro ao conectar")

        try:  
            cursor.execute("""
                            DELETE FROM tb_despesas
                            WHERE id_despesa = %s;                    
                            """,
                            [id_despesa])
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro:
            print(f"Erro ao excluir: {erro}")
            return False

    @staticmethod
    def pegar(id_login:str) -> list:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("Erro ao conectar")
            return None

        try:
            cursor.execute("""
                            SELECT * FROM tb_despesas
                            WHERE id_login = %s;
                            """,
                            [id_login])
            pegador = cursor.fetchall()
            conexao.close()
            return pegador
        except Exception as erro:
            print(f"Erro ao recuperar dados: {erro}")
            return None
        

    @staticmethod
    def pegar_categoria(id_login:str,id_categoria:int) -> list:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("Erro ao conectar")
            return None

        try:
            cursor.execute("""
                            SELECT id_despesa, id_categoria, id_login FROM tb_despesas
                            WHERE id_login = %s;
                            and id_categoria = %s;
                            """,
                            [id_login,id_categoria])
            pegador = cursor.fetchall()
            conexao.close()
            return pegador
        except Exception as erro:
            print(f"Erro ao recuperar dados: {erro}")
            return None
        
    @staticmethod
    def alterar(id_despesa:int, id_login:str, id_categoria:int, data:str, hora:int, descricao:str, valor:int) -> bool:
            conexao, cursor = Conexao().conectar()
            
            if conexao == False:
                print("Erro ao tentar conectar na tb_despesas!")
                return False
    
            try:
                cursor.execute("""
                                UPDATE tb_despesas SET
                                    id_categoria = %s.
                                    descricao = %s,
                                    valor = %s,
                                    data = %s,
                                    hora = %s
                                WHERE 
                                    id_despesa = %s
                                    and id_login = %s;
                               
                            """,
                            [id_categoria,descricao,valor,data,hora,id_despesa,id_login])
                id_despesa=cursor.lastrowid
                conexao.commit()
                conexao.close()
    
                return True
            except Exception as erro:
                print(f"ERRO AO ADICIONAR: {erro}")
                return False