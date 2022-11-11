lista_um = []
lista_dois = []
for i in range(5):
    numero = int(input("Digite um número: "))
    lista_um.append(numero)

for j in range(5):
    numero = int(input("Digite um número: "))
    lista_dois.append(numero)

tupla = tuple(lista_um + lista_dois)
print(tupla)