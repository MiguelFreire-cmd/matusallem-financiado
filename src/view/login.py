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

        title = ft.Text(value="Matusalem Financiado",
                        color="#505ab4",
                        size=20)
        subtitle = ft.Text(value="Login AQUI!!",
                        color="#505ab4",
                        size=20)
        
        self.route = "/login"
        
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
                             can_reveal_password=True
                             )
        
        cadastrar = ft.Button(content="Entrar",
                              width=300,
                              height=50,
                              color= "#505ab4",
                              on_click=self.verificar
        )
        entrar = ft.TextButton(content="Não tem uma conta? Cadastre-se aqui",
                              width=300,
                              height=50,
                              style=ft.ButtonStyle(color="#505ab4"),
                              on_click=self.voltar
        )
        coluna_acesso = ft.Column(controls=[self.login,self.senha])

        coluna_botoes = ft.Column(controls=[cadastrar,entrar])
        

        self.controls = [title,subtitle,coluna_acesso, coluna_botoes]

    async def verificar(self):
    
    
            usuario = self.login.value
            senha = self.senha.value
    
            if usuario == "" or senha == "":
                self.page.show_dialog(ft.SnackBar(content="Para de ser burro e escreve",
                                                bgcolor="#a0aff1"))
                return
    
            resultado = Usuario().verificar(usuario,senha)
            if resultado :
                self.page.show_dialog(ft.SnackBar(content="Deu certo meu patrão",
                            bgcolor="#94d1fa"))
                await self.ir_para_principal()
            else:
                self.page.show_dialog(ft.SnackBar(content="Deu merda...",
                bgcolor="#505ab4"))

            Usuario().verificar(usuario,senha)

    async def voltar(self):
            await self.page.push_route("/cadastro")

    async def ir_para_principal(self):
            await self.page.push_route("/principal")

    