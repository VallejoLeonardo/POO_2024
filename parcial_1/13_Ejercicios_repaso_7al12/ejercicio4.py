"""
4.- Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones
"""
import os
os.system('cls')
def tipo_variable(variable):
    if isinstance(variable, list):
        print("El tipo de la varianbles es de tipo: lista")
    elif isinstance(variable, str):
        print("El tipo de la varianbles es de tipo: string")
    elif isinstance(variable, int):
        print("El tipo de la varianbles es de tipo: entero")
    elif isinstance(variable, bool):
        print("El tipo de la varianbles es de tipo: booleano")
    else:
        print("El tipo de varible no es reconocido.")


# Define las variables
lista = [1, 2, 3]
print(lista)
string = "Hello, world!"
print(string)
integer = 42
print(integer)
boolean = True
print(boolean)

# Imprime el tipo de cada variable
tipo_variable(lista)
tipo_variable(string)
tipo_variable(integer)
tipo_variable(boolean)