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

    #  SQL
    insert_query = """INSERT INTO Employees (LastName, FirstName, BirthDate, Photo, Notes)
                      VALUES (%s, %s, %s, %s, %s)"""

    empleado_data = (last_name, first_name, birth_date, photo, notes)

    # Ejecutar la consulta
    cursor.execute(insert_query, empleado_data)

    # Confirmar la transacción
    conexion.commit()

    print("Nuevo empleado insertado correctamente.")

except mysql.connector.Error as error:
    print("Error al insertar el nuevo empleado:", error)

finally:
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()