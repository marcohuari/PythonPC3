
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
