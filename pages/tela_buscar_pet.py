from dash import html, dcc
import dash_bootstrap_components as dbc

def gerar_cards(pets):
    linhas = []
    cards = []
    count = 1
    qtd_pets = len(pets)
    for i, pet in enumerate(pets):
        if count <= 3:
            card = dbc.Col([
                    dbc.Card([
                        html.H4(f"Animal: {pet[2]}"),
                        html.H4(f"Estágio: {pet[3]}"),
                        html.H4(f"Cor: {pet[4]}"),
                        html.H4(f"Espécie: {pet[5]}"),
                        html.H4(f"Responsável: {pet[8]}"),
                        dbc.Button(id={'type': 'btn-card-adotar', 'index': pet[0]},children='Adotar',style={'margin':'5px'})
                    ],style={"box-shadow": "2px 2px 10px 0px rgba(10, 9, 7, 0.10)","backgroundColor": "#DCDCDC","widht":'100%','height':'95%',"margin-bottom":'10px'})
                ], md=4)
            cards.append(card)  
        if count ==3 or count >= qtd_pets:
            print(pet)
            linha = dbc.Row(cards,style={'width':'100%','height':'60%'})
            linhas.append(linha)
            cards = []
            qtd_pets -= count
            count = 0
        count += 1
    return linhas
def return_layout(pets):
    cards = gerar_cards(pets)
    layout = dbc.Card(
        dbc.CardBody([
            html.H3("RECOMENDAÇÕES DE PET", className="text-center mb-4", style={'fontWeight': 'bold','color':'black'}),
            html.Hr(style={'width':'100%'}),
            html.Div(children=[
                dbc.Input(id='input-buscar-busca', placeholder="Pesquise aqui seu próximo animal", type='text', size="sm", className="mb-3"),
                dbc.Button(id='btn-buscar-busca',children='Pesquisar',style={'margin-left':'5px','height':'68%'}, size="sm")
            ],style={'display':'flex','width':'100%'}),
            html.Div(id='div-rec-itens',children=cards,style={'overflowY': 'auto','width':'100%','height':'90%'}),

            
        ],style={'height':'100%','display':'flex','width':'100%','flex-wrap':'wrap'}),
        className="shadow-sm p-4",

        style={
            "width": "100%",
            "height":"100%",
            "borderRadius": "12px",
            "backgroundColor": "#f8f9fa"
        }
    )
    return layout