import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback_context
from dash.dependencies import Input, Output, State
from pages import tela_menu,tela_cad_plataforma,tela_login,tela_menu_dois,tela_cad_pet

class Callbacks:
    def __init__(self,app):
        self.app = app
    def definir_callbacks(self):
        print('aqui')
        @self.app.callback(Output('main-card', 'children'),[Input('url','pathname')])
        def update_tela(caminho):
            print(caminho)
            if caminho == '/':
                return tela_menu.return_layout()
            elif caminho == '/entrar':
                return tela_login.return_layout()
            elif caminho == '/cadastrar':
                return tela_cad_plataforma.return_layout()
            elif caminho == '/prox-menu':
                return tela_menu_dois.return_layout()
            elif caminho == '/adotar-pet':
                pass
            elif caminho == '/cadastrar-pet':
                return tela_cad_pet.return_layout()
            return tela_menu.return_layout()


