# Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

inicio = int(input("Teclee el numero inicial: "))
fin = int(input("Teclee el numero final: "))

for num in range(inicio+1, fin + 1):
    print(num)