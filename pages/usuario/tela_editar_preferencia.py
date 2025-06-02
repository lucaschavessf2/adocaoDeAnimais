from dash import html, dcc
import dash_bootstrap_components as dbc


def return_layout(session_usuario):
    layout = dbc.Card([

        html.H1('SUAS PREFERÊNCIAS',
                style={'display': 'flex', 'align-items': 'center', 'justify-itemns': 'center', 'color': 'black'}),
        html.H4('Espécie:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-editadotante-especie',
                           options=[{'label': 'Gato', 'value': 'Gato'}, {'label': 'Cachorro', 'value': 'Cachorro'},
                                    {'label': 'Ave', 'value': 'Ave'}, {'label': 'Réptil', 'value': 'Réptil'},
                                    {'label': 'Peixe', 'value': 'Peixe'}, {'label': 'Outro', 'value': 'Outro'}],
                           value=session_usuario['especie'],inline=True, inputStyle={"color": "black", "background-color": 'grey'}),
        ], style={'display': 'flex', 'align-items': 'center', 'justify-itemns': 'center'}),
        html.H4('Estágio da vida:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-editadotante-estagio', options=[{'label': 'Recém nascido', 'value': 'Recém nascido'},
                                                                 {'label': 'Filhote', 'value': 'Filhote'},
                                                                 {'label': 'Adulto', 'value': 'Adulto'},
                                                                 {'label': 'Velho', 'value': 'Velho'}], inline=True,
                           value=session_usuario['estagio'],inputStyle={"color": "black", "background-color": 'grey'}),
        ], style={'display': 'flex', 'align-items': 'center', 'justify-itemns': 'center'}),
        html.H4('Porte:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-editadotante-porte',
                           options=[{'label': 'Pequeno', 'value': 'Pequeno'}, {'label': 'Médio', 'value': 'Médio'},
                                    {'label': 'Grande', 'value': 'Grande'}], inline=True,
                           value=session_usuario['porte'],inputStyle={"color": "black", "background-color": 'grey'}),
        ], style={'display': 'flex', 'align-items': 'center', 'justify-itemns': 'center'}),
        html.H4('Deficiência:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-editadotante-deficiencia',
                           options=[{'label': 'Sim', 'value': 'Sim'}, {'label': 'Não', 'value': 'Não'}], inline=True,
                           value=session_usuario['deficiencia'],inputStyle={"color": "black", "background-color": 'grey'}),
        ], style={'display': 'flex', 'align-items': 'center', 'justify-itemns': 'center'}),
        html.H4('Para crianças:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-editadotante-criancas',
                           options=[{'label': 'Sim', 'value': 'Sim'}, {'label': 'Não', 'value': 'Não'}], inline=True,
                           value=session_usuario['criancas'],inputStyle={"color": "black", "background-color": 'grey'}),
        ], style={'display': 'flex', 'align-items': 'center', 'justify-itemns': 'center'}),
        html.H4('Pode viver com outros animais:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-editadotante-outros',
                           options=[{'label': 'Sim', 'value': 'Sim'}, {'label': 'Não', 'value': 'Não'}], inline=True,
                           value=session_usuario['outros_animais'],inputStyle={"color": "black", "background-color": 'grey'}),
        ], style={'display': 'flex', 'align-items': 'center', 'justify-itemns': 'center'}),
        html.H4('Temperamento:'),
        html.Div(children=[
            dbc.RadioItems(id='ri-editadotante-temperamento', options=[{'label': 'Calmo', 'value': 'Calmo'},
                                                                      {'label': 'Brincalhão', 'value': 'Brincalhão'},
                                                                      {'label': 'Raivoso', 'value': 'Raivoso'}],
                           value=session_usuario['temperamento'],inline=True, inputStyle={"color": "black", "background-color": 'grey'}),
        ], style={'display': 'flex', 'align-items': 'center', 'justify-itemns': 'center'}),
        html.Hr(style={'margin-top': '3px', 'margin-bottom': '10px'}),
        html.Span(id='span-editadotante-aviso', style={'color': '#fd7e14', 'text-aling': 'center'}),
        dbc.Button('Finalizar', id='btn-editadotante-add', color='primary')
    ]
        , style={
            "height": "100%",
            "background-color": "white",
            "padding": "20px"
        }
    )

    return layout