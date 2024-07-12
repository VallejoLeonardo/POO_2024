from conexionBD import *
import os
os.system("cls")

try:
    micursor=conexion.cursor()
    sql="UPDATE clientes SET nombre='Fulano' WHERE id=7"
    micursor.execute(sql)
    conexion.commit()
except:
    print('Error en la actualización del registro')
else:
    print("Registro actualizado con exito")