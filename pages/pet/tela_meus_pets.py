from dash import html, dcc
import dash_bootstrap_components as dbc

def gerar_cards(pets,tipo):
    linhas = []
    cards = []
    count = 1
    qtd_pets = len(pets)
    
    for i, pet in enumerate(pets):
        if tipo != 'adotados':
            botoes = html.Div(children=[
                            dbc.Button(id={'type': f'btn-{tipo}-editar', 'index': pet[0]},children='Editar',style={'margin':'5px'}),
                            dbc.Button(id={'type': f'btn-{tipo}-excluir', 'index': pet[0]},children='Excluir',style={'margin':'5px','background-color':'red'})
                    ])
        else:
            botoes = html.Div()
        if count <= 3:
            card = dbc.Col([
                    dbc.Card([
                        html.Img(src=f'../assets/imagens/{tipo}_{pet[0]}.jpg', style={'height':'50%','width':'100%'}),
                        html.Div(children = [
                            html.H4(f"Animal: {pet[2]}"),
                            html.H4(f"Estágio: {pet[3]}"),
                            html.H4(f"Porte: {pet[4]}"),
                            html.H4(f"Deficiência: {pet[5]}"),
                            html.H4(f"Para crianças: {pet[6]}"),
                            html.H4(f"Outros animais: {pet[7]}"),
                            html.H4(f"Temperamento: {pet[8]}"),
                            html.H4(f"Cor: {pet[9]}"),
                            html.H4(f"Raça: {pet[10]}"),
                        ],style={'overflowY': 'auto'}),
                        botoes
                    ],style={"box-shadow": "2px 2px 10px 0px rgba(10, 9, 7, 0.10)","backgroundColor": "#DCDCDC","widht":'100%','height':'100%',"margin-bottom":'10px'})
                ], md=4,style={'height':'100%'})
            # card = dbc.Col([
            #         dbc.Card([
            #             html.H4(f"Animal: {pet[2]}"),
            #             html.H4(f"Estágio: {pet[3]}"),
            #             html.H4(f"Cor: {pet[4]}"),
            #             html.H4(f"Espécie: {pet[5]}"),
            #             dbc.Button(id={'type': f'btn-{tipo}-editar', 'index': pet[0]},children='Editar',style={'margin':'5px'}),
            #             dbc.Button(id={'type': f'btn-{tipo}-excluir', 'index': pet[0]},children='Excluir',style={'margin':'5px','background-color':'red'})
            #         ],style={"box-shadow": "2px 2px 10px 0px rgba(10, 9, 7, 0.10)","backgroundColor": "#DCDCDC","widht":'100%','height':'95%',"margin-bottom":'10px'})
            #     ], md=4)
            cards.append(card)  
        if count ==3 or count >= qtd_pets:
            print(pet)
            linha = dbc.Row(cards,style={'width':'100%','height':'75%'})
            linhas.append(linha)
            cards = []
            qtd_pets -= count
            count = 0
        count += 1
    return linhas

def return_layout(pets,tipo,session_usuario):
    print(session_usuario)
    cards = gerar_cards(pets,tipo)
    print(pets)
    layout = dbc.Card(children=[
                html.H3("MEUS PETS", className="text-center mb-4", style={'fontWeight': 'bold','color':'black'}),
                html.Div(children=[
                    dbc.Button("Para adoção",href="/meus-pets/para-adocao",style={"margin":"10px"}), 
                    dbc.Button("Adotados",href="/meus-pets/adotados",style={"margin":"10px"}),
                    dbc.Button("Perdidos",href="/meus-pets/perdidos", style={"margin":"10px"}),
                ]),
                html.Div(children=cards,style={'height':'100%','overflowY': 'auto'})
            ],className="shadow-sm p-4",style={"width": "100%","height":"100%","borderRadius": "12px","backgroundColor": "#f8f9fa"}
            )
    return layout