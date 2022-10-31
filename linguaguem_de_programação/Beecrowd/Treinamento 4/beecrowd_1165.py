def divisivel(x, y):
    return x % y == 0

def primo(x):
    qtd = 0
    for divisor in range(1, x+1):
        if divisivel(x, divisor):
            qtd += 1
    return qtd == 2

n = int(input())

for i in range(n):
    x = int(input())
    if primo(x):
        print(f'{x} eh primo')
    else:
        print(f'{x} nao eh primo')