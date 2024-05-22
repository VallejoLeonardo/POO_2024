"""
El ciclo while es una esrtructura de control que repite o itera la
ejecución de una serie de instrucciones tajtas ncomo las condicion
se cumpla 'True'
"""
"""
While condcicion:
    bloque de instrucciones
"""
#EJ1.-
contador=1
while contador<=5:
    print("@")
    contador+=1
    
#EJ2
contador=1
suma=0
while contador<=5:
    print(contador)
    suma+=contador
    contador+=1
print(f"La suma es: {suma}")

# EJ3.- crear un programa que solicite un numero entero e continuacion imprima la tabla de multiplicar correspondiente
numero=int(input("Ingrese un numero"))
multi=0
i=1
while i<=10:
    multi=i*numero
    print(f"{numero} X {i} = {multi}")
    i+=1
    