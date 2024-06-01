def verifica_triangulo(a, b, c):
    # Testando se é triângulo
    if (a + b > c) and (a + c > b) and (b + c > a):
        if (a == b) and (a == c):
            return 'Equilátero'
        elif (a == b) or (a == c) or (b == c):
            return 'Isósceles'
        else:
            return 'Escaleno'
    else:
        return 'Não é um triângulo!'