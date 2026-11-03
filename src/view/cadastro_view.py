import flet as ft 
from src.model.usuario import Usuario

class Cadastro(ft.View):
    def __init__(self,pg:ft.Page):
        super().__init__()

        self.width = 800
        self.height = 600
        self.title = "Formulário"
        self.bgcolor = "#ffffff"
        self.horizontal_alignment = "center"
        self.vertical_alignment = "center"


        title = ft.Text(value="Criar Nova Conta",
                        color="#505ab4")
        subtitle = ft.Text(value="Preencha os dados abaixo",
                        color="#505ab4")
        
        self.login = ft.TextField(label="Login",
                             width=300,
                             border_color="#505ab4",
                             color="#505ab4",
                             margin=5)
        
        self.senha = ft.TextField(label="Senha",
                             width=300,
                             border_color="#505ab4",
                             color="#505ab4",
                             margin=5,
                             password= True,
                             can_reveal_password=True)
        
        cadastrar = ft.Button(content="Cadastrar",
                              width=300,
                              height=50,
                              color= "#505ab4",
                              margin=5,
                              on_click=self.cadastrar
        )
        entrar = ft.Button(content="Entrar",
                              width=300,
                              height=50,
                              color= "#505ab4",
                              margin=5
        )
        coluna_acesso = ft.Column(controls=[self.login,self.senha])

        coluna_botoes = ft.Column(controls=[cadastrar,entrar])
        

        self.controls = [title,subtitle,coluna_acesso, coluna_botoes]

    def cadastrar(self):
        usuario = self.login.value
        senha = self.senha.value

        Usuario().cadastrar(usuario,senha)

            
        

