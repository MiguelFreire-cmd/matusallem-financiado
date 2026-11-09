import flet as ft
from src.view.cadastro_view import Cadastro
from src.view.login import Login

def main(pg:ft.Page):
    tela_cadastro = Cadastro(pg)
    tela_login = Login(pg)

    def roteament(e=None):
        pg.views.clear

        if pg.route == "/cadatro":
            pg.views.append(tela_cadastro)
        elif pg.route == "/login":
            pg.views.append(tela_login)

        pg.update()

    pg.on_route_change = roteament
    roteament()

    pg.views.append(tela_cadastro)
ft.run(main)