import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='futbol'
    )
    cursor = conexion.cursor(buffered=True)
except mysql.connector.Error as err:
    print(f"Ocurrió un error conectando a base de datos por favor verifique: {err}")
