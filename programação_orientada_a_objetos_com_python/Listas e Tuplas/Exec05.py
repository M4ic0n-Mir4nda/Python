def intercala_numeros(lista1, lista2):
    lista = []
    for i in range(len(lista1)):
        lista.append(lista1[i])
        lista.append(lista2[i])
    return lista

print(intercala_numeros([1, 2, 3], [4, 5, 6]))
