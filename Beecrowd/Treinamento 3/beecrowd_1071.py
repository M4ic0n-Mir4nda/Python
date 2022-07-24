n1 = int(input())
n2 = int(input())
num_impares = []
soma_impares = 0

n1 -= 1
if n1 % 2 == 0:
    for impar in range(n1 - 1, n2, -1):
        num_impares.append(impar)
elif n1 % 2 == 1:
    for impar in range(n1, n2, -2):
        num_impares.append(impar)
for number in num_impares:
    soma_impares += number
print(soma_impares)

