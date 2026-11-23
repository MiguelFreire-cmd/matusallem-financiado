import flet as ft

from src.model.usuario import Usuario
from src.model.categoria import Categoria
from src.model.despesas import Despesa
from datetime import datetime

class DespesaView(ft.View):
    def __init__(self,pg:ft.Page):
        super().__init__()

        self.width = 800
        self.height = 600
        self.title = "Formulário"
        self.bgcolor = "#ffffff"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"
        self.dados_usuario = pg.session.store.get("usuario_logado")
        title = ft.Text(value="Despesas",
                        color="#505ab4",
                        size=30,)

        self.descricao = ft.TextField(label="Descrição",
                                 width=300,
                                 color="#505ab4",
                                 border_color="#505ab4",
                                 bgcolor="#ffffff")
        self.valor = ft.TextField(label="Valor",
                                 width=300,
                                 color="#505ab4",
                                 border_color="#505ab4",
                                 bgcolor="#ffffff")
        self.campo_data = ft.TextField(label="Data ",
                                 width=300,
                                 color="#505ab4",
                                 border_color="#505ab4",
                                 bgcolor="#ffffff")
        
        self.campo_hora = ft.TextField(label="Hora ",
                                 width=300,
                                 color="#505ab4",
                                 border_color="#505ab4",
                                 bgcolor="#ffffff")

        opcoes_categoria = []
        categorias = Categoria.recuperar(self.dados_usuario)

        for x in categorias:
            opcao = ft.DropdownOption(key=x.get("id_categoria"),
                              text=x.get("tipo"))
            opcoes_categoria.append(opcao)

        self.campo_categoria = ft.Dropdown(width=300,
                                      color="#505ab4",
                                      border_color="#505ab4",
                                      options=opcoes_categoria,
                                      )

        self.botao_cadastrar = ft.Button(content="Cadastrar",
                                         width=300,
                                         on_click=self.cadastrar_despesas,
                                         bgcolor="#c0dff1",
                                         color= "#ffffff",)

        
        coluna_campos = ft.Column(controls=[self.descricao,self.valor,self.campo_data,self.campo_hora,self.campo_categoria,self.botao_cadastrar])
        
        self.route = "/despesas"
        self.controls = [title,coluna_campos]

    def cadastrar_despesas(self):
        descricao = self.descricao.value
        valor = self.valor.value
        data = self.campo_data.value
        id_categoria = self.campo_categoria.value
        hora = self.campo_hora.value

        data_formatada = datetime.strptime(data, "%d/%m/%Y").date()
        hora_formatada = datetime.strptime(hora, "%H:%M:%S")

        Despesa().adicionar(self.dados_usuario, id_categoria, data_formatada, hora_formatada, descricao, valor)
