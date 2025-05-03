from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout():
    layout = dbc.Card([
        html.H1('LOGIN',style={'display':'flex','align-items': 'center','justify-itemns':'center'}),
        html.H4('Email: '),
        html.Div(children=[
            dbc.Input(id='input-login-email',placeholder="",type="email", size="sm"),
        ],style={'display':'flex'}),
        
        html.H4('Senha:'),
        html.Div(children=[
            dbc.Input(id='input-login-senha',placeholder="",type='password', size="sm"),
        ],style={'display':'flex'}),
        html.Hr(style={'margin-top': '3px','margin-bottom': '10px'}),
        html.Span(id='span-login-aviso',style={'color':'#fd7e14','text-aling':'center'}),
        html.Hr(style={'margin-top': '3px','margin-bottom': '10px'}),
        dbc.Button('ENTRAR',id='btn-login-entrar',color='success', style={'background-color': '#0c581e'}),
         
    ])
    return layout