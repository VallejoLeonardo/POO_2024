#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

# Pedir al usuario los dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Verificar que el primer número sea menor que el segundo número
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

# Mostrar los números impares entre los dos números ingresados
print("Números impares entre", numero1, "y", numero2, ":")

for num in range(numero1, numero2 + 1):
    if num % 2 != 0:
        print(num)