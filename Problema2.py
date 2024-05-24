

def main():
    while(True):
        try:
            notas = input('Digite las calificaciones de los alumnos separados por comas (,): ')
            lista = []
            lista = notas.split(',')

            for i, nota in enumerate(lista):
                lista[i] = int(lista[i])
                
        except ValueError:
            print('Dato erroneo, introduce solo números enteros')
        else:
            print('Tipos de datos correctamente convertidos')
            print(lista)
            break
    pass

if __name__ == '__main__':
    main()
