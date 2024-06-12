"""
1.- Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
a.- Recorrer la lista y mostrarla
b.- hacer una funcion que recorra la lista de numeros y devuelva un string
c.- ordenarla y mostrarla
d.- mostrar su longitud
e.- buscar algun elemento que el usuario pida por teclado
"""
import os
os.system('cls')
# a) Recorrer la lista y mostrarla
numeros = [100,250,10,89,36,56,1]
for numero in numeros:
    print("a)",numero)

# b) Hacer una función que recorra la lista de números y devuelva un string
def recorrer_lista(lista):
    cadena = ""
    for numero in lista:
        cadena += str(numero) + " "
    return cadena

# c) Ordenar la lista y mostrarla
numeros.sort()
print("c)Lista ordenada",numeros)

# d) Mostrar la longitud de la lista
print("d)La longitud de la lista es:",len(numeros))

# e) Buscar algún elemento que el usuario pida por teclado
elemento = int(input("Ingrese el elemento que desea buscar: "))
if elemento in numeros:
    print("El elemento", elemento, "se encuentra en la lista.")
else:
    print("El elemento", elemento, "no se encuentra en la lista.")


