# Esta es una variable global
x = 10

def funcion_ejemplo():
    # Esta es una variable local
    y = 5
    
    # Podemos acceder y modificar la variable global usando la palabra clave 'global'
    global x
    x = x + y
    print("Dentro de la función, x (global) es:", x)
    print("Dentro de la función, y (local) es:", y)

# Llamamos a la función
funcion_ejemplo()

# Imprimimos la variable global fuera de la función para ver si cambió
print("Fuera de la función, x (global) es:", x)

# Si intentamos imprimir y fuera de la función, dará un error porque y es una variable local
# print(y)  # Esto daría un error


#VARIABLES LOCALEEES
def calcular_area_rectangulo(base, altura):
    # Estas son variables locales
    area = base * altura
    mensaje = f"El área del rectángulo es {area} unidades cuadradas."
    return mensaje

def calcular_perimetro_rectangulo(base, altura):
    # Estas son variables locales
    perimetro = 2 * (base + altura)
    mensaje = f"El perímetro del rectángulo es {perimetro} unidades."
    return mensaje

# Definimos las dimensiones del rectángulo
base = 5
altura = 10

# Llamamos a las funciones y mostramos los resultados
resultado_area = calcular_area_rectangulo(base, altura)
resultado_perimetro = calcular_perimetro_rectangulo(base, altura)

print(resultado_area)
print(resultado_perimetro)