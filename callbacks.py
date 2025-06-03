import re
import os
import dash
import json
import base64
import bcrypt
import requests
import urllib.parse
from dash import dcc, ALL, ctx
from datetime import datetime
from db_conexao import Conexao
from dash.dependencies import Input, Output, State
from pages.principais import tela_menu, tela_cad_plataforma, tela_login, tela_menu_dois
from pages.pet import tela_cad_pet, tela_buscar_pet, tela_edit_pet, tela_meus_pets
from pages.usuario import tela_perfil, tela_cad_adotante,tela_editar_perfil, tela_editar_preferencia
from pages.perdido import tela_cad_perdido, tela_buscar_perdidos, tela_edit_perdidos

def verificar_email(email):
    try:
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
    except:
        return False


def verificar_data(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except:
        return False
    
def verificar_endereco(endereco):
    if len(endereco) != 8:
        return False
    else:
        requisicao = requests.get(f'https://viacep.com.br/ws/{endereco}/json/')
        endereco_total = requisicao.json()
        if 'erro' not in endereco_total:
            return True
    return False

def verificar_cadastro(nome,data,email,senha,telefone,endereco,db_conexao):
    email_real = verificar_email(email)
    data_real = verificar_data(data)
    email_existe = db_conexao.consultar_dados("login_usuarios","COUNT(*)",f"WHERE email = ?",(email,))
    endereco_existe = verificar_endereco(endereco)
    if None in [nome,data,email,senha,telefone,endereco] or "" in [nome,data,email,senha,telefone,endereco] or email_real == False or email_existe[0][0] > 0 or data_real == False or endereco_existe == False:
        return False
    return True

def buscar_maps(endereco):
    requisicao = requests.get(f'https://viacep.com.br/ws/{endereco}/json/')
    endereco_total = requisicao.json()
    endereco_formatado = f"{endereco_total['logradouro']}, {endereco_total['bairro']}, {endereco_total['localidade']} - {endereco_total['uf']}"
    endereco_url = urllib.parse.quote(endereco_formatado)
    return f"https://www.google.com/maps/search/?api=1&query={endereco_url}"



class Callbacks:
    def __init__(self,app):
        self.app = app
        self.db_conexao = Conexao()

    def definir_callbacks(self):
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
                        busca = caminho.split('/')[2].lower()
                        print(busca)
                        if busca in [None,"","recomendações","recomendacoes"]:
                            pets= self.db_conexao.recomendar_pets(session_usuario['id'])
                            span = ""
                        else:
                            pets = self.db_conexao.consultar_dados("pets","*",f"as p  left join usuarios as us where p.id_usuario == us.id and p.id_usuario != ? and (LOWER(especie) like '%{busca}%')",(session_usuario['id'],))
                            for i,pet in enumerate(pets):
                                pet = list(pet)
                                pet.insert(11,'?')
                                pets[i] = pet
                            span = 'Você saiu do modo de recomendações, para voltar pesquise "recomendações"'
                        print(pets)
                        layout_interno = tela_buscar_pet.return_layout(pets,span)
                    else:
                        layout_interno = tela_cad_adotante.return_layout()
                    return tela_menu_dois.return_layout(layout_interno,session_usuario)
                
                if '/buscar-perdidos/' in caminho:
                    busca = caminho.split('/')[2].lower()
                    perdidos = self.db_conexao.consultar_dados("perdidos","*",f"as p  left join usuarios as us where p.id_usuario == us.id and p.id_usuario != ? and (LOWER(especie) like '%{busca}%')",(session_usuario['id'],))
                    layout_interno = tela_buscar_perdidos.return_layout(perdidos)
                    return tela_menu_dois.return_layout(layout_interno,session_usuario)
                
                elif caminho == '/cadastrar-pet':
                    layout_interno =  tela_cad_pet.return_layout()
                    return tela_menu_dois.return_layout(layout_interno,session_usuario)
                elif caminho == '/pets-perdidos':
                    layout_interno =  tela_cad_perdido.return_layout()
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
                elif '/editar-perdidos/' in caminho:
                    id_pet = caminho.split('/')[2].split('$')[0]
                    id_usuario = caminho.split('/')[2].split('$')[1]
                    pet = self.db_conexao.consultar_dados('perdidos','*','where id = ?',(id_pet,))[0]
                    print(pet)
                    layout_interno =  tela_edit_perdidos.return_layout(pet,id_usuario,session_usuario['id'])
                    return tela_menu_dois.return_layout(layout_interno,session_usuario)
                elif  '/meus-pets' in caminho:
                    tipo = caminho.split('/')[2]
                    print(tipo)
                    if tipo == "adotados":
                        pets = self.db_conexao.consultar_dados("adotados","*",f"where id_usuario == ?",(session_usuario['id'],))
                    elif tipo == "perdidos":
                        pets = self.db_conexao.consultar_dados("perdidos","*",f"where id_usuario == ?",(session_usuario['id'],))
                    else:
                        tipo = "card"
                        pets = self.db_conexao.consultar_dados("pets","*",f"where id_usuario == ?",(session_usuario['id'],))
                    layout_interno =  tela_meus_pets.return_layout(pets,tipo,session_usuario)
                    return tela_menu_dois.return_layout(layout_interno,session_usuario)    
                elif '/tela-editar-perfil' in caminho:
                    layout_interno = tela_editar_perfil.return_layout(session_usuario)
                    return tela_menu_dois.return_layout(layout_interno, session_usuario)
                elif '/tela-editar-preferencia' in caminho:
                    layout_interno = tela_editar_preferencia.return_layout(session_usuario)
                    return tela_menu_dois.return_layout(layout_interno, session_usuario)
                
                return tela_menu.return_layout()
            else:
                return dcc.Location(href="/entrar", id="redirect-login")
            
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
            
        @self.app.callback([Output('session-login', 'data')],[Input('btn-menu-sair','n_clicks')],prevent_initial_call=True)
        def __botao_sair(botao):
            if botao:
                return [{'logado': False}]
            return dash.no_update
        



        @self.app.callback([Output('url','pathname', allow_duplicate=True),Output('span-cadastro-aviso','children')],[Input('btn-cad-cadastrar','n_clicks'),State('input-cd-nome','value'),State('input-cd-dtnascimento','value'),
        State('input-cd-email','value'),State('input-cd-senha','value'),State('input-cd-telefone','value'),State('input-cd-endereco','value')],prevent_initial_call=True)
        def __botao_cadastro(botao,nome,data,email,senha,telefone,cep):
            if botao:
                print('||',nome,"||")
                cep = re.sub(r'\D', '', cep)
                if verificar_cadastro(nome,data,email,senha,telefone,cep,self.db_conexao):
                    senha_bytes = senha.encode('utf-8')
                    senha = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
                    localizacao = buscar_maps(cep)
                    id_login = self.db_conexao.inserir_dados("login_usuarios","(email,senha)",(email,senha))
                    self.db_conexao.inserir_dados("usuarios","(id_login,nome,data_nascimento,telefone,cep,localizacao)",(id_login,nome,data,telefone,cep,localizacao))
                    return ["/entrar",""]
                else:
                    return [dash.no_update,"Campos vázios, email em uso, data ou CEP inválidos!"]
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

        @self.app.callback([Output('url', 'pathname', allow_duplicate=True), Output('session-usuario','data', allow_duplicate=True), Output('session-login', 'data', allow_duplicate=True)],[Input('btn-perfil-excluir', 'n_clicks'), State('session-usuario','data')], prevent_initial_call=True)
        def __botao_excluir_adotante(botao,session_usuario):
            if botao:
                id_usuario = session_usuario['id']
                self.db_conexao.deletar_dados('pets', 'WHERE id_usuario = ?', (id_usuario,))
                self.db_conexao.deletar_dados('perdidos', 'WHERE id_usuario = ?', (id_usuario,))
                self.db_conexao.deletar_dados('adotantes', 'WHERE id_usuario = ?', (id_usuario,))
                self.db_conexao.deletar_dados('adotados', 'WHERE id_usuario = ?', (id_usuario,))
                self.db_conexao.deletar_dados('login_usuarios', 'WHERE id = ?', (id_usuario,))
                self.db_conexao.deletar_dados('usuarios', 'WHERE id = ?', (id_usuario,))

                return ("/entrar", {}, {'logado': False})
            return dash.no_update

        @self.app.callback(
            [Output('url', 'pathname', allow_duplicate=True), Output('session-usuario', 'data', allow_duplicate=True)],
            [Input('btn-edit-alterar', 'n_clicks'),State('session-usuario','data'), State('input-edit-dtnascimento', 'value'), State('input-edit-telefone', 'value'), State('input-edit-endereco',  'value'), State('input-edit-nome', 'value')], prevent_initial_call=True)
        def __botao_editar_perfil(botao, session_usuario, data, telefone, endereco, nome):
            if botao:
                id_usuario = session_usuario['id']
                self.db_conexao.atualizar_dados("usuarios", "(data_nascimento,telefone,cep,nome)", (data, telefone, endereco, nome),f"WHERE id ={id_usuario}")
                session_usuario = self.db_conexao.coletar_dados_usuario(id_usuario)
                return("/perfil",session_usuario)
            return dash.no_update

        @self.app.callback(
            [Output('url', 'pathname', allow_duplicate=True), Output('session-usuario', 'data', allow_duplicate=True)],
            [Input('btn-editadotante-add', 'n_clicks'),State('session-usuario','data'), State('ri-editadotante-especie', 'value'), State('ri-editadotante-estagio', 'value'), State('ri-editadotante-porte',  'value'), State('ri-editadotante-deficiencia', 'value'), State('ri-editadotante-criancas', 'value'), State('ri-editadotante-outros', 'value'), State('ri-editadotante-temperamento', 'value')], prevent_initial_call=True)
        def __botao_editar_preferencias(botao, session_usuario, especie, estagio, porte, deficiencia, criancas, outros_animais, temperamento):
            if botao:
                id_usuario = session_usuario['id']
                self.db_conexao.atualizar_dados("adotantes", "(especie,estagio,porte,deficiencia,criancas,outros_animais,temperamento)", (especie,estagio,porte,deficiencia,criancas,outros_animais,temperamento),f"WHERE id ={id_usuario}")
                session_usuario = self.db_conexao.coletar_dados_usuario(id_usuario)
                return("/perfil",session_usuario)
            return dash.no_update





        @self.app.callback([Output('span-cadpet-aviso','children', allow_duplicate=True)],[Input('btn-cadpet-add','n_clicks'),
        State('ri-cadpet-especie','value'),State('ri-cadpet-estagio','value'),State('ri-cadpet-porte','value'),State('ri-cadpet-deficiencia','value'),
        State('ri-cadpet-criancas','value'),State('ri-cadpet-outros','value'),State('ri-cadpet-temperamento','value'),
        State('input-cadpet-cor','value'),State('input-cadpet-raca','value'),State('session-usuario', 'data'),
        State('upload-image', 'contents')],prevent_initial_call=True)
        def __botao_cadastro_pet(botao,especie,estagio,porte,deficiencia,criancas,outros,temperamento,cor,raca,session_usuario,conteudo):
            if botao:
                    id_pet = self.db_conexao.inserir_dados("pets","(id_usuario,especie,estagio,porte,deficiencia,criancas,outros_animais,temperamento,cor,raca)",(session_usuario['id'],especie,estagio,porte,deficiencia,criancas,outros,temperamento,cor,raca))
                    if conteudo is not None:
                        data = conteudo.encode("utf8").split(b";base64,")[1]
                        caminho_imagem = f'./assets/imagens/card_{id_pet}.jpg'
                        
                        with open(caminho_imagem, "wb") as fp:
                            fp.write(base64.decodebytes(data))
                    return ["Cadastro efetuado com sucesso"]
            else:
                return dash.no_update
            
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input('btn-buscar-busca','n_clicks'),State('input-buscar-busca','value')],prevent_initial_call=True)
        def __botao_pesquisa_pet(botao,pesquisa):
            if botao:
                    if pesquisa == None:
                        pesquisa = ""
                    return [f"/buscar-pet/{pesquisa}"]
            else:
                return dash.no_update
        
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input({'type': 'btn-card-adotar', 'index': ALL},'n_clicks'),State('session-usuario', 'data')],prevent_initial_call=True)
        def __botao_adotar_pet(botao,session_usuario):
            if set(botao)!={None}:
                triggered_id = ctx.triggered_id
                if triggered_id:
                    id_pet = triggered_id['index']
                    adotado = self.db_conexao.consultar_dados('pets','*','where id = ?',(id_pet,))[0]
                    print(adotado)
                    valores_adotado = tuple(list(adotado)[2:])
                    id_adotado = self.db_conexao.inserir_dados('adotados',"(id_usuario,especie,estagio,porte,deficiencia,criancas,outros_animais,temperamento,cor,raca)",(session_usuario['id'],)+  (valores_adotado))
                    self.db_conexao.deletar_dados('pets','WHERE id = ?',(id_pet,))
                    os.rename(f"./assets/imagens/card_{id_pet}.jpg", f"./assets/imagens/adotar_{id_adotado}.jpg")
                    return ['/buscar-pet/']
            return dash.no_update
        
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input({'type': 'btn-card-editar', 'index': ALL},'n_clicks')],prevent_initial_call=True)
        def __botao_editar_pet(botao):
            if set(botao)!={None}:
                triggered_id = ctx.triggered_id
                if triggered_id:
                    id_pet = triggered_id['index']
                    adotado = self.db_conexao.consultar_dados('pets','*','where id = ?',(id_pet,))
                    id_usuario = adotado[0][1]
                    return [f'/editar-pet/{id_pet}${id_usuario}']
            return dash.no_update
        
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input('btn-editpet-finalizar','n_clicks'),State('url','pathname'),State('ri-editpet-estagio','value'),
                            State('ri-editpet-porte','value'),State('ri-editpet-deficiencia','value'),State('ri-editpet-criancas','value'),
                            State('ri-editpet-outros','value'),State('ri-editpet-temperamento','value'),
                            State('input-editpet-cor','value'),State('input-editpet-raca','value')],prevent_initial_call=True)
        def __botao_atualizar_pet(botao,caminho,estagio,porte,deficiencia,criancas,outros_animais,temperamento,cor,raca):
            if botao:
                    id_pet = caminho.split('/')[2].split('$')[0]
                    self.db_conexao.atualizar_dados("pets","(estagio,porte,deficiencia,criancas,outros_animais,temperamento,cor,raca)",(estagio,porte,deficiencia,criancas,outros_animais,temperamento,cor,raca),f"WHERE id ={id_pet}")
                    return ["/meus-pets/"]
            else:
                return dash.no_update
            
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input({'type': 'btn-card-excluir', 'index': ALL},'n_clicks')],prevent_initial_call=True)
        def __botao_excluir_pet(botao):
            if set(botao)!={None}:
                triggered_id = ctx.triggered_id
                if triggered_id:
                    id_pet = triggered_id['index']
                    self.db_conexao.deletar_dados('pets','WHERE id = ?',(id_pet,))
                    return ['/meus-pets/']
            return dash.no_update





        @self.app.callback([Output('span-perdidos-aviso','children', allow_duplicate=True)],[Input('btn-perdidos-add','n_clicks'),
        State('ri-perdidos-especie','value'),State('ri-perdidos-estagio','value'),State('ri-perdidos-porte','value'),
        State('ri-perdidos-temperamento','value'),State('input-perdidos-cor','value'),State('input-perdidos-raca','value'),
        State('input-perdidos-nome','value'),State('input-perdidos-descricao','value'),State('input-perdidos-recompensa','value'),
        State('session-usuario', 'data'),State('upload-image-perdido', 'contents')],prevent_initial_call=True)
        def __botao_cadastro_perdido(botao,especie,estagio,porte,temperamento,cor,raca,nome,descricao,recompensa,session_usuario,conteudo):
            if botao:
                    id_perdido = self.db_conexao.inserir_dados("perdidos","(id_usuario,especie,estagio,porte,temperamento,cor,raca,nome,descricao,recompensa)",(session_usuario['id'],especie,estagio,porte,temperamento,cor,raca,nome,descricao,recompensa))
                    if conteudo is not None:
                        data = conteudo.encode("utf8").split(b";base64,")[1]
                        caminho_imagem = f'./assets/imagens/perdidos_{id_perdido}.jpg'
                        
                        with open(caminho_imagem, "wb") as fp:
                            fp.write(base64.decodebytes(data))
                    return ["Cadastro efetuado com sucesso"]
            else:
                return dash.no_update
            
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input('btn-perdidos-busca','n_clicks'),State('input-perdidos-busca','value')],prevent_initial_call=True)
        def __botao_pesquisa_perdido(botao,pesquisa):
            if botao:
                    if pesquisa == None:
                        pesquisa = ""
                    return [f"/buscar-perdidos/{pesquisa}"]
            else:
                return dash.no_update
        
        
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input({'type': 'btn-perdidos-editar', 'index': ALL},'n_clicks')],prevent_initial_call=True)
        def __botao_editar_perdido(botao):
            if set(botao)!={None}:
                triggered_id = ctx.triggered_id
                if triggered_id:
                    id_perdidos = triggered_id['index']
                    adotado = self.db_conexao.consultar_dados('perdidos','*','where id = ?',(id_perdidos,))
                    id_usuario = adotado[0][1]
                    return [f'/editar-perdidos/{id_perdidos}${id_usuario}']
            return dash.no_update  
        
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input('btn-editperdidos-finalizar','n_clicks'),State('url','pathname'),
                            State('ri-editperdidos-estagio','value'),State('ri-editperdidos-porte','value'),
        State('ri-editperdidos-temperamento','value'),State('input-editperdidos-cor','value'),State('input-editperdidos-raca','value'),
        State('input-editperdidos-nome','value'),State('input-editperdidos-descricao','value'),State('input-editperdidos-recompensa','value')],prevent_initial_call=True)
        def __botao_atualizar_perdido(botao,caminho,estagio,porte,temperamento,cor,raca,nome,descricao,recompensa):
            if botao:
                    id_pet = caminho.split('/')[2].split('$')[0]
                    self.db_conexao.atualizar_dados("perdidos","(estagio,porte,temperamento,cor,raca,nome,descricao,recompensa)",(estagio,porte,temperamento,cor,raca,nome,descricao,recompensa),f"WHERE id ={id_pet}")
                    return ["/meus-pets/perdidos"]
            else:
                return dash.no_update
            
        @self.app.callback([Output('url','pathname', allow_duplicate=True)],[Input({'type': 'btn-perdidos-excluir', 'index': ALL},'n_clicks')],prevent_initial_call=True)
        def __botao_excluir_perdido(botao):
            if set(botao)!={None}:
                triggered_id = ctx.triggered_id
                if triggered_id:
                    id_pet = triggered_id['index']
                    self.db_conexao.deletar_dados('perdidos','WHERE id = ?',(id_pet,))
                    return ['/meus-pets/perdidos']
            return dash.no_update


