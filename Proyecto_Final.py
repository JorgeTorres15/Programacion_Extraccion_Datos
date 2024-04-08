from mysql.connector import connect,Error


def conexion():
    try:
        conexiondb = connect(host="127.0.0.1",user="root",password="", database="Chinatown")
        return conexiondb
    except Error as e:
        print(e)


def insertar():
    dbConexion = conexion()
    cursor = dbConexion.cursor()
    codigo = "Insert into Clientes (ID_Clientes,Nombre,Apellido) values (%s,%s,%s)"
    ID_Clientes = input("Ingresa el ID de el clientes")
    Nombre_Cliente = input("Ingrese el nombre de el cliente")
    Apellido_Cliente = input("Ingrese el apellido de el cliente")
    parametros = (ID_Clientes,Nombre_Cliente,Apellido_Cliente)



    cursor.execute(codigo,parametros)
    dbConexion.commit()
    print(cursor.rowcount)
    cursor.close()
    dbConexion.close()


def Consultas():
    dbConexion = conexion()
    cursor = dbConexion.cursor()
    codigo = ("Select * from Clientes where Nombre like %s")
    busqueda = input("Dame la condicion de la bisqueda")
    like_busqueda = f"%{busqueda}%"
    parametros = (like_busqueda,)
    cursor.execute(codigo,parametros)
    lista_datos = cursor.fetchall()

    for datos in lista_datos:
        print(datos[1],datos[2])



if __name__ == "__main__":
    #insertar()
    #conexion()
    Consultas()
