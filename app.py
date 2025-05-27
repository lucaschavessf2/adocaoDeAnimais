import dash
import webbrowser 
from pages import tela_padrao
import dash_bootstrap_components as dbc
from callbacks import Callbacks

#Código inicial, cria uma aplicação dash e inicia o servidor
if __name__ == "__main__":
    #Inicia a aplicação
    app = dash.Dash(__name__,external_stylesheets=[dbc.themes.DARKLY], suppress_callback_exceptions=True)
    #Utiliza o template padrão para a tela
    app.layout= tela_padrao.return_layout()
    app.config.suppress_callback_exceptions = True
    #Inicia a classe e os callbacks
    callbacks = Callbacks(app)
    callbacks.definir_callbacks()
    # webbrowser.open_new_tab('http://localhost:8050')
    #Inicia o servidor
    app.run(port=8050, debug=True)
                   