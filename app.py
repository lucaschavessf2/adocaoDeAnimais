import dash
import webbrowser 
from pages import tela_padrao
import dash_bootstrap_components as dbc
from callbacks import Callbacks


if __name__ == "__main__":
    app = dash.Dash(__name__,external_stylesheets=[dbc.themes.DARKLY], suppress_callback_exceptions=True)
    app.layout= tela_padrao.return_layout()
    app.config.suppress_callback_exceptions = True
    callbacks = Callbacks(app)
    callbacks.definir_callbacks()
    #webbrowser.open_new_tab('http://localhost:8050')
    app.run(port=8050, debug=True)
                   