"""
list(array)
son colecciones o conjusnto de datos/valores bajo
un unico nombre, para acceder a los valores se hace
con un indice numerico

NOTA: sus valores si son modificables
La lista es una coleccion ordenada y modificable. Permite miembros duplicados.
"""

import os
os.system("cls")
#EJEMPLO 1.-crear una lista con datos numricos e imprimir el contemido
print("\n..::Ejemplo1::..\n")
lista=[23,34]
print(lista)
print("=======FOR==============") 
   
#recorre la lista con el for
for i in lista:
    print(i)
print("=======WHILE============")  
  
#recorrer lista con el while
i=0
while i<=len(lista)-1:
    print(lista[i])
    i+=1
print("=======================")  

#Eejenplo 2.-crear un lista de 4 palabras, solicitar una palabra y  buscar la coicidencia
# en a lista e indicar si la contro o no y en que posusion
print("\n..::Ejemplo2::..\n")
palabras=["hola","2024","bye","UTD"]
palabras_buscar=input("Ingresa la palabra a buscar:")
if palabras_buscar in palabras:
    print("La palabra se encuentra en la lista.")
    posicion = palabras.index(palabras_buscar)
    print("La palabra se encuentra en la posición:", posicion)
else:
    print("La palabra no se encuentra en la lista.")
    
#Ejemplo 4.- Crear una lista multidimensional (matriz) para almacenar los contactos telefonicos

agenda=[
   ["Carlos",6182334567],
   ["Karin",6182334568],
   ["Leon",6182334569],
   ["Pedro",6182334569],
]

print(agenda)

for i in agenda:
   print(f"{agenda.index(i)+1}.- {i}")


#Ejemplo 5.- Crear un programa qye permita gestionar(administrar) peliculas colocar un menu de opciones para agregar, remover, consultar peliculas
# Ejemplo 5.- Crear un programa que permita gestionar (administrar) peliculas colocar un menu de opciones para agregar, remover, consultar peliculas.

#NOTAS:
#1.- Utilizar funciones y mandar llamar desde otro archivo
#2.- Utilizar listas para alamacenar los nombres de peliculas

from funciones_ej5 import agregar_pelicula, remover_pelicula, consultar_peliculas

# Ejemplo de uso
peliculas = []
while True:
    print("\nMENU DE OPCIONES")
    print("1. Agregar pelicula")
    print("2. Remover pelicula")
    print("3. Consultar peliculas")
    print("4. Salir")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        pelicula = input("Ingrese el nombre de la pelicula: ")
        agregar_pelicula(pelicula, peliculas)
    elif opcion == "2":
        pelicula = input("Ingrese el nombre de la pelicula: ")
        remover_pelicula(pelicula, peliculas)
    elif opcion == "3":
        consultar_peliculas(peliculas)
    elif opcion == "4":
        print("Saliendo del programa...")
    else:
        print("Opcion invalida. Por favor ingrese una opcion valida.")


