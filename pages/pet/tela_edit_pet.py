from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout(pet,id_usuario_url,id_usuario_logado):
    if str(id_usuario_url) == str(id_usuario_logado):
        layout = dbc.Card([
        
            html.H1(f'Edite o seu {pet[2]}',style={'display':'flex','align-items': 'center','justify-itemns':'center', 'color' : 'black'}),
            html.H4('Estágio da vida:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-editpet-estagio',options=[{'label':'Recém nascido','value':'Recém nascido'},{'label':'Filhote','value':'Filhote'},{'label':'Adulto','value':'Adulto'},{'label':'Velho','value':'Velho'}],value=pet[3],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Porte:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-editpet-porte',options=[{'label':'Pequeno','value':'Pequeno'},{'label':'Médio','value':'Médio'},{'label':'Grande','value':'Grande'}],value=pet[4],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Deficiência:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-editpet-deficiencia',options=[{'label':'Sim','value':'Sim'},{'label':'Não','value':'Não'}],value=pet[5],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Para crianças:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-editpet-criancas',options=[{'label':'Sim','value':'Sim'},{'label':'Não','value':'Não'}],value=pet[6],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Pode viver com outros animais:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-editpet-outros',options=[{'label':'Sim','value':'Sim'},{'label':'Não','value':'Não'}],value=pet[7],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Temperamento:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-editpet-temperamento',options=[{'label':'Calmo','value':'Calmo'},{'label':'Brincalhão','value':'Brincalhão'},{'label':'Raivoso','value':'Raivoso'}],value=pet[8],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Cor:'),
            html.Div(children=[
                dbc.Input(id='input-editpet-cor',placeholder="Insira a Cor do PET",value=pet[9],type='text', size="sm"),
            ],style={'display':'flex'}),
            html.H4('Raça:'),
            html.Div(children=[
                dbc.Input(id='input-editpet-raca',placeholder="Insira a Raça do PET",value=pet[10],type='text', size="sm"),
            ],style={'display':'flex'}),
            dbc.Button('FINALIZAR',id='btn-editpet-finalizar',color='primary',style={'margin-bottom':'7px'}),
            dbc.Button('CANCELAR',id='btn-editpet-cancelar',style={'background-color':'red'},href='/meus-pets/')     
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