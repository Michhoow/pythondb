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
        IdAlumno = input("Ingrese la id del alumno: ")
        NombreCompleto = input("Ingrese el nombre completo: ")
        Genero = input("Ingrese el genero : ")
        CURP = input("Ingrese la matricula: ")
        Fecha_Nac = input("Ingrese la fecha de nacimiento: Año/Mes/Dia: ")
        Direccion = input("Ingrese la direccion (Pais, provincia): ")
        Telefono = input("Ingrese el numero de telefono: ")
        IdGrupo = input("Ingrese la id del grupo: ")

        cursor = conexion.cursor()

        consulta = f"insert into {tabla} (IdAlumno,NombreCompleto,Genero,CURP,Fecha_Nac,Direccion,Telefono,IdGrupo) values(?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(consulta, (IdAlumno,NombreCompleto,Genero,CURP,Fecha_Nac,Direccion,Telefono,IdGrupo))
        conexion.commit()

        print("Datos agregados.")

        cursor.close()
        conexion.close()
    except Exception as e:
        print(f"Error al agregar los datos: {e}")
while True:

    mostrarestudiantes("Alumno")
    clear_console()
    agregarestudiante("Alumno")
    clear_console()