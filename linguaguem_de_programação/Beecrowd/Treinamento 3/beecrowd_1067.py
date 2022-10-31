"""
Feito com Lucas Villar;
n = int(input())
lista = []
if n >= 1 and n <= 1000:
    if n % 2 == 0:
        for impar in range(n - 1, 0, -2):
            lista.append(impar)
            lista.sort(reverse=False)
    else:
        for impar in range(n, 0, -2):
            lista.append(impar)
            lista.sort(reverse=False)
for list in lista:
    print(list)
"""

n = int(input())
lista = []

if n >= 1 and n <= 1000:
    while n >= 1:
        lista.append(n)
        lista.sort(reverse=False)
        if n % 2 == 0:
            n = n - 1
        else:
            n = n - 2
for list in lista:
    print(list)








