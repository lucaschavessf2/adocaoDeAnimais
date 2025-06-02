from dash import html, dcc
import dash_bootstrap_components as dbc

card_style = {
    'width':'500px',

    'min-height' :'250px',
    'padding-top':'5px',
    'padding-right':'25px',
    'padding-left':'25px',
    'padding-bottom':'25px',
    'align-self':'center',
    'margin-bottom':'100px'
}


def return_layout():

    layout = dbc.Card([
        # html.Img(src='assets\logo_5.png',style={'padding':'20px','padding-bottom':'40px',}),
        dbc.Button('ENTRAR', id='btn-entrar',href='/entrar', color='success', style={'background-color': '#0c581e'}),
        html.Div(style={'margin':'5px'}),
        dbc.Button('CADASTRAR', id='btn-cadastrar',href='/cadastrar', color='success', style={'background-color': '#0c581e'}),
        html.Span('',style={'text-aling':'center'}),

    ],style=card_style)

        
    return layout