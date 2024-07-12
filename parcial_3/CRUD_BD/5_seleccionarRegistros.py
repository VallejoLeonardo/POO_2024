from conexionBD import *

import os
os.system("cls")
try:
    micursor=conexion.cursor()
    sql="SELECT * FROM clientes"
    micursor.execute(sql)
    resultado=micursor.fetchall()
except:
    print('Error en la selección de los registros')


else:
    for i in resultado:
        print(i)
