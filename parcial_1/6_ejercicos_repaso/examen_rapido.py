respuesta = "Si"
contador = 0
suma_calificaciones_finales = 0

while respuesta == "Si":
    nom = input("Ingrese su nombre: ")
    carrera = input("Ingrese su carrera: ")
    cal1 = input("Ingrese la calificación 1: ")
    cal2 = input("Ingrese la calificación 2: ")
    cal3 = input("Ingrese la calificación 3: ")
    cal_PF = input("Ingrese la calificación del proyecto final: ")
    promedio = (float(cal1) + float(cal2) + float(cal3) + float(cal_PF)) / 4

    # a Calcular e imprimir el promedio de los parciales
    print("El promedio de los parciales es:", promedio)

    # b Calcular e imprimir la calificación final 
    calificacion_final = (promedio + float(cal_PF)) / 2
    if calificacion_final < 80 and float(cal_PF) > 50:
        print("Calificación final:", calificacion_final, "- Presenta examen extraordinario")
    else:
        print("Calificación final:", calificacion_final)

    # c Calcular el promedio de la calificación final de los alumnos capturados
    suma_calificaciones_finales += calificacion_final
    contador += 1

    respuesta = input("¿Desea otra captura? (Si/No): ")
    
promedio_calificaciones_finales = suma_calificaciones_finales / contador
print("El promedio de la calificación final de los alumnos capturados es:", promedio_calificaciones_finales)

print("Hola")

