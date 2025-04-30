from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout():
    layout = dbc.Container(
    dbc.Row(
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Location(id='url',refresh=False),
                    html.Div(id="main-card",children=[
                    ])   
                ]),className="shadow p-4",style={"backgroundColor": "#f8f9fa", "borderRadius": "20px"}
            ),width=8,className="d-flex justify-content-center align-items-center flex-column",
        ),className="vh-100 d-flex justify-content-center align-items-center"
    ),fluid=True,className="bg-light"
)
    return layout