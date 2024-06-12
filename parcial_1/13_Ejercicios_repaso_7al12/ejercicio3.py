"""
3.- Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
el contenido de la lista en mayusculas
"""
import os
os.system('cls')
lista = []

if not lista:
    while True:
        palabra = input("Ingrese una palabra o frase (o presione Enter para terminar): ")
        if palabra == "":
            break
        lista.append(palabra)

lista_en_mayusculas = [palabra.upper() for palabra in lista]
print(lista_en_mayusculas)