from conexionBD import *

import os
os.system("cls")

try:
    micursor=conexion.cursor()
    id = input("Ingrese el ID del registro a eliminar: ")
    sql = f"DELETE FROM clientes WHERE id = {id}"
    micursor.execute(sql)
    conexion.commit()
except:
    print('Error en la eliminación del registro')

else:
    print("Registro eliminado con exito")