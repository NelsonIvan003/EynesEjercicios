import random
import doctest


def crear_lista_diccionarios():
    # [{'id':1, 'edad': 'aleatorio(1,100)}]
    lst = []
    for i in range(10):
        e = random.randint(1, 100)
        lst.append({'id': i + 1, 'edad': e})
    return lst

