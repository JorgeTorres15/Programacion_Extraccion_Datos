import mysql.connector
import pandas as pd

def extraer_datos_tabla(conn, nombre_tabla):
    consulta = f"SELECT * FROM {nombre_tabla}"
    cursor = conn.cursor()
    cursor.execute(consulta)
    nombres_columnas = [i[0] for i in cursor.description]
    filas = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(filas, columns=nombres_columnas)
    return df

def integrar_datos_videojuegos(df_videojuegos, df_plataforma, df_desarrollador, df_publicado_por, df_genero):
    df_plataforma = df_plataforma.rename(columns={"Nombre": "nombre_plataforma"})
    df_desarrollador = df_desarrollador.rename(columns={"Nombre": "nombre_desarrollador"})
    df_publicado_por = df_publicado_por.rename(columns={"Nombre": "nombre_publicado_por"})
    df_genero = df_genero.rename(columns={"Nombre": "nombre_genero"})

    df_videojuegos = df_videojuegos.merge(df_plataforma, left_on="Plataforma_ID", right_on="id", how="left", suffixes=("", "_plataforma"))
    df_videojuegos = df_videojuegos.merge(df_desarrollador, left_on="Desarrollador_ID", right_on="id", how="left", suffixes=("", "_desarrollador"))
    df_videojuegos = df_videojuegos.merge(df_publicado_por, left_on="Publicado_por_ID", right_on="id", how="left", suffixes=("", "_publicado_por"))
    df_videojuegos = df_videojuegos.merge(df_genero, left_on="Genero_ID", right_on="id", how="left", suffixes=("", "_genero"))

    df_combinado = df_videojuegos[["Nombre", "Fecha_Lanzamiento", "Meta_Score", "Catalogado_por_Meta", "User_Score", "Catalogado_por_Usuario",
                                     "nombre_plataforma", "nombre_desarrollador", "nombre_publicado_por", "nombre_genero"]]

    df_combinado = df_combinado.rename(columns={
        "Nombre": "Nombre",
        "Fecha_Lanzamiento": "Fecha Lanzamiento",
        "Meta_Score": "Meta Score",
        "Catalogado_por_Meta": "Catalogado por Meta",
        "User_Score": "User Score",
        "Catalogado_por_Usuario": "Catalogado por Usuario",
        "nombre_plataforma": "Plataforma",
        "nombre_desarrollador": "Desarrollador",
        "nombre_publicado_por": "Publicado_por",
        "nombre_genero": "Genero"
    })

    return df_combinado

def obtener_conexion(config):
    return mysql.connector.connect(**config)

def extraer_todas_tablas(conn, tablas):
    dataframes = {}
    for tabla in tablas:
        dataframes[tabla] = extraer_datos_tabla(conn, tabla)
    return dataframes

def imprimir_tablas(dataframes):
    for tabla, df in dataframes.items():
        print(f"\nTabla: {tabla}")
        print(df)

def combinar_datos(dataframes):
    df_plataforma = dataframes["Plataforma"]
    df_desarrollador = dataframes["Desarrollador"]
    df_publicado_por = dataframes["Publicado_por"]
    df_genero = dataframes["Genero"]
    df_videojuegos = dataframes["Videojuegos"]

    df_combinado = integrar_datos_videojuegos(
        df_videojuegos,
        df_plataforma,
        df_desarrollador,
        df_publicado_por,
        df_genero
    )

    return df_combinado

if __name__ == "__main__":
    config = {
        "user": "root",
        "password": "12345",  # Cambia password
        "host": "localhost",
        "database": "Metacritics"
    }

    conn = obtener_conexion(config)

    tablas = ["Plataforma", "Desarrollador", "Publicado_por", "Genero", "Videojuegos"]

    dataframes = extraer_todas_tablas(conn, tablas)
    conn.close()

    imprimir_tablas(dataframes)

    df_combinado = combinar_datos(dataframes)

    print("\nDataFrame combinado:")
    print(df_combinado)
    print(df_combinado.columns)
