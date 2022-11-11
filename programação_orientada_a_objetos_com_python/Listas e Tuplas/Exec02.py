lista = []
par = 0
impar = 0
for i in range(5):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        par += 1
    else:
        impar += numero
    lista.append(numero)

print(par)
print(impar)