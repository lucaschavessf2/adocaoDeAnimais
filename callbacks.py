import re
import dash
import bcrypt
from datetime import datetime
from db_conexao import Conexao
from dash.dependencies import Input, Output, State
from pages import tela_menu,tela_cad_plataforma,tela_login,tela_menu_dois,tela_cad_pet

#Função para verificar se é um email
def verificar_email(email):
    try:
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
    except:
        return False


#Função para verificar se é uma data válida
def verificar_data(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except:
        return False

#Função que verifica se o cadastro é válido
def verificar_cadastro(nome,data,email,senha,db_conexao):
    email_real = verificar_email(email)
    data_real = verificar_data(data)
    email_existe = db_conexao.consultar_dados("login_usuarios","COUNT(*)",f"WHERE email = ?",(email,))
    if None in [nome,data,email,senha] or "" in [nome,data,email,senha] or email_real == False or email_existe[0][0] > 0 or data_real == False:
        return False
    return True


#Classe dos callbacks
class Callbacks:
    def __init__(self,app):
        self.app = app
        self.db_conexao = Conexao()

    #Função que cria todos os callbacks
    def definir_callbacks(self):
        #Esse callback ativa toda vez que a url muda e retorna uma tela dependendo do caminho da url
        @self.app.callback(Output('main-card', 'children'),Input('url','pathname'))
        def __atualizar_tela(caminho):
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

        #Ativa quando o botão da tela de cadastro é ativado, verifica se é possível o cadastro e muda a url
        @self.app.callback([Output('url','pathname', allow_duplicate=True),Output('span-cadastro-aviso','children')],[Input('btn-cad-cadastrar','n_clicks'),State('input-cd-nome','value'),State('input-cd-dtnascimento','value'),State('input-cd-email','value'),State('input-cd-senha','value')],prevent_initial_call=True)
        def __botao_cadastro(botao,nome,data,email,senha):
            if botao:
                print('||',nome,"||")
                if verificar_cadastro(nome,data,email,senha,self.db_conexao):
                    senha_bytes = senha.encode('utf-8')
                    senha = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
                    self.db_conexao.inserir_dados("login_usuarios","(email,senha)",(email,senha))
                    return ["/entrar",""]
                else:
                    return [dash.no_update,"Campos vázios, email em uso ou data inválida!"]
            else:
                return dash.no_update

        #Ativa quando o botão da tela de login é ativado, verifica se é possível o login e muda a url 
        @self.app.callback([Output('url','pathname', allow_duplicate=True),Output('span-login-aviso','children')],[Input('btn-login-entrar','n_clicks'),State('input-login-email','value'),State('input-login-senha','value')],prevent_initial_call=True)
        def __botao_login(botao,email,senha):
            if botao:
                login = self.db_conexao.verificar_login(email,senha)
                if login:
                    return ["/prox-menu",""]
                else:
                    return [dash.no_update,"E-mail ou senha inválidos"]
            else:
                return dash.no_update

        
    


