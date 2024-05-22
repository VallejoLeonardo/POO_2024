#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?

x = float(input("Ingrese el valor de X: "))
numero = float(input("Ingrese el número: "))

porcentaje = (x / 100) * numero

print(f"El {x}% de {numero} es: {porcentaje}")