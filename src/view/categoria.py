import flet as ft

from src.model.usuario import Usuario
from src.model.categoria import Categoria

class CategoriaView(ft.View):
    def __init__(self,pg:ft.Page):
        super().__init__()

        self.width = 800
        self.height = 600
        self.title = "Formulário"
        self.bgcolor = "#ffffff"
        self.horizontal_alignment = "center"
        self.lista_categoria = []
        self.dados_usuario = pg.session.store.get("usuario_logado")
        title = ft.Text(value="Categoria",
                        color="#505ab4",
                        size=50,
                        margin=15,)
        

        self.pegar_categoria = ft.TextField(label="Nome da Categoria",
                                       color="#505ab4",
                                       border_color="#505ab4",
                                       bgcolor="#ffffff")

        botão_salvar = ft.Button(content="salvar",
                                 color="#505ab4",
                                 on_click= self.cadastrar_categoria)
        
        

        coluna_lista = ft.Column(controls=self.lista_categoria,
                                 expand=True,
                                 scroll=ft.ScrollMode.AUTO,
                                 alignment="center",
                                 width=400)
        subtitle = ft.Text(value="Categorias Existentes",
                                 color="#505ab4",
                                 size=25)

        linha_categoria = ft.Row(controls=[self.pegar_categoria,botão_salvar],
                                 alignment="center")
        
        countainer = ft.Container(content=linha_categoria,
                                  bgcolor= "#c0dff1",
                                  border_radius=20,
                                  width=425,
                                  height=100,
                                  padding=5)


        self.route = "/categoriaview"
        self.controls = [title,countainer,subtitle, coluna_lista]
        

    def cadastrar_categoria(self):

            
            categoria = self.pegar_categoria.value


            resultado = Categoria().adicionar(categoria, self.dados_usuario)

            if resultado:
                self.page.show_dialog(ft.SnackBar(content="Belo cadastro irmão",
                                                  bgcolor="#94d1fa"))
            else:
                self.page.show_dialog(ft.SnackBar(content="Você come merda?",
                                                  bgcolor="#35abfa"))

            self.lista_categoria.clear()
            self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_categoria.clear()
        categorias = Categoria().recuperar(self.dados_usuario)

        for x in categorias:
             campo = x.get("tipo")
             linha = ft.Row(controls=[ft.TextField(value=campo,
                                  height=50,
                                  width=275), 
                                  ft.Button(icon=ft.Icon(ft.CupertinoIcons.DELETE),key=x.get("id_categoria"), on_click=self.excluir_lista, width=100)])
             
             
             self.lista_categoria.append(linha)
             
             self.page.update()

    def excluir_lista(self,botao_excluir):

        id_categoria = botao_excluir.control.key
        Categoria().excluir(id_categoria)

        self.atualizar_lista()

        
                

        

        
        