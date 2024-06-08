import mysql.connector
user = 'root'
password = ''
host = 'localhost'
database = 'Northwind'

last_name = 'felipe'
first_name = 'restrepo'
birth_date = '1990-01-01'
photo = 'jaes-MR.jpg'
notes = 'colombia gana hoy :3'

try:
    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd="1234",
        database=database
    )

    cursor = conexion.cursor()

    # Ejecutar una consulta de lectura
    cursor.execute("SELECT * FROM employees")

    # Obtener los resultados
    resultados = cursor.fetchall()

    # Imprimir los resultados
    for EmployeeID in resultados:
        print(EmployeeID)

    print("Nuevo empleado insertado correctamente.")

except mysql.connector.Error as error:
    print("Error al insertar el nuevo empleado:", error)

finally:
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()

