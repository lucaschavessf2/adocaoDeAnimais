from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout():
    layout = dbc.Card([
    
        html.H1('CADASTRO DE PET',style={'display':'flex','align-items': 'center','justify-itemns':'center', 'color' : 'black'}),
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
            dbc.Input(id='input-cadpet-cor',placeholder="Insira a Cor do PET",type='text', size="sm"),
        ],style={'display':'flex'}),
        html.H4('Raça:'),
        html.Div(children=[
            dbc.Input(id='input-cadpet-raca',placeholder="Insira a Raça do PET",type='text', size="sm"),
        ],style={'display':'flex'}),
        html.Hr(style={'margin-top': '3px','margin-bottom': '10px'}),
        html.Span(id='span-cadpet-aviso',style={'color':'#fd7e14','text-aling':'center'}),
        dbc.Button('ADICIONAR',id='btn-cadpet-add',color='primary')     
    ]
        ,style = {
            "background-color" : "grey",
        }
    )

    return layout