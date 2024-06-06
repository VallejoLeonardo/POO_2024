def agregar_pelicula(pelicula, lista_peliculas):
    lista_peliculas.append(pelicula)
    print("Pelicula agregada exitosamente.")

def remover_pelicula(pelicula, lista_peliculas):
    if pelicula in lista_peliculas:
        lista_peliculas.remove(pelicula)
        print("Pelicula removida exitosamente.")
    else:
        print("La pelicula no se encuentra en la lista.")

def consultar_peliculas(lista_peliculas):
    print("Lista de peliculas:")
    for pelicula in lista_peliculas:
        print(pelicula)