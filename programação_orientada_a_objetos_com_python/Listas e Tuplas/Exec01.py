lista = []
for i in range(10):
    numero = int(input('Digite um número: '))
    lista.append(numero)

print(max(lista))
print(min(lista))
print(sum(lista) / len(lista))