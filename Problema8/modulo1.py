

import random

lista_1 = []

def numeros_aleatorios(lista):

    for i in range(20):
        num_aleatorio = int(random.random()*100)
        lista.append(num_aleatorio)

    return lista
    pass

def mostrar_num_aleatorio(lista):
    print(lista)

def ordenar_lista(lista):
    lista.sort()    
    print(lista)

