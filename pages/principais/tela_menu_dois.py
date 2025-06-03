from dash import html, dcc
import dash_bootstrap_components as dbc
style_sidebar={"box-shadow": "2px 2px 10px 0px rgba(10, 9, 7, 0.10)","height":"100%","backgroundColor": "#f8f9fa",'padding':'10px'}



def return_layout(layout_interno,session_usuario):


    layout = html.Div(children=[ 
            dbc.Row([
                dbc.Col(children=[
                    dbc.Card([
                        html.Img(src='/assets/logo.png', style={
                            'height': '20%',
                            "width": "100%"
                        }),
                        html.H1(f"Olá, {session_usuario['nome']}", style={'font-family': 'Voltaire, sans-serif', 'font-size': '24px','color':'black', 'text-align': 'center','font-weight': 'bold' }),
                        dbc.Button(id='btn-menu-perfil', children='Meu Perfil', href='/perfil', style={'font-family': 'Voltaire, sans-serif', 'font-size': '18px','color':'white', 'text-align': 'center', 'margin-bottom':'10px'}),
                        dbc.Button(id='btn-menu-pets', children='Meus Pets', href='/meus-pets/', style={'font-family': 'Voltaire, sans-serif', 'font-size': '18px','color':'white', 'text-align': 'center', 'margin-bottom':'10px'}),
                        dbc.Button(id='btn-menu-buscar', children='Pets para Adoção', href='/buscar-pet/', style={'font-family': 'Voltaire, sans-serif', 'font-size': '18px','color':'white', 'text-align': 'center', 'margin-bottom':'10px'}),
                        dbc.Button(id='btn-menu-cadastrar', children='Cadastrar Pet Para Adoção', href='/cadastrar-pet', style={'font-family': 'Voltaire, sans-serif', 'font-size': '18px','color':'white', 'text-align': 'center', 'margin-bottom':'10px'}),
                        dbc.Button(id='btn-menu-buscar-perdidos', children='Pets Perdidos', href='/buscar-perdidos/', style={'font-family': 'Voltaire, sans-serif', 'font-size': '18px','color':'white', 'text-align': 'center', 'margin-bottom':'10px'}),
                        dbc.Button(id='btn-menu-perdidos', children='Cadastrar Pet Perdido', href='/pets-perdidos', style={'font-family': 'Voltaire, sans-serif', 'font-size': '18px','color':'white', 'text-align': 'center', 'margin-bottom':'10px'}),
                        
                        
                        html.Div(style={'height':'100%'}),
                        dbc.Button(id='btn-menu-sair', children='Sair', href='/entrar',style={'background-color':'red'}),
                    ], style=style_sidebar)
                ], md=2),
                dbc.Col(children=[
                    html.Div(id='tela',children=[layout_interno],style={'height':'100%'}),
                ], md=10,style={'height':'100%'})
            ],style={'height':'95%','width':'98%','margin-top':'10px'})   
    ],style={'height':'100%','width':'98%'})

        
    return layout