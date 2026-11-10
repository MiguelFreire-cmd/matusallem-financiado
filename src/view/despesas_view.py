import flet as ft

from src.model.usuario import Usuario

class Despesas_visualização(ft.View):
    def __init__(self,pg:ft.Page):
        super().__init__()

        self.width = 800
        self.height = 600
        self.title = "Formulário"
        self.bgcolor = "#ffffff"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        title = ft.Text(value="Visualizar Despesas",
                        color="#505ab4",
                        size=30,)
        
        self.route = "/despesasview"
        self.controls = [title]