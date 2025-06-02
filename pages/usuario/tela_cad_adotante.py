from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout():
    layout = dbc.Card([
    
        html.H1('SUAS PREFERÊNCIAS',style={'display':'flex','align-items': 'center','justify-itemns':'center', 'color' : 'black'}),
        html.H4('Espécie:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-cadadotante-especie',options=[{'label':'Gato','value':'gato'},{'label':'Cachorro','value':'cachorro'},{'label':'Ave','value':'ave'},{'label':'Réptil','value':'réptil'},{'label':'Peixe','value':'peixe'},{'label':'Outro','value':'outro'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Estágio da vida:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-cadadotante-estagio',options=[{'label':'Recém nascido','value':'Recém nascido'},{'label':'Filhote','value':'Filhote'},{'label':'Adulto','value':'Adulto'},{'label':'Velho','value':'Velho'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Porte:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-cadadotante-porte',options=[{'label':'Pequeno','value':'Pequeno'},{'label':'Médio','value':'Médio'},{'label':'Grande','value':'Grande'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Deficiência:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-cadadotante-deficiencia',options=[{'label':'Sim','value':'Sim'},{'label':'Não','value':'Não'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Para crianças:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-cadadotante-criancas',options=[{'label':'Sim','value':'Sim'},{'label':'Não','value':'Não'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Pode viver com outros animais:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-cadadotante-outros',options=[{'label':'Sim','value':'Sim'},{'label':'Não','value':'Não'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.H4('Temperamento:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-cadadotante-temperamento',options=[{'label':'Calmo','value':'Calmo'},{'label':'Brincalhão','value':'Brincalhão'},{'label':'Raivoso','value':'Raivoso'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
        ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
        html.Hr(style={'margin-top': '3px','margin-bottom': '10px'}),
        html.Span(id='span-cadadotante-aviso',style={'color':'#fd7e14','text-aling':'center'}),
        dbc.Button('Finalizar',id='btn-cadadotante-add',color='primary')     
    ]
        ,style = {
            "height":"100%",
            "background-color" : "white",
            "padding":"20px"
        }
    )

    return layout