from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout(pet,id_usuario_url,id_usuario_logado):
    if str(id_usuario_url) == str(id_usuario_logado):
        layout = dbc.Card([
        
            html.H1(f'Edite o seu {pet[2]}',style={'display':'flex','align-items': 'center','justify-itemns':'center', 'color' : 'black'}),
            html.H4('Estágio da vida:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-editpet-estagio',options=[{'label':'Recém nascido','value':'rc'},{'label':'Filhote','value':'filhote'},{'label':'Adulto','value':'adulto'},{'label':'Velho','value':'Velho'}],value=pet[3],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Cor:'),
            html.Div(children=[
                dbc.Input(id='input-editpet-cor',placeholder="Insira a Cor do PET",value=pet[4],type='text', size="sm"),
            ],style={'display':'flex'}),
            html.H4('Raça:'),
            html.Div(children=[
                dbc.Input(id='input-editpet-raca',placeholder="Insira a Raça do PET",value=pet[5],type='text', size="sm"),
            ],style={'display':'flex'}),
            html.Hr(style={'margin-top': '3px','margin-bottom': '10px'}),
            dbc.Button('FINALIZAR',id='btn-editpet-finalizar',color='primary',style={'margin-bottom':'7px'}),
            dbc.Button('CANCELAR',id='btn-editpet-cancelar',style={'background-color':'red'},href='/perfil')     
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