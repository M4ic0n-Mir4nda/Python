lista = []
soma_idade = 0
while True:
    idade = int(input())
    if idade >= 0:
        lista.append(idade)
        continue
    else:
        break
for soma in lista:
    soma_idade += soma
    conta = len(lista)
print(f'{soma_idade / conta:.2f}')
