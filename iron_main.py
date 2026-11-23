import flet as ft
from src.view.cadastro_view import Cadastro
from src.view.principal import Principal
from src.view.login import Login
from src.view.categoria_view import Categoria_visualização
from src.view.categoria import CategoriaView
from src.view.despesa import DespesaView
from src.view.despesas_view import Despesas_visualização

def main(pg:ft.Page):
    def navegacao(e):
        item_clicado = e.control.selected_index
        if item_clicado == 0:
            pg.navigate("/categoriaview")
        if item_clicado ==1:
            pg.navigate("/categoria")
        if item_clicado ==2:
            pg.navigate("/despesas")
        if item_clicado ==3:
            pg.navigate("/despesasview")
        if item_clicado ==4:
            pg.navigate("/login")

    tela_navegacao = ft.NavigationBar(destinations=[
                                        ft.NavigationBarDestination(icon=ft.Icons.LIST, label="Criar Categoria"),
                                        ft.NavigationBarDestination(icon=ft.Icons.PAGEVIEW_OUTLINED, label="Despesas por Categoria"),
                                        ft.NavigationBarDestination(icon=ft.Icons.GIF_BOX, label=" Criar Despesas"),
                                        ft.NavigationBarDestination(icon=ft.Icons.FILTER, label="Visualizar Despesas"),
                                        ft.NavigationBarDestination(icon=ft.Icons.EXIT_TO_APP, label="Sair"),
                                        ],
                                        on_change=navegacao)













    def roteament(e=None):
        pg.views.clear()

        if pg.route == "/cadastro":
            tela_cadastro = Cadastro(pg)
            pg.views.append(tela_cadastro)
        elif pg.route == "/login":
            tela_login = Login(pg)
            pg.views.append(tela_login)
        elif pg.route == "/principal":
            tela_principal = Principal(pg)
            tela_principal.navigation_bar = tela_navegacao
            pg.views.append(tela_principal)
        elif pg.route == "/categoriaview":
            tela_categoria = CategoriaView(pg)
            tela_categoria.navigation_bar = tela_navegacao
            pg.views.append(tela_categoria)
        elif pg.route == "/categoria":
            tela_despesas_por_categoria = Categoria_visualização(pg)
            tela_despesas_por_categoria.navigation_bar = tela_navegacao
            pg.views.append(tela_despesas_por_categoria)
        elif pg.route == "/despesas":
            tela_despesas = DespesaView(pg)
            tela_despesas.navigation_bar = tela_navegacao
            pg.views.append(tela_despesas)
        elif pg.route == "/despesasview":
            tela_visualizar_despesas = Despesas_visualização(pg)
            tela_visualizar_despesas.navigation_bar = tela_navegacao
            pg.views.append(tela_visualizar_despesas)

        pg.update()

    pg.on_route_change = roteament
    roteament()

    pg.navigate("/login")
ft.run(main)