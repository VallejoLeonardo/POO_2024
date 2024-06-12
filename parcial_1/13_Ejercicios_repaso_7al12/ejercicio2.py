"""
2.- Escribir un programa  que añada valores a una lista mientras que su longitud 
sea menor a 120, y luego mostrar la lista: Usar un while y for
"""
import os
os.system('cls')

lista = []
while len(lista) < 120:
    value = input("Teclea un valor: ")
    lista.append(value)
    print("La lista tiene", len(lista), "elementos.")

for item in lista:
    print(item)


    

