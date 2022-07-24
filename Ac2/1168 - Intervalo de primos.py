inicio = int(input())
fim = int(input())
i = 2
while inicio <= fim:
    if inicio == 1:
        inicio += 1
        if inicio % i == 0:

            continue
        else:
            print(inicio)
            inicio += 1
i += 1