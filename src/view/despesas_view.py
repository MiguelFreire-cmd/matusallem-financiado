import flet as ft

from src.model.usuario import Usuario
from src.model.categoria import Categoria
from src.model.despesas import Despesa
from datetime import datetime

class Despesas_visualização(ft.View):
    def __init__(self,pg:ft.Page):
        super().__init__()

        self.width = 800
        self.height = 600
        self.title = "Formulário"
        self.bgcolor = "#e0eeff"
        self.horizontal_alignment = "center"
        self.dados_usuario = pg.session.store.get("usuario_logado")
        title = ft.Text(value="Visualizar Despesas",
                        color="#7392f7",
                        size=30,)
        self.lista_despesas = []

        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="ID DA DESPESA"),
                                                ft.DataColumn(label="CATEGORIA"),
                                                ft.DataColumn(label="DATA"),
                                                ft.DataColumn(label="HORA"),
                                                ft.DataColumn(label="DESCRIÇÃO"),
                                                ft.DataColumn(label="VALOR"),
                                                ft.DataColumn(label="EXCLUIR DESPESA")],
                                                rows=self.lista_despesas, heading_row_color="#7392f7",)
        
        botao_despesas = ft.Button(icon=ft.Icon(ft.Icons.ADD_BOX_OUTLINED),
                                   bgcolor="#7392f7",
                                   color="#ffffff",
                                   on_click=self.recuperar_despesas
                                   )
        
        self.route = "/despesasview"
        self.controls = [title,botao_despesas,tabela_despesas]

    def recuperar_despesas(self):
        self.lista_despesas.clear()
        categorias = Despesa().pegar(self.dados_usuario)


        for x in categorias:
            id_despesas = x.get("id_despesa")
            id_categoria = x.get("tipo")
            data = x.get("data")
            hora = x.get("hora")
            descricao = x.get("descricao")
            valor = x.get("valor")

            dados_linha = ft.DataRow(cells=[ft.DataCell(content=f"{id_despesas}"),
                                            ft.DataCell(content=f"{id_categoria}"),
                                            ft.DataCell(content=f"{data}"),
                                            ft.DataCell(content=f"{hora}"),
                                            ft.DataCell(content=f"{descricao}"),
                                            ft.DataCell(content=f"{valor}"),
                                            ft.DataCell(ft.Button(icon=ft.Icon(ft.Icons.DELETE_FOREVER),
                                                        bgcolor="#7392f7",
                                                        color="#ffffff",
                                                        key=x.get("id_despesa"),
                                                        on_click=self.excluir_lista,
                                                        width=125))],
                                                                             color="#ffffff")

            self.lista_despesas.append(dados_linha)
        self.page.update()   

    def excluir_lista(self,botao_excluir):

        id_despesa = botao_excluir.control.key
        Despesa().excluir(id_despesa)

        self.recuperar_despesas()



