import random
import doctest


def crear_lista_diccionarios():
    #
    # [{'id':1, 'edad': 'aleatorio(1,100)}]
    lst = []
    for i in range(10):
        e = random.randint(1, 100)
        lst.append({'id': i + 1, 'edad': e})
    return lst

def ordena_mayor_a_menor(inputdecrearlistadicc):
    lista_original = inputdecrearlistadicc

    # según el req no especifica sobre la lista_original,
    # quizás se pueda necesitar y el método sort la va a cambiar
    # por lo tanto se deba guardar en alguna variable (local-global), por ahora simplemente no la uso#
    lista_ordenada = lista_original

    lista_ordenada.sort(key=lambda e: e['edad'], reverse=True)

    # como el ejercicio no dice nada sobre edades menores repetidas o edades mayores, printeo los
    # id del primero en la lista y el último en la lista.
    print("El ID de la persona más longeva es:", lista_ordenada[0]['id'])
    print("El ID de la persona más joven es:", lista_ordenada[-1]['id'])

    return lista_ordenada


lista = ordena_mayor_a_menor(crear_lista_diccionarios())
print(lista)


def _test():

    """
    Examino si la lista en verdad se encuentra ordenada comprobando que la edad
    del primer diccionario sea mayor o igual que la del segundo.
    Y también verifico que la edad del último diccionario sea menor o igual que la del penúltimo.
    Es muy improbable que random.randint en el rango del 1 al 100 me cree 10 números iguales, por lo
    tanto podría aventurarme a analizar que la primera edad sea si o si mayor que la última edad guardada
    dentro de la lista ordenada de diccionarios

    >>> lista[0]['edad'] >= lista[1]['edad']
    True
    >>> lista[-1]['edad'] <= lista[-2]['edad']
    True
    >>> lista[0]['edad'] < lista[-1]['edad']
    False

    """
    print(doctest.testmod())


if __name__ == "__main__":
    _test()
