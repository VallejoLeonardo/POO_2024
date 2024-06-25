"""  
Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:
    def getColor(self):
        return self.color
    
    def setColor(self,color):
        self.colr=color
    
    def getMarca(self):
        return self.marca
    
    def setMarca(self,marca):
        self.colr=marca

    def getModelo(self):
        return self.modelo
    
    def setModelo(self,modelo):
        self.colr=modelo

    def getvalocidad(self):
        return self.velocidad
    
    def setvalocidad(self,velocidad):
        self.colr=velocidad
    
    def getPlazas(self):
        return self.plazas
    
    def setPlazas(self,plazas):
        self.colr=plazas

    def getCaballaje(self):
        return self.caballaje
    
    def setCaballaje(self,caballaje):
        self.colr=caballaje

    
    
    """
        Crear los métodos setters y getters, estos métodos son importantes
        y necesarios en todas las clases para que el programador interactue
        con los valores de los atributos a través de estos métodos. Digamos
        que es la manera más adecuada y recomendada para solicitar un valor
        (get) y/o ingresar o cambiar uno (set) a un atributo particular de
        la clase a través de un objeto.
        °En teoria se deberia de crear un método Getter y Setter por cada
        atributo que contenga la clase.
        °Los métodos get siempre regresan valor, es decir el valor de la propiedad
        a través del return
        °Por otro lado el método set siempre recibe parametros para cambiar o
        modificar el valor del atributo o propiedad en cuestión.
    """

    marca="Ferrari"
    color="rojo"
    modelo="2010"
    velocidad=300
    caballaje=500
    plazas=2

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        self.velocidad+=1

    def frenar(self):
        self.velocidad-=1   

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches()

#Mostrar los valores inicales del objeto o instancia de la clase
print(f"Marca: {coche1.marca} {coche1.color}, numeros de plazas: {coche1.plazas} \nModelo: {coche1.modelo} con una velocidad de {coche1.velocidad} Km/h y un potencia de {coche1.caballaje} hp")

#Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")

#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
    coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")

coche2=Coches()
coche2.marca='Porsche'
coche2.color='Amarillo'
coche2.modelo='2024'
coche2.caballaje='550'
coche2.plazas='2'
coche2.velocidad='320'
print(f"Marca: {coche2.marca} {coche2.color}, numeros de plazas: {coche2.plazas} \nModelo: {coche2.modelo} con una velocidad de {coche2.velocidad} Km/h y un potencia de {coche2.caballaje} hp")



