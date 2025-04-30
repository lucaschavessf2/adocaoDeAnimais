from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout():
    layout = dbc.Card([
        html.H1('CADASTRO DE PET',style={'display':'flex','align-items': 'center','justify-itemns':'center'}),
        html.H4('Espécie:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-cadpet-especie',options=[{'label':'Gato','value':'gato'},{'label':'Cachorro','value':'cahorro'},{'label':'Ave','value':'ave'},{'label':'Réptil','value':'réptil'},{'label':'Peixe','value':'peixe'},{'label':'Outro','value':'outro'}],inline=True),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Estágio da vida:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-cadpet-estagio',options=[{'label':'Recém nascido','value':'rc'},{'label':'Filhote','value':'filhote'},{'label':'Adulto','value':'adulto'},{'label':'Velho','value':'Velho'}],inline=True),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Cor:'),
        html.Div(children=[
            dbc.Input(id='input-cadpet-cor',placeholder="",type='text', size="sm"),
        ],style={'display':'flex'}),
        html.H4('Raça:'),
        html.Div(children=[
            dbc.Input(id='input-cadpet-raca',placeholder="Descrição",type='text', size="sm"),
        ],style={'display':'flex'}),
        html.H4('Foto:'),
        html.Div(children=[
            dbc.Input(id='input-cadpet-foto',placeholder="Valor",type="number", size="sm"),
        ],style={'display':'flex'}),
        html.Hr(style={'margin-top': '3px','margin-bottom': '10px'}),
        dbc.Button('ADICIONAR',id='btn-cadpet-add',color='success', style={'background-color': '#0c581e'}),
        html.Span(id='span-add-final',style={'color':'#fd7e14','text-aling':'center'}),  
    ])
    return layout