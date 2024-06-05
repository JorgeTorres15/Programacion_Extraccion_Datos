import mysql.connector
import pandas as pd
from Dataframes import combinar_datos, obtener_conexion, extraer_todas_tablas, imprimir_tablas
import dash_bootstrap_components as dbc
# Importar funciones personalizadas desde el modulo Dataframes
from dash import Dash, html, dcc, dash_table, callback, Input, Output, State
# Inicializar la aplicacion Dash con un tema Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# se define una funcion para crear componentes visuales personalizados
def componentes(title, value, image_path):
    return html.Div(
        dbc.Card([
            dbc.CardImg(src=image_path, top=True, style={"width": "100px", "alignSelf": "center"}),
            dbc.CardBody([
                html.P(value, className="card-value",
                       style={"margin": "0px", "fontSize": "22px", "fontWeight": "bold"}),
                html.H4(title, className="card-title",
                        style={"margin": "0px", "fontSize": "18px", "fontWeight": "bold"})
            ], style={"textAlign": "center"}),
        ], style={"paddingBlock": "10px", "backgroundColor": "#19BB11", "border": "none", "borderRadius": "10px"})
    )

# estilos personalizados para las pestañas
tab_style = {
    "idle": {
        "borderRadius": "10px",
        "padding": "0px",
        "marginInline": "5px",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
        "fontWeight": "bold",
        "backgroundColor": "#F7FC8F",
        "border": "none",
        "color": "black"
    },
    "active": {
        "borderRadius": "10px",
        "padding": "0px",
        "marginInline": "5px",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
        "fontWeight": "bold",
        "border": "none",
        "textDecoration": "underline",
        "backgroundColor": "#F7FC8F",
        "color": "black"
    }
}

# Definir la estructura del diseño de la aplicacion
def diseño():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col(html.Img(src="./assets/meta.png", width=300,
                                 style={"display": "block", "margin": "auto"}), width=12),
                dbc.Col(
                    dcc.Tabs(id="graph-tabs", value="overview", children=[
                        dcc.Tab(label="Inicio ", value="overview", style=tab_style["idle"],
                                selected_style=tab_style["active"]),
                        dcc.Tab(label="Dashboard 1", value="publishers", style=tab_style["idle"],
                                selected_style=tab_style["active"]),
                        dcc.Tab(label="Dashboard 2", value="genres", style=tab_style["idle"],
                                selected_style=tab_style["active"]),
                        dcc.Tab(label="Dashboard 3", value="platforms", style=tab_style["idle"],
                                selected_style=tab_style["active"]),
                        dcc.Tab(label="Github", value="github", style=tab_style["idle"],
                                selected_style=tab_style["active"],
                                children=dcc.Link(href="https://github.com/JorgeTorres15/Programacion_Extraccion_Datos/issues", children="Da click para ir al repositorio", target="_blank"))
                    ], style={"marginTop": "15px", "width": "600px", "height": "50px"}),
                    width=6),
                dbc.Col(
                    html.Div([
                    ], style={"display": "flex", "justifyContent": "flex-end", "marginTop": "20px"}),
                    width=4
                )
            ]),
            dbc.Row([
                dbc.Col(componentes("Videojuegos", "366", "./assets/LINKGOAT.png"), width=3),
                dbc.Col(componentes("Desarrollador", "146", "./assets/desarrolador.png"), width=3),
                dbc.Col(componentes("Genero", "59", "./assets/genero.png"), width=3),
                dbc.Col(componentes("Publicado por", "80", "./assets/publisher.png"), width=3),
                dbc.Col(componentes("Plataforma", "22", "./assets/SACKBOY.png"), width=3),
            ], style={"marginBlock": "12px"}),
            dbc.Row([
                dbc.Col([
                    dcc.Loading([
                        html.Div(id="graph-tabs-content")
                    ], type="default", color="#19BB11")
                ], width=12)
            ], style={"marginBottom": "20px"}),

            dbc.Row([
                dcc.Tabs(id="tabs", value="all", children=[
                    dcc.Tab(label="Lista de juegos", value="all", style=tab_style["idle"],
                            selected_style=tab_style["active"]),
                    dcc.Tab(label="Juegos con mejor rating", value="top_rated", style=tab_style["idle"],
                            selected_style=tab_style["active"]),
                    dcc.Tab(label="Juegos con peor rating", value="worst_rated", style=tab_style["idle"],
                            selected_style=tab_style["active"]),
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Loading([
                        html.Div(id="tabs-content")
                    ], type="default", color="#19BB11")
                ], width=12)
            ], style={"marginBottom": "20px"})
        ])
    ], style={"backgroundColor": "black", "minHeight": "100vh"})

#Establecer el diseño de la aplicacn con la funcion definida
app.layout = diseño()

# Definir el callback para actualizar el contenido basado en la pestaña seleccionada
@app.callback(
    Output("tabs-content", "children"),
    [Input("tabs", "value")]
)
def update_content(tab):
    config = {
        "user": "root",
        "password": "",
        "host": "localhost",
        "database": "Metacritics"
    }
    conn = obtener_conexion(config)
    # Especificar las tablas a extraer
    tablas = ["Plataforma", "Desarrollador", "Publicado_por", "Genero", "Videojuegos"]
    dataframes = extraer_todas_tablas(conn, tablas)
    conn.close()
    # Combinar los datos extraidos en un solo dataframe
    df_combinado = combinar_datos(dataframes)
    # Actualizar el contenido segun la pestaña seleccionada
    if tab == "all":
        return html.Div([
            dash_table.DataTable(
                id="table-all-games",
                columns=[{"name": "Nombre", "id": "Nombre"}],
                data=df_combinado[["Nombre"]].to_dict("records")
            )
        ])
    elif tab == "top_rated":
        return html.Div([
            dash_table.DataTable(
                id="table-top-rated-games",
                columns=[{"name": "Nombre", "id": "Nombre"}, {"name": "Meta Score", "id": "Meta Score"},
                         {"name": "User Score", "id": "User Score"}],
                data=df_combinado[["Nombre", "Meta Score", "User Score"]].to_dict("records")
            )
        ])



# Ejecutar la aplicacion
if __name__ == "__main__":
    app.run_server(debug=True)
