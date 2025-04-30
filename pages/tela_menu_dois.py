from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout():

    layout = dbc.Card([
        # html.Img(src='assets\logo_5.png',style={'padding':'20px','padding-bottom':'40px',}),
        dbc.Button('Adotar PET', id='btn-adotarpet',href='/adotar-pet', color='success', style={'background-color': '#0c581e'}),
        html.Div(style={'margin':'5px'}),
        dbc.Button('Cadastrar PET', id='btn-cadastrarpet',href='/cadastrar-pet', color='success', style={'background-color': '#0c581e'}),
        html.Span('',style={'text-aling':'center'}),

    ])

        
    return layout