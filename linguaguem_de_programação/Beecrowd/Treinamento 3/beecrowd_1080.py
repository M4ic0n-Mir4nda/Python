lista = []
validador = 0

while True:
    if validador < 100:
        numeros = int(input())
        lista.append(numeros)
        maior_valor = max(lista)
        posicao = lista.index(maior_valor)
        validador += 1
    else:
        break
print(maior_valor)
print(posicao + 1)
