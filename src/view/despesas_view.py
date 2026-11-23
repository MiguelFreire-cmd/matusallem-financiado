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
        self.bgcolor = "#d5dce5"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"
        self.dados_usuario = pg.session.store.get("usuario_logado")
        title = ft.Text(value="Visualizar Despesas",
                        color="#3765fc",
                        size=30,)
        self.lista_despesas = []

        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="ID DA DESPESA"),
                                                ft.DataColumn(label="DESCRIÇÃO"),
                                                ft.DataColumn(label="VALOR"),
                                                ft.DataColumn(label="CATEGORIA"),
                                                ft.DataColumn(label="DATA")],
                                                rows=self.lista_despesas)
        
        self.route = "/despesasview"
        self.controls = [title]
    def pegar_despesas(self):

        categorias = Despesa().pegar(self.dados_usuario)

        for x in categorias:
             campo = x.get("id_despesa")
             
             
             self.lista_despesas.append(campo)
             