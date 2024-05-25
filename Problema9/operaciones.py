

def sumar(a,b):
    try:
        resultado = a + b
        return print(resultado)
    except TypeError:
        print('Tipo de dato no valido')
    pass

def restar(a,b):
    try:
        resultado = a - b
        return print(resultado)
    except TypeError:
        print('Tipo de dato no valido')
    pass

def multiplicar(a,b):
    try:
        resultado = a * b
        return print(resultado)
    except TypeError:
        print('Tipo de dato no valido')
    pass

def dividir(a,b):
    try:
        resultado = a / b
        return print(resultado)
    except TypeError:
        print('Tipo de dato no valido')
    except ZeroDivisionError:
        print('División entre 0')
    pass

if __name__ == '__main__':
    dividir(5,0)