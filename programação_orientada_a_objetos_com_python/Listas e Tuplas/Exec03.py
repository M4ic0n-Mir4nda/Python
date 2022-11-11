lista = []
lista_par = []
lista_impar = []

for i in range(10):
    numero = int(input('Digite um número: '))
    lista.append(numero)

for numero in range(len(lista)):
    if lista[numero] % 2 == 0:
        lista_par.append(lista[numero])
    else:
        lista_impar.append(lista[numero])

print(lista)
print(lista_par)
print(lista_impar)