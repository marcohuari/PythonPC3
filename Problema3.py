
import math

class Circulo:
    def __init__(self,radio):
        self.radio = radio
        pass
    
    def calcular_area_circulo(self):
        PI = math.pi
        area = PI*(math.pow(self.radio,2))
        return area
        pass
    pass


circulo_1 = Circulo(5)
print(circulo_1.calcular_area_circulo())

circulo_2 = Circulo(7)
print(circulo_2.calcular_area_circulo())

    