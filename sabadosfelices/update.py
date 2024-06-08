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

    # Definir la consulta de actualización con múltiples columnas y valores
    consulta = "UPDATE employees SET FirstName = %s, LastName = %s WHERE EmployeeID = %s"

    # Definir los valores para la actualización
    valores = ("Jamecito", "pepe",
               11)  # Por ejemplo, aquí se actualiza el primer nombre, el apellido y el ID del empleado

    # Ejecutar la consulta de actualización
    cursor.execute(consulta, valores)

    # Confirmar la transacción
    conexion.commit()
except mysql.connector.Error as error:
    print("Error al insertar el nuevo empleado:", error)

finally:
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()