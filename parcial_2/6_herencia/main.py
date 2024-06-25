from coches import *
import os
os.system('cls')

#print("Objeto 1")
coche1=Coches('Rojo','Porsche','2020',250,450,2)
coche1.getInfo()

#print("Objeto 2")
coche2=Coches('Negro','Ferrari','2022',320,500,2)
coche2.getInfo()

#print("Objeto 3")
camion1=Camiones('Negro','Dina','2020',180,300,12,8,2500)
camion1.getInfo()

#print("Objeto 4")
camion2=Camiones('Rojo','Dina','2020',180,300,14,6,2500)
camion2.getInfo()

#print("Objeto 5")
camioneta1=Camionetas('Amarillo','Renault','2025',240,250,8,"Delantera",True)
camioneta1.getInfo()

#print("Objeto 6")
camioneta2=Camionetas('Blanca','Nissan','2020',220,300,4,"Tracera",False)
camioneta2.getInfo()



