import mysql.connector

# Conexión a la base de datos
try:
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
    )
except:
    print('Error en la creación de la base de datos')
else:
    micursor=conexion.cursor()
    sql=("CREATE DATABASE bd_python")
    # Ejecutar la sentencia SQL
    micursor.execute(sql)

    if micursor:
        print('Base de datos creada con éxito')
    micursor.execute("SHOW DATABASES")   
    for i in micursor:
        print(i)
