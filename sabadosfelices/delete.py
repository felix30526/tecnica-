import mysql.connector
user = 'root'
password = ''
host = 'localhost'
database = 'Northwind'

last_name = 'Mosquera'
first_name = 'Jmes'
birth_date = '1990-01-01'
photo = 'jaes-MR.jpg'
notes = 'New employee'

try:
    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd="1234",
        database=database
    )

    cursor = conexion.cursor()

    # Ejecutar una consulta de eliminación
    cursor.execute("DELETE FROM employees WHERE EmployeeID = %s", (11,))

    # Confirmar los cambios
    conexion.commit()

    # Cerrar cursor y conexión
    cursor.close()

    # Imprimir el número de filas afectadas
    print(f"Se eliminó {cursor.rowcount} fila(s).")

except mysql.connector.Error as error:
    print("Error al insertar el nuevo empleado:", error)

finally:
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()