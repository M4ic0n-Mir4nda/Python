import math

def calcular_delta(a, b, c):
    return b * b - 4 * a * c


def calcular_raizes(a, b, c):
    if type(a) != float and type(a) != int:
        raise TypeError() 
    if type(b) != float and type(b) != int:
        raise TypeError() 
    if type(c) != float and type(c) != int:
        raise TypeError()
    delta = calcular_delta(a, b, c)
    if delta == 0:
        raiz = -b / (2 * a)
        return 1, raiz
    else:
        if delta < 0:
            return 0
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            return 2, raiz1, raiz2 