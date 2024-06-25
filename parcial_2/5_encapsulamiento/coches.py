"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.

Metodo Constructor.- este metodo especial se coloca dentro de la clase y se utiliza para darle un valor a los atributos al momento de crearlos

"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos) llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase

    def _init_(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas 


    ##En python el encapsulamiento tambien se llamllama visibilidad y por lo general define como seran los atributos y metodos, es decir, publicos o privados

    ##Atributo publico
    publico_atributo="Soy un atributo publico"

    ##Atributo privado
    __privado_atributo=("Soy un atributo privado")

    ##Nota 1, para utilizar un atributo privado se tendra que hacer dentro de un metodo que fuera publico el metodo

    def getPrivadoAtributo(self):
        return self.__privado_atributo

    ##Metodo privado 
    def __getMetodoPrivada(self):
        print("Soy un metodo privado")

    ##Nota 2 para utilizar un metodo privado es necesario hacerlo dentro de un metodo publico 

    def getMetodoPublico(self):
        self.__getMetodoPrivado()

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1


    #Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
    #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def getColor(self):
        return self.color

    def setColor(self,color):
        self.color=color 

    def getMarca(self):
        return self.marca

    def setMarca(self,marca):
        self.marca=marca 

    def getModelo(self):
        return self.modelo

    def setModelo(self,modelo):
        self.modelo=modelo        

    def getVelocidad(self):
        return self.velocidad

    def setVelocidad(self,velocidad):
        self.velocidad=velocidad 

    def getCaballaje(self):
        return self.caballaje

    def setCaballaje(self,caballaje):
        self.caballaje=caballaje  

    def getPlazas(self):
        return self.plazas

    def setPlazas(self,plazas):
        self.plazas=plazas

    def getInfo(self):
        print(f"Marca: {self.getMarca()} {self.getColor()}, numeros de plazas: {self.getPlazas()} \nModelo: {self.getModelo()} con una velocidad de {self.getVelocidad()} Km/h y un potencia de {self.getCaballaje()} hp")     

class Camiones(Coches):
    def _init_(self, color, marca, modelo, velocidad, caballaje, plazas, eje, capacidadCarga):
        super()._init_(color, marca, modelo, velocidad, caballaje, plazas)
        self.eje=eje
        self.capacidadCarga=capacidadCarga

    __tipo_carga=""
    def carga(self, tipo_carga):
        self.__tipo_carga=tipo_carga
        return self.__tipo_carga