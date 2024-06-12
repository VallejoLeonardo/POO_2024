"""
5.- Crear una lista y un diccionario con el contenido de esta tabla: 

ACCION              TERROR        DEPORTES
MAXIMA VELOCIDAD    LA MONJA       ESPN
ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
RAPIDO Y FURIOSO I  LA MALDICION   ACCION

imprimir la información
"""
import os
os.system('cls')
# Crea una lista con los datos de la tabla
lista_tabla = [
    ["ACCION", "TERROR", "DEPORTES"],
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

# Crea un diccionario con los datos de la tabla
dict_tabla = {
    "ACCION": ["MAXIMA VELOCIDAD", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE"],
}

# imprime la información
print("Lista:", lista_tabla, "\n")
print("Diccionario:", dict_tabla)