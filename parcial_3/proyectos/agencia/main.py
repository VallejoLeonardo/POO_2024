from revisiones.revision import Revision
from clientes.clientes import Cliente
from autos.autos import Auto
from usuarios.usuario import Usuario
from funciones import *
import os
import getpass

os.system("cls")


def menu_principal():
    while True:
        borrarPantalla()
        print("""
                \n \t 
                    .::  Menú Principal ::. 
                1.- Registrarse
                2.- Iniciar Sesión
                3.- Salir
                """)
        opcion = input("\t\t Elige una opción: ")
        
        if opcion == '1':
            registrarse()
        elif opcion == '2':
            if iniciar_sesion():
                menu_secundario()
        elif opcion == '3':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def registrarse():
    borrarPantalla()
    print(f"\n \t .:: Registrarse ::. ")
    email = input("\tEmail: ")
    nombre = input("\tNombre: ")
    contrasena = getpass.getpass("\tContraseña: ")
    usuario = Usuario(email, nombre, contrasena)
    resultado = usuario.registrarse()
    if resultado:
        print(f"\n \t \t .:: Usuario registrado con éxito ::. ")
    else:
        print(f"\n \t \t ** No fue posible registrar el usuario, por favor intente de nuevo ** ... ")
    esperarTecla()

def iniciar_sesion():
    borrarPantalla()
    print(f"\n \t .:: Iniciar Sesión ::. ")
    email = input("\tEmail: ")
    contrasena = getpass.getpass("\tContraseña: ")
    usuario = Usuario.iniciar_sesion(email, contrasena)
    if usuario:
        print(f"\n \t \t .:: Sesión iniciada con éxito ::. ")
        esperarTecla()
        return True
    else:
        print(f"\n \t \t ** Email o contraseña incorrectos, por favor intente de nuevo ** ... ")
        esperarTecla()
        return False



def menu_secundario():
    while True:
        borrarPantalla()
        print("""
                \n \t 
                    .::  Menú Secundario ::. 
                1.- Gestión de Clientes
                2.- Gestión de Autos
                3.- Gestión de Revisiones
                4.- Cerrar Sesión
                """)
        opcion = input("\t\t Elige una opción: ")
        
        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_autos()
        elif opcion == '3':
            menu_revisiones()
        elif opcion == '4':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_clientes():
    while True:
        borrarPantalla()
        print("""
                    \n \t 
                        .::  Menú Clientes ::. 
                    1.- Insertar Cliente
                    2.- Consultar Clientes
                    3.- Actualizar Cliente
                    4.- Eliminar Cliente
                    5.- Volver al Menú Principal
                    """)
        opcion = input("\t\t Elige una opción: ")
        
        if opcion == '1':
            borrarPantalla()
            print(f"\n \t .:: Insertar Cliente ::. ")
            nif = input("\tNIF: ")
            nombre = input("\tNombre: ")
            direccion = input("\tDirección: ")
            ciudad = input("\tCiudad: ")
            tel = input("\tTeléfono: ")
            obj_cliente = Cliente(nif, nombre, direccion, ciudad, tel)
            resultado = obj_cliente.insertar()
            if resultado:
                print(f"\n \t \t .:: El Cliente se guardó con Éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible guardar el Cliente, por favor verifique ** ... ")
            esperarTecla()

        elif opcion == '2':
            borrarPantalla()
            registros = Cliente.consultar()
            if registros:
                for fila in registros:
                    print(f"\n \t NIF: {fila[0]}")
                    print(f"\t Nombre: {fila[1]}")
                    print(f"\t Dirección: {fila[2]}")
                    print(f"\t Ciudad: {fila[3]}")
                    print(f"\t Teléfono: {fila[4]}")
            else:
                print("\n \t \t ** No hay Clientes registrados ** ... ")
            esperarTecla()
            
        elif opcion == '3':
            borrarPantalla()
            print(f"\n \t .:: Actualizar Cliente ::. ")
            nif = input("\tNIF a actualizar: ")
            nombre = input("\tNombre: ")
            direccion = input("\tDirección: ")
            ciudad = input("\tCiudad: ")
            tel = input("\tTeléfono: ")
            resultado = Cliente.actualizar(nif, nombre, direccion, ciudad, tel)  
            if resultado:
                print(f"\n \t \t .:: El Cliente se actualizó con Éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible actualizar el Cliente, por favor verifique ** ... ")
            esperarTecla()
            
        elif opcion == '4':
            borrarPantalla()
            print(f"\n \t .:: Eliminar Cliente ::. ")
            nif = input("\tNIF a eliminar: ")
            resultado = Cliente.eliminar(nif)
            if resultado:
                print(f"\n \t \t .:: El Cliente se eliminó con Éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible eliminar el Cliente, por favor verifique ** ... ")
            esperarTecla()
            
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_autos():
    while True:
        borrarPantalla()
        print("""
                    \n \t 
                        .::  Menú Autos ::. 
                    1.- Insertar Auto
                    2.- Consultar Autos
                    3.- Actualizar Auto
                    4.- Eliminar Auto
                    5.- Volver al Menú Principal
                    """)
        opcion = input("\t\t Elige una opción: ")
        
        if opcion == '1':
            borrarPantalla()
            print(f"\n \t .:: Insertar Auto ::. ")
            matricula = input("\tMatrícula: ")
            marca = input("\tMarca: ")
            modelo = input("\tModelo: ")
            color = input("\tColor: ")
            nif = input("\tNIF del Cliente: ")
            obj_auto = Auto(matricula, marca, modelo, color, nif)
            resultado = obj_auto.insertar()
            if resultado:
                print(f"\n \t \t .:: El Auto se guardó con Éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible guardar el Auto, por favor verifique ** ... ")
            esperarTecla()

        elif opcion == '2':
            borrarPantalla()
            registros = Auto.consultar()
            if registros:
                for fila in registros:
                    print(f"\n \t Matrícula: {fila[0]}")
                    print(f"\t Marca: {fila[1]}")
                    print(f"\t Modelo: {fila[2]}")
                    print(f"\t Color: {fila[3]}")
                    print(f"\t NIF del Cliente: {fila[4]}")
            else:
                print("\n \t \t ** No hay Autos registrados ** ... ")
            esperarTecla()
            
        elif opcion == '3':
            borrarPantalla()
            print(f"\n \t .:: Actualizar Auto ::. ")
            matricula = input("\tMatrícula a actualizar: ")
            marca = input("\tMarca: ")
            modelo = input("\tModelo: ")
            color = input("\tColor: ")
            nif = input("\tNIF del Cliente: ")
            resultado = Auto.actualizar(matricula, marca, modelo, color, nif)  
            if resultado:
                print(f"\n \t \t .:: El Auto se actualizó con Éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible actualizar el Auto, por favor verifique ** ... ")
            esperarTecla()
            
        elif opcion == '4':
            borrarPantalla()
            print(f"\n \t .:: Eliminar Auto ::. ")
            matricula = input("\tMatrícula a eliminar: ")
            resultado = Auto.eliminar(matricula)
            if resultado:
                print(f"\n \t \t .:: El Auto se eliminó con Éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible eliminar el Auto, por favor verifique ** ... ")
            esperarTecla()
            
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_revisiones():
    while True:
        borrarPantalla()
        print("""
                    \n \t 
                        .::  Menu Revisiones ::. 
                    1.- Insertar 
                    2.- Consultar
                    3.- Actualizar
                    4.- Eliminar
                    5.- Volver al Menú Principal 
                    """)
        opcion = input("\t\t Elige una opción: ")
        
        if opcion == '1' or opcion == 'INSERTAR':
            borrarPantalla()
            print(f"\n \t .:: Insertar Revision ::. ")
            no_revision = input("\tNo_Revision: ")
            cambifiltro = input("\tCambifiltroS/N: ")
            cambioaceite = input("\tCambioaceiteS/N: ")
            cambiofrenos = input("\tCambiofrenosS/N: ")
            otros = input("\tOtros: ")
            matricula = input("\tMatricula: ")
            obj_revision = Revision(no_revision, cambifiltro, cambioaceite, cambiofrenos, otros, matricula)
            resultado = obj_revision.insertar()
            if resultado:
                print(f"\n \t \t .:: La Revision se guardó con Éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible guardar la Revision, por favor verifique ** ... ")
            esperarTecla()

        elif opcion == '2' or opcion == 'CONSULTAR':
            borrarPantalla()
            registros = Revision.consultar()
            if len(registros) > 0:
                for fila in registros:
                    print(f"\n \t No_Revision: {fila[0]}")
                    print(f"\t Cambifiltro: {fila[1]}")
                    print(f"\t Cambioaceite: {fila[2]}")
                    print(f"\t Cambiofrenos: {fila[3]}")
                    print(f"\t Otros: {fila[4]}")
                    print(f"\t Matricula: {fila[5]}")
            else:
                print("\n \t \t ** No hay Revisiones registrados ** ... ")
            esperarTecla()
            
        elif opcion == '3' or opcion == 'ACTUALIZAR':
            borrarPantalla()
            print(f"\n \t .:: Actualizar Revision ::. ")
            no_revision = input("\tNo_Revision a actualizar: ")
            cambifiltro = input("\tCambifiltroS/N: ")
            cambioaceite = input("\tCambioaceiteS/N: ")
            cambiofrenos = input("\tCambiofrenosS/N: ")
            otros = input("\tOtros: ")
            matricula = input("\tMatricula: ")
            resultado = Revision.actualizar(no_revision, cambifiltro, cambioaceite, cambiofrenos, otros, matricula)  
            if resultado:
                print(f"\n \t \t .:: La Revision se actualizó con Éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible actualizar la Revision, por favor verifique ** ... ")
            esperarTecla()
            
        elif opcion == '4' or opcion == 'ELIMINAR':
            borrarPantalla()
            print(f"\n \t .:: Eliminar Revision ::. ")
            no_revision = input("\tNo_Revision a eliminar: ")
            resultado = Revision.eliminar(no_revision)
            if resultado:
                print(f"\n \t \t .:: La Revision se eliminó con Éxito ::. ")
            else:
                print(f"\n \t \t  ** No fue posible eliminar la Revision, por favor verifique ** ... ")
            esperarTecla()
            
        elif opcion == '5' or opcion == 'VOLVER':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == '__main__':
    menu_principal()
