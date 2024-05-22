"""
Este ciclo es un interativo
"""
"""
sintaxis
    for(variable) in (elemento) _iterable (rengo,lista,etc.)
        bloque de instrucción
"""

#crear un programa que imprima 5 veces el caracter @
contador=1
for contador in range (1,6):
    print("@")
    
#EJ2.-crear un programa que imprima los numeros del 1 al 5 los sume y al final imprima la suma
suma=0
for numero in range(1,6):
    print(numero)
    suma+=numero
print(f"La suma es: {suma}")

#EJ3.- crear un programa que solicite un numero entero e continuacion imprima la tabla de multiplicar correspondiente
numero=int(input("Ingrese un numero"))
multi=0
for i in range(1,11):
    multi=1*numero
    print(f"({numero}X {i}={multi})")
