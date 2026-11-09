import flet as ft
from src.view.cadastro_view import Cadastro
from src.view.login import Login

def main(pg:ft.Page):
    tela_cadastro = Cadastro(pg)
    tela_login = Login(pg)
    pg.views.append(tela_login)
ft.run(main)