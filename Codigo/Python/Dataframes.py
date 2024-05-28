import mysql.connector
import pandas as pd

def extraer_datos_tabla(nombre_tabla):
    consulta = f"SELECT * FROM {nombre_tabla}"
    cursor = conn.cursor()
    cursor.execute(consulta)
    nombres_columnas = [i[0] for i in cursor.description]
    filas = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(filas, columns=nombres_columnas)
    return df

if __name__ == "__main__":
    config = {
        "user": "root",
        "password": "XXXXX",  # Cambia password
        "host": "localhost",
        "database": "Metacritics"
    }

    conn = mysql.connector.connect(**config)

    tablas = ["Plataforma", "Desarrollador", "Publicado_por", "Genero", "Videojuegos"]

    dataframes = {}

    for tabla in tablas:
        dataframes[tabla] = extraer_datos_tabla(tabla)

    conn.close()

    for tabla, df in dataframes.items():
        print(f"\nTabla: {tabla}")
        print(df)

    df_plataforma = dataframes["Plataforma"]
    df_desarrollador = dataframes["Desarrollador"]
    df_publicado_por = dataframes["Publicado_por"]
    df_genero = dataframes["Genero"]
    df_videojuegos = dataframes["Videojuegos"]
    
