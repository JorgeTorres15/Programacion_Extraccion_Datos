# esto es la parte de la conexion y la de la inserciond e los arcjivos csv 

import pandas as pd
import mysql.connector

def conectar(host, user, password, database):
    try:
        conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if conexion.is_connected():
            print("Conexión exitosa")
            return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def cerrar(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")

def normalizar_plataforma(plataforma):
    return plataforma.replace(' ', '').lower()

def obtener_o_insertar_id(cursor, tabla, columna, valor):
    cursor.execute(f"SELECT id FROM {tabla} WHERE {columna} = %s", (valor,))
    result = cursor.fetchone()
    if result is None:
        cursor.execute(f"INSERT INTO {tabla} ({columna}) VALUES (%s)", (valor,))
        return cursor.lastrowid
    else:
        return result[0]

def insertar_registros(ruta_archivo, connection):
    if connection is None:
        return

    cursor = connection.cursor()
    data_juegos = pd.read_csv(ruta_archivo)

    for index, row in data_juegos.iterrows():
        plataforma = normalizar_plataforma(row['Plataforma'])
        desarrollador = row['Desarrollador']
        publicado_por = row['Publicado por']
        genero = row['Genero']

        # Obtener o insertar IDs para cada una de las tablas relacionadas
        plataforma_id = obtener_o_insertar_id(cursor, 'Plataforma', 'Nombre', plataforma)
        desarrollador_id = obtener_o_insertar_id(cursor, 'Desarrollador', 'Nombre', desarrollador)
        publicado_por_id = obtener_o_insertar_id(cursor, 'Publicado_por', 'Nombre', publicado_por)
        genero_id = obtener_o_insertar_id(cursor, 'Genero', 'Nombre', genero)

        # Insertar el registro del videojuego
        cursor.execute("""
            INSERT INTO Videojuegos (Nombre, Fecha_Lanzamiento, Meta_Score, Catalogado_por_Meta, User_Score,
            Catalogado_por_Usuario, Plataforma_id, Desarrollador_id, Publicado_por_id, Genero_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Nombre'], row['Fecha Lanzamiento'], row['Meta Score'], row['Catalogado por Meta'],
            row['User Score'], row['Catalogado por Usuario'], plataforma_id, desarrollador_id, publicado_por_id, genero_id
        ))

    connection.commit()
    print("Los datos se han insertado correctamente en la base de datos.")

if __name__ == '__main__':
    host = "127.0.0.1"
    user = "root"
    password = "12345"
    database = "Metacritics"
    connection = conectar(host, user, password, database)

    archivo = "datasets/datasets_300_registros.csv"

    insertar_registros(archivo, connection)

    cerrar(connection)
