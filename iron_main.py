import flet as ft
from src.view.cadastro_view import Cadastro

def main(pg:ft.Page):
    tela_cadastro = Cadastro(pg)
    pg.views.append(tela_cadastro)
ft.run(main)