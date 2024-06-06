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





