# es el menu para que le sea mas facil revisar el proyecto pero si por alguna razon no funciona a la hora de usarlo se supone que si cada paso o archivo tiene su Main

import os
import time
from Webscraping_Metacritics import metacritic
from Limpieza_SQL_Metacritics import conectar, insertar_registros, cerrar
from Extracción_SQL_Metacritics import obtener_conexion, extraer_todas_tablas, imprimir_tablas,  combinar_datos
from Dashboards_Metacritics import app
import Graficas_Metacritics




def limpiar_pantalla():
   os.system('cls' if os.name == 'nt' else 'clear')




def mostrar_menu():
   limpiar_pantalla()
   print("=== Menu de Metacritic ===")
   print("1. Iniciar Web Scraping")
   print("2. Insertar datos en MySQL")
   print("3. Extraer y combinar datos de MySQL")
   print("4. Mostrar Dashboard")
   print("5. Salir")
   print("=========================")




def main():
   while True:
       mostrar_menu()
       opcion = input("Seleccione una opcion (1-5): ")


       if opcion == "1":
           print("Iniciando Web Scraping de Metacritic...")
           time.sleep(1)
           metacritic()
           print("Web Scraping completado. Los datos se han guardado en datasets_300_registros.csv")
           input("Presione Enter para continuar...")
       elif opcion == "2":
           print("Insertando datos en MySQL...")
           time.sleep(1)


           # Configuracion de la conexion MySQL
           host = "127.0.0.1"
           user = "root"
           password = ""
           database = "Metacritics"


           # Intentar conectar a la base de datos
           connection = conectar(host, user, password, database)
           if connection:
               archivo = "datasets_300_registros.csv"


               # Verificar si el archivo existe
               if os.path.isfile(archivo):
                   insertar_registros(archivo, connection)
               else:
                   print(f"El archivo {archivo} no existe.")


               # Cerrar la conexion
               cerrar(connection)
           else:
               print("No se pudo establecer la conexion con la base de datos.")


           input("Presione Enter para continuar...")
       elif opcion == "3":
           print("Extrayendo y combinando datos de MySQL...")
           time.sleep(1)


           # Configuracion de la conexion MySQL
           config = {
               "user": "root",
               "password": "",
               "host": "localhost",
               "database": "Metacritics"
           }


           try:
               conn = obtener_conexion(config)
               # Especificar las tablas a extraer
               tablas = ["Plataforma", "Desarrollador", "Publicado_por", "Genero", "Videojuegos"]
               dataframes = extraer_todas_tablas(conn, tablas)


               # Combinar los datos extraidos en un solo dataframe
               imprimir_tablas(dataframes)
               df_combinado = combinar_datos(dataframes)


               print("\nDataFrame combinado:")
               print(df_combinado)


               # Cerrar la conexion
               conn.close()


           except Exception as e:
               print(f"Error al extraer datos: {e}")


           input("Presione Enter para continuar...")
       elif opcion == "4":
           print("Iniciando Dashboard...")
           time.sleep(1)
           app.run_server(debug=False)


       elif opcion == "5":
           print("Saliendo del programa...")
           break
       else:
           print("Opcion no valida. Por favor, intente de nuevo.")
           time.sleep(1)




if __name__ == "__main__":
   main()

