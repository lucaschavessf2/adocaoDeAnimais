
from db_conexao import Conexao
import dash
from dash.dependencies import Input, Output, State
from pages import tela_menu,tela_cad_plataforma,tela_login,tela_menu_dois,tela_cad_pet

class Callbacks:
    def __init__(self,app):
        self.app = app
        self.db_conexao = Conexao()
    def definir_callbacks(self):
        @self.app.callback(Output('main-card', 'children'),[Input('url_geral','pathname'),Input('url_cadastro','pathname'),Input('url_login','pathname')])
        def __atualizar_tela(caminho,__,___):
            caminho = __ = ___
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
    
        @self.app.callback([Output('url_cadastro','pathname')],[Input('btn-cad-cadastrar','n_clicks'),State('input-cd-nome','value'),State('input-cd-dtnascimento','value'),State('input-cd-email','value'),State('input-cd-senha','value')])
        def __botao_cadastro(botao,nome,data,email,senha):
            if botao:
                self.db_conexao.inserir_dados("login_usuarios","(email,senha)",(email,senha))
                return ["/entrar"]
            else:
                return dash.no_update
            
        @self.app.callback([Output('url_login','pathname'),Output('span-login-aviso','children')],[Input('btn-login-entrar','n_clicks'),State('input-login-email','value'),State('input-login-senha','value')])
        def __botao_login(botao,email,senha):
            if botao:
                login = self.db_conexao.verificar_login(email,senha)
                if login:
                    return ["/prox-menu",""]
                else:
                    print('caiu aqui')
                    return ["/entrar","E-mail ou senha inválidos"]
            else:
                return dash.no_update

        
    


