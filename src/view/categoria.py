import flet as ft

from src.model.usuario import Usuario

class CategoriaView(ft.View):
    def __init__(self,pg:ft.Page):
        super().__init__()

        self.width = 800
        self.height = 600
        self.title = "Formulário"
        self.bgcolor = "#ffffff"
        self.vertical_alignment = "center"
        self.horizontal_alignment = "center"

        title = ft.Text(value="Categoria",
                        color="#505ab4",
                        size=30,)
        
        self.route = "/categoriaview"
        self.controls = [title]