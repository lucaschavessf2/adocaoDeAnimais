from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout():
    layout = dbc.Card([
    
        html.H1('CADASTRO PET PERDIDO',style={'display':'flex','align-items': 'center','justify-itemns':'center', 'color' : 'black'}),
        html.H4('Espécie:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-perdidos-especie',options=[{'label':'Gato','value':'gato'},{'label':'Cachorro','value':'cachorro'},{'label':'Ave','value':'ave'},{'label':'Réptil','value':'réptil'},{'label':'Peixe','value':'peixe'},{'label':'Outro','value':'outro'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Estágio da vida:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-perdidos-estagio',options=[{'label':'Recém nascido','value':'Recém nascido'},{'label':'Filhote','value':'Filhote'},{'label':'Adulto','value':'Adulto'},{'label':'Velho','value':'Velho'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Porte:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-perdidos-porte',options=[{'label':'Pequeno','value':'Pequeno'},{'label':'Médio','value':'Médio'},{'label':'Grande','value':'Grande'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Temperamento:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-perdidos-temperamento',options=[{'label':'Calmo','value':'Calmo'},{'label':'Brincalhão','value':'Brincalhão'},{'label':'Raivoso','value':'Raivoso'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Cor:'),
        html.Div(children=[
            dbc.Input(id='input-perdidos-cor',placeholder="Insira a Cor do PET",type='text', size="sm"),
        ],style={'display':'flex'}),
        html.H4('Raça:'),
        html.Div(children=[
            dbc.Input(id='input-perdidos-raca',placeholder="Insira a Raça do PET",type='text', size="sm"),
        ],style={'display':'flex'}),
        html.H4('Nome:'),
        html.Div(children=[
            dbc.Input(id='input-perdidos-nome',placeholder="Insira o nome do seu PET",type='text', size="sm"),
        ],style={'display':'flex'}),
        html.H4('Descrição do animal:'),
        html.Div(children=[
            dbc.Input(id='input-perdidos-descricao',placeholder="Insira uma descrição do seu PET",type='text', size="sm"),
        ],style={'display':'flex'}),
        html.H4('Recompensa:'),
        html.Div(children=[
            dbc.Input(id='input-perdidos-recompensa',placeholder="Insira uma recompensa",type='text', size="sm"),
        ],style={'display':'flex'}),
        html.Hr(style={'margin-top': '3px','margin-bottom': '10px'}),
        html.Span(id='span-perdidos-aviso',style={'color':'#fd7e14','text-aling':'center'}),
        dbc.Button('ADICIONAR',id='btn-perdidos-add',color='primary')     
    ]
        ,style = {
            "height":"100%",
            "background-color" : "white",
            "padding":"20px"
        }
    )

    return layout