#FORMAS DE CONCANACION EN PYHONT

nombre="Leonardo Vallejo"
especialidad="Area de SW multiplataforma"
carrera="Ingieneria en Gestion Y desarrollo de SW"

#1er forma
print("Mi nombre es:"+ nombre+"estoy en la especialidad de:"+especialidad+ "mi carrera es"+ carrera)

print("\n")

#2da forma
print("Mi nombre es:",nombre,"estoy en la especialidad de:",especialidad,"mi carrera es",carrera)
print("\n")

#3ra forma
print("Mi nombre es %s estoy en la especialidad de %s mi carrera es %s" %(nombre,especialidad,carrera))
print("\n")

#4ta forma
print("Mi nombre es {} estoy en la especialidad de {} mi carrera es {}".format(nombre,especialidad,carrera))
print("\n")

#5ta forma(MAS COMUN EN PYTHON)
print(f"Mi nombre es {nombre} estoy en la especialidad de {especialidad} mi carrera es {carrera}")
print("\n")


