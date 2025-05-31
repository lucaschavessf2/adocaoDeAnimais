import re
import dash
import bcrypt
from dash import dcc, ALL, ctx
from datetime import datetime
from db_conexao import Conexao
from dash.dependencies import Input, Output, State
from pages import tela_menu,tela_cad_plataforma,tela_login,tela_menu_dois,tela_cad_pet,tela_buscar_pet,tela_perfil,tela_edit_pet,tela_cad_adotante, tela_pet_perdido, tela_meus_pets, tela_buscar_perdidos

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
def verificar_cadastro(nome,data,email,senha,telefone,endereco,db_conexao):
    email_real = verificar_email(email)
    data_real = verificar_data(data)
    email_existe = db_conexao.consultar_dados("login_usuarios","COUNT(*)",f"WHERE email = ?",(email,))
    if None in [nome,data,email,senha,telefone,endereco] or "" in [nome,data,email,senha,telefone,endereco] or email_real == False or email_existe[0][0] > 0 or data_real == False:
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
        @self.app.callback(Output('main-card', 'children'),Input('url','pathname'),State('session-login', 'data'),State('session-usuario', 'data'))
        def __atualizar_tela(caminho,session_data,session_usuario):
            print(caminho)
            logado = session_data.get('logado', False)
            print(logado)
            if caminho in  ['/','/entrar']:
                return tela_login.return_layout()
            elif caminho == '/cadastrar':
                return tela_cad_plataforma.return_layout()
            if logado:
                if '/buscar-pet/' in caminho:
                    adotantes = self.db_conexao.consultar_dados("adotantes","COUNT(*)",f"WHERE id_usuario = ?",(session_usuario['id'],))
                    print(adotantes[0][0],'----------')
                    if adotantes[0][0]>0:
                        busca = caminho.split('/')[2]
                        print(busca)
                        pets = self.db_conexao.consultar_dados("pets","*",f"as p  left join usuarios as us where p.id_usuario == us.id and p.id_usuario != ? and (especie like '%{busca}%')",(session_usuario['id'],))
                        layout_interno = tela_buscar_pet.return_layout(pets)
                    else:
                        layout_interno = tela_cad_adotante.return_layout()
                    return tela_menu_dois.return_layout(layout_interno,session_usuario)
                
                if '/buscar-perdidos/' in caminho:

                    busca = caminho.split('/')[2]
                    print(busca)
                    perdidos = self.db_conexao.consultar_dados("perdidos","*",f"as p  left join usuarios as us where p.id_usuario == us.id and p.id_usuario != ? and (especie like '%{busca}%')",(session_usuario['id'],))
                    layout_interno = tela_buscar_perdidos.return_layout(perdidos)
                    return tela_menu_dois.return_layout(layout_interno,session_usuario)
                
                elif caminho == '/cadastrar-pet':
                    layout_interno =  tela_cad_pet.return_layout()
                    return tela_menu_dois.return_layout(layout_interno,session_usuario)
                elif caminho == '/pets-perdidos':
                    layout_interno =  tela_pet_perdido.return_layout()
                    return tela_menu_dois.return_layout(layout_interno,session_usuario)
                elif caminho == '/perfil':
                    layout_interno =  tela_perfil.return_layout(session_usuario)
                    return tela_menu_dois.return_layout(layout_interno,session_usuario)
                elif '/editar-pet/' in caminho:
                    id_pet = caminho.split('/')[2].split('$')[0]
                    id_usuario = caminho.split('/')[2].split('$')[1]
                    pet = self.db_conexao.consultar_dados('pets','*','where id = ?',(id_pet,))[0]
                    layout_interno =  tela_edit_pet.return_layout(pet,id_usuario,session_usuario['id'])
                    return tela_menu_dois.return_layout(layout_interno,session_usuario)
                elif caminho == '/meus-pets':
                    pets = self.db_conexao.consultar_dados("pets","*",f"where id_usuario == ?",(session_usuario['id'],))
                    layout_interno =  tela_meus_pets.return_layout(pets,session_usuario)
                    return tela_menu_dois.return_layout(layout_interno,session_usuario)    
                    
                
                return tela_menu.return_layout()
            else:
                return dcc.Location(href="/entrar", id="redirect-login")

        #Ativa quando o botão da tela de cadastro é ativado, verifica se é possível o cadastro e muda a url
        @self.app.callback([Output('url','pathname', allow_duplicate=True),Output('span-cadastro-aviso','children')],[Input('btn-cad-cadastrar','n_clicks'),State('input-cd-nome','value'),State('input-cd-dtnascimento','value'),
        State('input-cd-email','value'),State('input-cd-senha','value'),State('input-cd-telefone','value'),State('input-cd-endereco','value')],prevent_initial_call=True)
        def __botao_cadastro(botao,nome,data,email,senha,telefone,endereco):
            if botao:
                print('||',nome,"||")
                if verificar_cadastro(nome,data,email,senha,telefone,endereco,self.db_conexao):
                    senha_bytes = senha.encode('utf-8')
                    senha = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
                    id_login = self.db_conexao.inserir_dados("login_usuarios","(email,senha)",(email,senha))
                    self.db_conexao.inserir_dados("usuarios","(id_login,nome,data_nascimento,telefone,endereco)",(id_login,nome,data,telefone,endereco))
                    return ["/entrar",""]
                else:
                    return [dash.no_update,"Campos vázios, email em uso ou data inválida!"]
            else:
                return dash.no_update

        #Ativa quando o botão da tela de login é ativado, verifica se é possível o login e muda a url 
        @self.app.callback([Output('session-login', 'data', allow_duplicate=True),Output('url','pathname', allow_duplicate=True),Output('span-login-aviso','children'),Output('session-usuario', 'data')],[Input('btn-login-entrar','n_clicks'),State('input-login-email','value'),State('input-login-senha','value')],prevent_initial_call=True)
        def __botao_login(botao,email,senha):
            if botao:
                login = self.db_conexao.verificar_login(email,senha)
                if login[0]:
                    dados_usuario = self.db_conexao.coletar_dados_usuario(login[1])
                    return [{'logado': True},'/buscar-pet/',"",dados_usuario]
                else:
                    return [dash.no_update,dash.no_update,"E-mail ou senha inválidos",dash.no_update]
            else:
                return dash.no_update

        #Ativa quando o botão da tela de cadastro é ativado
        @self.app.callback([Output('span-cadpet-aviso','children', allow_duplicate=True)],[Input('btn-cadpet-add','n_clicks'),
        State('ri-cadpet-especie','value'),State('ri-cadpet-estagio','value'),State('ri-cadpet-porte','value'),State('ri-cadpet-deficiencia','value'),
        State('ri-cadpet-criancas','value'),State('ri-cadpet-outros','value'),State('ri-cadpet-temperamento','value'),
        State('input-cadpet-cor','value'),State('input-cadpet-raca','value'),State('session-usuario', 'data')],prevent_initial_call=True)
        def __botao_cadastro_pet(botao,especie,estagio,porte,deficiencia,criancas,outros,temperamento,cor,raca,session_usuario):
            if botao:
                    self.db_conexao.inserir_dados("pets","(id_usuario,especie,estagio,porte,deficiencia,criancas,outros_animais,temperamento,cor,raca)",(session_usuario['id'],especie,estagio,porte,deficiencia,criancas,outros,temperamento,cor,raca))
                    return ["Cadastro efetuado com sucesso"]
            else:
                return dash.no_update
        @self.app.callback([Output('span-perdidos-aviso','children', allow_duplicate=True)],[Input('btn-perdidos-add','n_clicks'),
        State('ri-perdidos-especie','value'),State('ri-perdidos-estagio','value'),State('ri-perdidos-porte','value'),State('ri-perdidos-deficiencia','value'),
        State('ri-perdidos-criancas','value'),State('ri-perdidos-outros','value'),State('ri-perdidos-temperamento','value'),
        State('input-perdidos-cor','value'),State('input-perdidos-raca','value'),State('session-usuario', 'data')],prevent_initial_call=True)
        def __botao_cadastro_perdidos(botao,especie,estagio,porte,deficiencia,criancas,outros,temperamento,cor,raca,session_usuario):
            if botao:
                    self.db_conexao.inserir_dados("perdidos","(id_usuario,especie,estagio,porte,deficiencia,criancas,outros_animais,temperamento,cor,raca)",(session_usuario['id'],especie,estagio,porte,deficiencia,criancas,outros,temperamento,cor,raca))
                    return ["Cadastro efetuado com sucesso"]
                    
            else:
                return dash.no_update
    
            
        @self.app.callback([Output('url','pathname', allow_duplicate=True),Output('span-cadadotante-aviso','children', allow_duplicate=True),Output('session-usuario','data', allow_duplicate=True)],[Input('btn-cadadotante-add','n_clicks'),
        State('ri-cadadotante-especie','value'),State('ri-cadadotante-estagio','value'),State('ri-cadadotante-porte','value'),State('ri-cadadotante-deficiencia','value'),
        State('ri-cadadotante-criancas','value'),State('ri-cadadotante-outros','value'),State('ri-cadadotante-temperamento','value'),State('session-usuario', 'data')],prevent_initial_call=True)
        def __botao_cadastro_adotante(botao,especie,estagio,porte,deficiencia,criancas,outros,temperamento,session_usuario):
            if botao:
                self.db_conexao.inserir_dados("adotantes","(id_usuario,especie,estagio,porte,deficiencia,criancas,outros_animais,temperamento)",(session_usuario['id'],especie,estagio,porte,deficiencia,criancas,outros,temperamento))
                dados_usuario = self.db_conexao.coletar_dados_usuario(session_usuario["id"])
                return ["/buscar-pet/","Cadastro efetuado com sucesso",dados_usuario]
            else:
                return dash.no_update
            
        @self.app.callback([Output('session-login', 'data')],[Input('btn-menu-sair','n_clicks')],prevent_initial_call=True)
        def __botao_sair(botao):
            if botao:
                return [{'logado': False}]
            return dash.no_update


        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input('btn-buscar-busca','n_clicks'),State('input-buscar-busca','value')],prevent_initial_call=True)
        def __botao_pesquisa(botao,pesquisa):
            if botao:
                    if pesquisa == None:
                        pesquisa = ""
                    return [f"/buscar-pet/{pesquisa}"]
            else:
                return dash.no_update
            
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input('btn-perdidos-busca','n_clicks'),State('input-perdidos-busca','value')],prevent_initial_call=True)
        def __botao_pesquisa_perdidos(botao,pesquisa):
            if botao:
                    if pesquisa == None:
                        pesquisa = ""
                    return [f"/buscar-perdidos/{pesquisa}"]
            else:
                return dash.no_update
            
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input({'type': 'btn-card-adotar', 'index': ALL},'n_clicks'),State('session-usuario', 'data')],prevent_initial_call=True)
        def __botao_adotar(botao,session_usuario):
            if set(botao)!={None}:
                triggered_id = ctx.triggered_id
                if triggered_id:
                    id_pet = triggered_id['index']
                    adotado = self.db_conexao.consultar_dados('pets','*','where id = ?',(id_pet,))[0]
                    print(adotado)
                    valores_adotado = (adotado[2],adotado[3],adotado[9],adotado[10])
                    self.db_conexao.inserir_dados('adotados',"(id_usuario,especie,estagio,cor,raca)",(session_usuario['id'],)+  (valores_adotado))
                    self.db_conexao.deletar_dados('pets','WHERE id = ?',(id_pet,))
                    # print((session_usuario['id'],)+(tuple(list(adotado[0])[2:])))
                    return ['/buscar-pet/']
            return dash.no_update
        
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input({'type': 'btn-card-excluir', 'index': ALL},'n_clicks')],prevent_initial_call=True)
        def __botao_excluir(botao):
            if set(botao)!={None}:
                triggered_id = ctx.triggered_id
                if triggered_id:
                    id_pet = triggered_id['index']
                    self.db_conexao.deletar_dados('pets','WHERE id = ?',(id_pet,))
                    return ['/perfil']
            return dash.no_update
        
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input({'type': 'btn-card-editar', 'index': ALL},'n_clicks')],prevent_initial_call=True)
        def __botao_editar(botao):
            if set(botao)!={None}:
                triggered_id = ctx.triggered_id
                if triggered_id:
                    id_pet = triggered_id['index']
                    adotado = self.db_conexao.consultar_dados('pets','*','where id = ?',(id_pet,))
                    id_usuario = adotado[0][1]
                    return [f'/editar-pet/{id_pet}${id_usuario}']
            return dash.no_update
        
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input('btn-editpet-finalizar','n_clicks'),State('url','pathname'),State('ri-editpet-estagio','value'),State('input-editpet-cor','value'),State('input-editpet-raca','value')],prevent_initial_call=True)
        def __botao_atualizar_pet(botao,caminho,estagio,cor,raca):
            if botao:
                    id_pet = caminho.split('/')[2].split('$')[0]
                    self.db_conexao.atualizar_dados("pets","(estagio,cor,raca)",(estagio,cor,raca),f"WHERE id ={id_pet}")
                    return ["/perfil"]
            else:
                return dash.no_update


