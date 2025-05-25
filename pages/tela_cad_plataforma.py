from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout():
    layout = dbc.Card(
    dbc.CardBody([
        html.H3("CADASTRO DE USUÁRIO", className="text-center mb-4", style={'fontWeight': 'bold','color':'black'}),

        html.H4("Nome:", style = {'color':'black'}),
        dbc.Input(id='input-cd-nome', placeholder="Digite seu nome completo", type='text', size="sm", className="mb-3"),

        html.H4("Data de nascimento:", style = {'color': 'black'}),
        dbc.Input(id='input-cd-dtnascimento', placeholder="DD/MM/AAAA", type='text', size="sm", className="mb-3"),

        html.H4("Telefone:"),
        dbc.Input(id='input-cd-telefone', placeholder="(00) 00000-0000", type='text', size="sm", className="mb-3"),

        html.H4("Endereco:"),
        dbc.Input(id='input-cd-endereco', placeholder="Município-UF", type='text', size="sm", className="mb-3"),

        html.H4("Email:"),
        dbc.Input(id='input-cd-email', placeholder="Digite seu email", type='email', size="sm", className="mb-3"),

        html.H4("Senha:"),
        dbc.Input(id='input-cd-senha', placeholder="Crie uma senha", type='password', size="sm", className="mb-3"),

        html.Span(id='span-cadastro-aviso', className="text-warning text-center d-block mb-2"),

        dbc.Button("CADASTRAR", id='btn-cad-cadastrar', color="primary", className="w-100 mb-2", size="md"),
        dbc.Button("VOLTAR", id="btn-cad-voltar", href="/", color="secondary", className="w-100", size="md"),
    
        
        html.Span(id='span-add-final', className="text-success text-center d-block")
    ],style={'maxHeigth':'200px','display':'inline-table'}),
    className="shadow-sm p-4",

    style={
        "maxWidth": "700px",
        "width": "100%",
        "borderRadius": "12px",
        "backgroundColor": "#f8f9fa"
    }
)
    return layout