import mysql.connector
import pandas as pd
import datetime
from Extracción_SQL_Metacritics import combinar_datos, obtener_conexion, extraer_todas_tablas, imprimir_tablas
# Importar bibliotecas necesarias para la visualizacion y creacion de dashboards
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table, callback, Input, Output, State
# Importar elementos y funciones necesarios desde el módulo 'DASHBOARDS'
from Dashboards_Metacritics import app, diseño, componentes, update_content

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

# definir una funcion para dibujar una grafica de lanzamientos por año
def dibujar_lanzamientos_por_año(data):
    lanzamientos_por_año = data.groupby(pd.to_datetime(data['Fecha Lanzamiento']).dt.year).size().reset_index()
    lanzamientos_por_año.columns = ['Año', 'Lanzamientos']

    fig1 = px.bar(lanzamientos_por_año, x='Año', y='Lanzamientos', title='Lanzamientos por año (barras)')
    fig1.update_layout(plot_bgcolor='black', paper_bgcolor='black', font=dict(color='white'))

    fig2 = px.line(lanzamientos_por_año, x='Año', y='Lanzamientos', title='Lanzamientos por año (línea)')
    fig2.update_layout(plot_bgcolor='black', paper_bgcolor='black', font=dict(color='white'))

    return fig1, fig2
#definir el 2do dashboard
def dashboard2(df):
    fig1, fig2 = dibujar_lanzamientos_por_año(df)
    return html.Div([
        html.H2("Lanzamientos de videojuegos por año", style={"textAlign": "center", "color": "white"}),
        html.P("¿Cuantos lanzamientos de videojuegos hubo por año?,"
               " El análisis del número de lanzamientos de videojuegos por año proporciona información valiosa desde múltiples perspectivas, incluyendo la planificación empresarial, el análisis de mercado, la investigación histórica y el interés general en la industria de los videojuegos.", style={"color": "white"}),
        html.Hr(style={"borderColor": "white"}),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig1), width=6),
            dbc.Col(dcc.Graph(figure=fig2), width=6)
        ])
    ], style={"backgroundColor": "black", "padding": "20px"})

# definir filtros para 2do dashboard
def dashboard2(df):
    fig1, fig2 = dibujar_lanzamientos_por_año(df)
    generos = ["All"] + sorted(df["Genero"].unique().tolist())
    tarjeta_filtros = dbc.Card([
        html.Div([
            dbc.Label("Genero", style={"color": "white"}),
            dcc.Dropdown(options=generos, value="All", id="ddlGenero")
        ])
    ], style={"backgroundColor": "green", "padding": "15px"})
    return html.Div([
        html.H2("Lanzamientos de videojuegos por año", style={"textAlign": "center", "color": "white"}),
        html.P("¿Cuantos lanzamientos de videojuegos hubo por año?,"
               " El análisis del número de lanzamientos de videojuegos por año proporciona información valiosa desde múltiples perspectivas, incluyendo la planificación empresarial, el análisis de mercado, la investigación histórica y el interés general en la industria de los videojuegos.", style={"color": "white"}),
        html.Hr(style={"borderColor": "white"}),
        dbc.Row([
            dbc.Col(tarjeta_filtros, width=3),
            dbc.Col([
                dbc.Row([
                    dbc.Col(dcc.Graph(figure=fig1, id="figLanzamientos1"), width=6),
                    dbc.Col(dcc.Graph(figure=fig2, id="figLanzamientos2"), width=6)
                ])
            ], width=9)
        ])
    ], style={"backgroundColor": "black", "padding": "20px"})

@app.callback(
    Output("figLanzamientos1", "figure"),
    Output("figLanzamientos2", "figure"),
    [Input("ddlGenero", "value")]
)
def actualizar_graficas_lanzamientos(genero):
    config = {
        "user": "root",
        "password": "1803",
        "host": "localhost",
        "database": "Metacritics"
    }
    conn = obtener_conexion(config)
    tablas = ["Plataforma", "Desarrollador", "Publicado_por", "Genero", "Videojuegos"]
    dataframes = extraer_todas_tablas(conn, tablas)
    conn.close()
    df = combinar_datos(dataframes)
# filtrar los datos segun el genero seleccionado
    if genero!= "All":
        df = df[df["Genero"] == genero]

    fig1, fig2 = dibujar_lanzamientos_por_año(df)
    return fig1, fig2

# definir la funcion para calcular el mejor juego por año
def mejor_juego_por_año(df):
    if 'Fecha Lanzamiento' in df.columns and 'Nombre' in df.columns and 'Meta Score' in df.columns:
        mejor_juego_por_año = df.loc[df.groupby('Fecha Lanzamiento')['Meta Score'].idxmax()]
        return mejor_juego_por_año

# definir la funcion para dibujar la grafica del mejor juego por año
def dibujar_mejor_juego_por_año(data):
    if data is not None:
        fig3 = px.bar(data, x='Fecha Lanzamiento', y='Meta Score', text='Nombre', title='Mejor Juego por Año (Según Puntaje de Críticos)')
        fig3.update_traces(texttemplate='%{text}', textposition='outside')
        fig3.update_layout(plot_bgcolor='black', paper_bgcolor='black', font=dict(color='white'))
        return fig3

# definir el contenido del 3er dashboard
def dashboard3(df):
    mejor_juego_data = mejor_juego_por_año(df.loc[df.groupby('Fecha Lanzamiento')['Meta Score'].idxmax()][['Fecha Lanzamiento', 'Nombre', 'Meta Score']])
    fig3 = dibujar_mejor_juego_por_año(mejor_juego_data)
    return html.Div([
        html.H2("Mejor Juego por Año", style={"textAlign": "center", "color": "white"}),
        html.P("¿Cuál fue el mejor juego de cada año según el puntaje de los críticos?"
               "Para responder a esta pregunta, podemos observar la columna 'Genero' en el conjunto de datos y contar el número de juegos en cada género. El género con más juegos se consideraría el género más popular en el conjunto de datos. Basándonos en el conjunto de datos proporcionado, el género más popular de videojuegos es 'Open-World Action' con 10 juegos, seguido de '3D Platformer' con 9 juegos, y 'Action Adventure' con 8 juegos.", style={"color": "white"}),
        html.Hr(style={"borderColor": "white"}),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig3), width=12)
        ])
    ], style={"backgroundColor": "black", "padding": "20px"})

def dashboard3(df):
    mejor_juego_data = mejor_juego_por_año(df.loc[df.groupby('Fecha Lanzamiento')['Meta Score'].idxmax()][['Fecha Lanzamiento', 'Nombre', 'Meta Score']])
    fig3 = dibujar_mejor_juego_por_año(mejor_juego_data)
    fig3.update_layout(plot_bgcolor='black', paper_bgcolor='black', font=dict(color='white'))

    # Create a pie chart of top 10 genres by count
    top_genres = df['Genero'].value_counts().head(10)
    fig4 = px.pie(top_genres, names=top_genres.index, values=top_genres.values, title='Top 10 Generos por Cantidad')
    fig4.update_layout(plot_bgcolor='black', paper_bgcolor='black', font=dict(color='white'))

    return html.Div([
        html.H2("Mejor Juego por Año", style={"textAlign": "center", "color": "white"}),
        html.P("¿Cuál fue el mejor juego de cada año según el puntaje de los críticos?"
               "Para responder a esta pregunta, podemos observar la columna 'Genero' en el conjunto de datos y contar el número de juegos en cada género. El género con más juegos se consideraría el género más popular en el conjunto de datos. Basándonos en el conjunto de datos proporcionado, el género más popular de videojuegos es 'Open-World Action' con 10 juegos, seguido de '3D Platformer' con 9 juegos, y 'Action Adventure' con 8 juegos.", style={"color": "white"}),
        html.Hr(style={"borderColor": "white"}),
        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig3), width=6),
            dbc.Col(dcc.Graph(figure=fig4), width=6)
        ])
    ], style={"backgroundColor": "black", "padding": "20px"})
def dashboard3(df):
    mejor_juego_data = mejor_juego_por_año(df.loc[df.groupby('Fecha Lanzamiento')['Meta Score'].idxmax()][['Fecha Lanzamiento', 'Nombre', 'Meta Score']])
    fig3 = dibujar_mejor_juego_por_año(mejor_juego_data)
    fig3.update_layout(plot_bgcolor='black', paper_bgcolor='black', font=dict(color='white'))

    # Create a pie chart of top 10 genres by count
    top_genres = df['Genero'].value_counts().head(10)
    fig4 = px.pie(top_genres, names=top_genres.index, values=top_genres.values, title='Top 10 Generos por Cantidad')
    fig4.update_layout(plot_bgcolor='black', paper_bgcolor='black', font=dict(color='white'))

    # Crear una lista de fechas únicas en el DataFrame
    fechas = sorted(df['Fecha Lanzamiento'].unique().tolist())

    # Crear tarjeta con dropdown para filtro de fecha
    tarjeta_filtros = dbc.Card([
        html.Div([
            dbc.Label("Fecha de Lanzamiento", style={"color": "white"}),
            dcc.Dropdown(options=[{"label": str(fecha), "value": fecha} for fecha in fechas], value=fechas[-1], id="ddlFecha")
        ])
    ], style={"backgroundColor": "green", "padding": "15px"})

    return html.Div([
        html.H2("Mejor Juego por Fecha", style={"textAlign": "center", "color": "white"}),
        html.P("¿Cuál fue el mejor juego de cada fecha según el puntaje de los críticos?", style={"color": "white"}),
        html.Hr(style={"borderColor": "white"}),
        dbc.Row([
            dbc.Col(tarjeta_filtros, width=3),
            dbc.Col([
                dbc.Row([
                    dbc.Col(dcc.Graph(figure=fig3, id="figMejorJuego"), width=6),
                    dbc.Col(dcc.Graph(figure=fig4, id="figTopGeneros"), width=6)
                ])
            ], width=9)
        ])
    ], style={"backgroundColor": "black", "padding": "20px"})
@app.callback(
    Output("figMejorJuego", "figure"),
    [Input("ddlFecha", "value")]
)
def actualizar_grafica_mejor_juego(fecha):
    config = {
        "user": "root",
        "password": "1803",
        "host": "localhost",
        "database": "Metacritics"
    }
    conn = obtener_conexion(config)
    tablas = ["Plataforma", "Desarrollador", "Publicado_por", "Genero", "Videojuegos"]
    dataframes = extraer_todas_tablas(conn, tablas)
    conn.close()
    df_combinado = combinar_datos(dataframes)

    # Filtrar los datos por la fecha seleccionada
    df_filtrado = df_combinado[df_combinado['Fecha Lanzamiento'] == fecha]

    mejor_juego_data = mejor_juego_por_año(df_filtrado.loc[df_filtrado.groupby('Fecha Lanzamiento')['Meta Score'].idxmax()][['Fecha Lanzamiento', 'Nombre', 'Meta Score']])
    fig3 = dibujar_mejor_juego_por_año(mejor_juego_data)
    fig3.update_layout(plot_bgcolor='black', paper_bgcolor='black', font=dict(color='white'))

    return fig3

def dibujar_ranking_desarrolladores(data):
    # Agrupar los datos por desarrollador y calcular las métricas relevantes
    ranking = data.groupby("Desarrollador")['Meta Score', 'User Score'].agg(['mean', 'count'])
    ranking.columns = ['Meta Score Mean', 'Meta Score Count', 'User Score Mean', 'User Score Count']
    ranking = ranking.sort_values(by=['Meta Score Mean', 'Meta Score Count'], ascending=[False, False])
    ranking = ranking.reset_index()

    # Crear un grafico de barras con el ranking
    fig3 = px.bar(ranking, x="Desarrollador", y=["Meta Score Mean", "Meta Score Count", "User Score Mean", "User Score Count"],
                labels={"x": "Desarrollador", "y": "Métricas"},
                title="Ranking de Desarrolladores", height=500)
    fig3.update_layout(plot_bgcolor="black", paper_bgcolor="black", font={"color": "white"})
    return fig3



# se define el callback para actualizar el contenido basado en la pestaña seleccionada
@app.callback(
    Output("graph-tabs-content", "children"),
    [Input("graph-tabs", "value")]
)
def update_graph_tab(tab):
    config = {
        "user": "root",
        "password": "1803",
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
        return dashboard2(df_combinado)
    elif tab == "platforms":
        return dashboard3(df_combinado)
    elif tab == "github":
        return html.Div([
        ])
    else:
        return html.Div("WIP...",style={"color": "white", "textAlign": "center"})


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
        "password": "1803",
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

    app.run_server(debug=False)

