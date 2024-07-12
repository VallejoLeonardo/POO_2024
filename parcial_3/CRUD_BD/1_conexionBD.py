import mysql.connector
import os
os.system("cls")

# Conexión a la base de datos
try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python'
)
except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de excepcion: {type(e).__name__}")
    print('Error en la conexión....VERIFIQUE')
else :
    if conexion.is_connected():
        print('Conexión exitosa')
    else:
        print('Error en la conexión')