from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout_preferencias(session_usuario):
    if("especie" in session_usuario.keys()):
        layout =html.Div(children=[
                html.Div(children=[
                html.H3("SUAS PREFERÊNCIAS", className="text-center mb-4", style={'fontWeight': 'bold','color':'black'}),

                html.H4("Animal que deseja:", style = {'color':'black'}),
                html.H6(id='h6-perfil-especie',children=session_usuario['especie']),

                html.H4("Estágio da vida do animal desejado:", style = {'color': 'black'}),
                html.H6(id='h6-perfil-estagio',children=session_usuario['estagio']),
                
                html.H4("Porte do Animal desejado: "),
                html.H6(id='h6-perfil-porte',children=session_usuario['porte']),

                html.H4("Deseja que o animal possua alguma deficiência?"),
                html.H6(id='h6-perfil-deficiencia',children=session_usuario['deficiencia']),
        
                html.H4("Quer que o animal seja adaptado a crianças? "),
                html.H6(id='h6-perfil-criancas',children=session_usuario['criancas']),
                
                html.H4("Quer que o animal seja adaptado a outros animais? "),
                html.H6(id='h6-perfil-outros_animais',children=session_usuario['outros_animais']),
                
                html.H4("Qual o temperamento esperado do Animal? "),
                html.H6(id='h6-perfil-temperamento',children=session_usuario['temperamento']),
                
                ])
            ])
        return layout
    else:
        return html.Div()
def return_layout(session_usuario):
    print(session_usuario)
    layout_preferencias = return_layout_preferencias(session_usuario)
    layout = dbc.Card(
        dbc.CardBody([
            html.Div(children=[
                html.Div(children=[
                html.H3("SEU PERFIL", className="text-center mb-4", style={'fontWeight': 'bold','color':'black'}),

                html.H4("Nome:", style = {'color':'black'}),
                html.H6(id='h6-perfil-nome',children=session_usuario['nome']),

                html.H4("Data de nascimento:", style = {'color': 'black'}),
                html.H6(id='h6-perfil-data',children=session_usuario['data']),
                
                html.H4("Endereço: "),
                html.H6(id='h6-perfil-endereco',children=session_usuario['endereco']),

                html.H4("Telefone:"),
                html.H6(id='h6-perfil-telefone',children=session_usuario['telefone']),
        
                ])
            ]),
            layout_preferencias
            
        ],style={'height':'100%','display':'inline-table','width':'100%'}),
        className="shadow-sm p-4",

        style={
            "width": "100%",
            "height":"100%",
            "borderRadius": "12px",
            "backgroundColor": "#f8f9fa"
        }
    )
    return layout