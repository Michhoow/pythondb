import pyodbc
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Función para establecer la conexión a la base de datos
def conectarbd():
    try:
        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=MICHAEL;"
            "DATABASE=Escuela;"
            "Trusted_Connection=yes;"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Función para mostrar los datos de una tabla
def mostrarestudiantes(tabla):
    try:
        # Conexión a la base de datos

        conexion = conectarbd()
        if not conexion:  # Verifica si la conexión falló
            return "Conexión no disponible."

        cursor = conexion.cursor()  # Crea el cursor para ejecutar SQL
        consulta = f"SELECT * FROM {tabla}"  # Consulta para obtener todos los datos de la tabla
        cursor.execute(consulta)  # Ejecuta la consulta

        filas = cursor.fetchall()  # Recupera todas las filas del resultado
        if filas:
            print(f"Datos de la tabla '{tabla}':")
            for fila in filas:
                # Elimina las comillas simples al formatear
                print(" | ".join(map(str, fila)))
        else:
            print(f"No hay datos en la tabla '{tabla}'.")

        # Cierre del cursor y la conexión
        cursor.close()
        conexion.close()
    except Exception as e:
        print(f"Error al mostrar los datos: {e}")


def agregarestudiante(tabla):

    try:
        conexion = conectarbd()
        if not conexion:
            return "Conexion no disponible."
        print("Ingrese los datos para ingresar")
        print()
        id = input("Ingrese la id: ")
        nombre = input("Ingrese el nombre: ")
        fecha = input("Ingrese la fecha: ")
        carrera = input("Ingrese la carrera: ")
        cursor = conexion.cursor()

        consulta = f"insert into {tabla} (Id,Nombre,FechaNacimiento,Carrera) values(?, ?, ?, ?)"
        cursor.execute(consulta, (id,nombre,fecha,carrera))
        conexion.commit()

        print("Datos agregados.")

        cursor.close()
        conexion.close()
    except Exception as e:
        print(f"Error al agregar los datos: {e}")
while True:

    mostrarestudiantes("Alumno")
    agregarestudiante("Alumno")
    clear_console()