from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout(pet,id_usuario_url,id_usuario_logado):
    if str(id_usuario_url) == str(id_usuario_logado):
        layout = dbc.Card([
        
            html.H4('Estágio da vida:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-editperdidos-estagio',options=[{'label':'Recém nascido','value':'Recém nascido'},{'label':'Filhote','value':'Filhote'},{'label':'Adulto','value':'Adulto'},{'label':'Velho','value':'Velho'}],value = pet [3],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Porte:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-editperdidos-porte',options=[{'label':'Pequeno','value':'Pequeno'},{'label':'Médio','value':'Médio'},{'label':'Grande','value':'Grande'}],value = pet [4],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Temperamento:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-editperdidos-temperamento',options=[{'label':'Calmo','value':'Calmo'},{'label':'Brincalhão','value':'Brincalhão'},{'label':'Raivoso','value':'Raivoso'}],value = pet [5],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Cor:'),
        html.Div(children=[
            dbc.Input(id='input-editperdidos-cor',placeholder="Insira a Cor do PET",type='text',value = pet [6], size="sm"),
        ],style={'display':'flex'}),
        html.H4('Raça:'),
        html.Div(children=[
            dbc.Input(id='input-editperdidos-raca',placeholder="Insira a Raça do PET",type='text',value = pet [7], size="sm"),
        ],style={'display':'flex'}),
        html.H4('Nome:'),
        html.Div(children=[
            dbc.Input(id='input-editperdidos-nome',placeholder="Insira o nome do seu PET",type='text',value = pet [8], size="sm"),
        ],style={'display':'flex'}),
        html.H4('Descrição do animal:'),
        html.Div(children=[
            dbc.Input(id='input-editperdidos-descricao',placeholder="Insira uma descrição do seu PET",type='text',value = pet [9], size="sm"),
        ],style={'display':'flex'}),
        html.H4('Recompensa:'),
        html.Div(children=[
            dbc.Input(id='input-editperdidos-recompensa',placeholder="Insira uma recompensa",type='text',value = pet [10], size="sm"),
        ],style={'display':'flex'}),
            dbc.Button('FINALIZAR',id='btn-editperdidos-finalizar',color='primary',style={'margin-bottom':'7px'}),
            dbc.Button('CANCELAR',id='btn-editperdidos-cancelar',style={'background-color':'red'},href='/perfil')     
        ]
            ,style = {
                "background-color" : "white",
                "padding":"20px"
            }
        )
    else:
        layout = dbc.Card([
        
            html.H1('PET NÃO ENCONTRADO',style={'display':'flex','align-items': 'center','justify-itemns':'center', 'color' : 'black'}),

        ]
            ,style = {
                "background-color" : "white",
                "padding":"20px"
            }
        )

    return layout