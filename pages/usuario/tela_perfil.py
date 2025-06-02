from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout_preferencias(session_usuario):
    if("especie" in session_usuario.keys()):
        layout =html.Div(children=[
                html.H3("SUAS PREFERÊNCIAS", className="text-center mb-4", style={'fontWeight': 'bold','color':'black'}),
                html.Div(children=[
                
                html.Div(children=[
                    html.H4("Animal que deseja:", style = {'color':'black','fontWeight': 'bold'}),
                    html.H6(id='h6-perfil-especie',children=session_usuario['especie']),

                    html.H4("Estágio da vida do animal desejado:", style = {'color': 'black','fontWeight': 'bold'}),
                    html.H6(id='h6-perfil-estagio',children=session_usuario['estagio']),
                    
                    html.H4("Porte do Animal desejado: ",style={'fontWeight': 'bold'}),
                    html.H6(id='h6-perfil-porte',children=session_usuario['porte']),

                    html.H4("Deseja que o animal possua alguma deficiência?",style={'fontWeight': 'bold'}),
                    html.H6(id='h6-perfil-deficiencia',children=session_usuario['deficiencia'])
                ],style={'height':'100%','width':'45%'}),
                html.Div(children=[
                    html.H4("Quer que o animal seja adaptado a crianças? ",style={'fontWeight': 'bold'}),
                    html.H6(id='h6-perfil-criancas',children=session_usuario['criancas']),
                    
                    html.H4("Quer que o animal seja adaptado a outros animais? ",style={'fontWeight': 'bold'}),
                    html.H6(id='h6-perfil-outros_animais',children=session_usuario['outros_animais']),
                    
                    html.H4("Qual o temperamento esperado do Animal? ",style={'fontWeight': 'bold'}),
                    html.H6(id='h6-perfil-temperamento',children=session_usuario['temperamento'])
                ],style={'height':'100%','width':'50%'}),

                html.Div(
                   dbc.Button("Editar ", id="btn-preferencia-editar",href="/tela-editar-preferencia")
                )
                ],style={'height':'75%','overflowY': 'auto','background-color':'#e5e5e5','border-radius':'12px','padding':'12px','display':'flex'})
            ],style={'height':'70%'})
        return layout
    else:
        return html.Div()
def return_layout(session_usuario):
    print(session_usuario)
    layout_preferencias = return_layout_preferencias(session_usuario)
    layout = dbc.Card(children=[
            html.H3("SEU PERFIL", className="text-center mb-4", style={'fontWeight': 'bold','color':'black'}),
            html.Div(children=[
                
                html.Div(children=[
                    html.H4("Nome:", style = {'color':'black','fontWeight': 'bold'}),
                    html.H6(id='h6-perfil-nome',children=session_usuario['nome']),

                    html.H4("Data de nascimento:", style = {'color': 'black','fontWeight': 'bold'}),
                    html.H6(id='h6-perfil-data',children=session_usuario['data']),
                ],style={'height':'100%','width':'45%'}),
                html.Div(children=[
                    html.H4("CEP: ",style={'fontWeight': 'bold'}),
                    html.H6(id='h6-perfil-endereco',children=session_usuario['cep']),

                    html.H4("Telefone:",style={'fontWeight': 'bold'}),
                    html.H6(id='h6-perfil-telefone',children=session_usuario['telefone']),
                ],style={'height':'100%','width':'50%'}),
                

                html.Div(
                    dbc.Button("Editar", id="btn-perfil-editar", href='/tela-editar-perfil')
                )
                
            ],style={'height':'20%','display':'flex','background-color':'#e5e5e5','border-radius':'12px','padding':'12px','margin-bottom':'15px'}),
            layout_preferencias,

            html.Div(children=[
                dbc.Button(children="Excluir Conta", id = "btn-perfil-excluir",style={'background-color':'red'})
            ],style={'height':'10%'})],

        style={
            "width": "100%",
            "height":"100%",
            "borderRadius": "12px",
            "backgroundColor": "#f8f9fa",
            "padding":"15px"
        }
)
    return layout