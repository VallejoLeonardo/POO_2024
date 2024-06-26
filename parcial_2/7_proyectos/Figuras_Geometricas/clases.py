import math
import os
os.system('cls')

class Figuras:
    def __init__(self,x:int,y:int,visible:bool):
        self.visible=visible
        self.y=y
        self.x=x

    def estaVisible(self)->bool:
        return self.visible
    
    def mostrar(self):
        self.visible=True

    def ocultar(self):
        self.visible=False
    
    def mover(self,x,y):
        self.visible=True
        self.y=y
        self.x=x
    def calcularArea(self):
        pass
    

class Rectangulos(Figuras):
    def __init__(self,x,y,visible,alto,ancho):
        super().__init__(x,y,visible)
        self.alto=alto
        self.ancho=ancho

    def getAlto(self):
        return self.Alto
    def setAlto(self,alto):
        self.alto=alto

    def getAncho(self):
        return self.ancho
    def set(self,ancho):
        self.ancho=ancho

    def calcularArea(self):
        return self.alto * self.ancho
    
    def ocultar(self):
        super().ocultar()

    def mostrar(self):
        super().mostrar()

class Circulos(Figuras):
    def __init__(self,x,y,visible,radio):
        super().__init__(x, y, visible)
        self.radio = radio

    def calcularArea(self):
        return math.pi * (self.radio ** 2)

    def ocultar(self):
        super().ocultar()

    def mostrar(self):
        super().mostrar()


