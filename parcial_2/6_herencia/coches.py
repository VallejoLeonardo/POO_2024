"""  
Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.4

METODO CONTRUCTOR.- Este metodo especial se coloca dentro de la clase y de utiliza para darle un valor a los atributos del objeto al momento de crealo
"""
#Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
    #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

#Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares
import os
os.system('cls')
class Coches:

    #Metodo contructor
    def _init_(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color="rojo"
        self.marca="Ferrari"
        self.modelo="2010"
        self.velocidad=300
        self.caballaje=500
        self.plazas=2

    #Metodos o acciones o funciones que hace el objeto 

    publico_atributo="Soy un atributo publico"
    __privado_atributo="Soy un atributo privado"

    def getPrivadoAtributo(self):
        return self._
    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1

    def getColor(self):
        return self.Color

    def setColor(self,color):
        self.Color=color 

    def getMarca(self):
        return self.Marca

    def setMarca(self,marca):
        self.Marca=marca 

    def getModelo(self):
        return self.Modelo

    def setModelo(self,modelo):
        self.Modelo=modelo        

    def getVelocidad(self):
        return self.Velocidad

    def setVelocidad(self,velocidad):
        self.Velocidad=velocidad 

    def getCaballaje(self):
        return self.Caballaje

    def setCaballaje(self,caballaje):
        self.Caballaje=caballaje  

    def getPlazas(self):
        return self.Plazas

    def setPlazas(self,plazas):
        self.Plazas=plazas

    def getInfo(self):
        print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp")     

class Camiones(Coches):
    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas,eje,capacidadCarga):
        super().__init__(color,marca,modelo,velocidad,caballaje,plazas)
        self.eje=eje
        self.capacidadCarga=capacidadCarga

    __tipo_carga=""
    def cargar(self,tipo_carga):
            self.tipo_carga=tipo_carga
            return self.tipo_carga
        

    def getEje(self):
        return self.__eje

    def setEje(self,eje):
        self.__eje=eje

    def getCapacidadCarga(self):
        return self.__capacidadCarga

    def setCapacidadCarga(self,capacidadCarga):
        self.__capacidadCarga=capacidadCarga

    def getInfo(self):
        print(f"Marca: {self.getMarca()}, color: {self.getColor()}, modelo: {self.getModelo()}, velocidad: {self.getVelocidad()}, caballaje: {self.getCaballaje()}, plazas: {self.getPlazas()}, con {self.getEje()} y una capacidad de {self.getCapacidad()}")

class Camionetas(Coches):
    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas,traccion,cerrada):
        super().__init__(color,marca,modelo,velocidad,caballaje,plazas)
        self.traccion=traccion
        self.cerrada=cerrada

    def transportar(self,num_pasajeros):
            self.__num_pasajeros=num_pasajeros
            return self.__num_pasajeros

    def getTraccion(self):
        return self.__traccion

    def setTraccion(self,traccion):
        self.__traccion=traccion

    def getCerrada(self):
        return self.__cerrada

    def setCerrada(self,cerrada):
        self.__cerrada=cerrada

    def getInfo(self):
        print(f"Marca: {self.getMarca()}, color: {self.getColor()}, modelo: {self.getModelo()}, velocidad: {self.getVelocidad()}, caballaje: {self.getCaballaje()}, plazas: {self.getPlazas()}, una traccion de {self.getTraccion()}, y es cerrada {self.getCerrada()}")
#Fin definir clases 

