from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout():
    layout = dbc.Card(
    dbc.CardBody([
        html.Img(src='/assets/logo.png', style={
        'height': '35%',
        "width": "95%"
    }),
        html.P("Com Petmatch, seu par perfeito te espera para um lar cheio de amor.", style={'text-aling':'center', 'fontWeight': 'bold'}),
        
        html.Div([
            dbc.Label("Email:", html_for="input-login-email", className="mb-1"),
            dbc.Input(id="input-login-email", type="email", placeholder="Digite seu email", className="mb-3", size="md")
        ]),

        html.Div([
            dbc.Label("Senha:", html_for="input-login-senha", className="mb-1"),
            dbc.Input(id="input-login-senha", type="password", placeholder="Digite sua senha", className="mb-3", size="md")
        ]),

        html.Span(id='span-login-aviso', className="text-warning text-center d-block mb-2"),

        dbc.Button("Entrar", id="btn-login-entrar", color="primary", className="w-100 mb-2", size="md"),
        dbc.Button("Cadastrar", id="btn-login-cadastrar", href="/cadastrar", color="success", className="w-100", size="md"),
    ]),
    className="shadow-sm p-4",
    style={
        "maxWidth": "500px",
        "width": "100%",
        "borderRadius": "12px",
        "backgroundColor": "#ffffff"
    }
)
    return layout