
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


class Cuadrado(Rectangulo):
    def __init__(self,lado):
        super().__init__(base=lado,altura=lado)
        pass

    pass



