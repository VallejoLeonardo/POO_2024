import math

class Figura:
    def calcular_area(self):
        pass
class Rectangulo(Figura):
    def __init__(self, largo: float, ancho: float):
        self._largo = largo
        self._ancho = ancho
    

    def largo(self):
        return self._largo
    
    def largo(self, valor: float):
        self._largo = valor
    

    def ancho(self) -> float:
        return self._ancho
    
    def ancho(self, valor: float):
        self._ancho = valor
    
    def calcular_area(self) -> float:
        return self._largo * self._ancho

class Circulo(Figura):
    def __init__(self, radio: float):
        self._radio = radio
    
    def radio(self) -> float:
        return self._radio
    

    def radio(self, valor: float):
        self._radio = valor
    
    def calcular_area(self) -> float:
        return math.pi * (self._radio ** 2)

class Triangulo(Figura):
    def __init__(self, altura: float, ancho: float):
        self._altura = altura
        self._ancho = ancho
    

    def altura(self) -> float:
        return self._altura
    
    def altura(self, valor: float):
        self._altura = valor
    

    def ancho(self) -> float:
        return self._ancho
    

    def ancho(self, valor: float):
        self._ancho = valor
    
    def calcular_area(self) -> float:
        return 0.5 * self._ancho * self._altura
    
