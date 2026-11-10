import flet as ft

from src.model.usuario import Usuario

class CategoriaView(ft.View):
    def __init__(self,pg:ft.Page):
        super().__init__()

        self.width = 800
        self.height = 600
        self.title = "Formulário"
        self.bgcolor = "#ffffff"
        self.horizontal_alignment = "center"

        lista_incluir = []          

        title = ft.Text(value="Categoria",
                        color="#505ab4",
                        size=50,
                        margin=15,)
        

        pegar_categoria = ft.TextField(label="Nome da Categoria",
                                       color="#505ab4",
                                       border_color="#505ab4",
                                       width=300,
                                       height=50)

        botão_salvar = ft.Button(content="salvar",
                                 color="#505ab4",
                                 width=200,
                                 height=50)

        subtitle = ft.Text(value="Categorias Existentes",
                                 color="#3549f8",
                                 size=30)

        linha_categoria = ft.Row(controls=[pegar_categoria,botão_salvar],
                                 alignment="center")

                
                

        

        
        
        self.route = "/categoriaview"
        self.controls = [title, linha_categoria]