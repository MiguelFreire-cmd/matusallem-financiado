from src.database.conexao import Conexao

class Despesa:
    def __init__(self):
        pass

    @staticmethod
    def adicionar(login:str, id_categoria:int, data:str, hora:int, descricao:str, valor:int) -> int:
            conexao, cursor = Conexao().conectar()
            
            if conexao == None:
                print("Erro ao tentar conectar na tb_despesas!")
                return None
    
            try:
                cursor.execute("""
                            INSERT INTO tb_despesas(id_categoria, login, data, hora, descricao, valor)
                            VALUES (%s, %s,%s, %s, %s, %s);
                            """,
                            [id_categoria,login, data, hora, descricao, valor])
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
    def pegar(login:str) -> list:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("Erro ao conectar")
            return None

        try:
            cursor.execute("""
                            SELECT id_despesa, id_categoria, login FROM tb_despesas
                            WHERE login = %s;
                            """,
                            [login])
            pegador = cursor.fetchall()
            conexao.close()
            return pegador
        except Exception as erro:
            print(f"Erro ao recuperar dados: {erro}")
            return None
        

    @staticmethod
    def pegar_catgoria(login:str,id_categoria:int) -> list:
        conexao, cursor = Conexao().conectar()
        if not conexao:
            print("Erro ao conectar")
            return None

        try:
            cursor.execute("""
                            SELECT id_despesa, id_categoria, login FROM tb_despesas
                            WHERE login = %s;
                            and id_categoria = %s;
                            """,
                            [login,id_categoria])
            pegador = cursor.fetchall()
            conexao.close()
            return pegador
        except Exception as erro:
            print(f"Erro ao recuperar dados: {erro}")
            return None
        
    @staticmethod
    def alterar(id_despesa:int, login:str, id_categoria:int, data:str, hora:int, descricao:str, valor:int) -> bool:
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
                                    and login = %s;
                               
                            """,
                            [id_categoria,descricao,valor,data,hora,id_despesa,login])
                id_despesa=cursor.lastrowid
                conexao.commit()
                conexao.close()
    
                return True
            except Exception as erro:
                print(f"ERRO AO ADICIONAR: {erro}")
                return False