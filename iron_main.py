import flet as ft
from src.view.cadastro_view import Cadastro
from src.view.principal import Principal
from src.view.login import Login

def main(pg:ft.Page):
    tela_navegacao = ft.NavigationBar(destinations=[
                                        ft.NavigationBarDestination(icon=ft.Icons.EXPOSURE_PLUS_1, label="Criar Categoria"),
                                        ft.NavigationBarDestination(icon=ft.Icons.PAGEVIEW_OUTLINED, label="Despesas por Categoria"),
                                        ft.NavigationBarDestination(icon=ft.Icons.EXPOSURE_PLUS_1, label=" Criar Despesas"),
                                        ft.NavigationBarDestination(icon=ft.Icons.PAGEVIEW_OUTLINED, label="Visualizar Despesas"),
                                        ]

    )
    tela_cadastro = Cadastro(pg)
    tela_login = Login(pg)
    tela_principal = Principal(pg)
    tela_principal.navigation_bar = tela_navegacao

    def roteament(e=None):
        pg.views.clear()

        if pg.route == "/cadastro":
            pg.views.append(tela_cadastro)
        elif pg.route == "/login":
            pg.views.append(tela_login)
        elif pg.route == "/principal":
            pg.views.append(tela_principal)

        pg.update()

    pg.on_route_change = roteament
    roteament()

    pg.views.append(tela_login)
ft.run(main)