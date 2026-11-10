import flet as ft

from src.model.usuario import Usuario

class Principal(ft.View):
    def __init__(self,pg:ft.Page):
        super().__init__()

        self.width = 800
        self.height = 600
        self.title = "Formulário"
        self.bgcolor = "#ffffff"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        dados_usuario = pg.session.store.get("usuario_logado")

        title = ft.Text(value="Matusalem Financiado",
                        color="#505ab4",
                        size=30,)
        subtitle = ft.Text(value=f"{dados_usuario} Manda tudo para eu roubar suas informações",
                        color="#505ab4",
                        size=12,)


        self.route = "/principal"

        self.controls = [title,subtitle]