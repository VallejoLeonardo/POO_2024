from coches import Coches
#Crear un objetos o instanciar la clase

print("Objeto 1")
coche1=Coches('Amarillo','Porsche','2020',250,450,2)
coche1.getInfo()


print("Objeto 2")
coche2=Coches('Rojo','Ferrari','2022',320,500,2)
coche2.getInfo()

print("Objeto 3")
coche3=Coches("Azul Metalico","Lancer","2024",220,300,5)
coche3.getInfo()
coche3.setColor("Acul Metalico")