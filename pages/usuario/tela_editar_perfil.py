from dash import html, dcc
import dash_bootstrap_components as dbc


def return_layout(session_usuario):
    layout = dbc.Card(
        dbc.CardBody([
            html.H3("Editar Usuário", className="text-center mb-4",
                    style={'fontWeight': 'bold', 'color': 'black'}),

            html.H4("Nome:", style={'color': 'black'}),
            dbc.Input(id='input-edit-nome', placeholder="Digite seu nome completo", value=session_usuario['nome'], type='text', size="sm",
                      className="mb-3"),

            html.H4("Data de nascimento:", style={'color': 'black'}),
            dbc.Input(id='input-edit-dtnascimento', placeholder="DD/MM/AAAA", value=session_usuario['data'], type='text', size="sm", className="mb-3"),

            html.H4("Telefone:"),
            dbc.Input(id='input-edit-telefone', placeholder="(00) 00000-0000",  value=session_usuario['telefone'], type='text', size="sm", className="mb-3"),

            html.H4("CEP:"),
            dbc.Input(id='input-edit-endereco', placeholder="00000-000", value=session_usuario['cep'], type='text', size="sm", className="mb-3"),

            html.Span(id='span-edit-aviso', className="text-warning text-center d-block mb-2"),

            dbc.Button("ALTERAR", id='btn-edit-alterar', color="primary", className="w-100 mb-2", size="md"),
            dbc.Button("VOLTAR", id="btn-edit-voltar", href="/perfil", color="secondary", className="w-100", size="md"),

        ], style={'maxHeigth': '200px', 'display': 'inline-table'}),
        className="shadow-sm p-4",

        style={
            "maxWidth": "700px",
            "width": "100%",
            "borderRadius": "12px",
            "backgroundColor": "#f8f9fa"
        }
    )
    return layout