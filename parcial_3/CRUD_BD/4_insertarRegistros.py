from conexionBD import *

try:
    micursor=conexion.cursor()
    nombre=input('Ingrese el nombre del cliente: ')
    direccion=input('Ingrese la dirección del cliente: ')
    tel=input('Ingrese el teléfono del cliente: ')
    sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, '"+nombre+"', '"+direccion+"','"+tel+"');"
    # sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Leonardo Vallejo', '5 de Febrero','6182563698');"
    micursor.execute(sql)
    conexion.commit()
except:
    print('Error en la inserción del registro')
else:
    print('Registro insertado con éxito')

