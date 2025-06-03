from dash import html, dcc
import dash_bootstrap_components as dbc

def gerar_cards(perdidos):
    linhas = []
    cards = []
    count = 1
    qtd_perdidos = len(perdidos)
    for i, perdido in enumerate(perdidos):
        if count <= 3:
            card = dbc.Col([
                    dbc.Card([
                        html.Img(src=f'../assets/imagens/perdidos_{perdido[0]}.jpg', style={'height':'50%','width':'100%',"object-fit": "cover","padding-bottom":"3px","border-radius":"10px"}),
                        html.Div(children = [
                            html.H3(f"{perdido[2]}"),
                            html.Hr(style={'size':'4px','color':'grey'}),
                            html.Div(children=[
                                html.Div(children=[
                                    html.H5(f"Nome: {perdido[8]}"),
                                    html.H5(f"Raça: {perdido[7]}"),
                                    html.H5(f"Temperamento: {perdido[5]}"),
                                    html.H5(f"Descrição: {perdido[9]}")
                                ],style={'width':'50%'}),
                                html.Div(children=[
                                    html.H5(f"Cor: {perdido[6]}"),
                                    html.H5(f"Porte: {perdido[4]}"),
                                    html.H5(f"Estagio: {perdido[3]}"),
                                    html.H5(f"Recompensa: {perdido[10]}"),
                                    
                                    
                                ],style={'width':'50%'}),
                            ],style={'display':'flex'}),
                            html.Hr(style={'size':'4px','color':'grey'}),
                            html.H5(f"Responsável: {perdido[13]}"),
                            html.H5(f"Contato: {perdido[17]}"),
                            html.H5(f"CEP: {perdido[15]}"),
                            html.A(children="Ver endereço",href=perdido[16],target="_blank")
                        ],style={'overflowY': 'auto',"width":"100%","padding":"10px","backgroundColor": "#EEEEEE","border-left":'10px'}),
                        dbc.Button(id={'type': 'btn-card-encontrar', 'index': perdido[0]},children='Adotar',style={'margin':'5px','width':'80%'})
                ],style={"box-shadow": "2px 2px 10px 0px rgba(10, 9, 7, 0.10)","backgroundColor": "#EEEDED","widht":'100%','height':'95%',"margin-bottom":'10px',"font-family": 'Segoe UI',"border-radius":'16px',"flex-direction": "column","display":"flex","align-items":"center"})
                ], md=4,style={'height':'100%'})
            cards.append(card)  
        if count ==3 or count >= qtd_perdidos:
            print(perdidos)
            linha = dbc.Row(cards,style={'width':'100%','height':'80%'})
            linhas.append(linha)
            cards = []
            qtd_perdidos -= count
            count = 0
        count += 1
    return linhas
def return_layout(perdidos):
    cards = gerar_cards(perdidos)
    layout = dbc.Card(children=[
        html.H3("PETS PERDIDOS", className="text-center mb-4", style={'fontWeight': 'bold','color':'black'}),
        html.Hr(style={'width':'100%'}),
        html.Div(children=[
            dbc.Input(id='input-perdidos-busca', placeholder="Pesquise aqui seu próximo animal", type='text', size="sm", className="mb-3"),
            dbc.Button(id='btn-perdidos-busca',children='Pesquisar',style={'margin-left':'5px','height':'68%'}, size="sm")
        ],style={'display':'flex','width':'100%'}),
        html.Div(id='div-rec-itens',children=cards,style={'overflowY': 'auto','width':'100%','height':'90%'}),

    ],style={"width": "100%","height":"100%","borderRadius": "12px","backgroundColor": "#f8f9fa","padding":"20px"})
    return layout