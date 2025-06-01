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
                        html.H4(f"Animal: {perdido[2]}"),
                        html.H4(f"Estágio: {perdido[3]}"),
                        html.H4(f"Porte: {perdido[4]}"),
                        html.H4(f"Deficiência: {perdido[5]}"),
                        html.H4(f"Para crianças: {perdido[6]}"),
                        html.H4(f"Outros animais: {perdido[7]}"),
                        html.H4(f"Temperamento: {perdido[8]}"),
                        html.H4(f"Cor: {perdido[9]}"),
                        html.H4(f"Raça: {perdido[10]}"),
                        html.H4(f"Responsável: {perdido[13]}"),
                        html.H4(f"Endereço: {perdido[15]}"),
                        html.H4(f"Contato: {perdido[16]}"),
                        dbc.Button(id={'type': 'btn-card-encontrar', 'index': perdido[0]},children='Encontrei',style={'margin':'5px'})
                    ],style={"box-shadow": "2px 2px 10px 0px rgba(10, 9, 7, 0.10)","backgroundColor": "#DCDCDC","widht":'100%','height':'95%',"margin-bottom":'10px'})
                ], md=4)
            cards.append(card)  
        if count ==3 or count >= qtd_perdidos:
            print(perdidos)
            linha = dbc.Row(cards,style={'width':'100%','height':'65%'})
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