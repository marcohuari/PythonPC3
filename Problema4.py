

class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        pass

    def calcular_area(self):
        area = self.base * self.altura
        return area
        pass
    pass

rectangulo_1 = Rectangulo(5,4)
rectangulo_2 = Rectangulo(3,7)

print(rectangulo_1.calcular_area())
print(rectangulo_2.calcular_area())
