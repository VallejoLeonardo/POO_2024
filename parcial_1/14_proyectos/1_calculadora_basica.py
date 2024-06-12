import os
import math

from f_calculadora import *


opcion=True
while opcion:
    os.system("cls")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- Potencia \n 6.- Raiz \n 7.- Salir\n")
    opcion=input("\t Elige una opción: ").upper()
    

    if opcion!="7":
      n1,n2=solicitarDatos()
      print(getCalculadora(n1,n2,opcion))
      esperaTecla()
    else:
      opcion=False
      print("Gracias por usar el sistema...")