from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout():
    layout = dbc.Card([
        html.H1('CADASTRO USUÁRIO',style={'display':'flex','align-items': 'center','justify-itemns':'center'}),
        html.H4('Nome: '),
        html.Div(children=[
            dbc.Input(id='input-cd-nome',placeholder="",type='text', size="sm"),
        ],style={'display':'flex'}),
        html.H4('DATA DE NASCIMENTO:'),
        html.Div(children=[
            dbc.Input(id='input-cd-dtnascimento',placeholder="(DD/MM/YYYY)",type='text', size="sm"),
        ],style={'display':'flex'}),
        html.H4('Email: '),
        html.Div(children=[
            dbc.Input(id='input-cd-email',placeholder="",type="email", size="sm"),
        ],style={'display':'flex'}),
        
        html.H4('Senha:'),
        html.Div(children=[
            dbc.Input(id='input-cd-senha',placeholder="",type='password', size="sm"),
        ],style={'display':'flex'}),
        html.Hr(style={'margin-top': '3px','margin-bottom': '10px'}),
        dbc.Button('CADASTRAR',id='btn-cad-cadastrar',color='success', style={'background-color': '#0c581e'}),
        html.Span(id='span-add-final',style={'color':'#fd7e14','text-aling':'center'}),  
    ])
    return layout