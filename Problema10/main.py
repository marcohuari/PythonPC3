
from circulo import *
from cuadrilatero import *

MENU = """
1. Calcular el área de un circulo
2. Calcular el área de un rectangulo
3. Calcular el área de un cuadrado
4. Salir.
"""

def main():
    print('Bienvenido')
    
    while(True):
        opc = int(input(MENU))
        if opc == 1:
            r = int(input('Digite el radio del círculo: '))
            c1 = Circulo(r)
            area = c1.calcular_area_circulo()
            print(area)
            pass
        elif opc == 2:
            b = int(input('Digite la base del rectángulo: '))
            h = int(input('Digite la altura del rectángulo: '))
            r1 = Rectangulo(b,h)
            area = r1.calcular_area()
            print(area)
            pass
        elif opc == 3:
            lado = int(input('Digite el lado del cuadrado: '))
            c1 = Cuadrado(lado)
            area = c1.calcular_area()
            print(area)
            pass
        elif opc == 4:
            print('Saliendo del programa.')
            break
        else:
            break
        pass
    pass

if __name__ == '__main__':
    main()

    
    

