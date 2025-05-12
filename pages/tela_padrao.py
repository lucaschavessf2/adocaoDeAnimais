from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout():
    layout = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.Div([
                dcc.Location(id='url', refresh=False),
                dcc.Store(id='session-login', data={'logado': False}, storage_type='session'),
                dcc.Store(id='session-usuario', storage_type='session'),
                html.Div(id="main-card",children=[], className="d-flex flex-column justify-content-center align-items-center", style={"height": "100vh"})  
            ], ),
            width=12
        ),
    style={"backgroundImage": "url('/assets/Design-sem-nome-69.png')",}),
    fluid=True,
    className="bg-light"
)
    return layout