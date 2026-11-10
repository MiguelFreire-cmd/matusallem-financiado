import flet as ft

from src.model.usuario import Usuario

class Principal(ft.View):
    def __init__(self,pg:ft.Page):
        super().__init__()

        self.width = 800
        self.height = 600
        self.title = "Formulário"
        self.bgcolor = "#ffffff"
        self.horizontal_alignment = "center"
        self.vertical_alignment_alignment = "center"

        title = ft.Text(value="Matusalem Financiado",
                        color="#505ab4",
                        size=30)
        subtitle = ft.Text(value="Manda tudo para eu roubar suas informações",
                        color="#505ab4",
                        size=12,)

        inserir_despesa = ft.Button(content="Anserir despesa", width= 200, color="#505ab4")
        ver_despesa = ft.Button(content="Ver a despesa", width= 200, color="#505ab4")
        inserir_categoria = ft.Button(content="inserir categoria", width= 200, color="#505ab4")
        ver_categorias = ft.Button(content="Vizualizar suas categorias", width= 200, color="#505ab4")

        self.route = "/principal"

        self.controls = [title,subtitle]