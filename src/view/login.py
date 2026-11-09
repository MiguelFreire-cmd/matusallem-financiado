import flet as ft

from src.model.usuario import Usuario

class Login(ft.View):
    def __init__(self,pg:ft.Page):
        super().__init__()

        self.width = 800
        self.height = 600
        self.title = "Formulário"
        self.bgcolor = "#ffffff"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"

        title = ft.Text(value="Abre ai vai",
                        color="#505ab4",
                        size=200)

        self.controls=[title]