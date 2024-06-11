#Los errores de excepciones en un lenguaje de programacion no es otra cosa que los errores en tiempo de ejecucion 
#Cuando se manejan los errores mediante las excepciones en realidad se dice que se evita que se presenten esos errores en el programa
#En tiempo de ejecucion 

#Ejemplo Se presenta un error cuando n o es generada una variable

try:
    nombre=input("Dame el nombre completo de una persona")
    if len(nombre)>0:
        nombre_usuario="El nombre del usuario en el sistema es: "+nombre

        print(nombre_usuario)
except:
    print("No se ha ingresado un nombre")
    
#Ejemplo 2 Cuando se solicita un numero y se ingresa otra cosa
try:
    numero=input("Tecle un numero entero")
    if numero>0:
        print("El numero entero es positivo")   
    else:
        print("El numero entero es negativo")
        
except ValueError:
    print("No es posible convertir una letra a un numero entero {EJEMPLO.-4} ")
    
#Ejemplo 3 Cuando se genra multiples execepciones
try:
    numero=int(input("Dame un numero entero"))
    print("El numero entero es: "+str(numero*numero))
except TypeError:
    print("Es necesario ingresar un numero entero")
except ValueError:
    print("No es posible convertir una letra a un numero entero")
    
else:
    print("El programa se ha ejecutado correctamente") 
