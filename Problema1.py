

def main():
    while(True):
        try: 
            fraccion = input("Digite una fracción en formato (X/Y), donde X sea menor o igual a Y (X<Y): ")

            largo = 0
            for i in fraccion:
                largo += 1

            corte = fraccion.find("/")
            num = int(fraccion[0:corte])
            den = int(fraccion[corte+1:largo])

            if num > den and den != 0:
                continue

            if num/den < 0.01:
                resultado = "E"
            elif num/den > 0.9:
                resultado = "F"
            else:
                resultado = num/den

        except ValueError:
            print('Dato ingreso es incorrecto')
        except ZeroDivisionError:
            print('Error División entre 0')
        else:
            print(resultado)
            break
    pass

#Inicio
if __name__ == '__main__':
    main()

