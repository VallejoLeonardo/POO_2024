import os

from varias_funciones import *

# def solicitarDatos():
#    global n1,n2
#    n1=int(input("Numero #1: "))
#    n2=int(input("Numero #2: "))
  

# def getCalculadora(num1,num2,operacion):
#     if operacion=="1" or operacion=="+" or operacion=="SUMA":
#         return f"{num1}+{num2}={int(num1)+int(num2)}"
#     elif operacion=="2" or operacion=="-" or operacion=="RESTA":
#         return f"{num1}-{num2}={int(num1)-int(num2)}"  
#     elif operacion=="3" or operacion=="*" or operacion=="MULTIPLICACION":
#         return f"{num1}*{num2}={int(num1)*int(num2)}"        
#     elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
#         return f"{num1}/{num2}={int(num1)/int(num2)}"  
#     else:
#         return "Opción invalida por favor vuelve a intentarlo"        
    

# def esperaTecla():
#    # Muestra un mensaje
#    print("Presiona cualquier tecla para continuar...")

#    # Espera a que el usuario presione una tecla
#    input()


opcion=True
while opcion:
    os.system("cls")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    if opcion!="5":
     n1,n2=solicitarDatos()
     #solicitarDatos()
     print(getCalculadora(n1,n2,opcion))
     esperaTecla()
    else:
      opcion=False
      print("Gracias por utilizar el sistema...")