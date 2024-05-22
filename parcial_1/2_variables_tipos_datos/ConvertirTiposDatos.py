
# Cuando se imprime en pantalla una cadena de caracteres se trabaja
# por default con "CADENAS", ed decir, python no puede concatenar
# otra cosa que no sea un String(str)

texto ="Soy una cadena de valores"
numero =23

#concatenar str con str
print("Soy una cadena de y "+texto)

#concatenar str con int
numero_str = str(numero)
print("El numeoro es:" + numero_str)
print("El numeoro es:" + str(numero))

#concatenar int con str
n1=23
n2=33
suma=n1+n2
print("La suma es: "+str(suma))
print(f"La suma es: {suma}")

#concatenar float e int con str
n1=23.99
n2=33.0
suma=n1+n2
print(f"La suma es: {suma}")