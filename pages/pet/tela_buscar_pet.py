from dash import html, dcc
import dash_bootstrap_components as dbc

def gerar_cards(pets):
    linhas = []
    cards = []
    count = 1
    qtd_pets = len(pets)
    for i, pet in enumerate(pets):
        print(pet)
        if count <= 3:
            card = dbc.Col([
                    dbc.Card([
                        html.Img(src=f'../assets/imagens/card_{pet[0]}.jpg', style={'height':'50%','width':'100%',"object-fit": "cover","padding-bottom":"3px","border-radius":"10px"}),
                        html.Div(children = [
                            html.H3(f"{pet[2]}"),
                            html.Hr(style={'size':'4px','color':'grey'}),
                            html.Div(children=[
                                html.Div(children=[
                                    html.H5(f"Raça: {pet[10]}"),
                                    html.H5(f"Estágio: {pet[3]}"),
                                    html.H5(f"Deficiência: {pet[5]}"),
                                    html.H5(f"Para crianças: {pet[6]}")
                                ],style={'width':'50%'}),
                                html.Div(children=[
                                    html.H5(f"Cor: {pet[9]}"),
                                    html.H5(f"Porte: {pet[4]}"),
                                    html.H5(f"Outros animais: {pet[7]}"),
                                    html.H5(f"Temperamento: {pet[8]}"),
                                    
                                    
                                ],style={'width':'50%'}),
                            ],style={'display':'flex'}),
                            html.Hr(style={'size':'4px','color':'grey'}),
                            html.H5(f"Responsável: {pet[14]}"),
                            html.H5(f"Contato: {pet[18]}"),
                            html.H5(f"CEP: {pet[16]}"),
                            html.A(children="Ver endereço",href=pet[17],target="_blank")
                        ],style={'overflowY': 'auto',"width":"100%","padding":"10px","backgroundColor": "#EEEEEE","border-left":'10px'}),
                        dbc.Button(id={'type': 'btn-card-adotar', 'index': pet[0]},children='Adotar',style={'margin':'5px','width':'80%'})
                ],style={"box-shadow": "2px 2px 10px 0px rgba(10, 9, 7, 0.10)","backgroundColor": "#EEEDED","widht":'100%','height':'95%',"margin-bottom":'10px',"font-family": 'Segoe UI',"border-radius":'16px',"flex-direction": "column","display":"flex","align-items":"center"})
                ], md=4,style={'height':'100%'})
            cards.append(card)  
        if count ==3 or count >= qtd_pets:
            print(pet)
            linha = dbc.Row(cards,style={'width':'100%','height':'80%'})
            linhas.append(linha)
            cards = []
            qtd_pets -= count
            count = 0
        count += 1
    return linhas
# def return_layout(pets):
#     cards = gerar_cards(pets)
#     layout = dbc.Card(
#         dbc.CardBody([
#             html.H3("RECOMENDAÇÕES DE PET", className="text-center mb-4", style={'fontWeight': 'bold','color':'black'}),
#             html.Hr(style={'width':'100%'}),
#             html.Div(children=[
#                 dbc.Input(id='input-buscar-busca', placeholder="Pesquise aqui seu próximo animal", type='text', size="sm", className="mb-3"),
#                 dbc.Button(id='btn-buscar-busca',children='Pesquisar',style={'margin-left':'5px','height':'68%'}, size="sm")
#             ],style={'display':'flex','width':'100%'}),
#             html.Div(id='div-rec-itens',children=cards,style={'overflowY': 'auto','width':'100%','height':'90%'}),

            
#         ],style={'height':'100%','display':'flex','width':'100%','flex-wrap':'wrap'}),
#         className="shadow-sm p-4",

#         style={
#             "width": "100%",
#             "height":"100%",
#             "borderRadius": "12px",
#             "backgroundColor": "#f8f9fa"
#         }
#     )
#     return layout

def return_layout(pets):
    cards = gerar_cards(pets)
    layout = dbc.Card(children=[
        html.H3("RECOMENDAÇÕES DE PET", className="text-center mb-4", style={'fontWeight': 'bold','color':'black'}),
        html.Hr(style={'width':'100%'}),
        html.Div(children=[
            dbc.Input(id='input-buscar-busca', placeholder="Pesquise aqui seu próximo animal", type='text', size="sm", className="mb-3"),
            dbc.Button(id='btn-buscar-busca',children='Pesquisar',style={'margin-left':'5px','height':'68%'}, size="sm")
        ],style={'display':'flex','width':'100%'}),
        html.Div(id='div-rec-itens',children=cards,style={'overflowY': 'auto','width':'100%','height':'90%'}),
    ],style={"width": "100%","height":"100%","borderRadius": "12px","backgroundColor": "#f8f9fa", "padding":'20px'})
    return layout