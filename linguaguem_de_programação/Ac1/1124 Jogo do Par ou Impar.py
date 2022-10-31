numero = int(input())
if numero >= 2:
    if numero % 2 == 0:
        antecessor = numero - 1
    else:
        antecessor = numero - 2
    if numero % 2 == 0:
        sucessor = numero + 2
    else:
        sucessor = numero + 1
print(antecessor, sucessor)
