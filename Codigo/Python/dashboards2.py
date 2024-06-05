import mysql.connector
import pandas as pd
from Dataframes import combinar_datos, obtener_conexion, extraer_todas_tablas, imprimir_tablas
# Importar bibliotecas necesarias para la visualizacion y creacion de dashboards
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, callback, Input, Output, State
# Importar elementos y funciones necesarios desde el módulo 'DASHBOARDS'
from DASHBOARDS import app, diseño, componentes, update_content

# Definir una función para crear filtros basados en los datos del dataframe
def filtros(df):
    desarrolladores = ["All"] + sorted(df["Desarrollador"].unique().tolist())
    publicadores = ["All"] + sorted(df["Publicado_por"].unique().tolist())
    # Crear tarjeta con dropdowns para filtros de desarrollador y publicador
    tarjeta = dbc.Card([
        html.Div([
            dbc.Label("Desarrollador", style={"color": "white"}),
            dcc.Dropdown(options=desarrolladores, value="All", id="ddlDesarrollador")
        ]),
        html.Div([
            dbc.Label("Publicador", style={"color": "white"}),
            dcc.Dropdown(options=publicadores, value="All", id="ddlPublicador")
        ])
    ], style={"backgroundColor": "green", "padding": "15px"})
    return tarjeta

# se define una funcion para dibujar un grafico de los generos mas comunes
def dibujar_generos(data):
    generos = data["Genero"].value_counts().sort_values(ascending=False).head(10)
    fig = px.scatter(x=generos.index, y=generos.values, size=generos.values, color=generos.index,
                     labels={"x": "Genero", "y": "Cantidad de Juegos"},
                     title="Top 10 Generos mas comunes", height=500)
    fig.update_layout(plot_bgcolor="black", paper_bgcolor="black", font={"color": "white"})
    return fig

# se define una funcion para dibujar un grafico de los generos mas comunes
def dibujar_plataformas(data):
    plataformas = data["Plataforma"].value_counts().sort_values(ascending=False).head(10)
    fig = px.line(x=plataformas.index, y=plataformas.values, markers=True,
                  labels={"x": "Plataforma", "y": "Cantidad de Juegos"},
                  title="Top 10 Plataformas con mas Juegos", height=500)
    fig.update_layout(plot_bgcolor="black", paper_bgcolor="black", font={"color": "white"})
    return fig

# se define el contenido del primer dashboard
def dashboard1(df):
    return html.Div([
        html.H2("Generos y Plataformas", style={"textAlign": "center", "color": "white"}),
        html.P("¿Cual es el genero que mas se repite en los videojuegos y en que plataforma se desarrollan mas?,"
               "Se busca responder que genero son los mas desarrollados en los videojuegos, tambien se puede saber el genero mas repetido por las compañias y las plataformas donde se desarrollan mas juegos", style={"color": "white"}),
        html.Hr(style={"borderColor": "white"}),
        dbc.Row([
            dbc.Col(filtros(df), width=3),
            dbc.Col([
                dbc.Row([
                    dbc.Col(dcc.Graph(figure=dibujar_generos(df), id="figGeneros"), width=6),
                    dbc.Col(dcc.Graph(figure=dibujar_plataformas(df), id="figPlataformas"), width=6)
                ])
            ], width=9)
        ])
    ], style={"backgroundColor": "black", "padding": "20px"})

# se define el callback para actualizar el contenido basado en la pestaña seleccionada
@app.callback(
    Output("graph-tabs-content", "children"),
    [Input("graph-tabs", "value")]
)
def update_graph_tab(tab):
    config = {
        "user": "root",
        "password": "",
        "host": "localhost",
        "database": "Metacritics"
    }
    conn = obtener_conexion(config)
    tablas = ["Plataforma", "Desarrollador", "Publicado_por", "Genero", "Videojuegos"]
    dataframes = extraer_todas_tablas(conn, tablas)
    conn.close()
    df_combinado = combinar_datos(dataframes)

    if tab == "overview":
        return html.Div("Bienvenido al Dashboard de Metacritic, EQUIPO CABRA",
                        style={"color": "white", "textAlign": "center", "fontSize": "24px"})
    elif tab == "publishers":
        return dashboard1(df_combinado)
    elif tab == "genres":
        return html.Div("WIP...", style={"color": "white", "textAlign": "center"})
    elif tab == "platforms":
        return html.Div("WIP...", style={"color": "white", "textAlign": "center"})
    elif tab == "github":
        return html.Div([
        ])
    else:
        return html.Div("WIP...",
                        style={"color": "white", "textAlign": "center"})


# se define el callback para actualizar los grafuicas basados en los filtros seleccionados
@app.callback(
    Output("figGeneros", "figure"),
    Output("figPlataformas", "figure"),
    [Input("ddlDesarrollador", "value"),
     Input("ddlPublicador", "value")]
)
def actualizar_graficas(desarrollador, publicador):
    config = {
        "user": "root",
        "password": "",
        "host": "localhost",
        "database": "Metacritics"
    }
    conn = obtener_conexion(config)
    tablas = ["Plataforma", "Desarrollador", "Publicado_por", "Genero", "Videojuegos"]
    dataframes = extraer_todas_tablas(conn, tablas)
    conn.close()
    df = combinar_datos(dataframes)
    # Filtrar los datos segun el desarrollador y publicador seleccionados
    if desarrollador != "All":
        df = df[df["Desarrollador"] == desarrollador]
    if publicador != "All":
        df = df[df["Publicado_por"] == publicador]

    fig_generos = dibujar_generos(df)
    fig_plataformas = dibujar_plataformas(df)
    return fig_generos, fig_plataformas


def update_content(tab):
    config = {
        "user": "root",
        "password": "",
        "host": "localhost",
        "database": "Metacritics"
    }
    conn = obtener_conexion(config)
    tablas = ["Plataforma", "Desarrollador", "Publicado_por", "Genero", "Videojuegos"]
    dataframes = extraer_todas_tablas(conn, tablas)
    conn.close()
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

if __name__ == "__main__":

    app.run_server(debug=True)

