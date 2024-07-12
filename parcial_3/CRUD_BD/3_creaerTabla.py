from conexionBD import*
import os
os.system("cls")

try:
    micursor = conexion.cursor()
    sql="CREATE TABLE clientes3(id int primary key auto_increment, nombre varchar(60), direccion varchar(120), tel varchar(10))"
    micursor.execute(sql)
except:
    print('Error en la creación de la tabla...VERIFIQUE')

else:
    print('Tabla creada con éxito')