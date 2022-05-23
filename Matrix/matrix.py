import random


def matriz():
    mtx = [[random.randint(1, 5) for j in range(5)] for i in range(5)]
    for f in range(len(mtx)):
        print(mtx[f])

    # Reviso números consecutivos en forma horizontal
    for i in range(5):
        for j in range(2):
            if mtx[i][j] == mtx[i][j+1] and mtx[i][j] == mtx[i][j+2] and mtx[i][j] == mtx[i][j+3]:
                print("inicio fila:", i+1, "columna:", j+1, "| fin fila:", i+1, "columna:", j+4)
                print("#######")

    # Reviso números consecutivos en forma vertical
    for k in range(2):
        for m in range(5):
            if mtx[k][m] == mtx[k+1][m] and mtx[k][m] == mtx[k+2][m] and mtx[k][m] == mtx[k+3][m]:
                print("inicio fila:", k + 1, "columna:", m + 1, "| fin fila:", k + 4, "columna:", m + 1)
                print("#######")


matriz()
