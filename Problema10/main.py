
from Figuras import circulo
from Figuras import cuadrilatero

MENU = """
1. Calcular el área de un circulo
2. Calcular el área de un rectangulo
3. Calcular el área de un cuadrado
4. Salir.
"""




opc = int(input(MENU))

if opc == 1:
    r = int('Digite el radio del círculo: ')
    c1 = Circulo(r)
    area = c1.calcular_area_radio()
    print(area)

    
    

